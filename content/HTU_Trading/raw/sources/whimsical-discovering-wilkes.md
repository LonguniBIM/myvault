# Implementation Plan: Chart Screenshot Context Workflow

## Context

**Problem**: When user sends trading chart screenshots, Claude struggles to read fine details (candles, price levels, swing points) due to image resolution/size limitations. This makes it difficult to accurately identify Protected Swings, Failure Swings, and other trading patterns.

**Goal**: Create a workflow that automatically processes chart screenshots to provide better context for analysis:
1. **Repo script** (`D:\wiki\.shared\scripts\analyze_chart.py`) - Preprocesses images (crop, upscale, sharpen, tile) and generates markdown context
2. **Claude skill** (`~/.claude/skills/chart-context-analysis/`) - Guides Claude through structured chart analysis using the preprocessed images

**User requirements** (from questions):
- Both repo script + custom skill
- Full package: crop, upscale, sharpen, tile, markdown context
- Optimized for trading charts (Protected/Failure Swings, liquidity, structure)

## Architecture Decisions

### 1. Two-Component Design

**Script** (`analyze_chart.py`):
- Standalone Python script in `.shared/scripts/`
- Handles image preprocessing only (crop, upscale, sharpen, tile)
- Outputs: processed images + markdown manifest
- No Claude API calls (keeps it fast and reusable)

**Skill** (`chart-context-analysis`):
- Guides Claude through analysis workflow
- Uses script output as enhanced context
- Applies HTU_Trading 12-question framework
- Generates structured wiki pages

**Rationale**: Separation of concerns. Script is reusable for other tools; skill provides domain-specific guidance.

### 2. Leverage Existing Infrastructure

**Use what's already there**:
- Pillow (already installed) for image processing
- `.shared/scripts/` pattern for script location
- HTU_Trading schema for output format
- Existing `extract_content.py` pattern for file organization

**Add minimal dependencies**:
- `opencv-python` for advanced preprocessing (contrast, sharpening)
- No Claude API in script (skill handles that)

### 3. Workflow Integration

```
User sends chart.png
    ↓
Claude invokes /chart-context-analysis skill
    ↓
Skill runs: python scripts/analyze_chart.py chart.png
    ↓
Script outputs:
    - chart_processed/
        ├── full.png (upscaled, sharpened)
        ├── tile_1.png (top-left quadrant)
        ├── tile_2.png (top-right quadrant)
        ├── tile_3.png (bottom-left quadrant)
        ├── tile_4.png (bottom-right quadrant)
        └── manifest.md (metadata + context)
    ↓
Skill reads manifest.md + tiles
    ↓
Claude analyzes with enhanced context
    ↓
Skill generates wiki page following HTU_Trading schema
```

## Implementation Tasks

### Phase 1: Script Foundation (analyze_chart.py)

**Task 1: Create script skeleton**
- File: `D:\wiki\.shared\scripts\analyze_chart.py`
- CLI interface: `python analyze_chart.py <input_image> [--output-dir <dir>]`
- Acceptance:
  - Script accepts image path argument
  - Creates output directory structure
  - Handles missing file gracefully
- Verify: `python scripts/analyze_chart.py --help` shows usage

**Task 2: Implement image preprocessing pipeline**
- Functions:
  - `load_image(path)` - Load with Pillow
  - `upscale_image(img, factor=2)` - Bicubic upscaling
  - `sharpen_image(img)` - OpenCV unsharp mask
  - `crop_chart_area(img)` - Auto-detect chart region (remove UI chrome)
- Acceptance:
  - Upscales 2x while preserving aspect ratio
  - Sharpens without artifacts
  - Crops to chart canvas (removes TradingView UI)
- Verify: Visual inspection of `full.png` output

**Task 3: Implement tiling logic**
- Function: `create_tiles(img, grid=(2,2))` - Split into 4 quadrants
- Acceptance:
  - Creates 4 tiles with 10% overlap at edges
  - Each tile is properly labeled (tile_1.png = top-left, etc.)
  - Tiles maintain aspect ratio
- Verify: All 4 tiles load correctly and cover full image

**Task 4: Generate manifest.md**
- Function: `generate_manifest(input_path, output_dir, metadata)`
- Content:
  ```markdown
  # Chart Analysis Context
  
  **Original**: chart.png (1920x1080)
  **Processed**: full.png (3840x2160, upscaled 2x, sharpened)
  
  ## Tiles
  - tile_1.png: Top-left (price action, recent swings)
  - tile_2.png: Top-right (indicators, volume)
  - tile_3.png: Bottom-left (older price history)
  - tile_4.png: Bottom-right (timeline, annotations)
  
  ## Analysis Checklist
  - [ ] Identify swing highs/lows
  - [ ] Mark Protected Swings (swept + confirmed)
  - [ ] Mark Failure Swings (swept, no confirm)
  - [ ] Note liquidity zones
  - [ ] Apply 12-question framework
  ```
- Acceptance:
  - Manifest includes all metadata
  - Checklist aligns with HTU_Trading methodology
- Verify: `manifest.md` is valid markdown

### Checkpoint: Script Complete
- [ ] Script runs end-to-end on sample chart
- [ ] Outputs 1 full.png + 4 tiles + manifest.md
- [ ] No errors on various image formats (PNG, JPG)

### Phase 2: Claude Skill (chart-context-analysis)

