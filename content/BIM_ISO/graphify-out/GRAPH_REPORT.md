# Graph Report - D:\wiki\BIM_ISO  (2026-07-25)

## Corpus Check
- 44 files · ~335,615 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 334 nodes · 750 edges · 22 communities detected
- Extraction: 64% EXTRACTED · 36% INFERRED · 0% AMBIGUOUS · INFERRED: 271 edges (avg confidence: 0.67)
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

## God Nodes (most connected - your core abstractions)
1. `RiseAdapter` - 24 edges
2. `DocumentIR` - 23 edges
3. `DocxRenderer` - 23 edges
4. `Config` - 22 edges
5. `run_extract()` - 20 edges
6. `MarkdownRenderer` - 18 edges
7. `main()` - 16 edges
8. `main()` - 16 edges
9. `BlockIR` - 15 edges
10. `Adapter for Articulate Rise-style lesson pages.  Recognises ``.blocks-lesson`` w` - 14 edges

## Surprising Connections (you probably didn't know these)
- `parse_document()` --calls--> `load_html()`  [INFERRED]
  D:\wiki\BIM_ISO\tools\webpage-content-extractor\src\course_extractor\pipeline.py → D:\wiki\BIM_ISO\tools\webpage-content-extractor\src\course_extractor\html_loader.py
- `test_rich_text_inline_and_list()` --calls--> `parse_rich_text()`  [INFERRED]
  D:\wiki\BIM_ISO\tools\webpage-content-extractor\tests\unit\test_parsers.py → D:\wiki\BIM_ISO\tools\webpage-content-extractor\src\course_extractor\parsers\rich_text.py
- `scan_files()` --calls--> `in_lesson_scope()`  [INFERRED]
  D:\wiki\BIM_ISO\scripts\extract_content.py → D:\wiki\BIM_ISO\scripts\lesson_utils.py
- `extract_pdf()` --calls--> `Run`  [INFERRED]
  D:\wiki\BIM_ISO\scripts\extract_content.py → D:\wiki\BIM_ISO\tools\webpage-content-extractor\src\course_extractor\models.py
- `download_youtube_audio()` --calls--> `Run`  [INFERRED]
  D:\wiki\BIM_ISO\scripts\extract_content.py → D:\wiki\BIM_ISO\tools\webpage-content-extractor\src\course_extractor\models.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.11
Nodes (36): BaseModel, detect_adapter(), Select the best adapter for a given soup., Render DocumentIR -> a self-contained DOCX (images embedded, transcripts filled, Try a direct embed; fall back to a Pillow re-encode (python-docx's         heade, Enum, Render DocumentIR -> Markdown, copying referenced assets into assets/.  Designed, AssetKind (+28 more)

### Community 1 - "Community 1"
Cohesion: 0.09
Nodes (32): discover_local_audio(), LocalAudio, match_audio_by_duration(), probe_duration(), Duration-based matching of local audio files to audio placeholders, plus optiona, Greedy nearest-duration matching; each file is used at most once., transcribe_matched_audio(), Transcriber (+24 more)

### Community 2 - "Community 2"
Cohesion: 0.08
Nodes (45): create_wiki_page(), derive_title(), detect_file_type(), download_youtube_audio(), extract_docx(), extract_image(), extract_pdf(), extract_text() (+37 more)

### Community 3 - "Community 3"
Cohesion: 0.09
Nodes (30): extract(), inspect(), _parse_formats(), Typer CLI: inspect / extract / validate., Print discovered lesson structure without writing any output., Extract a lesson to Markdown / DOCX / manifest with audio transcripts., Validate a previously extracted output folder., _render_docx_qa() (+22 more)

### Community 4 - "Community 4"
Cohesion: 0.1
Nodes (30): create_wiki_source_page(), derive_title_from_filename(), download_youtube_audio(), file_sha256(), format_duration(), get_new_files(), load_manifest(), main() (+22 more)

### Community 5 - "Community 5"
Cohesion: 0.1
Nodes (24): attach_local_file(), _fill_file_info(), _looks_remote(), Resolve local image/audio references to on-disk files, safely.  Never mutates so, Resolve ``src`` (as written in HTML) to a local file under ``root_dir``., Bind a concrete on-disk file to an asset (used for duration-matched audio)., resolve_local_asset(), parse_timer_label() (+16 more)

### Community 6 - "Community 6"
Cohesion: 0.13
Nodes (20): Exception, _iter_html(), Resolve a user input into a root directory + candidate HTML files.  Accepts a ``, Heuristic score for how likely a file is the lesson page (PLAN M1.3)., resolve_input(), ResolvedInput, score_html(), is_within() (+12 more)

### Community 7 - "Community 7"
Cohesion: 0.14
Nodes (21): find_lesson_folders(), folder_signature(), in_lesson_scope(), is_lesson_folder(), Shared helpers for detecting "Webpage, Complete" lesson folders.  A lesson folde, True if ``path`` is a lesson's saved asset or a file inside a lesson folder., Cheap change-detection signature over a folder's files., derive_title() (+13 more)

### Community 8 - "Community 8"
Cohesion: 0.25
Nodes (2): DocxRenderer, _reencode_png()

### Community 9 - "Community 9"
Cohesion: 0.32
Nodes (4): _esc(), MarkdownRenderer, _rich_md(), _runs_md()

### Community 10 - "Community 10"
Cohesion: 0.4
Nodes (4): extract_source_url(), load_html(), Load saved HTML into a BeautifulSoup tree without running any JavaScript., Read the ``<!-- saved from url=(NNNN)... -->`` comment if present.

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

## Knowledge Gaps
- **63 isolated node(s):** `Extract content from all file types in raw/ and ingest into the wiki.  Handles`, `Convert text to kebab-case slug safe for filenames.`, `Compute SHA256 hash for change detection.`, `Load processed files manifest.`, `Persist manifest to disk.` (+58 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 11`** (1 nodes): `extract_sample.ps1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 12`** (1 nodes): `ingest_to_wiki.ps1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 13`** (1 nodes): `setup.ps1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 14`** (1 nodes): `__init__.py`
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

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `run_extract()` connect `Community 1` to `Community 2`, `Community 3`, `Community 5`, `Community 8`, `Community 9`?**
  _High betweenness centrality (0.162) - this node is a cross-community bridge._
- **Why does `main()` connect `Community 4` to `Community 2`?**
  _High betweenness centrality (0.097) - this node is a cross-community bridge._
- **Are the 23 inferred relationships involving `str` (e.g. with `get_new_files()` and `extract_video_audio()`) actually correct?**
  _`str` has 23 INFERRED edges - model-reasoned connections that need verification._
- **Are the 14 inferred relationships involving `RiseAdapter` (e.g. with `Select the best adapter for a given soup.` and `AssetKind`) actually correct?**
  _`RiseAdapter` has 14 INFERRED edges - model-reasoned connections that need verification._
- **Are the 18 inferred relationships involving `DocumentIR` (e.g. with `LocalAudio` and `Transcriber`) actually correct?**
  _`DocumentIR` has 18 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `DocxRenderer` (e.g. with `ExtractResult` and `End-to-end extraction pipeline (IR-first).`) actually correct?**
  _`DocxRenderer` has 10 INFERRED edges - model-reasoned connections that need verification._
- **Are the 20 inferred relationships involving `Config` (e.g. with `Ingest a "Webpage, Complete" lesson (HTML + _files + separate audio) into the wi` and `Extract one lesson folder and publish it as a flat wiki source page.`) actually correct?**
  _`Config` has 20 INFERRED edges - model-reasoned connections that need verification._