# Mapping Governance and Intended Use

## 1. Why mapping requires governance

A control mapping is a documented analytical relationship between two or more requirements, outcomes, control objectives, practices, safeguards, or evidence expectations. It can support program design, scoping, reuse, gap analysis, reporting, and audit preparation. It cannot replace the authoritative source or prove that any requirement is satisfied.

Weak mappings create false confidence. They may collapse distinct obligations, ignore scope conditions, conceal partial coverage, or imply that one implementation satisfies every mapped requirement. A governed mapping process therefore treats each relationship as a reviewable assertion supported by rationale and evidence.

## 2. Define the intended use before mapping

Every mapping set must state its intended use. Common uses include:

- designing a common control framework;
- identifying reusable implementations;
- preparing an audit or assessment scope;
- translating executive outcomes into control activities;
- identifying gaps or duplicated effort;
- supporting product, supplier, or business-unit reporting;
- planning migration between framework versions;
- connecting requirements to evidence and ownership.

The intended use determines the required precision. A high-level executive comparison may map categories or outcomes. An audit-support mapping requires requirement-level decomposition, scope conditions, implementation references, evidence expectations, and independent review.

## 3. Establish mapping authority

The mapping owner is accountable for methodology, source integrity, reviewer assignment, approval, maintenance, and retirement. Subject-matter contributors may propose relationships, but approval should include people who understand both source domains and the actual implementation environment.

Recommended roles include:

- **mapping owner** — governs the mapping set and methodology;
- **source steward** — confirms authoritative versions and licensing constraints;
- **domain reviewer** — validates source meaning and applicability;
- **control owner** — confirms implementation scope and evidence;
- **independent approver** — challenges unsupported equivalence;
- **records custodian** — retains versions, decisions, and review evidence.

## 4. Separate source text from organization interpretation

Maintain distinct fields for:

1. the source identifier;
2. an authorized source excerpt or licensed reference location;
3. the organization's concise interpretation;
4. the normalized control objective;
5. the proposed relationship;
6. the rationale and limitations.

This separation prevents an organization-authored summary from being mistaken for official language. It also allows the interpretation to be corrected without changing the source record.

## 5. Use explicit relationship types

Do not use a single undifferentiated value such as “mapped.” Recommended relationship types are:

- **equivalent** — objectives, scope, and expected result are materially the same;
- **strong overlap** — substantial coverage exists, but one or more conditions differ;
- **partial overlap** — only part of the source objective is covered;
- **supports** — the target contributes to the source objective but is not sufficient alone;
- **related** — the items address a common topic but do not establish coverage;
- **conflicts or constrains** — obligations or implementation expectations require reconciliation;
- **no mapping** — no defensible relationship was identified;
- **not applicable** — applicability was evaluated and excluded with rationale.

“Equivalent” should be rare and must require documented comparison of scope, actor, action, object, condition, frequency, evidence, and outcome.

## 6. Record confidence separately from relationship type

Relationship strength and analyst confidence are different. A proposed partial overlap may have high confidence; a proposed equivalence may have low confidence.

Use a controlled confidence scale such as:

- **high** — authoritative sources and implementation facts support the conclusion, with independent review;
- **medium** — the relationship is reasonable but contains interpretation or unresolved conditions;
- **low** — the relationship is preliminary, indirect, or based on incomplete information.

Low-confidence mappings should not drive compliance claims or control-reuse decisions without further review.

## 7. Preserve scope and applicability

A mapping record should identify relevant scope dimensions, including:

- legal entity and jurisdiction;
- business process and service;
- system, application, infrastructure, or facility;
- data type and sensitivity;
- workforce, supplier, or customer population;
- technology model, including cloud responsibility boundaries;
- assessment period;
- implementation group, profile, baseline, or assurance level;
- contractual and regulatory triggers.

A relationship may be valid in one scope and invalid in another.

## 8. Approval criteria

A mapping should not be approved unless:

- both sources and versions are identified;
- source licensing and reproduction constraints are respected;
- requirements are decomposed to a comparable level;
- scope and applicability are recorded;
- relationship type and confidence are explicit;
- rationale identifies both coverage and limitations;
- implementation and evidence links are distinguished from source relationships;
- conflicts and gaps are visible;
- an independent reviewer has recorded a decision;
- a review trigger and expiration date are assigned.

## 9. Prohibited claims

Do not state that:

- implementation of one framework automatically establishes compliance with another;
- a mapping proves design or operating effectiveness;
- a crosswalk is a legal opinion or certification;
- a high-level category relationship satisfies detailed requirements;
- identical terminology means identical obligation;
- a vendor-provided mapping removes the organization's duty to validate scope and implementation.

## 10. Minimum governance evidence

Retain:

- approved methodology and relationship definitions;
- source register and version history;
- mapping records and rationale;
- reviewer comments and approval decisions;
- conflicts, exceptions, and unresolved gaps;
- change logs and retired mappings;
- evidence of periodic and event-driven review.
