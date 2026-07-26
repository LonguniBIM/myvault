# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Project Overview

This is a **Trading Knowledge Base** — a research wiki focused on extracting and distilling trading knowledge into executable Playbooks and Claude Skills. Content is captured from videos, PDFs, and articles, then analyzed through a structured 12-question framework (Groups A–D) aligned with the **Expansion Model** (4-layer filter: Caution → Structure → Invalidation → Execution).

The repository is **not a code/build project** — it's a knowledge management system. Work here involves creating and maintaining markdown wiki pages following a strict schema, and extracting validated trading methodologies into deployable Claude Skills.

**Core thesis:** Any trading system that can be described through the 4-layer filter has potential to become a Claude Skill. A methodology without a clear Invalidation answer is not ready to build.

## Key Files and Purpose

- **`purpose.md`** — Central research question, hypothesis, methodology, success criteria
- **`schema.md`** — Page types, naming conventions, frontmatter format, tag categories
- **`wiki/index.md`** — Central index of all pages, grouped by type
- **`wiki/log.md`** — Activity log in reverse chronological order
- **`wiki/overview.md`** — High-level summary of current state

## Directory Structure

```
wiki/
├── entities/        # Tools, platforms, indicators, organizations
├── concepts/        # Strategies, patterns, methodologies
├── sources/         # Articles, papers, tutorials, reports
├── queries/         # Open questions under investigation
├── comparisons/     # Side-by-side analysis
├── findings/        # Backtesting results, empirical observations
├── methodology/     # Trading methods, checklists
├── synthesis/       # Cross-cutting conclusions
├── thesis/          # Working hypotheses
├── index.md
├── log.md
└── overview.md
```

## Adding New Pages: Workflow

1. **Choose page type** based on `schema.md`
2. **Create file** in appropriate directory with kebab-case naming
3. **Add required frontmatter** (type, title, tags, related, created, updated)
4. **Add type-specific frontmatter** (see schema.md)
5. **Update `wiki/index.md`** with new entry
6. **Update `wiki/log.md`** with date and action
7. **Cross-reference** with `[[wikilinks]]` to related pages

## Auto-Ingest Pipeline

When new content lands in `raw/sources/`:

1. **Read** the full raw source document
2. **Apply 12-question framework** — answer all questions; flag any unanswered ones:
   - **Group A (Timing):** Khoảng thời gian đứng ngoài? Liên hệ ngày trong tuần? Killzones quan trọng?
   - **Group B (Structure):** Swings có giá trị? Loại Range (External/Internal/Neutral)? Tín hiệu chuyển sang Expansion?
   - **Group C (Invalidation):** Điểm vi phạm cụ thể? Reversal vs Continuation? Định nghĩa "Respecting"?
   - **Group D (Execution):** Vai trò Killzones? Signature LTF (M15/M5)? Objectives và dấu hiệu Expansion hoàn tất?
3. **Invalidation check** — nếu Group C chưa có câu trả lời rõ ràng: đánh dấu `invalidation_complete: false`, không tiến hành build Skill
4. **Create source page** in `wiki/sources/` với kết quả phân tích 12 câu hỏi
5. **Extract entities** (tools, sessions, concepts) → create/update entity pages
6. **Extract methodology** (numbered steps hoặc decision tree) → create methodology page, đánh dấu `skill_status: candidate` nếu Group C đã đầy đủ
7. **Map to existing pages** — search index for related content, update comparisons nếu trùng chủ đề
8. **Update cross-references** với `[[wikilinks]]`
9. **Update `wiki/index.md`** và `wiki/log.md`

## Skill Extraction Pipeline

When a methodology page has `skill_status: candidate` và `invalidation_complete: true`:

1. **Verify** logic flow có dạng cây quyết định (If... Then...) qua đủ 4 lớp
2. **Color-check** — Đỏ (Invalidation/SL) rõ ràng, Xanh (Confirmation/Entry) rõ ràng, Vàng (Context) xác định
3. **Draft skill page** in `wiki/skills/` với trigger, steps, và usage examples
4. **Link**: skill ← methodology ← source
5. **Update** `skill_status: validated` sau khi áp dụng thực tế ≥3 lần
6. **Deploy** nếu validated → copy sang `.claude/skills/`
7. **Update** `skill_status: deployed` và ghi nhận trong `wiki/log.md`

## Integration with External Tools

- **Obsidian**: Wiki directory works as an Obsidian vault with full backlink support
- **graphify**: Knowledge graph at `graphify-out/`. Consult `GRAPH_REPORT.md` for relationships
- **LLM Wiki Clipper**: Web extension for capturing content. Auto-triggers ingest pipeline

## Skills Configuration

### obsidian-skills (`.claude/skills/obsidian-skills/`)

| Skill | Trigger | Use |
|-------|---------|-----|
| **obsidian-markdown** | Any `.md` file work | Wikilinks, callouts, frontmatter, embeds |
| **obsidian-bases** | `.base` files | Dashboard metrics |
| **json-canvas** | `.canvas` files | Visual maps |
| **obsidian-cli** | Vault operations | Search, read, append |
| **defuddle** | Web URL fetching | Clean page extraction |

### Content Extraction (`scripts/`)

| Command | Purpose |
|---------|---------|
| `/extract-content` | Scan `raw/` for all new files |
| `/extract-media` | Transcribe video/audio |
| `/graphify .` | Build/update knowledge graph |
| `/graphify-to-wiki` | Sync graph insights to wiki pages |

## Maintenance Tasks

- Update `wiki/overview.md` metrics as content is ingested
- Keep `wiki/index.md` in sync with newly created pages
- Update `wiki/log.md` after every action
- Run `/graphify . --update` after significant wiki changes
