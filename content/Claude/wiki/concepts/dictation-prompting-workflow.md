---
type: concept
title: Dictation Prompting Workflow
tags: [workflow, efficiency, voice, prompts]
related: ["[[whisper-flow]]", "[[wispr-flow]]", "[[cowork-token-optimization]]"]
created: 2026-05-10
updated: 2026-05-10
---

# Dictation Prompting Workflow

The **Dictation Prompting Workflow** is an efficiency-first method for generating high-context Claude prompts using voice input. It leverages the speed of speech (150+ words per minute) vs. typing (40-80 words per minute) to provide more detail with less friction.

## Process

1. **Think**: Brief mental outline of the goal.
2. **Speak**: Use a tool like [[whisper-flow]] or [[wispr-flow]] to dictate the task, context, and constraints.
3. **Clean**: Let Claude or a dedicated "Voice Compiler" prompt normalize the messy transcription into a structured prompt.
4. **Execute**: Run the cleaned prompt in Claude Code or Cowork.

## Key Advantages

- **High Context**: Users are more likely to explain "the why" when speaking, leading to better AI performance.
- **Lower Friction**: Reduces the "blank page" problem of starting a complex task.
- **Token Efficiency**: By dictating into a text file first ([[files-replace-prompts]]), you can curate the context before sending it to Claude, preventing token waste.

## Part of Ecosystem

This workflow is a core component of the **[[cowork-token-optimization|Cowork Token-Saving Habits]]** and is the primary source of context for the **[[voice-context-ingest]]** pipeline.

> [!info] Tip
> Use "Technical Dictation" — verbally describing the folder structure or code blocks you want to modify — to jumpstart [[vibecoding]] sessions.
