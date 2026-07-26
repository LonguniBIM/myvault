# Project Purpose — BIM ISO 19650 Mastery

## Research Question

> Làm thế nào để hiểu có hệ thống các nguyên tắc, yêu cầu và quy trình của BIM theo ISO 19650; chuyển hóa chúng thành các phương pháp có thể áp dụng trong dự án thực tế; đồng thời tổng hợp kiến thức từ tiêu chuẩn, tài liệu hướng dẫn và bài học dự án thành các Claude Skills có thể tái sử dụng?

## Hypothesis / Working Thesis

> Mọi yêu cầu BIM ISO có thể triển khai hiệu quả khi được chuyển đổi từ ngôn ngữ tiêu chuẩn thành các thành phần vận hành rõ ràng: mục tiêu thông tin → vai trò và trách nhiệm → yêu cầu đầu vào → quy trình thực hiện → điểm kiểm soát → bằng chứng tuân thủ → đầu ra cần bàn giao. Nếu một quy trình có thể được mô tả thành các bước, điều kiện, câu hỏi chẩn đoán và tiêu chí nghiệm thu, quy trình đó có tiềm năng được đóng gói thành một Claude Skill để hỗ trợ triển khai BIM nhất quán giữa nhiều dự án.

## Background

ISO 19650 cung cấp khung quản lý thông tin trong toàn bộ vòng đời tài sản xây dựng, nhưng nội dung tiêu chuẩn thường mang tính nguyên tắc và cần được diễn giải thành quy trình cụ thể trước khi áp dụng vào dự án.

Trong thực tế, các nhóm dự án thường gặp khó khăn khi chuyển từ yêu cầu trong ISO, EIR/AIR, BEP, MIDP/TIDP hoặc CDE workflow sang các hành động có thể thực hiện trong Revit, IFC, hệ thống kiểm tra mô hình, quy trình phối hợp và quản lý bàn giao. Sự khác biệt giữa cách hiểu của từng cá nhân hoặc từng bộ môn có thể dẫn đến thiếu thông tin, sai cấu trúc dữ liệu, không rõ trách nhiệm, kiểm tra không nhất quán và khó chứng minh mức độ tuân thủ.

Nghiên cứu này nhằm xây dựng một knowledge framework về BIM ISO 19650, kết nối kiến thức tiêu chuẩn với tình huống dự án thực tế và chuyển các phương pháp đã được kiểm chứng thành thư viện Claude Skills. Các Skills này sẽ hỗ trợ phân tích yêu cầu, lập kế hoạch triển khai, kiểm tra tài liệu, đánh giá mô hình, chuẩn hóa workflow và tạo bằng chứng tuân thủ.

## Sub-questions

1. Tài liệu hoặc điều khoản này đang giải quyết vấn đề quản lý thông tin nào? (Problem identification)
2. Yêu cầu này áp dụng cho giai đoạn, tổ chức, vai trò hoặc loại thông tin nào? (Applicability and responsibility)
3. Quy trình được mô tả gồm những bước, quyết định và điểm kiểm soát nào? (Methodology extraction → potential Skill)
4. Những đầu vào, đầu ra và bằng chứng nào cần có để chứng minh việc thực hiện? (Inputs, deliverables and evidence)
5. Những nguyên tắc hoặc yêu cầu nào được lặp lại xuyên suốt các tài liệu? (Recurring principles → rules/constraints)
6. Những sai sót, hiểu nhầm hoặc anti-pattern nào thường xảy ra khi áp dụng vào dự án? (Risks → guardrails)
7. Nội dung này cần được chuyển hóa như thế nào thành checklist, template, validation rule hoặc workflow thực tế? (Operationalization)
8. Tôi có thể mô tả phương pháp này thành các bước đánh số, điều kiện kích hoạt và tiêu chí hoàn thành không? (Skill potential test)
9. Claude Skill được tạo ra sẽ hỗ trợ vai trò nào, tại thời điểm nào và tạo ra đầu ra gì? (Skill trigger and outcome)
10. Phương pháp này cần được kiểm thử trên dự án thực tế như thế nào trước khi tái sử dụng? (Validation and feedback)

## Scope

**In scope:**
- ISO 19650-1 và ISO 19650-2 về khái niệm và quản lý thông tin trong giai đoạn delivery
- Các phần ISO 19650 khác khi liên quan đến vận hành, trao đổi thông tin, an toàn thông tin hoặc quản lý tài sản
- EIR, AIR, OIR, PIR, BEP, MIDP, TIDP, Responsibility Matrix và Information Delivery Milestones
- Common Data Environment (CDE), trạng thái thông tin, revision, status, suitability và approval workflow
- Vai trò appointing party, lead appointed party, appointed party và task team
- Level of Information Need, yêu cầu hình học, dữ liệu thuộc tính và tài liệu
- Naming convention, classification, metadata, container identification và file exchange
- Workflow phối hợp BIM giữa Revit, IFC, Navisworks, Revizto, BIMcollab và các hệ thống CDE
- Model checking, information validation, QA/QC, issue management và evidence of compliance
- Quy trình authoring, review, approve, authorize, publish, archive và handover
- Áp dụng ISO 19650 vào dự án thiết kế, thi công, phối hợp MEP và quản lý tài sản
- Tài liệu hướng dẫn từ UK BIM Framework, buildingSMART, BSI, BRE và các nguồn chuyên ngành đáng tin cậy
- Bài học thực tế, case study, template, checklist và quy trình nội bộ
- Claude Skills dùng để phân tích yêu cầu, tạo checklist, review BEP, đánh giá CDE workflow, kiểm tra mô hình và hỗ trợ quyết định BIM

