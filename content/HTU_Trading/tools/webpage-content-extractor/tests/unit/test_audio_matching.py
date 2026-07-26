from pathlib import Path

from course_extractor.audio import LocalAudio, match_audio_by_duration
from course_extractor.models import AudioIR, BlockIR, BlockType, DocumentIR


def _doc_with_audio(durations: list[float]) -> DocumentIR:
    doc = DocumentIR()
    for i, d in enumerate(durations, 1):
        doc.blocks.append(
            BlockIR(
                index=i,
                type=BlockType.AUDIO,
                audio=AudioIR(placeholder_index=i, duration_seconds=d),
            )
        )
    return doc


def _mkfile(tmp: Path, name: str) -> Path:
    p = tmp / name
    p.write_bytes(name.encode())
    return p


def test_greedy_nearest_matching_and_missing(tmp_path: Path):
    # placeholders 33.04, 22.94, 41.15, 33.65, 40.19; only 4 files (no ~22.9)
    doc = _doc_with_audio([33.041995, 22.941315, 41.14576, 33.645714, 40.193741])
    pool = [
        LocalAudio(_mkfile(tmp_path, "a.mp3"), 40.193741),
        LocalAudio(_mkfile(tmp_path, "b.mp3"), 33.041995),
        LocalAudio(_mkfile(tmp_path, "c.mp3"), 41.145760),
        LocalAudio(_mkfile(tmp_path, "d.mp3"), 33.645714),
    ]
    match_audio_by_duration(doc, pool, tolerance=1.0)
    audios = list(doc.iter_audio())
    assert audios[0].asset.source_path.name == "b.mp3"  # 33.04
    assert audios[1].asset is None                      # 22.94 -> missing
    assert audios[2].asset.source_path.name == "c.mp3"  # 41.15
    assert audios[3].asset.source_path.name == "d.mp3"  # 33.65
    assert audios[4].asset.source_path.name == "a.mp3"  # 40.19
    assert any(w.code == "audio_missing" for w in doc.warnings)


def test_each_file_used_once(tmp_path: Path):
    doc = _doc_with_audio([30.0, 30.2])
    pool = [LocalAudio(_mkfile(tmp_path, "only.mp3"), 30.1)]
    match_audio_by_duration(doc, pool, tolerance=1.0)
    matched = [a for a in doc.iter_audio() if a.asset]
    assert len(matched) == 1
