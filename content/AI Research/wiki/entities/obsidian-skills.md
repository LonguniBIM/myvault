---
type: entity
title: "Obsidian Skills (kepano/obsidian-skills)"
tags: [agent-skills, obsidian, claude-code, codex-cli, opencode, markdown, json-canvas, defuddle]
related: ["[[andrej-karpathy-skills]]", "[[llm-agent-skills]]", "[[agent-skills-for-llm-coding]]"]
created: 2026-04-29
updated: 2026-04-29
repo_url: "https://github.com/kepano/obsidian-skills"
author: "kepano"
language: [Markdown]
stars: 27000
license: "MIT"
last_commit: 2026-04-03
use_case: [llm-agent-skills, obsidian-integration, claude-code-config, codex-cli-config]
status: active
---

# Obsidian Skills

**Summary**: Agent skills that teach LLM coding agents (Claude Code, Codex CLI, OpenCode) how to use Obsidian-specific formats — Markdown with wikilinks, Bases, JSON Canvas, CLI, and Defuddle web extraction.

**Sources**: [[github---kepano-obsidian-skills-agent-skills-for-o-20260429]]

---

## What It Does

Provides a set of SKILL.md files following the Agent Skills specification. Each skill teaches an LLM agent a specific Obsidian capability, enabling it to create and edit Obsidian vault content correctly.

## Skills Included

| Skill | Description |
|-------|-------------|
| **obsidian-markdown** | Obsidian Flavored Markdown — wikilinks, embeds, callouts, properties |
| **obsidian-bases** | Obsidian Bases (.base) — views, filters, formulas, summaries |
| **json-canvas** | JSON Canvas (.canvas) — nodes, edges, groups, connections |
| **obsidian-cli** | Obsidian CLI — vault interaction, plugin/theme development |
| **defuddle** | Clean markdown extraction from web pages (removes clutter, saves tokens) |

## Strengths

- **Domain-specific knowledge** — teaches agents Obsidian-specific syntax that generic LLMs don't know well
- **Multi-agent support** — works with Claude Code, Codex CLI, and OpenCode
- **Follows Agent Skills spec** — standard format, portable across compatible agents
- **Very popular** — 27k stars, strong community validation
- **Modular** — 5 independent skills, use only what you need
- **MIT license** — no restrictions
- **Active community** — 13 contributors, maintained by kepano (Obsidian CEO)
- **Defuddle** — unique web extraction skill useful beyond Obsidian

## Weaknesses

- **Obsidian-specific** — most skills only useful if you work in Obsidian
- **Not a tool/application** — configuration/skill files, not software
- **No automation** — relies on the agent honoring the skill instructions
- **No releases** — repo has no published releases or versioning
- **Limited to supported agents** — only Claude Code, Codex CLI, OpenCode
- **Narrow scope** — teaches format knowledge, not coding principles or behavior

## Install Methods

1. **Marketplace** (Claude Code): `/plugin install obsidian@obsidian-skills`
2. **npx skills**: `npx skills add git@github.com:kepano/obsidian-skills.git`
3. **Manual**: Copy to `/.claude/`, `~/.codex/skills/`, or `~/.opencode/skills/`

## Related Pages

- [[andrej-karpathy-skills]]
- [[llm-agent-skills]]
- [[agent-skills-for-llm-coding]]
