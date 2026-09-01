# Manual 54 — AI Model Risk & Independent Validation Baseline

**Canonical stage:** 1 — authoritative-source baseline and validation-control architecture  
**Currentness baseline:** 1 September 2026

This stage establishes the controlled architecture for independent AI model-risk review without representing any single banking, regulatory, or assurance regime as universally applicable.

## Validation domains

1. model/use-case inventory and materiality;
2. intended purpose, assumptions and limitations;
3. data provenance, quality and representativeness;
4. methodology and design rationale;
5. performance and acceptance criteria;
6. robustness, stress and sensitivity testing;
7. security/adversarial testing where applicable;
8. fairness/bias evaluation where relevant;
9. GenAI factuality, groundedness and hallucination evaluation;
10. RAG retrieval quality, source integrity and authorization;
11. agentic action-risk, permissions and containment testing;
12. human-oversight effectiveness;
13. explainability/interpretability appropriate to use and audience;
14. third-party/model-provider dependency validation;
15. implementation verification and configuration controls;
16. findings severity, remediation and exceptions;
17. conditional approval/restriction/suspension criteria;
18. monitoring thresholds and drift detection;
19. material-change triggers and revalidation;
20. independent challenge, evidence retention and governance reporting.

## Independence criteria

Validation must have sufficient organizational and technical independence from model development/operation to provide credible challenge. Record validator competence, conflicts, scope, evidence access, limitations, unresolved disagreements and final disposition authority.

Independence does not require isolation from subject-matter experts; it requires that challenge, findings and conclusions cannot be overridden informally by the development team.

## Materiality and tiering

Use materiality to scale validation depth. Factors include decision impact, affected population, financial/operational consequence, safety/security impact, autonomy, external exposure, sensitive data, legal/regulatory relevance, model novelty, provider opacity and reversibility.

## GenAI/RAG evaluation architecture

Evaluation should separate at least: prompt/task performance; factuality/groundedness; harmful or policy-violating outputs; retrieval relevance; citation/source fidelity; stale-source behavior; sensitive-data leakage; jailbreak/prompt injection; tool-use behavior; refusal/abstention; and monitoring detectability.

## Agentic validation architecture

For agents, validate identity, permissions, tool scope, action classes, approval checkpoints, delegation, memory/state, cross-agent trust, external side effects, kill/containment paths, audit trail and reauthorization after material change.

## Findings and disposition

Every validation finding should record severity, affected objective, evidence, risk rationale, owner, due date, compensating control if any, retest result and disposition. Allowed outcomes should include approve, approve with conditions, restrict, remediate before use, suspend or reject.

## Stage-1 completion criterion

Stage 1 is complete when the validation domains, independence criteria, materiality model, GenAI/RAG/agentic evaluation architecture, findings model and revalidation triggers are explicit enough to support detailed source verification and evidence-catalog construction at the next stage.
