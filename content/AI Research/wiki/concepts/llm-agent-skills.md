---
type: concept
title: "LLM Agent Skills"
tags: [agent-skills, claude-code, codex-cli, opencode, cursor, skill-files]
related: ["[[obsidian-skills]]", "[[andrej-karpathy-skills]]", "[[llm-coding-guidelines]]", "[[agent-skills-for-llm-coding]]"]
created: 2026-04-29
updated: 2026-04-29
---

# LLM Agent Skills

**Summary**: Portable skill/configuration files that extend LLM coding agents with new knowledge or behavioral constraints. Follows emerging standards like the Agent Skills specification.

---

## What Are Agent Skills?

Agent skills are files (typically SKILL.md, CLAUDE.md, or rule files) that:
- Teach agents domain-specific knowledge they lack
- Constrain agent behavior to produce better output
- Are installable via plugin marketplaces or manual copy
- Are portable across compatible agents

## Two Types

| Type | Purpose | Example |
|------|---------|---------|
| **Behavioral** | How the agent should think and act | [[andrej-karpathy-skills]] |
| **Domain knowledge** | What the agent should know about a specific tool/format | [[obsidian-skills]] |
| **Structural Context** | Navigable map of a specific project/codebase | [[graphify]] |

## Compatible Agents

| Agent | Skill format |
|-------|-------------|
| Claude Code | CLAUDE.md, .claude-plugin/, SKILL.md |
| Cursor | .cursor/rules/*.mdc |
| Codex CLI | ~/.codex/skills/*/SKILL.md |
| OpenCode | ~/.opencode/skills/*/SKILL.md |
| Gemini CLI | ~/.gemini/skills/*/SKILL.md |

## Repos in This Category

- [[andrej-karpathy-skills]] — Behavioral guidelines (94.8k stars)
- [[obsidian-skills]] — Obsidian domain knowledge (27k stars)
- [[graphify]] — Structural context / Knowledge graph (37.5k stars)

See [[agent-skills-for-llm-coding]] for detailed comparison.

## Related Pages

- [[agent-skills-for-llm-coding]]
- [[llm-coding-guidelines]]
