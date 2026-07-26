---
type: concept
title: "ultrathink — Claude Code Extended Thinking Keyword"
tags: [topic:optimization, topic:prompts, priority:high]
related: [claude-ai-assistant, vibe-coder-workflow, be-a-10x-vibe-coder-claude-code-cursor-mcp]
created: 2026-05-08
updated: 2026-05-08
---

# ultrathink — Claude Code Extended Thinking Keyword

A special keyword recognized by Claude Code that triggers deeper reasoning on the problem before responding.

## How It Works

Type `ultrathink` anywhere in your message to Claude Code (e.g., *"can you fix this issue ultrathink"*). Claude Code responds with a visual indicator (color change in the UI) confirming it's thinking harder.

## Observed Behavior

- Response takes roughly 2x longer
- Produces noticeably better output on complex problems
- Works in 90% of messages without apparent token consumption penalty vs. not using it

## Usage Recommendation

Use in most messages, especially for anything non-trivial. There's no observed downside in token cost despite the deeper reasoning.

## Cursor Compatibility

Typing `ultrathink` in Cursor (with Sonnet model) may work but does not trigger the visual color animation that confirms activation.

## Sources

- [[be-a-10x-vibe-coder-claude-code-cursor-mcp]]
