# Manual 53 — Jurisdiction Scenarios and Privacy Evidence Workbook

**Controlled stage:** 3 — jurisdiction/source mapping, scenarios, and evidence construction

## Evidence register

| ID | Evidence | Minimum content |
|---|---|---|
| PD-E01 | AI data inventory | dataset/source, purpose, owner, sensitivity, jurisdiction, model/use case |
| PD-E02 | Data provenance and lineage | source, rights/authorization, transformations, training/RAG use, downstream outputs |
| PD-E03 | Lawful/authorized-use assessment | legal/contractual basis, purpose compatibility, restrictions, accountable reviewer |
| PD-E04 | DPIA / AI impact assessment | affected people, risks, mitigations, residual risk, approval |
| PD-E05 | Sensitive-data control record | categories, access, minimization, masking, retention, monitoring |
| PD-E06 | RAG/vector governance record | corpus sources, embeddings, access boundaries, deletion propagation, retrieval logging |
| PD-E07 | Rights-response evidence | access, correction, deletion, objection/appeal support and model/RAG implications |
| PD-E08 | Cross-border transfer assessment | origin, destination, mechanism, safeguards, provider chain |
| PD-E09 | Third-party data assessment | provider, role, purpose, subprocessors, retention, training use, incident duties |
| PD-E10 | Retention/deletion verification | retention rule, deletion event, replicas/vector stores/logs, verification |
| PD-E11 | Privacy incident record | affected data/people/systems, containment, notification analysis, remediation |
| PD-E12 | Change/revalidation record | new data/source/purpose/model/provider/jurisdiction and resulting reassessment |

## Jurisdiction mapping rule

Every jurisdiction/source row must preserve its own legal scope, definitions, rights, lawful-processing rules, transfer requirements, notice/consent obligations, regulator guidance, and enforcement status. Shared enterprise controls may support multiple laws but do not make those laws equivalent.

## Scenario pack

### Scenario 1 — Global GenAI assistant with internal RAG
Track document provenance, employee/customer data sensitivity, access boundaries, embedding/vector retention, provider training-use restrictions, cross-border hosting, deletion propagation, and retrieval logs. Separate enterprise governance evidence from jurisdiction-specific privacy obligations.

### Scenario 2 — Model trained on historical customer data
Validate original collection purpose, rights/authorization, minimization, sensitive-data handling, retention, representativeness, de-identification claims, and downstream model risks. Record whether retraining or deletion is technically required after rights requests or source withdrawal.

### Scenario 3 — AI-supported employment decision
Combine AI impact assessment with privacy/employment-law analysis, data minimization, sensitive/inferred attributes, human review, explanation/appeal support, retention, and vendor accountability.

### Scenario 4 — External foundation-model provider
Document controller/processor or analogous role analysis where applicable, provider use of prompts/outputs, subprocessors, hosting locations, retention, security, incident obligations, model-improvement settings, and exit/deletion requirements.

### Scenario 5 — New jurisdiction added after deployment
Trigger applicability review, transfer assessment, notices/rights analysis, local retention rules, provider-location review, and reapproval before broadening use where required.

## Stage completion criterion

Stage 3 is complete when the control architecture has jurisdiction-qualified source rows, practical privacy/data scenarios, evidence classes, RAG/vector governance requirements, rights-support mechanics, cross-border analysis, and change triggers sufficient for release-depth training and localization preparation.