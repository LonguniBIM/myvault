---
type: concept
title: "Karpathy LLM Wiki Pattern"
tags: [llm-wiki-pattern, karpathy, knowledge-base, methodology]
related: ["[[llm-wiki]]", "[[andrej-karpathy-skills]]", "[[llm-knowledge-base]]"]
created: 2026-04-29
updated: 2026-04-29
---

# Karpathy LLM Wiki Pattern

**Summary**: A methodology for building personal knowledge bases using LLMs, originally described by Andrej Karpathy in `llm-wiki.md`. Human curates sources and asks questions; LLM maintains the wiki.

---

## Core Architecture

- **Three layers**: Raw Sources (immutable) → Wiki (LLM-generated) → Schema (rules & config)
- **Three operations**: Ingest, Query, Lint
- `index.md` as content catalog and LLM navigation entry point
- `log.md` as chronological operation record
- `[[wikilink]]` syntax for cross-references
- YAML frontmatter on every wiki page
- Obsidian compatibility

## Key Principle

> Human curates, LLM maintains.

The human decides *what* to add and *what questions* to ask. The LLM handles the mechanical work of creating pages, cross-referencing, updating indexes, and maintaining consistency.

## Implementations

| Repo | Approach |
|------|----------|
| [[llm-wiki]] | Full desktop app with knowledge graph, web clipper, deep research |
| [[andrej-karpathy-skills]] | Guidelines file only (not a wiki implementation, but references the pattern) |

## Related Pages

- [[llm-wiki]]
- [[andrej-karpathy-skills]]
- [[llm-knowledge-base]]
