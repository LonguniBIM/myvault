# Research Log

## 2026-05-10

### Ingestion: Multi-Source Markdown Batch & Graph Sync

**Sources**: 16 markdown files in `raw/sources/` (Certified, Claude Code, Design, Skills, etc.)  
**Method**: Batch extraction via `extract_content.py` + Graphify update + manual classification

**Actions completed**:
- ✅ Extracted 16 markdown files into `raw/extracts/` and created wiki source pages
- ✅ Updated Knowledge Graph with 110 nodes and 110 edges across 13 communities
- ✅ Created 5 new entity pages: `design-md.md`, `skill-creator.md`, `makemyskill.md`, `canva.md`, `figma.md`
- ✅ Created 2 new concept pages: `convert-one-methodology.md`, `dictation-prompting-workflow.md`
- ✅ Updated `wiki/index.md` with 23 new entries (Sources, Entities, Concepts)
- ✅ Cross-linked new entities/concepts based on Community 0 and Community 8 clusters

**Key batch findings**:
- The "Claude Design Pipeline" ([[claude-cowork]] → [[design-md]] → [[claude-design]]) is a core abstraction for brand consistency
- The "Skills Creation Ecosystem" ([[skill-creator]] + [[makemyskill]] + [[skill-md]]) is the primary driver for team-wide efficiency
- Voice input ([[dictation-prompting-workflow]]) reduces prompting friction and enables higher context density

**Next steps**:
- Apply six-question framework to the high-priority extracted sources
- Extract methodologies from `Claude For Teams` (5-Day Playbook)
- Investigate remaining secondary nodes from graphify-out
- Run `/graphify . --update` to incorporate these new pages into the graph

---

## 2026-05-10

### Ingestion: Claude Code (Ruben Hassid)

**Source**: `raw/sources/Claude Code.md` / https://ruben.substack.com/p/claude-code  
**Published**: 2026-03-19  
**Method**: Manual six-question framework analysis of markdown source

**Actions completed**:
- Applied six-question framework — all 6 questions answered
- Created detailed source page: `ruben-hassid-2026-claude-code.md`
- Extracted 3 entities: GitHub, VS Code, Wispr Flow
- Extracted 4 concepts: Vibecoding, Screenshot-First Prompting, Permission Friction, Project Memory File
- Extracted 1 methodology marked as skill candidate: Claude Code for Non-Coders Workflow
- Updated existing Claude Code entity with non-coder workflow connections
- Updated wiki/index.md with new entries

**Key findings from this source**:
- Claude Code can be framed for non-coders as English-driven project management rather than programming
- Screenshot-first prompting is a practical shortcut for UI generation and bug repair
- Permission prompts are a major workflow bottleneck; VS Code + bypass permissions is presented as the faster route
- CLAUDE.md functions as durable project memory and supports the existing files-replace-prompts thesis
- Non-coders should treat live website testing as their code review substitute

**Skill candidate assessment**:
- **Skill name**: `claude-code-for-non-coders-workflow`
- **Potential**: HIGH — clear setup, prompt template, iteration loop, and failure recovery rule
- **Steps**: 7
- **Deployment readiness**: Candidate, needs real-world testing before deployment

---

## 2026-05-09

### Ingestion: Graphify Knowledge Graph Sync

