---
type: methodology
title: "Submit, Review & Approve for Sharing Method"
steps: 5
source: "[[unit-9-lesson-3-submit-review-approve-for-sharing]]"
applicable_role: "appointed party / lead appointed party"
skill_status: candidate
tags: [collaborative-production, cde, methodology]
related: ["[[common-data-environment-protocol]]", "[[lead-appointed-party]]"]
created: 2026-09-05
updated: 2026-09-05
---

# Submit, Review & Approve for Sharing Method

## Overview
A 5-step procedure to transition information containers through CDE states with standard status codes and revision increments (ISO 19650-2 §5.6.3 - §5.6.5).

## Procedure

### Step 1: Assign Suitability Status Code
Assign standard suitability code (e.g. `S1` - Coordination, `S2` - Information, `S3` - Review & Comment) based on intended use.

### Step 2: Increment Metadata Revision Identifier
Update revision code from WIP draft decimal (`P01.01`) to preliminary shared integer (`P01`).

### Step 3: Transition Container to CDE Shared State
Submit container into the CDE Shared area, notifying multidisciplinary delivery team members.

### Step 4: Conduct Multidisciplinary Coordination Review
Lead Appointed Party federates shared containers, runs cross-discipline clash detection, and logs issues via BCF.

### Step 5: Authorize Transition to Published State
Upon achieving coordination sign-off, assign contractual status code (e.g. `A1`) and transition container to Published.

## Control Points & Pass/Fail Criteria
- **Pass**: Status code explicitly declared; revision syntax valid; CDE audit log records transition timestamp.
- **Fail**: Container shared with informal status tag ("For review") or skipped CDE approval gates.
