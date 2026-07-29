# Chapter 92 — Inherent-Risk Assessment

## Purpose

This chapter establishes a consistent method for assessing the risk of an AI use case before considering the effect of controls.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should assess inherent AI risk before approval, procurement, development, deployment, or material change. The assessment should consider intended purpose, affected people, legal classification, decision consequence, data sensitivity, autonomy, scale, technical complexity, third-party dependency, and credible misuse or failure scenarios.

## Plain-language explanation

Inherent risk is the level of risk that exists without assuming safeguards will work. It provides a conservative starting point for deciding how much governance, testing, evidence, oversight, and approval a use case requires.

## Assessment principles

The assessment should be:

- completed before controls are credited;
- based on the real use case rather than the product name;
- documented and repeatable;
- proportionate to consequence and scale;
- conservative where information is incomplete;
- reviewed by relevant legal, privacy, security, risk, technical, and business stakeholders;
- repeated after material change, incident, or expansion of use.

## Assessment scope

Evaluate at least:

- intended and reasonably foreseeable use;
- prohibited-practice exposure;
- high-risk, transparency, or GPAI classification;
- affected persons and vulnerable groups;
- importance of the decision or recommendation;
- degree of automation and human dependency;
- physical, financial, legal, privacy, safety, employment, accessibility, and fundamental-rights effects;
- personal, confidential, special-category, biometric, or regulated data;
- geographic reach and number of people affected;
- model and system complexity;
- explainability and contestability;
- third-party, cloud, API, and open-source dependencies;
- potential misuse, abuse, manipulation, or circumvention;
- operational criticality and recovery requirements.

## Rating dimensions

Assess impact severity, likelihood, scale, reversibility, human dependency, and uncertainty. Organizations may use qualitative tiers or a documented numerical scale, but a numerical score must not conceal a mandatory legal classification or a single unacceptable risk.

## Mandatory escalation triggers

Escalate regardless of aggregate score when the use case may involve:

- a prohibited AI practice;
- an Annex I or Annex III high-risk use case;
- employment, education, credit, insurance, migration, law-enforcement, biometric, or essential-service decisions;
- children or other vulnerable persons;
- special-category or biometric data;
- physical safety or emergency response;
- large-scale profiling or monitoring;
- autonomous execution of consequential transactions;
- material uncertainty about purpose, data, model behavior, or vendor evidence.

## GlobalWay Travel Services example

GlobalWay proposes an AI assistant that recommends itinerary changes during severe weather. The system may influence safety-sensitive decisions, processes traveler-location and health-accommodation information, depends on airline and weather data, and may generate recommendations at scale.

Before considering controls, GlobalWay rates the use case as high inherent risk. The rating requires enhanced testing, human approval for critical actions, resilience controls, vendor assurance, and executive risk acceptance before deployment.

## Control activities

- Maintain an approved inherent-risk methodology.
- Require assessment during intake and before procurement or development commitment.
- Define mandatory escalation triggers.
- Record assumptions, evidence, uncertainty, and rationale.
- Prevent control effectiveness from reducing the inherent-risk score.
- Link the assessment to approval, testing, monitoring, and assurance requirements.
- Reassess after material change, incident, or expanded use.

## Evidence

- completed inherent-risk assessment;
- use-case description and process map;
- classification analysis;
- data inventory;
- affected-person analysis;
- scoring rationale;
- stakeholder review comments;
- uncertainty and assumption register;
- escalation and approval records;
- reassessment history.

## Audit tests

1. Select AI use cases across risk tiers and verify that inherent risk was assessed before controls were credited.
2. Confirm the use case, data, affected people, autonomy, scale, and dependencies were accurately described.
3. Reperform selected ratings using the approved methodology.
4. Verify mandatory escalation triggers were applied.
5. Review whether uncertainty was documented conservatively.
6. Confirm the rating drove required approval, testing, oversight, and monitoring.
7. Verify reassessment occurred after material change or incident.

## Metrics

- percentage of inventoried systems with current inherent-risk assessments;
- assessments completed before approval or procurement;
- use cases by inherent-risk tier;
- overdue reassessments;
- assessments with unresolved uncertainty;
- mandatory escalations triggered;
- rating overrides and accountable approvers;
- incidents involving understated inherent risk.

## Management checklist

- Is the assessment completed before controls are considered?
- Does it reflect the real use case and affected people?
- Are legal classification and mandatory triggers addressed?
- Are uncertainty and incomplete evidence treated conservatively?
- Does the rating drive governance and assurance requirements?
- Is reassessment required after material change or incident?

## Figure specification — Inherent AI Risk Assessment Funnel

Create a funnel showing use-case context, legal classification, affected people, consequence, data, autonomy, scale, dependencies, misuse, and uncertainty flowing into an inherent-risk tier. Show mandatory escalation triggers bypassing the aggregate score and routing directly to enhanced governance.

**Alt text:** Inherent AI risk assessment funnel combining use-case context, legal classification, affected people, consequence, data, autonomy, scale, dependencies, misuse, and uncertainty, with mandatory escalation triggers routing directly to enhanced governance.
