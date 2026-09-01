# Manual 49 — Practical Scenarios

## Scenario 1 — Enterprise GenAI assistant

A company deploys a GenAI assistant over internal policies and customer procedures.

### GOVERN
Assign owner, risk tier, policies, provider oversight and decision rights.

### MAP
Document users, intended purpose, RAG sources, affected data, foreseeable misuse and dependencies.

### MEASURE
Test retrieval relevance, groundedness, hallucination, sensitive-data leakage and unsafe responses.

### MANAGE
Set deployment limits, human escalation, monitoring thresholds, provider-change triggers and incident procedures.

## Scenario 2 — High-impact hiring support

A GenAI system summarises candidate materials and proposes interview priorities.

Learners must identify human-AI configuration risk, overreliance, performance/fairness concerns where relevant, privacy, vendor/data issues and evidence needed for independent challenge. The final decision authority must remain explicit.

## Scenario 3 — RAG poisoning

An internal knowledge base contains a malicious or incorrect document that instructs the model to ignore policy and expose sensitive information.

### Required controls
- controlled ingestion and source provenance;
- content trust classification;
- retrieval/access controls;
- prompt/context isolation;
- adversarial testing;
- source removal/re-indexing;
- incident reconstruction.

## Scenario 4 — Provider silently changes the model

A SaaS vendor changes the underlying model and safety behavior without a customer release process.

Learners define the revalidation trigger, contract/change-notification requirement, regression test set, monitoring and deployment disposition until acceptable evidence exists.

## Scenario 5 — Customer-facing financial explanation

A GenAI system explains financial products but cannot give binding investment advice or approve transactions.

Learners MAP intended/forbidden uses, MEASURE false/confabulated claims and MANAGE escalation, disclosures and monitoring.

## Scenario 6 — Red-team finding

A red team demonstrates that indirect prompt injection can cause the system to exfiltrate content from an internal RAG source.

Learners must record the finding, severity, containment, technical remediation, retest, residual risk decision and conditions for return to service.

## Scenario 7 — Automation bias

Operators accept almost every GenAI recommendation even though policy requires independent judgment.

Learners propose reviewer training, forced independent checks, override/disagreement metrics and investigation thresholds.

## Scenario 8 — Incident after harmful output

A public GenAI service generates dangerous guidance and the incident cannot initially be reproduced because the exact model version and context were not retained.

Learners identify evidence/provenance failures, IR improvements and minimum logging/version-control requirements.

## Scenario 9 — Executive risk decision

A dashboard shows one system with strong benchmark scores but unresolved privacy and provider-change controls. Another has lower accuracy but strong human review and bounded use.

Learners explain why AI risk cannot be reduced to one performance score and produce a documented MANAGE decision.

## Scenario 10 — Cross-framework claim

A manager says: “We follow NIST AI RMF, so we comply with the EU AI Act and are ISO/IEC 42001 certified.”

Learners must reject the claim and create a qualified mapping showing common controls, framework-specific obligations/evidence and different legal/standards status.