---
type: source
title: "Source: safishamsi/graphify — AI coding assistant skill"
authors: ["safishamsi"]
year: 2026
url: "https://github.com/safishamsi/graphify"
venue: "GitHub"
created: 2026-04-29
updated: 2026-04-29
tags: [agent-skills, knowledge-graph, graphrag, multi-modal]
related: ["[[graphify]]"]
---

# Source: safishamsi/graphify — AI coding assistant skill

## Summary
`graphify` is a multi-modal AI coding assistant skill that turns any folder of code, documents, papers, images, or videos into a queryable knowledge graph. It integrates with major LLM coding agents (Claude Code, Codex, Cursor, Gemini CLI, etc.) to provide structural context that helps agents navigate codebases more effectively.

## Key Features
- **Multi-modal Ingest**: Supports code (25+ languages), PDFs, markdown, images (screenshots, diagrams), and video/audio (local transcription via Whisper).
- **Knowledge Graph Construction**: Uses tree-sitter for deterministic code extraction and Claude subagents for semantic extraction from docs and media.
- **GraphRAG**: 71.5x fewer tokens per query vs reading raw files by querying a compact graph.json.
- **Always-on Integration**: Installs hooks and instructions into coding tools (e.g., CLAUDE.md, .cursor/rules/) so the agent always references the graph.
- **Interactive Visualization**: Generates an interactive HTML graph and a plain-language GRAPH_REPORT.md.
- **Platform Agnostic**: Supports Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, Aider, Trae, and more.

## Technical Details
- **Tech Stack**: Python, NetworkX, Leiden community detection, tree-sitter, faster-whisper.
- **Metrics**: 37.5k stars, 4.1k forks, 69 releases.
- **Performance**: SHA256 caching and mtime-based rebuilds ensure fast incremental updates.
