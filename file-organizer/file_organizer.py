"""File Organizer: choose a folder, preview the moves, then apply them.

Run with:  python3 file_organizer.py
"""
import tkinter as tk
from collections import Counter
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

import organizer_core as core

START_TEXT = "Choose a folder to see a preview. Nothing is moved until you click Apply."


class App(ttk.Frame):
    def __init__(self, root):
        super().__init__(root, padding=12)
        self.pack(fill="both", expand=True)
        self.folder = None
        self.plan = []
        self._build()

    def _build(self):
        top = ttk.Frame(self)
        top.pack(fill="x")
        ttk.Button(top, text="1. Choose Folder…", command=self.choose_folder).pack(side="left")
        self.path_label = ttk.Label(top, text="No folder chosen yet", padding=(10, 0))
        self.path_label.pack(side="left")

        self.info = ttk.Label(self, text=START_TEXT, padding=(0, 8))
        self.info.pack(fill="x")

        box = ttk.Frame(self)
        box.pack(fill="both", expand=True)
        self.tree = ttk.Treeview(box, columns=("file", "category", "dest"), show="headings", height=12)
        for col, title, width in (("file", "File", 230), ("category", "Category", 90), ("dest", "Will be moved to", 280)):
            self.tree.heading(col, text=title)
            self.tree.column(col, width=width)
        scroll = ttk.Scrollbar(box, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        buttons = ttk.Frame(self, padding=(0, 8))
        buttons.pack(fill="x")
        self.apply_btn = ttk.Button(buttons, text="2. Apply Organization", command=self.apply, state="disabled")
        self.apply_btn.pack(side="left")
        self.cancel_btn = ttk.Button(buttons, text="Cancel", command=self.cancel, state="disabled")
        self.cancel_btn.pack(side="left", padx=8)

        ttk.Label(self, text="Summary").pack(anchor="w")
        self.summary = tk.Text(self, height=8, wrap="word", state="disabled")
        self.summary.pack(fill="both", expand=True)

    def _set_summary(self, text):
        self.summary.config(state="normal")
        self.summary.delete("1.0", "end")
        self.summary.insert("1.0", text)
        self.summary.config(state="disabled")

    def _show_preview(self):
        self.tree.delete(*self.tree.get_children())
        for m in self.plan:
            dest = str(m.destination.relative_to(self.folder)) + ("  (renamed)" if m.renamed else "")
            self.tree.insert("", "end", values=(m.source.name, m.category, dest))
        state = "normal" if self.plan else "disabled"
        self.apply_btn.config(state=state)
        self.cancel_btn.config(state=state)
        if self.plan:
            counts = Counter(m.category for m in self.plan)
            parts = ", ".join(f"{counts[c]} {c}" for c in core.CATEGORY_NAMES if counts[c])
            self.info.config(text=f"Preview: {len(self.plan)} file(s) would be moved ({parts}). Nothing has changed yet.")
        else:
            self.info.config(text="No files to organize in this folder.")

    def choose_folder(self):
        chosen = filedialog.askdirectory(title="Choose a folder to organize")
        if not chosen:
            return
        self.folder = Path(chosen)
        self.path_label.config(text=str(self.folder))
        self._set_summary("")
        try:
            self.plan = core.build_plan(self.folder)
        except OSError as err:
            self.plan = []
            messagebox.showerror("Cannot preview folder", str(err))
        self._show_preview()

    def cancel(self):
        self.plan = []
        self._show_preview()
        self.info.config(text="Cancelled. No files were changed. Choose a folder to start again.")

    def apply(self):
        if not self.plan:
            return
        if not messagebox.askyesno(
            "Apply organization?",
            f"Move {len(self.plan)} file(s) into category folders inside:\n{self.folder}\n\n"
            "No existing file will be overwritten.",
        ):
            return
        self.apply_btn.config(state="disabled")
        self.cancel_btn.config(state="disabled")
        result = core.apply_plan(self.plan)
        self._set_summary(core.format_summary(result, self.folder))
        self.plan = []
        self.tree.delete(*self.tree.get_children())
        self.info.config(text=f"Finished: {len(result.moved)} moved, {len(result.errors)} error(s). See the summary below.")


def main():
    root = tk.Tk()
    root.title("File Organizer")
    root.geometry("760x620")
    root.minsize(600, 480)
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
