# EU AI Act GRC Manual — English Editorial and Internal-Consistency QA Register

**Branch:** `manual/eu-ai-act-grc-compliance`  
**Status:** Active publication-closure register

## Scope

This register controls the full English editorial review of the foundation, front matter, Chapters 1–138, Appendices A–Z, figures, tables, source notes, and publication assembly.

## Editorial baseline

- Use professional English consistently.
- Use British spelling where EU legal terminology or established source wording requires it, including `authorised`, `organisation`, `categorisation`, and `minimisation`.
- Preserve exact statutory terminology when quoting or closely paraphrasing the regulation.
- Do not mix British and American variants within a chapter except in proper names or source titles.
- Distinguish statutory duty, contractual duty, organisation-imposed control, recommended governance practice, and optional enhancement.
- Use `must` only for a verified binding duty or a clearly identified internal mandatory control.
- Use `should` for recommended governance and assurance practices.
- Use `may` for permission, possibility, or optional enhancement.

## Required chapter sequence

The default sequence is:

1. Requirement
2. Plain-English explanation
3. GlobalWay example
4. Control activity
5. Evidence
6. Audit test
7. Primary legal references

A justified variation may be used for worksheets, roadmaps, legal classifications, or chapters requiring additional technical structure.

## Global terminology controls

| Term | Controlled usage |
|---|---|
| AI system | Use the statutory concept and avoid treating every algorithm or software rule as an AI system without assessment |
| GPAI model | Keep distinct from a downstream AI system |
| Provider | Use only where the facts satisfy the applicable statutory role |
| Deployer | Use for an organisation using an AI system under its authority in the relevant professional context |
| Authorised representative | Use British spelling and the statutory role meaning |
| High-risk AI system | Use only after Article 6 and Annex I/III analysis |
| Fundamental-rights impact assessment | Distinguish the Article 27 statutory process from broader voluntary rights-impact reviews |
| Post-market monitoring | Distinguish binding provider duties from broader organisational operational monitoring |
| Serious incident | Use the statutory definition and actor-specific reporting framework where making a legal claim |
| Substantial modification | Use the statutory concept; do not equate every material business change with a legal substantial modification |
| Conformity readiness | Identify as an internal readiness practice, not the conformity assessment itself |

## Known consistency findings

| ID | Area | Finding | Required action | Status |
|---|---|---|---|---|
| ED-001 | Foundation | Source hierarchy and timeline predate the 30 July 2026 correction | Integrate Regulation (EU) 2026/1744 and corrected dates directly into the canonical foundation source | Open |
| ED-002 | Chapters 71–79 | Alternate titles and topic overlap remain | Complete content migration and lock one canonical title per chapter | Open |
| ED-003 | Chapters 80–138 | Long-form originals and shorter corrected masters coexist | Compare nonduplicative examples, tables, controls, and tests before archive decision | Open |
| ED-004 | Appendices A–Z | Original and corrected-master pairs coexist | Lock corrected masters in publication source map and validate internal references | Open |
| ED-005 | Mandatory language | Some original drafts may present governance practices as direct legal duties | Recheck all canonical sources and migrated content for `must`, `required`, `shall`, and equivalent wording | Open |
| ED-006 | Spelling | British and American variants may be mixed across source families | Run whole-manual spelling normalization while preserving proper names and source titles | Open |
| ED-007 | Cross-references | Chapter and appendix references may point to original or alternate files | Validate all links against the canonical source map | Open |
| ED-008 | GlobalWay | Business-owner titles and system descriptions vary between chapters | Create and enforce a GlobalWay fact sheet and role register | Open |
| ED-009 | Controls | Control IDs may be incomplete or inconsistent | Reconcile all control IDs against Appendix U and the article-to-control map | Open |
| ED-010 | Evidence | Evidence descriptions vary in specificity | Require system, model, version, owner, date, and repository traceability where relevant | Open |
| ED-011 | Audit tests | Some audit tests may not identify population, period, criteria, or evidence | Normalize audit-test language using a risk-based and reproducible structure | Open |
| ED-012 | Roadmaps | Internal 30/90-day and annual milestones may be mistaken for statutory dates | Retain explicit non-statutory roadmap disclaimers and link to the legal timeline | Open |

## GlobalWay controlled facts

Until replaced by a verified publication fact sheet, use the following baseline:

- Name: GlobalWay Travel Services
- Nature: fictional multinational travel-management company
- Primary customers: enterprise clients and corporate travellers
- Geographic scope: European Union and other regions
- Recurring systems: traveller assistant, travel-recommendation engine, disruption support, recruitment screening, employee analytics, fraud detection, supplier-risk scoring, and generative-AI support for travel consultants
- Typical legal posture: often a deployer, but role must be reassessed for own-brand placement, product integration, intended-purpose change, or substantial modification
- Core oversight principle: consequential, safety-sensitive, employment, accessibility, refund, legal, and exceptional travel matters require meaningful trained human review

## Cross-reference validation protocol

For every internal reference:

1. confirm the chapter or appendix exists;
2. confirm the number and title match the canonical source map;
3. confirm the referenced section actually addresses the stated topic;
4. replace file-name references with publication-stable chapter or appendix references where possible;
5. test relative repository links;
6. record broken or ambiguous references in the closure log.

## Control-ID protocol

Control IDs must:

- use a stable `EUAI-<DOMAIN>-<NN>` format;
- map to one or more legal, contractual, or organisational requirements;
- identify an accountable owner and operator;
- define frequency or trigger;
- identify evidence;
- identify a test method;
- avoid duplicate IDs for materially different controls.

## Editorial closure evidence

| Batch | Scope | Reviewer | Findings | Corrections committed | Validation complete | Commit SHA |
|---|---|---|---|---|---|---|
| | | | | | | |

## Closure criteria

Editorial closure requires:

- one canonical English source for every chapter and appendix;
- no unresolved duplicate numbering or title conflicts;
- consistent terminology and spelling;
- correct mandatory/recommended/optional modality;
- verified chapter, article, appendix, figure, table, and control references;
- no placeholders, abandoned notes, or unexplained incomplete sections;
- GlobalWay facts and roles internally consistent;
- evidence and audit-test language publication-ready;
- all material findings closed or explicitly accepted by the owner.