## Hướng dẫn Setup Graphify cho Video/Audio Extraction

Tôi đã kiểm tra xong trạng thái hệ thống của bạn. Đây là kết quả:

### Trạng thái hiện tại
- ✅ **graphifyy** đã cài (v0.4.23) — nhưng CLI `graphify` không nằm trên PATH
- ✅ **raw/video/** đã tồn tại, có file `Karpathy's_LLM_Wiki_-_Full_Beginner_Setup_Guide-20260429231327.mp4.mkv` (~13MB)
- ❌ **faster-whisper** chưa cài (cần cho transcription)
- ❌ **yt-dlp** chưa cài (cần cho download YouTube)

---

## Bước 1: Cài đặt dependencies còn thiếu

```powershell
# Cài video extras (faster-whisper + yt-dlp)
pip install "graphifyy[video]"

# Thêm graphify vào PATH (Windows)
# Scripts nằm ở: %APPDATA%\Python\Python314\Scripts
# Hoặc dùng: python -m graphify thay cho graphify
```

## Bước 2: Folder structure cho video

Folder `raw/video/` **đã tồn tại** với file MKV. Graphify sẽ tự detect các file video/audio khi scan folder. Bạn chỉ cần drop file vào `raw/` (hoặc subfolder bất kỳ).

Các format được hỗ trợ: `.mp4 .mov .mkv .webm .avi .m4v .mp3 .wav .m4a .ogg`

## Bước 3: Extract nội dung từ Video/Audio local

```powershell
# Chạy graphify trên folder raw (sẽ tự detect video files)
python -m graphify   # trong Cursor, gõ: /graphify ./raw

# Hoặc để accuracy cao hơn cho technical content:
# /graphify ./raw --whisper-model medium
```

**Quy trình tự động:**
1. Graphify detect file `.mkv` trong `raw/video/`
2. faster-whisper transcribe audio locally (không gửi lên cloud)
3. Transcript được cache ở `graphify-out/transcripts/`
4. Claude extract concepts & relationships từ transcript
5. Output: `graphify-out/graph.html`, `GRAPH_REPORT.md`, `graph.json`

## Bước 4: Extract Video từ YouTube URL

```powershell
# Download + transcribe + add to graph
python -m graphify add https://www.youtube.com/watch?v=iXd0t60YmMw

# Với metadata
python -m graphify add https://www.youtube.com/watch?v=iXd0t60YmMw --author "Channel Name"
```

**Quy trình:** yt-dlp download audio-only → Whisper transcribe locally → transcript fed into extraction pipeline → graph updated.

---

### Bạn muốn tôi chạy cài đặt luôn không? (pip install "graphifyy[video]")





## Cài đặt hoàn tất!

### Đã cài thành công:
- ✅ **faster-whisper** v1.2.1 — transcription engine chạy local
- ✅ **yt-dlp** v2026.3.17 — YouTube/video downloader
- ✅ **ctranslate2, onnxruntime, tokenizers, av** — supporting libs
- ✅ **graphify cursor integration** — `.cursor/rules/graphify.mdc` đã có

### ⚠️ Lưu ý quan trọng: PATH
Scripts nằm ở `C:\Users\Admin\AppData\Roaming\Python\Python314\Scripts` nhưng **chưa nằm trên PATH**. Bạn có 2 lựa chọn:
1. **Thêm vào PATH** (khuyến nghị): Thêm đường dẫn trên vào System PATH
2. **Dùng `python -m`**: Thay vì gõ `graphify`, gõ `python -m graphify`

---

### Cách sử dụng ngay bây giờ:

#### 1️⃣ Extract video local (file MKV đã có trong raw/video/):
Trong Cursor, gõ: `/graphify ./raw`
Hoặc terminal: `python -m graphify` (rồi follow skill instructions)

#### 2️⃣ Extract YouTube video:
Trong Cursor, gõ: `/graphify add https://www.youtube.com/watch?v=iXd0t60YmMw`
Hoặc terminal: `python -m graphify add https://www.youtube.com/watch?v=iXd0t60YmMw`

#### 3️⃣ Query graph sau khi build:
```
/graphify query "what is the main topic?"
/graphify explain "NodeName"
```

### Output sẽ nằm ở:
```
graphify-out/
├── graph.html        # Mở browser để xem interactive graph
├── GRAPH_REPORT.md   # Summary: god nodes, connections, questions
├── graph.json        # Query programmatically
├── transcripts/      # Cached transcripts (re-run sẽ skip)
└── cache/            # SHA256 cache
```

Bạn muốn tôi thêm PATH luôn, hay còn câu hỏi gì khác?

## Hoàn tất 100%!

### PATH đã được thêm:
✅ `C:\Users\Admin\AppData\Roaming\Python\Python314\Scripts` → User PATH
✅ `graphify` CLI hoạt động — verified thành công

> **Lưu ý:** Terminal hiện tại trong Cursor đã nhận PATH mới. Nhưng nếu bạn mở terminal mới bên ngoài (cmd/PowerShell), nó cũng sẽ tự nhận vì đã ghi vào User PATH.

---

### Tóm tắt toàn bộ setup:

| Thành phần | Trạng thái |
|---|---|
| graphifyy v0.4.23 | ✅ Installed |
| faster-whisper v1.2.1 | ✅ Installed |
| yt-dlp v2026.3.17 | ✅ Installed |
| Cursor integration | ✅ `.cursor/rules/graphify.mdc` |
| PATH | ✅ Added to User PATH |
| Folder `raw/video/` | ✅ Có file MKV sẵn |

### Bạn có thể bắt đầu ngay:

**Local video:**
```
/graphify ./raw
```

**YouTube URL:**
```
/graphify add https://www.youtube.com/watch?v=iXd0t60YmMw
```

**Query sau khi build:**
```
/graphify query "main concepts"
```

Còn gì cần hỗ trợ thêm không?

## Xác nhận: Đúng 100%

Bạn hiểu chính xác rồi. Đây là quy trình thực tế:

### Pipeline xử lý video của Graphify:

```
Video file (.mp4/.mkv/.webm/...)
    ↓
Extract AUDIO track only (via PyAV/ffmpeg)
    ↓
faster-whisper transcribe audio → text
    ↓
Transcript text → Claude extract concepts & relationships
    ↓
→ Knowledge graph
```

### Điều này có nghĩa:

- **Chất lượng video (resolution) hoàn toàn KHÔNG quan trọng** — 360p hay 4K đều cho kết quả giống nhau
- **Chỉ cần audio rõ ràng** — giọng nói clean, ít noise → transcript chính xác hơn
- **Với YouTube:** yt-dlp chỉ download **audio-only** (không download video), nên rất nhanh và nhẹ
- **File MKV 13MB của bạn** hoàn toàn OK — tool chỉ cần audio track trong đó

### Tips để có transcript tốt hơn:
- Nếu technical content (thuật ngữ chuyên ngành), dùng model lớn hơn: `/graphify ./raw --whisper-model medium` (mặc định là `base`, nhẹ nhưng kém chính xác hơn với từ kỹ thuật)
- Audio có nhiều noise → transcript kém → graph kém
- Nhiều speaker nói cùng lúc → khó transcribe chính xác

Còn câu hỏi gì khác không?

## Cách chạy bằng Terminal

Mở terminal trong Cursor (Ctrl+`) hoặc PowerShell bên ngoài, rồi chạy:

### 1. Transcribe tất cả video/audio mới trong `raw/`:

```powershell
cd "D:\wiki\AI Research"
python scripts/extract_media.py
```

### 2. Xem trước file nào sẽ xử lý (không transcribe):

```powershell
python scripts/extract_media.py --dry-run
```

### 3. Dùng model chính xác hơn (cho nội dung kỹ thuật):

```powershell
python scripts/extract_media.py --model medium
```

> Model options: `tiny` (nhanh nhất) → `base` (mặc định) → `small` → `medium` → `large-v3` (chính xác nhất, chậm nhất)

### 4. Download + transcribe YouTube video:

```powershell
python scripts/extract_media.py --url "https://www.youtube.com/watch?v=iXd0t60YmMw"
```

### 5. Force ngôn ngữ English:

```powershell
python scripts/extract_media.py --language en
```

### 6. Kết hợp nhiều options:

```powershell
python scripts/extract_media.py --model medium --language en
python scripts/extract_media.py --url "https://youtube.com/..." --model medium
```

---

### Lưu ý:
- **Lần đầu chạy** sẽ tự download Whisper model (~140MB cho `base`, ~500MB cho `medium`) — chỉ download 1 lần
- **Re-run** sẽ tự skip file đã transcribe (nhờ manifest tracking)
- **Output** nằm ở `raw/transcripts/` và `wiki/sources/media-*`

Bạn muốn tôi chạy thử ngay với file MKV hiện tại không?


## Test thành công!

### Kết quả chạy YouTube URL:

```
python scripts/extract_media.py --url "https://www.youtube.com/watch?v=iXd0t60YmMw"
```

- **Thời gian**: 2m01s (download + transcribe)
- **Ngôn ngữ**: Detected English (99.9% confidence)
- **Chất lượng transcript**: Rất tốt — nhận diện đúng tên "Andre Karpathi", "ChatGPT", "Notebook LM", "RAG", "OpenAI", "Tesla"

### Files được tạo:

| File | Nội dung |
|------|---------|
| `raw/video/Karpathy's LLM Wiki - Full Beginner Setup Guide-iXd0t60YmMw.m4a` | Audio downloaded từ YouTube |
| `raw/transcripts/karpathys-llm-wiki-full-beginner-setup-guide.md` | Full transcript với timestamps |
| `wiki/sources/media-karpathys-llm-wiki-full-beginner-setup-guide.md` | Wiki source page (đúng schema) |
| `wiki/log.md` | Đã cập nhật |
| `scripts/.media_manifest.json` | Track file đã xử lý |

### Cũng đã fix thêm:
- Cài **ffmpeg v8.1** (cần thiết cho yt-dlp convert audio)
- Fix script hiển thị lỗi stderr chi tiết thay vì crash
- PATH đã cập nhật cho ffmpeg

### Transcript preview (dòng đầu):
```
[00:00-00:03] There's a problem with the way most of us use AI right now.
[00:03-00:06] And once you see it, you're not going to be able to unsee it.
[00:06-00:09] When you upload documents to something like ChatGPT or Notebook
[00:36-00:38] He calls it the LLM Wiki.
```

### Tiếp theo bạn có thể:
1. Chạy `python scripts/extract_media.py` để transcribe file MKV local (đã có sẵn)
2. Chạy `/graphify --update` để thêm transcript vào knowledge graph
3. Drop thêm video vào `raw/video/` rồi chạy lại command

Bạn cần gì thêm?

## Giải thích `graphify update` chạy trong terminal

### Có 2 cách chạy graphify, khác nhau hoàn toàn:

---

### 1. Terminal CLI: `python -m graphify update .`
- **Chỉ xử lý code files** (Python, JS, TS, Go, etc.)
- Dùng **tree-sitter AST** — parse cấu trúc code (classes, functions, imports)
- **KHÔNG cần LLM** → miễn phí, rất nhanh (~5 giây)
- **KHÔNG đọc** markdown, transcript, PDF, images
- Phù hợp khi bạn chỉ thay đổi code

### 2. AI Assistant: `/graphify . --update` (gõ trong chat Cursor)
- Xử lý **tất cả**: code + docs + markdown + transcripts + images + PDF
- Code → tree-sitter AST (giống trên)
- Docs/transcripts → **Claude LLM** extract concepts & relationships
- **Tốn tokens** nhưng tạo graph semantic đầy đủ
- Phù hợp khi bạn thêm content mới (transcript, papers, wiki pages)

---

### Tóm lại:

| Lệnh | Chạy ở đâu | Xử lý gì | Cần LLM? | Tốc độ |
|-------|-----------|-----------|-----------|--------|
| `python -m graphify update .` | Terminal | Code only | Không | ~5s |
| `/graphify . --update` | Cursor chat | Code + docs + transcript | Có (Claude) | Minutes |
| `/graphify .` | Cursor chat | Full rebuild từ đầu | Có (Claude) | Minutes+ |

### Vậy để transcript mới được tích hợp vào graph:
Bạn cần gõ `/graphify . --update` **trong Cursor chat** (không phải terminal), vì Cursor sẽ dùng Claude đọc transcript và extract ra concepts/relationships.

Bạn rõ chưa? Cần thêm gì không?