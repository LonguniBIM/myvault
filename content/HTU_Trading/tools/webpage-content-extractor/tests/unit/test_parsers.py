from bs4 import BeautifulSoup

from course_extractor.parsers.duration import (
    parse_timer_label,
    parse_valuemax,
    timer_to_seconds,
)
from course_extractor.parsers.rich_text import parse_rich_text
from course_extractor.util.paths import sanitize_filename, slugify


def test_slugify():
    assert slugify("Lesson 1 - BIM Defined") == "lesson-1-bim-defined"
    assert slugify("  ") == "lesson"
    assert slugify("CON") == "con-file"


def test_sanitize_filename():
    assert sanitize_filename('a:b/c*.png') == "a_b_c_.png"
    assert sanitize_filename("") == "file"


def test_duration_parsing():
    html = """
    <div class="audio-player">
      <div class="audio-player__tracker-handle" aria-valuemax="41.14576"></div>
      <div class="audio-player__timer">00:41</div>
    </div>"""
    soup = BeautifulSoup(html, "lxml")
    container = soup.select_one(".audio-player")
    assert abs(parse_valuemax(container) - 41.14576) < 1e-6
    assert parse_timer_label(container) == "00:41"
    assert timer_to_seconds("00:41") == 41
    assert timer_to_seconds("01:05") == 65


def test_rich_text_inline_and_list():
    html = """
    <div class="fr-view">
      <p>Hello <strong>bold</strong> and <em>italic</em> and <a href="http://x">link</a>.</p>
      <ul><li>one</li><li>two</li></ul>
    </div>"""
    soup = BeautifulSoup(html, "lxml")
    rt = parse_rich_text(soup.select_one(".fr-view"))
    assert len(rt.paragraphs) == 3
    runs = rt.paragraphs[0].runs
    assert any(r.bold and r.text == "bold" for r in runs)
    assert any(r.italic and r.text == "italic" for r in runs)
    assert any(r.link == "http://x" for r in runs)
    assert rt.paragraphs[1].list_type == "bullet"
    assert rt.paragraphs[1].text == "one"
