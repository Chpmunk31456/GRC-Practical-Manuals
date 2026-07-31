# Chapter 42 — Human Oversight and Accountability

**Status:** English master drafting block for owner review  
**Legal verification date:** 29 July 2026  
**Primary legal basis:** Regulation (EU) 2024/1689, especially Articles 14 and 26, as currently applicable following the 2026 AI Omnibus amendments  

> **Core principle:** AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## 42.1 Why human oversight matters

AI systems can process large volumes of information, identify patterns, rank options, generate recommendations, and automate routine activities. These capabilities can improve speed and consistency, but they can also create risks when people rely on outputs without understanding their limitations, when no qualified person can intervene, or when responsibility becomes unclear.

Human oversight is therefore not satisfied by merely placing a person somewhere in the process. Oversight must be **meaningful, informed, timely, authorized, documented, and capable of changing the outcome**.

A person assigned to oversee an AI system must be able to:

- understand the system’s intended purpose, capabilities, and known limitations;
- recognize circumstances in which an output may be unreliable, inappropriate, discriminatory, unsafe, or inconsistent with policy;
- avoid over-reliance on AI-generated recommendations;
- interpret the output correctly, considering the available tools and explanatory information;
- decide not to use the system or its output in a particular case;
- intervene, stop, override, correct, or escalate the system when necessary; and
- document the decision and remain accountable for the resulting action.

## 42.2 Legal requirement

Article 14 requires high-risk AI systems to be designed and developed so that natural persons can effectively oversee them while they are in use. The oversight measures must be proportionate to the system’s risks, autonomy, and context of use. Their purpose is to prevent or minimize risks to health, safety, and fundamental rights, including risks that remain after other controls have been implemented.

The Regulation requires the oversight arrangements to enable the assigned person, as appropriate, to:

1. understand the relevant capacities and limitations of the high-risk AI system;
2. remain aware of possible automation bias, especially where outputs are used to support decisions made by people;
3. interpret the system’s output correctly;
4. decide not to use the system or disregard, override, or reverse its output;
5. intervene in the system’s operation or stop it through an appropriate mechanism; and
6. apply special safeguards where the system performs remote biometric identification, when applicable.

Providers are responsible for identifying and, where technically feasible, building appropriate oversight measures into the system. Deployers must assign oversight to people who have the necessary competence, training, authority, and organizational support.

### Plain-language explanation

A high-risk AI system cannot be placed into operation with the assumption that a person will somehow notice and fix problems. The provider and deployer must deliberately design the human role.

That means answering practical questions before deployment:

- What may the AI do by itself?
- What may it recommend but not decide?
- Which decisions require human approval?
- Who is qualified and authorized to review the output?
- What information does that reviewer need?
- How much time is available for review?
- What conditions require the system to stop or escalate?
- How can an affected person challenge an outcome?
- Who remains accountable for the final decision?

## 42.3 Scope: legal requirement versus broader good practice

Article 14 is a specific legal requirement for high-risk AI systems. However, meaningful human oversight is also a strong governance practice for other AI systems that can materially affect people, safety, access to services, employment, finances, privacy, or legal rights.

This manual therefore uses two labels:

- **Required control:** necessary where Article 14 or another binding obligation applies.
- **Recommended control:** applied as organizational good practice where the system is not legally classified as high-risk but could still create meaningful harm.

Organizations must not describe a recommended control as a statutory requirement unless the legal basis has been confirmed.

## 42.4 GlobalWay Travel Services example

GlobalWay Travel Services uses an AI-enabled disruption-management system. The system analyzes flight cancellations, missed connections, hotel availability, traveler preferences, contract rules, loyalty status, and travel-risk information. It then recommends alternative itineraries and prioritizes cases for travel consultants.

### What the AI may do

The AI may:

- identify disrupted itineraries;
- generate available rerouting options;
- rank options using approved business rules;
- flag time-sensitive cases;
- identify missing information;
- draft a proposed message to the traveler; and
- route a case to the correct support queue.

### What remains a human decision

A qualified travel consultant must review and decide cases involving:

- medical or disability-related requirements;
- accessibility accommodations;
- unaccompanied or stranded minors;
- safety, security, or geopolitical concerns;
- visa, passport, or immigration complications;
- disputed denials or refunds;
- material additional cost outside approved thresholds;
- conflicting traveler and employer instructions;
- low-confidence or incomplete AI output;
- suspected discrimination or unfair prioritization; or
- any circumstance in which the traveler requests human review.

### Oversight workflow

**AI identifies disruption → AI proposes options → qualified consultant reviews → approve, correct, reject, or escalate → traveler is informed → decision and rationale are recorded → outcome is monitored**

### Human concern

> **“Will a qualified person review this before it materially affects my safety, accessibility, cost, or ability to travel?”**

