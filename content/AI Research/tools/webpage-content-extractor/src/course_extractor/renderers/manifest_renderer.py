"""Render a deterministic manifest JSON summarising the extraction."""

from __future__ import annotations

import json
from pathlib import Path

from .. import SCHEMA_VERSION
from ..models import BlockType, DocumentIR


def build_manifest(doc: DocumentIR) -> dict:
    images = list(doc.iter_images())
    audios = list(doc.iter_audio())
    block_types: dict[str, int] = {}
    for b in doc.blocks:
        block_types[b.type.value] = block_types.get(b.type.value, 0) + 1

    return {
        "schema_version": SCHEMA_VERSION,
        "source": {
            "title": doc.source.title,
            "course": doc.source.course,
            "lesson_count": doc.source.lesson_count,
            "source_url": doc.source.source_url,
            "source_html": doc.source.source_html,
            "adapter": doc.source.adapter,
        },
        "counts": {
            "blocks": len(doc.blocks),
            "block_types": dict(sorted(block_types.items())),
            "images_found": sum(1 for i in images if i.asset.exists),
            "images_missing": sum(1 for i in images if not i.asset.exists),
            "audio_referenced": len(audios),
            "audio_matched": sum(1 for a in audios if a.asset and a.asset.exists),
            "audio_transcribed": sum(1 for a in audios if a.transcript),
            "warnings": len(doc.warnings),
        },
        "audio": [
            {
                "placeholder_index": a.placeholder_index,
                "duration_seconds": a.duration_seconds,
                "duration_label": a.duration_label,
                "matched_file": (a.asset.output_name if a.asset else None),
                "matched_by": (a.asset.matched_by if a.asset else None),
                "transcribed": bool(a.transcript),
                "transcript_source": a.transcript_source,
            }
            for a in audios
        ],
        "images": [
            {
                "src_ref": i.asset.src_ref,
                "output_name": i.asset.output_name,
                "exists": i.asset.exists,
                "mime": i.asset.mime,
                "sha256": i.asset.sha256,
                "width": i.asset.width,
                "height": i.asset.height,
            }
            for i in images
        ],
        "warnings": [
            {"code": w.code, "message": w.message, "block_index": w.block_index}
            for w in doc.warnings
        ],
    }


def write_manifest(doc: DocumentIR, out_path: Path) -> Path:
    manifest = build_manifest(doc)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return out_path
