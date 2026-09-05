---
type: methodology
title: "Test Information Production Methods & Procedures Method"
steps: 5
source: "[[unit-8-lesson-2-test-projects-information-production-methods-procedures]]"
applicable_role: "lead appointed party"
skill_status: candidate
tags: [mobilization, qaqc, methodology]
related: ["[[project-information-production-methods-and-procedures]]", "[[shared-resources]]"]
created: 2026-09-05
updated: 2026-09-05
---

# Test Information Production Methods & Procedures Method

## Overview
A 5-step procedure for executing dry-run tests of models, coordinates, data exports, and CDE workflows before production begins (ISO 19650-2 §5.5.2).

## Procedure

### Step 1: Distribute Verified Shared Project Templates
Upload approved project seed files, shared parameters, title blocks, and classification tables to CDE Shared Resources.

### Step 2: Author Discipline Test Containers
Have architectural, structural, and MEP task teams create simplified test models containing basic spatial and equipment elements.

### Step 3: Execute Multidisciplinary Federation & Coordinate Test
Export native models to OpenBIM IFC, federate within the coordination viewer, and verify perfect coordinate origin and level alignment.

### Step 4: Test Alphanumeric Data & COBie Extraction
Extract parameter schedules and test COBie spreadsheet generation against client Level of Information Need specifications.

### Step 5: Document Findings & Refine Methods
Hold a testing debrief, rectify template errors or coordinate offsets, and issue the final Mobilization Acceptance Certificate.

## Control Points & Pass/Fail Criteria
- **Pass**: Zero coordinate offset in federated viewer; test IFC and COBie pass schema validation without errors.
- **Fail**: Coordinate drift discovered or required parameter fields failing export from native software.
