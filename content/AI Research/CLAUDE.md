# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **GitHub Repository Knowledge Base** — a curated wiki that aggregates useful GitHub repos into a queryable decision-support system. The user captures repos via the **LLM Wiki Clipper** web extension, and the system automatically ingests, categorizes, compares similar-purpose repos, and produces best-fit recommendations.

The repository is **not a code/build project** — it's a knowledge management system. There are no build commands, tests, or linting. Work here involves creating and maintaining markdown wiki pages following a strict schema.

**Scope**: Only GitHub repositories. Non-GitHub content is out of scope.

## Key Files and Purpose

- **`purpose.md`** — Defines the central research question, hypothesis, methodology, and success criteria. Start here to understand what this research is investigating.
- **`schema.md`** — The authoritative specification for page types, naming conventions, frontmatter format, cross-referencing rules, and contradiction handling. This is the "law of the land" — all wiki pages must conform to it.
- **`wiki/index.md`** — Central index of all pages, grouped by type. Every page created must be listed here.
- **`wiki/log.md`** — Activity log in reverse chronological order. Record each research action, finding, or page addition here.
- **`wiki/overview.md`** — High-level summary of the wiki's current state. Update this as understanding evolves.

## Directory Structure

```
wiki/
├── entities/        # Named things (people, tools, orgs, datasets)
├── concepts/        # Ideas, techniques, phenomena, frameworks
├── sources/         # Papers, articles, talks, books, blog posts
├── queries/         # Open questions under active investigation
├── comparisons/     # Side-by-side analysis of related entities
├── findings/        # Individual empirical results or observations
├── methodology/     # Research methods, protocols, study designs
├── synthesis/       # Cross-cutting summaries and conclusions
├── thesis/          # Working hypotheses and their evolution
├── index.md         # Central index of all pages
├── log.md           # Activity log (reverse chronological)
└── overview.md      # High-level project summary
```

## Adding New Pages: Workflow

1. **Choose the page type** based on `schema.md`:
   - Entity: person, tool, org, dataset
   - Concept: idea, technique, phenomenon, framework
   - Source: paper, article, talk, book, blog post
   - Query: open question under investigation
   - Comparison: side-by-side analysis
   - Finding: empirical result or observation
   - Synthesis: cross-cutting summary
   - Thesis: working hypothesis
   - Methodology: research method or protocol

2. **Create the file** in the appropriate directory with proper naming:
   - General: `kebab-case.md`
   - Sources: `author-year-slug.md` (e.g., `wei-2022-cot.md`)
   - Queries: question as slug (e.g., `does-scale-improve-reasoning.md`)

3. **Add required frontmatter** (all pages):
   ```yaml
   ---
   type: entity | concept | source | query | comparison | synthesis | overview
   title: Human-readable title
   tags: []
   related: []
   created: YYYY-MM-DD
   updated: YYYY-MM-DD
   ---
   ```

4. **Add type-specific frontmatter**:
   - **Sources**: add `authors: []`, `year: YYYY`, `url: ""`, `venue: ""`
   - **Findings**: add `source: "[[source-slug]]"`, `confidence: low | medium | high`, `replicated: true | false | null`
   - **Theses**: add `confidence: low | medium | high`, `status: speculative | supported | refuted | settled`

5. **Update `wiki/index.md`** — Add an entry under the appropriate type:
   ```markdown
   - [[page-slug]] — one-line description
   ```

6. **Update `wiki/log.md`** — Add entry under today's date (or create a new date section):
   ```markdown
   ## YYYY-MM-DD
   - Action taken / finding noted
   ```

## Cross-referencing and Linking

- Use `[[page-slug]]` syntax to link between wiki pages (Obsidian convention)
- Entities and concepts → must appear in `wiki/index.md`
- Queries → link to sources and concepts they draw on
- Synthesis pages → cite contributing sources via `related:` frontmatter
- Findings → link to their source via `source:` frontmatter field
- Thesis pages → reference supporting and refuting findings via `related:`
- Methodology pages → cited by findings that used them

## Handling Contradictions

