---
type: concept
title: "Tokens: Unit of Conversation Memory"
created: 2026-05-06
updated: 2026-05-06
tags: [topic:setup, priority:high, confidence:high]
related: ["auto-complete-at-scale", "claude-ai-assistant"]
---

# Tokens: Fundamental Unit of LLM Memory

## Definition

**Tokens** are roughly word-sized units that form the basis of Claude's conversation memory limits. Understanding tokens is essential to understanding why conversations have practical length limits.

## Basic Properties

- **Size**: Approximately 1 token per word (with some variation)
- **Function**: Claude processes and remembers conversations token-by-token
- **Limits**: Different pricing tiers have different context window sizes
- **Cost**: Tokens consumed determine pricing in API usage

## Why This Matters

### Conversation Length
A 200-page document (≈80,000 words) requires roughly 80,000 tokens. Claude can handle this because its context window accommodates it, but once the token limit is reached, older information is lost.

### Pricing
- **Pro users**: Larger token allowances per day than free users
- **API users**: Pay per token consumed (input + output)
- **Max tier**: For heavy daily usage with large token budgets

## Token-Efficient Practices

1. Summarize old conversations to preserve context
2. Break very long documents into sections
3. Be explicit about what information to prioritize
4. Clear irrelevant context to make room for new information

## Technical Note

Tokens don't map 1:1 to words due to:
- Multi-character tokens (common words are single tokens)
- Punctuation handling
- Language-specific variations

## Sources

- [[claude-for-dummies-source|Claude for Dummies]] (Ruben Hassid)

## See Also

- [[auto-complete-at-scale]]
- [[claude-ai-assistant]]
