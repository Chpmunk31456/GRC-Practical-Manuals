# Chapter 128 — Evidence Preservation and Legal Hold

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 128 draft language.

## Purpose

This chapter explains how organizations should preserve AI-related evidence and implement legal holds when litigation, investigation, enforcement, a serious incident, a complaint, or a material dispute is reasonably anticipated.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations must preserve records required by the EU AI Act and other applicable law and should implement legal holds when litigation, investigation, enforcement, incident, complaint, or dispute is reasonably anticipated. A legal hold is a legal-process control, not a standalone EU AI Act obligation, but it supports compliance with documentation, logging, recordkeeping, authority-access, incident, corrective-action, and post-market-monitoring duties.

## Plain-English explanation

AI evidence may be distributed across cloud services, model providers, source-code repositories, monitoring platforms, ticketing systems, business applications, employee communications, and third-party systems. Routine deletion, log rotation, model retirement, or supplier overwrite must stop when relevant evidence may be needed. Preservation must cover documents and technical artifacts together so that decisions, model behavior, system context, and human actions can be reconstructed.

## Trigger events

Consider preservation or a legal hold after:

- a regulatory inquiry, inspection, or information request;
- threatened or filed litigation;
- a serious incident or credible allegation of harm;
- suspected use of a prohibited AI practice;
- a discrimination, privacy, safety, employment, or consumer complaint;
- a cybersecurity compromise affecting AI operation or evidence integrity;
- a whistleblower report or internal investigation;
- a material vendor dispute, outage, or model change;
- an executive- or board-directed review;
- an anticipated insurance claim;
- system restriction, suspension, recall, withdrawal, or major corrective action.

## Preservation requirements

Define at minimum:

1. statutory, regulatory, contractual, and policy retention obligations;
2. legal-hold triggers, decision authority, and escalation routes;
3. custodians, systems, models, versions, repositories, environments, and suppliers in scope;
4. relevant logs, prompts, outputs, datasets, code, configuration, documentation, and communications;
5. preservation of metadata, authenticity, integrity, context, and chain of custody;
6. suspension of deletion, rotation, overwriting, archival disposal, and model retirement;
7. prompt capture of volatile, ephemeral, or externally controlled evidence;
8. third-party preservation notices, acknowledgements, and verification;
9. privacy, data-minimisation, confidentiality, privilege, security, and access controls;
10. collection, export, indexing, reproducibility, and review requirements;
11. periodic review, expansion, modification, and authorized release of the hold;
12. documentation of unavailable evidence, preservation gaps, compensating measures, and remediation;
13. secure disposition after lawful release.

## Evidence scope

Preserve as relevant:

- AI inventory, ownership, role, and classification records;
- model binaries, weights, versions, identifiers, checksums, and release metadata where available;
- source code, scripts, prompts, system instructions, retrieval configuration, and tool definitions;
- training, tuning, validation, testing, and production data where lawful;
- data lineage, provenance, quality, representativeness, bias, and preprocessing records;
- logs, monitoring alerts, outputs, overrides, approvals, and user interactions;
- deployment, release, rollback, and change-management records;
- risk, impact, privacy, security, legal, and conformity assessments;
- technical documentation, instructions for use, and registration records;
- human-oversight instructions, reviewer actions, and decision records;
- vendor contracts, notices, attestations, incident records, and communications;
- complaints, tickets, investigations, corrective actions, and closure evidence;
- emails, messages, meeting minutes, executive decisions, and regulator correspondence.

## AI-specific preservation challenges

Address:

- rapidly changing vendor models and inaccessible proprietary artifacts;
- ephemeral prompts, temporary sessions, and short log-retention periods;
- dynamic retrieval sources and continuously updated datasets;
- agent tool calls, external API actions, and downstream system changes;
- model nondeterminism and reproducibility limits;
- distributed cloud, regional storage, and cross-border restrictions;
- privacy constraints and special-category data;
- open-source component changes and dependency replacement;
- employee use of unapproved or personal AI tools.

## Vendor preservation

