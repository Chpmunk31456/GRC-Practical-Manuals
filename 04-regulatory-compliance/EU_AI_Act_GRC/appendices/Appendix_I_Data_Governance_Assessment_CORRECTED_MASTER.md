# Appendix I — Data-Governance Assessment

> **Legal status:** Corrected English master. This file distinguishes Article 10 duties for providers of high-risk AI systems from broader organizational data-governance, privacy, security, quality, intellectual-property, and records-management controls.

## Purpose

Use this assessment to evaluate whether data used to train, fine-tune, validate, test, retrieve for, operate, monitor, or improve an AI system is suitable, lawful, secure, representative, traceable, and governed for the documented intended purpose and affected population.

The assessment must be version-linked and repeated when source, population, purpose, model, feature, label, transformation, supplier, jurisdiction, or legal conditions change.

## 1. Applicability and scope

| Field | Response |
|---|---|
| System/model | |
| Inventory ID | |
| Version/configuration | |
| Legal entity and actor role | |
| High-risk classification and legal basis | |
| Dataset/source name and version | |
| Data owner and steward | |
| Intended purpose and lifecycle use | |
| Affected persons and populations | |
| Jurisdictions | |
| Article 10 applies? | |
| Related DPIA/FRIA/security assessment | |
| Current legal source and application date | |
| Assessment owner/date | |

## 2. Dataset and lifecycle use

Record each use separately.

| Data use | Dataset/version | Purpose | Population/context | Owner | Evidence location |
|---|---|---|---|---|---|
| Training | | | | | |
| Validation | | | | | |
| Testing | | | | | |
| Fine-tuning | | | | | |
| Retrieval/grounding | | | | | |
| Operational input | | | | | |
| Feedback/continuous learning | | | | | |
| Monitoring | | | | | |
| Synthetic or augmented data | | | | | |

## 3. Purpose and data requirements

Document:

- intended use and prohibited or restricted uses;
- lifecycle stage supported;
- expected contribution to system behaviour and performance;
- required population, geographic, temporal, language, class, and rare-event coverage;
- operational environment and decision context;
- affected populations and vulnerable groups;
- assumptions about what the data measure or represent;
- required quality, quantity, statistical, and lineage characteristics;
- known limitations and acceptable-use conditions.

## 4. Provenance, acquisition, and rights

| Question | Response | Evidence |
|---|---|---|
| Is the source known and documented? | | |
| Are collection and acquisition lawful? | | |
| Are licences, permissions, contracts, and intellectual-property rights documented? | | |
| Are scraping, reuse, training, fine-tuning, redistribution, and downstream restrictions understood? | | |
| Are data-subject, community, customer, or supplier impacts understood? | | |
| Are vendor representations independently verified where proportionate? | | |
| Are provenance gaps or unverifiable sources identified and escalated? | | |

## 5. Article 10 and governance criteria

Assess, as applicable:

- relevant design choices;
- data collection processes and origin;
- preparation, annotation, labelling, cleaning, enrichment, and aggregation;
- formulation of assumptions about what data measure and represent;
- prior assessment of availability, quantity, suitability, and required characteristics;
- examination for possible bias affecting health, safety, fundamental rights, or prohibited discrimination;
- measures to detect, prevent, reduce, and mitigate bias;
- identification of gaps, shortcomings, and remediation;
- representativeness for the intended population and context;
- appropriate statistical properties;
- geographic, contextual, behavioural, functional, language, and accessibility setting;
- versioning, lineage, integrity, security, and reproducibility.

## 6. Relevance and representativeness

Assess:

- relevance to intended purpose;
- population and subgroup coverage;
- geographic and cultural coverage;
- temporal currency;
- class balance and rare-event coverage;
- intersectional representation;
- differences between training, validation, testing, and production conditions;
- coverage of realistic failure, misuse, and edge cases;
- representativeness of feedback and monitoring data.

| Criterion | Method | Result | Limitation | Action |
|---|---|---|---|---|
| Population coverage | | | | |
| Geographic/contextual coverage | | | | |
| Temporal currency | | | | |
| Class/rare-event coverage | | | | |
| Subgroup/intersectional coverage | | | | |
| Production alignment | | | | |

## 7. Quality assessment

| Quality dimension | Rating/result | Evidence | Threshold | Remediation |
|---|---|---|---|---|
| Accuracy | | | | |
| Completeness | | | | |
| Consistency | | | | |
| Timeliness | | | | |
| Validity | | | | |
| Uniqueness/deduplication | | | | |
| Label/annotation quality | | | | |
| Noise and outliers | | | | |
| Missingness | | | | |
| Integrity and corruption | | | | |
| Reproducibility | | | | |

