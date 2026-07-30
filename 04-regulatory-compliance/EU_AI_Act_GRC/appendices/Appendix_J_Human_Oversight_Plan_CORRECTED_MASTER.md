# Appendix J — Human-Oversight Plan

> **Legal status:** Corrected English master. This file distinguishes provider design duties under Article 14 from deployer duties to assign competent natural persons and operate the system according to applicable instructions. Human oversight must be meaningful in practice and cannot be reduced to nominal approval or after-the-fact review.

## Purpose

Use this plan to define how qualified people will understand, supervise, challenge, disregard, override, interrupt, stop, suspend, and escalate the operation of an AI system.

The plan must link oversight objectives, roles, decision points, information, authority, competence, workload, fallback, evidence, testing, monitoring, and review triggers to the approved system version and intended purpose.

## 1. Applicability record

| Field | Response |
|---|---|
| System/model | |
| Version/configuration | |
| Inventory ID | |
| Legal entity and actor role | |
| High-risk classification and legal basis | |
| Intended purpose | |
| Actual or proposed use | |
| Users and affected persons | |
| Provider instructions reviewed | |
| Related FRIA/DPIA/risk assessment | |
| Current legal source and application date | |
| Plan owner/date/version | |

## 2. Oversight objectives

Define the risks oversight is intended to prevent or reduce, including:

- unsafe or unlawful outcomes;
- automation bias and over-reliance;
- inaccurate, unreliable, discriminatory, or manipulated outputs;
- use outside intended purpose or approved population;
- failure to recognize uncertainty, abnormal behaviour, drift, or model limitations;
- inappropriate autonomous action or tool use;
- delayed incident, complaint, or escalation response;
- inability of affected persons to obtain human review, correction, appeal, or remedy;
- inadequate fallback during outages, attacks, supplier failures, or unexpected conditions.

## 3. Provider-designed oversight measures

Record design capabilities enabling natural persons to:

- understand relevant capacities, limitations, assumptions, and foreseeable misuse;
- remain aware of automation bias and performance limits;
- correctly interpret outputs in context;
- access relevant inputs, source information, confidence or uncertainty indicators where meaningful, and prior actions;
- disregard, override, reverse, or correct outputs;
- prevent or approve external actions;
- interrupt or stop operation safely;
- detect anomalies, drift, misuse, and abnormal conditions;
- escalate incidents, rights concerns, safety risks, and control failures;
- use logs, explanations, version information, and evidence needed for review.

| Measure | Design owner | System feature or procedure | Version | Test evidence | Limitation |
|---|---|---|---|---|---|
| | | | | | |

## 4. Deployer operating model

| Role | Responsibilities | Decision authority | Required competence | Workload/time | Backup | Escalation route |
|---|---|---|---|---|---|---|
| | | | | | | |

Confirm that oversight personnel:

- are natural persons;
- have the necessary competence, training, authority, independence, time, tools, and support;
- understand the intended purpose, instructions, limitations, and relevant risks;
- can override or stop the system without retaliation or conflicting performance pressure;
- have access to specialists and emergency contacts;
- are not assigned workloads that make meaningful review impossible;
- are supported by alternates and continuity arrangements.

## 5. Decision points and interventions

| Lifecycle/process step | AI output or action | Human review required | Information available | Override/stop method | Escalation threshold | Evidence created |
|---|---|---|---|---|---|---|
| | | | | | | |

Include pre-release approval, real-time operation, exceptions, appeals, incident response, rollback, restoration, and retirement where applicable.

## 6. Information available to reviewers

Confirm reviewers receive:

- intended purpose, approved use, and prohibited or restricted use;
- input and output context;
- relevant source, retrieval, tool, and action information;
- confidence, uncertainty, abstention, or warning indicators where meaningful;
- known accuracy, bias, subgroup, language, accessibility, security, and robustness limitations;
- applicable legal, policy, and decision criteria;
- prior overrides, disagreements, incidents, complaints, and appeals;
- instructions for challenge, correction, override, suspension, stop, escalation, and fallback;
- version and change information;
- contact and support routes.

## 7. Authority, independence, and incentives

Document whether reviewers can:

- disregard, reverse, or correct the output;
- require additional evidence or a second review;
- defer or refuse a decision;
- obtain legal, technical, clinical, HR, safety, or domain advice;
- stop, suspend, roll back, or isolate the system;
- escalate without retaliation;
- record dissent and unresolved uncertainty;
- protect affected persons while investigation proceeds.

Assess whether production targets, speed metrics, staffing, incentives, or management pressure undermine meaningful review.

## 8. Automation-bias controls

Use proportionate controls such as:

- independent analysis before displaying the AI recommendation;
- staged presentation of source evidence and AI output;
- mandatory rationale for acceptance and override in material decisions;
- randomized quality review;
- reviewer rotation and second-level review;
- alerts for unusually high acceptance or low override rates;
- scenario-based training and challenge exercises;
- separation of production targets from oversight-quality measures;
- monitoring of disagreement, appeal, and reversal patterns;
- periodic blind testing of reviewer judgment.

