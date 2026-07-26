---
type: comparison
title: "LLM Knowledge Base Tools — Comparison"
tags: [knowledge-base, llm-wiki, graphify, graphrag, personal-wiki]
related: ["[[llm-wiki]]", "[[graphify]]", "[[llm-knowledge-base]]"]
created: 2026-04-29
updated: 2026-04-29
use_case: "Building a persistent knowledge base from documents using LLMs"
repos: ["[[llm-wiki]]", "[[graphify]]"]
best_fit: "depends on user type — see recommendation below"
best_fit_reason: "One is a desktop app for general users, the other is a CLI/skill for developers/agents"
---

# LLM Knowledge Base Tools

**Summary**: Comparison of tools that use LLMs to automatically build structured, queryable knowledge bases from collections of documents (markdown, PDF, code, etc.).

---

## Overview

| Aspect | [[llm-wiki]] | [[graphify]] |
|--------|-------------|--------------|
| **Type** | Desktop Application (GUI) | CLI Tool / Agent Skill |
| **Primary Goal** | Human-readable personal wiki | Agent-navigable knowledge graph |
| **Tech Stack** | Node.js, React, LanceDB | Python, NetworkX, Leiden |
| **Stars** | 12k | 37.5k |
| **License** | MIT | MIT |
| **Multi-modal** | Limited (Docs/Web) | Full (Code, Docs, Image, Video) |

## Feature Matrix

| Feature | llm-wiki | graphify |
|---------|:-----:|:-----:|
| Graphical User Interface | **Yes** | No (Interactive HTML only) |
| Persistent DB/Graph | **Yes** | **Yes** |
| Code AST Analysis | No | **Yes** |
| Multi-modal (Video/Image) | No | **Yes** |
| Agent Integration (Hooks) | No | **Yes** |
| Desktop App | **Yes** | No |
| GraphRAG | No | **Yes** |

## Pros & Cons

### llm-wiki

| Pros | Cons |
|------|------|
| Accessible to non-technical users | No deep code analysis |
| Integrated chat and document viewer | Limited to document types (MD, PDF) |
| Easy to manage local LanceDB | No direct hooks for coding agents |
| Visually polished interface | Lower star count/smaller community |

### graphify

| Pros | Cons |
|------|------|
| Deep integration with coding agents | Steeper learning curve (CLI) |
| Understands code structure (classes, functions) | Heavy dependencies (Whisper, Python) |
| Multi-modal ingest (transcribes video) | No built-in document viewer/chat GUI |
| Massive community support (37.5k stars) | Initial setup can be complex |

## Best Fit Recommendation

| If you are... | Best fit |
|---------------|----------|
| A general user wanting a personal AI wiki | **[[llm-wiki]]** |
| A developer needing help navigating a codebase | **[[graphify]]** |
| Building an agentic workflow | **[[graphify]]** |
| Looking for a GUI to manage local documents | **[[llm-wiki]]** |

**Bottom line**: Use **[[llm-wiki]]** if you want to *read* your knowledge base in a nice UI. Use **[[graphify]]** if you want your *AI agent* to use the knowledge base to help you code.
