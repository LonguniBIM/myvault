# Graph Report - D:\wiki\BIM_ISO  (2026-09-03)

## Corpus Check
- 45 files · ~5,004,511 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 336 nodes · 756 edges · 23 communities detected
- Extraction: 63% EXTRACTED · 37% INFERRED · 0% AMBIGUOUS · INFERRED: 276 edges (avg confidence: 0.68)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]

## God Nodes (most connected - your core abstractions)
1. `RiseAdapter` - 25 edges
2. `DocumentIR` - 24 edges
3. `Config` - 23 edges
4. `DocxRenderer` - 23 edges
5. `run_extract()` - 20 edges
6. `MarkdownRenderer` - 18 edges
7. `main()` - 16 edges
8. `main()` - 16 edges
9. `BlockIR` - 15 edges
10. `Adapter for Articulate Rise-style lesson pages.  Recognises ``.blocks-lesson`` w` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Ingest a "Webpage, Complete" lesson (HTML + _files + separate audio) into the wi` --uses--> `Config`  [INFERRED]
  D:\wiki\BIM_ISO\scripts\ingest_lesson.py → D:\wiki\BIM_ISO\tools\webpage-content-extractor\src\course_extractor\config.py
- `Extract one lesson folder and publish it as a flat wiki source page.` --uses--> `Config`  [INFERRED]
  D:\wiki\BIM_ISO\scripts\ingest_lesson.py → D:\wiki\BIM_ISO\tools\webpage-content-extractor\src\course_extractor\config.py
- `Typer CLI: inspect / extract / validate.` --uses--> `Config`  [INFERRED]
  D:\wiki\BIM_ISO\tools\webpage-content-extractor\src\course_extractor\cli.py → D:\wiki\BIM_ISO\tools\webpage-content-extractor\src\course_extractor\config.py
- `Extract a lesson to Markdown / DOCX / manifest with audio transcripts.` --uses--> `Config`  [INFERRED]
  D:\wiki\BIM_ISO\tools\webpage-content-extractor\src\course_extractor\cli.py → D:\wiki\BIM_ISO\tools\webpage-content-extractor\src\course_extractor\config.py
- `Validate a previously extracted output folder.` --uses--> `Config`  [INFERRED]
  D:\wiki\BIM_ISO\tools\webpage-content-extractor\src\course_extractor\cli.py → D:\wiki\BIM_ISO\tools\webpage-content-extractor\src\course_extractor\config.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.07
Nodes (45): discover_local_audio(), LocalAudio, match_audio_by_duration(), probe_duration(), transcribe_matched_audio(), Transcriber, ContentAdapter, ParseContext (+37 more)

### Community 1 - "Community 1"
Cohesion: 0.11
Nodes (37): BaseModel, detect_adapter(), Select the best adapter for a given soup., Render DocumentIR -> a self-contained DOCX (images embedded, transcripts filled, Try a direct embed; fall back to a Pillow re-encode (python-docx's         heade, Enum, extract_source_url(), Read the ``<!-- saved from url=(NNNN)... -->`` comment if present. (+29 more)

### Community 2 - "Community 2"
Cohesion: 0.08
Nodes (45): create_wiki_page(), derive_title(), detect_file_type(), download_youtube_audio(), extract_docx(), extract_image(), extract_pdf(), extract_text() (+37 more)

### Community 3 - "Community 3"
Cohesion: 0.1
Nodes (29): find_lesson_folders(), ingest_folder(), load_manifest(), main(), Ingest a "Webpage, Complete" lesson (HTML + _files + separate audio) into the wi, Extract one lesson folder and publish it as a flat wiki source page., _require_course_extractor(), save_manifest() (+21 more)

### Community 4 - "Community 4"
Cohesion: 0.1
Nodes (30): create_wiki_source_page(), derive_title_from_filename(), download_youtube_audio(), file_sha256(), format_duration(), get_new_files(), load_manifest(), main() (+22 more)

### Community 5 - "Community 5"
Cohesion: 0.13
Nodes (20): Exception, _iter_html(), Resolve a user input into a root directory + candidate HTML files.  Accepts a ``, Heuristic score for how likely a file is the lesson page (PLAN M1.3)., resolve_input(), ResolvedInput, score_html(), is_within() (+12 more)

### Community 6 - "Community 6"
Cohesion: 0.22
Nodes (7): Hashing helpers for deterministic asset identity., sha256_file(), _esc(), MarkdownRenderer, _rich_md(), _runs_md(), _sha()

### Community 7 - "Community 7"
Cohesion: 0.15
Nodes (13): parse_timer_label(), parse_valuemax(), Parse audio durations from Rise audio-player DOM., timer_to_seconds(), Filename / slug helpers that stay safe on Windows., Readable ASCII slug suitable for a folder / file name., Make an arbitrary asset name safe as a Windows filename., sanitize_filename() (+5 more)

### Community 8 - "Community 8"
Cohesion: 0.25
Nodes (2): DocxRenderer, _reencode_png()

### Community 9 - "Community 9"
Cohesion: 0.19
Nodes (10): extract(), _parse_formats(), Typer CLI: inspect / extract / validate., Extract a lesson to Markdown / DOCX / manifest with audio transcripts., Validate a previously extracted output folder., _render_docx_qa(), validate(), Structural validation of extraction outputs. (+2 more)

### Community 10 - "Community 10"
Cohesion: 0.32
Nodes (11): attach_local_file(), _fill_file_info(), _looks_remote(), Resolve local image/audio references to on-disk files, safely.  Never mutates so, Resolve ``src`` (as written in HTML) to a local file under ``root_dir``., Bind a concrete on-disk file to an asset (used for duration-matched audio)., resolve_local_asset(), Duration-based matching of local audio files to audio placeholders, plus optiona (+3 more)

### Community 11 - "Community 11"
Cohesion: 1.0
Nodes (0): 

### Community 12 - "Community 12"
Cohesion: 1.0
Nodes (0): 

### Community 13 - "Community 13"
Cohesion: 1.0
Nodes (0): 

### Community 14 - "Community 14"
Cohesion: 1.0
Nodes (0): 

### Community 15 - "Community 15"
Cohesion: 1.0
Nodes (0): 

### Community 16 - "Community 16"
Cohesion: 1.0
Nodes (0): 

### Community 17 - "Community 17"
Cohesion: 1.0
Nodes (0): 

### Community 18 - "Community 18"
Cohesion: 1.0
Nodes (0): 

### Community 19 - "Community 19"
Cohesion: 1.0
Nodes (0): 

### Community 20 - "Community 20"
Cohesion: 1.0
Nodes (0): 

### Community 21 - "Community 21"
Cohesion: 1.0
Nodes (0): 

### Community 22 - "Community 22"
Cohesion: 1.0
Nodes (0): 

## Knowledge Gaps
- **63 isolated node(s):** `Extract content from all file types in raw/ and ingest into the wiki.  Handles`, `Convert text to kebab-case slug safe for filenames.`, `Compute SHA256 hash for change detection.`, `Load processed files manifest.`, `Persist manifest to disk.` (+58 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 11`** (1 nodes): `ingest_lesson.ps1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 12`** (1 nodes): `extract_sample.ps1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 13`** (1 nodes): `ingest_to_wiki.ps1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 14`** (1 nodes): `setup.ps1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 15`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 16`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 17`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 18`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 19`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 20`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 21`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 22`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `run_extract()` connect `Community 0` to `Community 2`, `Community 3`, `Community 6`, `Community 7`, `Community 8`, `Community 9`?**
  _High betweenness centrality (0.156) - this node is a cross-community bridge._
- **Why does `main()` connect `Community 4` to `Community 2`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._
- **Are the 23 inferred relationships involving `str` (e.g. with `get_new_files()` and `extract_video_audio()`) actually correct?**
  _`str` has 23 INFERRED edges - model-reasoned connections that need verification._
- **Are the 15 inferred relationships involving `RiseAdapter` (e.g. with `Select the best adapter for a given soup.` and `AssetKind`) actually correct?**
  _`RiseAdapter` has 15 INFERRED edges - model-reasoned connections that need verification._
- **Are the 19 inferred relationships involving `DocumentIR` (e.g. with `LocalAudio` and `Transcriber`) actually correct?**
  _`DocumentIR` has 19 INFERRED edges - model-reasoned connections that need verification._
- **Are the 21 inferred relationships involving `Config` (e.g. with `Ingest a "Webpage, Complete" lesson (HTML + _files + separate audio) into the wi` and `Extract one lesson folder and publish it as a flat wiki source page.`) actually correct?**
  _`Config` has 21 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `DocxRenderer` (e.g. with `ExtractResult` and `End-to-end extraction pipeline (IR-first).`) actually correct?**
  _`DocxRenderer` has 10 INFERRED edges - model-reasoned connections that need verification._