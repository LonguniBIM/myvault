---
type: methodology
title: "Archive Project Information Model Method"
steps: 5
source: "[[unit-11-lesson-1-archive-the-pim]]"
applicable_role: "appointing party / lead appointed party"
skill_status: candidate
tags: [close-out, cde, methodology]
related: ["[[project-information-model]]", "[[common-data-environment-protocol]]"]
created: 2026-09-05
updated: 2026-09-05
---

# Archive Project Information Model Method

## Overview
A 5-step procedure for archiving the Project Information Model and extracting operational data for the Asset Information Model at project close-out (ISO 19650-2 §5.8.1).

## Procedure

### Step 1: Finalize As-Constructed Verified Containers
Ensure all Published containers reflect final as-built conditions and manufacturer asset specifications.

### Step 2: Extract Maintainable Asset Data for AIM
Filter operational asset parameters (equipment tags, serial numbers, maintenance manuals) to generate the Asset Information Model (AIM).

### Step 3: Transition Entire CDE Repository to Archive State
Lock the project CDE environment, transitioning all containers, WIP logs, and coordination records into read-only Archive.

### Step 4: Export Open Standards Backup Packages
Generate permanent OpenBIM archive packages (IFC models, PDF/A documentation, COBie spreadsheets) to prevent proprietary lock-in.

### Step 5: Transfer Archive Ownership & Issue Protocol Sign-off
Deliver the archived PIM dataset and CDE transfer certificate to the Appointing Party's facilities management organization.

## Control Points & Pass/Fail Criteria
- **Pass**: CDE permanently locked to read-only; OpenBIM backup complete; verified AIM handed to client FM.
- **Fail**: CDE left open to ongoing editing or abandoned without generating accessible archive backups.