## 9. Competence and training

| Training/competence topic | Audience | Frequency | Completion evidence | Competence test | Refresher trigger |
|---|---|---|---|---|---|
| Intended purpose and limitations | | | | | |
| Interpretation and uncertainty | | | | | |
| Automation bias | | | | | |
| Rights, safety, privacy, and discrimination risks | | | | | |
| Override, stop, fallback, and escalation | | | | | |
| Incident and evidence preservation | | | | | |
| Accessibility and affected-person communication | | | | | |

Training completion alone does not demonstrate competence. Use observation, simulation, testing, and performance evidence.

## 10. Override and escalation procedure

1. Identify the questionable output, action, or operating condition.
2. Prevent or contain immediate harm and use approved fallback where needed.
3. Preserve relevant inputs, outputs, prompts, tools, versions, logs, decisions, and context.
4. Apply the approved alternative or manual process.
5. Record the reviewer’s decision, evidence, rationale, and uncertainty.
6. Notify affected persons or responsible functions where required.
7. Escalate material, repeated, systemic, legal, safety, rights, or security issues.
8. Trigger incident, risk, change, supplier, notification, or corrective-action processes where required.
9. Validate remediation and restoration before normal operation resumes.
10. Communicate outcomes and lessons learned.

## 11. Validation

Test:

- reviewer comprehension of system purpose and limitations;
- access to required information;
- authority to disregard, override, interrupt, stop, and escalate;
- technical effectiveness of override and stop mechanisms;
- manual fallback and continuity;
- workload, staffing, fatigue, and response time;
- resistance to automation bias and management pressure;
- language and accessibility support;
- detection of abnormal conditions, misuse, drift, and uncertainty;
- escalation and incident-response effectiveness;
- evidence creation and retrievability.

| Test scenario | Acceptance criterion | Result | Defect | Owner | Retest evidence |
|---|---|---|---|---|---|
| | | | | | |

## 12. Monitoring

Track:

- acceptance, override, correction, and reversal rates;
- reviewer disagreement and second-review outcomes;
- time to review and escalation;
- unusually high reliance or low challenge rates;
- quality defects, false positives, false negatives, and abstentions;
- subgroup, language, disability, and accessibility differences;
- complaints, appeals, remedies, and affected-person outcomes;
- reviewer workload, fatigue, turnover, and staffing gaps;
- training and competence status;
- failed interventions, stop failures, and fallback failures;
- repeat issues after corrective action.

| Indicator | Threshold | Source | Frequency | Owner | Required action |
|---|---|---|---|---|---|
| | | | | | |

## 13. Failure and fallback

Document:

- safe suspension and stop criteria;
- manual or alternative process;
- emergency and specialist contacts;
- continuity, recovery, and restoration arrangements;
- evidence preservation;
- communication to affected persons, customers, workers, or authorities;
- restrictions during degraded operation;
- approval and validation required before restoration.

## 14. Decision

- [ ] Oversight design and operating model approved
- [ ] Approved with conditions
- [ ] Restricted pilot only
- [ ] Remediation and retesting required
- [ ] Deployment blocked or suspended
- [ ] Qualified legal or specialist review required

**Decision rationale:**  
**Residual limitations:**  
**Conditions and restrictions:**  
**Open actions and due dates:**  

## 15. Review triggers

Reassess after:

- model, data, prompt, tool, agent, interface, threshold, or workflow change;
- intended-purpose, population, jurisdiction, or automation change;
- provider instruction or supplier change;
- staffing, workload, competence, incentive, or authority change;
- incident, complaint, appeal, adverse outcome, or failed intervention;
- performance, bias, language, accessibility, or security drift;
- substantial modification, reclassification, or legal change.

## GlobalWay Travel Services example

GlobalWay’s traveler-disruption assistant recommends rebooking and refund actions. The oversight plan requires a travel consultant to confirm safety-sensitive changes and all external financial actions. Consultants receive itinerary context, supplier rules, uncertainty warnings, and prior tool actions. Monitoring detects unusually high acceptance rates during severe weather. GlobalWay reduces workload, adds independent review for high-impact actions, retrains staff, and blocks automatic execution until override and escalation tests pass.

## Approval

| Role | Name | Decision | Date |
|---|---|---|---|
| Provider/technical owner | | | |
| Deployer/business owner | | | |
| Oversight owner | | | |
| Legal/Compliance | | | |
| Risk/Privacy/Security/HR, as applicable | | | |

**Evidence references:**  
**Residual limitations:**  
**Next review trigger/date:**  
**Plan version:**  

## Primary legal references

- Regulation (EU) 2024/1689, as amended: Article 14 and applicable provider, deployer, risk-management, transparency, logging, monitoring, incident, corrective-action, and authority provisions.
- Regulation (EU) 2026/1744 where applicable.
- Applicable employment, equality, accessibility, privacy, safety, consumer-protection, and sector law.
- Current consolidated official texts and provider instructions control over this template.