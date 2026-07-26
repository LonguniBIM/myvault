---
type: comparison
title: "Agent Skills for LLM Coding Agents — Comparison"
tags: [agent-skills, claude-code, codex-cli, cursor, llm-guidelines, obsidian, graphify]
related: ["[[obsidian-skills]]", "[[andrej-karpathy-skills]]", "[[graphify]]", "[[llm-coding-guidelines]]", "[[llm-agent-skills]]"]
created: 2026-04-29
updated: 2026-04-29
use_case: "Agent skills / configuration files for LLM coding agents"
repos: ["[[obsidian-skills]]", "[[andrej-karpathy-skills]]", "[[graphify]]"]
best_fit: "depends on goal — see recommendation below"
best_fit_reason: "They solve different sub-problems; use all three for maximum capability"
---

# Agent Skills for LLM Coding Agents

**Summary**: Comparison of repos that provide skill files / configuration for LLM coding agents (Claude Code, Codex CLI, Cursor). These tools teach agents to behave better, know more, or navigate complex structures.

---

## Overview

| Aspect | [[andrej-karpathy-skills]] | [[obsidian-skills]] | [[graphify]] |
|--------|---------------------------|---------------------|--------------|
| **Author** | forrestchang | kepano (Obsidian CEO) | safishamsi |
| **Stars** | 94.8k | 27k | 37.5k |
| **Forks** | 9.2k | 1.8k | 4.1k |
| **Contributors** | 8 | 13 | 7 |
| **License** | MIT | MIT | MIT |
| **Last commit** | Apr 20, 2026 | Apr 3, 2026 | Apr 28, 2026 |
| **Install** | Plugin / CLAUDE.md / Cursor rule | Plugin / npx / manual | uv / pip / manual |

## What Each Does

| Dimension | andrej-karpathy-skills | obsidian-skills | graphify |
|-----------|----------------------|-----------------|----------|
| **Type** | Behavioral guidelines (how to think) | Domain knowledge (what to know) | Structural/Semantic context (where to look) |
| **Content** | 4 coding principles | 5 discrete skills | Multi-modal knowledge graph |
| **Scope** | Universal — any coding project | Obsidian-specific | Universal — any folder/codebase |
| **Agent support** | Claude Code, Cursor | Claude Code, Codex CLI, OpenCode | Claude Code, Cursor, Gemini, and more |
| **Approach** | Constrains agent behavior | Teaches agent new formats | Provides navigable map of project |

## Feature Matrix

| Feature | andrej-karpathy-skills | obsidian-skills | graphify |
|---------|:-----:|:-----:|:-----:|
| Behavioral guidelines | **Yes** | No | No |
| Domain-specific knowledge | No | **Yes** | **Yes** (via extraction) |
| Structural mapping | No | No | **Yes** |
| Multi-modal ingest | No | No | **Yes** |
| Claude Code support | **Yes** | **Yes** | **Yes** |
| Cursor support | **Yes** | No | **Yes** |
| Codex CLI support | No | **Yes** | **Yes** |
| OpenCode support | No | **Yes** | **Yes** |
| Plugin marketplace install | **Yes** | **Yes** | No |
| Web extraction | No | **Yes** | **Yes** |
| Composable with other skills | **Yes** | **Yes** | **Yes** |

## Pros & Cons

### andrej-karpathy-skills

| Pros | Cons |
|------|------|
| Universal — works on any project | Only addresses coding behavior, not domain knowledge |
| Extremely lightweight (1 file) | No automation — agent must honor guidelines voluntarily |
| Backed by Karpathy's real observations | Subjective effectiveness, hard to measure |
| Massive community validation (94.8k stars) | Static content, doesn't adapt dynamically |
| Works with Cursor too | No Codex CLI / OpenCode support |

### obsidian-skills

| Pros | Cons |
|------|------|
| Teaches agents Obsidian-specific syntax they don't know | Useless outside Obsidian ecosystem |
| Modular — pick only the skills you need | Doesn't improve general coding behavior |
| Wider agent support (Claude Code + Codex CLI + OpenCode) | No Cursor support |
| Defuddle is useful beyond Obsidian | Still relies on agent honoring instructions |
| Maintained by Obsidian's CEO (authoritative) | Narrow scope — format knowledge only |

### graphify

| Pros | Cons |
|------|------|
| Massive structural clarity for large codebases | Requires local setup (Python, Whisper) |
| Drastic token reduction (70x+) via GraphRAG | High initial token cost for document ingest |
| Multi-modal: connects code to docs, images, video | CLI-first workflow |
| Always-on agent integration via hooks | complex dependency tree |

## Best Fit Recommendation

**These repos are complementary, not competing.** They solve different sub-problems:

| If your goal is... | Best fit |
|---------------------|----------|
| Improve general LLM coding quality (any project) | **[[andrej-karpathy-skills]]** |
| Work with Obsidian vaults via LLM agents | **[[obsidian-skills]]** |
| Navigate complex, multi-modal project structures | **[[graphify]]** |
| Reduce token usage on large corpora | **[[graphify]]** |
| Both: better coding + Obsidian knowledge | **Use both together** |
| Maximum agent capability | **Use all three** |

**Bottom line**: If you use Claude Code, install all three. `andrej-karpathy-skills` makes the agent *think better*, `obsidian-skills` makes the agent *know more about Obsidian*, and `graphify` gives the agent *a map of everything*.

## Related Pages

- [[llm-coding-guidelines]]
- [[llm-agent-skills]]
- [[graphify]]
