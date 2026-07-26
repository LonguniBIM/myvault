# Wiki Schema — HTU Trading

## Page Types

| Type | Directory | Purpose |
|------|-----------|---------|
| entity | `wiki/entities/` | Trading tools, platforms, indicators, people, organizations |
| concept | `wiki/concepts/` | Strategies, patterns, methodologies, frameworks |
| source | `wiki/sources/` | Articles, papers, tutorials, market reports |
| query | `wiki/queries/` | Open questions under investigation |
| comparison | `wiki/comparisons/` | Side-by-side analysis of strategies or tools |
| finding | `wiki/findings/` | Empirical results, backtesting outcomes |
| synthesis | `wiki/synthesis/` | Cross-cutting conclusions across multiple sources |
| thesis | `wiki/thesis/` | Working hypotheses about market behavior |
| methodology | `wiki/methodology/` | Trading methods, protocols, checklists — Skill candidates |
| skill | `wiki/skills/` | Validated Claude Skills derived from methodology pages |

## Naming Conventions

- General: `kebab-case.md` (e.g., `moving-average-crossover.md`)
- Sources: `author-year-slug.md` (e.g., `murphy-1999-technical-analysis.md`)
- Queries: question as slug (e.g., `best-indicator-for-trend-following.md`)

## Frontmatter

All pages require:

```yaml
---
type: entity | concept | source | query | comparison | synthesis | finding | thesis | methodology
title: Human-readable title
tags: []
related: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Type-specific additions:
- **Sources**: `authors: []`, `year: YYYY`, `url: ""`, `venue: ""`
- **Findings**: `source: "[[source-slug]]"`, `confidence: low | medium | high`, `replicated: true | false | null`, `layer: caution | structure | invalidation | execution`
- **Theses**: `confidence: low | medium | high`, `status: speculative | supported | refuted | settled`
- **Methodology**: `skill_status: candidate | validated | deployed`, `invalidation_complete: true | false`, `layers_covered: []`
- **Skills**: `trigger: ""`, `source_methodology: "[[methodology-slug]]"`, `tested_in: []`, `effectiveness: low | medium | high`

## Tag Strategy

| Category | Values |
|----------|--------|
| **layer** | `caution`, `structure`, `invalidation`, `execution` |
| **topic** | `killzone`, `swing`, `range-type`, `expansion`, `reversal`, `continuation`, `bias`, `signature`, `objective`, `news-protocol`, `session`, `strategy`, `backtesting`, `risk-management` |
| **market** | `forex`, `crypto`, `stocks`, `commodities`, `options`, `futures` |
| **timeframe** | `scalping`, `day-trading`, `swing`, `position`, `long-term` |
| **priority** | `critical`, `high`, `medium`, `low` |
| **confidence** | `high`, `medium`, `low`, `speculative` |

## Index Format

`wiki/index.md` lists all pages grouped by type. Each entry:
- [[page-slug]] — one-line description

## Log Format

`wiki/log.md` records activity in reverse chronological order.

## Cross-referencing Rules

- Use `[[wikilinks]]` for internal cross-references
- Entities and concepts must appear in `wiki/index.md`
- Findings link to their source via `source:` frontmatter
- Thesis pages reference supporting/refuting findings via `related:`

## Contradiction Handling

When sources contradict each other:
1. Note the contradiction in the relevant concept or entity page
2. Create or update a query page to track the open question
3. Link both sources from the query page
4. Resolve in a synthesis page once sufficient evidence exists
