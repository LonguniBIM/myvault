# Image, PDF & Document Extraction Guide

> How to extract knowledge from images, PDFs, and Office documents using graphify and ingest into the wiki.

**Date**: 2026-04-30
**Status**: Ready to use

---

## Table of Contents

1. [Overview — How Graphify Handles Each Type](#overview--how-graphify-handles-each-type)
2. [Dependencies Status](#dependencies-status)
3. [Folder Structure](#folder-structure)
4. [Images (.png .jpg .webp .gif)](#images-png-jpg-webp-gif)
5. [PDFs (.pdf)](#pdfs-pdf)
6. [Office Documents (.docx .xlsx)](#office-documents-docx-xlsx)
7. [Markdown & Text (.md .txt .html .rst)](#markdown--text-md-txt-html-rst)
8. [Running Graphify](#running-graphify)
9. [Extraction Modes Comparison](#extraction-modes-comparison)
10. [Complete Workflow Example](#complete-workflow-example)
11. [Tips for Best Results](#tips-for-best-results)

---

## Overview — How Graphify Handles Each Type

Graphify xử lý mỗi loại file **khác nhau hoàn toàn**:

| File Type | Extensions | Extraction Method | Needs LLM? |
|-----------|-----------|-------------------|------------|
| **Code** | .py .js .ts .go .rs .java ... | tree-sitter AST (local) | No |
| **Docs** | .md .mdx .html .txt .rst | Claude LLM extraction | **Yes** |
| **Images** | .png .jpg .webp .gif | **Claude Vision** — reads screenshots, diagrams, any language | **Yes** |
| **PDFs** | .pdf | Citation mining + concept extraction via Claude | **Yes** |
| **Office** | .docx .xlsx | Convert to markdown → Claude extraction | **Yes** |
| **Video/Audio** | .mp4 .mkv .mp3 ... | faster-whisper (local) → Claude extraction | **Yes** (for concepts) |

**Key point**: Chỉ code files xử lý local hoàn toàn. Tất cả docs/images/PDFs đều cần Claude LLM để extract concepts & relationships → phải chạy qua `/graphify` trong Cursor chat (không phải terminal).

---

## Dependencies Status

| Package | Status | Purpose |
|---------|--------|---------|
| graphifyy | ✅ v0.4.23 | Core engine |
| graphifyy[video] | ✅ Installed | faster-whisper + yt-dlp |
| graphifyy[office] | ✅ Installed | python-docx + openpyxl |
| python-docx | ✅ v1.2.0 | Read .docx files |
| openpyxl | ✅ v3.1.5 | Read .xlsx files |
| pypdf | ✅ Installed | PDF text extraction |
| Pillow | ✅ v12.1.1 | Image processing |
| ffmpeg | ✅ v8.1 | Audio conversion |

**Tất cả đã sẵn sàng.** Unified command: `python scripts/extract_content.py`

### Unified Extraction Command

```powershell
python scripts/extract_content.py                     # extract all new files
python scripts/extract_content.py --type video         # only video/audio
python scripts/extract_content.py --type image         # only images
python scripts/extract_content.py --type pdf           # only PDFs
python scripts/extract_content.py --type doc           # only .docx/.xlsx
python scripts/extract_content.py --url <youtube-url>  # download + transcribe YouTube
python scripts/extract_content.py --dry-run            # preview without processing
```

Trong Cursor chat: `/extract-content` (hoặc `/extract-content --type pdf`, etc.)

---

## Folder Structure

Drop files vào `raw/` hoặc bất kỳ subfolder nào. Graphify scan đệ quy (recursive).

Gợi ý tổ chức:

```
raw/
├── sources/         ← Web sources (clipped repos, articles)
├── video/           ← Video/audio files
├── transcripts/     ← Generated transcripts (auto)
├── papers/          ← PDF research papers
├── images/          ← Screenshots, diagrams, whiteboard photos
├── docs/            ← Word/Excel documents
└── notes/           ← Text/markdown notes
```

Tạo folders theo nhu cầu:

```powershell
mkdir "D:\wiki\AI Research\raw\papers"
mkdir "D:\wiki\AI Research\raw\images"
mkdir "D:\wiki\AI Research\raw\docs"
mkdir "D:\wiki\AI Research\raw\notes"
```

---

## Images (.png .jpg .webp .gif)

### Cách hoạt động
- Graphify gửi ảnh tới **Claude Vision API**
- Claude "nhìn" ảnh và extract: concepts, text trong ảnh, diagram relationships, architectural patterns
- Hỗ trợ: screenshots, whiteboard photos, diagrams, slides, ảnh có text bất kỳ ngôn ngữ

### Khi nào hữu ích
- Screenshot architecture diagrams
- Whiteboard brainstorm sessions
- Slides từ presentations
- Diagrams (flowcharts, ER diagrams, system diagrams)
- Screenshots of code/UI that you want to cross-reference

### Cách dùng

1. Drop ảnh vào `raw/images/` (hoặc bất kỳ đâu trong `raw/`)
2. Chạy trong Cursor chat:

```
/graphify ./raw
```

Hoặc chỉ scan folder images:

```
/graphify ./raw/images
```

### Lưu ý
- Ảnh rõ ràng, text đọc được → kết quả tốt
- Ảnh mờ, low-res → Claude có thể đọc sai
- Ảnh nhiều ngôn ngữ → Claude nhận diện được (tiếng Việt, Nhật, Trung, etc.)
- **Tốn tokens** vì image data lớn — chỉ add ảnh thực sự có giá trị

---

## PDFs (.pdf)

### Cách hoạt động
- Graphify extract text từ PDF
- Claude thực hiện **citation mining** — tìm references, citations giữa papers
- Claude extract concepts, relationships, key findings

### Khi nào hữu ích
- Research papers (arXiv, conference papers)
- Technical documentation
- Reports, whitepapers
- Ebooks (chapters)

### Cách dùng

1. Drop PDF vào `raw/papers/`:

```powershell
# Copy PDF vào folder
Copy-Item "C:\path\to\paper.pdf" "D:\wiki\AI Research\raw\papers\"
```

2. Chạy trong Cursor chat:

```
/graphify ./raw
```

### Fetch paper trực tiếp từ URL

```
/graphify add https://arxiv.org/abs/1706.03762
```

Graphify sẽ download PDF, save vào `raw/`, và extract luôn.

### Lưu ý
- Scanned PDFs (ảnh, không phải text) → cần OCR, graphify có thể không extract được text
- PDFs quá dài → tốn nhiều tokens → có thể chia nhỏ
- Encrypted/password-protected PDFs → không đọc được

---

## Office Documents (.docx .xlsx)

### Cách hoạt động
- `.docx`: python-docx convert sang markdown → Claude extract
- `.xlsx`: openpyxl convert sang markdown tables → Claude extract

### Khi nào hữu ích
- Meeting notes (Word)
- Technical specs (Word)
- Data tables, comparisons (Excel)
- Project documentation

### Cách dùng

1. Drop file vào `raw/docs/`:

```powershell
Copy-Item "C:\path\to\report.docx" "D:\wiki\AI Research\raw\docs\"
Copy-Item "C:\path\to\data.xlsx" "D:\wiki\AI Research\raw\docs\"
```

2. Chạy trong Cursor chat:

```
/graphify ./raw
```

### Lưu ý
- `.docx` với images embedded → images có thể không được extract
- `.xlsx` chỉ lấy data + headers → formatting bị bỏ
- Macro-heavy files (.xlsm) → macros không được extract
- `.pptx` → **chưa hỗ trợ** (có thể export sang PDF trước)

---

## Markdown & Text (.md .txt .html .rst)

### Cách hoạt động
- Claude đọc nội dung và extract: concepts, relationships, design rationale
- Đây là loại file graphify xử lý tốt nhất (native text)

### Khi nào hữu ích
- Research notes
- Blog posts (saved as markdown)
- README files
- Technical documentation

### Cách dùng

Drop vào `raw/notes/` hoặc bất kỳ đâu trong `raw/`:

```powershell
# Save web content as markdown (recommend defuddle for clean extraction)
defuddle parse https://example.com/article --md > "D:\wiki\AI Research\raw\notes\article-title.md"
```

Hoặc dùng graphify add:

```
/graphify add https://example.com/article
```

---

## Running Graphify

### Chạy lần đầu (full build)

Trong Cursor chat:

```
/graphify ./raw
```

Sẽ:
1. Scan tất cả files trong `raw/`
2. Code → tree-sitter AST (instant)
3. Docs/images/PDFs → Claude subagents chạy song song (parallel)
4. Merge thành knowledge graph
5. Output ở `graphify-out/`

### Chạy update (chỉ files mới/changed)

```
/graphify ./raw --update
```

Graphify dùng SHA256 cache (`graphify-out/cache/`), nên chỉ xử lý files thay đổi → nhanh hơn nhiều.

### Chạy deep mode (aggressive inference)

```
/graphify ./raw --mode deep
```

Extract nhiều INFERRED edges hơn — Claude sẽ tìm nhiều connections hơn giữa concepts.

### Chạy trên subfolder cụ thể

```
/graphify ./raw/papers       # Chỉ papers
/graphify ./raw/images       # Chỉ images
/graphify ./raw/docs         # Chỉ office docs
```

### Query graph sau khi build

```
/graphify query "what connects attention to the optimizer?"
/graphify query "show the auth flow" --dfs
/graphify path "ConceptA" "ConceptB"     # Shortest path
/graphify explain "NodeName"              # Explain a node
```

---

## Extraction Modes Comparison

| Mode | Command | What it does | LLM tokens |
|------|---------|-------------|------------|
| **Full build** | `/graphify ./raw` | Everything from scratch | High |
| **Update** | `/graphify ./raw --update` | Only new/changed files | Low-Medium |
| **Deep** | `/graphify ./raw --mode deep` | More aggressive inference | Higher |
| **Cluster only** | `/graphify ./raw --cluster-only` | Re-cluster existing graph | None |
| **Code only** | `python -m graphify update .` (terminal) | AST only, no LLM | None |

### Token cost tradeoff

| Corpus size | First build | Update (1 new file) |
|-------------|-------------|---------------------|
| 5 files | ~few K tokens | ~1K tokens |
| 20 files | ~20-50K tokens | ~2-5K tokens |
| 50+ files | ~100K+ tokens | ~5-10K tokens |

Sau first build, mỗi query chỉ đọc graph.json (compact) → **71.5x ít tokens** so với đọc raw files.

---

## Complete Workflow Example

### Scenario: Thêm 1 paper PDF + 2 screenshot + 1 Word doc

```powershell
# 1. Copy files vào raw/
Copy-Item "attention-is-all-you-need.pdf" "D:\wiki\AI Research\raw\papers\"
Copy-Item "architecture-diagram.png" "D:\wiki\AI Research\raw\images\"
Copy-Item "whiteboard-notes.jpg" "D:\wiki\AI Research\raw\images\"
Copy-Item "meeting-notes.docx" "D:\wiki\AI Research\raw\docs\"
```

```
# 2. Trong Cursor chat — update graph với files mới
/graphify ./raw --update

# 3. Xem kết quả
# Mở graphify-out/graph.html trong browser để xem interactive graph
# Đọc graphify-out/GRAPH_REPORT.md cho god nodes + surprising connections

# 4. Query
/graphify query "what are the key concepts in the attention paper?"
/graphify explain "Transformer"
/graphify path "Attention" "Optimizer"
```

### Scenario: Thêm YouTube video + transcript vào graph

```powershell
# 1. Download + transcribe
python scripts/extract_media.py --url "https://youtube.com/watch?v=..." --model medium

# 2. Update graph trong Cursor chat
/graphify ./raw --update

# 3. Query
/graphify query "what did the video discuss about LLM Wiki?"
```

---

## Tips for Best Results

### Images
- Crop ảnh sát nội dung cần extract (bỏ borders, backgrounds)
- Screenshot text → đảm bảo font đủ lớn, rõ ràng
- Diagrams → label nodes/boxes rõ ràng

### PDFs
- Text-based PDFs (not scanned) cho kết quả tốt nhất
- Papers dài → graphify xử lý OK nhưng tốn tokens
- Nếu paper quá dài, extract sections quan trọng thành .md files riêng

### Office docs
- `.docx` nên có headings rõ ràng → giúp Claude structure nội dung
- `.xlsx` nên có header row → giúp nhận diện columns
- Complex formatting (merged cells, charts) sẽ bị mất khi convert sang markdown

### General
- Đặt tên file có ý nghĩa (không dùng `document1.pdf`) → giúp graph labels rõ hơn
- Dùng `.graphifyignore` để exclude files không muốn:

```
# .graphifyignore
*.generated.py
node_modules/
dist/
temp/
```

- Commit `graphify-out/` vào git (nếu dùng git) để team share graph
- Exclude `graphify-out/cache/` và `graphify-out/manifest.json` khỏi git

---

## Summary Table — All Supported File Types

| Type | Extensions | Method | Local? | Needs Claude? |
|------|-----------|--------|--------|---------------|
| Code | .py .js .ts .go .rs .java .c .cpp .rb .cs .kt .scala .php .swift .lua .zig .ps1 .ex .m .jl .vue .svelte | tree-sitter AST | ✅ Yes | No |
| Docs | .md .mdx .html .txt .rst | Text → Claude | ❌ | Yes |
| Office | .docx .xlsx | Convert → Claude | ❌ | Yes |
| Papers | .pdf | Text extract → Claude | ❌ | Yes |
| Images | .png .jpg .webp .gif | Claude Vision | ❌ | Yes |
| Video | .mp4 .mov .mkv .webm .avi .m4v | Whisper (local) → Claude | ✅ Audio | Yes (concepts) |
| Audio | .mp3 .wav .m4a .ogg | Whisper (local) → Claude | ✅ Audio | Yes (concepts) |
| YouTube | Any video URL | yt-dlp + Whisper → Claude | ✅ Audio | Yes (concepts) |
