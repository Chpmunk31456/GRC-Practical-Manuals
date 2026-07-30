# Chapter 76 — Cloud, API, and Model Dependency Risk

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 76 draft language.

## Requirement

Organizations must identify and manage material cloud, API, model, data, software-component, and subprocessor dependencies that affect their AI systems. The EU AI Act does not create a standalone dependency-risk programme for every operator, but applicable provider, deployer, importer, distributor, product-manufacturer, quality-management, risk-management, cybersecurity, monitoring, incident, documentation, and cooperation duties require sufficient visibility and control over relevant dependencies.

## Plain-English explanation

An AI service may depend on several external components even when it appears to users as a single system. A provider change, outage, model substitution, API deprecation, regional routing change, undocumented subprocessor, or loss of logs can alter legal classification, safety, accuracy, accessibility, privacy, security, human oversight, or continuity. Contracting out a component does not remove the organization’s own legal duties.

## Dependency-governance requirements

For each material dependency, document and assess:

1. component, provider, subprocessor, purpose, owner, and criticality;
2. model, API, software, data, and configuration versions;
3. processing and support locations, data flows, retention, and transfer arrangements;
4. availability, service levels, recovery capability, quotas, and rate limits;
5. change-notification, release, deprecation, and emergency-change processes;
6. security, privileged access, secrets, tenant separation, and vulnerability management;
7. logging, monitoring, evidence access, and incident-notification capability;
8. concentration, lock-in, substitution, and single-point-of-failure risk;
9. tested fallback, safe-mode, human-only, or controlled-suspension arrangements;
10. triggers for reassessment, revalidation, transparency review, or substantial-modification analysis.

## GlobalWay example

GlobalWay’s traveler-assistance service relies on a hosted model, cloud platform, translation API, identity provider, retrieval database, and monitoring service. After an unannounced model update reduces multilingual accuracy and omits accessibility constraints, GlobalWay restricts affected functions, routes cases to trained consultants, preserves version and output evidence, requires provider investigation, and revalidates the service before restoration.

## Control activity

Material dependencies must be recorded in the AI inventory and architecture documentation. High or critical dependencies must be monitored for change and outage, tested before material production changes, and supported by approved continuity and escalation arrangements. Unknown critical dependencies or unavailable mandatory evidence are release or continued-operation blockers.

## Evidence

- dependency and architecture inventory;
- provider and subprocessor records;
- version and configuration history;
- contracts, service levels, and change notices;
- data-location and transfer assessments;
- security and access reviews;
- test, regression, and revalidation results;
- monitoring, outage, and incident records;
- fallback and continuity exercises;
- risk acceptance and accountable-owner decisions.

## Audit test

Select high and critical AI systems. Confirm that material dependencies are complete and current; versions, regions, subprocessors, and owners are known; material changes triggered appropriate review and testing; continuity arrangements were exercised; evidence remained accessible; and unresolved dependency risks were escalated to authorized decision-makers.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable Articles 9–17, 20–26, 72–74, 78–82, and related annexes, depending on role and system classification.
- Regulation (EU) 2016/679 and other applicable privacy, cybersecurity, product-safety, consumer-protection, and sector requirements.
- Dependency-management practices in this chapter are governance and assurance methods used to support applicable legal duties; they are not a standalone statutory control catalogue.
- Current consolidated official texts control over older summaries.
