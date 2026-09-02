# Manual 54 — Training Architecture and Revalidation Program

**Controlled stage:** 3 — release-depth training, validation execution, findings and revalidation
**Date:** 1 September 2026

## Operating cycle

1. classify use case and materiality;
2. define independent validation scope and independence safeguards;
3. freeze model/system/data/provider versions under test;
4. challenge assumptions, data, methodology, performance and controls;
5. execute GenAI, RAG, agentic, security and human-oversight tests where applicable;
6. record findings, severity, evidence and management response;
7. approve, conditionally approve, restrict or reject use;
8. establish monitoring and explicit revalidation triggers;
9. preserve reproducible validation evidence and dissent.

## Required training scenarios

- silent hosted-model version change;
- data drift that changes residual risk before a hard performance threshold is breached;
- inflated evaluation from train/test leakage;
- unsupported GenAI factual output in a consequential workflow;
- RAG retrieval of stale or unauthorized content;
- agent action beyond delegated authority;
- nominal human review that cannot practically stop the action;
- unresolved red-team finding with business request for conditional approval;
- third-party performance/security claim that cannot be independently reproduced;
- post-incident revalidation after containment and configuration rollback.

## Finding/disposition matrix

Every finding records severity, affected use case, evidence, owner, remediation, compensating control, residual risk, due date, approval authority, use restriction and closure evidence. Conditional approval must expire or trigger re-review; it is not permanent acceptance by default.

## Revalidation triggers

Revalidation is required when materiality changes or when there is a significant model/provider/version, data, prompt/system instruction, retrieval corpus, tool/permission, orchestration, hosting, security, monitoring, incident, regulatory or business-purpose change. Time-based revalidation supplements rather than replaces event-driven triggers.

## Independence test

The validator must be able to challenge the development team, reproduce or independently test claims, document dissent, escalate unresolved material findings and avoid self-validating substantive design decisions without compensating governance.

## Stage-3 completion criterion

Stage 3 is complete when the validation domains, execution sequence, scenario pack, finding/disposition mechanics, independence safeguards, monitoring and revalidation triggers are sufficient to construct controlled trilingual release sources and deterministic candidate tooling.