---
type: methodology
title: "Undertake Quality Assurance Checks Method"
steps: 5
source: "[[unit-9-lesson-2-undertake-quality-assurance-checks]]"
applicable_role: "appointed party"
skill_status: candidate
tags: [collaborative-production, qaqc, methodology]
related: ["[[appointed-party]]", "[[task-information-delivery-plan]]"]
created: 2026-09-05
updated: 2026-09-05
---

# Undertake Quality Assurance Checks Method

## Overview
A 5-step procedure for performing internal quality control and standards verification before releasing containers for sharing (ISO 19650-2 §5.6.2).

## Procedure

### Step 1: Execute Technical & Regulatory Review
Verify that engineering calculations, architectural layouts, and dimensions satisfy project design criteria and safety codes.

### Step 2: Execute BIM Standards & Syntax Audit
Run automated rule checkers to verify container naming, layer conventions, material definitions, and parameter population.

### Step 3: Verify LOIN Compliance Against TIDP
Compare container geometric detail and alphanumeric data fields against the requirements scheduled in the team's TIDP.

### Step 4: Run Internal Discipline Clash Detection
Perform collision tests within the discipline model and against recent Shared reference containers to eliminate obvious clashes.

### Step 5: Sign Off QA Gate or Issue Rectification Notes
If checks pass, sign the Task QA Certificate and authorize transition; if failed, assign rework tasks to authors within WIP.

## Control Points & Pass/Fail Criteria
- **Pass**: 100% of mandatory parameters populated; zero major internal clashes; signed QA check sheet.
- **Fail**: Model contains unclassified elements, missing COBie properties, or uncoordinated spatial collisions.
