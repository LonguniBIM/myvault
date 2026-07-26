# Setup Guide: LLM Wiki + Graphify + Obsidian Skills Workspace

> **Reference workspace:** `D:\wiki\AI Research`
> **Agent command:** Type `/setup-wiki` in Cursor or Claude Code to start the interactive wizard.

---

## Overview

This guide sets up a fully integrated wiki workspace with:

| Component | Role |
|-----------|------|
| **LLM Wiki pattern** | Structure: `purpose.md` + `schema.md` + `wiki/` directories |
| **Graphify** | Knowledge graph: maps all content into queryable graph |
| **Obsidian Skills** | Formatting: proper wikilinks, callouts, frontmatter, CLI |
| **Auto-ingest pipeline** | Automation: file watcher + queue + agent processing |
| **Obsidian Bases** | Dashboard: .base files for metrics and tracking |

---

## Quick Start (5 minutes)

```bash
# 1. Create workspace directory
mkdir my-wiki && cd my-wiki

# 2. Install tools
pip install graphifyy faster-whisper yt-dlp PyMuPDF python-docx openpyxl
npm install -g defuddle
graphify cursor install

# 3. Start the interactive setup wizard
# Open in Cursor → type "/setup-wiki" in chat
```

The agent will ask you questions about your wiki's purpose, then generate all files automatically.

---

## What `/setup-wiki` Does

When you type `/setup-wiki`, the agent:

1. **Asks 6 questions** about your wiki purpose, content sources, and preferences
2. **Generates `purpose.md`** — tailored to your research question/goals
3. **Generates `schema.md`** — page types and rules matching your needs
4. **Generates `CLAUDE.md`** — agent instructions for your specific workflow
5. **Creates directory structure** — all wiki/ folders and support files
6. **Copies scripts** from reference workspace (extract, watch, ingest)
7. **Copies cursor/claude rules** — graphify-to-wiki, auto-ingest, extract rules
8. **Installs obsidian-skills** — clones the skill files into .claude/skills/
9. **Guides first-run verification** — tests each pipeline component

---

## Directory Structure (After Setup)

```
my-wiki/
├── purpose.md              ← Why this wiki exists (generated interactively)
├── schema.md               ← Page types, naming, frontmatter rules
├── CLAUDE.md               ← Agent instructions for this project
│
├── raw/
│   ├── sources/            ← Captured content (immutable)
│   ├── extracts/           ← Extracted text from media/PDFs
│   ├── transcripts/        ← Video/audio transcripts
│   └── assets/             ← Images and attachments
│
├── wiki/
│   ├── index.md            ← Central page catalog
│   ├── log.md              ← Activity log (reverse chronological)
│   ├── overview.md         ← High-level summary
│   ├── entities/           ← Named things (tools, people, orgs)
│   ├── concepts/           ← Ideas, techniques, frameworks
│   ├── sources/            ← Source summaries
│   ├── queries/            ← Open questions
│   ├── comparisons/        ← Side-by-side analysis
│   ├── synthesis/          ← Cross-cutting insights
│   ├── wiki-dashboard.base ← Obsidian metrics view
│   └── repo-tracker.base   ← Entity tracker (if applicable)
│
├── scripts/
│   ├── extract_content.py  ← Multi-format extraction
│   ├── extract_media.py    ← Video/audio transcription
│   └── watch_ingest.py     ← File watcher for auto-queue
│
├── .cursor/rules/
│   ├── graphify-to-wiki.mdc    ← Sync graph → wiki
│   ├── auto-ingest.mdc         ← Process queued items
│   ├── extract-content.mdc     ← /extract-content command
│   ├── extract-media.mdc       ← /extract-media command
│   └── wiki-workspace-setup.mdc← This setup wizard
│
├── .claude/
│   ├── commands/graphify-to-wiki.md
│   ├── skills/obsidian-skills/  ← 5 Obsidian agent skills
│   └── settings.json
│
├── .obsidian/              ← Obsidian vault config
├── .llm-wiki/ingest-queue/ ← Pending ingest items
├── .graphifyignore         ← Files to exclude from graph
└── graphify-out/           ← Knowledge graph output (after first /graphify)
```

---

## Daily Workflow

