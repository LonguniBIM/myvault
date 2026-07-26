---
type: entity
title: "Cursor IDE"
tags: [topic:workflow, topic:agents, priority:high]
related: [claude-ai-assistant, dual-tool-workflow, vibe-coder-workflow, be-a-10x-vibe-coder-claude-code-cursor-mcp]
created: 2026-05-08
updated: 2026-05-08
---

# Cursor IDE

AI-powered code editor with built-in agent and plan modes. Commonly used alongside Claude Code in a dual-tool vibe coding workflow.

## Key Features for Vibe Coding

**Plan Mode** — Toggle from agent mode; AI plans all steps before executing. You review and approve the plan, then click Build. Uses GPT-5.1 high for planning (best results) and Sonnet for execution.

- Better than Claude Code plan mode for complex bugs (asks more follow-up questions, more detailed plans)
- Increases output quality ~20%+ vs no plan mode

**Agent Mode** — Direct execution without planning step. Good for simple changes.

**AI Code Review** — GitHub integration at ~$40/month; catches security issues on every PR automatically.

## Recommended Model Configuration (per source)

| Task | Model |
|------|-------|
| Planning (Plan Mode) | GPT-5.1 high |
| Execution | Sonnet 4.5 / 4.7 |

## When to Use Cursor vs Claude Code

| Task | Preferred Tool |
|------|---------------|
| Complex bugs | Cursor Plan Mode |
| Complex architecture | Claude Code (Opus) |
| UI / animations | Claude Code (edge even on same model) |
| Simple changes | Either |

## Sources

- [[be-a-10x-vibe-coder-claude-code-cursor-mcp]]
