---
type: concept
title: "LLM-Powered Knowledge Base"
tags: [knowledge-base, llm, rag, personal-wiki, knowledge-management]
related: ["[[llm-wiki]]", "[[karpathy-llm-wiki-pattern]]"]
created: 2026-04-29
updated: 2026-04-29
---

# LLM-Powered Knowledge Base

**Summary**: Tools and systems that use Large Language Models to automatically build, maintain, and query structured knowledge bases from user-provided documents.

---

## Key Characteristics

- **Automated structuring** — LLM reads raw documents and produces organized wiki pages with metadata
- **Cross-referencing** — Entities and concepts are linked automatically across the knowledge base
- **Incremental updates** — New sources are integrated into the existing knowledge structure, not processed in isolation
- **Queryable** — Users can ask natural language questions answered from the accumulated knowledge

## Persistent Wiki vs Traditional RAG

| Aspect | Persistent Wiki | Traditional RAG |
|--------|----------------|-----------------|
| Knowledge storage | Compiled into structured pages | Raw chunks in vector DB |
| Update model | Incremental — new sources woven in | Re-index entire corpus |
| Query cost | Low — read pre-built pages | High — re-derive every query |
| Contradictions | Explicitly surfaced and tracked | Hidden / ignored |
| Human reviewable | Yes — readable markdown pages | No — opaque embeddings |

## Repos in This Category

- [[llm-wiki]] — Full desktop app implementing the persistent wiki approach
- [[graphify]] — CLI-first tool focused on building a queryable knowledge graph for agents (GraphRAG)

## Related Pages

- [[karpathy-llm-wiki-pattern]]
- [[llm-wiki]]
- [[graphify]]
- [[llm-knowledge-base-tools]]
