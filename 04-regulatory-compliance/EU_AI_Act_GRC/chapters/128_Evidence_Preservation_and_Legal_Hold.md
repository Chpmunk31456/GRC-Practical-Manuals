# Chapter 128 — Evidence Preservation and Legal Hold

## Purpose

This chapter explains how organizations should preserve AI-related evidence and implement legal holds when litigation, investigation, regulatory inquiry, serious incident, or material dispute is reasonably anticipated.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should maintain documented evidence-preservation and legal-hold procedures that cover AI systems, models, data, prompts, logs, configurations, vendor records, communications, approvals, and decision evidence. Preservation must be timely, proportionate, secure, and capable of demonstrating authenticity, integrity, custody, and relevance.

## Plain-language explanation

AI evidence is often distributed across cloud services, model providers, source-code repositories, monitoring platforms, ticketing systems, business applications, user interfaces, and employee communications. Ordinary retention schedules or automated deletion can destroy critical evidence unless preservation is activated quickly and verified.

## Trigger events

Consider preservation or legal hold after:

- regulatory inquiry, inspection, or information request;
- threatened or filed litigation;
- serious incident or credible harm allegation;
- suspected prohibited practice;
- discrimination, privacy, safety, or consumer complaint;
- cybersecurity compromise;
- whistleblower report;
- internal investigation;
- material vendor dispute or failure;
- executive or board-directed review;
- anticipated insurance claim;
- system suspension, recall, withdrawal, or major corrective action.

## Evidence scope

Preserve as relevant:

- AI inventory and ownership records;
- model binaries, weights, versions, and checksums where available;
- source code, scripts, prompts, system instructions, and configuration;
- training, tuning, validation, testing, and production data where lawful;
- data lineage, provenance, quality, and preprocessing records;
- logs, monitoring alerts, outputs, overrides, and user interactions;
- deployment, release, rollback, and change records;
- risk, impact, privacy, security, and legal assessments;
- technical documentation and conformity records;
- human-oversight instructions and reviewer decisions;
- vendor contracts, notices, attestations, and communications;
- incidents, complaints, tickets, and corrective actions;
- emails, messages, meeting records, and executive decisions;
- regulator, customer, insurer, auditor, and counsel correspondence.

## Preservation process

1. Identify the triggering event and legal basis.
2. Appoint legal, investigation, and evidence leads.
3. Define custodians, systems, date ranges, jurisdictions, and evidence categories.
4. Suspend conflicting deletion, rotation, overwrite, or disposal processes.
5. Issue clear preservation notices to relevant personnel and vendors.
6. Capture volatile evidence promptly.
7. Preserve original metadata and system context.
8. Record collection method, custody, access, and transfers.
9. Validate completeness and integrity.
10. Review, update, and release the hold only through authorized approval.

## AI-specific preservation challenges

Address:

- rapidly changing vendor models;
- inaccessible proprietary model artifacts;
- ephemeral prompts and session data;
- overwritten application and security logs;
- dynamic retrieval sources;
- continuously updated datasets;
- agent tool calls and external API actions;
- model nondeterminism;
- distributed cloud and regional storage;
- privacy and cross-border restrictions;
- open-source component changes;
- employee use of unapproved AI tools.

## Vendor preservation

Contracts and response procedures should support prompt vendor preservation of relevant versions, logs, documentation, incident evidence, subprocessors, and service changes. Record any limitation on the organization’s ability to obtain or preserve supplier evidence and escalate material gaps.

## Integrity and chain of custody

Maintain:

- source and custodian;
- collection date and collector;
- file or object identifiers;
- hashes or integrity checks where appropriate;
- original metadata;
- storage location;
- access and transfer history;
- transformations or redactions;
- reviewer and approval records.

Preserve originals separately from working copies.

## Privacy, confidentiality, and privilege

Preservation does not remove privacy, confidentiality, security, or privilege obligations. Limit access, apply lawful collection boundaries, protect sensitive data, document redactions, and consult legal and privacy specialists on cross-border transfers and special-category data.

## GlobalWay Travel Services example

After travelers allege discriminatory blocking by GlobalWay’s fraud-detection system, legal counsel issues a hold covering the deployed model version, feature configurations, transaction decisions, human overrides, subgroup tests, complaints, vendor change notices, and internal communications.

GlobalWay discovers that application logs normally rotate after 30 days. It suspends deletion, exports the relevant logs with integrity checks, obtains preservation confirmation from the vendor, and documents a gap involving one unavailable historical model artifact. The limitation is disclosed and considered in the investigation.

## Control activities

- Define legal-hold triggers and authority.
- Maintain maps of AI evidence sources and retention schedules.
- Suspend deletion and overwrite processes promptly.
- Preserve volatile and vendor-controlled evidence.
- Maintain integrity and chain-of-custody records.
- Verify hold acknowledgements and compliance.
- Review scope after new facts, systems, or custodians emerge.
- Release holds only after legal authorization and documented verification.

## Evidence

- preservation and legal-hold policy;
- evidence-source maps;
- retention schedules;
- hold notices and acknowledgements;
- custodian and system lists;
- collection logs;
- hashes and chain-of-custody records;
- vendor preservation confirmations;
- access records;
- scope updates;
- exception and gap records;
- hold-release approvals.

## Audit tests

1. Select legal holds involving AI and verify triggers, scope, custodians, and systems were documented.
2. Confirm automated deletion or log rotation was suspended where required.
3. Trace selected evidence from source through collection, storage, access, and production.
4. Review integrity checks and separation of originals from working copies.
5. Verify vendors preserved relevant evidence and disclosed limitations.
6. Confirm privacy, confidentiality, privilege, and cross-border controls were applied.
7. Review hold releases for legal approval and verified disposition.

## Metrics

- time from trigger to preservation action;
- custodians and systems under hold;
- missed or late acknowledgements;
- evidence lost before preservation;
- vendor preservation gaps;
- log sources with inadequate retention;
- chain-of-custody exceptions;
- unauthorized access to held evidence;
- open holds by age;
- released holds awaiting disposition verification.

## Management checklist

- Do we know where material AI evidence resides?
- Can we stop deletion, rotation, and vendor overwrite quickly?
- Are model, prompt, data, log, and configuration versions preserved together?
- Can we demonstrate authenticity and chain of custody?
- Are privacy and privilege protected during preservation?
- Are evidence gaps disclosed and escalated?

## Figure specification — AI Evidence Preservation Map

Create a map connecting trigger events to legal-hold activation, custodians, models, data, prompts, logs, code, vendors, communications, collection, integrity validation, secure storage, review, production, and authorized release.

**Alt text:** AI evidence-preservation map linking legal-hold triggers to custodians and technical evidence sources, followed by collection, integrity validation, secure storage, controlled review, production, and authorized release.