---
type: entity
title: Claude Code
tags: [claude-code, ide-integration, workflow, development]
related: "[[claude-chat]], [[claude-cowork]], [[cursor-ide]], [[mcp-servers]], [[background-tasks]], [[ruben-hassid-2026-claude-code]], [[claude-code-for-non-coders-workflow]], [[vscode]], [[github]]"
created: 2026-05-09
updated: 2026-05-10
---

# Claude Code

Claude Code is Anthropic's official IDE integration for Claude, enabling AI-assisted software development workflows directly in your editor.

## Core Features

- **File editing** — Direct code modifications with verification
- **Terminal execution** — Run commands and see output in real-time
- **Background tasks** — Long-running processes with live log access
- **MCP servers** — Extensible integrations (Context7, Supabase, etc.)
- **Skill system** — Custom workflows via `/skill-name` commands
- **Plan mode** — Structured approach to complex tasks

## Dual-Tool Workflow

Claude Code works best alongside [[cursor-ide]]:
- **Claude Code** — Complex reasoning, multi-file refactoring, architecture
- **Cursor** — Quick edits, Plan Mode for local exploration

## Integration Points

- **[[mcp-servers]]** — Extend capabilities with custom integrations
- **[[background-tasks]]** — Run dev server while debugging
- **[[claude-skills]]** — Create custom workflows
- **[[github]]** — PR creation and code review

## Non-Coder Workflow

[[ruben-hassid-2026-claude-code]] frames Claude Code as a tool non-coders can use by pairing [[github]] publishing, [[vscode]] sessions, [[screenshot-first-prompting]], and live preview testing. The extracted [[claude-code-for-non-coders-workflow]] treats the user as project manager and Claude Code as implementation agent.

## Related Concepts

- [[dual-tool-workflow]] — Running Claude Code + Cursor simultaneously
- [[vibecoding]] — Vibe-driven development approach
- [[screenshot-first-prompting]] — Starting with visual context
- [[permission-friction]] — Repeated approvals as a workflow bottleneck
- [[project-memory-file]] — CLAUDE.md as durable project context

> [!info] God Node
> Claude Code is one of the most-connected nodes (8 edges), indicating it's central to the developer experience.
