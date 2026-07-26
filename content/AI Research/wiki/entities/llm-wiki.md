---
type: entity
title: "LLM Wiki (nashsu/llm_wiki)"
tags: [knowledge-base, desktop-app, llm-wiki-pattern, knowledge-graph, rag, web-clipper, tauri, react]
related: ["[[andrej-karpathy-skills]]", "[[karpathy-llm-wiki-pattern]]", "[[llm-knowledge-base]]"]
created: 2026-04-29
updated: 2026-04-29
repo_url: "https://github.com/nashsu/llm_wiki"
author: "nashsu"
language: [TypeScript, Rust, JavaScript]
stars: 4400
license: "GPL-3.0"
last_commit: 2026-04-28
use_case: [llm-knowledge-base, personal-wiki, document-ingestion, knowledge-graph-visualization]
status: active
---

# LLM Wiki

**Summary**: Cross-platform desktop app that turns documents into an organized, interlinked knowledge base automatically using LLMs. Based on Andrej Karpathy's LLM Wiki pattern, with major extensions.

**Sources**: [[github---nashsu-llm-wiki-llm-wiki-is-a-cross-platf-20260429]]

---

## What It Does

LLM Wiki replaces traditional RAG (retrieve-and-answer from scratch each time) with a **persistent, incrementally-built wiki**. Knowledge is compiled once and kept current — not re-derived on every query.

## Key Features

| Feature | Description |
|---------|-------------|
| Two-Step CoT Ingest | Analysis → Generation split for higher quality wiki pages |
| 4-Signal Knowledge Graph | Direct links, source overlap, Adamic-Adar, type affinity |
| Louvain Community Detection | Automatic knowledge cluster discovery |
| Chrome Web Clipper | One-click capture with auto-ingest (3s poll interval) |
| Vector Semantic Search | Optional LanceDB embedding search (58% → 71% recall) |
| Deep Research | LLM-generated topics → Tavily web search → auto-ingest |
| Multi-format Ingest | PDF, DOCX, PPTX, XLSX, images, video/audio, web clips |
| Review System | Async human-in-the-loop judgment queue |
| Graph Insights | Surprising connections + knowledge gap detection |
| Multi-conversation Chat | Persistent chat sessions with cited references |
| Multimodal Images | Extract images from PDF, caption with vision LLM |

## Strengths

- **Full desktop application** with polished UI (three-column layout, icon sidebar, resizable panels)
- **Knowledge graph with relevance model** — goes beyond simple wikilinks into a weighted multi-signal relevance engine
- **Two-step ingest** produces significantly better wiki quality than single-pass approaches
- **Web Clipper extension** enables seamless capture-to-wiki workflow
- **Deep Research** can autonomously fill knowledge gaps via web search
- **Cross-platform** (macOS, Windows, Linux) with CI/CD automated builds
- **Active development** — 359 commits, 20 releases, latest v0.4.3 (Apr 2026)
- **Multi-format support** — handles most common document types natively
- **Optional vector search** boosts recall without being required

## Weaknesses

- **GPL-3.0 license** — restricts use in proprietary/commercial projects
- **Single contributor** — bus factor of 1, long-term maintenance risk
- **Requires LLM API key** — depends on external paid LLM services (OpenAI, Anthropic, etc.)
- **No mobile app** — desktop only (Tauri)
- **Relatively new** — project started Apr 2026, may have undiscovered bugs
- **Tavily API dependency** for Deep Research feature

## Tech Stack

Tauri v2 (Rust) | React 19 + TypeScript + Vite | shadcn/ui + Tailwind CSS v4 | sigma.js + graphology + ForceAtlas2 | LanceDB | Zustand | react-i18next

## Related Pages

- [[andrej-karpathy-skills]]
- [[karpathy-llm-wiki-pattern]]
- [[llm-knowledge-base]]
