# Project Purpose — HTU Trading Knowledge Base

## Research Question

> Làm thế nào để trích xuất và đúc kết có hệ thống các kiến thức giao dịch từ tài liệu rời rạc thành một bộ quy tắc (Playbook) có tính thực thi cao, và từ đó xây dựng thành workflow + Claude Skills có thể tái sử dụng?

## Hypothesis / Working Thesis

> Bất kỳ hệ thống giao dịch nào có thể được mô tả qua 4 lớp lọc — Thận trọng (Caution), Vùng giá trị (Structure), Điểm vi phạm (Invalidation), và Xác nhận vào lệnh (Execution) — đều có tiềm năng trở thành một Claude Skill. Bằng cách luôn áp dụng bộ 12 câu hỏi chuẩn (nhóm A–D) vào mọi tài liệu mới, ta có thể biến thông tin thô thành Playbook nhất quán và kiểm chứng được.

## Background

Kiến thức giao dịch phân tán dưới nhiều hình thức — video, PDF, tweet thread, livestream — và thường thiếu tính nhất quán: không rõ điểm vi phạm, không xác định khung giờ hành động, không có tiêu chí kết thúc một pha. Repo này lấy **Expansion Model** (themarketlens.com) làm khung tham chiếu: một hệ thống đi từ bối cảnh vĩ mô → cấu trúc thị trường → điểm xác nhận cụ thể, với 4 lớp lọc chặt chẽ. Mọi tài liệu giao dịch mới đều được đối chiếu với khung này để đánh giá mức độ hoàn chỉnh và tiềm năng xây dựng thành Skill.

## Sub-questions

### Nhóm A — Bối cảnh và Thời điểm (Timing & Context)

1. Những khoảng thời gian hoặc sự kiện nào hệ thống yêu cầu **đứng ngoài**? (Caution Protocol)
2. Mối liên hệ giữa các ngày trong tuần là gì? (Ví dụ: dùng nến thứ Hai để dự đoán bias)
3. Các khung giờ cụ thể (Time windows / Killzones) nào quan trọng nhất để quan sát phản ứng giá?

### Nhóm B — Cấu trúc và Biên độ (Structure & Range)

4. Đâu là các điểm xoay (Swings) có giá trị? Làm thế nào phân biệt Swing "được bảo vệ" (Protected) với Swing yếu?
5. Thị trường đang ở loại biên độ nào: External, Internal, hay Neutral?
6. Tín hiệu nào cho thấy sự chuyển đổi từ trạng thái đi ngang (Range) sang mở rộng (Expansion)?

### Nhóm C — Điểm Vi phạm và Sai số (Invalidation)

7. Điểm cụ thể nào (giá đóng cửa, râu nến, Equilibrium) nếu bị vượt qua sẽ làm thay đổi hoàn toàn kịch bản (Bias)?
8. Sự khác biệt giữa điểm vi phạm của ngày Đảo chiều (Reversal) và ngày Tiếp diễn (Continuation) là gì?
9. Phản ứng giá tại các cấp độ quan trọng như thế nào thì được coi là "tôn trọng" (Respecting)?

### Nhóm D — Tín hiệu và Thực thi (Execution & Entry)

10. Các khung giờ "vàng" (Killzones) đóng vai trò gì: thiết lập điểm cao/thấp hay xác nhận hướng đi?
11. Tín hiệu xác nhận (Signature) ở khung thời gian thấp (LTF: M15/M5) là gì?
12. Các mục tiêu giá (Objectives) nằm ở đâu và làm thế nào để biết một pha Expansion đã hoàn tất?

## Scope

**In scope:**
- Hệ thống giao dịch dựa trên cấu trúc thị trường (Market Structure, Smart Money, ICT)
- Phân tích đa khung thời gian (HTF context → LTF execution)
- Killzones, session analysis, News protocol
- Swing analysis, Range classification (External / Internal / Neutral)
- Invalidation rules và Bias confirmation
- Backtesting notes và empirical observations
- Tài liệu: video, PDF, tweet thread, livestream, blog

**Out of scope:**
- Giao dịch thực tế (live execution) và quản lý tài khoản
- Phân tích cơ bản thuần túy (macro fundamentals không liên quan cấu trúc)
- Chỉ báo kỹ thuật truyền thống không gắn với cấu trúc (RSI, MACD độc lập)
- Lời khuyên tài chính hoặc tín hiệu giao dịch cụ thể

## Methodology

- **Capture**: Thu thập tài liệu qua web clipper, transcript video, PDF — lưu vào `raw/sources/`
- **Analyze**: Với mỗi nguồn, trả lời đủ 12 câu hỏi (Nhóm A → D)
- **Map**: Vẽ luồng logic dạng cây quyết định (If... Then...) — không ghi chép rời rạc
- **Classify**: Phân loại theo màu — Đỏ (Invalidation/SL), Xanh (Confirmation/Entry), Vàng (Context)
- **Validate**: Kiểm tra tính nhất quán — nếu tài liệu không trả lời được câu hỏi về Invalidation thì chưa đủ điều kiện build Skill
- **Synthesize**: Nhóm theo chủ đề (Timing, Structure, Invalidation, Execution)
- **Build**: Chuyển Playbook đã xác thực thành SKILL.md cho Claude
- **Test**: Áp dụng Skill trong phân tích thực tế, ghi nhận hiệu quả
- **Iterate**: Cập nhật Skill dựa trên phản hồi thực chiến

## Success Criteria

- Mọi tài liệu mới đều được phân tích qua đủ 12 câu hỏi (Nhóm A–D)
- Mỗi hệ thống giao dịch được vẽ thành cây quyết định có Invalidation rõ ràng
- Thư viện ≥5 Claude Skills giao dịch có thể tái sử dụng (phân tích session, xác định Range, đọc Swing, v.v.)
- Knowledge base trả lời được câu hỏi "Trong điều kiện X, hành động tiếp theo là gì?" trong <30 giây
- Phương pháp mới bất kỳ đều có thể được đánh giá mức độ hoàn chỉnh dựa trên 4-layer framework

## Current Status

> Initialized — purpose viết lại theo framework Expansion Model. Sẵn sàng ingest tài liệu đầu tiên.
