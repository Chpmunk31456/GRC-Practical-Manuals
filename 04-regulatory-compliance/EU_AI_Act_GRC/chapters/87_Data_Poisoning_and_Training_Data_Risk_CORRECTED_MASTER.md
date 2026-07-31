# Chapter 87 — Data Poisoning and Training Data Risk

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 87 draft language.

## Requirement

Organizations must protect training, validation, testing, fine-tuning, retrieval, and feedback data against unauthorized alteration, malicious contamination, provenance failure, quality degradation, and hidden bias that could undermine compliance, safety, security, or performance.

## Plain-English explanation

Data poisoning can be deliberate or accidental. A small amount of manipulated data may create hidden behaviors, biased outcomes, degraded accuracy, or security weaknesses. Controls must cover data sources, transformations, labels, access, lineage, approvals, and post-deployment feedback loops.

## Control requirements

Implement as appropriate:

1. approved-source and provenance controls;
2. access control, segregation of duties, and change logging;
3. integrity checks, hashes, versioning, and reproducible pipelines;
4. anomaly, duplication, outlier, and label-quality testing;
5. subgroup and representativeness analysis;
6. supplier and open-source dataset due diligence;
7. quarantine and review of user feedback or production data before reuse;
8. backdoor, trigger, and targeted-poisoning tests;
9. rollback, retraining, and affected-version identification;
10. retention of datasets, decisions, transformations, and validation evidence.

## GlobalWay example

GlobalWay fine-tunes a recruitment model using historical application data. Before use, the team validates provenance, detects duplicate and manipulated records, reviews protected-group representation, separates production feedback from approved retraining data, and blocks unreviewed data from entering the pipeline.

## Control activity

No dataset may enter a material AI training or fine-tuning pipeline without documented ownership, provenance, integrity, quality, legal-use, and risk approval. Material changes require retesting and version-linked release authorization.

## Evidence

- dataset inventory and provenance records;
- access and change logs;
- integrity and quality test results;
- subgroup and representativeness analysis;
- supplier dataset assurance;
- poisoning and backdoor test results;
- retraining and rollback records;
- approval and release evidence.

## Audit test

Select a sample of datasets used in production models. Verify approved provenance, controlled access, reproducible transformations, integrity and poisoning tests, documented quality limitations, and linkage between dataset version, model version, and release decision.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable data and data-governance, risk-management, accuracy, robustness, cybersecurity, technical-documentation, and post-market provisions.
- Current consolidated EUR-Lex text controls over older summaries.