GlobalWay addresses this concern by making human review mandatory for consequential exceptions, presenting a visible human-escalation option, recording the reviewer’s decision, and monitoring complaints and overrides.

## 42.5 Control objective

**Control objective HO-01:** AI-supported decisions are subject to proportionate and meaningful human oversight, with clear authority, competence, intervention rights, accountability, and evidence.

## 42.6 Control activities

### HO-01.1 — Define the human decision boundary

For each AI use case, the business owner must document:

- actions the AI may perform automatically;
- outputs the AI may recommend;
- decisions reserved for a person;
- prohibited autonomous actions;
- monetary, safety, legal, or impact thresholds requiring review;
- mandatory escalation conditions; and
- the accountable role for the final outcome.

**Evidence:** approved AI use-case record, decision-rights matrix, process map, policy approval.

### HO-01.2 — Assign qualified oversight personnel

The deployer must assign oversight only to people with appropriate:

- domain knowledge;
- AI-system training;
- understanding of known limitations and failure modes;
- authority to reject or override outputs;
- access to relevant contextual information; and
- sufficient time and organizational support to perform the review.

A nominal reviewer who lacks authority or time does not constitute meaningful oversight.

**Evidence:** role descriptions, assignment records, training completion, competence assessment, staffing analysis.

### HO-01.3 — Provide usable oversight information

The interface and operating procedure must provide the reviewer with enough information to make an informed decision. Depending on the use case, this may include:

- the AI recommendation;
- relevant source information;
- confidence or uncertainty indicators;
- known data-quality limitations;
- policy rules applied;
- prior related decisions;
- material alternatives;
- reasons for escalation; and
- warnings when the system is operating outside expected conditions.

**Evidence:** interface screenshots, instructions for use, user-acceptance testing, reviewer feedback.

### HO-01.4 — Enable intervention, override, and stop

The oversight design must allow an authorized person to take effective action. Available mechanisms should include, as appropriate:

- reject output;
- correct output;
- select an alternative;
- pause processing;
- stop the system;
- revert to a safe manual process;
- escalate to a specialist; and
- record the reason for intervention.

A control is ineffective when the reviewer can see a problem but cannot change the outcome.

**Evidence:** functional test results, override logs, stop-control tests, fallback procedures.

### HO-01.5 — Control automation bias

The organization must reduce the risk that reviewers accept AI outputs simply because they appear objective, precise, or technologically sophisticated.

Controls may include:

- training on automation bias and system limitations;
- requiring independent consideration before displaying the recommendation in sensitive cases;
- presenting alternatives rather than a single default answer;
- avoiding interface designs that pressure the reviewer to accept the AI output;
- requiring a reason for exceptional or high-impact approvals;
- periodic blinded comparison of human and AI assessments; and
- monitoring unusually high acceptance rates.

**Evidence:** training materials, interface-design review, acceptance-rate reports, quality-review samples.

### HO-01.6 — Define stop and escalation conditions

The system must be stopped, restricted, or escalated when predefined conditions occur, including:

- performance falls below an approved threshold;
- input data is missing, corrupted, stale, or outside the intended scope;
- the system produces unsafe, discriminatory, or clearly implausible output;
- a material model or vendor change has not been approved;
- monitoring detects unexpected behavior;
- required human review is unavailable;
- an affected person raises a credible challenge; or
- continued use could create a serious incident or fundamental-rights risk.

**Evidence:** escalation matrix, incident tickets, suspension records, monitoring alerts, corrective-action records.

### HO-01.7 — Preserve challenge, correction, and human-review rights

Where an AI-supported process materially affects a person, the organization should provide a clear way to:

- request human review;
- correct inaccurate information;
- submit relevant contextual information;
- challenge an outcome;
- obtain an understandable explanation of the process, subject to applicable law; and
- receive a timely response.

The process must not merely return the same automated outcome without genuine reconsideration.

**Evidence:** notice text, complaint procedure, case records, response-time metrics, overturned-decision analysis.

### HO-01.8 — Record the decision and accountability trail

For consequential decisions, records should identify:

- the AI system and version used;
- relevant input and output;
- the human reviewer;
- review date and time;
- decision taken;
- whether the AI output was accepted, corrected, rejected, or escalated;
- rationale where required;
- exceptions or policy deviations; and
- subsequent outcome or complaint.

**Evidence:** system logs, case-management records, approval records, audit trail.

### HO-01.9 — Monitor oversight effectiveness

The organization must periodically assess whether human oversight is working in practice. Metrics may include:

- AI-output acceptance and override rates;
- reviewer disagreement rates;
- escalation frequency;
- complaint and appeal volumes;
- overturned decisions;
- safety or fairness incidents;
- time available for review;
- reviewer workload;
- training completion; and
- recurring reasons for correction.

An extremely low override rate is not automatically proof of quality. It may indicate high system accuracy, but it may also indicate automation bias, inadequate authority, or superficial review.

