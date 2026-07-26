---
type: concept
title: Screenshot-First Prompting
tags: [claude-code, prompts, workflow, context, high, high]
related: [claude-code, ruben-hassid-2026-claude-code, claude-code-for-non-coders-workflow, vibecoding]
created: 2026-05-10
updated: 2026-05-10
---

# Screenshot-First Prompting

Screenshot-first prompting is the practice of giving [[claude-code]] visual context before writing a long natural-language description.

## Why It Matters

Screenshots compress layout, spacing, hierarchy, color, and visual bugs into a form Claude Code can inspect directly. In [[ruben-hassid-2026-claude-code]], Ruben Hassid recommends screenshots both at the start of a build and during the feedback loop when the generated UI looks wrong.

## Pattern

1. Attach a screenshot of a reference design or broken UI state.
2. State the desired adaptation or fix in one sentence.
3. Ask Claude Code to update the implementation.
4. Refresh the preview and repeat with another screenshot if needed.

## Connections

This concept supports [[vibecoding]] because non-coders can steer UI quality through visual judgment instead of code review.
