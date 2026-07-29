**NIST RISK MANAGEMENT FRAMEWORK**

**AND SP 800-53 RELEASE 5.2.0**

Practical Manager and Junior Analyst Manual

| **What this manual does:** Explains the seven RMF steps, all 20 SP 800-53 control families, baselines, tailoring, implementation, assessment, authorization, monitoring, OSCAL, open-source tools, management decisions, and job-ready analyst work. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Alberto (Al) Leiva**

First Edition • July 2026

# Preface

The Risk Management Framework is a disciplined way to connect mission needs, system design, security, privacy, evidence, and accountable risk decisions throughout a system life cycle. SP 800-53 is the control catalog used within that process; it is not a checklist that automatically creates security or an authorization.

This manual uses plain language, realistic workpapers, and safe labs. Federal terms are explained, but nonfederal organizations can adapt the concepts. Requirements and authority vary by law, agency, contract, sector, system, and risk. Use current official sources and qualified security, privacy, engineering, legal, acquisition, audit, and authorizing professionals for real decisions.

| **Current-information note:** Verified July 14, 2026: SP 800-37 Rev. 2 remains the current final RMF; SP 800-53 and SP 800-53A are at Release 5.2.0 (August 2025); SP 800-53B baselines were reissued without baseline changes; SP 800-18 Rev. 2 was finalized June 30, 2026. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## How to use this manual

- Managers: begin with Chapters 1–4, 7–13, 17–18, and 27.

- Junior analysts: study in order, practice Chapters 26 and 28–29, and use the templates.

- System owners and engineers: focus on boundary, selection, implementation, evidence, monitoring, and family chapters.

- Assessors: focus on Chapters 10, 15–18, 25, and 30.

- Tailor every artifact to the organization’s authority, risk tolerance, system, and obligations.

# Table of Contents

This document contains a native Word table of contents and a permanent chapter guide.

