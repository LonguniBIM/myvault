---
type: methodology
title: Tender Response Evaluation Method (ISO 19650-2 §5.2.3)
tags:
  - information-management
  - invitation-tender
  - compliance
  - high
  - high
related:
  - "[[tender-evaluation-criteria]]"
  - "[[tender-response-requirements]]"
  - "[[pre-appointment-bep]]"
  - "[[appointing-party]]"
created: 2026-09-03
updated: 2026-09-03
steps: 7
source: "[[unit-5-lesson-3-tender-response-evaluation-criteria]]"
applicable_role: "appointing party"
skill_status: candidate
---

# Tender Response Evaluation Method

This methodology operationalizes the technical evaluation of prospective delivery teams' tender returns under **ISO 19650-2 Clause 5.2.3**. It provides a structured, repeatable procedure for the [[appointing-party]] (or its appointed information management representative) to evaluate compliance, capability, and risk.

## Pre-conditions & Inputs
- Issued [[invitation-to-tender]] (ITT) package including Exchange Information Requirements (EIR).
- Defined acceptance criteria and scoring rubric.
- Submitted tender returns from prospective lead appointed parties containing the 6 required submission artifacts.

## Step-by-Step Procedure

### Step 1: Completeness & Compliance Check (Pass/Fail Gate)
- Review the completed tender return checklist.
- Verify that all mandatory components are present: Pre-appointment BEP, IM competency assessment, capability/capacity summary, risk assessment, and mobilization plan.
- *Gate criteria*: Any missing mandatory artifact results in immediate request for clarification or rejection.

### Step 2: Pre-appointment BEP Assessment (Understanding of Requirements)
- Cross-reference the proposed [[pre-appointment-bep]] against the project EIR.
- Check whether the proposed information standards, formats, and container conventions directly satisfy EIR requirements.
- Evaluate the proposed federation, clash management, and quality control procedures.

### Step 3: Information Management Function Competency Audit
- Audit the curriculum vitae, project portfolio, and certifications of nominated Information Management leads.
- Validate experience against the project scale and BIM maturity requirements.

### Step 4: Capability and Capacity Verification
- Analyze the Delivery Team Capability and Capacity Summary.
- Verify hardware/software infrastructure, license readiness, and available staffing hours throughout the anticipated delivery milestones.

### Step 5: Information Delivery Risk Assessment Evaluation
- Review the submitted Information Risk Register.
- Assess whether identified risks are realistic, comprehensive, and paired with actionable mitigation measures.

### Step 6: Mobilization Plan Feasibility Review
- Inspect the mobilization schedule and testing proposals.
- Ensure adequate time and testing protocols are allocated for:
  - CDE integration and access configuration.
  - Software template setup and IFC schema exchange tests.
  - Delivery team training on project information standards.

### Step 7: Scoring, Normalization & Recommendation
- Synthesize technical scores across all categories.
- Ensure the IM score is kept strictly independent of commercial pricing.
- Provide the technical IM evaluation report to the procurement board with clear recommendations (Accept, Accept with conditions, or Reject).

## Diagnostic & Acceptance Questions (Skill Rules)
1. *Did the delivery team address each item in the EIR or merely provide a standard template?*
2. *Is the Information Management role assigned to dedicated, qualified individuals?*
3. *Does the mobilization plan contain specific, verifiable test milestones before information production?*

---
**Skill Candidate:**
- Potential Claude Skill: `tender-evaluation-checker` / `pre-appointment-bep-reviewer`
- Trigger: Receipt of tender package submission during `invitation-tender` stage.
