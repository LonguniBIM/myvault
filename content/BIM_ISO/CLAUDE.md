# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Project Overview

This is the **BIM ISO 19650 Mastery** knowledge space — a research wiki that systematically breaks down ISO 19650 (information management for the built environment) and related guidance (EIR/AIR, BEP, MIDP/TIDP, CDE workflows) into applicable project methods, and converts validated methods into reusable Claude Skills.

The repository is **not a code/build project** — it's a knowledge management system. Work here involves creating and maintaining markdown wiki pages following `schema.md`, and extracting methodologies into deployable Skills that support BIM requirement analysis, BEP review, CDE assessment, model checking, and compliance evidence.

**Core thesis** (from `purpose.md`): Any ISO 19650 requirement can be operationalized when translated from standard language into clear components — information purpose → roles and responsibility → input requirements → process → control points → compliance evidence → deliverables. If a process can be described as steps, conditions, diagnostic questions, and acceptance criteria, it can become a Claude Skill.

## Key Files and Purpose

- **`purpose.md`** — Research question, hypothesis, sub-questions, scope, methodology, skill candidate areas, success criteria (read this first)
- **`schema.md`** — Page types, naming conventions, frontmatter format, ten-question analysis framework, tag categories
- **`wiki/index.md`** — Central index of all pages, grouped by type
- **`wiki/log.md`** — Activity log in reverse chronological order
- **`wiki/overview.md`** — High-level summary of current state and research focus areas

## Directory Structure

```
wiki/
├── entities/        # ISO 19650 parts, EIR/AIR/BEP/MIDP/TIDP, roles, CDE platforms, orgs
├── concepts/         # LOIN, container states, CDE workflow, classification, naming convention
├── sources/          # Standard clauses, guidance docs, templates, case studies
├── queries/           # Open applicability/responsibility questions
├── comparisons/       # CDE platforms, BEP templates, LOIN approaches compared
├── findings/          # Empirical results from applying methods to real documents
├── methodology/       # Step-by-step methods extracted from standards (Skill candidates)
├── synthesis/         # Cross-cutting conclusions across standards/guidance
├── thesis/            # Working hypotheses about effective implementation
├── skills/            # Validated, deployable Claude Skills
├── index.md
├── log.md
└── overview.md
```

## Ten-Question Analysis Framework

When ingesting ANY new source (ISO clause, EIR/BEP template, guidance doc, case study), apply this framework from `purpose.md`:

| # | Question | Maps to |
|---|----------|---------|
| 1 | What information-management problem does this solve? | `wiki/concepts/` or entity description |
| 2 | What stage/org/role/information-type does it apply to? | Entity/concept "applicability" section |
| 3 | What steps, decisions, control points does it describe? | `wiki/methodology/` (Skill candidate) |
| 4 | What inputs, outputs, evidence are needed? | Methodology "evidence" section |
| 5 | What principles recur across documents? | `wiki/concepts/` or entity "principles" section |
| 6 | What mistakes/anti-patterns commonly occur? | `wiki/findings/` |
| 7 | How does this become a checklist/template/rule/workflow? | Methodology "operationalization" section |
| 8 | Can it be expressed as numbered steps + criteria? | If YES → `wiki/skills/` candidate |
| 9 | What role/moment/output would the Skill support? | Skill page `trigger:` and description |
| 10 | How should this be validated on a real project? | Skill page `tested_in:` plan |

## Adding New Pages: Workflow

1. **Choose page type** based on `schema.md`
2. **Create file** in appropriate directory with kebab-case naming
3. **Add required frontmatter** (type, title, tags, related, created, updated)
4. **Add type-specific frontmatter** (see schema.md) — include `clause_refs:` for traceability
5. **Apply ten-question framework** if the page is a source
6. **Update `wiki/index.md`** with new entry
7. **Update `wiki/log.md`** with date and action
8. **Cross-reference** with `[[wikilinks]]` to related pages

## Auto-Ingest Pipeline

> [!IMPORTANT]
> **Mandatory Batch Auto-Ingest Directive**: Whenever the user asks to perform Auto-Ingest (or refers to a new lesson file), the AI **MUST NOT** stop at just the single newest file. The AI must scan `wiki/sources/`, cross-reference with `wiki/overview.md` and `wiki/index.md`, and **AUTO-INGEST ALL LESSONS/SOURCES THAT HAVE NOT YET BEEN INGESTED INTO THE KNOWLEDGE SPACE**.

When content lands in `raw/sources/` or `wiki/sources/`:

