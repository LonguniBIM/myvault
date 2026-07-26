# Wiki Schema — BIM ISO 19650 Mastery

## Page Types

| Type | Directory | Purpose |
|------|-----------|---------|
| entity | wiki/entities/ | Named things: standards (ISO 19650-1/2), documents (EIR, BEP, MIDP/TIDP), roles (appointing party), systems (CDE platforms), organizations (buildingSMART, BSI) |
| concept | wiki/concepts/ | Ideas and frameworks: Level of Information Need, information container, common data environment states, classification systems |
| source | wiki/sources/ | Standards text, guidance documents, templates, training materials, case studies |
| query | wiki/queries/ | Open questions: "When does this requirement apply?", "Who is responsible for X?" |
| comparison | wiki/comparisons/ | Side-by-side: CDE platforms, BEP templates, LOIN approaches by project type/stage |
| synthesis | wiki/synthesis/ | Cross-cutting conclusions spanning multiple standards/sources |
| thesis | wiki/thesis/ | Working hypotheses about effective ISO 19650 implementation |
| methodology | wiki/methodology/ | Step-by-step methods extracted from standards/guidance (Skill candidates) |
| finding | wiki/findings/ | Empirical results from applying methods to real project documents |
| skill | wiki/skills/ | Validated Claude Skills ready for deployment (analyze EIR, review BEP, QA/QC, etc.) |

## Naming Conventions

- Files: `kebab-case.md`
- Entities: match official term (e.g., `iso-19650-2.md`, `eir.md`, `common-data-environment.md`, `appointing-party.md`)
- Concepts: descriptive noun phrases (e.g., `level-of-information-need.md`, `container-status-workflow.md`)
- Sources: `standard-or-org-year-slug.md` (e.g., `iso-19650-2-2018-delivery-phase.md`, `uk-bim-framework-2021-guidance-part-2.md`)
- Queries: question as slug (e.g., `who-approves-tidp-milestones.md`)
- Methodologies: method name (e.g., `eir-to-requirement-register.md`, `bep-compliance-review.md`)
- Skills: skill name (e.g., `bep-review-skill.md`, `model-qaqc-checklist-skill.md`)

## Frontmatter

All pages must include YAML frontmatter:

```yaml
---
type: entity | concept | source | query | comparison | synthesis | thesis | methodology | finding | skill
title: Human-readable title
tags: []
related: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### Tag Categories

| Category | Values | Usage |
|----------|--------|-------|
| topic | `information-management`, `eir-air`, `bep`, `cde`, `midp-tidp`, `roles-responsibility`, `loin`, `naming-classification`, `model-checking`, `coordination`, `handover`, `compliance` | Primary subject area |
| stage | `assessment-need`, `invitation-tender`, `mobilization`, `collaborative-production`, `operational` | ISO 19650 delivery phase |
| priority | `critical`, `high`, `medium`, `low` | Importance for mastery |
| confidence | `high`, `medium`, `low`, `speculative` | How well-validated the content is against source text |

### Type-Specific Frontmatter

**Source pages:**
```yaml
authors: []
year: YYYY
url: ""
venue: ""          # ISO, UK BIM Framework, buildingSMART, BSI, internal, etc.
clause_refs: []     # e.g. ["ISO 19650-2 §5.3"]
skill_potential: true | false    # Can this become a numbered-step Skill?
```

**Methodology pages:**
```yaml
steps: 5
source: "[[source-slug]]"
applicable_role: ""              # appointing party | lead appointed party | appointed party | task team
skill_status: candidate | drafted | tested | deployed
```

**Skill pages:**
```yaml
trigger: ""                      # When to invoke this skill
steps: 5
tested_in: []                    # Projects/documents where this was tested
effectiveness: low | medium | high
```

**Thesis pages:**
```yaml
confidence: low | medium | high
status: speculative | supported | refuted | settled
```

**Finding pages:**
```yaml
source: "[[source-slug]]"
confidence: low | medium | high
replicated: true | false | null
```

**Comparison pages:**
```yaml
subjects: []                     # Items being compared
best_fit: "[[entity-slug]]"
best_fit_reason: ""
```

## Index Format

`wiki/index.md` lists all pages grouped by type. Each entry:
```
- [[page-slug]] — one-line description
```

## Log Format

`wiki/log.md` records activity in reverse chronological order:
```
## YYYY-MM-DD

- Action taken / finding noted
```

## Cross-referencing Rules

- Use `[[page-slug]]` syntax to link between wiki pages
- Every entity and concept should appear in `wiki/index.md`
- Queries link to the sources and concepts they draw on
- Synthesis pages cite all contributing sources via `related:`
- Findings link back to their source via the `source:` frontmatter field
- Methodology pages link to the skill they generated (if any)
- Skill pages link back to methodology and source

## Ten-Question Analysis Framework

When ingesting any new source (standard clause, guidance doc, template, case study), answer these questions (from `purpose.md`):

1. **Problem**: What information-management problem does this document/clause solve?
2. **Applicability**: What stage, organization, role, or information type does it apply to?
3. **Process**: What steps, decisions, and control points does it describe? → methodology candidate
4. **Evidence**: What inputs, outputs, and evidence are needed to prove compliance?
5. **Principles**: What requirements or principles recur across documents?
6. **Risks**: What mistakes or anti-patterns commonly occur when applying this?
7. **Operationalization**: How does this become a checklist, template, validation rule, or workflow?
8. **Skill test**: Can the method be described as numbered steps, trigger conditions, and completion criteria?
9. **Skill design**: What role/moment/output would the resulting Claude Skill support?
10. **Validation**: How should this method be tested on a real project before reuse?

Record answers in the source page; extract methodologies to `wiki/methodology/` and skill candidates to `wiki/skills/`.

## Contradiction Handling

When sources or clauses contradict each other, or a guidance document diverges from the ISO text:
1. Note the contradiction in the relevant concept or entity page
2. Create or update a query page to track the open question
3. Link both sources from the query page, citing clause references
4. Resolve in a synthesis page once sufficient evidence exists
5. If both approaches are valid for different project types/stages, create a comparison page instead of forcing resolution

## Traceability Rule

Every compliance-relevant claim (e.g., "this satisfies ISO 19650-2 §5.6") must cite the specific clause or document section it is based on. Do not assert "ISO compliant" without a named criterion and project evidence — this mirrors the `purpose.md` out-of-scope constraint on unsupported compliance claims.
