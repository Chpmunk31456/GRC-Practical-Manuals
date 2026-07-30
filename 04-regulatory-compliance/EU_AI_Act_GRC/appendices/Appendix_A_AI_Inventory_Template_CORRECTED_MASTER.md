# Appendix A — AI Inventory Template

> **Legal status:** Corrected English master. This is an organizational governance register. Specific fields become legally required only where a binding provision applies to the relevant actor, system, model, component, or use.

## Purpose

Use this template to maintain a complete, current, version-linked, and auditable inventory of AI systems, GPAI models, embedded AI capabilities, components, integrations, pilots, and material use cases across the organization.

The inventory should support applicability, role, classification, risk, transparency, conformity, monitoring, incident, evidence, and change-management decisions. It must distinguish statutory classifications from organization-defined governance tiers.

## Inventory record

| Field | Required information |
|---|---|
| Inventory ID | Unique, persistent identifier |
| Record status | Draft, active, restricted, suspended, retired, archived |
| Legal entity | Entity developing, providing, importing, distributing, integrating, placing on the market, putting into service, or deploying the system/model |
| Actor role(s) | Provider, GPAI provider, downstream provider, deployer, importer, distributor, authorised representative, product manufacturer, other |
| System/model name | Official business, product, model, and technical names |
| Business owner | Accountable executive or process owner and alternate |
| Technical owner | Accountable engineering, architecture, data, or platform owner and alternate |
| Control owners | Legal, Compliance, Risk, Privacy, Security, Data, Procurement, HR, Product, Audit, or other accountable functions |
| Lifecycle stage | Idea, intake, pilot, development, validation, pre-release, production, restricted, suspended, retired |
| Intended purpose | Approved purpose, decision context, expected users, beneficiaries, and affected persons |
| Prohibited or restricted purposes | Uses, populations, data, decisions, jurisdictions, or functions that are not permitted |
| Actual use | Current operational use, including deviations from approved intended purpose |
| Users | Employees, contractors, customers, public users, partners, authorities, or others |
| Affected persons | Individuals or groups materially affected, including workers, applicants, travelers, children, vulnerable persons, or protected groups |
| AI technique | Rules, machine learning, deep learning, generative AI, GPAI, agentic AI, biometric system, recommender, hybrid, other |
| System architecture | Major components, interfaces, retrieval, tools, agents, automation, fallback, and human-control points |
| Version/configuration | Production model, system, prompts, system instructions, tools, data, parameters, code, and release identifiers |
| Provider/vendor | Internal team or external supplier |
| Critical dependencies | Models, APIs, cloud services, datasets, software, open-source components, subprocessors, and infrastructure |
| Jurisdictions | Development, market placement, deployment, output use, hosting, support, and affected-person locations |
| Sector/use context | Employment, education, credit, insurance, travel, health, public services, safety, law enforcement, migration, justice, consumer, other |
| EU AI Act applicability | In scope, partially in scope, out of scope, excluded/specially treated, uncertain, pending legal review |
| Article 5 screening | No concern, potential prohibited practice, prohibited, exception analysis required |
| High-risk classification | Article 6(1)/Annex I, Article 6(2)/Annex III, Article 6(3) exception considered, not high-risk, uncertain |
| Transparency classification | Article 13, Article 26, Article 50, other notice duty, none identified, uncertain |
| GPAI status | GPAI model, GPAI model with systemic risk, downstream system using GPAI, not applicable, uncertain |
| Governance risk tier | Organization-defined risk tier, clearly separated from statutory classification |
| Data sources | Training, tuning, validation, retrieval, input, operational, monitoring, and feedback data |
| Data characteristics | Personal, special-category, biometric, confidential, copyrighted, children’s, synthetic, public, licensed, other |
| Data governance | Provenance, lineage, quality, representativeness, bias controls, retention, deletion, localization, and transfer information |
| Outputs/actions | Predictions, rankings, recommendations, content, scores, classifications, decisions, alerts, tool calls, or automated actions |
| Decision impact | Advisory, material influence, automated decision, safety-critical, rights-impacting, financial, employment, service-access, other |
| Human oversight | Reviewer, competence, authority, override, stop, appeal, escalation, fallback, and staffing requirements |
| Required assessments | Applicability, role, prohibited practice, high-risk, FRIA, DPIA, security, data, vendor, conformity, transparency, substantial modification, other |
| Technical documentation | Index, owner, location, version, status, and applicable Annex IV mapping |
| Conformity/registration | Route, notified-body involvement, declaration, CE marking, registration, status, and evidence where applicable |
| Transparency duties | Notices, labels, instructions, disclosures, machine-readable markings, languages, and accessibility |
| Monitoring | Performance, accuracy, drift, subgroup outcomes, bias, security, robustness, incidents, complaints, overrides, and thresholds |
| Incident/notification duties | Serious-incident, corrective-action, privacy, cybersecurity, product, employment, consumer, or sector reporting considerations |
| Change triggers | Model, version, purpose, data, supplier, population, jurisdiction, interface, capability, or legal change |
| Evidence location | System of record and version-linked repository |
| Retention | Applicable statutory, contractual, operational, and legal-hold requirements |
| Application dates | Provision-specific effective dates and transitional rules |
| Approval/status | Approved, conditional, restricted, suspended, rejected, retired |
| Open findings | Material deficiencies, exceptions, conditions, remediation, and due dates |
| Review history | Last review, next review, trigger, reviewer, decision, and rationale |

