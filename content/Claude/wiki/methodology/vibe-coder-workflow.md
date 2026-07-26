---
type: methodology
title: "10x Vibe Coder Workflow"
tags: [topic:workflow, topic:optimization, topic:mcp, priority:high]
related: [be-a-10x-vibe-coder-claude-code-cursor-mcp, claude-ai-assistant, cursor-ide, ultrathink-keyword, dual-tool-workflow, background-tasks-feature, ai-code-review, context7-mcp, supabase-mcp, whisperflow]
created: 2026-05-08
updated: 2026-05-08
skill_status: candidate
source: "[[be-a-10x-vibe-coder-claude-code-cursor-mcp]]"
---

# 10x Vibe Coder Workflow

A complete workflow for solo developers and vibe coders to maximize AI coding output using Claude Code and Cursor together. Derived from Chris's live demonstration and rapid-fire tips.

## Session Setup (One-Time)

1. Open Cursor as main IDE
2. Move terminal panel to the right side
3. Run Claude Code in that right terminal
4. Connect MCP servers: Context7 and Supabase (or your DB equivalent)
5. Hook Bugbot (or Claude Code GitHub integration) to all repos
6. Install Whisper Flow for dictation

## Task Routing Decision Tree

Before starting any task:

1. Is it **very complex architecture** (whole app, major feature)? → Claude Code + Opus (`ultrathink` every message)
2. Is Opus quota exhausted or is it a **complex bug**? → Cursor Plan Mode (GPT-5.1 high for plan, Sonnet for build)
3. Is it **UI / animation / design polish**? → Claude Code (Sonnet is fine, still has edge)
4. Is it **simple / isolated**? → Either tool, no plan mode needed

## Per-Prompt Workflow

1. **Dictate** your prompt via Whisper Flow — don't type, be detailed
2. **Add `ultrathink`** to the message (Claude Code)
3. **Review the plan** before approving execution (plan mode)
4. Run and test → refine with more dictated prompts
5. Open PR → let AI code reviewer check before merge

## MCP Usage

- Need library docs? → *"use Context7 MCP for [library] documentation"*
- Setting up database? → use Supabase MCP to spin up schema + security rules
- Auditing existing setup? → *"use Supabase MCP to review my config and check all security rules"*

## Background Task Setup

At session start: *"run the server in the background for me"*
→ Claude now has live log access for all debugging in this session

## A/B Testing (Optional)

For uncertain tasks: run same prompt on both Claude Code and Cursor Plan Mode simultaneously, compare outputs, keep the better result.

## Anti-Patterns to Avoid

- Feeding documentation as URLs (use Context7 MCP instead)
- Skipping plan mode on complex tasks
- Typing prompts instead of dictating
- Merging without AI code review
- Running all debugging without background server running

## Why This Works

- Plan mode prevents retroactive fixing (better to catch before execution)
- `ultrathink` triggers deeper reasoning with no token cost penalty
- Background tasks eliminate copy-paste friction for debugging
- MCP gives AI accurate context (docs, DB state) rather than hallucinated APIs
- Dictation produces 3-5x more detailed prompts in same time

## Skill Candidate Notes

This method has clear numbered steps, specific tool configurations, and measurable outcomes (20%+ output improvement from plan mode alone). Ready for skill extraction.
