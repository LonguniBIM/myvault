"""Shared helpers for detecting "Webpage, Complete" lesson folders.

A lesson folder is a saved page: a directory that contains an ``.htm``/``.html``
file alongside a ``*_files`` assets directory (and usually separate audio files).
These must NOT be scanned by the per-file extractors (extract_content.py /
extract_media.py) — they are handled as a unit by ingest_lesson.py.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


def is_lesson_folder(path: Path) -> bool:
    if not path.is_dir():
        return False
    has_html = any(p.suffix.lower() in (".htm", ".html") for p in path.glob("*"))
    has_files = any(p.is_dir() and p.name.endswith("_files") for p in path.glob("*"))
    return has_html and has_files


def in_lesson_scope(path: Path) -> bool:
    """True if ``path`` is a lesson's saved asset or a file inside a lesson folder."""
    for parent in path.parents:
        if parent.name.endswith("_files"):
            return True
        if is_lesson_folder(parent):
            return True
    return False


def find_lesson_folders(sources_dir: Path) -> list[Path]:
    if not sources_dir.exists():
        return []
    return sorted(p for p in sources_dir.iterdir() if is_lesson_folder(p))


def folder_signature(folder: Path) -> str:
    """Cheap change-detection signature over a folder's files."""
    h = hashlib.sha256()
    for p in sorted(folder.rglob("*")):
        if p.is_file():
            st = p.stat()
            h.update(f"{p.relative_to(folder)}|{st.st_size}|{int(st.st_mtime)}".encode())
    return h.hexdigest()
