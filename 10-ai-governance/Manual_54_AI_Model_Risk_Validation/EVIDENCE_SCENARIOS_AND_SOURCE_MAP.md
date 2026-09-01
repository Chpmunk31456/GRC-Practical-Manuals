# Manual 54 — Evidence, Source Mapping, and Validation Scenarios

**Controlled stage:** 2 — source-qualified validation architecture and evidence construction

## Source-status discipline

Model-risk guidance, supervisory expectations, NIST AI RMF material, internal validation practices, and domain-specific legal obligations must retain their actual status. No supervisory guidance is represented as universally binding outside its scope, and no internal validation framework is represented as certification.

## Validation evidence catalogue

| ID | Evidence | Minimum content |
|---|---|---|
| MR-E01 | Model/use-case inventory | owner, purpose, model/provider, deployment, geography, materiality |
| MR-E02 | Development/design documentation | assumptions, architecture, objectives, limitations, dependencies |
| MR-E03 | Data validation package | provenance, quality, representativeness, leakage, sensitivity, lineage |
| MR-E04 | Performance validation | metrics, benchmarks, thresholds, confidence, limitations |
| MR-E05 | Robustness/security testing | stress, adversarial, misuse, prompt injection, agent/tool abuse where relevant |
| MR-E06 | Fairness/impact assessment | affected groups, metrics, limitations, remediation where relevant |
| MR-E07 | GenAI factuality/groundedness evaluation | hallucination, citation, retrieval support, refusal behavior, uncertainty |
| MR-E08 | RAG validation | corpus quality, retrieval relevance, access boundaries, poisoning, freshness |
| MR-E09 | Agentic action-risk validation | identity, permissions, tool use, action boundaries, approvals, containment |
| MR-E10 | Human-oversight validation | authority, information, intervention, escalation, automation-bias controls |
| MR-E11 | Third-party dependency review | provider, model change, data use, availability, security, exit |
| MR-E12 | Independent validation report | scope, methods, independence, findings, severity, limitations, disposition |
| MR-E13 | Conditional approval record | conditions, residual risk, owner, expiration/review date |
| MR-E14 | Monitoring and revalidation record | drift, incidents, changes, thresholds, trigger, outcome |

## Independence criteria

Independent validation should be organizationally and intellectually separate enough from development and business ownership to provide credible challenge. Record validator role, reporting line, conflicts, prior design involvement, scope limitations, and any compensating review.

## Materiality factors

Consider decision impact, affected population, legal/regulatory exposure, financial exposure, safety, autonomy, access to tools/data, model opacity, third-party dependency, change frequency, data sensitivity, and difficulty of human correction.

## Scenario pack

### Scenario 1 — Third-party foundation model in a regulated workflow
Validate provider dependency, data use, model limitations, performance, security, explainability limits, human oversight, monitoring, and provider-change triggers. The validation conclusion must distinguish the enterprise implementation from claims about the provider’s underlying model.

### Scenario 2 — RAG assistant for internal policy advice
Validate source completeness, retrieval quality, access control, stale content, conflicting sources, groundedness, citation behavior, and escalation when the corpus cannot support an answer.

### Scenario 3 — Agentic AI with transactional authority
Validate service identity, delegated authority, tool permissions, action boundaries, value thresholds, human approval checkpoints, rollback, provenance, kill switch, and cross-agent delegation.

### Scenario 4 — High-impact classification model
Validate data representativeness, performance by relevant subgroup, threshold selection, stability, override procedures, error consequences, monitoring, and revalidation after population or data changes.

### Scenario 5 — Material provider model update
Treat a provider change as a validation trigger when performance, behavior, safety, security, context length, tools, training data, or policy behavior may materially change. Re-run targeted tests and issue a new disposition where warranted.

## Findings and disposition

Classify findings by severity and decision impact. Permitted dispositions include approve, approve with conditions, restrict, remediate before deployment, suspend, or reject. Every conditional approval must identify owner, condition, due date, residual risk, and revalidation trigger.

## Stage completion criterion

Stage 2 is complete when source-status rules, evidence classes, independence criteria, materiality factors, validation domains, GenAI/RAG/agentic scenarios, findings, and disposition rules are sufficiently explicit to build detailed training modules and localization-ready implementation guidance.