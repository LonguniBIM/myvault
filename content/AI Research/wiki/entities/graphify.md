---
type: entity
title: "graphify"
tags: [tool, agent-skill, knowledge-graph, graphrag, python]
related: ["[[llm-wiki]]", "[[obsidian-skills]]", "[[andrej-karpathy-skills]]", "[[llm-agent-skills]]", "[[llm-knowledge-base]]"]
created: 2026-04-29
updated: 2026-04-29
repo_url: "https://github.com/safishamsi/graphify"
author: "safishamsi"
language: [Python]
stars: 37500
license: "MIT"
last_commit: 2026-04-28
use_case: [knowledge-graph, codebase-analysis, agent-augmentation, graphrag]
status: active
---

# graphify

**graphify** is an AI coding assistant skill and knowledge graph construction tool. It bridges the gap between raw project files (code, docs, media) and LLM context windows by building a persistent, queryable knowledge graph that agents can use for navigation and reasoning.

## Core Capabilities

- **Automated Mapping**: Scans a directory and builds a graph of classes, functions, concepts, and relationships.
- **Cross-Modal Linking**: Connects code to documentation, papers, and even video transcripts in a single unified structure.
- **Agent Skill**: Acts as a "plugin" for Claude Code, Cursor, and other agents, providing them with a `GRAPH_REPORT.md` that guides their file-search behavior.
- **GraphRAG**: Enables retrieval-augmented generation using graph topology rather than just vector similarity, significantly reducing token usage.

## Strengths

- **High Star Power**: 37.5k stars indicates massive community adoption and trust.
- **Broad Integration**: Works with almost every major LLM coding CLI and IDE.
- **Deterministic + Semantic**: Combines reliable AST parsing for code with LLM-based extraction for unstructured data.
- **Local-First**: Transcription (Whisper) and code analysis run locally; only semantic extraction of docs/images uses an external API.
- **Performance**: Exceptional token efficiency (reported 70x+ reduction for large corpora).

## Weaknesses

- **Complexity**: Requires Python 3.10+ and various dependencies (Whisper, tree-sitter) which can be heavy to install.
- **Token Cost (Initial)**: The first run requires LLM calls for all non-code files, which can be expensive for very large document sets.
- **CLI-Centric**: While it has HTML visualization, the core workflow is heavily CLI-based, which may be less approachable for non-technical users compared to [[llm-wiki]].

## Comparison Context

- **vs [[llm-wiki]]**: `graphify` is more focused on developer workflows and agent integration, while `llm-wiki` is a desktop app for general document wikis.
- **vs [[obsidian-skills]]**: `graphify` is a general-purpose tool for any codebase, whereas `obsidian-skills` is specifically for Obsidian vault management.
- **vs [[andrej-karpathy-skills]]**: `graphify` provides structural/domain knowledge (data), whereas `andrej-karpathy-skills` provides behavioral constraints (logic).

## Related Pages
- [[agent-skills-for-llm-coding]] — Comparison with other agent skills
- [[llm-knowledge-base]] — Concept page for LLM-driven knowledge management