Contracts and incident procedures should support prompt supplier preservation of relevant model versions, logs, documentation, subprocessors, service changes, and incident evidence. Record any limitation on the organization’s ability to obtain or preserve supplier-controlled evidence and escalate material gaps.

## Integrity and chain of custody

Maintain:

- source, custodian, and system of record;
- collection date, method, and collector;
- file, object, model, and version identifiers;
- hashes or other integrity checks where appropriate;
- original metadata and contextual relationships;
- secure storage location and access controls;
- access, transfer, export, and production history;
- transformations, redactions, or format conversions;
- reviewer, approval, and release records.

Preserve originals separately from working copies.

## Privacy, confidentiality, and privilege

Preservation does not remove privacy, confidentiality, cybersecurity, professional-secrecy, or privilege obligations. Limit access, apply lawful collection boundaries, protect sensitive data, document redactions, and obtain legal and privacy review for cross-border transfers, special-category data, employee data, and supplier-controlled evidence.

## GlobalWay Travel Services example

After travelers allege discriminatory blocking by GlobalWay’s fraud-detection system, legal counsel issues a hold covering the deployed model version, feature configuration, transaction decisions, human overrides, subgroup tests, complaints, vendor change notices, and internal communications.

GlobalWay discovers that application logs normally rotate after 30 days. It suspends deletion, exports relevant logs with integrity checks, obtains preservation confirmation from the vendor, and documents that one historical proprietary model artifact is unavailable. The limitation is disclosed, escalated, and considered in the investigation and remediation plan.

## Control activity

Legal must issue documented holds when required, and Technology, Records Management, Security, Privacy, HR, business owners, and suppliers must confirm implementation. The organization must test whether technically volatile AI evidence can actually be preserved, linked to the correct version, and reproduced sufficiently for investigation, audit, or authority review.

## Evidence

- retention schedule and legal-hold procedure;
- evidence-source and system maps;
- hold notices, scope changes, and acknowledgements;
- custodian, repository, supplier, and system lists;
- preservation, collection, and export logs;
- hashes, metadata, and chain-of-custody records;
- supplier preservation confirmations and disclosed limitations;
- access, redaction, and production records;
- periodic hold reviews;
- exception, gap, and remediation records;
- hold-release and disposition approvals.

## Audit test

Select legal holds involving AI systems. Confirm that triggers were identified promptly, scope included relevant technical and human evidence, deletion and overwrite were suspended, volatile and supplier-controlled evidence was addressed, integrity and custody were protected, privacy and privilege controls were applied, gaps were disclosed, and release was authorized and documented.

## Metrics

- time from trigger to preservation action;
- custodians, systems, suppliers, and evidence sources under hold;
- missed or late acknowledgements;
- evidence lost before preservation;
- supplier-preservation gaps;
- log sources with inadequate retention;
- chain-of-custody exceptions;
- unauthorized access to held evidence;
- open holds by age;
- released holds awaiting verified disposition.

## Management checklist

- Do we know where material AI evidence resides?
- Can we stop deletion, rotation, model retirement, and vendor overwrite quickly?
- Are model, prompt, data, log, configuration, and human-decision records preserved together?
- Can we demonstrate authenticity, integrity, context, and chain of custody?
- Are privacy, confidentiality, privilege, and cross-border restrictions protected?
- Are supplier limitations and evidence gaps disclosed and escalated?
- Is hold release controlled and verified?

## Figure specification — AI Evidence Preservation Map

Create a map connecting trigger events to legal-hold activation, custodians, models, data, prompts, logs, code, vendors, communications, collection, integrity validation, secure storage, review, production, and authorized release.

**Alt text:** AI evidence-preservation map linking legal-hold triggers to custodians and technical evidence sources, followed by collection, integrity validation, secure storage, controlled review, production, and authorized release.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable technical-documentation, logging, recordkeeping, quality-management, monitoring, incident, corrective-action, and authority-access provisions.
- Regulation (EU) 2016/679 and other applicable privacy, employment, evidentiary, and procedural law.
- Regulation (EU) 2026/1744 where applicable.
- Legal-hold duties depend on applicable procedural and substantive law and must not be presented as a universal standalone EU AI Act requirement.
