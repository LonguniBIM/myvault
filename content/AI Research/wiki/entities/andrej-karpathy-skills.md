---
type: entity
title: "Andrej Karpathy Skills (forrestchang/andrej-karpathy-skills)"
tags: [llm-guidelines, claude-code, cursor, coding-best-practices, karpathy, claude-md]
related: ["[[llm-wiki]]", "[[karpathy-llm-wiki-pattern]]", "[[llm-coding-guidelines]]", "[[obsidian-skills]]", "[[agent-skills-for-llm-coding]]", "[[llm-agent-skills]]"]
created: 2026-04-29
updated: 2026-04-29
repo_url: "https://github.com/forrestchang/andrej-karpathy-skills"
author: "forrestchang"
language: [Markdown]
stars: 94800
license: "MIT"
last_commit: 2026-04-20
use_case: [llm-coding-guidelines, claude-code-config, cursor-rules]
status: active
---

# Andrej Karpathy Skills

**Summary**: A single CLAUDE.md file containing four coding principles derived from Andrej Karpathy's observations on LLM coding pitfalls. Reduces overcomplication, wrong assumptions, and orthogonal edits in LLM-assisted coding.

**Sources**: [[github---forrestchang-andrej-karpathy-skills-a-sin-20260428]]

---

## What It Does

Provides a drop-in CLAUDE.md (or Cursor rule) file that guides LLM coding agents to produce better code by enforcing four principles addressing Karpathy's observed pitfalls.

## The Four Principles

| Principle | Addresses |
|-----------|-----------|
| **Think Before Coding** | Wrong assumptions, hidden confusion, missing tradeoffs |
| **Simplicity First** | Overcomplication, bloated abstractions |
| **Surgical Changes** | Orthogonal edits, touching unrelated code |
| **Goal-Driven Execution** | Leverage via tests-first, verifiable success criteria |

## Strengths

- **Extremely lightweight** — single file, zero dependencies, instant setup
- **Massively popular** — 94.8k stars, clearly resonates with the community
- **Works with Claude Code AND Cursor** — dual-platform support
- **MIT license** — no restrictions on use
- **Based on real observations** — derived from Karpathy's practical experience
- **Composable** — merges with existing project-specific CLAUDE.md instructions
- **Plugin install option** — can be installed as Claude Code plugin via marketplace

## Weaknesses

- **Not a tool/application** — it's configuration/guidelines, not software
- **No automation** — relies entirely on the LLM agent honoring the guidelines
- **Limited scope** — only addresses coding behavior, not knowledge management
- **No versioning/releases** — repo has no published releases
- **Subjective effectiveness** — hard to measure quantitative improvement
- **Static content** — doesn't adapt to project context dynamically

## Install Methods

1. **Claude Code Plugin** (recommended): `/plugin install andrej-karpathy-skills@karpathy-skills`
2. **CLAUDE.md** (per-project): `curl -o CLAUDE.md <raw url>`
3. **Cursor**: `.cursor/rules/karpathy-guidelines.mdc` included in repo

## Compared With

See [[agent-skills-for-llm-coding]] for a side-by-side comparison with [[obsidian-skills]].

## Related Pages

- [[obsidian-skills]]
- [[llm-wiki]]
- [[karpathy-llm-wiki-pattern]]
- [[llm-coding-guidelines]]
- [[llm-agent-skills]]
- [[agent-skills-for-llm-coding]]
