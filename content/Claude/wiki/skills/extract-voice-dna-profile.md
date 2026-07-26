---
name: extract-voice-dna-profile
description: A 2-hour workflow to capture your writing DNA, beliefs, and "taste" into a portable context file.
type: skill
trigger: "When you want Claude to write, judge, and think exactly like you across all sessions."
time_estimate: "2 hours"
difficulty: "hard"
prerequisites:
  - Claude Pro/Max (Opus 4.7 + Extended Thinking)
  - Wispr Flow (recommended for voice speed)
tags:
  - identity
  - voice
  - context
  - patterns
related:
  - "[[I Can Be You]]"
created: 2026-05-10
updated: 2026-05-10
---

# Extract Voice DNA Profile

## Why This Matters

Vagueness in prompts leads to "generic AI" outputs. By extracting your specific patterns (words you hate, analogies you love, core beliefs), you create a "Voice Profile" that makes you portable across any AI tool.

## The Skill

Run a deep 100-question interview and compress it into a high-fidelity XML/Markdown context file.

## Steps

### Phase 1: The 100-Question Interview (90 mins)

1. Open a fresh Claude chat (Opus 4.7 + Extended Thinking).
2. Use the **Taste Interviewer** prompt (see source for full prompt) to trigger 100 questions across:
   - Beliefs & Contrarian Takes
   - Writing Mechanics
   - Aesthetic Crimes (Cringes)
   - Voice & Personality
   - Structural Preferences
3. Use **Wispr Flow** to dictate answers verbatim. One question at a time.
4. Do not settle for vague answers; push Claude to push *you*.

### Phase 2: The Voice Compiler (30 mins)

1. Once the interview is complete, use the **Voice Compiler** prompt to turn the 20,000-word dump into a compact file.
2. Target: 2,000–4,000 tokens.
3. Structure: XML-style tags (`<writing_laws>`, `<hard_refusals>`, `<taste_disgusts>`).
4. Rule: If a line doesn't change how the AI writes or decides, cut it.

### Phase 3: Deployment & Maintenance

1. Save the result as `about-me.md`.
2. Move it to your root `Claude Cowork` folder.
3. **Continuous Maintenance**: Use Obsidian to edit your profile as your taste evolves. Review every 3 months.

## Watch Out For

- **Stopping at the Transcript**: 20,000 words is too much for every session. Compression is mandatory.
- **Bio-padding**: AI needs your *laws*, not your life story.
- **Generic Adjectives**: "I like it simple" means nothing. Use examples of "simple done right" vs. "simple done lazy."

## Source

**Article**: [[I Can Be You]]  
**Author**: [[Ruben Hassid]]  
**Published**: 2026-05-03
---
