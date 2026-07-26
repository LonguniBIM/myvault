"""Security boundary: safe ZIP extraction and path containment.

Owns Zip Slip prevention, uncompressed-size limits and path-containment
checks (PLAN M1.1).
"""

from __future__ import annotations

import zipfile
from pathlib import Path

from .util.paths import sanitize_filename


class UnsafeArchiveError(Exception):
    """Raised when an archive tries to escape the extraction root."""


def is_within(base: Path, target: Path) -> bool:
    """True if ``target`` resolves to a location inside ``base``."""
    try:
        base_r = base.resolve()
        target_r = target.resolve()
    except OSError:
        return False
    return base_r == target_r or base_r in target_r.parents


def safe_extract_zip(zip_path: Path, destination: Path, max_unpacked_bytes: int) -> Path:
    """Extract ``zip_path`` into ``destination`` rejecting unsafe entries.

    Rejects absolute paths, ``..`` traversal, symlink entries and archives
    whose cumulative uncompressed size exceeds ``max_unpacked_bytes``.
    """
    destination.mkdir(parents=True, exist_ok=True)
    total = 0
    with zipfile.ZipFile(zip_path) as zf:
        for info in zf.infolist():
            name = info.filename
            if name.endswith("/"):
                continue
            # symlink detection (unix mode bits in external_attr)
            mode = (info.external_attr >> 16) & 0xF000
            if mode == 0xA000:
                raise UnsafeArchiveError(f"symlink entry rejected: {name}")
            if Path(name).is_absolute() or name.startswith(("/", "\\")):
                raise UnsafeArchiveError(f"absolute path rejected: {name}")
            parts = [p for p in name.replace("\\", "/").split("/") if p not in ("", ".")]
            if any(p == ".." for p in parts):
                raise UnsafeArchiveError(f"path traversal rejected: {name}")
            safe_parts = [sanitize_filename(p) for p in parts]
            out_path = destination.joinpath(*safe_parts)
            if not is_within(destination, out_path):
                raise UnsafeArchiveError(f"escapes destination: {name}")

            total += info.file_size
            if total > max_unpacked_bytes:
                raise UnsafeArchiveError(
                    f"uncompressed size exceeds limit ({max_unpacked_bytes} bytes)"
                )
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with zf.open(info) as src, out_path.open("wb") as dst:
                while chunk := src.read(1 << 16):
                    dst.write(chunk)
    return destination
