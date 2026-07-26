---
name: audit-and-fix-ai-writing-style
description: Detect and remove robotic patterns like negative parallelism and banned vocabulary to make AI text sound human.
type: skill
trigger: "When AI-generated text sounds robotic, over-polished, or uses repetitive patterns."
time_estimate: "5 minutes"
difficulty: "easy"
prerequisites:
  - anti-ai-writing-style.md file
tags:
  - editing
  - humanize
  - writing
  - audit
related:
  - "[[It'S Not X, It'S Y]]"
created: 2026-05-10
updated: 2026-05-10
---

# Audit and Fix AI Writing Style

## Why This Matters

AI writing has distinct, detectable patterns that kill engagement (e.g., the "It's not X, it's Y" pattern). This skill provides a mechanical way to audit and strip these patterns out.

## The Skill

Use a persistent `anti-ai-writing-style.md` file to audit and regenerate text.

## Steps

### 1. Build the Audit File

Create an `anti-ai-writing-style.md` containing:
- **Hard Bans**: Negative parallelism ("This isn't X. This is Y."), rule of three, puffery, and metronome rhythm.
- **Banned Words**: 100+ words like "delve," "harness," "unlock," "leverage."
- **Pacing Rules**: Short paragraphs (1-2 sentences), varied rhythm.

### 2. The Audit Trigger

1. After Claude generates a draft, use the prompt:
   `"Audit this text against my anti-ai-writing-style.md file."`
2. If Claude misses a pattern, prompt:
   `"You missed the negative parallelism in section [X]. Fix it and be more aggressive with the banned word list."`

### 3. The Fix Logic

When a "reframe" (It's not X, it's Y) is found:
1. Delete the rejected half (the "It's not X" part).
2. Rewrite the positive claim as a direct, literal sentence.
   *Example: "It's not about the prompt. It's about context." → "Context controls the output."*

## Watch Out For

- **Throat-Clearing**: AI likes to announce what it's about to do. Delete these openings.
- **Inflated Significance**: "A pivotal moment" → Just state what happened.
- **Variation Overload**: Swapping names to avoid repetition. Just use the name again.

## Success Criteria

- [ ] All "negative parallelism" patterns removed.
- [ ] No words from the 100+ banned list present.
- [ ] Paragraphs average 1.5 sentences.

## Source

**Article**: [[It'S Not X, It'S Y]]  
**Author**: [[Ruben Hassid]]  
**Published**: 2026-04-29
