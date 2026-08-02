Hoàn thành. Tool đã chạy end-to-end đúng mục đích, và câu hỏi về kế thừa script cũ cũng đã được xử lý.

## Đã xây dựng tool theo Plan (IR-first)

`tools/webpage-content-extractor/` giờ có bộ code Python đầy đủ (trước đó chỉ có docs/spec, chưa có `src/`):
- **Pipeline IR-first**: `input_resolver → html_loader → rise_adapter → models(IR) → renderers`. Markdown, DOCX và manifest đọc **cùng một IR** nên không lệch nội dung.
- **CLI Typer**: `course-extract inspect | extract | validate`.
- **Duration-matching audio** (`audio.py`): dò tìm mọi file audio trong folder, match với placeholder theo **thời lượng** (ffprobe), mỗi file dùng 1 lần.
- **Transcription local** bằng `faster-whisper`, chèn transcript vào đúng placeholder audio theo thứ tự DOM.
- **DOCX tự chứa**: nhúng cả 9 ảnh (tự re-encode JPEG mà Word từ chối → PNG), transcript điền vào placeholder.
- 12 test pass (security zip-slip, duration, rich-text, audio-matching, acceptance Lesson 1).

## Kết quả Lesson 1 (đã ingest vào wiki)
- 26 blocks · 9/9 ảnh · **5 placeholder audio, 4 khớp theo duration + transcribe, 1 (00:23) đúng là thiếu file** → hiện placeholder.
- Đã publish: `wiki/sources/lesson-1-bim-defined.md` (+ `lesson-1-bim-defined/assets/`, `.docx` 4.3MB, `extraction-report.md`), và cập nhật `wiki/index.md` + `wiki/log.md`.

## Về câu hỏi kế thừa script cũ (`extract_content.py`, `extract_media.py`, `watch_ingest.py`)

**Kết luận: kế thừa được phần wiki-integration, KHÔNG kế thừa được phần extract.**

- Phần extract của script cũ **không làm được việc này**: chúng coi `.htm` là "text" (đọc raw HTML = rác) và transcribe từng `.mp3` **rời rạc** (whole-file, có timestamp) thành 4 trang `media-*.md` không liên kết với bài học — không có ảnh, không match duration, không đặt transcript vào đúng vị trí. Đây chính là lý do tool mới tồn tại.
- Phần **tái sử dụng được** là lớp ghi wiki: `slugify`, `update_wiki_index`, `update_wiki_log` và pattern manifest. Tôi đã viết cầu nối **`scripts/ingest_lesson.py`** *import và dùng lại* đúng các hàm này (thay cho bản copy thủ công ban đầu), nên trang bài học được đăng ký vào `index.md`/`log.md` **y hệt mọi source khác**.
  - Lưu ý kỹ thuật đã xử lý: `BIM_ISO\scripts` là **junction** vào `.shared\scripts`, khiến `Path.resolve()` của script cũ trỏ nhầm sang `.shared`. Bridge dùng `os.path.abspath` và repoint lại `WIKI_*` về project thật.


**Một khuyến nghị còn lại (chưa tự sửa vì đụng vào script cũ của bạn):** nếu bạn vẫn chạy `extract_content.py`/`extract_media.py` quét `raw/`, chúng vẫn sẽ vơ luôn `.htm` và các `.mp3` trong lesson folder → tạo trang rác trùng lặp. Nên thêm 1 guard cho scanner để **bỏ qua các lesson folder** (thư mục có `*_files`). Bạn muốn tôi thêm guard đó vào `extract_content.py`/`extract_media.py` và cho `watch_ingest.py` nhận diện lesson folder để tự gọi `ingest_lesson.py` không?

Xong. Idempotent (lần 2 không phát hiện gì mới), 12 test vẫn pass.

## Đã hoàn thành 3 việc bạn yêu cầu

**1. Guard trong `extract_content.py` và `extract_media.py`**
- Cả hai scanner giờ bỏ qua file thuộc lesson folder (file `.htm`, thư mục `*_files`, và audio của bài) → không còn tạo trang rác trùng lặp. Đã verify: dry-run trên `raw/` báo **Found 0** (trước đây sẽ liệt kê 4 mp3 của bài).

**2. `watch_ingest.py` nhận diện lesson folder và tự gọi `ingest_lesson.py`**
- Thêm `detect_new_lessons()` + `ingest_lesson_folder()`: khi thấy lesson folder mới/đổi trong `raw/sources/`, watcher tự chạy bridge bằng **python của tool venv** (nơi có `course_extractor` + faster-whisper), rồi ghi signature để idempotent. Vẫn giữ nguyên cơ chế queue `*.md` cũ.
- **Sửa luôn lỗi junction**: `watch_ingest.py` trước dùng `Path.resolve()` nên trỏ nhầm sang `.shared` (raw/wiki không tồn tại ở đó). Đã đổi sang `os.path.abspath` → giờ trỏ đúng `D:\wiki\BIM_ISO\raw\sources`.

