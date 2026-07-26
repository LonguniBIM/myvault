# Project Purpose — Claude Code Mastery

## Research Question

> Làm thế nào để am hiểu tường tận cách vận hành của Claude Code, sử dụng nó một cách hiệu quả, tối ưu thời gian và hiệu suất, và tổng hợp kiến thức từ tài liệu thành các Claude Skills có thể tái sử dụng?

## Hypothesis / Working Thesis

> Bất kỳ tài liệu nào mà phương pháp của nó có thể được mô tả thành các bước đánh số đều có tiềm năng trở thành một Claude Skill. Bằng cách hệ thống hóa việc phân tích tài liệu (vấn đề → phương pháp → nguyên tắc → cảnh báo → câu hỏi), ta có thể xây dựng một thư viện Skills tối ưu workflow và hiệu suất khi làm việc với Claude Code.

## Background

Claude Code là một AI coding agent mạnh mẽ nhưng hiệu quả sử dụng phụ thuộc rất nhiều vào cách thiết lập context, rules, skills, và workflow. Nhiều người dùng chỉ dùng Claude Code ở mức cơ bản mà không khai thác được hệ sinh thái rules/skills/memory/hooks. Nghiên cứu này nhằm tổng hợp tất cả kiến thức liên quan để tạo ra một framework sử dụng Claude Code tối ưu.

## Sub-questions

1. Tài liệu này giải quyết vấn đề gì? (Problem identification)
2. Phương pháp của tác giả gồm những bước nào? (Methodology extraction → potential Skill)
3. Tác giả lặp lại những nguyên tắc nào xuyên suốt tài liệu? (Recurring principles → rules/constraints)
4. Tác giả cảnh báo những sai lầm nào cần tránh? (Anti-patterns → guardrails)
5. Tác giả thường đặt ra những câu hỏi nào cho người đọc? (Diagnostic questions → prompts)
6. Tôi có thể mô tả phương pháp của tài liệu này thành các bước được đánh số không? (Skill potential test)

## Scope

**In scope:**
- Official Anthropic documentation (docs.anthropic.com)
- Claude Code CLI features, configuration, hooks, permissions
- CLAUDE.md best practices and patterns
- Agent Skills (.md skill files) — structure, triggers, effectiveness
- Memory systems (neural memory, memory bank, context engineering)
- MCP servers and tool integration
- Workflow optimization (parallel agents, subagents, best-of-N)
- Community best practices (blog posts, GitHub repos, tutorials, videos)
- Prompt engineering specific to Claude Code context

**Out of scope:**
- Claude API usage outside of Claude Code (raw API calls)
- Other AI coding assistants (Copilot, Cursor AI — except for comparison)
- General software engineering practices unrelated to AI-assisted coding
- Claude model internals (training, architecture) beyond what affects usage

## Methodology

- **Capture**: Clip documentation, blog posts, tutorials, GitHub repos via web clipper or manual
- **Analyze**: For each source, answer the 6 sub-questions above
- **Extract**: Identify numbered-step methodologies → candidate Skills
- **Synthesize**: Group findings by theme (setup, workflow, optimization, debugging)
- **Build**: Convert validated methodologies into working SKILL.md files
- **Test**: Apply generated skills in real projects, measure effectiveness
- **Iterate**: Update skills based on usage feedback

## Success Criteria

- Comprehensive entity coverage of Claude Code features and configuration options
- Each methodology source analyzed through the 6-question framework
- Library of ≥10 working Claude Skills derived from research findings
- Clear comparison pages showing which approaches work better and when
- Measurable improvement in Claude Code task completion speed/quality
- Queryable knowledge base that answers "how to X with Claude Code?" questions instantly

## Current Status

> Initialized — workspace structure created, purpose defined. Ready for first content capture.
