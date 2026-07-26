---
type: overview
title: GitHub Repo Knowledge Base — Project Overview
tags: [github, knowledge-base, tool-comparison, repo-analysis]
related: []
created: 2026-04-28
updated: 2026-04-29

---

# Overview

This wiki is a **curated knowledge base of GitHub repositories**, designed to help quickly identify the best-fit tool for any given use case.

## How It Works

1. **Capture** — User clips interesting GitHub repos via the **LLM Wiki Clipper** web extension
2. **Auto-Ingest** — Clipped content triggers a two-step pipeline: raw archival → AI-powered entity extraction and categorization
3. **Mapping** — Each new repo is matched against existing entries that serve a similar purpose
4. **Comparison** — Repos with overlapping use cases are compared (pros, cons, trade-offs) in dedicated comparison pages
5. **Decision** — Comparisons produce a best-fit recommendation with reasoning
6. **Query** — User asks a question → the system returns an answer grounded in the knowledge base

## Current State

| Metric | Count |
|--------|-------|
| Repos ingested | 5 |
| Entity pages | 5 |
| Concept pages | 4 |
| Comparisons | 2 |
| Decisions made | 2 |

### Repos by Use Case

| Use Case | Repos |
|----------|-------|
| LLM Knowledge Base / Personal Wiki | [[llm-wiki]], [[graphify]] |
| LLM Agent Skills (behavioral) | [[andrej-karpathy-skills]] |
| LLM Agent Skills (domain knowledge) | [[obsidian-skills]], [[graphify]] |
| Agentic Development Environment | [[warp]] |

### Comparisons

- [[agent-skills-for-llm-coding]] — andrej-karpathy-skills vs obsidian-skills vs graphify → **complementary, use all three for maximum agent capability**
- [[llm-knowledge-base-tools]] — llm-wiki vs graphify → **graphify for developers/agents, llm-wiki for general document management**

## Scope

Only GitHub repositories. Non-GitHub sources are out of scope.

## Key Directories

- `wiki/entities/` — One page per repo (metadata, purpose, strengths, weaknesses)
- `wiki/comparisons/` — Side-by-side analysis of repos solving the same problem
- `wiki/sources/` — Raw source summaries from LLM Wiki Clipper captures
- `wiki/synthesis/` — Cross-cutting insights and final recommendations
