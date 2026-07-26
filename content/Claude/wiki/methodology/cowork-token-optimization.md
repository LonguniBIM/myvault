---
type: methodology
title: Cowork Token Optimization
created: 2026-05-10
updated: 2026-05-10
tags: [topic:optimization, priority:high, confidence:high, skill_status:candidate]
related: ["cowork-april-2026-update", "tokens-concept"]
estimated_time: Ongoing
difficulty: intermediate
---

# Cowork Token Optimization

## Overview

A set of operational habits to minimize unnecessary token consumption in Claude Cowork sessions.

## Steps

1. **The Restart Habit**:
   - Instead of typing "No, I meant..." or corrective follow-ups, click **"Restart the conversation from here"** on a previous message.
   - This prevents stacking full history + correction on every subsequent turn.

2. **The 20-Message Rule**:
   - Every 20 exchanges, ask Claude to: `"Summarize our progress, decisions, and current state concisely."`
   - Copy the summary, start a **fresh Cowork session**, and paste the summary as message #1.

3. **Multi-Task Batching**:
   - Group related requests into a single prompt.
   - *Bad:* "Summarize." -> (response) -> "Now list items."
   - *Good:* "Summarize this AND list the action items in a single response."

4. **Model Tiering**:
   - Use **Sonnet** or **Haiku** for grammar checks, simple formatting, and brainstorming.
   - Reserve **Opus 4.6 + Extended Thinking** only for architectural changes, complex synthesis, or when a session reaches high complexity.

5. **Profile Maintenance**:
   - Audit your `ABOUT ME/` files monthly.
   - Use Claude to prune any information that is no longer current or relevant.

## Success Metric

Context window usage remains under 50% for standard tasks, avoiding the "loose summary" failure mode.

## Sources

- [[cowork-april-2026-update|Cowork (April 2026 update)]]
