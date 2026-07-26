"""Runtime configuration resolved from CLI flags and environment."""

from __future__ import annotations

import os
import shutil
from dataclasses import dataclass, field
from pathlib import Path

# Windows default install locations for LibreOffice.
_SOFFICE_DEFAULTS = [
    r"C:\Program Files\LibreOffice\program\soffice.exe",
    r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
]


def _first_existing(paths: list[str]) -> str | None:
    for p in paths:
        if p and Path(p).exists():
            return p
    return None


def find_soffice(explicit: str | None = None) -> str | None:
    """SOFFICE_PATH env / explicit -> PATH -> default Windows locations."""
    for cand in (explicit, os.environ.get("SOFFICE_PATH")):
        if cand and Path(cand).exists():
            return cand
    on_path = shutil.which("soffice") or shutil.which("soffice.exe")
    if on_path:
        return on_path
    return _first_existing(_SOFFICE_DEFAULTS)


def find_ffprobe(explicit: str | None = None) -> str | None:
    for cand in (explicit, os.environ.get("FFPROBE_PATH")):
        if cand and Path(cand).exists():
            return cand
    return shutil.which("ffprobe") or shutil.which("ffprobe.exe")


@dataclass
class Config:
    mode: str = "exact"  # exact | clean
    formats: list[str] = field(default_factory=lambda: ["md", "docx", "json"])
    # transcription
    transcribe: bool = True
    whisper_model: str = "small"
    whisper_language: str | None = "en"
    duration_tolerance: float = 1.0  # seconds
    # external tools
    soffice_path: str | None = None
    ffprobe_path: str | None = None
    render_docx: bool = False
    # limits
    max_unpacked_bytes: int = 512 * 1024 * 1024
    verbose: bool = False

    def resolve_tools(self) -> None:
        self.soffice_path = find_soffice(self.soffice_path)
        self.ffprobe_path = find_ffprobe(self.ffprobe_path)
