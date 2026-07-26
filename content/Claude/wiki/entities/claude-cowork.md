---
type: entity
title: Claude Cowork
tags: [cowork, autonomous-workflows, desktop-app, multi-step, projects, memory]
related: "[[claude-code]], [[claude-chat]], [[cowork-projects]], [[scheduled-tasks]], [[background-tasks]], [[claude-design]], [[mcp-servers]]"
created: 2026-05-09
updated: 2026-05-09
---

# Claude Cowork

## Overview

Claude Cowork is Anthropic's desktop application for autonomous multi-step task execution with file system access and scoped memory per project. It bridges multiple communities in the knowledge graph (6 edges), connecting Brand & Design System, Cowork Tooling & Rollout, Personal Context Files, and Claude Code Workflow.

## Key Features

- **File system access** - Reads and creates files on your computer
- **Autonomous execution** - Completes multi-step workflows without constant prompting
- **Question-driven** - Uses AskUserQuestion to clarify requirements before executing
- **Projects** - Persistent context folders that remember uploaded files
- **Plugins** - Pre-built skill packs (Sales, Marketing, Legal, Finance, Data, etc.)
- **Artifacts** - Interactive outputs (calculators, charts, dashboards)
- **Connectors** - Integration with Gmail, Drive, Slack, Notion, Figma, 50+ tools

## Installation

1. Go to claude.com/download
2. Download the desktop app (Mac/Windows)
3. Requires Claude Pro subscription ($20/month or $17/month annually)
4. Open app → Click "Cowork" tab
5. Select a folder to give Claude file access

## Optimal Setup (April 2026)

Following [[cowork-april-2026-update]], the "Triple-Folder" architecture is recommended:
- **Folder Setup**: [[cowork-folder-setup]] (ABOUT ME, OUTPUTS, TEMPLATES)
- **Voice Ingest**: [[voice-context-ingest]] (using [[wispr-flow]])
- **Optimization**: [[cowork-token-optimization]]

## Best Practices

- **Use markdown files** - Create `.md` files with context (writing style, brand rules, examples)
- **Force clarification** - Start prompts with "Read files, then ask me questions before executing"
- **Leverage text files over prompts** - Put knowledge in files, not in long prompts
- **Small Context Files** - Keep `ABOUT ME` files under 2,000 tokens to ensure Claude reads them accurately.

## Certification

Official certification available: **Introduction to Claude Cowork** (2 hours) via [[Anthropic Academy]]

Covers: Projects, Plugins, Skills, scheduling, file handling, research at scale, permissions, model selection.

## Integration Points

- **[[claude-code]]** — Complementary tool for development tasks
- **[[claude-design]]** — Design system integration via DESIGN.md
- **[[mcp-servers]]** — Access external data sources
- **[[scheduled-tasks]]** — Recurring workflow automation
- **[[cowork-projects]]** — Scoped memory per project

## Related Concepts

- [[cowork-workflows]] — Common patterns and use cases
- [[files-replace-prompts]] — Using structured files instead of prompts
- [[token-saving-habits]] — Optimization techniques for Cowork
- [[cowork-april-2026-update]] — Latest features and improvements

## Workflow Examples

- **Negotiation prep** — Synthesize Gmail/Notes/Slack into brief
- **Meeting notes** — Extract action items and decisions
- **Content pipeline** — Batch process multiple documents

> [!info] God Node
> Claude Cowork is highly connected (6 edges), serving as a cross-community bridge in the knowledge graph.