**Evidence:** oversight dashboard, trend analysis, committee minutes, remediation plans.

## 42.7 Human oversight plan

Each consequential AI system should have an approved Human Oversight Plan containing at least:

| Field | Required content |
|---|---|
| System and purpose | Name, version, intended purpose, affected population |
| Legal classification | High-risk, transparency risk, other regulated category, or internal risk tier |
| AI authority | Actions and recommendations permitted |
| Human authority | Decisions reserved for people |
| Oversight roles | Primary reviewer, specialist, escalation owner, accountable executive |
| Competence | Required knowledge, training, certification, and experience |
| Review timing | Before action, during operation, after action, or sampled review |
| Decision information | Context, warnings, explanations, confidence, alternatives |
| Intervention tools | Reject, correct, override, stop, rollback, manual fallback |
| Escalation triggers | Safety, rights, confidence, data, complaints, system performance |
| Affected-person process | Notice, correction, challenge, human review, response time |
| Records | Inputs, outputs, reviewer, decision, rationale, intervention, outcome |
| Monitoring | Metrics, thresholds, review frequency, control owner |
| Testing | Design testing, operating-effectiveness testing, scenario testing |
| Approval | Business, risk, compliance, privacy, security, and executive approval as applicable |

## 42.8 Audit test

An auditor should not conclude that human oversight is effective merely because a policy names a reviewer. The audit must test both **design effectiveness** and **operating effectiveness**.

### Design-effectiveness testing

1. Select the AI use case and confirm its legal and internal risk classification.
2. Inspect the documented division between AI authority and human authority.
3. Confirm that reviewers have sufficient competence, authority, information, time, and intervention capability.
4. Verify that stop, override, escalation, and fallback mechanisms are defined.
5. Confirm that affected people can request correction or human review where appropriate.
6. Evaluate whether the interface and process control automation bias.
7. Verify that decisions and interventions are logged.

### Operating-effectiveness testing

1. Select a representative sample of consequential decisions.
2. Confirm that required human review occurred before the action was finalized.
3. Verify the reviewer’s identity, competence, and authority.
4. Compare the AI output with the final decision.
5. Inspect evidence of corrections, overrides, or escalations.
6. Confirm that mandatory escalation cases were handled by the correct role.
7. Test complaints or challenges to determine whether genuine human reconsideration occurred.
8. Review monitoring reports for unusual acceptance rates, delays, repeated errors, or reviewer-capacity concerns.
9. Confirm that identified deficiencies resulted in corrective action.

### Example audit conclusion

> The control is designed effectively because GlobalWay defines the AI decision boundary, requires qualified review for consequential travel exceptions, provides override and escalation functions, and maintains decision records. Operating effectiveness is supported by sampled cases showing documented review and intervention. One deficiency was identified: weekend staffing did not consistently provide timely accessibility-specialist escalation. Management opened a corrective action with a defined owner and due date.

## 42.9 Failure patterns

Common weaknesses include:

- a “human in the loop” who routinely approves outputs without review;
- a reviewer who lacks authority to override the system;
- insufficient time to assess high volumes of AI-generated decisions;
- no safe manual fallback;
- confidence scores presented without explanation or validation;
- override capability that exists technically but is discouraged operationally;
- escalation procedures that are unclear or unavailable outside business hours;
- affected people unable to reach a real person;
- repeated overrides that are not analyzed; and
- accountability assigned to a committee rather than a named role.

## 42.10 Management questions

Executives and control owners should be able to answer:

1. Which AI-supported decisions can materially affect people?
2. Which of those decisions require human approval?
3. Who is personally accountable for each decision process?
4. Can reviewers reject, correct, stop, and escalate the AI output?
5. Are reviewers trained to identify system limitations and automation bias?
6. Can an affected person obtain meaningful human reconsideration?
7. What do override, complaint, and escalation trends show?
8. What happens when qualified oversight personnel are unavailable?
9. When was the oversight design last tested?
10. What evidence demonstrates that oversight changes outcomes in practice?

## 42.11 Source register

### Binding legal source

- Regulation (EU) 2024/1689, Article 14, Human oversight: https://eur-lex.europa.eu/eli/reg/2024/1689/oj

### Current official implementation sources

- European Commission, AI Act regulatory framework and application timeline: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- European Commission, Navigating the AI Act: https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act
- European Commission, AI Act standardisation: https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation
- European Commission, AI Omnibus entry into force, 27 July 2026: https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force

## 42.12 Legal and editorial caution

This chapter distinguishes the binding Article 14 requirements for high-risk AI systems from broader recommended governance practices. The high-risk application dates were amended in July 2026. The legal baseline must therefore be checked again against the current consolidated Regulation, applicable amending legislation, and official Commission implementation materials immediately before publication.