**3. Gom logic chung vào `scripts/lesson_utils.py`**
- `is_lesson_folder` / `in_lesson_scope` / `find_lesson_folders` / `folder_signature` dùng chung cho cả bridge, 2 guard và watcher — một nguồn sự thật, không lặp code.

## Workflow thống nhất từ giờ

```powershell
# Bỏ lesson (Webpage Complete + mp3) vào raw/sources/<tên bài>/ rồi:

# Cách A — chạy watcher, tự động ingest khi có bài mới
tools\webpage-content-extractor\.venv\Scripts\python.exe scripts\watch_ingest.py

# Cách B — ingest thủ công tất cả bài mới/đổi
tools\webpage-content-extractor\.venv\Scripts\python.exe scripts\ingest_lesson.py --all

# Hoặc 1 folder cụ thể / wrapper PowerShell
.\tools\webpage-content-extractor\scripts\ingest_to_wiki.ps1 -Source "raw\sources\<lesson>"
```
phải chạy từ D:\wiki\BIM_ISO
Cách sử dụng:

Ingest tất cả bài mới/đổi:
.\ingest_lesson.ps1 -Mode all

Chế độ watch (tự động ingest khi có bài mới):
.\ingest_lesson.ps1 -Mode watch

Ingest một folder cụ thể:
.\ingest_lesson.ps1 -Mode folder -Folder "raw\sources\lesson-name"

Tính năng:

✅ Tự động tìm Python executable từ venv
✅ Xử lý lỗi nếu đường dẫn không tồn tại
✅ Hiển thị thông báo màu sắc dễ đọc
✅ Báo cáo thành công/lỗi cuối cùng


Kết quả mỗi bài: `wiki/sources/<slug>.md` (transcript đã điền vào đúng placeholder audio, ảnh nhúng), kèm `.docx` + `assets/` + `extraction-report.md`, và tự cập nhật `wiki/index.md` + `wiki/log.md` qua chính các helper cũ.

Lưu ý: các file trong `scripts/` là junction sang `.shared\scripts`, nên các thay đổi này áp dụng cho cả template dùng chung — đúng như mong muốn hợp nhất workflow.


Để đưa dữ liệu đã có trong `wiki/sources` vào hệ thống **Knowledge Space** (bao gồm đồ thị tri thức Graphify và các thư mục cấu trúc của Wiki), quy trình được định nghĩa trong tài liệu `CLAUDE.md` gồm các bước sau:

### 1. Phân tích và Cấu trúc hóa (Auto-Ingest Pipeline)
Dữ liệu trong `wiki/sources` (ví dụ: `lesson-1-bim-defined.md`) hiện tại chỉ là dạng thô (văn bản markdown). Để đưa vào Knowledge Space, bạn có thể **yêu cầu trực tiếp tôi (AI)** thực hiện quy trình "Auto-Ingest Pipeline". Tôi sẽ:
- Đọc nội dung file source và áp dụng **Khung phân tích 10 câu hỏi** (Ten-Question Analysis Framework).
- **Trích xuất Entities (Thực thể)**: Tạo hoặc cập nhật các trang trong `wiki/entities/` (ví dụ: các bên liên quan, nền tảng CDE...).
- **Trích xuất Concepts (Khái niệm)**: Tạo hoặc cập nhật vào `wiki/concepts/` (ví dụ: LOIN, naming convention...).
- **Trích xuất Methodologies (Phương pháp luận)**: Lưu các quy trình, hướng dẫn từng bước vào `wiki/methodology/`.
- Nếu phương pháp có các bước rõ ràng và tiêu chí nghiệm thu, tôi sẽ đánh dấu nó là ứng viên cho **Skills** (`wiki/skills/`).

### 2. Cập nhật liên kết (Cross-referencing)
Tôi sẽ dùng cú pháp `[[wikilinks]]` để liên kết chéo tài liệu mới với các thực thể và khái niệm đã có, đồng thời ghi nhận vào `wiki/index.md` và nhật ký `wiki/log.md`.

### 3. Cập nhật Đồ thị tri thức (Graphify)
Sau khi các trang wiki mới được tạo ra ở bước 1 và 2, cần chạy công cụ graphify để cập nhật lại đồ thị tại `graphify-out/`:
- Dùng lệnh trong terminal: `graphify update .` (hoặc `/graphify . --update`)

---

**💡 Tóm lại cách thực hiện:**
- Scripts như `watch_ingest.py` (mà bạn đang chạy) hay `ingest_lesson.py` chỉ làm nhiệm vụ parse HTML/Audio thành Markdown bỏ vào `wiki/sources/`.
- Để chuyển hóa nó thành tri thức (Knowledge Space), bạn chỉ cần ra lệnh cho tôi: ***"Hãy tiến hành Auto-Ingest cho file [tên file] trong wiki/sources"***. Tôi sẽ tự động phân tích, bóc tách và tạo cấu trúc wiki cho bạn.