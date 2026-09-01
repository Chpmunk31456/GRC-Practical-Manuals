# Manual 50 — Evidence Harmonization Workbook

**Canonical stage:** 4 — release-depth mapping and training construction  
**Currentness baseline:** 1 September 2026

This workbook operationalises reuse of governance evidence across distinct AI regimes without claiming that shared evidence makes those regimes equivalent.

## 1. Evidence reuse rule

An evidence item may be reused only when all of the following are recorded:

1. the enterprise control objective it demonstrates;
2. the exact system/use-case scope;
3. the source/regime relationship type;
4. the sufficiency of the evidence for that source;
5. known limitations or missing source-specific evidence;
6. the accountable owner and evidence date/version.

Reuse reduces duplication. It does not erase legal actor definitions, jurisdiction, certification, conformity, assurance methodology, or source-specific documentation requirements.

## 2. Relationship taxonomy

| Relationship | Meaning | Permitted conclusion |
|---|---|---|
| Direct | The source materially addresses the same control objective at the relevant level. | Evidence may be strongly reusable if scope and sufficiency are confirmed. |
| Partial | Only part of the common objective is covered. | Reuse requires additional source-specific evidence. |
| Supporting | The control helps enable the source objective but is not itself sufficient. | Evidence is supporting only. |
| Contextual | The source informs governance intent or principles but does not impose the same control requirement. | Use for rationale, not compliance proof. |
| None / N/A | No defensible relationship for the assessed scope. | Do not force a mapping. |

## 3. Core evidence register

| Evidence ID | Evidence class | Common controls | Typical owner | Minimum metadata |
|---|---|---|---|---|
| EV-01 | AI inventory record | GC-02, GC-03, GC-11 | AI governance / system owner | system, owner, purpose, model/provider, lifecycle, geography, risk tier, version |
| EV-02 | Governance charter / RACI | GC-01, GC-03 | governance lead | decision rights, accountable roles, escalation, exceptions, review cadence |
| EV-03 | Risk / impact assessment | GC-04, GC-05 | risk owner | purpose, affected parties, harms, misuse, controls, residual risk, decision |
| EV-04 | Data / RAG lineage record | GC-06, GC-11 | data owner | sources, provenance, rights, sensitivity, retention, quality, access |
| EV-05 | Security architecture | GC-07, GC-13, GC-20 | security architect | trust boundaries, identities, permissions, tools, logging, containment |
| EV-06 | Transparency / communication artifact | GC-08 | product/legal/comms | audience, disclosure, limitations, responsibilities, date/version |
| EV-07 | Human oversight design | GC-09 | process owner | intervention points, authority, competence, override, escalation, logs |
| EV-08 | TEVV / validation package | GC-10, GC-17 | validation / assurance | claims, datasets, tests, thresholds, results, limitations, reviewer |
| EV-09 | Deployment approval | GC-12 | accountable approver | decision, conditions, residual risk, expiry/review date |
| EV-10 | Third-party assessment | GC-13 | procurement/vendor risk | provider, model/service, data, security, change notice, incidents, exit |
| EV-11 | Monitoring dashboard / report | GC-14 | operations | KPIs/KRIs, drift, denials, incidents, complaints, provider changes |
| EV-12 | Incident record | GC-15 | incident owner | detection, containment, impact, evidence, root cause, reporting, remediation |
| EV-13 | Change / revalidation record | GC-16 | change owner | trigger, materiality, retest, reassessment, decision, version |
| EV-14 | Audit / independent review | GC-17 | assurance/audit | scope, independence, criteria, findings, remediation, closure |
| EV-15 | Competence / training record | GC-18 | HR/governance | role, curriculum, completion, assessment, refresh date |
| EV-16 | Improvement backlog | GC-19 | governance owner | source of finding, action, owner, priority, due date, closure evidence |
| EV-17 | Agent action provenance | GC-20 | platform/security | agent identity, user/context, tool call, parameters, decision, result, timestamp |

## 4. Source-sufficiency worksheet

For each evidence item, complete one row per source family.

| Evidence ID | Source | Relationship | Sufficient as-is? | Limitations | Additional evidence required | Reviewer/owner |
|---|---|---|---|---|---|---|
| EV-03 | EU AI Act | partial/direct depending on system/actor | No default | legal scope and role are source-specific | actor analysis, applicable legal assessment, any required source-specific process/evidence | |
| EV-03 | ISO/IEC 42001 | direct/supporting at management-system level | Depends | certification audit criteria remain separate | management-system context and controlled documented information | |
| EV-03 | NIST AI RMF / AI 600-1 | direct/supporting | Often reusable | profile actions and measurement depth vary | source-specific profile/action evidence where needed | |
| EV-03 | Singapore governance | direct/supporting | Often reusable | assurance/testing expectations may need separate evidence | testing/assurance records as applicable | |
| EV-03 | OECD principles | contextual/direct objective | Yes for governance rationale, not legal compliance | principles are not a certification regime | usually none beyond rationale and operational evidence | |

Repeat for EV-01 through EV-17.

## 5. Gap classification

Every gap must be classified as exactly one primary type, with optional secondary tags:

- **control gap** — required capability is absent;
- **evidence gap** — control may exist but evidence is inadequate;
- **scope/role gap** — applicability or actor responsibility is unresolved;
- **legal interpretation gap** — specialist interpretation is needed;
- **process gap** — required workflow or decision path is incomplete;
- **assurance gap** — independent testing/audit/conformity evidence is absent;
- **competence gap** — accountable personnel lack demonstrated competence;
- **currentness gap** — source/version or system-change reconciliation is stale.

## 6. Materiality and remediation

Use three remediation priorities:

- **P1 — release blocker:** unresolved issue could materially invalidate deployment, legal position, security/safety, or assurance claim.
- **P2 — controlled remediation:** material weakness exists but can be managed under explicit conditions and deadline.
- **P3 — improvement:** non-material enhancement with no current release blocker.

Each remediation record must include owner, due date, compensating control if any, retest requirement, and closure evidence.

## 7. Evidence reuse examples

### Example A — one AI inventory, several regimes

EV-01 can be a common source of truth for system identity, owner, purpose, provider, geography and lifecycle. The same record may support NIST GOVERN/MAP, Singapore governance, ISO management-system context, and EU compliance operations. It does not by itself establish EU legal classification, satisfy ISO certification, or prove any source-specific filing or conformity requirement.

### Example B — shared TEVV package

EV-08 can carry common performance, robustness, security, privacy and control-effectiveness tests. The package must still state which claims each test validates and which source-specific assurance or conformity conclusions are not supported.

### Example C — agent provenance

EV-17 can support accountability, monitoring, incident investigation, security, and change analysis across several frameworks. It should record both successful and denied actions; otherwise the evidence may hide policy-enforcement failures.

## 8. Executive reporting model

Do not produce one universal compliance percentage. Report instead:

1. common-control implementation coverage;
2. evidence sufficiency by source;
3. open P1/P2/P3 gaps;
4. unresolved scope/legal interpretation items;
5. assurance/certification/conformity status separately;
6. currentness date and material changes since last review.

## 9. Release-depth completion criterion

This workbook is release-depth ready when each GC-01 through GC-20 control has at least one mapped evidence class, explicit reuse limitations, a source-sufficiency decision path, and a gap/remediation method that prevents false-equivalence conclusions.
