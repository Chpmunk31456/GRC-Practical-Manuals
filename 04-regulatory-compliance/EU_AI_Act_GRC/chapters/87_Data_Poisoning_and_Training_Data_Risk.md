# Chapter 87 — Data Poisoning and Training-Data Risk

## Purpose

This chapter establishes governance for risks arising from malicious, corrupted, biased, unlawful, low-quality, stale, or untraceable training, fine-tuning, validation, test, retrieval, and feedback data.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should control data provenance, lawfulness, suitability, quality, integrity, representativeness, access, change, and lineage throughout the AI lifecycle. Data must not be accepted merely because it is available or supplied by a trusted vendor.

## Plain-language explanation

Data poisoning occurs when data is intentionally or accidentally altered so the AI learns, retrieves, or produces harmful behaviour. Training-data risk also includes hidden bias, unlawful collection, missing populations, stale content, duplicate records, weak labels, and undocumented transformations.

## Data categories in scope

- pre-training and foundation-model data where information is available;
- fine-tuning and adaptation datasets;
- validation and test datasets;
- retrieval and vector-store content;
- user feedback and reinforcement data;
- synthetic data;
- third-party and public datasets;
- operational logs reused for improvement;
- human labels and annotations.

## Core controls

Controls should include:

- approved sources and acquisition criteria;
- provenance and licence records;
- legal-basis and purpose review;
- integrity verification and checksums;
- access control and segregation of duties;
- duplicate, anomaly, outlier, and contamination detection;
- label-quality review;
- representative sampling and subgroup analysis;
- separation of training, validation, and test data;
- change control and versioning;
- quarantine and rollback;
- documented transformations;
- retention and deletion controls;
- vendor evidence and contractual rights.

## Poisoning scenarios

Consider:

- malicious records inserted into public or supplier data;
- manipulated feedback that changes model behaviour;
- hostile content added to retrieval stores;
- backdoor triggers embedded in examples;
- deliberate mislabelling;
- test-set contamination;
- compromised data pipelines;
- insiders altering approved datasets;
- synthetic data amplifying prior errors;
- stale operational data producing unsafe recommendations.

## Quality and representativeness

Assess whether the data is sufficiently relevant, representative, complete, accurate, and appropriate for the intended context. Document known gaps, affected groups, geographic limitations, temporal limits, and conditions under which use must stop.

## Human review

Qualified humans should approve dataset inclusion, investigate anomalies, review high-impact labels, assess subgroup effects, and decide whether residual limitations are acceptable.

## Monitoring and change

Monitor for shifts in source quality, data distribution, labels, subgroup performance, retrieval content, and user-feedback patterns. Material changes should trigger revalidation and, where necessary, rollback or retraining.

## GlobalWay Travel Services example

GlobalWay uses disruption history to improve itinerary recommendations. A compromised supplier feed inserts false cancellation patterns favouring one carrier.

GlobalWay validates source identity, compares records with independent operational feeds, quarantines anomalies, reviews carrier-level distribution shifts, and requires human approval before the data enters training. The affected dataset version is rejected and preserved as incident evidence.

## Stop and escalation conditions

Stop use when:

- provenance or rights cannot be established;
- integrity checks fail;
- poisoning or backdoor indicators are detected;
- test contamination invalidates results;
- subgroup harm exceeds tolerance;
- critical data transformations are undocumented;
- deletion or correction obligations cannot be executed;
- vendor evidence is materially incomplete.

## Evidence

- dataset register and lineage;
- source and licence records;
- integrity results;
- quality and representativeness assessments;
- subgroup testing;
- annotation procedures;
- change and approval records;
- anomaly investigations;
- quarantine and rollback records;
- vendor documentation.

## Audit tests

1. Trace sampled data from source to deployed model or retrieval store.
2. Verify integrity, access, versioning, and approvals.
3. Test separation of training and test datasets.
4. Review anomaly and poisoning detection.
5. Confirm subgroup and temporal limitations are documented.
6. Verify material changes triggered revalidation.
7. Confirm rejected or corrected data can be removed and traced.

## Metrics

- datasets with complete provenance;
- integrity failures;
- quarantined records;
- unresolved quality exceptions;
- subgroup performance gaps;
- data changes requiring revalidation;
- time to remove poisoned or unlawful data;
- vendors lacking required evidence.

## Management checklist

- Do we know where the data came from?
- Is its use lawful and appropriate?
- Can tampering be detected?
- Are training and testing separated?
- Are gaps and subgroup impacts understood?
- Can data be corrected, removed, or rolled back?

## Figure specification — Trusted AI Data Pipeline

Create a formal pipeline showing source approval, provenance, legal review, integrity checks, quality and subgroup testing, quarantine, controlled transformation, versioning, model or retrieval use, monitoring, and rollback.

**Alt text:** Trusted AI data pipeline from approved sources through provenance, legal and integrity checks, quality testing, quarantine, controlled use, monitoring, and rollback.
