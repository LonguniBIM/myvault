---
type: concept
title: "CDE Sharing & Approval Workflow"
tags: [cde, collaborative-production, critical]
related: ["[[common-data-environment-protocol]]", "[[lead-appointed-party]]", "[[appointed-party]]"]
created: 2026-09-05
updated: 2026-09-05
---

# CDE Sharing & Approval Workflow

## Core Concept
Under ISO 19650-2 clauses 5.6.3 to 5.6.5, information transitions across CDE states (**WIP → Shared → Published → Archive**) are governed by explicit review gates, standard suitability status codes, and strict revision discipline.

## State Transitions & Status Codes
- **WIP → Shared (§5.6.3)**: Authorized by the task team upon passing internal QA. Assigned non-contractual status codes (e.g. `S1` - Coordination, `S2` - Information). Decimal revisions become integer revisions (`P01.01` → `P01`).
- **Shared Coordination (§5.6.4)**: Used for multidisciplinary federation and clash coordination.
- **Shared → Published (§5.6.5)**: Authorized by the Lead Appointed Party and accepted by the Appointing Party for milestone deliverables or construction. Assigned contractual status codes (e.g. `A1`, `B1`) and contractual revision codes (`C01`).
- **Published → Archive (§5.8.1)**: Preserved permanently as a read-only historical record.

## Standard References
- ISO 19650-1:2018 §12 (Common data environment)
- ISO 19650-2:2018 §5.6.3 - §5.6.5
- ISO 19650-2:2018 National Annex NA (Status and revision codes)
