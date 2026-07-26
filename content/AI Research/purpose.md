# Project Purpose — GitHub Repo Knowledge Base

## Research Question

> Given the vast ecosystem of open-source tools and libraries on GitHub, which repositories best fit a specific use case, and how do similar-purpose repos compare in terms of strengths, weaknesses, and trade-offs?

## Hypothesis / Working Thesis

> By systematically capturing, ingesting, and cross-referencing GitHub repositories into a structured knowledge base, we can build a queryable decision-support system that instantly recommends the best-fit tool for any given purpose — backed by pre-analyzed comparisons rather than ad-hoc evaluation.

## Background

The GitHub ecosystem contains millions of repositories addressing overlapping use cases. Developers and researchers frequently face the "paradox of choice" — multiple tools solve the same problem, but comparing them requires significant time and effort scattered across README files, blog posts, and community discussions.

This project addresses the gap by creating a **centralized, curated knowledge base** that:
- Aggregates useful GitHub repos captured during daily browsing via the **LLM Wiki Clipper** web extension
- Automatically processes clipped content through a two-step ingest pipeline
- Maps new repos against existing ones with similar purposes
- Produces structured comparisons and best-fit recommendations

The approach is inspired by Andrej Karpathy's LLM Wiki pattern, adapted specifically for GitHub repository analysis and tool selection.

## Sub-questions

1. How do we automatically classify and tag a newly captured repo by its primary purpose/use case?
2. How do we identify and map repos that share similar functionality or solve the same problem?
3. What criteria should be used to compare repos (stars, maintenance activity, documentation quality, community size, performance benchmarks, API design, etc.)?
4. How do we synthesize comparison results into a clear best-fit recommendation for a given use case?

## Scope

**In scope:**
- GitHub repositories captured via LLM Wiki Clipper web extension
- Auto-ingest pipeline triggered by clipped content (two-step: raw capture → wiki processing)
- Mapping new repos to existing ones with shared purpose/functionality
- Automated comparison and pros/cons analysis of similar repos
- Best-fit tool recommendation based on accumulated knowledge
- User query interface returning fast, accurate answers from the knowledge space

**Out of scope:**
- Content from non-GitHub sources (blog posts, documentation sites, papers, etc. that are not GitHub repos)
- Private/enterprise repositories not publicly accessible
- Runtime benchmarking or hands-on testing of repos (analysis is based on available metadata and documentation)
- Source code auditing or security vulnerability scanning

## Methodology

- **Capture**: Use LLM Wiki Clipper extension to clip GitHub repos of interest during daily browsing
- **Auto-Ingest**: Clipped content automatically triggers the two-step ingest pipeline:
  1. Raw source is saved to `raw/sources/` (immutable)
  2. AI processes the source → creates entity page, extracts metadata, identifies use case categories
- **Mapping**: Each ingested repo is cross-referenced against existing entities by tags and use case categories to find similar-purpose repos
- **Comparison**: When ≥2 repos share a use case, a `wiki/comparisons/` page is created or updated with structured pros/cons analysis
- **Decision**: Comparison pages culminate in a best-fit recommendation with clear reasoning
- **Query**: User queries are answered by traversing the knowledge graph — index → relevant entity/comparison/synthesis pages → synthesized response with citations

## Success Criteria

- **Auto-ingest works end-to-end**: Repo captured by LLM Wiki Clipper → automatically ingested into wiki with proper entity page, tags, and metadata
- **Mapping is accurate**: Newly ingested repos are correctly matched to existing repos that serve similar purposes
- **Comparisons are generated**: When similar repos exist, a structured comparison (pros, cons, trade-offs) is automatically produced
- **Decisions are clear**: Each comparison results in a best-fit recommendation with justification
- **Reports are generated**: Comparison and decision results are available as readable wiki pages
- **Query response is fast and accurate**: User can ask "What is the best tool for X?" and receive an answer grounded in the knowledge base with cited sources

## Current Status

> Initialized — project structure created, first source captured (andrej-karpathy-skills). Ingest pipeline and comparison workflow to be built out as more repos are captured.
