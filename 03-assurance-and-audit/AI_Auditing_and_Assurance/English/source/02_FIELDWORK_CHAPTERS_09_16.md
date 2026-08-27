# Manual 05 — AI Auditing and Assurance
## Controlled English Source — Chapters 09–16

> Original audit implementation guidance. This material does not reproduce proprietary standard or AAIA content and does not itself constitute an audit opinion.

## Chapter 09 — Governance and risk audit procedures

Auditors should test whether AI governance operates beyond policy language. Procedures should verify accountable ownership, risk classification, approval authority, escalation, exception handling, and periodic review for sampled systems.

Evidence may include inventories, risk records, committee decisions, release approvals, monitoring reports, and change records.

## Chapter 10 — AI operations audit procedures

Operational testing should evaluate deployment, monitoring, incident handling, access, change control, fallback, and retirement processes. The auditor should trace selected systems from approved design through current production state to determine whether the deployed configuration matches the evidence supporting release.

## Chapter 11 — Data governance audit procedures

Data-related testing should address provenance, classification, permitted use, access, retention, transformation, quality controls, privacy restrictions, and deletion where applicable.

Where AI systems depend on retrieval or vector stores, the auditor should test how content is admitted, updated, removed, and protected from unauthorized access or manipulation.

## Chapter 12 — Model and system testing

Audit testing should distinguish management’s own evaluation from independent audit procedures. The audit team may inspect test design, reproduce selected tests, challenge assumptions, perform targeted technical procedures, or engage specialists.

Testing should be linked to defined criteria and risks rather than performed only because a tool is available.

## Chapter 13 — Human oversight and decision controls

Auditors should determine whether required human review is actually possible and evidenced. Procedures may examine reviewer competency, available context, escalation authority, time pressure, override records, approval logs, and whether repeated overrides indicate control weakness.

## Chapter 14 — Third-party and component assurance

Supplier assurance should evaluate the evidence relied upon for external models, hosting, APIs, datasets, tools, and other material components. Auditor procedures should consider contract terms, independent reports, security evidence, change notifications, incident history, data practices, and concentration or exit risk.

A completed questionnaire should not be treated as equivalent to independently supported assurance.

## Chapter 15 — Technical audit tools and automation

Automated tools can support inventory analysis, configuration checks, log review, test execution, sampling, evidence correlation, and anomaly detection. Tool output remains audit evidence that must be understood, validated, and interpreted.

Auditors should document tool version, configuration, input population, limitations, and how exceptions were investigated.

## Chapter 16 — Workpaper discipline

Each significant conclusion should be traceable to the criterion, procedure, evidence, result, preparer, and reviewer. Workpapers should distinguish observed facts, management representations, auditor analysis, assumptions, and unresolved limitations.

Material reviewer comments must be resolved or explicitly carried into the report before the audit is closed.