"""Adapter for Articulate Rise-style lesson pages.

Recognises ``.blocks-lesson`` with ``[data-ba="lessonEdit.block"]`` children
and parses each block into a typed BlockIR, preserving DOM order.
"""

from __future__ import annotations

from bs4 import BeautifulSoup, Tag

from ..models import (
    AssetKind,
    AudioIR,
    BlockIR,
    BlockType,
    FlashcardIR,
    FlashcardsIR,
    HeadingIR,
    ImageIR,
    RichText,
    SourceMetadata,
    TabIR,
    TabsIR,
)
from ..asset_resolver import resolve_local_asset
from ..parsers.duration import parse_timer_label, parse_valuemax, timer_to_seconds
from ..parsers.rich_text import parse_rich_text
from .base import ParseContext

BLOCK_SELECTOR = '[data-ba="lessonEdit.block"]'


class RiseAdapter:
    name = "rise"

    def confidence(self, soup: BeautifulSoup) -> float:
        has_lesson = soup.select_one(".blocks-lesson") is not None
        has_block = soup.select_one(BLOCK_SELECTOR) is not None
        if has_lesson and has_block:
            return 0.9
        if has_block:
            return 0.6
        return 0.0

    # ------------------------------------------------------------------ #
    def parse(self, soup: BeautifulSoup, ctx: ParseContext):  # noqa: C901
        doc = ctx.document
        doc.source = self._metadata(soup, ctx)

        root = soup.select_one(".blocks-lesson")
        if root is None:
            doc.add_warning("no_root", "No .blocks-lesson root found")
            return doc

        blocks = root.select(f":scope > {BLOCK_SELECTOR}")
        if not blocks:
            blocks = root.select(BLOCK_SELECTOR)

        audio_counter = 0
        last_index = -1
        for pos, block in enumerate(blocks):
            index = _int_attr(block, "data-ba-index", pos)
            if index <= last_index:
                doc.add_warning(
                    "block_index", f"non-increasing data-ba-index at position {pos}", index
                )
            last_index = index
            block_id = block.get("data-block-id")
            bir, is_audio = self._parse_block(block, index, block_id, ctx)
            if is_audio and bir.audio is not None:
                audio_counter += 1
                bir.audio.placeholder_index = audio_counter
            doc.blocks.append(bir)
        return doc

    # ------------------------------------------------------------------ #
    def _metadata(self, soup: BeautifulSoup, ctx: ParseContext) -> SourceMetadata:
        import re
        from ..html_loader import extract_source_url

        def txt(sel: str) -> str | None:
            el = soup.select_one(sel)
            return el.get_text(" ", strip=True).replace("\u200b", "").strip() if el else None

        base_title = (
            txt(".lesson-header__title h1")
            or txt(".lesson-header__title")
            or (soup.title.get_text(strip=True).replace("\u200b", "").strip() if soup.title else None)
            or "Untitled lesson"
        )

        # Detect Unit / Module prefix from folder path, parent dir, or page title
        unit_prefix = ""
        candidates = [ctx.root_dir.name, ctx.html_path.parent.name, ctx.html_path.stem]
        for cand in candidates:
            m = re.match(r"^(Unit\s+\d+|Module\s+\d+)\b", cand, re.IGNORECASE)
            if m:
                unit_prefix = m.group(1).title() + " - "
                break

        if not unit_prefix and soup.title:
            title_txt = soup.title.get_text().replace("\u200b", " ")
            m = re.search(r"\b(Unit\s+\d+|Module\s+\d+)\b", title_txt, re.IGNORECASE)
            if m:
                unit_prefix = m.group(1).title() + " - "

        title = base_title
        if unit_prefix:
            prefix_core = unit_prefix.strip(" -")
            if not re.search(r"\b" + re.escape(prefix_core) + r"\b", base_title, re.IGNORECASE):
                title = f"{unit_prefix}{base_title}"

        course = txt(".coursecard__title") or txt(".course-header__title")
        return SourceMetadata(
            title=title,
            course=course,
            lesson_count=txt(".lesson-header__count"),
            source_url=extract_source_url(ctx.html_path),
            source_html=ctx.html_path.name,
            adapter=self.name,
        )

    # ------------------------------------------------------------------ #
    def _parse_block(
        self, block: Tag, index: int, block_id: str | None, ctx: ParseContext
    ) -> tuple[BlockIR, bool]:
        raw_class = " ".join(_class(block.select_one("[class*='block-']") or block))

        # audio
        if block.select_one(".block-audio, .audio-player"):
            return self._audio_block(block, index, block_id, raw_class), True
        # image
        if block.select_one(".block-image"):
            return self._image_block(block, index, block_id, raw_class, ctx), False
        # flashcards
        if block.select_one(".block-flashcards"):
            return self._flashcards_block(block, index, block_id, raw_class), False
        # tabs
        if block.select_one('[role="tab"]'):
            return self._tabs_block(block, index, block_id, raw_class, ctx), False
        # quote / impact
        if block.select_one(".block-impact"):
            rt = parse_rich_text(block.select_one(".block-impact"))
            return BlockIR(
                index=index, block_id=block_id, type=BlockType.QUOTE, quote=rt,
                raw_class=raw_class,
            ), False
        # heading
        if block.select_one(".block-text--heading"):
            fr = block.select_one(".block-text--heading .fr-view") or block.select_one(
                ".block-text--heading"
            )
            level = _heading_level(fr)
            return BlockIR(
                index=index, block_id=block_id, type=BlockType.HEADING,
                heading=HeadingIR(level=level, text=parse_rich_text(fr)),
                raw_class=raw_class,
            ), False
        # divider
        if block.select_one(".block-divider"):
            return BlockIR(
                index=index, block_id=block_id, type=BlockType.DIVIDER, raw_class=raw_class
            ), False
        # continue / button
        if block.select_one(".continue-btn, .block-continue"):
            btn = block.select_one(".continue-btn, .block-continue")
            return BlockIR(
                index=index, block_id=block_id, type=BlockType.BUTTON,
                button_text=btn.get_text(" ", strip=True) if btn else "Continue",
                raw_class=raw_class,
            ), False
        # generic rich text
        fr = block.select_one(".block-text .fr-view") or block.select_one(".fr-view")
        if fr is not None:
            rt = parse_rich_text(fr)
            if not rt.is_empty():
                return BlockIR(
                    index=index, block_id=block_id, type=BlockType.RICH_TEXT,
                    rich_text=rt, raw_class=raw_class,
                ), False

        # unknown
        bir = BlockIR(
            index=index, block_id=block_id, type=BlockType.UNKNOWN, raw_class=raw_class
        )
        text = block.get_text(" ", strip=True)
        if text:
            bir.rich_text = parse_rich_text(block)
        bir.warnings.append("unclassified block")
        return bir, False

    # ------------------------------------------------------------------ #
    def _audio_block(self, block, index, block_id, raw_class) -> BlockIR:
        player = block.select_one(".audio-player") or block
        seconds = parse_valuemax(player)
        label = parse_timer_label(player)
        if seconds is None:
            seconds = timer_to_seconds(label)
        audio_el = block.select_one("audio[src], audio source[src], source[src]")
        src_ref = audio_el.get("src") if audio_el else None
        audio = AudioIR(
            placeholder_index=0,  # assigned by caller
            duration_seconds=seconds,
            duration_label=label,
            src_ref=src_ref,
        )
        return BlockIR(
            index=index, block_id=block_id, type=BlockType.AUDIO, audio=audio,
            raw_class=raw_class,
        )

    def _image_block(self, block, index, block_id, raw_class, ctx: ParseContext) -> BlockIR:
        img = self._parse_img(block.select_one(".block-image"), ctx)
        return BlockIR(
            index=index, block_id=block_id, type=BlockType.IMAGE, image=img,
            raw_class=raw_class,
        )

    def _parse_img(self, container: Tag | None, ctx: ParseContext) -> ImageIR | None:
        if container is None:
            return None
        img_el = container.select_one("img[src]")
        if img_el is None:
            return None
        asset = resolve_local_asset(
            img_el.get("src", ""), ctx.html_path, ctx.root_dir, AssetKind.IMAGE
        )
        cap_el = container.select_one(".block-image__caption, figcaption")
        caption = parse_rich_text(cap_el) if cap_el else None
        return ImageIR(asset=asset, alt=img_el.get("alt", ""), caption=caption)

    def _flashcards_block(self, block, index, block_id, raw_class) -> BlockIR:
        cards: list[FlashcardIR] = []
        seen = set()
        for card in block.select(".flashcard"):
            # skip slick-cloned duplicates
            if any("slick-cloned" in _class(anc) for anc in card.parents):
                continue
            front = card.select_one(".flashcard-side--front")
            back = card.select_one(".flashcard-side--back")
            front_rt = parse_rich_text(front.select_one(".fr-view") if front else None)
            back_rt = parse_rich_text(back.select_one(".fr-view") if back else None)
            key = (front_rt.plain.strip(), back_rt.plain.strip())
            if key in seen:
                continue
            seen.add(key)
            cards.append(FlashcardIR(front=front_rt, back=back_rt))
        return BlockIR(
            index=index, block_id=block_id, type=BlockType.FLASHCARDS,
            flashcards=FlashcardsIR(cards=cards), raw_class=raw_class,
        )

    def _tabs_block(self, block, index, block_id, raw_class, ctx: ParseContext) -> BlockIR:
        tab_buttons = block.select('[role="tab"]')
        panels = block.select('[role="tabpanel"]')
        panel_by_id = {p.get("id"): p for p in panels if p.get("id")}
        tabs: list[TabIR] = []
        used = set()
        for i, btn in enumerate(tab_buttons):
            title = btn.get_text(" ", strip=True).replace("​", "")
            controls = btn.get("aria-controls")
            panel = panel_by_id.get(controls)
            if panel is None and i < len(panels):
                panel = panels[i]
            if panel is not None:
                used.add(id(panel))
            rt = parse_rich_text(panel.select_one(".fr-view") if panel else None)
            images: list[ImageIR] = []
            if panel is not None:
                for imgc in panel.select(".block-image, .img, figure"):
                    im = self._parse_img(imgc, ctx)
                    if im and im.asset.src_ref:
                        images.append(im)
                # de-dup images by src
                images = _dedup_images(images)
            tabs.append(TabIR(title=title, rich_text=rt, images=images))
        return BlockIR(
            index=index, block_id=block_id, type=BlockType.TABS,
            tabs=TabsIR(tabs=tabs), raw_class=raw_class,
        )


# --------------------------------------------------------------------------- #
def _dedup_images(images: list[ImageIR]) -> list[ImageIR]:
    out: list[ImageIR] = []
    seen = set()
    for im in images:
        key = im.asset.src_ref
        if key in seen:
            continue
        seen.add(key)
        out.append(im)
    return out


def _class(el) -> list[str]:
    if el is None or not hasattr(el, "get"):
        return []
    c = el.get("class")
    return c if isinstance(c, list) else ([c] if c else [])


def _int_attr(el: Tag, attr: str, default: int) -> int:
    try:
        return int(el.get(attr))
    except (TypeError, ValueError):
        return default


def _heading_level(el: Tag | None) -> int:
    if el is None:
        return 2
    for lvl in range(1, 7):
        if el.select_one(f"h{lvl}"):
            return max(2, lvl)
    return 2
