---
type: methodology
title: Cowork Folder Architecture
created: 2026-05-10
updated: 2026-05-10
tags: [topic:setup, topic:optimization, priority:high, confidence:high, skill_status:candidate]
related: ["cowork-april-2026-update", "cowork-feature"]
estimated_time: 10 minutes
difficulty: beginner
---

# Cowork Folder Architecture

## Overview

This methodology establishes the optimal physical folder structure for Claude Cowork to minimize token consumption and maximize contextual relevance.

## Steps

1. **Create Root Folder**:
   - Create a main directory on your computer named `Claude Cowork`.

2. **Initialize Subfolders**:
   - Create three essential sub-directories:
     - `ABOUT ME/`: For persistent identity and rules.
     - `OUTPUTS/`: For project-specific work.
     - `TEMPLATES/`: For reusable structural skeletons.

3. **Populate Identity Files**:
   - Create 3 core markdown files in `ABOUT ME/`:
     - `about-me.md`: Who you are, your role, how you think.
     - `anti-ai-writing-style.md`: Specific words, patterns, and habits you want Claude to avoid.
     - `my-company.md`: Your current targets, strategy, and "saying no to" list.

4. **Apply Token Limits**:
   - Ensure each file in `ABOUT ME/` is under **2,000 tokens**.
   - If files are larger, use Claude to summarize raw interview transcripts into high-signal prose.

5. **Configure Global Instructions**:
   - In Claude settings (**Settings → Cowork → Edit Global Instructions**), paste instructions that force Claude to read the `ABOUT ME/` folder before every task.
   - Example instruction: `"Before any task, read every file in ABOUT ME/. Never read OUTPUTS/ or TEMPLATES/ unless specifically directed."`

## Success Metric

Claude correctly identifies your role and style without any prompting in a fresh session.

## Sources

- [[cowork-april-2026-update|Cowork (April 2026 update)]]
