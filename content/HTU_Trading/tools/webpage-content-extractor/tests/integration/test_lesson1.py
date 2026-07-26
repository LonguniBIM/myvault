"""Acceptance test against the real Lesson 1 fixture.

Skips automatically when the (copyrighted, un-committed) source folder is not
present. Point at it explicitly with the WCE_LESSON1_DIR env var, otherwise the
default raw/sources location is tried.
"""

import os
from pathlib import Path

import pytest

from course_extractor.config import Config
from course_extractor.pipeline import parse_document

_DEFAULT = Path(
    r"d:/wiki/BIM_ISO/raw/sources/"
    r"Lesson 1 - BIM Defined - BIM ISO 19650 1&2 Project Delivery_ Unit 1 - Catalyst for Change"
)


def _fixture_dir() -> Path | None:
    env = os.environ.get("WCE_LESSON1_DIR")
    for cand in (Path(env) if env else None, _DEFAULT):
        if cand and cand.exists():
            return cand
    return None


@pytest.mark.skipif(_fixture_dir() is None, reason="Lesson 1 fixture not available")
def test_lesson1_structure():
    doc, *_ = parse_document(_fixture_dir(), Config(transcribe=False))
    images = list(doc.iter_images())
    audios = list(doc.iter_audio())
    assert len(doc.blocks) == 26
    assert doc.source.adapter == "rise"
    assert sum(1 for i in images if i.asset.exists) == 9
    assert sum(1 for i in images if not i.asset.exists) == 0
    assert len(audios) == 5
    # audio durations, in DOM order
    labels = [a.duration_label for a in audios]
    assert labels == ["00:33", "00:23", "00:41", "00:34", "00:40"]