1. **Scan & Identify**: List all files in `wiki/sources/` and compare with `wiki/overview.md` / `wiki/index.md` to identify all pending/un-ingested lessons.
2. **Apply ten-question framework**: Answer all 10 questions and add YAML frontmatter + clause references to every un-ingested source.
3. **Extract entities**: (documents, roles, systems, standards parts) → create/update entity pages in `wiki/entities/`.
4. **Extract concepts**: (LOIN, CDE states, classification schemes, BIM dimensions) → create/update concept pages in `wiki/concepts/`.
5. **Extract methodologies**: (numbered steps, control points) → create methodology pages in `wiki/methodology/` (mark `skill_status: candidate`).
6. **Map to existing pages**: Search index for related content, avoid duplicate entities, and update cross-references with `[[wikilinks]]`.
7. **Register**: Update `wiki/index.md`, append to `wiki/log.md`, and update counts/status in `wiki/overview.md`.
8. **Rebuild Graph**: Run `graphify update .` to synchronize the knowledge graph.

## Skill Extraction Pipeline

When a methodology is identified as a Skill candidate (see `purpose.md` → Skill Candidate Areas):

1. **Verify** the method has clear, numbered steps, trigger conditions, and completion criteria
2. **Create methodology page** in `wiki/methodology/` with full steps and clause traceability
3. **Draft skill page** in `wiki/skills/` with trigger, required inputs, workflow, guardrails, output format
4. **Link** methodology ← source, skill ← methodology
5. **Test** the skill on real project documents (record in `tested_in:` frontmatter)
6. **Update** effectiveness rating based on test results, compare against expert/approved process
7. **Deploy** if effectiveness is medium/high → copy to `.claude/skills/`

### Priority Skill Candidates (from `purpose.md`)

- EIR/AIR analysis → Requirement Register generation
- BEP review against ISO 19650 + project requirements
- Responsibility Matrix creation/checking
- MIDP/TIDP build + linkage checking
- CDE workflow / status / revision / approval-gate assessment
- Naming convention + metadata checking for information containers
- Model QA/QC checklist by project stage
- Information requirement → Revit parameter / IFC property mapping
- Level of Information Need assessment per use case
- Pre-issue/publish/handover readiness checking
- Non-conformance analysis + corrective action suggestions
- Project-specific BIM ISO implementation plan generation
- Lesson-learned → rule/guardrail/reusable workflow conversion

## Integration with External Tools

- **Obsidian**: `wiki/` works as an Obsidian vault. Use obsidian-skills for wikilinks, callouts, frontmatter, embeds.
- **graphify**: Knowledge graph at `graphify-out/`. Consult `GRAPH_REPORT.md` for god nodes, communities, and surprising connections before deep-diving into standard text.
- **Content extraction (`scripts/`)**: for parsing PDF standards text, Word EIR/BEP templates, Excel responsibility matrices.

### graphify (`graphify-out/`)

- Before answering relationship questions → read `GRAPH_REPORT.md`
- After wiki changes → run `/graphify . --update`
- To sync insights → run `/graphify-to-wiki`

### Content Extraction (`scripts/`)

| Command | Purpose |
|---------|---------|
| `/extract-content` | Scan `raw/` for all new files (PDF standards, DOCX templates, XLSX matrices) |
| `/graphify .` | Build/update knowledge graph |
| `/graphify-to-wiki` | Sync graph → wiki pages |

## Tag Strategy

| Category | Values |
|----------|--------|
| **topic** | `information-management`, `eir-air`, `bep`, `cde`, `midp-tidp`, `roles-responsibility`, `loin`, `naming-classification`, `model-checking`, `coordination`, `handover`, `compliance` |
| **stage** | `assessment-need`, `invitation-tender`, `mobilization`, `collaborative-production`, `operational` |
| **priority** | `critical`, `high`, `medium`, `low` |
| **confidence** | `high`, `medium`, `low`, `speculative` |

## Guardrails (from `purpose.md` scope)

- Do not assert "ISO compliant" without a named clause/criterion and project evidence
- Do not apply the same template mechanically to every project without considering contract, stage, and information requirements
- Software how-to content is out of scope unless tied directly to an ISO 19650 requirement
- Legal interpretation is out of scope — flag for legal/certification review instead of asserting compliance

## Maintenance Tasks

- Update `wiki/overview.md` metrics as sources/pages are ingested
- Keep `wiki/index.md` in sync with newly created pages
- Update `wiki/log.md` after every action
- Review methodology pages for skill extraction opportunities
- Periodically run `/graphify-to-wiki` to discover cross-standard connections
- Test and deploy skills from `wiki/skills/` to `.claude/skills/`
