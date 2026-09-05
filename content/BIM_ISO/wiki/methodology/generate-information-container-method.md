---
type: methodology
title: "Generate Information Container Method"
steps: 5
source: "[[unit-9-lesson-1-generate-information]]"
applicable_role: "appointed party"
skill_status: candidate
tags: [collaborative-production, methodology]
related: ["[[appointed-party]]", "[[project-information-standard]]"]
created: 2026-09-05
updated: 2026-09-05
---

# Generate Information Container Method

## Overview
A 5-step procedure for authoring compliant information containers strictly within the CDE Work In Progress (WIP) state (ISO 19650-2 §5.6.1).

## Procedure

### Step 1: Check Availability of Reference Information
Before modeling, check the CDE Shared state to download the latest approved structural, architectural, or civil reference models.

### Step 2: Initialize Container in WIP State
Create new container using project template; apply ISO 19650 standard container naming syntax and initial draft revision (`P01.01`).

### Step 3: Author Geometric Elements per LOIN
Model geometry in strict accordance with project spatial boundaries, discipline level of detail, and coordinate origins.

### Step 4: Embed Alphanumeric Properties & Classification
Attach required property sets, parameter values, and Uniclass 2015 classification codes to model elements.

### Step 5: Derive Linked Documentation
Generate 2D drawings, schedules, and calculation sheets directly linked to native geometry to preserve single source of truth.

## Control Points & Pass/Fail Criteria
- **Pass**: Container naming matches project standard; geometry aligns with origin; classification codes assigned.
- **Fail**: Container authored on local desktop outside WIP, using unverified reference backgrounds.