When sources contradict each other:
1. Note the contradiction in the relevant concept or entity page
2. Create or update a query page to track the open question
3. Link both sources from the query page
4. Resolve in a synthesis page once sufficient evidence exists

## Key Principles

- **Living documents**: Thesis pages evolve as evidence accumulates — keep them updated
- **Replication matters**: Assess replication status in finding pages when known
- **Explain the why**: Methodology pages explain rationale, not just procedure
- **Distinguish inference**: Be clear about direct evidence vs. inference in findings
- **Schema compliance**: All pages must follow the schema in `schema.md` — this enables consistent cross-referencing and querying

## Auto-Ingest Pipeline (LLM Wiki Clipper)

When a new GitHub repo is clipped via LLM Wiki Clipper and lands in `raw/sources/`:

1. **Read** the full raw source document
2. **Extract metadata**: repo name, author/org, description, primary language, stars, license, last updated, use case category
3. **Create entity page** in `wiki/entities/` with structured metadata and summary
4. **Map to existing repos**: search `wiki/index.md` and entity pages for repos with overlapping tags or use case categories
5. **If similar repos exist**: create or update a `wiki/comparisons/` page with structured pros/cons analysis and a best-fit recommendation
6. **Update cross-references**: add `[[wiki-links]]` connecting the new entity to related entities, comparisons, and concepts
7. **Update `wiki/index.md`** with new pages and one-line descriptions
8. **Append to `wiki/log.md`** with the date, source name, and what changed
9. **Update `wiki/overview.md`** metrics (repos ingested, comparisons, decisions)

A single repo ingest may touch 5–15 wiki pages. That is normal.

## Comparison & Recommendation Workflow

When ≥2 repos share a use case category:

1. Create a comparison page in `wiki/comparisons/` named by the shared use case (e.g., `web-scraping-tools.md`)
2. Structure the comparison with: overview, feature matrix, pros/cons for each repo, and a **Best Fit Recommendation** section
3. The recommendation must include clear reasoning citing specific strengths/weaknesses
4. Link all compared entity pages back to the comparison page via `related:`
5. Update the comparison whenever a new repo in the same category is ingested

## Integration with External Tools

- **Obsidian**: This wiki integrates with Obsidian (.obsidian/ directory). Pages are viewable and editable in Obsidian with full backlink support. Use obsidian-skills for proper Markdown, Bases, Canvas, and CLI interaction.
- **LLM Wiki Clipper**: Web extension used to capture GitHub repos. Clipped content automatically triggers the auto-ingest pipeline.
- **LLM Wiki**: The `.llm-wiki/` directory stores project metadata for tool integration; do not edit manually.
- **graphify**: Knowledge graph at `graphify-out/`. Always consult `GRAPH_REPORT.md` before deep-diving into files.

## Maintenance Tasks

- Update `wiki/overview.md` metrics as repos are ingested and comparisons are made
- Keep `wiki/index.md` in sync with newly created pages
- Update `wiki/log.md` after every ingest or comparison action
- Review comparison pages when new repos are added to existing categories
- Ensure frontmatter `updated: YYYY-MM-DD` is current when pages are modified

---

## Skills Configuration

### obsidian-skills (`.claude/skills/obsidian-skills/`)

Obsidian-native agent skills from [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills). These teach the agent proper Obsidian syntax and workflows.

| Skill | Trigger | Path |
|-------|---------|------|
| **obsidian-markdown** | Working with `.md` files, wikilinks, callouts, frontmatter, embeds | `skills/obsidian-markdown/SKILL.md` |
| **obsidian-bases** | Working with `.base` files, database views, filters, formulas | `skills/obsidian-bases/SKILL.md` |
| **json-canvas** | Working with `.canvas` files, mind maps, flowcharts | `skills/json-canvas/SKILL.md` |
| **obsidian-cli** | Vault operations via CLI, plugin dev, search, note management | `skills/obsidian-cli/SKILL.md` |
| **defuddle** | Extracting clean markdown from web pages (prefer over raw fetch) | `skills/defuddle/SKILL.md` |

