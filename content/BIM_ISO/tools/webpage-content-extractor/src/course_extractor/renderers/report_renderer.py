"""Human-readable extraction report."""

from __future__ import annotations

from pathlib import Path

from ..models import BlockType, DocumentIR


def write_report(doc: DocumentIR, out_path: Path) -> Path:
    images = list(doc.iter_images())
    audios = list(doc.iter_audio())
    lines: list[str] = []
    lines.append(f"# Extraction report — {doc.source.title}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Source: `{doc.source.source_html}`")
    lines.append(f"- Adapter: {doc.source.adapter}")
    lines.append(f"- Blocks: {len(doc.blocks)}")
    lines.append(f"- Images found / missing: "
                 f"{sum(1 for i in images if i.asset.exists)} / "
                 f"{sum(1 for i in images if not i.asset.exists)}")
    lines.append(f"- Audio placeholders: {len(audios)}")
    lines.append(f"- Audio matched to local files: {sum(1 for a in audios if a.asset and a.asset.exists)}")
    lines.append(f"- Audio transcribed: {sum(1 for a in audios if a.transcript)}")
    lines.append("")

    lines.append("## Audio placeholders")
    lines.append("")
    lines.append("| # | Duration | Matched file | Matched by | Transcribed |")
    lines.append("|---|---|---|---|---|")
    for a in audios:
        lines.append(
            f"| {a.placeholder_index} | {a.duration_label or a.duration_seconds} | "
            f"{a.asset.output_name if a.asset else '—'} | "
            f"{a.asset.matched_by if a.asset else '—'} | "
            f"{'yes' if a.transcript else 'no'} |"
        )
    lines.append("")

    missing = [i for i in images if not i.asset.exists]
    if missing:
        lines.append("## Missing images")
        lines.append("")
        for i in missing:
            lines.append(f"- `{i.asset.src_ref}`")
        lines.append("")

    unknown = [b for b in doc.blocks if b.type == BlockType.UNKNOWN]
    if unknown:
        lines.append("## Unknown / low-confidence blocks")
        lines.append("")
        for b in unknown:
            lines.append(f"- block index {b.index}: {', '.join(b.warnings) or 'unclassified'}")
        lines.append("")

    if doc.warnings:
        lines.append("## Warnings")
        lines.append("")
        for w in doc.warnings:
            loc = f" (block {w.block_index})" if w.block_index is not None else ""
            lines.append(f"- [{w.code}] {w.message}{loc}")
        lines.append("")

    lines.append("## Capture tips")
    lines.append("")
    lines.append("- If audio placeholders are unmatched, download the lesson audio files "
                 "and drop them into the same source folder; matching is by duration.")
    lines.append("- Expand all tabs / flip all flashcards before *Save Page As → Webpage, "
                 "Complete* so hidden panels are present in the DOM.")
    lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return out_path
