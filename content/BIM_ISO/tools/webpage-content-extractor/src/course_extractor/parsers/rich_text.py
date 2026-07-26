"""Convert a Froala/Rise ``.fr-view`` container into a RichText IR.

Keeps a minimal but faithful inline model: text, bold, italic, link, plus
paragraph / bullet / numbered-list structure and DOM order.
"""

from __future__ import annotations

from bs4 import NavigableString, Tag

from ..models import Paragraph, RichText, Run

_BLOCK_TAGS = {"p", "div", "li", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote"}
_BOLD_TAGS = {"strong", "b"}
_ITALIC_TAGS = {"em", "i"}


def _inline_runs(node: Tag, *, bold: bool, italic: bool, link: str | None) -> list[Run]:
    runs: list[Run] = []
    for child in node.children:
        if isinstance(child, NavigableString):
            text = str(child).replace("​", "")
            if text:
                runs.append(Run(text=text, bold=bold, italic=italic, link=link))
            continue
        if not isinstance(child, Tag):
            continue
        name = child.name.lower()
        if name == "br":
            runs.append(Run(text="\n", bold=bold, italic=italic, link=link))
            continue
        if name in ("script", "style", "svg", "button"):
            continue
        c_bold = bold or name in _BOLD_TAGS
        c_italic = italic or name in _ITALIC_TAGS
        c_link = link
        if name == "a" and child.get("href"):
            c_link = child["href"]
        runs.extend(_inline_runs(child, bold=c_bold, italic=c_italic, link=c_link))
    return runs


def _clean_runs(runs: list[Run]) -> list[Run]:
    merged: list[Run] = []
    for r in runs:
        if not r.text:
            continue
        if (
            merged
            and merged[-1].bold == r.bold
            and merged[-1].italic == r.italic
            and merged[-1].link == r.link
        ):
            merged[-1] = merged[-1].model_copy(update={"text": merged[-1].text + r.text})
        else:
            merged.append(r)
    # trim surrounding whitespace-only newlines
    return merged


def _paragraph_from(node: Tag, list_type: str = "", level: int = 0) -> Paragraph | None:
    runs = _clean_runs(_inline_runs(node, bold=False, italic=False, link=None))
    if not any(r.text.strip() for r in runs):
        return None
    return Paragraph(runs=runs, list_type=list_type, level=level)


def parse_rich_text(container: Tag | None) -> RichText:
    rich = RichText()
    if container is None:
        return rich
    _walk(container, rich, level=0)
    if not rich.paragraphs:
        # fall back to a single paragraph of the container's text
        text = container.get_text(" ", strip=True).replace("​", "")
        if text:
            rich.paragraphs.append(Paragraph(runs=[Run(text=text)]))
    return rich


def _walk(container: Tag, rich: RichText, *, level: int) -> None:
    for child in container.children:
        if not isinstance(child, Tag):
            continue
        name = child.name.lower()
        if name in ("ul", "ol"):
            list_type = "number" if name == "ol" else "bullet"
            for li in child.find_all("li", recursive=False):
                para = _paragraph_from(li, list_type=list_type, level=level)
                if para:
                    rich.paragraphs.append(para)
                # nested lists
                for sub in li.find_all(("ul", "ol"), recursive=False):
                    _walk_list(sub, rich, level=level + 1)
        elif name in _BLOCK_TAGS:
            para = _paragraph_from(child)
            if para:
                rich.paragraphs.append(para)
        elif name in ("script", "style"):
            continue


def _walk_list(list_node: Tag, rich: RichText, *, level: int) -> None:
    list_type = "number" if list_node.name.lower() == "ol" else "bullet"
    for li in list_node.find_all("li", recursive=False):
        para = _paragraph_from(li, list_type=list_type, level=level)
        if para:
            rich.paragraphs.append(para)