## 8. Bias and discrimination risk

Evaluate:

- historical and structural bias;
- proxy variables and correlated features;
- differential missingness;
- label and annotation bias;
- sampling, selection, survivorship, and measurement bias;
- subgroup and intersectional performance;
- language, disability, age, and geographic effects;
- feedback-loop and cumulative bias;
- mitigation trade-offs and unintended consequences;
- whether monitoring data can detect emerging disparities.

| Bias risk | Affected group | Detection method | Result | Mitigation | Residual limitation |
|---|---|---|---|---|---|
| | | | | | |

## 9. Privacy, sensitivity, and special-category data

Document:

- personal, special-category, biometric, children’s, confidential, proprietary, or regulated data;
- purpose limitation and minimisation;
- lawful processing basis;
- de-identification, pseudonymisation, and re-identification risk;
- access controls and segregation;
- international transfers and localization;
- retention, deletion, archival, and legal hold;
- restrictions on training, secondary use, supplier improvement, or onward disclosure;
- privacy notices, rights handling, and data-subject impacts.

Where special-category personal data are processed for bias monitoring, detection, or correction, record the exact legal basis, strict necessity, access limits, safeguards, pseudonymisation, deletion, documentation, and qualified privacy/legal approval. Do not treat the AI Act as a general permission to process sensitive data.

## 10. Preparation and transformation

Record:

- cleaning and normalization;
- feature engineering and selection;
- deduplication;
- labelling and annotation;
- augmentation or synthetic-data generation;
- filtering, exclusions, and outlier treatment;
- missing-data treatment;
- quality thresholds and rejection criteria;
- transformation code, approvals, and reproducibility;
- version control and rollback.

| Transformation | Method/tool | Version | Owner | Validation | Evidence |
|---|---|---|---|---|---|
| | | | | | |

## 11. Lineage and traceability

| Element | Location or identifier |
|---|---|
| Original source | |
| Acquisition/licence record | |
| Ingestion record | |
| Transformation pipeline | |
| Dataset version/checksum | |
| Approval | |
| Training/validation/test run | |
| Production system/model version | |
| Retention location | |
| Access history | |
| Disposal record | |

## 12. Security and integrity

Assess:

- source authenticity and integrity;
- unauthorized alteration, poisoning, contamination, and leakage;
- access control and segregation;
- encryption and secure transfer;
- supplier and pipeline security;
- backup, recovery, and availability;
- audit logging and anomaly detection;
- secure disposal.

## 13. Decision

- [ ] Approved for the documented use
- [ ] Approved with conditions
- [ ] Limited use or pilot only
- [ ] Remediation required before use
- [ ] Prohibited from use
- [ ] Qualified legal/privacy interpretation required

**Decision rationale:**  
**Residual limitations:**  
**Restricted or prohibited uses:**  
**Monitoring requirements:**  

## 14. Action plan

| Action | Owner | Due date | Status | Validation method | Closure evidence |
|---|---|---|---|---|---|
| | | | | | |

## 15. Change and reassessment triggers

Reassess after changes in:

- source, licence, provider, subprocessor, or acquisition method;
- intended purpose, affected population, jurisdiction, or sector;
- feature, label, annotation, transformation, or synthetic-data method;
- model, prompt, retrieval, feedback, or continuous-learning process;
- quality, bias, performance, privacy, or security results;
- data retention, transfer, location, or access;
- legal basis, consent, contract, authority position, or applicable law.

## GlobalWay Travel Services example

GlobalWay evaluates booking, disruption, and traveler-profile data used by a fraud model. The assessment finds underrepresentation of certain regional travel patterns, inconsistent labels, and supplier reuse of customer data for model improvement. GlobalWay restricts the dataset, corrects labels, expands representative testing, prohibits supplier training without authorization, and links the approved dataset version to the deployed model and monitoring thresholds.

## Approval

| Role | Name | Decision | Date |
|---|---|---|---|
| Data owner/steward | | | |
| Provider/technical owner | | | |
| Privacy/legal | | | |
| Risk/compliance | | | |
| Security, where applicable | | | |

**Evidence references:**  
**Residual limitations:**  
**Conditions/restrictions:**  
**Next review trigger/date:**  
**Assessment version:**  

## Primary legal references

- Regulation (EU) 2024/1689, as amended: Article 10 and applicable risk-management, technical-documentation, logging, monitoring, incident, and high-risk provisions.
- Regulation (EU) 2026/1744 where applicable.
- Regulation (EU) 2016/679 and applicable intellectual-property, database, copyright, confidentiality, cybersecurity, records-management, employment, equality, and sector law.
- Current consolidated official texts control over this template.