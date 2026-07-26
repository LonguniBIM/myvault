---
type: concept
title: Permission Friction
tags: [claude-code, permissions, workflow, optimization, medium, high]
related: [claude-code, ruben-hassid-2026-claude-code, claude-code-for-non-coders-workflow, vscode]
created: 2026-05-10
updated: 2026-05-10
---

# Permission Friction

Permission friction is the productivity cost created when [[claude-code]] repeatedly asks the user to approve file edits, file creation, or command execution.

## Why It Matters

In [[ruben-hassid-2026-claude-code]], permission prompts are framed as the main bottleneck for non-coders: a small website can require 20+ approvals, preventing the user from stepping away while Claude works.

## Mitigation

The source recommends moving from the desktop Code tab to [[vscode]], installing the Claude extension, and enabling bypass/skip permissions for faster sessions.

## Tradeoff

Reducing prompts increases speed but also reduces the user's opportunity to inspect actions before they happen. For non-coders, this makes live-output testing and small deliverable scopes more important.