```
                    ┌─────────────────────┐
                    │   Content Sources    │
                    │  (clip, upload, note)│
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   raw/sources/*.md   │
                    │   (immutable store)  │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
    ┌─────────▼────────┐  ┌───▼────────┐  ┌───▼──────────┐
    │  watch_ingest.py │  │ /graphify . │  │ /extract-*   │
    │  (auto-queue)    │  │ (graph build)│ │ (PDF/media)  │
    └─────────┬────────┘  └───┬────────┘  └───┬──────────┘
              │                │                │
    ┌─────────▼────────┐  ┌───▼────────────┐  │
    │ /ingest-pending  │  │ /graphify-to-  │  │
    │ (CLAUDE.md flow) │  │ wiki (sync)    │  │
    └─────────┬────────┘  └───┬────────────┘  │
              │                │                │
              └────────────────┼────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │   wiki/* pages      │
                    │ (Obsidian-formatted)│
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │ /graphify --update  │
                    │ (feedback loop)     │
                    └─────────────────────┘
```

---

## Commands Reference

| Command | Environment | What it does |
|---------|-------------|-------------|
| `/setup-wiki` | Cursor/Claude | Interactive workspace setup wizard |
| `/extract-content` | Cursor/Claude | Extract text from PDFs/docs/media |
| `/extract-media` | Cursor/Claude | Transcribe video/audio files |
| `/graphify .` | Cursor/Claude | Build/rebuild knowledge graph |
| `/graphify-to-wiki` | Cursor/Claude | Sync graph insights → wiki pages |
| `/ingest-pending` | Cursor/Claude | Process queued raw sources |

| Script | Terminal | What it does |
|--------|---------|-------------|
| `python scripts/watch_ingest.py` | PowerShell/Bash | Watch raw/sources/ for new files |
| `python scripts/watch_ingest.py --status` | PowerShell/Bash | Show pending ingest queue |
| `python scripts/extract_content.py` | PowerShell/Bash | Batch content extraction |
| `python scripts/extract_media.py` | PowerShell/Bash | Batch media transcription |

---

## Obsidian Skills Available

| Skill | Auto-Triggered When | Manual Use |
|-------|-------------------|------------|
| **obsidian-markdown** | Every .md file creation/edit | Formatting reference |
| **defuddle** | Fetching any web URL | `defuddle parse <url> --md` |
| **obsidian-cli** | Search/read vault operations | `obsidian search query="..."` |
| **json-canvas** | User requests visualization | Create .canvas files |
| **obsidian-bases** | User requests database views | Create .base files |

---

## Prerequisites

| Tool | Install | Purpose |
|------|---------|---------|
| Python 3.10+ | System install | Scripts, graphify |
| Node.js 18+ | System install | Defuddle |
| Obsidian | [obsidian.md](https://obsidian.md) | Vault viewer/editor |
| Cursor IDE | [cursor.sh](https://cursor.sh) | AI agent interface |
| graphify | `pip install graphifyy` | Knowledge graph |
| faster-whisper | `pip install faster-whisper` | Audio transcription |
| defuddle | `npm install -g defuddle` | Web page cleaning |

---

## Customization

### Adding Your Own Page Types

Edit `schema.md` to add new types. Each type needs:
- A directory under `wiki/`
- A section in `wiki/index.md`
- Frontmatter specification

### Changing the Ingest Pipeline

Edit `CLAUDE.md` "Auto-Ingest Pipeline" section to customize what happens when new content arrives.

### Extending Graphify Integration

Edit `.cursor/rules/graphify-to-wiki.mdc` to change how graph nodes map to wiki pages.

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `graphify: command not found` | `pip install graphifyy` or add `~/.local/bin` to PATH |
| `defuddle: command not found` | `npm install -g defuddle` |
| Obsidian doesn't show .base files | Update Obsidian to latest version (Bases require v1.8+) |
| watch_ingest.py doesn't detect files | Ensure files have `.md` extension in `raw/sources/` |
| `/graphify-to-wiki` says no graph | Run `/graphify .` first to build the graph |
| Wikilinks don't resolve in Obsidian | Open the wiki/ folder as an Obsidian vault |

---

## Reference Workspace

All templates, scripts, and configurations are available in:

```
D:\wiki\AI Research
```

This workspace contains a working implementation that can be used as a template for any new wiki project.