**When to invoke obsidian-skills:**
- Creating or editing any `.md` file in the wiki: use **obsidian-markdown** for correct wikilink and frontmatter syntax
- Building a `.base` dashboard for the wiki: use **obsidian-bases**
- Creating visual maps of repo relationships: use **json-canvas**
- Interacting with the Obsidian app (search, read, append): use **obsidian-cli**
- Fetching web content for a new raw source: use **defuddle** first, fall back to WebFetch for `.md` URLs

### graphify (`graphify-out/`)

Knowledge graph from [safishamsi/graphify](https://github.com/safishamsi/graphify). Converts the wiki corpus into a queryable graph of concepts, relationships, and communities.

**Initial build** (run once, then incrementally):
```
/graphify .
```

**Always-on rules:**
- Before answering architecture, relationship, or "how does X connect to Y" questions, **read `graphify-out/GRAPH_REPORT.md`** for god nodes, communities, and surprising connections
- If `graphify-out/wiki/index.md` exists, navigate it instead of reading raw files
- Use `/graphify query "<question>"` for targeted graph traversal
- Use `/graphify path "A" "B"` to find shortest paths between concepts
- Use `/graphify explain "X"` for plain-language node explanations
- After modifying wiki content, run `/graphify --update` to refresh semantic nodes
- After adding new raw sources, run `/graphify .` to rebuild the full graph

**Graph report injection:** When `graphify-out/GRAPH_REPORT.md` exists, treat it as mandatory pre-reading before any of these actions:
1. Answering questions about relationships between repos or concepts
2. Searching for files or content (consult god nodes first)
3. Creating new comparison or synthesis pages (check graph communities)
4. Investigating cross-cutting patterns across entities

### Content Extraction (`scripts/extract_content.py`)

Unified pipeline for extracting content from **all file types** and ingesting into the wiki. Triggered via `/extract-content` in Cursor.

| File Type | Method | Local? |
|-----------|--------|--------|
| Video/Audio | faster-whisper transcription | Yes |
| Images | Metadata + description (full analysis via /graphify) | Partial |
| PDFs | Text extraction (PyMuPDF/pypdf) | Yes |
| Office (.docx/.xlsx) | python-docx / openpyxl → markdown | Yes |

| Command | Purpose |
|---------|---------|
| `/extract-content` | Scan `raw/` for all new files, extract, ingest |
| `/extract-content --type video` | Only video/audio files |
| `/extract-content --type image` | Only images |
| `/extract-content --type pdf` | Only PDFs |
| `/extract-content --type doc` | Only .docx/.xlsx |
| `/extract-content --model medium` | Higher Whisper accuracy for technical content |
| `/extract-content --url <youtube-url>` | Download + transcribe YouTube video |
| `/extract-content --dry-run` | Preview without processing |

**After extraction**: Run `/graphify ./raw --update` to incorporate extracted content into the knowledge graph (needed for full semantic extraction, especially images and PDFs).

**File locations**:
- Extracts: `raw/extracts/<slug>.md`
- Wiki pages: `wiki/sources/extract-<slug>.md`
- Manifest (skip tracking): `scripts/.content_manifest.json`

**Legacy**: `scripts/extract_media.py` still works for video/audio-only extraction.

### Skills Orchestration

The obsidian-skills and graphify work together as a pipeline:

1. **Ingest phase**: New repo clipped → defuddle cleans the HTML → raw source saved
2. **Graph phase**: `/graphify --update` processes new content → GRAPH_REPORT.md updated
3. **Wiki phase**: obsidian-markdown creates entity/comparison pages with proper wikilinks, frontmatter, and cross-references informed by graph communities
4. **Query phase**: User asks a question → graphify query finds relevant nodes → obsidian-cli searches vault → answer synthesized from both

**Automatic triggers:**
- When creating a new entity page: consult GRAPH_REPORT.md to identify related god nodes and communities before writing `related:` frontmatter
- When writing comparisons: use `/graphify path` to discover non-obvious connections between repos
- When updating synthesis pages: use `/graphify query` to surface cross-cutting themes the graph detected
- When fetching a URL: prefer `defuddle parse <url> --md` over raw HTTP fetch
