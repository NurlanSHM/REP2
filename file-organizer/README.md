# File Organizer

A small desktop app that sorts the files in a folder into category folders
(Images, Documents, Audio, Video, Archives, Other). It shows you exactly what
will happen first, and never overwrites anything.

## Setup

You need Python 3 with Tkinter (the window toolkit). There is nothing to `pip install`.

1. Open Terminal and check Python: `python3 --version`
2. Check Tkinter works: `python3 -m tkinter` (a small test window should appear; close it).

**macOS notes**
- The installer from [python.org](https://www.python.org/downloads/) includes a modern Tkinter and is the most reliable choice.
- Homebrew Python: run `brew install python-tk`.
- The Python bundled with Apple's Command Line Tools has an old Tk that can show blank or broken windows on recent macOS. If that happens, install Python from python.org.

## Run

```bash
cd file-organizer
python3 file_organizer.py
```

## How to use

1. Click **Choose Folder…** and pick a folder. The app scans it and shows a preview table: each file, its category, and where it will go. **Nothing has been changed yet.**
2. Happy with the plan? Click **Apply Organization** and confirm. Not happy? Click **Cancel** (or answer *No* in the confirmation) and no files are touched.
3. Read the **Summary** box: every file moved, any that were renamed, and any errors.

## Rules the app follows

- **Never overwrites.** If `Images/photo.jpg` already exists, the file becomes `Images/photo (1).jpg`, then `(2)`, and so on. The destination name is reserved atomically, so a file created by another app after the preview is not replaced. If the filesystem does not support this safe move, the file stays in place and the error appears in the summary.
- Category folders that are symbolic links are refused, so organizing cannot redirect files outside the folder you selected.
- Only files **directly inside** the chosen folder are organized. Subfolders and their contents are left alone, and so are hidden files (names starting with `.`).
- If one file can't be moved (for example, a permissions problem), it stays where it was, the error is listed in the summary, and the rest continue.
- There is **no undo**. Try it on a copy of a folder first if you are unsure.

## Categories

| Category  | Extensions |
|-----------|------------|
| Images    | jpg, jpeg, png, gif, bmp, tif, tiff, webp, heic, svg, raw |
| Documents | pdf, doc, docx, txt, rtf, odt, md, xls, xlsx, csv, ppt, pptx, pages, numbers, key |
| Audio     | mp3, wav, aac, flac, m4a, ogg, aiff |
| Video     | mp4, mov, avi, mkv, wmv, webm, m4v |
| Archives  | zip, rar, 7z, tar, gz, bz2, xz, dmg, iso |
| Other     | everything else |

To change them, edit the `CATEGORIES` lists at the top of `organizer_core.py`.

## Files

- `file_organizer.py` – the window and buttons
- `organizer_core.py` – scanning, unique naming, moving, summary (no GUI code)

## Troubleshooting

- `No module named '_tkinter'` – Tkinter is missing; see Setup above.
- Folders like Desktop, Documents or Downloads: macOS may ask permission the first time. Click Allow, then choose the folder again.