**Source**: `d:\wiki\Claude\graphify-out\` (110 nodes, 110 edges, 13 communities)  
**Method**: AST-based graph extraction + god node prioritization + Obsidian wiki generation

**Actions completed**:
- ✅ Parsed graphify output (graph.json, GRAPH_REPORT.md)
- ✅ Classified 27 qualified nodes (≥3 edges, EXTRACTED/INFERRED confidence)
- ✅ Identified 9 god nodes (most-connected abstractions)
- ✅ Created 7 new wiki pages from god nodes:
  - 4 entity pages: `claude-overview.md`, `claude-code.md`, `claude-design.md`, `claude-skills.md`
  - 2 thesis pages: `claude-is-six-tools.md`, `files-replace-prompts.md`
  - 1 concept page: `token-saving-habits.md`
  - 1 source page: `cowork-april-2026-update.md`
- ✅ Updated existing entity: `claude-cowork.md` with graph metadata
- ✅ Updated wiki/index.md with 9 new entries + god node annotations
- ✅ Cross-linked all pages with wikilinks and betweenness centrality notes

**Files created/updated**: 8
- 4 new entity pages
- 2 new thesis pages
- 1 new concept page
- 1 new source page
- 1 updated entity page

**Key findings from graph**:
- **God nodes** (8+ edges): Claude Code, Claude Skills — core abstractions
- **Cross-community bridges** (high betweenness centrality):
  - Claude Cowork (0.437) — connects Brand & Design, Cowork Tooling, Personal Context, Code Workflow
  - Claude Cowork (intro) (0.383) — connects Surface Areas to Cowork Workflows
  - Files Replace Prompts (0.360) — connects Brand & Design to Surface Areas
- **13 communities detected**: Brand & Design, Cowork Tooling, Personal Context, Cowork Workflows, Claude vs Other AI, Claude Code Features, Vibe Coding Stack, Claude Code Workflow, Skills Ecosystem, Claude Surface Areas, Anthropic Certifications, Ruben & Anthropic, Podcast
- **Knowledge gaps**: 63 isolated nodes (≤1 connection) — possible missing edges or undocumented components
- **Surprising connections** (INFERRED): 
  - 23 Token-Saving Habits ↔ Token (concept)
  - Claude Skills ↔ /negotiation-prep skill
  - Voice Profile ↔ Claude Skills

**Wikilink resolution**:
- ✅ All new pages use Obsidian wikilinks `[[page-slug]]`
- ✅ All god nodes linked in index.md
- ✅ No dangling links in new pages

**Next steps**:
- Create pages for remaining 18 qualified nodes (secondary tier)
- Investigate 63 isolated nodes for missing edges
- Verify 2 INFERRED relationships (Claude Skills connections)
- Run `graphify update .` to re-index wiki and incorporate new pages

---

## 2026-05-09

### Ingestion: Certified - Getting Free Claude Certifications (Ruben Hassid)

**Source**: https://ruben.substack.com/p/im-claude-certified  
**Published**: 2026-05-06  
**Method**: Manual six-question framework analysis of markdown source

**Actions completed**:
- ✅ Applied six-question framework — all 6 questions answered
- ✅ Created detailed source page with full analysis: `certified-claude-certifications.md`
- ✅ Extracted 1 new entity: Anthropic Academy (anthropic.skilljar.com)
- ✅ Extracted 2 new concepts: Certification Strategy, AI Fluency Framework (4Ds)
- ✅ Extracted 1 methodology marked as skill candidate: Get Claude Certified
- ✅ Created 4 additional entity pages for unresolved wikilinks:
  - `claude.md` — Claude AI assistant
  - `anthropic.md` — Anthropic organization
  - `claude-cowork.md` — Claude Cowork desktop app
  - `ruben-hassid.md` — Author/educator
- ✅ Created 2 additional concept pages for unresolved wikilinks:
  - `ai-fluency.md` — AI Fluency concept
  - `taste-training.md` — Taste Training concept
- ✅ Cross-linked all pages with wikilinks
- ✅ Updated wiki/index.md with 9 new entries
- ✅ Updated wiki/log.md

**Files created**: 10
- 1 source page: `certified-claude-certifications.md`
- 5 entity pages: `anthropic-academy.md`, `claude.md`, `anthropic.md`, `claude-cowork.md`, `ruben-hassid.md`
- 4 concept pages: `certification-strategy.md`, `ai-fluency-framework.md`, `ai-fluency.md`, `taste-training.md`
- 1 methodology page: `get-claude-certified.md`
- 1 skill page: `get-claude-certified.md`

**Key findings from this source**:
- Only 3 real Claude certifications exist (all free via Anthropic Academy)
- All paid "Claude Certification" courses online are scams
- AI Fluency course is the most valuable (3 hours, teaches 4Ds framework)
- Market signal: <2% of people have tried Claude Pro; certification proves hands-on experience
- Career impact: Workers with AI skills earn 56% wage premium (PwC 2025), up from 25% in 2024
- 78% of organizations used AI in 2024 (Stanford AI Index 2025), up from 55% in 2023
- AI Fluency Vocabulary Cheat Sheet is the most valuable artifact (included in course)

**Skill candidate assessment**:
- **Skill name**: `get-claude-certified`
- **Potential**: HIGH — Clear, sequential steps with specific URLs and time estimates
- **Steps**: 4 main steps (access platform, take 3 certifications) + LinkedIn integration
- **Time estimate**: 6 hours total
- **Deployment readiness**: Ready for skill page creation

**Wikilink resolution**:
- ✅ All wikilinks in source page now resolve to existing entity/concept pages
- ✅ No dangling links remaining

**Next steps**:
- Test `get-claude-certified` skill in real workflow
- Consider deploying to `.claude/skills/` if validated
- Cross-reference with career development and learning strategy pages

---

## 2026-05-08

### Ingestion: Be a 10x Vibe Coder (YouTube — Chris, Craig)

**Source**: https://www.youtube.com/watch?v=li788UL1qyI
**Method**: YouTube download + Whisper transcription via `extract_content.py --url`

**Actions completed**:
- ✅ Downloaded and transcribed video (33 min, English, 100% confidence)
- ✅ Applied six-question framework — all 6 questions answered
- ✅ Created detailed source page with full analysis: `be-a-10x-vibe-coder-claude-code-cursor-mcp.md`
- ✅ Extracted 5 new entities: Cursor IDE, Context7 MCP, Supabase MCP, Bugbot, Whisper Flow
- ✅ Extracted 4 new concepts: ultrathink keyword, dual-tool workflow, background tasks, AI code review
- ✅ Extracted 1 methodology marked as skill candidate: 10x Vibe Coder Workflow
- ✅ Cross-linked all pages with wikilinks
- ✅ Updated wiki/index.md with 12 new entries
- ✅ Updated wiki/log.md

**Files created**: 12
- 1 source page
- 5 entity pages (cursor-ide, context7-mcp, supabase-mcp, bugbot, whisperflow)
- 4 concept pages (ultrathink-keyword, dual-tool-workflow, background-tasks-feature, ai-code-review)
- 1 methodology page (vibe-coder-workflow) [skill_status: candidate]
- Raw extract: `raw/extracts/be-a-10x-vibe-coder-claude-code-cursor-mcp.md`

**Key findings from this source**:
- `ultrathink` keyword boosts Claude Code reasoning with no observable token penalty
- Plan mode produces ~20%+ better output minimum
- Claude Code has UI/animation edge even when using identical Sonnet model as Cursor
- Background tasks feature gives Claude live server log access — underused
- Context7 MCP replaces unreliable URL-based documentation feeding

**Next steps**:
- Validate `ultrathink` keyword behavior (test in real project)
- Test vibe-coder-workflow skill candidate
- Consider deploying to `.claude/skills/` if validated

---

## 2026-05-06

### Ingestion: Claude for Dummies (Ruben Hassid)

**Source**: https://ruben.substack.com/p/claude-for-dummies

**Actions completed**:
- ✅ Applied six-question framework to source analysis (all 6 questions answered)
- ✅ Created detailed source page: `claude-for-dummies-source.md` with full analysis
- ✅ Extracted 2 entities: Claude AI Assistant, Anthropic Organization
- ✅ Extracted 4 core concepts: Auto-Complete at Scale, Sycophancy, Tokens, Cowork
- ✅ Extracted 2 methodologies marked as skill candidates:
  - Claude First-Week Experiments (4 experiments for new users)
  - Claude Negotiation Preparation Workflow (Gmail/Notes/Slack synthesis)
- ✅ Cross-linked all pages with wikilinks
- ✅ Updated wiki/index.md with new entries
- ✅ Updated wiki/log.md with ingestion summary

**Files created**: 9
- 1 source page (updated)
- 2 entity pages
- 4 concept pages
- 2 methodology pages

**Next steps**:
- Validate skill candidates through real-world testing
- Deploy to `.claude/skills/` if effectiveness validated
- Continue ingesting additional Claude resources

---

## Earlier (2026-05-06)

- Project initialized with Claude Code Mastery research focus
- Generated purpose.md, schema.md, CLAUDE.md from interactive wizard
- Set up directory structure: entities, concepts, sources, queries, comparisons, methodology, skills, findings, thesis, synthesis
- Installed obsidian-skills, graphify-to-wiki rule, auto-ingest pipeline
- Configured six-question analysis framework for source ingestion
- Tag strategy: topic (12 values), priority (4 levels), confidence (4 levels)
