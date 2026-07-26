---
type: concept
title: 23 Token-Saving Habits
tags: [optimization, tokens, workflow, efficiency]
related: "[[tokens-concept]], [[cowork-workflows]], [[model-routing]], [[dictation-prompting]]"
created: 2026-05-09
updated: 2026-05-09
---

# 23 Token-Saving Habits

A curated collection of 23 practical techniques for reducing token consumption in Claude workflows without sacrificing quality or speed.

## Categories

### Input Optimization
- Use structured formats (YAML, JSON) instead of prose descriptions
- Leverage context files (about-me.md, DESIGN.md) instead of inline context
- Reference external documentation via MCP servers instead of copying content

### Model Routing
- Route simple tasks to [[claude-haiku]] (cheaper, faster)
- Reserve [[claude-opus]] for complex reasoning and multi-step workflows
- Use [[claude-sonnet]] as the balanced default

### Workflow Patterns
- Batch similar operations to amortize context setup
- Use [[background-tasks]] to avoid re-reading logs
- Leverage [[cowork-projects]] scoped memory instead of global context

### Dictation & Voice
- Use [[whisper-flow]] for voice input (natural language is often more concise)
- Pre-structure thoughts before dictating
- Use [[dictation-prompting-workflow]] for consistent voice

## Semantic Similarity

This concept is semantically similar to [[token-concept]] — understanding token mechanics enables better optimization strategies.

## Related Workflows

- [[cowork-workflows]] — Where token-saving habits are applied
- [[model-routing]] — Choosing the right model for the task

> [!info] God Node
> 23 Token-Saving Habits is a highly-connected concept (6 edges), suggesting it's a central concern across multiple Claude workflows.