**Task 5: Create skill structure**
- Directory: `C:\Users\Admin\.claude\skills\chart-context-analysis\`
- File: `SKILL.md`
- Frontmatter:
  ```yaml
  ---
  name: chart-context-analysis
  description: Analyzes trading chart screenshots with enhanced context. Use when user sends chart images for Protected/Failure Swing analysis. Use when identifying market structure, liquidity, or expansion patterns.
  trigger: /chart-context-analysis
  ---
  ```
- Acceptance:
  - Skill appears in `/help` output
  - Trigger `/chart-context-analysis` invokes skill
- Verify: `/chart-context-analysis --help` works

**Task 6: Write skill workflow**
- Sections:
  1. **Overview** - What the skill does
  2. **When to Use** - Chart screenshots, swing analysis, structure questions
  3. **When NOT to Use** - Non-chart images, code screenshots
  4. **Workflow**:
     - Step 1: Run preprocessing script
     - Step 2: Read manifest.md
     - Step 3: Analyze tiles sequentially (1→2→3→4)
     - Step 4: Synthesize findings
     - Step 5: Apply 12-question framework
     - Step 6: Generate wiki page
  5. **Output Template** - Structured markdown following HTU_Trading schema
  6. **Verification** - Checklist for complete analysis
- Acceptance:
  - Workflow is clear and actionable
  - References actual file paths (D:\wiki\.shared\scripts\analyze_chart.py)
  - Includes HTU_Trading 12-question framework
- Verify: Skill content is complete and follows conventions

**Task 7: Add trading-specific guidance**
- Content:
  ```markdown
  ## Trading Pattern Recognition
  
  ### Protected Swing Detection
  1. Identify swing high/low
  2. Check if price swept beyond it
  3. Verify close outside opposing candle
  4. Mark as Protected if confirmed
  
  ### Failure Swing Detection
  1. Identify swing high/low
  2. Check if price swept beyond it
  3. If no close confirmation → Failure Swing
  4. Note as potential liquidity grab
  
  ### 12-Question Framework Application
  [Groups A-D questions from HTU_Trading/CLAUDE.md]
  ```
- Acceptance:
  - Definitions match HTU_Trading wiki concepts
  - Framework questions are complete
- Verify: Cross-reference with `HTU_Trading/wiki/concepts/*.md`

### Checkpoint: Skill Complete
- [ ] Skill invokes script correctly
- [ ] Workflow produces structured analysis
- [ ] Output follows HTU_Trading schema

### Phase 3: Integration & Testing

**Task 8: Test end-to-end workflow**
- Input: `HTU_Trading/raw/sources/TheMarketLens_TheExpansionFlow.png`
- Steps:
  1. Invoke `/chart-context-analysis TheMarketLens_TheExpansionFlow.png`
  2. Script processes image
  3. Skill analyzes tiles
  4. Output generated in `raw/extracts/`
- Acceptance:
  - Full workflow completes without errors
  - Output includes Protected/Failure Swing identification
  - Wiki page follows schema
- Verify: Manual review of generated analysis

**Task 9: Document usage**
- Update `HTU_Trading/CLAUDE.md`:
  ```markdown
  ## Chart Analysis Workflow
  
  When user sends chart screenshot:
  1. Invoke `/chart-context-analysis <image_path>`
  2. Review processed tiles in output directory
  3. Apply 12-question framework
  4. Generate wiki page with findings
  ```
- Update `.shared/scripts/README.md` (create if missing):
  ```markdown
  ## analyze_chart.py
  
  Preprocesses trading chart screenshots for enhanced analysis.
  
  Usage:
  ```bash
  python scripts/analyze_chart.py chart.png --output-dir chart_processed
  ```
  ```
- Acceptance:
  - Documentation is clear and complete
  - Examples use actual file paths
- Verify: Follow docs to run workflow from scratch

### Checkpoint: Complete
- [ ] End-to-end test passes
- [ ] Documentation updated
- [ ] Ready for production use

## Critical Files

**New files to create**:
- `D:\wiki\.shared\scripts\analyze_chart.py` - Image preprocessing script
- `C:\Users\Admin\.claude\skills\chart-context-analysis\SKILL.md` - Claude skill definition

**Files to update**:
- `HTU_Trading\CLAUDE.md` - Add chart analysis workflow section
- `.shared\scripts\README.md` - Document new script (create if missing)

**Reference files** (read-only):
- `HTU_Trading\wiki\concepts\protected-swings.md` - Protected Swing definition
- `HTU_Trading\wiki\concepts\failure-swings.md` - Failure Swing definition
- `HTU_Trading\CLAUDE.md` - 12-question framework
- `.shared\scripts\extract_content.py` - Pattern for script structure

## Dependencies

**Already installed**:
- Pillow (basic image processing)

**To install**:
```bash
pip install opencv-python  # Advanced preprocessing (sharpen, contrast)
pip install numpy          # Array operations for OpenCV
```

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Large images cause memory issues | High | Add max dimension limit (4K), downsample if needed |
| Script fails on non-chart images | Medium | Add image validation, graceful error handling |
| Tiling loses context at boundaries | Medium | Use 10% overlap between tiles |
| OpenCV not available on system | Low | Fallback to Pillow-only mode (skip sharpening) |

## Verification

Before marking complete:
- [ ] Script runs on sample chart without errors
- [ ] Skill appears in `/help` and is invokable
- [ ] End-to-end workflow produces valid wiki page
- [ ] Documentation is updated and accurate
- [ ] Dependencies are documented in requirements.txt or SETUP-FROM-SCRATCH.md

## Success Criteria

**Script**:
- Accepts any chart image (PNG, JPG)
- Outputs 1 full.png + 4 tiles + manifest.md
- Runs in <10 seconds for typical chart

**Skill**:
- Guides Claude through structured analysis
- Applies HTU_Trading methodology correctly
- Generates wiki page following schema

**Integration**:
- User sends chart → Claude invokes skill → Analysis complete
- Output includes Protected/Failure Swing identification
- No manual preprocessing required
