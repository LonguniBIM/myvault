---
type: methodology
title: Compile Invitation to Tender Package Method (ISO 19650-2 §5.2.4)
tags:
  - information-management
  - invitation-tender
  - cde
  - high
  - high
related:
  - "[[invitation-to-tender]]"
  - "[[appointing-party]]"
  - "[[tender-evaluation-criteria]]"
created: 2026-09-03
updated: 2026-09-03
steps: 4
source: "[[unit-5-lesson-3-tender-response-evaluation-criteria]]"
applicable_role: "appointing party"
skill_status: candidate
---

# Compile Invitation to Tender Package Method

This methodology operationalizes **ISO 19650-2 Clause 5.2.4**, detailing the process for the [[appointing-party]] to compile, verify, and publish the complete [[invitation-to-tender]] (ITT) information package via the Common Data Environment (CDE).

## Pre-conditions & Inputs
- Established Exchange Information Requirements (EIR) per §5.2.1.
- Assembled reference information and shared resources per §5.2.2.
- Established tender response requirements and evaluation criteria per §5.2.3.
- Operational Project Common Data Environment (CDE).

## Step-by-Step Procedure

### Step 1: Package Assembly & Verification
- Collate all required information containers comprising the ITT:
  1. EIR and Project Information Standard.
  2. Reference information (existing condition surveys, point clouds, utility records).
  3. Shared resources (BEP templates, responsibility matrix templates, model templates).
  4. Tender response requirements & evaluation scoring rubric.

### Step 2: Assign CDE Status Codes
- Mandated by ISO 19650-2 §5.2.4: Each information container must have a defined status code assigned prior to sharing.
- Ensure containers are flagged with the exact permitted use (e.g., "For Tender Reference Only", "Not for Construction", "Information Only").

### Step 3: Publish to Project CDE
- Upload assembled and status-coded containers to the appropriate section of the CDE.
- Configure access rights and permissions for prospective tendering organizations.

### Step 4: Issue ITT Notification & Audit Trail
- Issue formal ITT notification referencing the CDE location.
- Record timestamps, version IDs, and access logs as audit evidence.

---
**Skill Candidate:**
- Potential Claude Skill: `itt-package-validator`
- Trigger: Preparation of tender release package by Appointing Party.
