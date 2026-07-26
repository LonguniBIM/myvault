# Research Log

## 2026-07-25
- Extracted [lesson]: **Lesson 2 - Global Drivers** (from `Unit 1 - Lesson 2`)
- Extracted [lesson]: **Lesson 3 - A History of BIM** (from `Unit 1 - Lesson 2`)
- Extracted [lesson]: **Lesson 1 - BIM Defined** (from `Unit 1 - Lesson 1`)
- Extracted [lesson]: **Construction 4.0** (from `Unit 1 - Lesson 6`)
- Extracted [lesson]: **Lesson 5 - Making Change Happen** (from `Unit 1 - Lesson 5`)
- Extracted [lesson]: **Lesson 4 - The Effect of Poor Information** (from `Unit 1 - Lesson 4`)
- Extracted [lesson]: **Lesson 3 - A History of BIM** (from `Unit 1 - Lesson 3`)
- Extracted [lesson]: **Lesson 1 - BIM Defined** (from `Unit 1 -Lesson 1`)
- Auto-Ingested [lesson]: **Lesson 1 - BIM Defined** into Knowledge Space.
  - Applied 10-Question Analysis Framework.
  - Extracted Concepts: [[building-information-modeling]], [[information-model]], [[level-of-information-need]].
- Extracted [lesson]: **Lesson 1 - BIM Defined** (from `Lesson 1 - BIM Defined - BIM ISO 19650 1&2 Project Delivery_ Unit 1 - Catalyst for Change`)


## 2026-07-23
- Extracted [lesson]: **Lesson 1 - BIM Defined** (from `Lesson 1 - BIM Defined - BIM ISO 19650 1&2 Project Delivery_ Unit 1 - Catalyst for Change`)

### Wiki setup

**Method**: Ran `bridge.ps1 add-space "BIM_ISO"` from `D:\wiki`, then created space-specific files and wiki structure per `SETUP-FROM-SCRATCH.md`.

**Actions completed**:
- Created junctions (`scripts`, `.claude/skills`, `.claude/commands`, `.cursor/rules/tests`) and hard links (shared `.mdc` cursor rules) via bridge script
- Created `wiki/{entities,concepts,sources,queries,comparisons,findings,methodology,synthesis,thesis,skills}/` and `raw/sources/`
- Wrote `schema.md` (page types, naming, frontmatter, ten-question analysis framework — adapted from `purpose.md` sub-questions) and `CLAUDE.md` (agent operating guide) tailored to BIM ISO 19650
- Wrote `wiki/index.md`, `wiki/log.md`, `wiki/overview.md` starter files
- Updated `.space.json` purpose field

**Next**: Drop first ISO 19650 sources (standard extracts, EIR/BEP templates, guidance docs) into `raw/sources/`, then run ingest pipeline per `CLAUDE.md`.
