---
type: source
title: "Test Architecture Notes"
tags: [extract, docx]
related: []
created: 2026-04-30
updated: 2026-04-30
source_file: "test-architecture-notes.docx"
file_type: "docx"
---

# Test Architecture Notes

**Source**: `raw\docs\test-architecture-notes.docx`
**Extracted**: 2026-04-30
**Type**: docx

---

## LLM Wiki Architecture Notes

This document describes the architecture of an LLM Wiki system based on Andrej Karpathys pattern.

### Key Components

1. Raw folder: Immutable source documents (papers, screenshots, notes)

2. Wiki folder: Markdown pages maintained by Claude

3. Graphify: Converts corpus into a queryable knowledge graph

### Workflow

The human curates sources and asks questions. The LLM maintains the wiki, creates cross-references, and builds up structured knowledge over time.