**Out of scope:**
- Các quy trình BIM không liên quan đến quản lý thông tin hoặc mục tiêu tuân thủ đã xác định
- Hướng dẫn sử dụng phần mềm ở mức cơ bản nếu không gắn với yêu cầu BIM ISO
- Tự động hóa hoặc lập trình add-in không phục vụ trực tiếp cho workflow quản lý và kiểm tra thông tin
- Diễn giải pháp lý thay cho tư vấn pháp lý hoặc đánh giá chứng nhận chính thức
- Áp dụng máy móc cùng một template cho mọi dự án mà không xét đến hợp đồng, giai đoạn và yêu cầu thông tin
- Các tuyên bố “ISO compliant” không có tiêu chí kiểm tra và bằng chứng dự án cụ thể

## Methodology

- **Capture**: Thu thập tiêu chuẩn, hướng dẫn, EIR/BEP mẫu, tài liệu đào tạo, case study, checklist và bài học từ dự án thực tế
- **Classify**: Phân loại nguồn theo chủ đề, giai đoạn dự án, vai trò, loại yêu cầu thông tin và mức độ thẩm quyền
- **Analyze**: Với mỗi nguồn, trả lời các sub-questions và xác định nội dung được hỗ trợ trực tiếp bởi tài liệu
- **Map**: Liên kết yêu cầu tiêu chuẩn với tài liệu dự án, vai trò chịu trách nhiệm, phần mềm, dữ liệu và deliverable tương ứng
- **Extract**: Trích xuất quy trình có thể mô tả thành các bước, decision tree, checklist hoặc validation rule
- **Operationalize**: Chuyển ngôn ngữ tiêu chuẩn thành hành động dự án, điểm kiểm soát, tiêu chí pass/fail và bằng chứng cần lưu
- **Synthesize**: Tổng hợp kiến thức theo các nhóm như information requirements, BEP, CDE, delivery planning, model validation, coordination và handover
- **Build**: Chuyển các phương pháp đã xác thực thành Claude Skills với trigger, scope, required inputs, workflow, guardrails và output format rõ ràng
- **Test**: Áp dụng Skills trên tài liệu và dữ liệu dự án thực tế; so sánh kết quả với chuyên gia BIM hoặc quy trình đã được phê duyệt
- **Measure**: Theo dõi thời gian thực hiện, độ đầy đủ, số lỗi phát hiện, mức độ nhất quán và khả năng tái sử dụng
- **Iterate**: Cập nhật knowledge base và Skills dựa trên thay đổi tiêu chuẩn, phản hồi dự án và các trường hợp ngoại lệ mới

## Skill Candidate Areas

- Phân tích EIR/AIR và tạo Requirement Register
- Review BEP theo yêu cầu ISO 19650 và yêu cầu dự án
- Tạo hoặc kiểm tra Responsibility Matrix
- Xây dựng MIDP/TIDP và kiểm tra tính liên kết
- Đánh giá CDE workflow, status, revision và approval gates
- Kiểm tra naming convention và metadata của information containers
- Xây dựng Model QA/QC checklist theo giai đoạn
- Chuyển yêu cầu thông tin thành Revit parameter hoặc IFC property mapping
- Đánh giá Level of Information Need cho từng use case
- Kiểm tra readiness trước khi issue, publish hoặc handover
- Phân tích non-conformance và đề xuất corrective action
- Tạo project-specific BIM ISO implementation plan
- Tổng hợp lesson learned thành rule, guardrail và reusable workflow

## Success Criteria

- Bao phủ có hệ thống các khái niệm, vai trò, tài liệu và workflow cốt lõi của ISO 19650
- Mỗi nguồn được phân tích bằng cùng một framework và có traceability đến nội dung gốc
- Mỗi yêu cầu quan trọng được liên kết với hành động dự án, người chịu trách nhiệm, deliverable và bằng chứng
- Xây dựng được knowledge base có thể trả lời các câu hỏi như “yêu cầu này áp dụng khi nào?”, “ai chịu trách nhiệm?” và “cần kiểm tra bằng cách nào?”
- Thư viện có ít nhất 10 Claude Skills hoạt động được, mỗi Skill có trigger, input, workflow, guardrails và output rõ ràng
- Skills tạo ra kết quả nhất quán khi áp dụng cho nhiều tài liệu hoặc nhiều dự án có cấu hình khác nhau
- Có các comparison page giải thích phương án nào phù hợp với từng loại dự án, giai đoạn và mức độ trưởng thành BIM
- Giảm thời gian phân tích EIR/BEP, chuẩn bị checklist và thực hiện BIM QA/QC
- Tăng khả năng phát hiện thiếu sót, mâu thuẫn và yêu cầu chưa được phân công
- Các kết luận về tuân thủ đều có traceability và không vượt quá bằng chứng từ tài liệu dự án
- Có quy trình review, versioning, testing và deprecation cho Claude Skills

## Expected Outputs

- Knowledge map về BIM ISO 19650 và quan hệ giữa các khái niệm
- Glossary song ngữ cho các thuật ngữ quan trọng
- Source analysis notes theo framework chuẩn
- Requirement Register có traceability đến nguồn
- Bộ template cho BEP review, MIDP/TIDP, Responsibility Matrix và CDE assessment
- Bộ checklist BIM QA/QC theo giai đoạn dự án
- Project implementation playbook cho BIM ISO 19650
- Thư viện Claude Skills và tài liệu hướng dẫn sử dụng
- Skill test cases, evaluation criteria và usage log
- Lesson-learned register để cập nhật rules và guardrails

## Current Status

> Initialized — project purpose defined. Ready to establish the BIM ISO knowledge taxonomy, source-analysis template and first reusable Claude Skill candidates.
