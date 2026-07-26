# Wiki Schema — Claude Code Mastery

## Page Types

| Type | Directory | Purpose |
|------|-----------|---------|
| entity | wiki/entities/ | Named things: tools (Claude Code, MCP servers), people (Anthropic team), features, configs |
| concept | wiki/concepts/ | Ideas, techniques: prompt patterns, context engineering, skill design, agent patterns |
| source | wiki/sources/ | Documentation, blog posts, tutorials, videos, GitHub repos |
| query | wiki/queries/ | Open questions: "How to optimize X?", "What's the best approach for Y?" |
| comparison | wiki/comparisons/ | Side-by-side: different approaches, tools, configurations |
| synthesis | wiki/synthesis/ | Cross-cutting conclusions from multiple sources |
| thesis | wiki/thesis/ | Working hypotheses about effective Claude Code usage |
| methodology | wiki/methodology/ | Step-by-step methods extracted from sources (Skill candidates) |
| finding | wiki/findings/ | Empirical results from testing approaches |
| skill | wiki/skills/ | Validated Skills ready for deployment (.md format documentation) |

## Naming Conventions

- Files: `kebab-case.md`
- Entities: match official name (e.g., `claude-code.md`, `mcp-server.md`)
- Concepts: descriptive noun phrases (e.g., `context-engineering.md`, `skill-design-pattern.md`)
- Sources: `author-year-slug.md` or `domain-slug-date.md` (e.g., `anthropic-2026-claude-code-docs.md`)
- Queries: question as slug (e.g., `how-to-optimize-token-usage.md`)
- Methodologies: method name (e.g., `source-to-skill-pipeline.md`)
- Skills: skill name (e.g., `debugging-workflow.md`, `code-review-checklist.md`)

## Frontmatter

All pages must include YAML frontmatter:

```yaml
---
type: entity | concept | source | query | comparison | synthesis | thesis | methodology | finding | skill
title: Human-readable title
tags: []
related: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### Tag Categories

| Category | Values | Usage |
|----------|--------|-------|
| topic | `setup`, `workflow`, `optimization`, `debugging`, `skills`, `memory`, `mcp`, `hooks`, `permissions`, `context`, `agents`, `prompts` | Primary subject area |
| priority | `critical`, `high`, `medium`, `low` | Importance for mastery |
| confidence | `high`, `medium`, `low`, `speculative` | How well-validated the content is |

### Type-Specific Frontmatter

**Source pages:**
```yaml
authors: []
year: YYYY
url: ""
venue: ""          # docs.anthropic.com, blog, github, youtube, etc.
skill_potential: true | false    # Can this become a numbered-step Skill?
```

**Methodology pages:**
```yaml
steps: 5                         # Number of steps in the method
source: "[[source-slug]]"        # Where this method was extracted from
skill_status: candidate | drafted | tested | deployed
```

**Skill pages:**
```yaml
trigger: ""                      # When to invoke this skill
steps: 5                         # Number of steps
tested_in: []                    # Projects where this was tested
effectiveness: low | medium | high
```

**Thesis pages:**
```yaml
confidence: low | medium | high
status: speculative | supported | refuted | settled
```

**Finding pages:**
```yaml
source: "[[source-slug]]"
confidence: low | medium | high
replicated: true | false | null
```

**Comparison pages:**
```yaml
subjects: []                     # Items being compared
best_fit: "[[entity-slug]]"
best_fit_reason: ""
```

## Index Format

`wiki/index.md` lists all pages grouped by type. Each entry:
```
- [[page-slug]] — one-line description
```

## Log Format

`wiki/log.md` records activity in reverse chronological order:
```
## YYYY-MM-DD

- Action taken / finding noted
```

## Cross-referencing Rules

- Use `[[page-slug]]` syntax to link between wiki pages
- Every entity and concept should appear in `wiki/index.md`
- Queries link to the sources and concepts they draw on
- Synthesis pages cite all contributing sources via `related:`
- Findings link back to their source via the `source:` frontmatter field
- Methodology pages link to the skill they generated (if any)
- Skill pages link back to methodology and source

## Six-Question Analysis Framework

When ingesting any new source, answer these questions:

1. **Problem**: What does this document solve?
2. **Method**: What numbered steps does the author prescribe?
3. **Principles**: What recurring themes or rules appear throughout?
4. **Warnings**: What mistakes does the author caution against?
5. **Questions**: What diagnostic questions does the author pose?
6. **Skill Test**: Can the method be expressed as numbered steps → Skill candidate?

Record answers in the source page and extract methodologies to `wiki/methodology/`.

## Contradiction Handling

When sources contradict each other:
1. Note the contradiction in the relevant concept or entity page
2. Create or update a query page to track the open question
3. Link both sources from the query page
4. Resolve in a synthesis page once sufficient evidence exists
5. If both approaches work in different contexts, create a comparison page
