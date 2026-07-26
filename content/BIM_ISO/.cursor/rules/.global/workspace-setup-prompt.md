# Workspace Setup Prompt Template

Copy the prompt below and paste into a new Cursor chat when setting up a new workspace. Replace `<placeholders>` with actual values.

---

## Prompt

```
Hãy đọc codebase và tiến hành setup đầy đủ cho workspace này. Lần lượt thực hiện các bước sau:

### Step 1: Serena — Activate & Onboard
1. Gọi `activate_project` với tham số **`project`** (KHÔNG dùng `project_name`) — ví dụ: `activate_project(project="F:\path\to\workspace")`.
2. Gọi `onboarding` — đọc codebase, tạo các memory files:
   - `project_overview` (mục đích, cấu trúc, tools)
   - `suggested_commands` (dev commands, build, test, git, system utils cho OS hiện tại)
   - `style_and_conventions` (code style, naming, commit conventions)
   - `task_completion_checklist` (verify, quality, docs, git steps)
3. Gọi `check_onboarding_performed` để xác nhận hoàn tất.

### Step 2: Memory Bank
Tạo thư mục `memory-bank/` với 7 core files:
| File | Nội dung |
|------|----------|
| `projectbrief.md` | Mục đích, core requirements, target platform |
| `productContext.md` | Lý do tồn tại, user flow, UX goals |
| `techContext.md` | Tech stack, dev setup, constraints, dependencies |
| `systemPatterns.md` | Architecture overview, design patterns |
| `activeContext.md` | Current state, active work focus, next steps |
| `progress.md` | Completed, remaining, known issues |
| `decisionLog.md` | Chronological decisions (DEC-001, DEC-002...) |

Nội dung phải dựa trên phân tích codebase thực tế, không dùng placeholder.

### Step 3: GitNexus Setup
1. Chạy `npx gitnexus analyze` để index codebase.
2. Tạo 2 Cursor rules trong `.cursor/rules/.global/`:
   - `neural-memory-workflow.mdc` (alwaysApply: true) — recall/remember lifecycle
   - `gitnexus-neural-bridge.mdc` (alwaysApply: true) — cross-reference workflow
3. Copy bridge script từ template sang `.cursor/skills/.global/gitnexus/gitnexus_bridge.py`.
4. Chạy bridge script: `python .cursor/skills/.global/gitnexus/gitnexus_bridge.py --repo <RepoName>`
   → Tạo ra `memory-bank/codebaseGraph.md` + `memory-bank/codebase_graph_summary.json`.
5. Seed Neural-Memory với key insights từ codebase graph (facts, decisions, insights, workflows).

### Step 4: Verify mcp-feedback-enhanced
1. Kiểm tra file `.cursor/rules/.global/mcp-feedback-enhanced.mdc` tồn tại và có `alwaysApply: true`. (Đường dẫn đã đúng)
2. Xác nhận rule hoạt động đúng: gọi `interactive_feedback` ở Phase 1 (trước khi bắt đầu) và Phase 2 (sau khi hoàn thành).
3. Đảm bảo luôn đợi confirmation của user trước khi tiến hành và sau khi hoàn thành.

### Verification Checklist
Sau khi hoàn tất, chạy checklist xác nhận:
- [ ] Git repo exists
- [ ] memory-bank/ có 7+ files (.md)
- [ ] .cursor/rules/.global/ có neural-memory-workflow.mdc và gitnexus-neural-bridge.mdc
- [ ] .cursor/skills/.global/gitnexus/gitnexus_bridge.py exists
- [ ] GitNexus index exists (.gitnexus/)
- [ ] memory-bank/codebaseGraph.md generated
- [ ] memory-bank/codebase_graph_summary.json generated
- [ ] Neural-Memory seeded (nmem_recall trả về kết quả)
- [ ] mcp-feedback-enhanced rule active
```

---

## Notes
- Prompt này yêu cầu MCP servers: `user-serena`, `user-neural-memory`, `user-gitnexus`, `user-mcp-feedback-enhanced`.
- GitNexus cần Node.js >= 18 và git repo đã được initialized.
- Bridge script cần Python 3.8+ (stdlib only, không cần pip install thêm).
- Thời gian setup trung bình: 3-5 phút (tùy kích thước codebase).
