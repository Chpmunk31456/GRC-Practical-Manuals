# Manual 54 — Source-to-Validation Mapping

**Controlled stage:** 2 — verified source/control mapping, evidence architecture, and scenario construction  
**Date:** 1 September 2026

## Purpose

Translate the Manual 54 validation-control baseline into a repeatable independent-validation program for predictive AI, generative AI, RAG systems, and agentic AI. Source relationships are used as supporting guidance; they do not convert voluntary frameworks or sector guidance into universal legal obligations.

## Validation domains

### MRM-01 — Use-case and materiality classification
Validate business purpose, affected stakeholders, decision consequence, autonomy, data sensitivity, financial/operational impact, regulatory exposure, and reversibility. Evidence: use-case inventory, materiality score, owner, approval tier, and escalation path.

### MRM-02 — Model and system inventory
Validate model/provider/version, orchestration, prompts, retrieval stores, tools, agents, data pipelines, hosting, and dependencies. Evidence: inventory record, architecture diagram, dependency register, and version history.

### MRM-03 — Assumptions and limitations
Identify explicit and implicit assumptions, supported operating ranges, known failure modes, prohibited uses, uncertainty, and reliance on third-party claims. Evidence: limitation register and validation challenge record.

### MRM-04 — Data validation
Assess provenance, lineage, representativeness, quality, leakage, duplication, contamination, label integrity, temporal relevance, sensitive-data handling, and train/test separation where applicable.

### MRM-05 — Methodology and implementation
Assess whether the selected methodology is appropriate for the use case and whether implementation matches the approved design. Evidence: technical specification, code/configuration review, reproducibility record, and independent challenge.

### MRM-06 — Performance and robustness
Test accuracy or task performance using fit-for-purpose metrics, stress cases, distribution shift, edge cases, uncertainty, stability, and failure thresholds.

### MRM-07 — Security and adversarial resilience
Challenge prompt injection, data poisoning, model/provider changes, unsafe output execution, tool abuse, privilege escalation, exfiltration, supply-chain integrity, and containment capability where relevant.

### MRM-08 — Fairness and harmful-bias evaluation
Where relevant to context and applicable requirements, evaluate subgroup performance, disparate impact indicators, proxy effects, data imbalance, and mitigation effectiveness. Document when fairness testing is not applicable and why.

### MRM-09 — Explainability and decision traceability
Validate that explanations, rationale traces, feature or evidence attribution, provenance, and decision records are suitable for the use case and stakeholder need. Do not claim explanation methods reveal internal truth beyond their actual capability.

### MRM-10 — GenAI factuality, groundedness, and hallucination risk
Define task-specific factuality and groundedness tests, reference-source expectations, citation/provenance checks, unsupported-claim thresholds, abstention behavior, and escalation rules.

### MRM-11 — RAG retrieval quality and authorization
Validate source eligibility, retrieval relevance, freshness, access control, chunking/indexing behavior, poisoning resistance, citation fidelity, and unauthorized retrieval prevention.

### MRM-12 — Agentic action risk
Validate agent identity, delegated authority, tool permissions, action boundaries, human approval thresholds, cross-agent delegation, transaction limits, rollback, containment, and attributable logs.

### MRM-13 — Human oversight effectiveness
Test whether assigned reviewers can understand, intervene, override, stop, escalate, and document decisions at the point where human oversight is claimed as a control.

### MRM-14 — Third-party dependency validation
Challenge provider claims, model cards, security statements, change notices, contractual evidence, service continuity, exit options, and independent evidence availability.

### MRM-15 — Monitoring and revalidation
Define metrics, drift/change thresholds, incidents, provider/model/data/tool changes, performance degradation, control failures, and time-based triggers requiring revalidation.

### MRM-16 — Findings and disposition
Classify findings by severity and materiality. Track remediation, compensating controls, accepted residual risk, conditional approval, use restrictions, expiration dates, and closure evidence.

## Independence criteria

Independent validation should be organizationally and intellectually separate from primary model/system development to a degree proportionate to materiality. The validator must be able to challenge assumptions, reproduce or independently test claims, document dissent, escalate unresolved findings, and avoid validating their own substantive design decisions without compensating governance.

## Evidence catalogue

- EV-01 validation charter and scope
- EV-02 use-case/materiality assessment
- EV-03 model/system inventory
- EV-04 architecture and data-flow diagrams
- EV-05 assumptions/limitations register
- EV-06 data-quality/provenance tests
- EV-07 reproducible performance results
- EV-08 robustness/stress tests
- EV-09 adversarial/security test results
- EV-10 fairness assessment where applicable
- EV-11 GenAI factuality/groundedness evaluation
- EV-12 RAG retrieval/authorization evaluation
- EV-13 agentic action-boundary tests
- EV-14 human-oversight effectiveness test
- EV-15 third-party evidence challenge
- EV-16 findings/remediation register
- EV-17 conditional approval or residual-risk record
- EV-18 monitoring and revalidation plan

## Required scenarios

1. Model performance deteriorates after an upstream data-distribution change.
2. A provider silently changes a hosted model version and behavior shifts.
3. A GenAI assistant produces fluent but unsupported factual claims in a consequential workflow.
4. A RAG system retrieves authoritative-looking but unauthorized or stale content.
5. An agent attempts an action outside its approved transaction boundary.
6. Human oversight exists on paper but reviewers cannot practically intervene before consequence.
7. Evaluation data has leaked into training or tuning, inflating apparent performance.
8. A third-party model claim cannot be independently reproduced.
9. A security finding remains open but the business requests conditional production approval.
10. Monitoring detects drift that does not yet breach a hard threshold but changes residual risk materially.

## Stage-2 completion criterion

Stage 2 is complete when each validation domain has a source-qualified relationship, evidence expectation, challenge method, scenario coverage, finding/disposition rule, and revalidation trigger sufficient to build the controlled training architecture and later localization/candidate package.