# Manual 04 — NIST AI 600-1 Generative AI Profile Implementation
## Controlled English Source — Chapters 25–32

> Original implementation guidance. The chapter set supports ongoing GAI risk management and does not reproduce NIST publication text.

## Chapter 25 — Deployment and release controls

Deployment should use a controlled release record tied to the tested artifact, configuration, model version, data/retrieval state, tools, guardrails, and approved operating conditions. Material deviation between the tested candidate and deployed system invalidates the release evidence until assessed.

Release records should identify accountable approvers, open exceptions, monitoring thresholds, rollback authority, and review dates.

## Chapter 26 — Monitoring and operating thresholds

Monitoring should be tied to known risks and decision thresholds rather than generic telemetry. Relevant measures may include harmful-output rates, unsupported-answer rates, security events, data leakage signals, user complaints, tool failures, model drift indicators, latency/availability, supplier changes, and exception volume.

Threshold breaches should map to predefined actions: investigate, restrict, increase human review, disable a function, roll back, or stop the system.

## Chapter 27 — Change management and reassessment

Changes to models, prompts, system instructions, retrieval sources, tools, permissions, data handling, suppliers, guardrails, interfaces, or business use can alter risk. Change records should classify materiality and identify which prior evidence remains valid.

Material changes reopen the affected risk, test, security, privacy, accessibility, human-review, and release gates. Emergency changes require retrospective review and evidence completion within a defined period.

## Chapter 28 — Incident response and containment

GAI incident response should integrate with enterprise incident management while preserving AI-specific evidence. Teams should capture prompts, outputs, model/configuration identifiers, retrieval context, tool calls, identities, timestamps, logs, affected records, supplier notices, and control state where lawful and feasible.

Containment options can include disabling tools, reducing permissions, isolating retrieval sources, reverting configuration, limiting users, increasing human review, or suspending the service.

## Chapter 29 — Corrective action and remediation validation

Corrective action should address root causes rather than only suppressing the observed output. Remediation records should identify the finding, cause, owner, planned action, due date, validation method, evidence, residual risk, and closure decision.

A fix should not be considered closed solely because one test case now passes. Retesting should assess likely variants and regression risk.

## Chapter 30 — Periodic review and management reporting

Periodic review should evaluate whether the use case remains appropriate, controls remain effective, risk assumptions remain valid, evidence is current, suppliers or components have changed, and operating results remain within tolerance.

Management reporting should distinguish facts, trends, assumptions, unresolved risks, accepted exceptions, and decisions required. High-risk issues should be visible to the accountable risk owner rather than buried in technical reporting.

## Chapter 31 — Retirement, data disposition, and exit

Retirement planning should address model endpoints, credentials, prompts, retrieval indexes, vector stores, logs, user data, caches, integrations, vendor access, retained evidence, and contractual obligations.

The organization should verify data return or deletion where required, revoke access and secrets, disable integrations, preserve required records, document unresolved obligations, and record the retirement decision.

## Chapter 32 — Assurance, limitations, and final release boundary

Assurance is cumulative and scope-specific. Repository QA, automated testing, red teaming, documentation, or a completed checklist does not guarantee that a GAI system is safe, secure, compliant, accurate, fair, or fit for every context.

Before publication of this manual itself, the controlled package must complete source verification, technical/editorial review, `es-419` and `pt-BR` semantic review, graphics/accessibility verification, DOCX/PDF generation, page-level QA, provenance and checksums, repository/security review, and explicit Final Human Release Approval.

Any material content change after human approval reopens the affected review gate.