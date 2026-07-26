"""Render DocumentIR -> Markdown, copying referenced assets into assets/.

Designed so the Markdown can be ingested into an Obsidian-style wiki: audio
placeholders are filled with the transcript text; missing media surfaces as a
callout so nothing is silently dropped.
"""

from __future__ import annotations

import shutil
from datetime import date
from pathlib import Path

from ..models import (
    AudioIR,
    BlockIR,
    BlockType,
    DocumentIR,
    ImageIR,
    Paragraph,
    RichText,
)


def _esc(text: str) -> str:
    return text.replace("\\", "\\\\").replace("*", "\\*").replace("_", "\\_").replace("`", "\\`")


def _runs_md(para: Paragraph) -> str:
    parts: list[str] = []
    for run in para.runs:
        t = run.text
        if t == "\n":
            parts.append("  \n")
            continue
        t = _esc(t)
        if run.bold:
            t = f"**{t}**"
        if run.italic:
            t = f"*{t}*"
        if run.link:
            t = f"[{t}]({run.link})"
        parts.append(t)
    return "".join(parts).strip()


def _rich_md(rt: RichText | None, out: list[str]) -> None:
    if rt is None:
        return
    for para in rt.paragraphs:
        text = _runs_md(para)
        if not text:
            continue
        if para.list_type == "bullet":
            out.append(f"{'  ' * para.level}- {text}")
        elif para.list_type == "number":
            out.append(f"{'  ' * para.level}1. {text}")
        else:
            out.append(text)
            out.append("")


class MarkdownRenderer:
    def __init__(self, doc: DocumentIR, out_dir: Path, mode: str = "exact"):
        self.doc = doc
        self.out_dir = out_dir
        self.assets_dir = out_dir / "assets"
        self.mode = mode
        self.copied: dict[str, str] = {}  # sha -> relative path

    def render(self) -> Path:
        self.assets_dir.mkdir(parents=True, exist_ok=True)
        lines: list[str] = []
        lines.extend(self._frontmatter())
        src = self.doc.source
        lines.append(f"# {src.title}")
        lines.append("")
        if src.lesson_count:
            lines.append(f"*{src.lesson_count}*")
            lines.append("")

        for block in self.doc.blocks:
            self._render_block(block, lines)

        lines.append("")
        lines.append("---")
        lines.append(f"*Extracted from `{src.source_html}` via webpage-content-extractor.*")
        md_path = self.out_dir / "index.md"
        md_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        return md_path

    # ------------------------------------------------------------------ #
    def _frontmatter(self) -> list[str]:
        src = self.doc.source
        fm = ["---", f'title: "{src.title}"', "type: source", "tags:", "  - information-management"]
        if src.source_url:
            fm.append(f"source_url: {src.source_url}")
        fm.append(f"created: {date.today().isoformat()}")
        fm.append(f"updated: {date.today().isoformat()}")
        fm.append("---")
        fm.append("")
        return fm

    def _render_block(self, block: BlockIR, out: list[str]) -> None:
        t = block.type
        if t == BlockType.HEADING and block.heading:
            level = "#" * min(6, max(2, block.heading.level))
            out.append(f"{level} {block.heading.text.plain}")
            out.append("")
        elif t == BlockType.QUOTE and block.quote:
            for para in block.quote.paragraphs:
                out.append(f"> {_runs_md(para)}")
            out.append("")
        elif t == BlockType.RICH_TEXT and block.rich_text:
            _rich_md(block.rich_text, out)
        elif t == BlockType.IMAGE and block.image:
            self._render_image(block.image, out)
        elif t == BlockType.AUDIO and block.audio:
            self._render_audio(block.audio, out)
        elif t == BlockType.FLASHCARDS and block.flashcards:
            out.append("### Flashcards")
            out.append("")
            for i, card in enumerate(block.flashcards.cards, 1):
                front = card.front.plain.strip() or f"Card {i}"
                out.append(f"**{front}**")
                out.append("")
                _rich_md(card.back, out)
            out.append("")
        elif t == BlockType.TABS and block.tabs:
            for tab in block.tabs.tabs:
                out.append(f"### {tab.title}")
                out.append("")
                _rich_md(tab.rich_text, out)
                for im in tab.images:
                    self._render_image(im, out)
            out.append("")
        elif t == BlockType.DIVIDER:
            if self.mode == "exact":
                out.append("---")
                out.append("")
        elif t == BlockType.BUTTON and block.button_text:
            out.append(f"**[{block.button_text}]**")
            out.append("")
        elif block.rich_text:
            _rich_md(block.rich_text, out)

    def _render_image(self, image: ImageIR, out: list[str]) -> None:
        asset = image.asset
        if asset.exists and asset.source_path:
            rel = self._copy_asset(asset)
            alt = image.alt or "image"
            out.append(f"![{alt}]({rel})")
        else:
            out.append(f"> [!warning] Missing image\n> Source reference: `{asset.src_ref}`")
        if image.caption and not image.caption.is_empty():
            out.append("")
            out.append(f"*{image.caption.plain}*")
        out.append("")

    def _render_audio(self, audio: AudioIR, out: list[str]) -> None:
        dur = audio.duration_label or (
            f"{audio.duration_seconds:.0f}s" if audio.duration_seconds else "unknown"
        )
        if audio.transcript:
            out.append(f"> [!note] Audio transcript ({dur})")
            for line in audio.transcript.splitlines() or [audio.transcript]:
                out.append(f"> {line}")
            if audio.asset and audio.asset.exists:
                rel = self._copy_asset(audio.asset)
                out.append(f">")
                out.append(f"> Source: [{Path(rel).name}]({rel})")
            out.append("")
        elif audio.asset and audio.asset.exists:
            rel = self._copy_asset(audio.asset)
            out.append(f"> [!note] Audio ({dur}) — [{Path(rel).name}]({rel})")
            out.append("> _(transcription unavailable)_")
            out.append("")
        else:
            out.append(f"> [!warning] Missing audio ({dur})")
            out.append(f"> No local audio file matched this placeholder "
                       f"(referenced `{audio.src_ref}`).")
            out.append("")

    def _copy_asset(self, asset) -> str:
        if asset.sha256 in self.copied:
            return self.copied[asset.sha256]
        name = asset.output_name or asset.source_path.name
        dest = self.assets_dir / name
        counter = 1
        while dest.exists() and asset.sha256 and _sha(dest) != asset.sha256:
            stem, ext = (name.rsplit(".", 1) + [""])[:2]
            dest = self.assets_dir / (f"{stem}-{counter}.{ext}" if ext else f"{stem}-{counter}")
            counter += 1
        if not dest.exists():
            shutil.copy2(asset.source_path, dest)
        rel = f"assets/{dest.name}"
        if asset.sha256:
            self.copied[asset.sha256] = rel
        return rel


def _sha(path: Path) -> str:
    from ..util.hashing import sha256_file

    return sha256_file(path)
