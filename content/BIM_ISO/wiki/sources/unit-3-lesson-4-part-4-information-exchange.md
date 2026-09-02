---
title: "Unit 3 - Lesson 4 - Part 4: Information Exchange"
type: source
tags:
  - information-management
  - compliance
  - naming-classification
  - high
  - high
source_url: https://elearning.bre.ac/pluginfile.php/191403/mod_resource/content/8/content/index.html#/lessons/94hiuVT-qIcTrVFJShdE_LYturNfgGqY
venue: "BRE Academy / ISO 19650"
clause_refs:
  - "ISO 19650-4"
  - "BS 1192-4"
skill_potential: true
created: 2026-08-23
updated: 2026-09-03
---

# Unit 3 - Lesson 4 - Part 4: Information Exchange

*Lesson 4 of 5*

## Lesson Objectives


At the end of this lesson, you will be able to:

Understand the soon to be released ISO 19650 part 4, and the transition from BS 1192-4.

Describe COBIe

## BS 1192-4 / ISO 19650:4 

BS 1192-4 is a code of best practise for the implementation of COBie that formed part of the BIM Level 2 suite of documents.

COBie is an internationally agreed information exchange schema for exchanging information relating to maintainable assets.  COBie is managed by the building SMART alliance.

**ISO 19650 Part 4: Information Exchange** is currently under development and out for public comments.

An information exchange is defined as: “act of satisfying an information requirement or part thereof”

'data drops’ as they were formally known, or information exchanges now are required at key milestones to enable the exchange, and checking of information for compliance with the project standards.

---

![m3s227.PNG](unit-3-lesson-4-part-4-information-exchange/assets/jfyW30TNSnpt08Ww_WDV_fJQXBkFXAmVn.jpg)

There should be a valid reason and in what context, to ask for COBie information In relation to an asset. BS 1192-4 requires that the Employer (Now referred to as Appointing Party states:

The aspects of the facility that are intended to be managed

## Uniclass 2015


Uniclass 2015 is a key component in the U.K, as all maintainable assets must be assigned an appropriate classification code.

The three levels of Uniclass that can be assigned to an object are:

EF - Elements/function

EF - Elements/function

[https://toolkit.thenbs.com(opens in a new tab)](https://toolkit.thenbs.com/)

many CAFM systems are using classification systems to structure documentation., and manage assets. This provides a single, international method of recognising items within buildings.

## COBIe Spreadsheet


COBie can be delivered as a spreadsheet or an xml file, and is software agnostic.

See below an example delivery, provided by Prairie Sky Consulting of a typical output.

The input method, contents, and delivery of COBie shall be covered under a separate course by the BRE.

![https://www.prairieskyconsulting.com/resource.htm](unit-3-lesson-4-part-4-information-exchange/assets/CpShaV_ukL_OKRyj_BruX_nxBpEOnyu5X.jpg)

*
https://www.prairieskyconsulting.com/resource.htm
*

![See here an example delivery, from our Building 16 model.](unit-3-lesson-4-part-4-information-exchange/assets/eOGOckQ0W_Uij_EK_LmBhEM8hcJiG0a38.jpg)

*See here an example delivery, from our Building 16 model.*

## Learning Summary 

Lesson complete! You are now able to:

Understand the soon to be released ISO 19650 part 4, and the transition from BS 1192-4.

Describe COBIe

**[CONTINUE]**


---

## Ten-Question Analysis Framework

### 1. Problem
How do parties verify that an information exchange satisfies its requirements in a software-agnostic, open format without vendor lock-in?

### 2. Applicability
- **Standards**: ISO 19650-4, BS 1192-4 (COBie), buildingSMART standards.
- **Key Concepts**: OpenBIM, COBie (Construction Operations Building information exchange), Uniclass 2015.

### 3. Process
1. Define information exchange criteria and required schemas (e.g. COBie spreadsheet / XML / IFC).
2. Assign standardized classification codes (Uniclass 2015 tables).
3. Validate alphanumeric asset data against the EIR.
4. Execute formal exchange at the scheduled milestone date.
5. Ingest into CAFM / computerized maintenance management systems.

### 4. Evidence
- Validated COBie spreadsheets / IFC datasets.
- Schema compliance check reports.

### 5. Principles
- **Satisfying Requirements**: An information exchange is defined as the act of satisfying an information requirement.
- **Software Agnostic**: Data must survive across systems independently of authoring applications.

### 6. Risks & Anti-patterns
- Generating COBie without checking data accuracy, resulting in empty or corrupt rows.
- Demanding COBie without clear facility management use cases.

### 7. Operationalization
- Automated COBie / IFC data validator checking field completion and classification syntax.

### 8. Skill Test
Can this become a Skill?
**Yes** — Candidate: `cobie-validator`.

### 9. Skill Design
- **Supported Role**: Information Manager / Handover Coordinator.
- **Trigger**: Information exchange submission.

### 10. Validation Plan
Run automated schema validation against sample COBie files.

---

## Knowledge Space Links
- **Entities**: [[iso-19650-4]]
- **Concepts**: [[openbim-information-exchange]]

---
*Extracted from `Lesson 4 - Part 4: Information Exchange - ISO 19650 1&2 Project Delivery_ Unit 3 - BIM According to ISO 19650_.html` via webpage-content-extractor.*
