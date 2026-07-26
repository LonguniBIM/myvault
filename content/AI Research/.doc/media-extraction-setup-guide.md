# Media Extraction Setup Guide

> Full setup guide for extracting transcripts from video/audio files and ingesting them into the wiki knowledge base.

**Date**: 2026-04-30
**Status**: Fully operational

---

## Table of Contents

1. [Overview](#overview)
2. [Dependencies Installed](#dependencies-installed)
3. [Folder Structure](#folder-structure)
4. [How It Works](#how-it-works)
5. [Usage — Terminal Commands](#usage--terminal-commands)
6. [Usage — Cursor Commands](#usage--cursor-commands)
7. [Graphify Update: Terminal vs AI Assistant](#graphify-update-terminal-vs-ai-assistant)
8. [Important Notes](#important-notes)
9. [Troubleshooting](#troubleshooting)

---

## Overview

This system lets you:
- Drop video/audio files into `raw/video/` and transcribe them automatically
- Download YouTube videos by URL, transcribe, and ingest into the wiki
- Track what's been processed so re-runs skip already-transcribed files
- Create wiki source pages following the project schema
- Integrate transcripts into the graphify knowledge graph

### Pipeline

```
Video/Audio file (or YouTube URL)
    ↓ yt-dlp (download audio-only, for YouTube)
    ↓ PyAV/ffmpeg (extract audio track, for local files)
    ↓ faster-whisper (local transcription — nothing leaves your machine)
    ↓ Transcript saved to raw/transcripts/<slug>.md
    ↓ Wiki page created at wiki/sources/media-<slug>.md
    ↓ wiki/index.md and wiki/log.md updated
    ↓ (optional) /graphify --update to add to knowledge graph
```

**Key insight**: Only the audio track matters. Video resolution (360p vs 4K) is irrelevant — only audio clarity affects transcript quality.

---

## Dependencies Installed

| Package | Version | Purpose |
|---------|---------|---------|
| graphifyy | 0.4.23 | Knowledge graph builder |
| faster-whisper | 1.2.1 | Local audio transcription (Whisper) |
| yt-dlp | 2026.3.17 | YouTube/video URL downloader |
| ffmpeg | 8.1 | Audio format conversion |
| ctranslate2 | 4.7.1 | Efficient inference backend for Whisper |
| onnxruntime | 1.25.1 | ML runtime |
| av (PyAV) | 17.0.1 | Audio/video processing |

### How they were installed

```powershell
# Graphify with video extras (installs faster-whisper + yt-dlp + dependencies)
pip install "graphifyy[video]"

# FFmpeg (needed by yt-dlp for audio conversion)
winget install --id Gyan.FFmpeg
```

### PATH Configuration

The following was added to User PATH:
```
C:\Users\Admin\AppData\Roaming\Python\Python314\Scripts
```

This enables running `graphify`, `yt-dlp`, etc. directly from any terminal.

---

## Folder Structure

```
D:\wiki\AI Research\
├── raw/
│   ├── video/              ← Drop video/audio files here
│   │   ├── *.mp4, *.mkv, *.webm, *.m4a, ...
│   │   └── (YouTube downloads land here too)
│   ├── transcripts/        ← Generated transcripts (markdown)
│   │   └── <slug>.md
│   └── sources/            ← Raw web sources (existing)
├── wiki/
│   ├── sources/
│   │   └── media-<slug>.md ← Wiki pages for each transcript
│   ├── index.md            ← Auto-updated with new entries
│   └── log.md              ← Auto-updated with activity
├── scripts/
│   ├── extract_media.py    ← Main extraction script
│   └── .media_manifest.json ← Tracks processed files (auto-generated)
├── graphify-out/           ← Knowledge graph output
│   ├── graph.html          ← Interactive graph (open in browser)
│   ├── GRAPH_REPORT.md     ← God nodes, communities, connections
│   └── graph.json          ← Queryable graph data
└── .cursor/rules/
    └── extract-media.mdc   ← Cursor rule for /extract-media command
```

### Supported media formats

| Type | Extensions |
|------|-----------|
| Video | `.mp4 .mov .mkv .webm .avi .m4v` |
| Audio | `.mp3 .wav .m4a .ogg .flac` |
| YouTube | Any video URL (audio-only download) |

---

## How It Works

### 1. Local file transcription
1. Script scans `raw/` recursively for video/audio files
2. Checks `scripts/.media_manifest.json` — skips already-processed files
3. For each new file:
   - Extracts audio track
   - Runs faster-whisper locally (auto-detects language)
   - Saves timestamped transcript to `raw/transcripts/<slug>.md`
   - Creates wiki source page at `wiki/sources/media-<slug>.md`
   - Updates `wiki/index.md` and `wiki/log.md`
   - Records file hash in manifest (for skip-on-rerun)

### 2. YouTube URL download
1. yt-dlp downloads **audio-only** (fast, small file size)
2. ffmpeg converts to m4a format
3. File saved to `raw/video/`
4. Same transcription pipeline as local files

### 3. Manifest tracking
- `scripts/.media_manifest.json` stores SHA256 hash of each processed file
- Re-running the script automatically skips files that haven't changed
- If you replace a file with the same name but different content, it will be re-transcribed

---

## Usage — Terminal Commands

All commands run from the workspace root: `D:\wiki\AI Research`

### Scan and transcribe all new media in raw/

```powershell
python scripts/extract_media.py
```

### Dry run — preview what would be processed

```powershell
python scripts/extract_media.py --dry-run
```

### Download and transcribe a YouTube video

```powershell
python scripts/extract_media.py --url "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Use a more accurate Whisper model (for technical content)

```powershell
python scripts/extract_media.py --model medium
```

Model options (accuracy vs speed tradeoff):

| Model | Size | Speed | Best for |
|-------|------|-------|----------|
| `tiny` | ~40MB | Fastest | Quick drafts |
| `base` | ~140MB | Fast | **Default** — general content |
| `small` | ~500MB | Medium | Better accuracy |
| `medium` | ~1.5GB | Slow | Technical/specialized content |
| `large-v3` | ~3GB | Slowest | Maximum accuracy |

### Force a specific language

```powershell
python scripts/extract_media.py --language en
python scripts/extract_media.py --language vi
```

Default: auto-detect (worked at 99.9% confidence in tests).

### Combine options

```powershell
python scripts/extract_media.py --model medium --language en
python scripts/extract_media.py --url "https://youtube.com/..." --model medium
```

---

## Usage — Cursor Commands

### In Cursor chat

Type `/extract-media` and the agent will run the script for you.

### With graphify

```
/graphify ./raw              # Full build including new transcripts
/graphify ./raw --update     # Update graph with new/changed content
/graphify query "topic"      # Query the knowledge graph
/graphify explain "NodeName" # Explain a specific concept
```

---

## Graphify Update: Terminal vs AI Assistant

This is an important distinction:

| Command | Where | Processes | Needs LLM? | Speed |
|---------|-------|-----------|------------|-------|
| `python -m graphify update .` | Terminal | Code files only (AST) | No | ~5 seconds |
| `/graphify . --update` | Cursor chat | Code + docs + transcripts + images | Yes (Claude) | Minutes |
| `/graphify .` | Cursor chat | Full rebuild from scratch | Yes (Claude) | Minutes+ |

### When to use which:

- **Terminal `update`**: After changing code files only. Fast, free, no LLM tokens.
- **Chat `/graphify . --update`**: After adding new transcripts, wiki pages, or documents. Needs Claude to read and extract semantic relationships.
- **Chat `/graphify .`**: Fresh full rebuild. Use when graph seems stale or after major changes.

### To integrate new transcripts into the knowledge graph:
You **must** use `/graphify . --update` in Cursor chat (not terminal), because the transcript is a markdown file that needs LLM extraction.

---

## Important Notes

### Audio quality matters more than video quality
- Video resolution is completely irrelevant — only the audio track is used
- Clean speech with minimal background noise produces the best transcripts
- Multiple overlapping speakers reduce accuracy

### First run downloads the Whisper model
- `base` model: ~140MB download (one-time)
- `medium` model: ~1.5GB download (one-time)
- Models are cached in `~/.cache/huggingface/`

### Privacy
- All transcription runs **100% locally** — audio never leaves your machine
- YouTube downloads use yt-dlp (same as downloading manually)
- Only the transcript text goes to Claude for concept extraction (when using graphify)

### Legal
- Only download content you have rights to use
- yt-dlp terms of service apply for YouTube downloads

---

## Troubleshooting

### `ffprobe and ffmpeg not found`
```powershell
winget install --id Gyan.FFmpeg
# Then restart your terminal to pick up the new PATH
```

### `graphify: command not found`
```powershell
# Use python -m instead:
python -m graphify update .

# Or add to PATH:
$scriptsPath = "$env:APPDATA\Python\Python314\Scripts"
[System.Environment]::SetEnvironmentVariable("Path", "$([System.Environment]::GetEnvironmentVariable('Path', 'User'));$scriptsPath", "User")
```

### `faster-whisper not installed`
```powershell
pip install "graphifyy[video]"
```

### yt-dlp fails with JavaScript runtime warning
This is a non-critical warning. If downloads fail completely, install deno:
```powershell
winget install DenoLand.Deno
```

### Transcript quality is poor
- Try a larger model: `--model medium` or `--model large-v3`
- Force the correct language: `--language en`
- Check if the audio track has clear speech vs noise

### Re-transcribe a file that was already processed
Delete its entry from `scripts/.media_manifest.json` and re-run the script.

---

## Test Results

### YouTube download test (2026-04-30)

```
URL: https://www.youtube.com/watch?v=iXd0t60YmMw
Title: Karpathy's LLM Wiki - Full Beginner Setup Guide
Duration: 2m01s (processing time)
Language: English (99.9% confidence)
Model: base
Result: SUCCESS — clean transcript with timestamps
```

Output files:
- `raw/video/Karpathy's LLM Wiki - Full Beginner Setup Guide-iXd0t60YmMw.m4a`
- `raw/transcripts/karpathys-llm-wiki-full-beginner-setup-guide.md`
- `wiki/sources/media-karpathys-llm-wiki-full-beginner-setup-guide.md`
