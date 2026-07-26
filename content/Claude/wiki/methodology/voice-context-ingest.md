---
type: methodology
title: Voice-Driven Context Extraction
created: 2026-05-10
updated: 2026-05-10
tags: [topic:setup, topic:prompts, priority:high, confidence:high, skill_status:candidate]
related: ["cowork-april-2026-update", "wispr-flow"]
estimated_time: 15-20 minutes
difficulty: beginner
---

# Voice-Driven Context Extraction

## Overview

This method solves the "human bottleneck" by using dictation to feed rich, high-context information into Claude Cowork for profile building.

## Steps

1. **Install Dictation Layer**:
   - Download and install **Wispr Flow** (or equivalent 150+ wpm dictation tool).
   - Set a comfortable activation hotkey (e.g., `Shift` or `Caps Lock`).

2. **Trigger the Interview**:
   - Start a fresh Cowork session using **Opus 4.6**.
   - Paste the "About Me Interview" prompt (found in [[cowork-april-2026-update#Method 2]]).

3. **"Yapping" Phase**:
   - When Claude asks a question via `AskUserQuestion`, hold the dictation key.
   - Speak naturally. Do not self-edit. Provide specific examples and "vent" about bad work habits.
   - Aim for 150+ words per answer.

4. **Pattern Extraction**:
   - Once the interview is complete, command Claude: `"Do not save raw transcripts. Extract the underlying patterns and write them as condensed prose/bullets."`
   - Review the output to ensure it captures your "voice" without the verbal filler.

5. **File Finalization**:
   - Save the result as `about-me.md` in your `ABOUT ME/` folder.

## Success Metric

The resulting markdown file feels like a professional summary of your thinking that you couldn't have typed manually in under an hour.

## Sources

- [[cowork-april-2026-update|Cowork (April 2026 update)]]
