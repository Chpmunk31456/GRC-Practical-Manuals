# Chapter 104 — Control-Library Design

## Purpose

This chapter explains how to design and maintain a practical AI control library that translates legal duties, policy expectations, technical safeguards, and business-risk decisions into testable control activities.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should maintain a structured AI control library that is traceable to applicable requirements, assigned to accountable owners, written in testable language, supported by defined evidence, and tailored to system role, risk, lifecycle stage, and jurisdiction.

## Plain-language explanation

A control library converts broad obligations into repeatable actions. It should answer who performs the control, what they do, when they do it, what evidence is retained, and how failure is identified and corrected. A list of vague principles is not an auditable control framework.

## Control architecture

Organize controls into domains such as:

- governance and accountability;
- inventory, intake, and classification;
- prohibited-practice screening;
- risk and impact assessment;
- data governance;
- model and system development;
- technical documentation;
- transparency and human communication;
- human oversight;
- accuracy, robustness, cybersecurity, and resilience;
- third-party and supply-chain management;
- conformity and regulatory readiness;
- deployment and change management;
- logging, monitoring, and post-market oversight;
- incident and corrective-action management;
- training and AI literacy;
- records, evidence, and assurance.

## Control statement format

Each control should define:

- unique control identifier;
- control objective;
- control activity;
- requirement or risk addressed;
- accountable owner;
- performer;
- frequency or trigger;
- systems and processes in scope;
- required evidence;
- retention requirement;
- control type;
- automation status;
- testing method;
- related controls;
- exception path.

A strong control statement uses active, specific language. Example:

> Before production deployment, the AI product owner must obtain documented approval of the use-case classification, prohibited-practice screen, privacy review, security review, and human-oversight plan. The release manager must verify all approvals in the deployment record and block release when any mandatory approval is missing or expired.

## Control types

Classify controls as appropriate:

- preventive, detective, corrective, or directive;
- manual, automated, or hybrid;
- entity-level, process-level, system-level, or transaction-level;
- continuous, periodic, event-triggered, or one-time;
- key or supporting;
- legal requirement, recommended practice, or optional enhancement.

## Design principles

Controls should be:

- proportionate to risk;
- aligned with actual business processes;
- understandable to performers;
- specific enough to test;
- supported by reliable evidence;
- resistant to self-approval and conflicts of interest;
- integrated into lifecycle gates;
- adaptable to role and jurisdiction;
- version controlled;
- reviewed after incidents, findings, and regulatory change.

## Control rationalization

Avoid unnecessary duplication. Where one control supports several obligations, map it to each requirement rather than creating multiple inconsistent versions. Retain separate controls when ownership, evidence, frequency, population, or testing method differs materially.

## Baseline and overlays

Use:

- an enterprise AI-control baseline;
- role overlays for provider, deployer, importer, distributor, authorized representative, and product manufacturer;
- risk overlays for prohibited, high-risk, transparency, GPAI, systemic-risk, and lower-risk use cases;
- jurisdiction and sector overlays;
- technology overlays for generative AI, agents, biometrics, employment tools, and safety-related systems.

## GlobalWay Travel Services example

GlobalWay creates a baseline control requiring every AI use case to be inventoried, classified, approved, monitored, and assigned an owner. A high-risk overlay adds technical-documentation, human-oversight, logging, conformity, and post-market controls. A generative-AI overlay adds prompt-injection testing, content marking, retrieval governance, and tool-use restrictions.

The same control library supports traveler-assistance, recruitment, fraud-detection, and supplier-risk systems without forcing every system to use identical controls.

## Control activities

- Establish a control taxonomy and naming convention.
- Define standard control attributes.
- Map controls to requirements and risks.
- Identify key controls and dependencies.
- Assign owners and performers.
- Define evidence and retention.
- Set control frequencies and triggers.
- Establish change, exception, and retirement processes.
- Review the library after legal, technical, or business change.

## Evidence

- approved control taxonomy;
- control-library register;
- requirement and risk mappings;
- control-owner assignments;
- evidence standards;
- version history;
- change approvals;
- rationalization decisions;
- overlay definitions;
- exception records;
- periodic review results.

## Audit tests

1. Select key controls and verify statements identify owner, activity, frequency, evidence, scope, and trigger.
2. Trace controls to legal requirements and risk statements.
3. Confirm role and risk overlays are applied consistently.
4. Review whether duplicate controls have been rationalized appropriately.
5. Test whether retired or changed controls retain version history and approval.
6. Verify evidence requirements are sufficient to demonstrate operation.
7. Confirm incidents, findings, and regulatory changes trigger library review.

## Metrics

- controls by domain and type;
- key controls without owners;
- controls without defined evidence;
- unmapped requirements or risks;
- duplicate or conflicting controls;
- overdue control reviews;
- controls with repeated failures;
- automated-control coverage;
- exceptions by control domain;
- time to update controls after material change.

## Management checklist

- Does every material obligation map to a practical control?
- Can each control be performed and tested consistently?
- Are owners, evidence, frequency, and scope explicit?
- Are role, risk, and jurisdiction differences handled through overlays?
- Is the library current, version controlled, and connected to change management?

## Figure specification — AI Control-Library Architecture

Create a layered diagram with an enterprise baseline at the center, surrounded by role, risk, jurisdiction, sector, and technology overlays. Connect legal requirements and risk statements on the left to control activities, evidence, testing, findings, and remediation on the right.

**Alt text:** Layered AI control-library architecture connecting legal requirements and risks to an enterprise control baseline, role and risk overlays, evidence, testing, findings, and remediation.
