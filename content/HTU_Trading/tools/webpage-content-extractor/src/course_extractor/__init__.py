"""Webpage-Complete lesson content extractor (IR-first).

Parses a locally-saved "Webpage, Complete" lesson into an intermediate
representation, then renders Markdown / DOCX / manifest from that single IR.
Audio placeholders are filled with transcripts of local audio files that are
auto-matched by duration.
"""

__version__ = "0.1.0"
SCHEMA_VERSION = 1
