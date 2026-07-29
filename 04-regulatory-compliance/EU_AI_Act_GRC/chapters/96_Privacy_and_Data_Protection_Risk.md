# Chapter 96 — Privacy and Data-Protection Risk

## Purpose

This chapter provides a practical method for assessing and controlling privacy and data-protection risks across the AI lifecycle.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should identify how an AI system collects, generates, infers, combines, stores, uses, shares, and deletes personal data. Privacy and data-protection risk must be evaluated before deployment, after material change, and continuously during operation.

The assessment should be coordinated with applicable privacy-law obligations, including data-protection impact assessment processes where required, while remaining distinct from the AI Act risk-management process.

## Plain-language explanation

AI can create privacy risk even when it does not use obvious identifiers. Models may infer sensitive information, combine datasets to reveal identity, memorize training data, expose personal information through outputs, or use data for purposes people did not reasonably expect.

Privacy review therefore covers the entire data and model lifecycle, not only a privacy notice or consent screen.

## Privacy-risk categories

Assess at least:

- excessive or irrelevant data collection;
- unclear or incompatible purpose;
- weak lawful-basis analysis;
- undisclosed secondary use;
- sensitive or special-category data;
- children’s data;
- inferred attributes and profiling;
- re-identification and linkage risk;
- training-data memorization;
- prompt, output, or retrieval-data leakage;
- cross-border transfers;
- vendor and subprocessor access;
- excessive retention;
- ineffective deletion;
- inaccurate personal data;
- inability to exercise rights;
- opaque automated decisions;
- surveillance or monitoring disproportionate to purpose;
- security weaknesses affecting confidentiality, integrity, or availability.

## Assessment method

### 1. Map the data lifecycle

Document:

- data sources;
- data subjects;
- collection methods;
- purposes;
- categories of personal data;
- sensitive and inferred attributes;
- transformations and enrichment;
- training, validation, retrieval, prompt, and output flows;
- storage locations;
- recipients and subprocessors;
- transfer mechanisms;
- retention and deletion rules.

### 2. Confirm necessity and proportionality

Determine whether each data element is necessary for the stated purpose. Consider less intrusive alternatives, smaller datasets, shorter retention, local processing, aggregation, pseudonymization, or human-only processes.

A technically useful data element is not automatically necessary or proportionate.

### 3. Assess lawful and transparent use

Verify:

- a documented legal basis;
- compatible and specific purposes;
- clear notices;
- appropriate consent where relied upon;
- controls for secondary use;
- treatment of sensitive and children’s data;
- automated-decision and profiling implications;
- mechanisms for rights requests and complaints.

### 4. Evaluate model-specific privacy threats

Test for:

- memorization and unintended reproduction;
- model inversion;
- membership inference;
- prompt leakage;
- retrieval leakage;
- cross-user or cross-tenant exposure;
- sensitive-attribute inference;
- re-identification;
- training-data extraction;
- insecure logging;
- excessive telemetry;
- privacy leakage through human-review workflows.

### 5. Select controls

Controls may include:

- data minimization;
- purpose limitation;
- pseudonymization or anonymization;
- field-level masking;
- access control and segregation;
- encryption;
- privacy-preserving training techniques;
- synthetic or representative test data;
- output filtering;
- prompt and retrieval isolation;
- retention automation;
- deletion verification;
- rights-request workflows;
- vendor restrictions;
- transfer controls;
- privacy testing and independent review.

### 6. Coordinate assessments

Align, without improperly merging:

- AI risk assessment;
- data-protection impact assessment;
- fundamental-rights impact assessment;
- security risk assessment;
- vendor risk assessment;
- records of processing;
- incident and breach response.

Each assessment should retain its own purpose, owner, conclusions, and approval record while sharing evidence where appropriate.

### 7. Approve residual privacy risk

Document remaining risk, affected persons, safeguards, uncertainty, and accountable approval. Unresolved high-risk privacy impacts should block deployment, trigger redesign, or require additional legal and regulatory review.

## Data-subject rights and contestability

Operational processes should support applicable rights, including:

- access;
- correction;
- deletion;
- restriction;
- objection;
- portability;
- explanation or meaningful information where required;
- challenge and human review of consequential decisions;
- complaint and remedy.

Teams must know whether a request requires changes to source data, derived features, prompts, retrieval stores, logs, model outputs, or downstream systems.

## GlobalWay Travel Services example

GlobalWay plans to use traveler support transcripts to improve a generative-AI assistant. The privacy assessment identifies passport numbers, health-related accommodation requests, payment details, and travel histories within the transcripts.

GlobalWay excludes payment data, applies automated and manual redaction, separates accommodation data, limits the training purpose, restricts vendor use, shortens retention, tests for memorization, and provides an internal deletion workflow. The project cannot proceed until the privacy team approves the data flow and test evidence.

## Control activities

- Maintain an accurate AI personal-data flow map.
- Define purpose, legal basis, necessity, and retention.
- Minimize and protect training, prompt, retrieval, output, and log data.
- Assess sensitive, inferred, children’s, and cross-border data.
- Test model-specific privacy threats.
- Implement rights-request and deletion workflows.
- Coordinate AI, privacy, rights, security, and vendor assessments.
- Monitor incidents, complaints, drift, and new uses.
- Reassess after material changes.

## Evidence

- data-flow map;
- records of processing;
- purpose and lawful-basis analysis;
- necessity and proportionality assessment;
- data-protection impact assessment where applicable;
- data inventory and classification;
- retention schedule;
- vendor and transfer records;
- privacy test plans and results;
- redaction and minimization evidence;
- rights-request procedures and records;
- deletion-verification records;
- incident and breach records;
- residual-risk approvals;
- change and reassessment records.

## Audit tests

1. Select AI systems processing personal data and inspect their data-flow maps.
2. Verify purpose, legal basis, minimization, and retention decisions.
3. Confirm that sensitive, inferred, children’s, and transferred data were assessed.
4. Review model-specific privacy testing and remediation.
5. Trace data-subject requests through source, derived, and downstream data stores.
6. Inspect deletion controls and verification evidence.
7. Review vendor access, reuse restrictions, subprocessors, and transfer controls.
8. Confirm that material changes triggered renewed privacy assessment.

## Metrics

- AI systems with complete personal-data maps;
- systems requiring and completing privacy impact assessments;
- excessive-data findings;
- privacy test failures;
- sensitive-data exposures;
- rights requests involving AI systems;
- average response and deletion-verification time;
- unresolved high privacy risks;
- privacy incidents and near misses;
- vendor privacy exceptions;
- overdue reassessments.

## Management checklist

- What personal data does the system use, infer, or expose?
- Is each data element necessary and proportionate?
- Are purposes, legal bases, notices, and retention documented?
- Can the model memorize, reveal, or permit inference of personal data?
- Can people exercise applicable rights effectively?
- Are vendors and cross-border transfers controlled?
- Are AI, privacy, rights, and security assessments coordinated?
- Is residual privacy risk within approved tolerance?

## Figure specification — AI Privacy and Data-Protection Lifecycle

Create a lifecycle diagram showing: map data flows, define purpose and legal basis, minimize and protect data, test model-specific privacy threats, enable rights and deletion, control vendors and transfers, approve residual risk, monitor incidents and new uses, and reassess after change. Include a redesign or stop-deployment path for unacceptable privacy risk.

**Alt text:** AI privacy and data-protection lifecycle from data mapping and purpose definition through minimization, privacy testing, rights handling, vendor controls, residual-risk approval, and continuous reassessment.
