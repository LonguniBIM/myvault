---
type: concept
title: "Claude Code Background Tasks"
tags: [topic:workflow, topic:optimization, priority:high]
related: [claude-ai-assistant, vibe-coder-workflow, be-a-10x-vibe-coder-claude-code-cursor-mcp]
created: 2026-05-08
updated: 2026-05-08
---

# Claude Code Background Tasks

A Claude Code feature (added ~early 2026) that allows Claude to run long-running processes (like a dev server) in the background and read their output during the session.

## How to Use

Tell Claude Code: *"run the server in the background for me"*

Claude starts the process and you'll see "1 background task" indicator. The server runs continuously while you continue coding.

## Why It Matters

Claude now has **live access to server logs** without you manually copying and pasting. When debugging, Claude can read the actual error output directly — dramatically faster feedback loop.

## Example Workflow

1. Start session: *"run the server in the background"*
2. Make changes and ask Claude to test/debug
3. Claude reads live logs, identifies errors, fixes without you pasting anything

## Note

The author reports most developers aren't using this yet, likely because it's a recent feature.

## Sources

- [[be-a-10x-vibe-coder-claude-code-cursor-mcp]]
