---
type: concept
title: "Mobilization Testing Procedures"
tags: [mobilization, qaqc, high]
related: ["[[mobilization-plan]]", "[[project-information-production-methods-and-procedures]]"]
created: 2026-09-05
updated: 2026-09-05
---

# Mobilization Testing Procedures

## Core Concept
Under ISO 19650-2 clause 5.5.2, delivery teams must execute dry-run testing of information authoring, federation, and exchange protocols before generating live project containers, preventing costly systematic errors during production.

## Key Test Stages
1. **Shared Resources Verification**: Verifying project templates, title blocks, and classification tables.
2. **Federation & Coordinate Dry-Run**: Exporting sample test models from each authoring tool and checking coordinate origin, orientation, and spatial alignment.
3. **Interoperability & Data Extraction Test**: Testing IFC exports and automated COBie data extraction routines.
4. **CDE Workflow Simulation**: Testing state transitions (WIP -> Shared -> Published), metadata tagging, and approval gates.

## Standard References
- ISO 19650-2:2018 §5.5.2
