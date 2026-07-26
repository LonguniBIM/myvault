"""Pydantic intermediate representation (IR).

Every renderer (Markdown, DOCX, manifest) reads from this single source of
truth so the outputs cannot drift apart.
"""

from __future__ import annotations

from enum import Enum
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field

from . import SCHEMA_VERSION


# --------------------------------------------------------------------------- #
# Rich text
# --------------------------------------------------------------------------- #
class Run(BaseModel):
    text: str = ""
    bold: bool = False
    italic: bool = False
    link: Optional[str] = None


class Paragraph(BaseModel):
    runs: list[Run] = Field(default_factory=list)
    # "" = normal paragraph, "bullet" / "number" = list item
    list_type: str = ""
    level: int = 0

    @property
    def text(self) -> str:
        return "".join(r.text for r in self.runs)


class RichText(BaseModel):
    paragraphs: list[Paragraph] = Field(default_factory=list)

    @property
    def plain(self) -> str:
        return "\n".join(p.text for p in self.paragraphs)

    def is_empty(self) -> bool:
        return not self.plain.strip()


# --------------------------------------------------------------------------- #
# Assets
# --------------------------------------------------------------------------- #
class AssetKind(str, Enum):
    IMAGE = "image"
    AUDIO = "audio"


class AssetIR(BaseModel):
    kind: AssetKind
    # href exactly as written in the HTML (unescaped)
    src_ref: Optional[str] = None
    # absolute path on disk, if the file was found
    source_path: Optional[Path] = None
    # filename to use inside the output assets/ folder
    output_name: Optional[str] = None
    exists: bool = False
    mime: Optional[str] = None
    sha256: Optional[str] = None
    bytes: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    # how an audio file was linked to its placeholder
    matched_by: Optional[str] = None


# --------------------------------------------------------------------------- #
# Block payloads
# --------------------------------------------------------------------------- #
class HeadingIR(BaseModel):
    level: int = 2
    text: RichText


class ImageIR(BaseModel):
    asset: AssetIR
    alt: str = ""
    caption: Optional[RichText] = None


class AudioIR(BaseModel):
    placeholder_index: int
    duration_seconds: Optional[float] = None
    duration_label: Optional[str] = None
    src_ref: Optional[str] = None
    asset: Optional[AssetIR] = None  # matched local file, if any
    transcript: Optional[str] = None
    transcript_source: Optional[str] = None  # e.g. "faster-whisper:small.en"


class FlashcardIR(BaseModel):
    front: RichText
    back: RichText


class FlashcardsIR(BaseModel):
    cards: list[FlashcardIR] = Field(default_factory=list)


class TabIR(BaseModel):
    title: str
    rich_text: Optional[RichText] = None
    images: list[ImageIR] = Field(default_factory=list)


class TabsIR(BaseModel):
    tabs: list[TabIR] = Field(default_factory=list)


# --------------------------------------------------------------------------- #
# Block
# --------------------------------------------------------------------------- #
class BlockType(str, Enum):
    HEADING = "heading"
    RICH_TEXT = "rich_text"
    QUOTE = "quote"
    IMAGE = "image"
    AUDIO = "audio"
    FLASHCARDS = "flashcards"
    TABS = "tabs"
    DIVIDER = "divider"
    BUTTON = "button"
    UNKNOWN = "unknown"


class BlockIR(BaseModel):
    index: int
    block_id: Optional[str] = None
    type: BlockType
    heading: Optional[HeadingIR] = None
    rich_text: Optional[RichText] = None
    quote: Optional[RichText] = None
    image: Optional[ImageIR] = None
    audio: Optional[AudioIR] = None
    flashcards: Optional[FlashcardsIR] = None
    tabs: Optional[TabsIR] = None
    button_text: Optional[str] = None
    raw_class: Optional[str] = None
    warnings: list[str] = Field(default_factory=list)


# --------------------------------------------------------------------------- #
# Document
# --------------------------------------------------------------------------- #
class ExtractionWarning(BaseModel):
    code: str
    message: str
    block_index: Optional[int] = None


class SourceMetadata(BaseModel):
    title: str = "Untitled lesson"
    course: Optional[str] = None
    lesson_count: Optional[str] = None
    source_url: Optional[str] = None
    source_html: Optional[str] = None
    adapter: Optional[str] = None


class DocumentIR(BaseModel):
    schema_version: int = SCHEMA_VERSION
    source: SourceMetadata = Field(default_factory=SourceMetadata)
    blocks: list[BlockIR] = Field(default_factory=list)
    warnings: list[ExtractionWarning] = Field(default_factory=list)

    def add_warning(self, code: str, message: str, block_index: int | None = None) -> None:
        self.warnings.append(
            ExtractionWarning(code=code, message=message, block_index=block_index)
        )

    def iter_images(self):
        for b in self.blocks:
            if b.image:
                yield b.image
            if b.tabs:
                for t in b.tabs.tabs:
                    yield from t.images

    def iter_audio(self):
        for b in self.blocks:
            if b.audio:
                yield b.audio
