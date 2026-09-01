# Manual 49 — NIST AI RMF + GenAI Control Architecture

**Canonical stage:** 2 — controlled architecture  
**Currentness baseline:** 1 September 2026

## Operating model

Manual 49 treats NIST AI RMF as a continuous operating cycle rather than a one-time checklist:

**GOVERN → MAP → MEASURE → MANAGE → feedback into GOVERN/MAP**

The architecture maps every selected AI RMF outcome or NIST AI 600-1 action into:

**NIST outcome/action → organisational interpretation → risk/control objective → control owner → control activity → evidence → test/TEVV method → result/finding → remediation → residual risk**

## GOVERN architecture

### Objectives
- establish accountable AI risk governance;
- define policies, risk tolerance and decision rights;
- integrate legal, security, privacy, safety, model-risk, procurement and business perspectives;
- maintain an AI inventory and lifecycle accountability;
- govern third-party AI and model/provider dependencies;
- define escalation, exception and incident structures.

### Core evidence
- AI governance charter;
- AI policy and standards;
- RACI / decision-rights matrix;
- AI inventory;
- risk-tiering methodology;
- committee minutes and approvals;
- exception/risk-acceptance records;
- vendor/model-provider governance records;
- training and competence records.

## MAP architecture

### Objectives
- establish intended purpose and context;
- identify AI actors and affected parties;
- understand data, model, RAG, tool and external dependencies;
- identify potential benefits, harms, misuse and foreseeable failure modes;
- document deployment environment and human-AI configuration;
- characterize third-party and supply-chain dependencies.

### Core evidence
- use-case description;
- system/context diagram;
- data lineage and RAG source map;
- actor/stakeholder analysis;
- misuse/abuse cases;
- impact assessment;
- dependency inventory;
- assumptions/limitations register.

## MEASURE architecture

### Objectives
- establish measurable acceptance criteria;
- perform testing, evaluation, verification and validation (TEVV);
- evaluate uncertainty and limitations;
- test control effectiveness;
- assess GenAI-specific risks under representative and adversarial conditions;
- preserve reproducibility and test provenance.

### Core evidence
- evaluation/TEVV plan;
- datasets/test sets and provenance;
- test configuration and model/version identity;
- benchmark/task-performance results;
- robustness/security/privacy tests;
- red-team/adversarial results;
- human-factors/overreliance evaluation where relevant;
- reproducibility record;
- findings and remediation.

## MANAGE architecture

### Objectives
- prioritise and treat identified risk;
- decide deploy/restrict/accept/remediate/retire dispositions;
- monitor performance, incidents and changes;
- respond to emerging risk;
- trigger revalidation after material change;
- preserve contingency, rollback and retirement capability.

### Core evidence
- risk treatment plan;
- deployment decision;
- residual-risk acceptance;
- monitoring/KRI dashboard;
- incident records;
- model/provider change log;
- revalidation records;
- rollback/containment plan;
- retirement/decommission record.

## GenAI risk-extension architecture

Manual 49 will treat NIST AI 600-1 as a cross-sectoral companion profile and map its risk/action set into control families. The controlled architecture includes at least:

1. confabulation / false or misleading output;
2. information integrity and content provenance;
3. information-security risk;
4. privacy and sensitive-data risk;
5. harmful bias / representational harms where applicable;
6. human-AI configuration, overreliance and automation effects;
7. intellectual-property and data-provenance concerns;
8. dangerous, harmful or policy-violating content;
9. model/provider and third-party dependencies;
10. misuse/abuse and adversarial interaction;
11. RAG/source poisoning and retrieval integrity;
12. evaluation/TEVV limitations and measurement uncertainty;
13. incident, monitoring and change/revalidation risk.

## RAG control architecture

For retrieval-augmented systems record:

- approved source classes;
- source provenance;
- ingestion authorization;
- freshness/version controls;
- poisoning/tampering protections;
- access-control inheritance;
- sensitive-data restrictions;
- retrieval filtering;
- citation/traceability where relevant;
- source removal and re-indexing procedures;
- evaluation for retrieval relevance and groundedness.

## Third-party/model-provider architecture

### Control objectives
- know model/provider identity and material versions;
- understand data use and retention commitments;
- detect material model/API/capability changes;
- constrain provider/tool access;
- preserve portability/exit options;
- re-evaluate risk after material change;
- establish incident/change-notification expectations.

## TEVV independence model

Testing depth and independence should scale with risk and materiality.

Possible assurance levels:

- **Level 1 — developer self-test:** routine low-risk checks;
- **Level 2 — independent internal challenge:** separate reviewer/team validates assumptions and evidence;
- **Level 3 — specialist/red-team assessment:** security/safety/technical adversarial testing;
- **Level 4 — external/regulated assurance where required:** use only where applicable and never imply NIST itself certifies the system.

## Cross-framework mapping rule

Mappings to EU AI Act, ISO/IEC 42001, Singapore governance or Manual 46 must include a relationship type and a difference/caveat field. No mapping may state that NIST AI RMF alignment automatically satisfies law, certification or another framework.

## Stage-2 completion criterion

Stage 2 is complete when the source/currentness baseline, GOVERN/MAP/MEASURE/MANAGE architecture, GenAI risk-extension architecture, evidence model and TEVV model are controlled and ready for full training-module drafting.