# Manual 53 — AI Privacy & Data Governance Source/Control Architecture

**Canonical stage:** 2 — jurisdiction/source matrix and detailed control architecture  
**Currentness baseline:** 1 September 2026

This stage converts the initial privacy/data-governance scope into a controlled source-to-control architecture. It preserves jurisdictional differences and does not treat one privacy framework as a substitute for another.

## Control domains

1. lawful/authorized data use and purpose limitation;
2. data inventory, provenance, lineage and ownership;
3. minimisation and collection limitation;
4. sensitive/special-category data handling;
5. data quality and representativeness;
6. training-data governance;
7. RAG/vector-store boundary controls;
8. retrieval authorization and tenant isolation;
9. retention and deletion;
10. cross-border transfer controls;
11. data-subject/individual rights support where applicable;
12. privacy notices and transparency;
13. DPIA/privacy impact assessment integration;
14. AI-specific impact/risk assessment integration;
15. de-identification, pseudonymisation and re-identification risk;
16. logging and privacy-preserving observability;
17. third-party/model-provider data governance;
18. incident/breach handling and evidence preservation;
19. change management and re-assessment;
20. assurance, audit and management reporting.

## Jurisdiction/source matrix rule

For every detailed mapping row, record: source/regime; legal or guidance status; territorial/organizational applicability; controller/processor/provider/deployer or equivalent actor; data category; trigger; required action; evidence; retention; exception/derogation; and unresolved legal interpretation.

A common enterprise control may support several regimes, but source-specific legal bases, rights, timelines, thresholds and transfer mechanisms remain distinct.

## AI data-flow model

Each governed use case should trace data through: source → ingestion → preprocessing → training/fine-tuning → model/provider boundary → prompt/context → RAG/vector store → tools/APIs → output → logs/telemetry → retention/deletion.

For each boundary record owner, purpose, data class, authorization, encryption/protection, residency/transfer, retention, monitoring, and change trigger.

## Impact-assessment integration

Privacy/DPIA analysis and broader AI risk/impact assessment may share evidence but must retain separate decision criteria where source obligations differ. Shared evidence can include data-flow diagrams, stakeholder/affected-party analysis, necessity/proportionality rationale, risk register, control design, residual risk, approval and re-assessment triggers.

## RAG and vector controls

Minimum control design includes corpus authorization, document provenance, tenant/role filtering, embedding/vector-store access control, retrieval policy, prompt-injection/data-exfiltration defenses, retention/deletion propagation, stale-source handling, sensitive-data filters and auditability of retrieved context.

## Evidence model

Representative evidence classes: data inventory, RoPA/equivalent processing record, data-flow diagram, DPIA/PIA, AI impact assessment, transfer assessment, vendor DPA/contract, consent/legal-basis record where applicable, retention schedule, deletion evidence, access-control review, data-quality test, red-team privacy test, incident record, change approval and audit finding.

## Stage-2 completion criterion

Stage 2 is complete when the jurisdiction/source dimensions, detailed control domains, AI data-flow model, assessment integration, RAG/data-boundary controls and evidence classes are defined well enough to begin scenario and release-depth training construction without collapsing jurisdiction-specific obligations into generic privacy claims.
