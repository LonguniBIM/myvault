---
type: source
title: "nashsu/llm_wiki — Cross-platform LLM-powered knowledge base builder"
created: 2026-04-29
updated: 2026-04-29
sources: ["github---nashsu-llm-wiki-llm-wiki-is-a-cross-platf-20260429.md"]
authors: [nashsu]
year: 2026
url: "https://github.com/nashsu/llm_wiki"
tags: [llm-wiki, knowledge-base, desktop-app, tauri, knowledge-graph, rag, web-clipper]
related: ["[[llm-wiki]]", "[[andrej-karpathy-skills]]", "[[llm-knowledge-base]]", "[[karpathy-llm-wiki-pattern]]"]
---

# nashsu/llm_wiki — Source Summary

**Summary**: LLM Wiki is a cross-platform desktop application (Tauri v2 + React + TypeScript) that turns documents into an organized, interlinked knowledge base automatically. Built on Andrej Karpathy's LLM Wiki pattern, it replaces traditional RAG with persistent, incrementally-built wiki pages.

**Key Takeaways**:

1. **Two-Step Chain-of-Thought Ingest** — Splits ingestion into Analysis (extract entities, find contradictions) then Generation (create wiki pages with cross-references). Significantly better quality than single-step.
2. **4-Signal Knowledge Graph** — Relevance model using direct links, source overlap, Adamic-Adar, and type affinity. Visualized with sigma.js + ForceAtlas2.
3. **Louvain Community Detection** — Automatic discovery of knowledge clusters with cohesion scoring.
4. **Chrome Web Clipper** — One-click web page capture with auto-ingest into knowledge base (polls every 3s).
5. **Vector Semantic Search** — Optional embedding-based retrieval via LanceDB, improving recall from 58.2% to 71.4%.
6. **Deep Research** — LLM-generated search topics → Tavily web search → auto-ingest results into wiki.
7. **Multi-format Support** — PDF, DOCX, PPTX, XLSX, images, video/audio, web clips.
8. **Review System** — Async human-in-the-loop: LLM flags items for human judgment during ingest.
9. **Multimodal Image Ingestion** — Extract images from PDFs, generate captions via vision LLM.

**Tech Stack**: Tauri v2 (Rust) | React 19 + TypeScript + Vite | shadcn/ui + Tailwind CSS v4 | sigma.js + graphology | LanceDB | Zustand | react-i18next

**Metrics**: 4.4k stars | 533 forks | 359 commits | 20 releases | 1 contributor | License: GPL v3 | Last release: v0.4.3 (Apr 28, 2026)
