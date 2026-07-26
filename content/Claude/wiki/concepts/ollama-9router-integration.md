---
title: "Hướng Dẫn Kết Nối Ollama LLM với 9router"
---

# 🦙 Hướng Dẫn Kết Nối Ollama LLM với 9router

Tài liệu hướng dẫn chi tiết cách thiết lập và kết nối mô hình ngôn ngữ chạy cục bộ (Local LLM) qua **Ollama** vào hệ thống **9router**, giúp điều phối API tập trung và tích hợp dễ dàng với các công cụ lập trình AI như Cursor, Roo Code, Claude Desktop, NextChat...

---

## 📌 1. Tổng quan về Ollama & 9router

- **Ollama**: Công cụ chạy các mô hình AI mã nguồn mở cục bộ (Qwen 2.5, Llama 3.2, DeepSeek-R1, Mistral, Phi-3...) mượt mà trên máy cá nhân mà không tốn chi phí API Cloud.
- **9router**: Proxy Gateway & Router mạnh mẽ giúp hợp nhất tất cả các AI Providers (OpenAI, Claude, Gemini, Vertex, Ollama, Antigravity...) về một chuẩn API duy nhất (OpenAI REST / SSE Format), quản lý API Key, kiểm soát Rate Limit, Cân bằng tải (Load Balancing) và Chuyển đổi Model linh hoạt.

---

## 🚀 2. Bước 1: Cài đặt và Cấu hình Ollama

### 2.1 Cài đặt Ollama
1. Tải Ollama tại trang chủ [ollama.com](https://ollama.com).
2. Kiểm tra cài đặt trong terminal:
   ```bash
   ollama --version
   ```

### 2.2 Tải các Model LLM mong muốn
Chạy các lệnh tải model phù hợp với dung lượng VRAM/RAM máy bạn:
```bash
# Model lập trình chuyên sâu
ollama pull qwen2.5-coder:7b

# Model suy luận / Chat tổng quát
ollama pull llama3.2:3b

# Model reasoning nhẹ
ollama pull deepseek-r1:8b
```

### 2.3 Cấu hình biến môi trường mạng (Nếu dùng Docker / Remote / WSL)
Mặc định Ollama chỉ mở cổng `http://localhost:11434` cho máy cục bộ. Nếu bạn chạy 9router trong Docker hoặc trên máy chủ khác trong mạng LAN, hãy thiết lập biến môi trường:

**Trên Windows (PowerShell):**
```powershell
$env:OLLAMA_HOST="0.0.0.0:11434"
$env:OLLAMA_ORIGINS="*"
ollama serve
```

**Trên Linux / macOS:**
```bash
export OLLAMA_HOST="0.0.0.0:11434"
export OLLAMA_ORIGINS="*"
ollama serve
```

---

## ⚙️ 3. Bước 2: Tích hợp Ollama vào 9router

9router hỗ trợ **native provider** cho `Ollama Local` và `Ollama Cloud`.

### Cách 1: Thao tác qua Giao diện Dashboard (Web UI)
1. Mở giao diện 9router tại địa chỉ `http://localhost:3000` (hoặc cổng cấu hình của bạn).
2. Vào mục **Providers** từ menu bên trái -> Click **Add Provider**.
3. Chọn loại Provider là **Ollama Local** (hoặc `ollama-local`).
4. Cấu hình thông số:
   - **Provider Name**: `Ollama Local`
   - **Ollama Host URL**:
     - Nếu 9router & Ollama cùng chạy trên máy thật (Host): Để trống hoặc nhập `http://localhost:11434`
     - Nếu 9router chạy trong Docker: Nhập `http://host.docker.internal:11434`
     - Nếu Ollama chạy trên máy chủ khác trong LAN: Nhập `http://192.168.x.x:11434`
   - **API Key**: Không bắt buộc với local Ollama.
5. Click **Validate Connection** -> 9router sẽ tự động quét endpoint `/api/tags` của Ollama và danh sách các model local (`qwen2.5-coder:7b`, `llama3.2:3b`,...) sẽ lập tức xuất hiện!
6. Click **Save Provider**.

### Cách 2: Thao tác qua CLI (`9r` / REST API)
Bạn cũng có thể thêm Provider trực tiếp bằng lệnh API:
```bash
curl -X POST http://localhost:3000/api/providers \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Ollama Local",
    "provider": "ollama-local",
    "baseUrl": "http://localhost:11434"
  }'
```

---

## 🔀 4. Bước 3: Cấu hình Routing & Model Alias trong 9router

Để sử dụng tên mô hình ngắn gọn (ví dụ gọi `gpt-4o` nhưng thực chất điều hướng sang `qwen2.5-coder:7b` của Ollama):

1. Trong 9router Dashboard, vào mục **Model Routing / Aliases**.
2. Thêm Model Alias mới:
   - **Alias Name**: `local-coder` hoặc `gpt-4o`
   - **Target Provider**: `Ollama Local`
   - **Target Model**: `qwen2.5-coder:7b`
3. Lưu cấu hình. Bây giờ bất kỳ client nào yêu cầu model `local-coder` thông qua 9router sẽ tự động được điều hướng tới Ollama local!

---

## 💻 5. Bước 4: Kết nối Client Apps với 9router

Tất cả các ứng dụng hỗ trợ OpenAI API đều có thể kết nối tới Ollama thông qua 9router Gateway:

### 5.1 Kết nối trong VS Code Extensions (Roo Code / Cline / Continue)
- **API Provider**: `OpenAI Compatible`
- **Base URL**: `http://localhost:3000/v1` (hoặc `http://localhost:4000/v1`)
- **API Key**: Nhập key của 9router (hoặc `any-key` nếu tắt auth)
- **Model ID**: `qwen2.5-coder:7b` hoặc Alias vừa đặt.

### 5.2 Kết nối trong Cursor IDE
1. Mở **Cursor Settings** -> **Models**.
2. Thêm Model Name: `qwen2.5-coder:7b`.
3. Bật **OpenAI API Key Override**:
   - Base URL: `http://localhost:3000/v1`
   - API Key: `sk-9router-local`

### 5.3 Kết nối qua Ollama Native Format (`/v1/api/chat`)
9router cũng cung cấp đường dẫn hỗ trợ chuẩn Ollama native API:
- **Endpoint**: `http://localhost:3000/v1/api/chat`
- **Tags Endpoint**: `http://localhost:3000/api/tags`

---

## 🛠️ 6. Troubleshooting & Mẹo Tối ưu

| Sự cố | Nguyên nhân | Cách khắc phục |
| :--- | :--- | :--- |
| **`Connection refused` / `Ollama not reachable`** | Ollama chưa chạy hoặc đang chặn IP | Chạy `ollama serve` và thiết lập `OLLAMA_HOST="0.0.0.0:11434"`. |
| **Model load chậm / Out of Memory (OOM)** | VRAM GPU không đủ cho dung lượng model | Dùng các bản Quantized nhẹ hơn (ví dụ `qwen2.5-coder:7b-instruct-q4_K_M`). |
| **Docker container không gọi được Ollama host** | Cổng localhost trong Docker trỏ vào container | Sử dụng `http://host.docker.internal:11434` thay vì `localhost`. |
