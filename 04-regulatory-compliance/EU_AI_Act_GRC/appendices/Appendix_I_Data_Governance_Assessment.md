# Appendix I — Data-Governance Assessment

## Purpose

Use this assessment to evaluate whether data used to train, tune, validate, test, retrieve for, or operate an AI system is governed appropriately for its intended purpose and risk.

## 1. Dataset identification

| Field | Response |
|---|---|
| System name | |
| Dataset or source name | |
| Data owner | |
| Data steward | |
| Source organization | |
| Data type | |
| Jurisdictions | |
| Assessment date | |

## 2. Purpose and use

Document:

- intended use of the data;
- lifecycle stage supported;
- expected contribution to system performance;
- prohibited or restricted uses;
- affected populations;
- known limitations.

## 3. Provenance and lawful acquisition

| Question | Response | Evidence |
|---|---|---|
| Is the source known and documented? | | |
| Are collection and acquisition lawful? | | |
| Are licenses, permissions, and contractual rights documented? | | |
| Are scraping, reuse, and redistribution restrictions understood? | | |
| Are data subjects or communities affected by reuse? | | |
| Are vendor representations independently verified where proportionate? | | |

## 4. Relevance and representativeness

Assess:

- relevance to intended purpose;
- population and geographic coverage;
- temporal currency;
- class balance;
- subgroup representation;
- rare-event coverage;
- operational-environment alignment;
- differences between training and production conditions.

## 5. Quality assessment

| Quality dimension | Rating | Evidence | Remediation |
|---|---|---|---|
| Accuracy | | | |
| Completeness | | | |
| Consistency | | | |
| Timeliness | | | |
| Validity | | | |
| Uniqueness | | | |
| Label quality | | | |
| Noise and outliers | | | |
| Missingness | | | |

## 6. Bias and discrimination risk

Evaluate:

- historical or structural bias;
- proxy variables;
- differential missingness;
- label bias;
- sampling bias;
- measurement bias;
- subgroup performance impact;
- intersectional effects;
- mitigation trade-offs.

## 7. Privacy and sensitivity

Document:

- personal, sensitive, special-category, confidential, or regulated data;
- minimization and purpose limitation;
- de-identification or pseudonymization;
- retention and deletion;
- access controls;
- cross-border transfers;
- re-identification risk;
- restrictions on training or secondary use.

## 8. Preparation and transformation

Record:

- cleaning and normalization;
- feature engineering;
- deduplication;
- labeling and annotation;
- augmentation or synthetic data;
- filtering and exclusion;
- quality thresholds;
- versioning and reproducibility.

## 9. Lineage and traceability

| Element | Location or identifier |
|---|---|
| Original source | |
| Ingestion record | |
| Transformation pipeline | |
| Version | |
| Approval | |
| Training or validation run | |
| Retention location | |
| Disposal record | |

## 10. Data-control conclusion

Select one:

- [ ] Approved
- [ ] Approved with conditions
- [ ] Limited use only
- [ ] Remediation required
- [ ] Prohibited from use
- [ ] Escalated for legal, privacy, or ethical review

## 11. Action plan

| Action | Owner | Due date | Status | Closure evidence |
|---|---|---|---|---|
| | | | | |

## Approval

| Role | Name | Decision | Date |
|---|---|---|---|
| Data owner | | | |
| Technical owner | | | |
| Privacy or legal | | | |
| Risk or compliance | | | |
