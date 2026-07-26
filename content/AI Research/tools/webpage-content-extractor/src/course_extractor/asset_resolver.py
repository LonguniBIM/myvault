"""Resolve local image/audio references to on-disk files, safely.

Never mutates source bytes. Blocks any path that escapes the extraction
root. Determines image MIME + dimensions via Pillow.
"""

from __future__ import annotations

import html
import mimetypes
from pathlib import Path
from urllib.parse import unquote, urlparse

from PIL import Image

from .models import AssetIR, AssetKind
from .security import is_within
from .util.hashing import sha256_file
from .util.paths import sanitize_filename


def _looks_remote(src: str) -> bool:
    parsed = urlparse(src)
    return parsed.scheme in ("http", "https", "data", "ftp") and bool(parsed.netloc or parsed.scheme == "data")


def resolve_local_asset(
    src: str,
    html_path: Path,
    root_dir: Path,
    kind: AssetKind,
) -> AssetIR:
    """Resolve ``src`` (as written in HTML) to a local file under ``root_dir``."""
    asset = AssetIR(kind=kind, src_ref=src)
    if not src:
        return asset

    decoded = unquote(html.unescape(src))
    if _looks_remote(decoded):
        # remote reference; nothing local to resolve
        asset.output_name = None
        return asset

    # strip any query/fragment and leading ./
    decoded = decoded.split("?", 1)[0].split("#", 1)[0]
    rel = decoded.lstrip("/").replace("\\", "/")

    candidate = (html_path.parent / rel).resolve()
    if not is_within(root_dir, candidate) and not is_within(html_path.parent, candidate):
        asset.exists = False
        return asset

    if candidate.exists() and candidate.is_file():
        _fill_file_info(asset, candidate)
    return asset


def attach_local_file(asset: AssetIR, path: Path) -> None:
    """Bind a concrete on-disk file to an asset (used for duration-matched audio)."""
    _fill_file_info(asset, path)


def _fill_file_info(asset: AssetIR, path: Path) -> None:
    asset.exists = True
    asset.source_path = path
    asset.bytes = path.stat().st_size
    asset.sha256 = sha256_file(path)
    asset.output_name = sanitize_filename(path.name)
    mime, _ = mimetypes.guess_type(str(path))
    asset.mime = mime
    if asset.kind == AssetKind.IMAGE:
        try:
            with Image.open(path) as im:
                asset.width, asset.height = im.size
                if not asset.mime and im.format:
                    asset.mime = Image.MIME.get(im.format)
        except Exception:  # noqa: BLE001 - broken image should not crash pipeline
            pass
