"""Core logic for the File Organizer. No window/GUI code lives here."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

# Edit these lists to change which extensions go into which category.
CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff", ".webp", ".heic", ".svg", ".raw"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".md", ".xls", ".xlsx", ".csv",
                  ".ppt", ".pptx", ".pages", ".numbers", ".key"},
    "Audio": {".mp3", ".wav", ".aac", ".flac", ".m4a", ".ogg", ".aiff"},
    "Video": {".mp4", ".mov", ".avi", ".mkv", ".wmv", ".webm", ".m4v"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".dmg", ".iso"},
}
OTHER = "Other"
CATEGORY_NAMES = [*CATEGORIES, OTHER]
_EXT_TO_CATEGORY = {ext: cat for cat, exts in CATEGORIES.items() for ext in exts}


@dataclass
class Move:
    source: Path
    destination: Path
    category: str
    renamed: bool = False  # True when the name was changed to avoid a clash


@dataclass
class Result:
    moved: list = field(default_factory=list)   # list[Move]
    errors: list = field(default_factory=list)  # list[(Path, message)]


def categorize(path: Path) -> str:
    return _EXT_TO_CATEGORY.get(path.suffix.lower(), OTHER)


def unique_path(dest: Path, taken: set | None = None) -> Path:
    """Return dest, or 'name (1).ext', 'name (2).ext', ... if that name is already in use."""
    taken = taken if taken is not None else set()
    candidate, n = dest, 1
    while os.path.lexists(candidate) or str(candidate).lower() in taken:
        candidate = dest.with_name(f"{dest.stem} ({n}){dest.suffix}")
        n += 1
    return candidate


def build_plan(folder: Path) -> list:
    """Look at the files directly inside `folder` and decide where each would go.

    Nothing is changed on disk. Hidden files, subfolders and symlinks are skipped.
    """
    folder = Path(folder)
    plan, taken = [], set()
    for item in sorted(folder.iterdir(), key=lambda p: p.name.lower()):
        if item.name.startswith(".") or item.is_symlink() or not item.is_file():
            continue
        category = categorize(item)
        category_dir = folder / category
        if category_dir.is_symlink():
            raise OSError(f"Refusing to organize into a symbolic-link folder: {category_dir}")
        wanted = category_dir / item.name
        dest = unique_path(wanted, taken)
        taken.add(str(dest).lower())
        plan.append(Move(item, dest, category, dest != wanted))
    return plan


def move_without_overwrite(source: Path, destination: Path) -> Path:
    """Move a file without replacing a destination created by another process.

    Source and destination are inside the same selected folder, so an atomic
    hard link can reserve the destination name. If linking is unsupported, the
    move fails safely and the source remains untouched.
    """
    candidate = unique_path(destination)
    while True:
        try:
            os.link(source, candidate)
        except FileExistsError:
            # Another process claimed this name after unique_path checked it.
            candidate = unique_path(destination)
            continue

        try:
            source.unlink()
        except OSError:
            # Roll back the new link when the original cannot be removed.
            try:
                candidate.unlink()
            except OSError:
                pass
            raise
        return candidate


def apply_plan(plan: list) -> Result:
    """Move planned files while refusing category symlinks and name clashes."""
    result = Result()
    for move in plan:
        try:
            if move.destination.parent.is_symlink():
                raise OSError(f"Refusing to organize into a symbolic-link folder: {move.destination.parent}")
            move.destination.parent.mkdir(exist_ok=True)
            final = move_without_overwrite(move.source, move.destination)
            result.moved.append(Move(move.source, final, move.category, final.name != move.source.name))
        except OSError as err:
            result.errors.append((move.source, str(err)))
    return result


def format_summary(result: Result, folder: Path) -> str:
    folder = Path(folder)
    lines = [f"Done: {len(result.moved)} moved, {len(result.errors)} error(s).", ""]
    for m in result.moved:
        note = "  (renamed to avoid overwriting)" if m.renamed else ""
        lines.append(f"  {m.source.name}  ->  {m.destination.relative_to(folder)}{note}")
    if result.errors:
        lines += ["", "Errors (these files were left where they were):"]
        lines += [f"  {src.name}: {msg}" for src, msg in result.errors]
    return "\n".join(lines)