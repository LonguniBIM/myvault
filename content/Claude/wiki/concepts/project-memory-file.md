---
type: concept
title: Project Memory File
tags: [claude-code, memory, context, workflow, high, high]
related: [claude-code, files-replace-prompts, ruben-hassid-2026-claude-code, claude-code-for-non-coders-workflow]
created: 2026-05-10
updated: 2026-05-10
---

# Project Memory File

A project memory file is a root CLAUDE.md that records what [[claude-code]] should remember about a project across sessions.

## Why It Matters

In [[ruben-hassid-2026-claude-code]], Claude Code is described as starting from zero unless the project has a durable memory layer. Asking Claude to create CLAUDE.md after the first session captures project structure, design decisions, preferences, and existing pages.

## Pattern

```markup
Create a CLAUDE.md file in the root of this project. Inside it, write down everything you've learned about this project so far: folder structure, what each file does, design choices, my preferences, and what pages or sections exist.
```

## Connection to Thesis

This concept directly supports [[files-replace-prompts]]: durable files become reusable context, reducing the need to repeat instructions in every prompt.
