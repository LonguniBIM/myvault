---
type: concept
title: Common Data Environment (CDE) Solution Architecture
tags:
  - information-management
  - cde
  - assessment-need
  - critical
  - high
related:
  - "[[common-data-environment-protocol]]"
  - "[[appointing-party]]"
created: 2026-09-03
updated: 2026-09-03
---

# Common Data Environment (CDE) Solution Architecture

Under **ISO 19650-2 §5.1.7**, the [[appointing-party]] must establish the project's Common Data Environment (CDE) solution to serve as the single source of truth for all project information containers.

## Mandatory Functional Capabilities

The CDE technology platform must support:
1. **Unique Container Identification**: Strict enforcement of the naming convention specified in the [[project-information-standard]].
2. **Metadata Attributes**: Capability to assign and track:
   - **Status Code**: Permitted usage suitability (WIP, Shared, Published, Archive).
   - **Revision Code**: Version tracking with minor and major increments.
   - **Classification**: Uniclass or OmniClass metadata tags.
3. **State Transition Workflows**: Managed transitions between CDE states with auditable electronic sign-offs.
4. **Access Control & Permissions**: Granular, role-based security protecting sensitive project information.

---
**Sources:**
- [[unit-4-lesson-6-establish-shared-resources-cde-protocol]]
