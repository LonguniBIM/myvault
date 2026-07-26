# GitHub Publish Guide

Hướng dẫn cho AI Agent cách khởi tạo và publish một project lên GitHub organization.

---

## Prerequisites

- Git đã cài đặt và cấu hình user name/email
- GitHub CLI (`gh`) đã cài đặt và đăng nhập (`gh auth login`)
- Quyền tạo repo trên GitHub organization

### Kiểm tra nhanh

```powershell
git --version          # Xác nhận git có sẵn
gh auth status         # Xác nhận đã login GitHub CLI
gh org list            # Xem danh sách org có quyền truy cập
```

---

## Step 1 — Khởi tạo Git Repository

Nếu project chưa là git repo:

```powershell
cd C:\path\to\project
git init -b main
```

Nếu đã có git repo, kiểm tra trạng thái:

```powershell
git status
git remote -v          # Xem remote hiện tại (nếu có)
```

---

## Step 2 — Tạo .gitignore

**Mục đích**: Loại trừ binary, secrets, và file lớn trước khi commit.

**Nguyên tắc**:
- Không push file binary (*.exe, *.dll, *.pdb, *.zip)
- Không push secrets (.env, credentials.json)
- Không push thư mục build (bin/, obj/, dist/, node_modules/)
- Không push IDE-specific cache (.specstory/, __pycache__/)
- Kiểm tra tổng size trước khi commit: GitHub khuyến nghị repo dưới 1GB

```powershell
# Kiểm tra size thư mục lớn
(Get-ChildItem . -Recurse -File | Measure-Object -Property Length -Sum).Sum / 1MB
```

Mẫu `.gitignore` cơ bản:

```gitignore
# Binary files
*.exe
*.dll
*.pdb
*.obj
*.lib

# Build output
bin/
obj/
build/
dist/

# Dependencies
node_modules/
.venv/
venv/
__pycache__/
*.pyc

# Secrets
.env
.env.*
credentials.json
secrets.json
appsettings.Development.json
appsettings.Production.json

# OS
Thumbs.db
.DS_Store

# IDE cache (optional)
.specstory/
```

Thêm thư mục lớn chứa binary/data vào `.gitignore` nếu có:

```gitignore
# Project-specific large directories
.reference/
data/raw/
```

---

## Step 3 — Stage và Commit

```powershell
# Stage tất cả (respecting .gitignore)
git add .

# Kiểm tra những gì sẽ commit
git status

# Xác nhận không có file binary lớn bị stage
git diff --cached --stat

# Commit
git commit -m "feat: initial project setup" -m "Mô tả chi tiết hơn ở đây"
```

### Lưu ý quan trọng

Nếu trước đó đã `git add` trước khi tạo `.gitignore`, cần reset cache:

```powershell
git rm -r --cached .
git add .
git status              # Kiểm tra lại
git commit -m "feat: initial project setup"
```

---

## Step 4 — Tạo Repo trên GitHub và Push

### Cách 1: GitHub CLI (khuyến nghị)

```powershell
# Tạo public repo trên organization
gh repo create <ORG_NAME>/<REPO_NAME> --public --description "Mô tả project" --source . --push

# Tạo private repo trên organization
gh repo create <ORG_NAME>/<REPO_NAME> --private --description "Mô tả project" --source . --push

# Tạo public repo trên tài khoản cá nhân
gh repo create <REPO_NAME> --public --description "Mô tả project" --source . --push
```

**Flags thường dùng**:

| Flag | Mục đích |
|------|----------|
| `--public` | Repo public (ai cũng xem được) |
| `--private` | Repo private |
| `--source .` | Dùng thư mục hiện tại làm source |
| `--push` | Tự động push sau khi tạo |
| `--description "..."` | Mô tả repo |
| `--homepage "URL"` | URL trang chủ project |
| `--disable-wiki` | Tắt wiki |
| `--disable-issues` | Tắt issues |

### Cách 2: Manual (nếu không có gh CLI)

```powershell
# 1. Tạo repo trên GitHub web: github.com/organizations/<ORG>/repositories/new

# 2. Add remote
git remote add origin https://github.com/<ORG_NAME>/<REPO_NAME>.git

# 3. Push
git push -u origin main
```

---

## Step 5 — Xác nhận thành công

```powershell
# Kiểm tra remote đã set đúng
git remote -v

# Kiểm tra branch tracking
git status

# Mở repo trên browser
gh repo view --web
```

---

## Ví dụ Hoàn chỉnh

Publish project `<your-project>` lên org `<your-org>` (hoặc personal account):

```powershell
cd "<absolute-path-to-your-project>"

# Kiểm tra git status
git status

# Tạo .gitignore (loại trừ binaries, secrets, runtime tooling state)
# ... (tạo file .gitignore phù hợp)

# Reset cache nếu cần, rồi stage
git rm -r --cached .
git add .

# Commit
git commit -m "feat: initialize <your-project> with Harness v0" -m "Install harness_template for agent-driven development."

# Tạo repo + push trong 1 lệnh
gh repo create <your-org-or-user>/<your-project> --public --description "<short description>" --source . --push
```

Kết quả:
```
https://github.com/&lt;your-org-or-user&gt;/&lt;your-project&gt;
branch 'main' set up to track 'origin/main'.
```

---

## Xử lý sự cố

### gh CLI chưa login

```powershell
gh auth login
# Chọn GitHub.com → HTTPS → Login with browser
```

### Không có quyền tạo repo trên org

```powershell
# Kiểm tra quyền
gh api orgs/<ORG_NAME>/memberships/$env:USERNAME

# Nếu thiếu quyền, nhờ admin org cấp "Member" role với create repo permission
```

### File quá lớn (>100MB)

GitHub từ chối push file >100MB. Giải pháp:
1. Thêm vào `.gitignore`
2. Nếu đã commit, dùng `git filter-branch` hoặc BFG Repo-Cleaner để xóa khỏi history
3. Sử dụng Git LFS cho file lớn cần track

```powershell
# Cài Git LFS
git lfs install
git lfs track "*.psd"    # Track file pattern cần thiết
git add .gitattributes
```

### Push bị reject (non-fast-forward)

```powershell
# Nếu repo mới tạo trên web có README/LICENSE
git pull origin main --allow-unrelated-histories
git push origin main
```

---

## Checklist cho Agent

Trước khi publish, agent cần xác nhận:

- [ ] `.gitignore` đã tạo và loại trừ binary/secrets/build output
- [ ] Tổng size staged files hợp lý (< 100MB, lý tưởng < 50MB)
- [ ] Không có file secrets bị stage (.env, credentials, API keys)
- [ ] Không có file binary lớn bị stage (.exe, .dll, .zip)
- [ ] `gh auth status` xác nhận đã đăng nhập
- [ ] Commit message tuân theo conventional commits
- [ ] Remote URL đúng org/repo name
- [ ] Push thành công, branch tracking đã set
