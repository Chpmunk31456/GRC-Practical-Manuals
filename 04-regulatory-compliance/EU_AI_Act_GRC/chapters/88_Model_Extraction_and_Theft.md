# Chapter 88 — Model Extraction and Theft

## Purpose

This chapter establishes governance and security controls to protect model weights, prompts, fine-tuning artefacts, embeddings, business logic, APIs, evaluation data, and related intellectual property from extraction, copying, inversion, unauthorised access, or misuse.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should identify model-related assets, classify their sensitivity, restrict access, monitor use, detect extraction patterns, and maintain response and recovery procedures proportionate to business, security, privacy, and rights impacts.

## Plain-language explanation

Attackers may copy a model by stealing files or by making enough carefully designed queries to reproduce its behaviour. Theft may expose confidential information, weaken competitive advantage, enable evasion of safeguards, or create unsafe copies outside the organization’s control.

## Assets in scope

- model weights and checkpoints;
- adapters and fine-tuning artefacts;
- system and developer prompts;
- embeddings and vector indexes;
- proprietary datasets and evaluation sets;
- model architecture and configuration;
- business rules and decision thresholds;
- API credentials and deployment images;
- safety policies and red-team results;
- logs that reveal model behaviour.

## Threat scenarios

Consider:

- theft from repositories, storage, endpoints, or backups;
- compromised cloud or vendor accounts;
- excessive API querying used to clone behaviour;
- membership inference or model inversion;
- insiders copying artefacts;
- exposed development environments;
- model files embedded in insecure client applications;
- leaked prompts or evaluation datasets;
- unauthorised export by vendors or subprocessors;
- stolen models used to discover bypasses.

## Preventive controls

Use risk-appropriate controls such as:

- asset classification and ownership;
- least privilege and just-in-time access;
- strong authentication and privileged-access management;
- encryption in transit and at rest;
- controlled repositories and signed artefacts;
- environment separation;
- export restrictions;
- API authentication, quotas, and rate limits;
- query and response minimisation;
- watermarking or fingerprinting where appropriate;
- endpoint and cloud monitoring;
- contractual restrictions and audit rights;
- secure deletion and key revocation.

## Detection

Monitor for:

- abnormal query volume or coverage patterns;
- repeated boundary probing;
- systematic variation of prompts;
- large artefact downloads;
- unusual administrative access;
- access from unexpected locations or devices;
- unauthorised copies or exports;
- suspicious model-performance replication;
- disabled logging or altered audit records.

## Privacy and rights considerations

Extraction and inversion may reveal personal or special-category data represented in model behaviour. Security response should therefore coordinate with privacy, legal, incident-response, and affected-person processes.

## Human approval

High-risk exports, model transfers, new API access, privileged downloads, and emergency restoration should require accountable human approval and complete records.

## GlobalWay Travel Services example

GlobalWay exposes an itinerary-ranking model through an internal API. Security monitoring detects a service account issuing thousands of systematically varied requests after normal hours.

The account is suspended, tokens are revoked, query logs are preserved, and the incident team assesses whether model behaviour, traveller data, or business rules were extracted. Restoration requires security and business-owner approval.

## Stop and escalation conditions

Escalate when:

- model files or credentials are exposed;
- extraction indicators exceed thresholds;
- privileged access is unexplained;
- logging is unavailable;
- personal data may have been inferred;
- vendor access cannot be constrained;
- stolen artefacts could enable safety-control bypass.

## Evidence

- model-asset register;
- access-control records;
- repository and storage configurations;
- API quotas and monitoring rules;
- export approvals;
- vendor contracts;
- alert and incident records;
- forensic evidence;
- revocation and recovery records;
- periodic access reviews.

## Audit tests

1. Trace sensitive model assets to owners and controls.
2. Review privileged and vendor access.
3. Test API limits and extraction detection.
4. Verify artefact encryption and repository protection.
5. Examine sampled exports for approval and traceability.
6. Confirm incident procedures cover inversion and privacy impacts.
7. Verify access and keys can be revoked rapidly.

## Metrics

- privileged users with model access;
- anomalous extraction alerts;
- unauthorised export attempts;
- stale service accounts;
- time to revoke compromised access;
- high-risk transfers lacking complete approval;
- vendors with unresolved access findings.

## Management checklist

- Are model assets classified and owned?
- Is access limited and reviewed?
- Can extraction through APIs be detected?
- Are exports controlled?
- Are privacy implications considered?
- Can compromised access be revoked immediately?

## Figure specification — Model Protection Architecture

Create a formal architecture showing protected model assets inside controlled repositories and runtime environments, surrounded by identity, encryption, API gateway, rate limiting, monitoring, export approval, incident response, and recovery controls.

**Alt text:** Model protection architecture showing controlled model assets protected by identity, encryption, API controls, monitoring, export approval, incident response, and recovery.
