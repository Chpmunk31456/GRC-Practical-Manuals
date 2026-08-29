# Manual 07 — AI Security and Lifecycle Controls
## Controlled English Source — Chapters 25–32

> Original defensive security implementation guidance. This material does not guarantee security or replace organization-specific review.

## Chapter 25 — Supplier and dependency change

Supplier or dependency changes should be assessed for security effect before adoption. Relevant changes include hosting, model version, service architecture, data processing, subprocessors, access methods, logging, safety controls, and contractual notification commitments.

## Chapter 26 — Resilience and degraded operation

Security planning should consider how the system behaves when models, APIs, retrieval, monitoring, or external services are degraded or unavailable. Fallback modes should not silently bypass security, approval, or data-protection controls.

## Chapter 27 — Backup and recovery considerations

Recovery planning should identify what configurations, prompts, policies, indexes, credentials, evidence, and dependencies are needed to restore a known controlled state. Recovery procedures should be validated proportionate to criticality.

## Chapter 28 — Decommissioning

Retirement should revoke identities, credentials, and integrations; disable endpoints; remove or archive data according to requirements; preserve required evidence; close supplier access; and document unresolved obligations.

## Chapter 29 — Security metrics and management reporting

Metrics should be linked to decisions. Useful reporting can include material findings, exceptions, reassessment status, incident trends, dependency changes, validation coverage, overdue remediation, and control-health indicators.

## Chapter 30 — Security assurance limitations

No automated test suite, control checklist, security review, or repository workflow can establish that an AI system is free from weaknesses. Assurance statements should identify the scope, time period, evidence, and limitations supporting them.

## Chapter 31 — Continuous improvement

Lessons from incidents, near misses, testing, supplier changes, user feedback, and control failures should feed back into threat models, validation plans, operating controls, and training.

## Chapter 32 — Manual release boundary

Before this manual is published, source verification, the complete controlled English master, technical/security review, `es-419` and `pt-BR` semantic review, graphics/accessibility review, document and page QA, provenance, repository/security release audit, and Final Human Release Approval must be complete.

Material content changes after human approval reopen the affected gates.