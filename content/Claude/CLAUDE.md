# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Project Overview

This is a **Claude Code Mastery Knowledge Base** — a research wiki focused on deeply understanding, effectively using, and optimizing Claude Code. Content is captured from official docs, tutorials, blog posts, and community resources, then analyzed through a structured framework to extract reusable Skills.

The repository is **not a code/build project** — it's a knowledge management system. Work here involves creating and maintaining markdown wiki pages following a strict schema, and extracting methodologies into deployable Skills.

**Core thesis:** Any document whose methodology can be expressed as numbered steps has potential to become a Claude Skill.

## Key Files and Purpose

- **`purpose.md`** — Central research question, hypothesis, methodology, success criteria
- **`schema.md`** — Page types, naming conventions, frontmatter format, six-question framework, tag categories
- **`wiki/index.md`** — Central index of all pages, grouped by type
- **`wiki/log.md`** — Activity log in reverse chronological order
- **`wiki/overview.md`** — High-level summary of current state

## Directory Structure

```
wiki/
├── entities/        # Claude Code, MCP servers, tools, people
├── concepts/        # Context engineering, skill design, agent patterns
├── sources/         # Docs, blog posts, tutorials, videos
├── queries/         # "How to optimize X?" open questions
├── comparisons/     # Different approaches compared
├── findings/        # Empirical test results
├── methodology/     # Step-by-step methods (Skill candidates)
├── synthesis/       # Cross-cutting conclusions
├── thesis/          # Working hypotheses
├── skills/          # Validated, deployable Skills
├── index.md
├── log.md
└── overview.md
```

## Six-Question Analysis Framework

When ingesting ANY new source, apply this framework:

| # | Question | Maps to |
|---|----------|---------|
| 1 | What problem does this document solve? | `wiki/concepts/` or entity description |
| 2 | What numbered steps does the author prescribe? | `wiki/methodology/` (Skill candidate) |
| 3 | What principles recur throughout? | `wiki/concepts/` or entity "principles" section |
| 4 | What mistakes does the author warn against? | `wiki/findings/` (anti-patterns) |
| 5 | What diagnostic questions does the author pose? | `wiki/queries/` or methodology checklist |
| 6 | Can the method be expressed as numbered steps? | If YES → `wiki/skills/` candidate |

## Adding New Pages: Workflow

1. **Choose page type** based on `schema.md`
2. **Create file** in appropriate directory with kebab-case naming
3. **Add required frontmatter** (type, title, tags, related, created, updated)
4. **Add type-specific frontmatter** (see schema.md)
5. **Apply six-question framework** if the page is a source
6. **Update `wiki/index.md`** with new entry
7. **Update `wiki/log.md`** with date and action
8. **Cross-reference** with `[[wikilinks]]` to related pages

## Auto-Ingest Pipeline

When new content lands in `raw/sources/`:

1. **Read** the full raw source document
2. **Apply six-question framework** — answer all 6 questions
3. **Create source page** in `wiki/sources/` with structured analysis
4. **Extract entities** (tools, features, people mentioned) → create/update entity pages
5. **Extract concepts** (techniques, patterns) → create/update concept pages
6. **Extract methodologies** (numbered steps) → create methodology pages
7. **Assess skill potential** — if method has clear steps → mark `skill_status: candidate`
8. **Map to existing pages** — search index for related content
9. **Update cross-references** with `[[wikilinks]]`
10. **Update `wiki/index.md`** and `wiki/log.md`

## Skill Extraction Pipeline

When a methodology is identified as a Skill candidate:

1. **Verify** the method has clear, numbered steps
2. **Create methodology page** in `wiki/methodology/` with full steps
3. **Draft skill page** in `wiki/skills/` with trigger, steps, and usage
4. **Link** methodology ← source, skill ← methodology
5. **Test** the skill in a real project (record in `tested_in:` frontmatter)
6. **Update** effectiveness rating based on test results
7. **Deploy** if effectiveness is medium/high → copy to `.claude/skills/` or `.cursor/skills/`

## Integration with External Tools

- **Obsidian**: Wiki directory works as an Obsidian vault. Use obsidian-skills for proper Markdown, Bases, Canvas, and CLI interaction.
- **graphify**: Knowledge graph at `graphify-out/`. Consult `GRAPH_REPORT.md` for god nodes, communities, and surprising connections before deep-diving.
- **LLM Wiki Clipper**: Web extension for capturing documentation pages. Auto-triggers ingest pipeline.

## Skills Configuration

### obsidian-skills (`.claude/skills/obsidian-skills/`)

| Skill | Trigger | Use |
|-------|---------|-----|
| **obsidian-markdown** | Any `.md` file work | Wikilinks, callouts, frontmatter, embeds |
| **obsidian-bases** | `.base` files, database views | Dashboard metrics |
| **json-canvas** | `.canvas` files, visual maps | Skill relationship diagrams |
| **obsidian-cli** | Vault operations | Search, read, append |
| **defuddle** | Web URL fetching | Clean page extraction |

### graphify (`graphify-out/`)

- Before answering relationship questions → read `GRAPH_REPORT.md`
- After wiki changes → run `/graphify . --update`
- To sync insights → run `/graphify-to-wiki`

### Content Extraction (`scripts/`)

| Command | Purpose |
|---------|---------|
| `/extract-content` | Scan `raw/` for all new files |
| `/extract-media` | Transcribe video/audio |
| `/graphify .` | Build/update knowledge graph |
| `/graphify-to-wiki` | Sync graph → wiki pages |
| `/ingest-pending` | Process queued items from watcher |

## Tag Strategy

| Category | Values |
|----------|--------|
| **topic** | `setup`, `workflow`, `optimization`, `debugging`, `skills`, `memory`, `mcp`, `hooks`, `permissions`, `context`, `agents`, `prompts` |
| **priority** | `critical`, `high`, `medium`, `low` |
| **confidence** | `high`, `medium`, `low`, `speculative` |

## Maintenance Tasks

- Update `wiki/overview.md` metrics as content is ingested
- Keep `wiki/index.md` in sync with newly created pages
- Update `wiki/log.md` after every action
- Review methodology pages for skill extraction opportunities
- Periodically run `/graphify-to-wiki` to discover new connections
- Test and deploy skills from `wiki/skills/` to actual skill directories
