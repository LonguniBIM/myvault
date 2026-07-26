---
type: concept
title: "LLM Coding Guidelines"
tags: [llm-guidelines, coding-best-practices, claude-code, cursor, prompt-engineering]
related: ["[[andrej-karpathy-skills]]", "[[obsidian-skills]]", "[[llm-agent-skills]]", "[[agent-skills-for-llm-coding]]"]
created: 2026-04-29
updated: 2026-04-29
---

# LLM Coding Guidelines

**Summary**: Configuration files and rule sets that guide LLM coding agents (Claude Code, Cursor, etc.) to produce better, simpler, and more focused code by constraining their default behaviors.

---

## Why They Exist

LLM coding agents tend to:
- Make wrong assumptions silently
- Overcomplicate code and abstractions
- Touch unrelated code as side effects
- Not manage their own confusion

Guidelines files (CLAUDE.md, .cursor/rules/) address these by providing explicit behavioral constraints.

## Common Principles

1. **Explicit reasoning** — State assumptions, surface tradeoffs
2. **Minimalism** — Only implement what was asked
3. **Surgical edits** — Don't modify unrelated code
4. **Goal-driven** — Define success criteria, loop until met

## Repos in This Category

- [[andrej-karpathy-skills]] — Behavioral guidelines (94.8k stars)
- [[obsidian-skills]] — Domain-specific skills for Obsidian (27k stars)

See [[agent-skills-for-llm-coding]] for a detailed comparison.

## Related Pages

- [[andrej-karpathy-skills]]
- [[obsidian-skills]]
- [[llm-agent-skills]]
- [[agent-skills-for-llm-coding]]
