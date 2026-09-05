---
type: concept
title: "PIM Archiving Protocol"
tags: [close-out, cde, high]
related: ["[[project-information-model]]", "[[common-data-environment-protocol]]", "[[iso-19650-3]]"]
created: 2026-09-05
updated: 2026-09-05
---

# PIM Archiving Protocol

## Core Concept
Under ISO 19650-2 clause 5.8.1, at project close-out, the final Project Information Model (PIM) and all historical CDE audit logs are transitioned to the CDE **Archive** state to ensure long-term legal protection and provide the baseline for operations.

## Protocol Core Elements
1. **Immutability**: Permanent read-only permissions preventing any retrospective tampering.
2. **PIM to AIM Extraction**: Filtering maintainable asset data to populate the operational Asset Information Model under ISO 19650-3.
3. **Format Longevity**: Archiving open data formats (IFC, PDF/A, COBie/CSV) alongside proprietary native files.
4. **Audit Trail Retention**: Preserving container transaction records, approval signatures, and status changes.

## Standard References
- ISO 19650-2:2018 §5.8.1
