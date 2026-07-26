---
name: optimize-claude-token-usage
description: 23 habits to minimize token consumption and avoid hitting Claude usage limits.
type: skill
trigger: "When you are hitting Claude usage limits early in the day or want to reduce API/credit costs."
time_estimate: "Immediate (Habit-based)"
difficulty: "easy"
prerequisites:
  - Claude Pro/Max account
tags:
  - optimization
  - tokens
  - cost-saving
  - limits
related:
  - "[[How To Stop Hitting Claude Usage Limits]]"
created: 2026-05-10
updated: 2026-05-10
---

# Optimize Claude Token Usage

## Why This Matters

Claude re-reads your entire conversation history for every new message. Message 30 is exponentially more expensive than message 1. Inefficient habits lead to "usage limit frustration" and wasted money.

## The Skill

Apply habit-based techniques to reduce token burn by up to 70%.

## Steps

### 1. File Optimization

- **Convert Before Upload**: Extract text from PDF/DOCX into a plain `.txt` or `.md` file. (A 3,000-token PDF page becomes 200 tokens of text).
- **Tight Crops**: Crop screenshots to only the essential area (reduces cost from 1,300 tokens to <100).

### 2. Interaction Design

- **Batch Tasks**: Combine instructions (e.g., "Summarize, list points, and suggest headline") into one message.
- **The Edit Hack (Chat)**: Click "Edit" on your original message to fix it and regenerate, rather than sending a follow-up.
- **Restart (Cowork)**: Use "Restart the conversation from here" higher up in the history to clear the stack.
- **AskUserQuestion Tool**: Use short prompts ("Read folder. Ask me questions.") to let Claude pull context via UI clicks, which are cheaper than walls of text.

### 3. Product Selection

- **Plan in Chat, Build in Cowork**: Do structure and thinking in the "cheaper" Chat product; move to "expensive" Cowork only for final file building.
- **Match the Model**: Use Sonnet/Haiku for grammar, formatting, and quick questions. Reserve Opus for deep reasoning.

### 4. Context Hygiene

- **Keep Profiles Lean**: Ensure `about-me.md` and `CLAUDE.md` are under 2,000 tokens.
- **Topic Isolation**: Start a new chat for every new topic. Don't carry unrelated "dead weight" history.

## Habits to Pick First

1. Convert text-only files before uploading.
2. Edit messages instead of sending follow-ups.
3. Use the "Restart from here" feature frequently.

## Watch Out For

- **"No, I meant..." follow-ups**: These are "token furnaces."
- **Full Redos**: Don't say "redo the report." Say "only redo section 3" to save thousands of output tokens.
- **Peak Hour Costs**: Avoid heavy tasks during peak hours (5-11 AM Pacific) if on a per-token API plan.

## Source

**Article**: [[How To Stop Hitting Claude Usage Limits]]  
**Author**: [[Ruben Hassid]]  
**Published**: 2026-04-12
