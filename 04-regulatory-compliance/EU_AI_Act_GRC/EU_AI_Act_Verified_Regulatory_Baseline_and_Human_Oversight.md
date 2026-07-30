# EU AI Act GRC Manual — Verified Regulatory Baseline and Human-Oversight Design

**Workstream:** English master review package  
**Branch:** `manual/eu-ai-act-grc-compliance`  
**Status:** Draft for owner review; not legal advice  
**Verification date:** 29 July 2026

## 1. Authoritative-source hierarchy

Use sources in this order:

1. EUR-Lex legal text and amending legislation.
2. European Commission and EU AI Office implementation material.
3. Adopted codes, templates, standards, and supervisory guidance.
4. Secondary commentary only for orientation; never as the controlling source.

Every legal date, duty, exception, actor role, and enforcement statement must be traceable to an official source. Drafting must clearly distinguish:

- binding legal requirement;
- official guidance or implementation support;
- recommended governance practice;
- optional maturity enhancement.

## 2. Verified regulatory baseline

Regulation (EU) 2024/1689 entered into force on 1 August 2024. Its phased application began on 2 February 2025, with further provisions applying from 2 August 2025 and 2 August 2026. The Commission’s current implementation material reflects later timeline changes introduced through the AI Omnibus. The manual must therefore verify the operative legal text and current Commission timeline before final publication.

Current official implementation milestones used for drafting:

| Date | Drafting baseline |
|---|---|
| 1 August 2024 | AI Act entered into force. |
| 2 February 2025 | Prohibited-practice and AI-literacy provisions began to apply. |
| 2 August 2025 | Governance provisions and obligations for general-purpose AI models began to apply. |
| 2 August 2026 | Most remaining provisions, including relevant transparency rules, apply. |
| 2 December 2027 | Current Commission timeline for specified Annex III high-risk uses. |
| 2 August 2028 | Current Commission timeline for high-risk systems embedded in regulated products. |

**Publication control:** Dates after amendment must not be copied from the original Article 113 schedule without checking the latest amending legislation and Commission implementation materials.

## 3. Core human-centred governance principle

> AI may assist a person, but it must not erase human responsibility, judgment, accountability, or the affected person’s ability to obtain meaningful review.

This principle applies across the manual, including systems that are not legally classified as high-risk. The level of oversight should be proportionate to impact, reversibility, uncertainty, vulnerability, and the seriousness of potential harm.

## 4. Human-oversight control framework

Every organizational AI use case must document the following before deployment:

| Control element | Required organizational decision |
|---|---|
| Permitted purpose | What the AI is allowed to do. |
| Prohibited action | What the AI may never decide or execute alone. |
| Human decision point | Where a trained person must review or approve. |
| Competence | What knowledge, authority, tools, and time the reviewer needs. |
| Override | How the reviewer can reject, correct, stop, or reverse the AI output. |
| Escalation | When uncertainty, conflict, safety, rights, or customer-impact concerns require escalation. |
| Accountability | Which named role owns the final decision and control effectiveness. |
| Affected-person notice | What the person must be told about AI involvement. |
| Challenge and correction | How a person can question, correct, or appeal an AI-assisted outcome. |
| Evidence | What logs, approvals, reasons, changes, and outcomes must be retained. |
| Monitoring | How errors, bias, drift, overrides, complaints, and incidents are reviewed. |
| Stop condition | What event requires suspension or withdrawal of the AI use case. |

## 5. GlobalWay Travel Services example

### Use case

GlobalWay uses an AI assistant to recommend itineraries, identify possible fraud, prioritize support requests, and draft customer communications.

### Human concern

> “Will a real person review this before it affects my trip, my money, my safety, or my ability to receive help?”

### Organizational rule

The AI may prepare recommendations and identify anomalies. It may not independently:

- deny emergency assistance;
- reject an accessibility request;
- cancel travel because of a fraud score;
- make an employment decision;
- resolve a customer complaint involving safety, discrimination, substantial loss, or legal rights;
- prevent a customer from reaching a qualified person.

### Required process

1. AI produces a recommendation or alert.
2. The system displays confidence, relevant limitations, and supporting information.
3. A trained employee reviews the recommendation.
4. The employee approves, corrects, rejects, or escalates it.
5. The final action and reason are recorded.
6. Affected customers receive an appropriate explanation and access to human review.
7. Outcomes, overrides, complaints, and errors feed ongoing monitoring.

## 6. Sample control pattern

### Requirement

Where applicable, human oversight must be assigned to people who are sufficiently competent, trained, authorised, and supported to understand limitations, identify anomalies, avoid over-reliance, interpret outputs, and intervene or stop use.

### Plain-language explanation

A person’s name on a procedure is not meaningful oversight. The reviewer must have enough information, authority, time, independence, and technical support to challenge the system rather than merely approve what it produces.

### Travel-agency example

A fraud model flags a traveller’s booking. The agent reviews the evidence, contacts the traveller when appropriate, checks for data or identity errors, and decides whether to approve, pause, or escalate the booking. The model cannot cancel the trip automatically.

### Control activity

GlobalWay shall establish a documented human-oversight procedure for each material AI use case, including decision thresholds, reviewer qualifications, override authority, escalation triggers, customer-review pathways, logging, and periodic effectiveness testing.

### Evidence

- approved use-case assessment;
- RACI or accountability assignment;
- reviewer training and competency records;
- operating instructions;
- override and escalation logs;
- customer notices and review requests;
- monitoring reports;
- incident and corrective-action records.

### Audit test

Select a sample of AI-assisted decisions and verify that:

1. the assigned reviewer met competency and authority requirements;
2. the required information was available before the decision;
3. the reviewer could override or stop the AI;
4. the final decision and reason were recorded;
5. affected persons received required information and access to review;
6. exceptions, complaints, and errors entered monitoring and corrective-action processes.

## 7. Mandatory graphic design rules

Every graphic must explain either a real process or a real human concern. Decorative-only graphics are prohibited.

### Graphic 1 — Human oversight decision path

**Purpose:** Show how an AI output becomes a responsible organizational decision.  
**Process:** AI recommendation → human review → approve, correct, reject, or escalate → decision recorded → outcome monitored.  
**Human concern:** “Will a qualified person review this before it affects me?”  
**Alt-text concept:** A flow diagram showing an AI recommendation moving to a trained human reviewer, four possible actions, a recorded final decision, and monitoring feedback.

### Graphic 2 — Affected-person concern and response map

**Purpose:** Connect common concerns to organizational safeguards.  
**Concerns:** Am I dealing with AI? Why was this decision made? Is the information correct? Can a person review it? Can I challenge it? Who is accountable?  
**Safeguards:** disclosure, explanation, data correction, human review, appeal route, named accountable owner.  
**Alt-text concept:** A two-column diagram linking six traveller concerns to six organizational responses.

## 8. Open verification items before final publication

- Obtain and cite the operative amending legal text for the AI Omnibus.
- Verify the final application dates against that legal text, not only Commission summaries.
- Confirm the latest Article 50 transparency guidance and any adopted templates.
- Confirm current guidance for providers, deployers, fundamental-rights impact assessments, serious incidents, post-market monitoring, and value-chain responsibilities.
- Verify interaction points with GDPR, consumer law, employment law, accessibility law, and sector-specific travel obligations.

## 9. Review gate

This file establishes the verified drafting baseline and control design. It does not authorize production publication, translation, DOCX/PDF generation, pull-request creation, merge, release, or tagging.
