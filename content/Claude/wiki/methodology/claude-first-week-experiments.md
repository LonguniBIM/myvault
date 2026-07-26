---
type: methodology
title: Claude First-Week Experiments
created: 2026-05-06
updated: 2026-05-06
tags: [topic:setup, priority:high, confidence:high, skill_status:candidate]
related: ["claude-for-dummies-source", "cowork-feature"]
estimated_time: 5-10 minutes per experiment
difficulty: beginner
---

# Claude First-Week Experiments

## Overview

These four guided experiments introduce new Claude users to core capabilities and establish practical confidence in the first week.

**Recommended pace**: One per day, or complete all in one session.

---

## Experiment 1: Content Rewriting

### Objective
Understand Claude's ability to match writing voice, tone, and style.

### Steps

1. **Find source material**: Locate a document, article, or email you've written (200-500 words)
2. **Prompt Claude**: "Rewrite this [document type] in the style of [target voice/audience]"
   - Example: "Rewrite this email in a casual, friendly tone"
   - Example: "Rewrite this technical explanation for a 10-year-old"
3. **Evaluate output**: Compare Claude's rewrite against your original
4. **Refine**: Ask Claude to adjust tone, length, or emphasis
5. **Document learning**: Note what works vs what needs refinement

### Success Metric
Claude's rewrite captures the essence while matching the target voice.

### Common Mistakes to Avoid
- Asking for rewrites without providing context about target audience
- Treating first output as final (iteration improves results)
- Forgetting to specify tone/voice explicitly

---

## Experiment 2: Document Summarization

### Objective
Leverage Claude's strength with long documents (200+ pages).

### Steps

1. **Find long document**: A PDF, book chapter, research paper, or meeting transcript (50+ pages)
2. **Upload to Claude**: Use desktop app or paste content
3. **Request summary**: "Summarize this document highlighting [key aspects: decisions, findings, action items]"
4. **Evaluate depth**: Check if Claude captured the core points without losing nuance
5. **Follow-up questions**: Ask for specific sections or deeper dives
6. **Extract actionables**: "What are the top 3 action items from this?"

### Success Metric
Claude produces a summary you could brief someone with in 5 minutes.

### Pro Tip (Requires Cowork)
Use Cowork to summarize multiple long documents and synthesize across them.

---

## Experiment 3: Meeting Decision Extraction

### Objective
Develop ability to quickly extract decisions and action items from meeting notes.

### Steps

1. **Gather notes**: Paste meeting transcript or notes (video transcript, handwritten notes scanned)
2. **Request extraction**: "Extract all decisions and action items with owners and deadlines"
3. **Structured format**: Ask Claude to format as:
   - **Decisions made**: (What was decided?)
   - **Action items**: (Who owns what? By when?)
   - **Blockers identified**: (What's holding us back?)
   - **Next meeting focus**: (What needs follow-up?)
4. **Share with team**: Use the extracted structure to communicate outcomes
5. **Iterate**: If Claude missed something, ask follow-up questions

### Success Metric
Team members get clarity on decisions and next steps without re-reading full notes.

---

## Experiment 4: File Folder Organization (Requires Cowork)

### Objective
Use Cowork to automate file categorization and organization.

### Steps

1. **Access local folder**: Give Claude access to a folder with mixed file types
   - Example: Downloads folder, project folder with mixed documents
2. **Define organization scheme**: Specify desired categories
   - Example: "Create folders: [Completed], [In Progress], [For Review], [Archived]"
3. **Request organization**: "Review all files and move them to the appropriate folder based on [criteria]"
   - Example criteria: date, file type, project status, priority
4. **Verify results**: Check that files landed in correct folders
5. **Iterate**: Ask Claude to adjust categorization rules and re-organize if needed

### Success Metric
Files are organized so you can find things faster without manual sorting.

### Requirements
- Claude Pro (for Cowork access)
- Desktop app or local file system integration

---

## Progression Path

**Suggested order for maximum learning**:

1. **Content Rewriting** (5 min) → Understand voice/style matching
2. **Document Summarization** (10 min) → See long-document handling
3. **Meeting Extraction** (5 min) → Apply to real problem
4. **File Organization** (15 min) → Experience Cowork autonomy

---

## Key Learnings from These Experiments

| Experiment | Core Learning |
|------------|---------------|
| **Rewriting** | Claude excels at capturing tone and adapting style |
| **Summarization** | Long-document processing is a genuine strength |
| **Meeting extraction** | Structured output requests improve usability |
| **File organization** | Cowork automates multi-step workflows effectively |

---

## Troubleshooting

### Claude didn't capture the right tone
- Provide more explicit tone guidance: "casual, like texting a friend" vs "formal, like legal documentation"
- Give an example of your desired tone
- Ask Claude to critique its own output

### Summary was too long/short
- Specify length: "1-paragraph summary" or "2-page summary"
- Define what to emphasize: "focus on decisions, not background"
- Ask for a second pass: "condense further, 30% shorter"

### File organization moved files incorrectly
- Review the criteria Claude used
- Provide clearer categorization rules
- Ask Claude to explain its logic for disputed files

---

## Sources

- [[claude-for-dummies-source|Claude for Dummies]] (Ruben Hassid)

## See Also

- [[cowork-feature]]
- [[claude-ai-assistant]]
- [[claude-negotiation-preparation|Negotiation Preparation Workflow]]

## Skill Status

**Candidate for deployment** as an interactive onboarding skill for new Claude users.
