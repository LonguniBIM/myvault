"""Filename / slug helpers that stay safe on Windows."""

from __future__ import annotations

import re
import unicodedata

_WINDOWS_RESERVED = {
    "CON", "PRN", "AUX", "NUL",
    *(f"COM{i}" for i in range(1, 10)),
    *(f"LPT{i}" for i in range(1, 10)),
}

_UNSAFE = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


def slugify(text: str, *, max_len: int = 80) -> str:
    """Readable ASCII slug suitable for a folder / file name."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    text = re.sub(r"-{2,}", "-", text)
    if not text:
        text = "lesson"
    if text.upper() in _WINDOWS_RESERVED:
        text = f"{text}-file"
    return text[:max_len].strip("-")


def sanitize_filename(name: str, *, fallback: str = "file") -> str:
    """Make an arbitrary asset name safe as a Windows filename."""
    name = _UNSAFE.sub("_", name).strip().strip(".")
    if not name:
        name = fallback
    stem = name.rsplit(".", 1)[0]
    if stem.upper() in _WINDOWS_RESERVED:
        name = f"_{name}"
    return name[:120]
