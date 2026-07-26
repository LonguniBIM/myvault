---
type: source
title: "forrestchang/andrej-karpathy-skills — CLAUDE.md guidelines from Karpathy's LLM coding observations"
created: 2026-04-28
updated: 2026-04-29
sources: ["github---forrestchang-andrej-karpathy-skills-a-sin-20260428.md"]
authors: [forrestchang, herobrine19]
year: 2026
url: "https://github.com/forrestchang/andrej-karpathy-skills"
tags: [claude-code, llm-guidelines, coding-best-practices, karpathy, cursor, claude-md]
related: ["[[andrej-karpathy-skills]]", "[[karpathy-llm-wiki-pattern]]", "[[llm-coding-guidelines]]"]
---

# forrestchang/andrej-karpathy-skills — Source Summary

**Summary**: A single CLAUDE.md file containing four coding principles derived from Andrej Karpathy's observations on LLM coding pitfalls. Designed to improve Claude Code (and Cursor) behavior by reducing overcomplication, wrong assumptions, and orthogonal edits.

**Key Takeaways**:

1. **Think Before Coding** — State assumptions explicitly, present multiple interpretations, push back when warranted, stop when confused.
2. **Simplicity First** — Minimum code that solves the problem. No speculative features, no unnecessary abstractions.
3. **Surgical Changes** — Touch only what you must. Don't "improve" adjacent code. Match existing style.
4. **Goal-Driven Execution** — Transform imperative tasks into declarative goals with verification loops. LLMs excel at looping until success criteria are met.

**Install Options**: Claude Code plugin (recommended) or copy CLAUDE.md to project root. Also supports Cursor via `.cursor/rules/`.

**Metrics**: 94.8k stars | 9.2k forks | 28 commits | 8 contributors | License: MIT | No releases published