## Minimum control requirements

- Assign accountable business, technical, and control owners.
- Record material production systems, pilots, proofs of concept, embedded AI features, GPAI integrations, and externally supplied AI.
- Reconcile the inventory with procurement, finance, cloud, software, data, security, HR, product, legal, and vendor records.
- Link each entry to applicability, role, classification, risk, vendor, assessment, control, evidence, and approval records.
- Distinguish actual operation from intended purpose and record unauthorized or shadow-AI use.
- Preserve historical versions, role and classification decisions, restrictions, suspensions, substantial-modification reviews, and retirement evidence.
- Reassess after intended-purpose, actor-role, version, model, data, supplier, population, jurisdiction, incident, complaint, or legal change.
- Escalate ownerless, undocumented, prohibited, or materially uncertain systems according to severity.
- Current consolidated official legal texts control over older summaries.

## Inventory quality checks

Confirm periodically that:

1. every material AI system and GPAI integration has a unique record;
2. production versions match approved documentation;
3. owners, suppliers, jurisdictions, and lifecycle status are current;
4. statutory classification and internal governance tier are not conflated;
5. required assessments and approvals are complete or explicitly pending;
6. evidence links are accessible, version-matched, and retained;
7. suspended and retired systems cannot continue unauthorized operation;
8. material changes trigger reassessment and approval.

## GlobalWay Travel Services example

GlobalWay records its traveler chatbot, recruitment-screening system, fraud model, disruption assistant, pricing model, and employee productivity tools. The inventory identifies a third-party GPAI model used in two systems, links each deployment to the correct legal entity and jurisdiction, records human-oversight and transparency controls, and flags one recruitment-system supplier update for substantial-modification and high-risk reassessment.

## Certification

| Role | Name | Decision | Date |
|---|---|---|---|
| Business owner | | | |
| Technical owner | | | |
| Legal/Compliance reviewer | | | |
| Privacy/Security/Data reviewer, where applicable | | | |

**Evidence references:**  
**Conditions or exceptions:**  
**Open findings and due dates:**  
**Next review trigger/date:**  
**Record version:**  

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable definitions, territorial scope, actor roles, prohibited practices, high-risk classification, GPAI, transparency, registration, documentation, monitoring, incident, and authority-access provisions.
- Regulation (EU) 2026/1744 where applicable.
- Regulation (EU) 2016/679 and applicable employment, consumer-protection, cybersecurity, product-safety, accessibility, equality, records-management, and sector law.
- The inventory fields in this template are governance controls unless a specific legal duty makes a field or record mandatory.