[Preface [2](#preface)](#preface)

[How to use this manual [2](#how-to-use-this-manual)](#how-to-use-this-manual)

[Table of Contents [3](#table-of-contents)](#table-of-contents)

[Chapter Guide [7](#chapter-guide)](#chapter-guide)

[1. RMF and SP 800-53 Foundations [8](#rmf-and-sp-800-53-foundations)](#rmf-and-sp-800-53-foundations)

[2. Current NIST Publication Suite [9](#current-nist-publication-suite)](#current-nist-publication-suite)

[3. Governance, Roles, and Risk Decisions [10](#governance-roles-and-risk-decisions)](#governance-roles-and-risk-decisions)

[4. System Life Cycle, Scope, and Authorization Boundary [11](#system-life-cycle-scope-and-authorization-boundary)](#system-life-cycle-scope-and-authorization-boundary)

[4.1 Boundary questions [11](#boundary-questions)](#boundary-questions)

[5. Prepare at the Organization Level [12](#prepare-at-the-organization-level)](#prepare-at-the-organization-level)

[5.1 Organization preparation [12](#organization-preparation)](#organization-preparation)

[6. Prepare at the System Level [13](#prepare-at-the-system-level)](#prepare-at-the-system-level)

[6.1 System preparation [13](#system-preparation)](#system-preparation)

[7. Categorize the System [14](#categorize-the-system)](#categorize-the-system)

[7.1 Method [14](#method)](#method)

[8. Select Controls [15](#select-controls)](#select-controls)

[8.1 Selection sequence [15](#selection-sequence)](#selection-sequence)

[9. Implement Controls [16](#implement-controls)](#implement-controls)

[9.1 Implementation workflow [16](#implementation-workflow)](#implementation-workflow)

[10. Assess Controls [17](#assess-controls)](#assess-controls)

[10.1 Assessment sequence [17](#assessment-sequence)](#assessment-sequence)

[11. Authorize the System or Common Controls [18](#authorize-the-system-or-common-controls)](#authorize-the-system-or-common-controls)

[11.1 Authorization package [18](#authorization-package)](#authorization-package)

[12. Monitor Continuously [19](#monitor-continuously)](#monitor-continuously)

[12.1 Monitoring activities [19](#monitoring-activities)](#monitoring-activities)

[13. Control Baselines and Tailoring [20](#control-baselines-and-tailoring)](#control-baselines-and-tailoring)

[13.1 Tailoring record [20](#tailoring-record)](#tailoring-record)

[14. Common, Hybrid, and System-Specific Controls [21](#common-hybrid-and-system-specific-controls)](#common-hybrid-and-system-specific-controls)

[14.1 Inheritance checks [21](#inheritance-checks)](#inheritance-checks)

[15. Writing Strong Implementation Statements [22](#writing-strong-implementation-statements)](#writing-strong-implementation-statements)

[15.1 Statement checklist [22](#statement-checklist)](#statement-checklist)

[16. Assessment Planning and Evidence [23](#assessment-planning-and-evidence)](#assessment-planning-and-evidence)

[16.1 Population and sampling [23](#population-and-sampling)](#population-and-sampling)

[17. Authorization Package and POA&M [24](#authorization-package-and-poam)](#authorization-package-and-poam)

[17.1 POA&M quality [24](#poam-quality)](#poam-quality)

[18. Continuous Monitoring Strategy [25](#continuous-monitoring-strategy)](#continuous-monitoring-strategy)

[19. OSCAL and Automation [26](#oscal-and-automation)](#oscal-and-automation)

[19.1 Automation safeguards [26](#automation-safeguards)](#automation-safeguards)

[20. Control Families: Access, Awareness, Audit, and Assessment [27](#control-families-access-awareness-audit-and-assessment)](#control-families-access-awareness-audit-and-assessment)

[AC — Access Control [27](#ac-access-control)](#ac-access-control)

[AT — Awareness and Training [27](#at-awareness-and-training)](#at-awareness-and-training)

[AU — Audit and Accountability [27](#au-audit-and-accountability)](#au-audit-and-accountability)

[CA — Assessment, Authorization, and Monitoring [27](#ca-assessment-authorization-and-monitoring)](#ca-assessment-authorization-and-monitoring)

[21. Control Families: Configuration, Contingency, Identity, Incident, and Maintenance [28](#control-families-configuration-contingency-identity-incident-and-maintenance)](#control-families-configuration-contingency-identity-incident-and-maintenance)

[CM — Configuration Management [28](#cm-configuration-management)](#cm-configuration-management)

[CP — Contingency Planning [28](#cp-contingency-planning)](#cp-contingency-planning)

[IA — Identification and Authentication [28](#ia-identification-and-authentication)](#ia-identification-and-authentication)

[IR — Incident Response [28](#ir-incident-response)](#ir-incident-response)

[MA — Maintenance [28](#ma-maintenance)](#ma-maintenance)

[22. Control Families: Media, Physical, Planning, Program, and Personnel [30](#control-families-media-physical-planning-program-and-personnel)](#control-families-media-physical-planning-program-and-personnel)

[MP — Media Protection [30](#mp-media-protection)](#mp-media-protection)

[PE — Physical and Environmental Protection [30](#pe-physical-and-environmental-protection)](#pe-physical-and-environmental-protection)

[PL — Planning [30](#pl-planning)](#pl-planning)

[PM — Program Management [30](#pm-program-management)](#pm-program-management)

[PS — Personnel Security [30](#ps-personnel-security)](#ps-personnel-security)

[23. Control Families: Privacy, Risk, Acquisition, Communications, Integrity, and Supply Chain [32](#control-families-privacy-risk-acquisition-communications-integrity-and-supply-chain)](#control-families-privacy-risk-acquisition-communications-integrity-and-supply-chain)

[PT — PII Processing and Transparency [32](#pt-pii-processing-and-transparency)](#pt-pii-processing-and-transparency)

[RA — Risk Assessment [32](#ra-risk-assessment)](#ra-risk-assessment)

[SA — System and Services Acquisition [32](#sa-system-and-services-acquisition)](#sa-system-and-services-acquisition)

[SC — System and Communications Protection [32](#sc-system-and-communications-protection)](#sc-system-and-communications-protection)

[SI — System and Information Integrity [32](#si-system-and-information-integrity)](#si-system-and-information-integrity)

[SR — Supply Chain Risk Management [33](#sr-supply-chain-risk-management)](#sr-supply-chain-risk-management)

[24. Privacy Risk and Security–Privacy Collaboration [34](#privacy-risk-and-securityprivacy-collaboration)](#privacy-risk-and-securityprivacy-collaboration)

[24.1 Collaboration [34](#collaboration)](#collaboration)

[25. Software Updates, Patch Reliability, and Release 5.2.0 [35](#software-updates-patch-reliability-and-release-5.2.0)](#software-updates-patch-reliability-and-release-5.2.0)

[25.1 Evidence focus [35](#evidence-focus)](#evidence-focus)

[26. Open-Source Tools and Official Resources [36](#open-source-tools-and-official-resources)](#open-source-tools-and-official-resources)

[26.1 NIST CPRT [36](#nist-cprt)](#nist-cprt)

[26.2 NIST OSCAL Content [36](#nist-oscal-content)](#nist-oscal-content)

[26.3 Compliance Trestle [37](#compliance-trestle)](#compliance-trestle)

[26.4 Lula [37](#lula)](#lula)

[26.5 CISO Assistant [37](#ciso-assistant)](#ciso-assistant)

[26.6 Heimdall [37](#heimdall)](#heimdall)

[26.7 OpenControl [37](#opencontrol)](#opencontrol)

[26.8 OSCAL CLI [38](#oscal-cli)](#oscal-cli)

[26.9 Wazuh [38](#wazuh)](#wazuh)

[26.10 OpenSCAP [38](#openscap)](#openscap)

[26.11 osquery [38](#osquery)](#osquery)

[26.12 Nmap [38](#nmap)](#nmap)

[26.13 Greenbone Community Edition [39](#greenbone-community-edition)](#greenbone-community-edition)

[26.14 Trivy [39](#trivy)](#trivy)

[26.15 OWASP ZAP [39](#owasp-zap)](#owasp-zap)

[26.16 Keycloak [39](#keycloak)](#keycloak)

[26.17 DefectDojo [40](#defectdojo)](#defectdojo)

[26.18 Open Policy Agent [40](#open-policy-agent)](#open-policy-agent)

[27. Manager’s RMF Playbook [41](#managers-rmf-playbook)](#managers-rmf-playbook)

[27.1 Manager rhythm [41](#manager-rhythm)](#manager-rhythm)

[28. Junior Analyst Career Guide [42](#junior-analyst-career-guide)](#junior-analyst-career-guide)

[28.1 Common roles [42](#common-roles)](#common-roles)

[28.2 Typical work [42](#typical-work)](#typical-work)

[29. Fictional Laboratory, Thirty-Day Plan, and Interview Preparation [44](#fictional-laboratory-thirty-day-plan-and-interview-preparation)](#fictional-laboratory-thirty-day-plan-and-interview-preparation)

[29.1 Portfolio lab [44](#portfolio-lab)](#portfolio-lab)

[29.2 Thirty-day plan [44](#thirty-day-plan)](#thirty-day-plan)

[29.3 What is RMF? [44](#what-is-rmf)](#what-is-rmf)

[29.4 Is SP 800-53 a checklist? [45](#is-sp-800-53-a-checklist)](#is-sp-800-53-a-checklist)

[29.5 What is a baseline? [45](#what-is-a-baseline)](#what-is-a-baseline)

[29.6 What is tailoring? [45](#what-is-tailoring)](#what-is-tailoring)

[29.7 What is control inheritance? [45](#what-is-control-inheritance)](#what-is-control-inheritance)

[29.8 How do you assess a control? [45](#how-do-you-assess-a-control)](#how-do-you-assess-a-control)

[29.9 What is authorization? [45](#what-is-authorization)](#what-is-authorization)

[29.10 What is a POA&M? [45](#what-is-a-poam)](#what-is-a-poam)

[29.11 What is OSCAL? [45](#what-is-oscal)](#what-is-oscal)

[29.12 What is current SP 800-53? [45](#what-is-current-sp-800-53)](#what-is-current-sp-800-53)

[30. Templates, Glossary, Index, and References [46](#templates-glossary-index-and-references)](#templates-glossary-index-and-references)

[30.1 System and boundary record [46](#system-and-boundary-record)](#system-and-boundary-record)

[30.2 Control implementation workpaper [46](#control-implementation-workpaper)](#control-implementation-workpaper)

[30.3 Assessment and finding record [46](#assessment-and-finding-record)](#assessment-and-finding-record)

[30.4 Authorization and monitoring record [46](#authorization-and-monitoring-record)](#authorization-and-monitoring-record)

[30.5 Glossary [47](#glossary)](#glossary)

[30.6 Subject index [47](#subject-index)](#subject-index)

[30.7 Official references [47](#official-references)](#official-references)

# Chapter Guide

| **Chapter** | **Title**                                                                                 | **Starts on page** |
|-------------|-------------------------------------------------------------------------------------------|--------------------|
| 1           | RMF and SP 800-53 Foundations                                                             | 5                  |
| 2           | Current NIST Publication Suite                                                            | 6                  |
| 3           | Governance, Roles, and Risk Decisions                                                     | 7                  |
| 4           | System Life Cycle, Scope, and Authorization Boundary                                      | 8                  |
| 5           | Prepare at the Organization Level                                                         | 9                  |
| 6           | Prepare at the System Level                                                               | 10                 |
| 7           | Categorize the System                                                                     | 11                 |
| 8           | Select Controls                                                                           | 12                 |
| 9           | Implement Controls                                                                        | 13                 |
| 10          | Assess Controls                                                                           | 14                 |
| 11          | Authorize the System or Common Controls                                                   | 15                 |
| 12          | Monitor Continuously                                                                      | 17                 |
| 13          | Control Baselines and Tailoring                                                           | 18                 |
| 14          | Common, Hybrid, and System-Specific Controls                                              | 19                 |
| 15          | Writing Strong Implementation Statements                                                  | 20                 |
| 16          | Assessment Planning and Evidence                                                          | 21                 |
| 17          | Authorization Package and POA&M                                                           | 22                 |
| 18          | Continuous Monitoring Strategy                                                            | 23                 |
| 19          | OSCAL and Automation                                                                      | 24                 |
| 20          | Control Families: Access, Awareness, Audit, and Assessment                                | 25                 |
| 21          | Control Families: Configuration, Contingency, Identity, Incident, and Maintenance         | 27                 |
| 22          | Control Families: Media, Physical, Planning, Program, and Personnel                       | 29                 |
| 23          | Control Families: Privacy, Risk, Acquisition, Communications, Integrity, and Supply Chain | 31                 |
| 24          | Privacy Risk and Security–Privacy Collaboration                                           | 33                 |
| 25          | Software Updates, Patch Reliability, and Release 5.2.0                                    | 34                 |
| 26          | Open-Source Tools and Official Resources                                                  | 35                 |
| 27          | Manager’s RMF Playbook                                                                    | 40                 |
| 28          | Junior Analyst Career Guide                                                               | 41                 |
| 29          | Fictional Laboratory, Thirty-Day Plan, and Interview Preparation                          | 43                 |
| 30          | Templates, Glossary, Index, and References                                                | 46                 |

# 1. RMF and SP 800-53 Foundations

*RMF manages security and privacy risk through accountable life-cycle decisions.*

<img src="media/image1.png" style="width:6.15in;height:3.39605in" alt="Prepare supports every step, and Monitor feeds new information back into risk decisions." />

Figure 1. Seven RMF steps

| **Item**              | **Purpose**                                                                | **Not the same as**                 |
|-----------------------|----------------------------------------------------------------------------|-------------------------------------|
| RMF                   | Process for organization and system risk management                        | A control catalog or certification  |
| SP 800-53             | Flexible security and privacy control catalog                              | A universal checklist or baseline   |
| SP 800-53B            | Federal low, moderate, high, and privacy baselines plus tailoring guidance | A final tailored control set        |
| SP 800-53A            | Assessment methodology and procedures                                      | Automatic proof of effectiveness    |
| Authorization         | Senior official’s risk decision based on an evidence package               | Statement that no risk remains      |
| Continuous monitoring | Ongoing awareness of controls, change, and risk                            | A dashboard without decision action |

| **Core idea:** Controls reduce risk only when they are correctly selected, implemented, operated, assessed, corrected, and monitored in the real system context. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# 2. Current NIST Publication Suite

*Use the current official source and understand how each publication supports the whole.*

| **Publication/resource** | **Current use**                                                                                |
|--------------------------|------------------------------------------------------------------------------------------------|
| SP 800-37 Rev. 2         | Seven-step RMF tasks, roles, organization/system preparation, and life-cycle risk management   |
| SP 800-53 Release 5.2.0  | Current security and privacy control catalog, including 2025 software update and patch changes |
| SP 800-53A Release 5.2.0 | Current assessment procedures corresponding to Release 5.2.0                                   |
| SP 800-53B Release 5.2.0 | Federal low/moderate/high and privacy baselines; 2025 reissue made no baseline changes         |
| SP 800-18 Rev. 2         | June 2026 system security, privacy, and C-SCRM plan elements; machine-readable emphasis        |
| SP 800-30 Rev. 1         | Risk assessment guidance                                                                       |
| SP 800-39                | Organization-wide risk management at three levels                                              |
| CPRT                     | Browser and downloads for current controls, baselines, procedures, and references              |
| OSCAL                    | Machine-readable models for catalogs, profiles, components, SSPs, assessments, and POA&Ms      |

| **Version control:** Record the source publication, release, format, retrieval date, profile/baseline version, and local tailoring. Never mix control text, procedures, and baselines from different releases without analysis. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# 3. Governance, Roles, and Risk Decisions

*RMF roles separate implementation, assessment, ownership, and risk acceptance.*

<img src="media/image2.png" style="width:6.15in;height:3.39605in" alt="Enterprise direction, mission/business needs, and system controls must stay connected." />

Figure 2. Three risk-management levels

| **Role**                                         | **Primary responsibility**                                                     |
|--------------------------------------------------|--------------------------------------------------------------------------------|
| Head of agency / organization                    | Organization-wide accountability and risk governance                           |
| Risk executive (function)                        | Consistent risk perspective and portfolio-level coordination                   |
| Authorizing official                             | Accepts system/common-control risk or imposes conditions/denies authorization  |
| Authorization official designated representative | Coordinates activities as delegated; does not inherit ungranted risk authority |
| System owner                                     | System mission, resources, plans, controls, package, and operation             |
| Information owner / steward                      | Information requirements, impact, use, sharing, and protection                 |
| Security / privacy officers                      | Program requirements, advice, oversight, and coordination                      |
| Control provider                                 | Implements and documents common, hybrid, or system-specific controls           |
| Control assessor                                 | Plans and performs objective assessment; reports results and limits            |
| System administrator / engineer                  | Builds, configures, operates, monitors, and corrects system capabilities       |
| Enterprise architect / mission owner             | Aligns systems, processes, dependencies, and organization architecture         |

# 4. System Life Cycle, Scope, and Authorization Boundary

*A clear boundary is the foundation for categorization, controls, assessment, and authorization.*

## 4.1 Boundary questions

- What mission or business function does the system support?

- Which people, processes, applications, services, devices, networks, data, interfaces, locations, cloud resources, operational technology, and suppliers belong inside?

- What is outside but connected, inherited, relied upon, or managed through an agreement?

- Where are trust boundaries, authorization boundaries, data flows, administrative paths, and external services?

- Who owns each component and control responsibility?

- Which changes require recategorization, reselection, reassessment, or authorization review?

| **Boundary artifact**     | **What it should show**                                                          |
|---------------------------|----------------------------------------------------------------------------------|
| System description        | Purpose, users, environment, operating status, technologies, dependencies        |
| Architecture diagram      | Components, zones, interfaces, trust boundaries, management paths                |
| Data flow                 | Information types, sources, destinations, processing, storage, sharing, disposal |
| Inventory                 | Hardware, software, firmware, virtual/cloud resources, owners, versions          |
| Interconnection agreement | Systems, data, controls, responsibilities, monitoring, incident and termination  |
| Control allocation        | Common, hybrid, system-specific, inherited, provider, customer responsibilities  |

# 5. Prepare at the Organization Level

*Organization-level preparation makes system RMF work consistently and efficiently.*

## 5.1 Organization preparation

- Establish risk-management roles, strategy, risk tolerance, priorities, and communication.

- Identify missions, business processes, legal/policy/contract requirements, stakeholders, and critical assets.

- Develop enterprise architecture, security/privacy architecture, common controls, organization-wide requirements, and monitoring strategy.

- Establish impact guidance, baseline tailoring rules, parameter values, overlays, assessment expectations, and authorization approach.

- Identify supply-chain risks, external providers, organization-wide threats, assumptions, and dependencies.

- Create repositories, automation, templates, evidence standards, quality review, metrics, and improvement processes.

| **Efficiency principle:** Reusable common controls, approved parameters, standard evidence, and machine-readable content reduce repeated system work—only when ownership and current operating evidence are reliable. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# 6. Prepare at the System Level

*System-level preparation defines the specific mission, stakeholders, boundary, information, and approach.*

## 6.1 System preparation

- Identify mission/business purpose, system owner, authorizing official, security/privacy officers, assessors, providers, users, and stakeholders.

- Define authorization boundary, system elements, operating environment, dependencies, interfaces, external services, and supply chain.

- Identify information types, processing purposes, privacy risks, data flows, and legal/contractual requirements.

- Determine life-cycle stage, development/acquisition approach, architecture, engineering needs, and planned authorization strategy.

- Register the system; identify common-control inheritance and organization-provided resources.

- Document assumptions, constraints, risks, required decisions, and package schedule.

# 7. Categorize the System

*Categorization describes the potential impact of the loss of confidentiality, integrity, or availability.*

<img src="media/image3.png" style="width:6.15in;height:3.39605in" alt="Categorization starts with information impact and produces an approved system impact level." />

Figure 3. Categorization workflow

## 7.1 Method

- Identify all information types processed, stored, or transmitted.

- Assign potential impact—low, moderate, or high—for confidentiality, integrity, and availability using applicable guidance and mission context.

- Apply the high-water-mark concept for the system security category, then review whether aggregation, dependencies, privacy, safety, or mission effects justify adjustment under authority.

- Document rationale, assumptions, affected parties, and approval.

- Revisit when mission, data, architecture, environment, users, suppliers, or threats materially change.

| **Categorization warning:** A high-impact category does not mean controls are weak, and a low-impact category does not mean the system is secure. It expresses potential harm if security objectives are lost. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# 8. Select Controls

*Selection creates a tailored set of controls that addresses system and organizational risk.*

## 8.1 Selection sequence

- Choose the appropriate baseline or organization-defined starting profile.

- Apply scoping considerations and identify controls that are applicable, not applicable, inherited, hybrid, or system-specific.

- Assign organization-defined parameters such as frequencies, time periods, roles, technologies, and thresholds.

- Add controls or enhancements for threat, mission, privacy, supply chain, law, policy, contract, architecture, or risk.

- Use compensating controls only through approved equivalence and documented rationale.

- Develop monitoring and assessment approaches; identify implementation responsibility and evidence.

- Document the tailored set, rationale, dependencies, common controls, and residual risk.

| **Control selection is not implementation:** Selecting AC-2 does not create account management. The system must define and operate the people, process, technology, evidence, and monitoring needed for every selected requirement. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# 9. Implement Controls

*Implementation turns selected controls into real, assigned, configured, and operated safeguards.*

## 9.1 Implementation workflow

- Parse each control statement, enhancement, parameter, supplemental guidance, related controls, and allocation.

- Translate requirements into architecture, procedures, configurations, automation, training, contracts, and operating tasks.

- Assign accountable control owner and responsible implementers; identify inherited and shared portions.

- Define population, frequency, trigger, approval, exception, logging, review, metric, and evidence.

- Build and test through the system development life cycle; use configuration and change management.

- Write an accurate implementation statement that explains who does what, where, how, when, with what configuration and evidence.

- Correct design or operation gaps before formal assessment when possible.

# 10. Assess Controls

*Assessment determines whether controls are implemented correctly, operating as intended, and producing the desired outcome.*

## 10.1 Assessment sequence

- Identify assessor independence and qualifications appropriate to risk.

- Develop and approve an assessment plan with scope, controls, procedures, methods, objects, depth, coverage, schedule, rules, evidence, sampling, and safety.

- Validate system boundary, control set, implementation, populations, inherited controls, and source reliability.

- Use examine, interview, and test methods; inquiry alone usually provides weak evidence.

- Record satisfied or other-than-satisfied results with evidence, exceptions, limitations, and risk.

- Allow responsible officials to correct findings; retest corrections independently.

- Issue an assessment report that supports the authorizing official’s decision without hiding uncertainty.

| **Assessment is not a scan:** Automated results can test important conditions at scale, but assessment also requires criteria, scope, population, design, operating context, human review, limitations, and risk analysis. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# 11. Authorize the System or Common Controls

*Authorization is an explicit senior risk decision based on the package and organizational context.*

<img src="media/image4.png" style="width:6.15in;height:3.39605in" alt="The package supports an accountable decision with defined scope, conditions, duration, and monitoring." />

Figure 7. Authorization risk decision

## 11.1 Authorization package

- Security, privacy, and C-SCRM plans as applicable.

- Security and privacy assessment reports.

- Plan of action and milestones (POA&M).

- Executive summary and current risk assessment.

- Continuous monitoring strategy and significant change information.

- System description, categorization, boundary, architecture, dependencies, common-control inheritance, and agreements.

| **Possible decision**          | **Meaning**                                                                          |
|--------------------------------|--------------------------------------------------------------------------------------|
| Authorization to operate/use   | Risk accepted for defined scope, conditions, and time                                |
| Common-control authorization   | Risk decision for controls inherited by multiple systems                             |
| Authorization with conditions  | Operation allowed only with stated limits, actions, milestones, or monitoring        |
| Denial                         | Risk is not accepted; operation/use is not authorized under stated conditions        |
| Ongoing authorization approach | Frequent current evidence supports continuing risk decisions under approved criteria |

| **Not a certification:** Authorization does not mean the system is risk-free or compliant forever. It is a documented acceptance of current residual risk by an official with authority. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# 12. Monitor Continuously

*Monitor tracks controls, system changes, threat, findings, and risk after authorization.*

## 12.1 Monitoring activities

- Track system, architecture, data, mission, user, supplier, ownership, location, threat, vulnerability, and legal changes.

- Assess selected controls at approved frequencies and event triggers using current evidence.

- Monitor common controls and communicate changes to inheriting systems.

- Update plans, inventories, diagrams, assessment results, risk register, and POA&M.

- Report posture and material change to system owners, risk executives, security/privacy officials, and authorizing officials.

- Correct weaknesses, retest, and determine whether significant change or increased risk requires reauthorization or changed terms.

| **Monitor for decisions:** Collect only evidence that has an owner, purpose, quality rule, threshold, review cadence, escalation, and response. More dashboards do not automatically improve risk management. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# 13. Control Baselines and Tailoring

*Baselines are starting points; tailoring makes them appropriate and defensible.*

<img src="media/image5.png" style="width:6.15in;height:3.39605in" alt="Tailoring changes a starting baseline into a documented, risk-based control set." />

Figure 4. Control tailoring

| **Baseline** | **Purpose**                                                                                  |
|--------------|----------------------------------------------------------------------------------------------|
| Low          | Starting security controls for low-impact federal systems                                    |
| Moderate     | Starting security controls for moderate-impact federal systems                               |
| High         | Starting security controls for high-impact federal systems                                   |
| Privacy      | Privacy controls applied based on processing and privacy risk, not system impact level alone |

## 13.1 Tailoring record

- Baseline/profile and release used.

- Control/enhancement added, removed, specialized, inherited, or compensated.

- Scoping rationale and risk basis.

- Every organization-defined parameter and source authority.

- Common/hybrid/system-specific allocation and provider.

- Compensating-control equivalence, limitation, approval, and monitoring.

- Residual risk, approver, date, and future review trigger.

# 14. Common, Hybrid, and System-Specific Controls

*Control allocation explains who provides each control and which portion the system must implement.*

| **Type**         | **Meaning**                                                                 | **Example**                                                  |
|------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------|
| Common           | Implemented once for multiple systems; inherited under defined scope        | Enterprise personnel screening or physical facility controls |
| System-specific  | Implemented for one system                                                  | Application authorization rules                              |
| Hybrid           | Part common and part system-specific                                        | Enterprise identity service plus application role design     |
| Inherited        | System relies on an authorized control provider                             | Cloud facility/environmental protection                      |
| External service | Provider and customer responsibilities are defined by service and agreement | SaaS logging, customer SSO, provider infrastructure          |

## 14.1 Inheritance checks

- Provider, authorization status, scope, implementation, evidence, assessment, findings, changes, and expiration are known.

- The inherited control actually applies to the system’s technology, location, service, and use.

- Customer/system responsibilities are implemented and tested.

- Provider changes and weaknesses are communicated to inheriting systems.

- If the common control fails or becomes unavailable, affected systems reassess risk and response.

# 15. Writing Strong Implementation Statements

*An implementation statement must let another person understand and test the real control.*

<img src="media/image6.png" style="width:6.15in;height:3.39605in" alt="Control identifiers alone are insufficient; read requirements, parameters, discussion, and enhancements together." />

Figure 5. Control anatomy

| **Weak statement**         | **Stronger statement pattern**                                                                                                                                                                                      |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The organization uses MFA. | Identity team requires phishing-resistant MFA for named administrator roles through the approved identity service; enrollment, exceptions, and quarterly coverage review are recorded in specified systems.         |
| Logs are reviewed.         | Security operations reviews defined high-risk events continuously through the SIEM and performs documented daily review of failed administrative logons; cases and exceptions are retained for the approved period. |
| Backups are performed.     | Operations creates encrypted daily backups of listed Tier 1 databases, maintains an isolated copy, monitors failures, and performs quarterly restore tests against four-hour RTO and 30-minute RPO.                 |

## 15.1 Statement checklist

- Who owns and performs the control?

- What exact systems, accounts, data, facilities, suppliers, and population are covered?

- What process, configuration, tool, rule, and parameter implements it?

- Where does it operate and where is evidence retained?

- When/frequency/trigger and how quickly?

- How are approvals, exceptions, failures, reviews, metrics, changes, and retests handled?

- Which portion is inherited, shared, planned, not applicable, or not yet operating?

# 16. Assessment Planning and Evidence

*SP 800-53A procedures are customized into an approved assessment plan.*

<img src="media/image7.png" style="width:6.15in;height:3.39605in" alt="Methods, objects, depth, and coverage must fit the objective and risk." />

Figure 6. Assessment procedure structure

| **Element**          | **Meaning**                                                          |
|----------------------|----------------------------------------------------------------------|
| Assessment objective | What determination the procedure is designed to support              |
| Method               | Examine, interview, or test                                          |
| Object               | Specification, mechanism, activity, individual, or evidence examined |
| Depth                | Level of rigor/detail: basic, focused, or comprehensive              |
| Coverage             | Breadth or scope: basic, focused, or comprehensive                   |
| Evidence             | Reliable information supporting the determination                    |
| Result               | Satisfied or other than satisfied, with exceptions and limitations   |

## 16.1 Population and sampling

- Identify the complete population before choosing a sample.

- Validate completeness and accuracy using independent sources where possible.

- Select full-population testing when automation and risk make it practical.

- For samples, document method, period, size, strata, random/judgmental basis, and limitation.

- Expand testing when exceptions suggest a pattern or population weakness.

# 17. Authorization Package and POA&M

*The package tells the risk story from system purpose to open weakness and monitoring.*

## 17.1 POA&M quality

- Unique finding and exact control/criteria.

- Condition, affected population, evidence, date, and source.

- Risk scenario, likelihood/impact context, severity, and dependencies.

- Cause and planned corrective action—not only a symptom.

- Milestones, resources, accountable owner, scheduled completion, and interim safeguards.

- Changes, delays, approvals, residual risk, and escalation.

- Retest procedure, evidence, result, closure reviewer, and date.

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p><strong>Package question</strong></p></li>
</ul></th>
<th><ul>
<li><p><strong>Evidence</strong></p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>What is being authorized?</td>
<td>Boundary, purpose, users, information, architecture, dependencies</td>
</tr>
<tr class="even">
<td>What controls should apply?</td>
<td>Categorization, baseline, tailoring, parameters, requirements</td>
</tr>
<tr class="odd">
<td>How are controls implemented?</td>
<td>System/common-control plans, implementation statements, diagrams</td>
</tr>
<tr class="even">
<td>Do controls operate?</td>
<td>Assessment plan/report, raw support, findings, retests</td>
</tr>
<tr class="odd">
<td>What risk remains?</td>
<td>Risk assessment, exceptions, POA&amp;M, threat/change context</td>
</tr>
<tr class="even">
<td>How will risk stay visible?</td>
<td>Monitoring strategy, metrics, reporting, triggers, ownership</td>
</tr>
</tbody>
</table>

# 18. Continuous Monitoring Strategy

*A monitoring strategy defines what evidence is collected, how often, and what decision follows.*

<img src="media/image8.png" style="width:6.15in;height:3.39605in" alt="Monitoring closes the loop from change and evidence to corrected risk decisions." />

Figure 8. Continuous monitoring and response

| **Field**         | **Example decision content**                                                               |
|-------------------|--------------------------------------------------------------------------------------------|
| Control/risk      | What requirement and risk the evidence addresses                                           |
| Indicator         | Configuration, coverage, event, finding, performance, exception, or change                 |
| Source/owner      | Authoritative system and accountable data owner                                            |
| Frequency/trigger | Daily, monthly, annual, release, incident, provider change, significant change             |
| Quality           | Completeness, accuracy, timeliness, integrity, access, time synchronization                |
| Threshold         | Condition requiring review, escalation, correction, reassessment, or authorization action  |
| Audience          | Implementer, system owner, security/privacy official, risk executive, authorizing official |
| Retention         | Required history, evidence protection, and package update                                  |

# 19. OSCAL and Automation

*OSCAL supports machine-readable control, implementation, assessment, and remediation information.*

<img src="media/image9.png" style="width:6.15in;height:3.39605in" alt="OSCAL models connect what is required, how it is implemented, how it is assessed, and what remains open." />

Figure 9. OSCAL model flow

| **OSCAL model**               | **Purpose**                                                           |
|-------------------------------|-----------------------------------------------------------------------|
| Catalog                       | Structured controls, enhancements, parameters, and supporting content |
| Profile                       | Selects, modifies, and organizes controls from catalogs               |
| Component Definition          | Describes reusable control implementation capabilities                |
| System Security Plan          | Describes system and control implementation                           |
| Assessment Plan               | Defines assessment scope, subjects, tasks, methods, and schedule      |
| Assessment Results            | Records observations, risks, findings, and results                    |
| Plan of Action and Milestones | Tracks risks, findings, actions, milestones, and status               |

## 19.1 Automation safeguards

- Treat official release/tag and schema as controlled dependencies.

- Validate syntax and semantics; schema-valid data can still be factually wrong.

- Use stable identifiers and trace evidence to source systems.

- Protect sensitive system, architecture, weakness, personal, and supplier information.

- Require human review for tailoring, risk, findings, exceptions, and authorization decisions.

- Track version, change, approval, transformation, inheritance, and export history.

# 20. Control Families: Access, Awareness, Audit, and Assessment

*Four families establish who may act, how people learn, what is logged, and how assurance decisions are made.*

## AC — Access Control

Limit system and information access to authorized users, processes, devices, and permitted actions.

| **Implementation focus**                                                                                 | **Possible evidence**                                                              | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | account inventory, roles, approvals, MFA, access rules, reviews, revocations, logs | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

## AT — Awareness and Training

Build general awareness and role-specific knowledge for security and privacy responsibilities.

| **Implementation focus**                                                                                 | **Possible evidence**                                                               | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | population, curriculum, role mapping, completion, exercises, exceptions, evaluation | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

## AU — Audit and Accountability

Create, protect, review, retain, and use records that support detection, investigation, and accountability.

| **Implementation focus**                                                                                 | **Possible evidence**                                                         | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | Event list, log sources, time sync, fields, retention, access, review, alerts | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

## CA — Assessment, Authorization, and Monitoring

Assess controls, manage findings, authorize risk, and monitor security and privacy posture.

| **Implementation focus**                                                                                 | **Possible evidence**                                                         | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | Assessment plans/reports, authorizations, POA&M, monitoring strategy, results | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

# 21. Control Families: Configuration, Contingency, Identity, Incident, and Maintenance

*These families secure configuration, resilience, identity, response, and controlled maintenance.*

## CM — Configuration Management

Establish controlled baselines and manage secure configuration and change.

| **Implementation focus**                                                                                 | **Possible evidence**                                                       | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | Baselines, inventories, approvals, change tests, scans, deviations, reviews | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

## CP — Contingency Planning

Prepare, test, and maintain recovery and continuity capabilities.

| **Implementation focus**                                                                                 | **Possible evidence**                                                   | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | BIA, plans, backups, alternate processing, exercises, restores, RTO/RPO | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

## IA — Identification and Authentication

Uniquely identify and authenticate people, devices, and processes with risk-appropriate strength.

| **Implementation focus**                                                                                 | **Possible evidence**                                                                  | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | identity proofing, authenticators, MFA, federation, service identities, lifecycle logs | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

## IR — Incident Response

Prepare for, detect, analyze, contain, recover from, report, and improve after incidents.

| **Implementation focus**                                                                                 | **Possible evidence**                                                     | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | plan, roles, playbooks, cases, evidence, notification, exercises, lessons | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

## MA — Maintenance

Control system maintenance, tools, personnel, access, and remote activity.

| **Implementation focus**                                                                                 | **Possible evidence**                                                       | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | maintenance schedule, approvals, tools, sanitization, remote sessions, logs | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

# 22. Control Families: Media, Physical, Planning, Program, and Personnel

*These families protect media, facilities, plans, programs, and personnel.*

## MP — Media Protection

Protect, control, transport, sanitize, and dispose of digital and non-digital media.

| **Implementation focus**                                                                                 | **Possible evidence**                                                           | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | media inventory, access, marking, transport, encryption, sanitization, disposal | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

## PE — Physical and Environmental Protection

Protect facilities, equipment, utilities, and people from physical and environmental threats.

| **Implementation focus**                                                                                 | **Possible evidence**                                                         | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | badges, visitors, cameras, alarms, power, fire, temperature, facility reviews | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

## PL — Planning

Document system security and privacy plans, rules of behavior, architecture, and intended controls.

| **Implementation focus**                                                                                 | **Possible evidence**                                                  | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | System plans, boundary, data flows, rules, approvals, versions, review | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

## PM — Program Management

Operate organization-wide information security and privacy programs and shared governance.

| **Implementation focus**                                                                                 | **Possible evidence**                                                             | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | program plans, leaders, resources, risk strategy, metrics, enterprise inventories | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

## PS — Personnel Security

Manage personnel screening, agreements, transfers, termination, sanctions, and risk.

| **Implementation focus**                                                                                 | **Possible evidence**                                                          | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | screening, agreements, role changes, access termination, third-party personnel | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

# 23. Control Families: Privacy, Risk, Acquisition, Communications, Integrity, and Supply Chain

*These families cover PII, risk, acquisition, architecture/communications, integrity, and supply chains.*

## PT — PII Processing and Transparency

Manage processing purposes, authority, minimization, consent, notice, access, correction, and privacy accountability.

| **Implementation focus**                                                                                 | **Possible evidence**                                                                  | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | Data inventory, purpose/authority, notices, consent, minimization, rights, assessments | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

## RA — Risk Assessment

Identify threats, vulnerabilities, likelihoods, impacts, privacy issues, and risk responses.

| **Implementation focus**                                                                                 | **Possible evidence**                                                               | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | Risk assessments, vulnerability results, threat sources, impact, treatment, updates | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

## SA — System and Services Acquisition

Build security and privacy into acquisition, development, engineering, supply, and external services.

| **Implementation focus**                                                                                 | **Possible evidence**                                                                     | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | requirements, contracts, SDLC, architecture, developers, testing, SBOM, supplier evidence | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

## SC — System and Communications Protection

Protect boundaries, communications, architecture, cryptography, isolation, and shared resources.

| **Implementation focus**                                                                                 | **Possible evidence**                                                               | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | diagrams, segmentation, firewall rules, encryption, keys, protocols, boundary tests | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

## SI — System and Information Integrity

Find and correct flaws, malicious code, integrity failures, unsafe updates, and anomalous behavior.

| **Implementation focus**                                                                                 | **Possible evidence**                                                                 | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | vulnerabilities, patches, integrity validation, malware defenses, alerts, corrections | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

## SR — Supply Chain Risk Management

Manage risks from products, services, suppliers, developers, integrators, and supply-chain tiers.

| **Implementation focus**                                                                                 | **Possible evidence**                                                                 | **Analyst checks**                                                                                                |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Define scope, owner, requirements, procedures, technology, responsibilities, exceptions, and monitoring. | C-SCRM plan, supplier inventory, criticality, contracts, provenance, monitoring, exit | Match evidence to the exact control; validate population, date, configuration, operation, exceptions, and retest. |

# 24. Privacy Risk and Security–Privacy Collaboration

*Rev. 5 integrates security and privacy controls while preserving distinct objectives and risk methods.*

## 24.1 Collaboration

- Security manages risks from loss of confidentiality, integrity, and availability to operations, assets, individuals, other organizations, and the Nation.

- Privacy risk management examines problems individuals may experience from data processing, even when security controls work as designed.

- Joint controls need clear security/privacy ownership, shared implementation, evidence, assessment, findings, and risk communication.

- PT controls address PII processing and transparency; relevant controls across every family can also support privacy.

- Privacy baseline selection and tailoring depend on processing, purpose, authority, people, data, context, and privacy risk—not only FIPS impact.

| **Question**                                       | **Example artifact**                                                 |
|----------------------------------------------------|----------------------------------------------------------------------|
| Why is data processed?                             | Purpose, authority, system/privacy plan                              |
| What data and people?                              | Data inventory, information types, data flow                         |
| What problems could processing create?             | Privacy risk assessment / PIA as applicable                          |
| How is processing limited and explained?           | Minimization, notice, consent, retention, sharing, rights procedures |
| How are security and privacy controls coordinated? | Collaboration index, allocations, joint evidence and findings        |

# 25. Software Updates, Patch Reliability, and Release 5.2.0

*Release 5.2.0 strengthens software update, patch, integrity, and resilient-development coverage.*

| **Release 5.2.0 change**                                          | **Plain meaning**                                                                                                              |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| SA-15(13) — development process, standards, and tools enhancement | Adds attention to resilient software development practices related to updates and patches                                      |
| SA-24 — Design for Cyber Resiliency                               | New control emphasizing system/software design that can withstand, recover, adapt, and continue under adverse conditions       |
| SI-02(07) — flaw remediation enhancement                          | Adds requirements focused on reliable and secure software/firmware updates                                                     |
| SI-07(12) — integrity verification enhancement revision           | Revises existing integrity-related requirements                                                                                |
| Discussion / related-control updates                              | Clarifies acquisition, design, documentation, update management, integrity, monitoring, incident, and assessment relationships |
| SP 800-53A 5.2.0                                                  | Adds corresponding procedures for the new controls/enhancements                                                                |
| SP 800-53B 5.2.0                                                  | Reissued for consistency; NIST states baseline selections did not change                                                       |

## 25.1 Evidence focus

- Update origin, signing, integrity verification, protected delivery, approval, testing, rollback, failure handling, inventory, deployment coverage, monitoring, and records.

- Developer and supplier practices, build/release access, provenance, SBOM, vulnerability response, support period, end-of-life, and customer communication.

- Resilient design assumptions, adverse-condition behavior, isolation, degradation, recovery, diversity, redundancy, and exercise results.

# 26. Open-Source Tools and Official Resources

*Official resources and open-source tools can support authoring, evidence, assessment, and continuous monitoring.*

| **Resource / tool**         | **Purpose**                                                     |
|-----------------------------|-----------------------------------------------------------------|
| NIST CPRT                   | Official current controls, baselines, procedures, and downloads |
| NIST OSCAL Content          | Official machine-readable NIST control content                  |
| Compliance Trestle          | OSCAL authoring, transformation, and governance                 |
| Lula                        | Evaluate control evidence as code                               |
| CISO Assistant              | Risk, controls, evidence, assessments, and findings             |
| Heimdall                    | View and normalize security assessment results                  |
| OpenControl                 | Compliance documentation as structured text                     |
| OSCAL CLI                   | Validate and transform OSCAL content                            |
| Wazuh                       | Endpoint monitoring, file integrity, log analysis, and alerts   |
| OpenSCAP                    | Configuration and vulnerability assessment                      |
| osquery                     | Endpoint inventory and configuration queries                    |
| Nmap                        | Authorized asset and service discovery                          |
| Greenbone Community Edition | Authorized vulnerability assessment                             |
| Trivy                       | Repository, image, dependency, secret, and IaC checks           |
| OWASP ZAP                   | Authorized web application security testing                     |
| Keycloak                    | Identity, roles, MFA, sessions, and audit events                |
| DefectDojo                  | Finding aggregation, assignment, remediation, and retest        |
| Open Policy Agent           | Policy-as-code decisions                                        |

| **Authorization and limits:** Use technical tools only on systems, networks, repositories, data, and accounts you own or have written permission to test. A tool can support evidence; it cannot choose risk tolerance, approve tailoring, accept risk, or issue authorization. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## 26.1 NIST CPRT

Purpose: Official current controls, baselines, procedures, and downloads. Official project: [<u>NIST CPRT</u>](https://csrc.nist.gov/projects/cprt/catalog)

Safe quick start: Open the catalog, select SP 800-53 Release 5.2.0, review the exact control and discussion, then export an approved format and record release/date.

Retain: authority, scope, source/release, version, configuration/query, population, date, raw result, analyst validation, limitation, control mapping, finding, correction, and retest. Protect system and vulnerability information.

## 26.2 NIST OSCAL Content

Purpose: Official machine-readable NIST control content. Official project: [<u>NIST OSCAL Content</u>](https://github.com/usnistgov/oscal-content)

Safe quick start: Clone or download a tagged release, validate file identity, inspect the SP 800-53 catalog/profile, and preserve the source version.

Retain: authority, scope, source/release, version, configuration/query, population, date, raw result, analyst validation, limitation, control mapping, finding, correction, and retest. Protect system and vulnerability information.

## 26.3 Compliance Trestle

Purpose: OSCAL authoring, transformation, and governance. Official project: [<u>Compliance Trestle</u>](https://github.com/oscal-compass/compliance-trestle)

Safe quick start: Create a lab workspace, import official OSCAL, author a small profile and component definition, validate, review changes, and export.

Retain: authority, scope, source/release, version, configuration/query, population, date, raw result, analyst validation, limitation, control mapping, finding, correction, and retest. Protect system and vulnerability information.

## 26.4 Lula

Purpose: Evaluate control evidence as code. Official project: [<u>Lula</u>](https://github.com/defenseunicorns/lula)

Safe quick start: Use a lab repository, define one non-destructive validation mapped to a control, run it against synthetic or authorized data, review evidence, and version the result.

Retain: authority, scope, source/release, version, configuration/query, population, date, raw result, analyst validation, limitation, control mapping, finding, correction, and retest. Protect system and vulnerability information.

## 26.5 CISO Assistant

Purpose: Risk, controls, evidence, assessments, and findings. Official project: [<u>CISO Assistant</u>](https://intuitem.github.io/ciso-assistant-community/)

Safe quick start: Create a scoped project, load a relevant framework, assign owners, document implementation, attach evidence, assess, and track findings.

Retain: authority, scope, source/release, version, configuration/query, population, date, raw result, analyst validation, limitation, control mapping, finding, correction, and retest. Protect system and vulnerability information.

## 26.6 Heimdall

Purpose: View and normalize security assessment results. Official project: [<u>Heimdall</u>](https://github.com/mitre/heimdall2)

Safe quick start: Import an approved sample result, confirm mappings and scoring, review exceptions, restrict access, and export a sanitized report.

Retain: authority, scope, source/release, version, configuration/query, population, date, raw result, analyst validation, limitation, control mapping, finding, correction, and retest. Protect system and vulnerability information.

## 26.7 OpenControl

Purpose: Compliance documentation as structured text. Official project: [<u>OpenControl</u>](https://github.com/opencontrol)

Safe quick start: Create a lab component, map one control, write implementation details and evidence references, peer-review, and track in version control.

Retain: authority, scope, source/release, version, configuration/query, population, date, raw result, analyst validation, limitation, control mapping, finding, correction, and retest. Protect system and vulnerability information.

## 26.8 OSCAL CLI

Purpose: Validate and transform OSCAL content. Official project: [<u>OSCAL CLI</u>](https://github.com/usnistgov/oscal-cli)

Safe quick start: Validate a small lab OSCAL file, correct schema errors, transform only with approved versions, and retain validation output.

Retain: authority, scope, source/release, version, configuration/query, population, date, raw result, analyst validation, limitation, control mapping, finding, correction, and retest. Protect system and vulnerability information.

## 26.9 Wazuh

Purpose: Endpoint monitoring, file integrity, log analysis, and alerts. Official project: [<u>Wazuh</u>](https://wazuh.com/)

Safe quick start: Enroll a lab endpoint, generate a harmless event, validate collection and alerting, document coverage and limitations, and retain evidence.

Retain: authority, scope, source/release, version, configuration/query, population, date, raw result, analyst validation, limitation, control mapping, finding, correction, and retest. Protect system and vulnerability information.

## 26.10 OpenSCAP

Purpose: Configuration and vulnerability assessment. Official project: [<u>OpenSCAP</u>](https://www.open-scap.org/)

Safe quick start: Choose an applicable profile for a lab system, run an authorized scan, validate results, document tailoring, remediate, and rescan.

Retain: authority, scope, source/release, version, configuration/query, population, date, raw result, analyst validation, limitation, control mapping, finding, correction, and retest. Protect system and vulnerability information.

## 26.11 osquery

Purpose: Endpoint inventory and configuration queries. Official project: [<u>osquery</u>](https://www.osquery.io/)

Safe quick start: Run read-only lab queries, define the population, compare results to requirements, validate exceptions, and record query/version.

Retain: authority, scope, source/release, version, configuration/query, population, date, raw result, analyst validation, limitation, control mapping, finding, correction, and retest. Protect system and vulnerability information.

## 26.12 Nmap

Purpose: Authorized asset and service discovery. Official project: [<u>Nmap</u>](https://nmap.org/)

Safe quick start: Scan only written-authorized ranges with limited options, reconcile to inventory, investigate unknowns, and preserve scope and command evidence.

Retain: authority, scope, source/release, version, configuration/query, population, date, raw result, analyst validation, limitation, control mapping, finding, correction, and retest. Protect system and vulnerability information.

## 26.13 Greenbone Community Edition

Purpose: Authorized vulnerability assessment. Official project: [<u>Greenbone Community Edition</u>](https://greenbone.github.io/docs/latest/)

Safe quick start: Update feeds, define approved targets and credentials, validate coverage, review findings, correct, and rescan.

Retain: authority, scope, source/release, version, configuration/query, population, date, raw result, analyst validation, limitation, control mapping, finding, correction, and retest. Protect system and vulnerability information.

## 26.14 Trivy

Purpose: Repository, image, dependency, secret, and IaC checks. Official project: [<u>Trivy</u>](https://trivy.dev/)

Safe quick start: Scan an authorized training repository or image, validate findings, correct or document approved exceptions, and rescan in CI.

Retain: authority, scope, source/release, version, configuration/query, population, date, raw result, analyst validation, limitation, control mapping, finding, correction, and retest. Protect system and vulnerability information.

## 26.15 OWASP ZAP

Purpose: Authorized web application security testing. Official project: [<u>OWASP ZAP</u>](https://www.zaproxy.org/)

Safe quick start: Use a training application, crawl passively, use active scanning only with permission, validate findings, fix, and retest.

Retain: authority, scope, source/release, version, configuration/query, population, date, raw result, analyst validation, limitation, control mapping, finding, correction, and retest. Protect system and vulnerability information.

## 26.16 Keycloak

Purpose: Identity, roles, MFA, sessions, and audit events. Official project: [<u>Keycloak</u>](https://www.keycloak.org/)

Safe quick start: Create a lab realm, configure roles and MFA, test joiner-mover-leaver and privileged cases, and review events.

Retain: authority, scope, source/release, version, configuration/query, population, date, raw result, analyst validation, limitation, control mapping, finding, correction, and retest. Protect system and vulnerability information.

## 26.17 DefectDojo

Purpose: Finding aggregation, assignment, remediation, and retest. Official project: [<u>DefectDojo</u>](https://www.defectdojo.org/)

Safe quick start: Import safe lab findings, validate deduplication and severity, assign action, attach evidence, and close only after retest.

Retain: authority, scope, source/release, version, configuration/query, population, date, raw result, analyst validation, limitation, control mapping, finding, correction, and retest. Protect system and vulnerability information.

## 26.18 Open Policy Agent

Purpose: Policy-as-code decisions. Official project: [<u>Open Policy Agent</u>](https://www.openpolicyagent.org/)

Safe quick start: Write a small lab policy for an approved configuration rule, test allow/deny and failure cases, peer-review, log decisions, and preserve human exception authority.

Retain: authority, scope, source/release, version, configuration/query, population, date, raw result, analyst validation, limitation, control mapping, finding, correction, and retest. Protect system and vulnerability information.

# 27. Manager’s RMF Playbook

*Managers keep RMF focused on mission risk, reliable evidence, timely decisions, and correction.*

| **Area**       | **Manager question**                                                                         | **Red flag**                                |
|----------------|----------------------------------------------------------------------------------------------|---------------------------------------------|
| Boundary       | Do we know what is inside, inherited, connected, and externally provided?                    | Unknown cloud, supplier, or admin path      |
| Categorization | Does impact reflect every information type, dependency, privacy, safety, and mission effect? | Category copied from another system         |
| Selection      | Are baseline, tailoring, parameters, additions, and allocations justified?                   | Control set treated as untailored checklist |
| Implementation | Can owners explain who/what/where/how/when and show operating evidence?                      | Policy language copied as implementation    |
| Assessment     | Are scope, population, methods, independence, limitations, and retests credible?             | Scan equals assessment                      |
| Authorization  | Does the decision official understand residual risk and conditions?                          | Package hides severe/open uncertainty       |
| Monitoring     | Do changes and indicators lead to response and package updates?                              | Dashboard without accountable action        |
| POA&M          | Are severe and overdue actions funded and independently retested?                            | Repeated extensions without risk decision   |

## 27.1 Manager rhythm

- Monthly: severe findings, significant changes, overdue POA&Ms, common-control changes, monitoring thresholds, and authorization conditions.

- Quarterly: control evidence quality, vulnerability and configuration trends, supplier risks, privacy risks, recovery/incident results, and resource blockers.

- At releases or major changes: boundary, categorization, control set, assessment, and authorization impact.

- Annually or approved cycle: risk strategy, common controls, parameter values, monitoring strategy, assessor capability, package quality, metrics, and process improvement.

# 28. Junior Analyst Career Guide

*Junior RMF analysts create value through accurate boundaries, mappings, statements, evidence, findings, and tracking.*

<img src="media/image10.png" style="width:6.15in;height:3.39605in" alt="Trace every conclusion from requirement to implementation, evidence, result, risk, and action." />

Figure 10. Junior RMF analyst pathway

## 28.1 Common roles

- Junior GRC Analyst

- RMF Analyst

- Security Controls Assessor (junior)

- Information System Security Officer support

- Cybersecurity Compliance Analyst

- Security Authorization Analyst

- Privacy Controls Analyst

- Continuous Monitoring Analyst

## 28.2 Typical work

- Maintain system inventory, boundary, information types, categorizations, control allocation, evidence, findings, POA&M, and package versions.

- Read exact control text and procedures; record release and organization-defined parameters.

- Draft implementation statements and validate them with owners and evidence.

- Gather evidence securely, validate population and source quality, perform approved examine/interview/test steps, and document limitations.

- Write clear findings and track milestones through independent retest.

- Use CPRT, OSCAL, spreadsheets, repositories, dashboards, and approved technical tools without claiming authority beyond the role.

# 29. Fictional Laboratory, Thirty-Day Plan, and Interview Preparation

*A fictional system and authorized lab can become a strong entry-level portfolio.*

| **Lab rule:** Use fictional organizations, synthetic data, isolated systems, and written authorization. Never scan public targets or publish real system plans, vulnerabilities, credentials, diagrams, or assessment evidence. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## 29.1 Portfolio lab

- Create a fictional 100-person organization and a cloud-hosted customer portal with an identity provider, database, CI/CD pipeline, support supplier, and personal data.

- Define mission, stakeholders, boundary, inventory, architecture, data flow, dependencies, external services, and control allocation.

- Categorize confidentiality, integrity, and availability with documented information types and impact rationale.

- Select a moderate baseline as an educational starting point; tailor 20 representative controls and parameters with fictional risk rationale.

- Write ten strong implementation statements across different families.

- Create an assessment plan and test five controls using synthetic evidence and authorized lab tools.

- Write two findings, a POA&M, correction evidence, and retest results.

- Create a short authorization briefing and continuous monitoring strategy.

- Represent one profile, SSP fragment, assessment result, or POA&M in OSCAL and validate it.

- Publish sanitized artifacts clearly labeled fictional and not a NIST authorization.

## 29.2 Thirty-day plan

| **Days** | **Focus**                                        | **Deliverable**                            |
|----------|--------------------------------------------------|--------------------------------------------|
| 1–4      | RMF, publication suite, roles, three levels      | Concept map and RACI                       |
| 5–7      | Boundary, information, data flow, categorization | System description and category memo       |
| 8–11     | Baselines, tailoring, parameters, allocation     | Tailored representative control set        |
| 12–15    | Implementation and family study                  | Ten implementation statements              |
| 16–19    | SP 800-53A methods, populations, sampling        | Assessment plan and five workpapers        |
| 20–22    | Findings, risk, POA&M, retest                    | Two finding-to-closure records             |
| 23–25    | Authorization and monitoring                     | Executive brief and monitoring strategy    |
| 26–27    | OSCAL and approved tools                         | Validated OSCAL fragment and tool evidence |
| 28–30    | Portfolio and interview                          | Sanitized portfolio and five STAR stories  |

## 29.3 What is RMF?

A seven-step life-cycle process for managing security and privacy risk: Prepare, Categorize, Select, Implement, Assess, Authorize, and Monitor.

## 29.4 Is SP 800-53 a checklist?

No. It is a flexible control catalog. Organizations choose and tailor controls through risk management and applicable requirements.

## 29.5 What is a baseline?

A starting set of controls. SP 800-53B provides low, moderate, high, and privacy baselines for federal use.

## 29.6 What is tailoring?

Documented scoping, parameters, additions, specialization, allocation, and approved compensating controls that make the starting set fit the system and risk.

## 29.7 What is control inheritance?

A system relies on a control provided by another authorized provider, while still implementing and testing its own customer responsibilities.

## 29.8 How do you assess a control?

Use approved objectives and examine, interview, or test methods with defined objects, depth, coverage, population, evidence, exceptions, and limitations.

## 29.9 What is authorization?

An authorized senior official’s decision to accept defined residual risk for a system or common controls under stated terms.

## 29.10 What is a POA&M?

A tracked plan for correcting identified weaknesses, with risk, owner, milestones, resources, schedule, status, and retest.

## 29.11 What is OSCAL?

NIST’s machine-readable models for controls, profiles, implementations, assessments, results, and POA&Ms.

## 29.12 What is current SP 800-53?

Revision 5, Release 5.2.0, issued in August 2025.

# 30. Templates, Glossary, Index, and References

*Reusable work structures, key terms, subject index, and official sources.*

## 30.1 System and boundary record

| **Field**                   | **Entry**                                                                        |
|-----------------------------|----------------------------------------------------------------------------------|
| System/owner/mission        | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Authorization boundary      | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Information types/data flow | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Architecture/interfaces     | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| External services/suppliers | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Common controls/inheritance | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Dependencies/locations      | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Category/rationale          | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Life-cycle stage/changes    | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Approvals/version           | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |

## 30.2 Control implementation workpaper

| **Field**                   | **Entry**                                                                        |
|-----------------------------|----------------------------------------------------------------------------------|
| Control/enhancement/release | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Parameter/requirement       | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Allocation/provider         | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Scope/population            | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Who / what / where          | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| How / configuration         | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| When / trigger/frequency    | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Evidence/source/retention   | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Exception/failure/review    | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Owner/approval/update       | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |

## 30.3 Assessment and finding record

| **Field**                       | **Entry**                                                                        |
|---------------------------------|----------------------------------------------------------------------------------|
| Objective/method/object         | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Depth/coverage/period           | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Population/sample/reliability   | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Steps/tools/version             | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Evidence/result                 | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Exception / affected population | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Risk/cause                      | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Action/owner/milestones         | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Interim protection              | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Retest/closure                  | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |

## 30.4 Authorization and monitoring record

| **Field**                   | **Entry**                                                                        |
|-----------------------------|----------------------------------------------------------------------------------|
| Package/version/date        | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Residual risk summary       | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Decision/official/terms     | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Conditions/expiration       | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| POA&M / severe risks        | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Indicators/source/frequency | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Threshold/escalation        | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Significant-change triggers | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Reporting/package update    | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Reauthorization/closure     | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |

## 30.5 Glossary

| **Term**                | **Meaning**                                                                                                         |
|-------------------------|---------------------------------------------------------------------------------------------------------------------|
| Authorization           | Official acceptance of defined residual risk for a system or common controls.                                       |
| Authorization boundary  | Set of system elements included in the risk decision.                                                               |
| Baseline                | Starting control set.                                                                                               |
| Common control          | Control implemented for multiple systems.                                                                           |
| Control enhancement     | Additional or stronger requirement associated with a base control.                                                  |
| Control inheritance     | Reliance on an applicable control implemented by another provider.                                                  |
| Control parameter       | Organization-assigned value inside a control.                                                                       |
| CPRT                    | NIST Cybersecurity and Privacy Reference Tool.                                                                      |
| High-water mark         | System impact takes precedence over other applicable information/security objectives, subject to approved analysis. |
| OSCAL                   | Open Security Controls Assessment Language.                                                                         |
| POA&M                   | Plan of action and milestones for weaknesses, with corrective actions.                                              |
| Residual risk           | Risk remaining after controls and treatment.                                                                        |
| RMF                     | Risk Management Framework.                                                                                          |
| Security categorization | Potential-impact determination for confidentiality, integrity, and availability.                                    |
| System Security Plan    | Description of system and control implementation.                                                                   |
| Tailoring               | Risk-based adjustment and specification of a starting control set.                                                  |

## 30.6 Subject index

| **Subject**         | **Chapter** |
|---------------------|-------------|
| Assessment          | 10, 16–17   |
| Authorization       | 11, 17      |
| Baselines/tailoring | 13          |
| Categorization      | 7           |
| Common controls     | 14          |
| Control families    | 20–23       |
| Implementation      | 9, 15       |
| Junior analyst      | 28–29       |
| Manager             | 27          |
| Monitoring          | 12, 18      |
| OSCAL               | 19, 26      |
| POA&M               | 17, 30      |
| Privacy             | 24          |
| Release 5.2.0       | 2, 25       |
| Roles               | 3           |
| Selection           | 8           |
| System boundary     | 4           |
| Tools               | 26          |

## 30.7 Official references

- [<u>NIST Risk Management Framework</u>](https://csrc.nist.gov/projects/risk-management)

- [<u>NIST SP 800-37 Rev. 2</u>](https://csrc.nist.gov/pubs/sp/800/37/r2/final)

- [<u>NIST SP 800-53 Rev. 5 and Release 5.2.0</u>](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

- [<u>NIST SP 800-53A Rev. 5 and Release 5.2.0</u>](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final)

- [<u>NIST SP 800-53B</u>](https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final)

- [<u>NIST 2025 Release 5.2.0 announcement</u>](https://csrc.nist.gov/News/2025/nist-releases-revision-to-sp-800-53-controls)

- [<u>NIST SP 800-18 Rev. 2</u>](https://csrc.nist.gov/pubs/sp/800/18/r2/final)

- [<u>NIST SP 800-30 Rev. 1</u>](https://csrc.nist.gov/pubs/sp/800/30/r1/final)

- [<u>NIST SP 800-39</u>](https://csrc.nist.gov/pubs/sp/800/39/final)

- [<u>NIST CPRT</u>](https://csrc.nist.gov/projects/cprt/catalog)

- [<u>NIST OSCAL</u>](https://pages.nist.gov/OSCAL/)

- [<u>NIST SP 800-53 controls downloads</u>](https://csrc.nist.gov/projects/risk-management/sp800-53-controls/downloads)

- [<u>NIST RMF introductory courses</u>](https://csrc.nist.gov/projects/risk-management/rmf-courses)

| **Final reminder:** NIST releases, baselines, parameters, overlays, systems, threats, laws, contracts, tools, and organizational risk change. Confirm the current official source, local authority, and applicable requirements before implementation, assessment, or authorization. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
