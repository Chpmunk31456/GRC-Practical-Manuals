# Manual 50 — Controlled Crosswalk Mapping Schema

**Canonical stage:** 1  
**Goal:** create a repeatable crosswalk method that maximises common-control reuse without creating false equivalence.

## Mandatory row structure

Each crosswalk row must contain:

1. **Common control objective** — independently worded enterprise objective.
2. **Manual 46 control relationship** — universal operating-model anchor.
3. **EU AI Act relationship** — legal relationship and role/scope qualifier.
4. **ISO/IEC 42001 relationship** — management-system relationship stated without reproducing protected standard text.
5. **NIST AI RMF / AI 600-1 relationship** — GOVERN/MAP/MEASURE/MANAGE or GenAI-profile relationship.
6. **Singapore relationship** — MGF / GenAI / AI Verify / Agentic AI relationship as applicable.
7. **OECD relationship** — relevant principle relationship.
8. **Relationship type** — direct, partial, supporting, contextual, or none.
9. **Shared evidence** — evidence that can legitimately support multiple governance objectives.
10. **Framework-specific evidence** — evidence needed only for a particular regime or obligation.
11. **Difference / qualification note** — actors, thresholds, scope, legal status, timing or terminology differences.
12. **Mapping rationale / source reference** — why the relationship is supportable.
13. **Review status** — drafted / technically reviewed / legally reviewed where required / approved.

## Relationship types

### Direct
The independently worded common control objective materially addresses the source concept, subject to stated scope. 'Direct' does not mean legal equivalence.

### Partial
The control addresses part of the source concept but additional process, evidence, scope or role treatment is required.

### Supporting
The control helps satisfy or evidence the source concept but is not itself sufficient.

### Contextual
The source concept informs governance design but does not map cleanly to the same control objective.

### None
No defensible relationship. Leave the mapping blank or state 'none'.

## Anti-false-equivalence tests

Before accepting a mapping, ask:

- Are the source instruments the same legal/status type?
- Do they apply to the same actors?
- Do they apply at the same lifecycle stage?
- Do they use the same threshold or risk condition?
- Do they require the same evidence?
- Does one impose a mandatory legal outcome while another merely recommends a practice?
- Is certification involved?
- Is the relationship based on actual source concepts rather than similar vocabulary?

If any answer exposes a material difference, record the difference explicitly and downgrade the relationship from direct where appropriate.

## Core crosswalk domains

1. governance and accountability;
2. AI inventory;
3. roles/value-chain responsibility;
4. risk classification/tiering;
5. risk and impact assessment;
6. human-rights/fundamental-rights/human-impact considerations;
7. data governance and privacy;
8. security, robustness and resilience;
9. transparency and explainability;
10. human oversight/accountability checkpoints;
11. testing, evaluation, verification and validation;
12. documentation and recordkeeping;
13. deployment/approval gates;
14. third-party and supply-chain governance;
15. monitoring and continuous assurance;
16. incident management;
17. change management and revalidation;
18. audit / independent assurance;
19. AI literacy and competence;
20. continuous improvement;
21. agent identity, autonomy, tool permissions and action provenance.

## Common evidence classes

Potential reusable evidence includes:

- governance charter and RACI;
- AI inventory;
- risk/impact assessment;
- data-flow and lineage documentation;
- model/system card or technical documentation;
- evaluation/TEVV report;
- human-oversight procedure and approval logs;
- security architecture and access-control evidence;
- vendor assessment and contractual controls;
- monitoring/KRI dashboard;
- incident records;
- change/revalidation records;
- training/competence records;
- audit findings and remediation;
- agent action/provenance logs.

Reuse is permitted only when the evidence actually satisfies the target source's purpose and scope.

## Copyright control

For copyrighted standards such as ISO/IEC 42001, use independently authored descriptions, high-level relationship labels and repository-authorised references. Do not reproduce protected clause text merely to make the crosswalk look complete.

## Stage-1 completion criterion

Stage 1 is complete when the source families, hierarchy, relationship taxonomy, row schema, evidence model, anti-equivalence tests and copyright boundary are controlled and ready for substantive mapping work at the next eligible stage.