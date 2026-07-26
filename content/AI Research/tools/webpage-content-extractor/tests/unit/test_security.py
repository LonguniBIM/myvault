import io
import zipfile
from pathlib import Path

import pytest

from course_extractor.security import UnsafeArchiveError, is_within, safe_extract_zip


def _make_zip(entries: dict[str, bytes]) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        for name, data in entries.items():
            zf.writestr(name, data)
    return buf.getvalue()


def test_normal_zip_extracts(tmp_path: Path):
    zpath = tmp_path / "ok.zip"
    zpath.write_bytes(_make_zip({"a/b.txt": b"hi"}))
    dest = tmp_path / "out"
    safe_extract_zip(zpath, dest, 1_000_000)
    assert (dest / "a" / "b.txt").read_bytes() == b"hi"


def test_path_traversal_rejected(tmp_path: Path):
    zpath = tmp_path / "evil.zip"
    zpath.write_bytes(_make_zip({"../../evil.txt": b"x"}))
    with pytest.raises(UnsafeArchiveError):
        safe_extract_zip(zpath, tmp_path / "out", 1_000_000)


def test_absolute_path_rejected(tmp_path: Path):
    zpath = tmp_path / "abs.zip"
    zpath.write_bytes(_make_zip({"/etc/passwd": b"x"}))
    with pytest.raises(UnsafeArchiveError):
        safe_extract_zip(zpath, tmp_path / "out", 1_000_000)


def test_oversized_rejected(tmp_path: Path):
    zpath = tmp_path / "big.zip"
    zpath.write_bytes(_make_zip({"big.bin": b"0" * 5000}))
    with pytest.raises(UnsafeArchiveError):
        safe_extract_zip(zpath, tmp_path / "out", 1000)


def test_is_within(tmp_path: Path):
    assert is_within(tmp_path, tmp_path / "a" / "b")
    assert not is_within(tmp_path, tmp_path.parent / "other")
