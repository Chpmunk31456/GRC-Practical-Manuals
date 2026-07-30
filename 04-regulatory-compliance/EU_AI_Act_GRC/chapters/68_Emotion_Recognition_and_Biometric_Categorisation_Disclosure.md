# Chapter 68 — Emotion-Recognition and Biometric-Categorisation Disclosure

## 68.1 Purpose

This chapter establishes a practical governance, transparency, and accountability framework for organizations that deploy AI systems intended to recognize emotions or categorize people using biometric data.

The objective is to ensure that affected people are informed clearly and at the right time, that prohibited uses are screened out before deployment, that human responsibility is preserved, and that the organization can demonstrate compliance through reliable evidence.

> **Core principle:** AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## 68.2 Legal Requirement

Article 50 requires deployers of emotion-recognition systems and biometric-categorisation systems to inform the natural persons exposed to those systems.

The notice obligation must be read together with the AI Act’s prohibited-practice rules. Some uses of emotion recognition and biometric categorisation are prohibited, including specified workplace and education uses and certain categorisation based on sensitive characteristics. A transparency notice does not make a prohibited use lawful.

The correct sequence is therefore:

1. determine whether the system falls within the legal definition;
2. screen the use case for prohibited-practice risk;
3. assess whether another legal basis or restriction applies;
4. provide timely, understandable disclosure when deployment is permitted;
5. maintain human oversight, challenge, correction, and escalation mechanisms;
6. retain evidence showing that the notice and controls operated effectively.

## 68.3 Plain-Language Explanation

People should not discover after the fact that a camera, microphone, kiosk, wearable device, or software tool was attempting to infer their emotional state or categorize them through biometric characteristics.

A compliant organization must tell people what is happening before or at the point of exposure, explain the purpose in language they can understand, identify who is responsible, and provide a practical route to ask questions or obtain human assistance.

Disclosure is only one control. The organization must also ask whether the system should be used at all.

## 68.4 Key Definitions

### Emotion-recognition system

An AI system intended to identify or infer emotions or intentions of natural persons on the basis of biometric data.

Examples may include systems that attempt to infer states such as happiness, sadness, anger, surprise, embarrassment, enthusiasm, or frustration from facial features, voice, posture, movement, or other biometric signals.

The legal concept does not automatically include every system that detects an obvious physical signal. A system that detects driver fatigue for safety purposes may require separate analysis from a system that claims to infer a person’s emotion or intention.

### Biometric-categorisation system

An AI system that assigns people to categories on the basis of biometric data.

Examples may include systems that group people by physical, physiological, or behavioral characteristics. Uses involving sensitive characteristics require especially careful legal screening, because some are prohibited.

### Exposure

A person is exposed when the system observes, processes, evaluates, or attempts to infer information about that person, even where the person does not actively interact with the system.

## 68.5 GlobalWay Travel Services Example

GlobalWay Travel Services considers several proposed AI uses:

- airport-lounge cameras that estimate traveler frustration;
- voice analytics that classify caller sentiment during disruption calls;
- kiosks that adjust support prompts based on inferred emotional state;
- biometric queue analytics that categorize travelers by apparent behavior;
- employee call-quality tools that infer emotion from voice;
- recruitment interview software that claims to assess confidence or enthusiasm.

GlobalWay does not treat these as ordinary analytics projects.

Each proposal is routed through a dedicated biometric and emotion-recognition review because:

- the system may infer sensitive information incorrectly;
- the person may not know the analysis is occurring;
- the output may influence service, employment, or safety decisions;
- some workplace or recruitment uses may be prohibited or otherwise legally restricted;
- the data may qualify as personal or special-category data under other laws;
- the technology may create discrimination, accessibility, cultural, or scientific-validity concerns.

### Approved limited use example

GlobalWay deploys an airport kiosk that detects clear signs of traveler distress only to offer an optional human-assistance button. The system does not score the traveler, restrict service, change price, assign priority, or make a decision about eligibility.

Before use, the traveler sees:

> “This kiosk uses AI-assisted visual analysis to detect whether you may need additional help. It does not make decisions about your booking or eligibility. You may skip this feature and request assistance from a person.”

A human agent remains responsible for any action.

### Rejected use example

GlobalWay rejects a proposal to infer employee emotions during customer calls for performance scoring. The organization determines that a notice would not cure the underlying legal and human-rights concerns.

## 68.6 Control Objective

GlobalWay shall ensure that emotion-recognition and biometric-categorisation systems are:

- identified before acquisition or deployment;
- screened for prohibited or restricted uses;
- supported by a documented legal and ethical assessment;
- deployed only for a defined, necessary, and proportionate purpose;
- disclosed to affected persons clearly and before or at exposure;
- subject to meaningful human oversight;
- prevented from making unsupported or solely automated adverse decisions;
- monitored for accuracy, bias, misuse, and unexpected impact;
- suspended when notice, legal basis, performance, or safeguards fail.

## 68.7 Required Use-Case Boundary

For every approved use case, GlobalWay documents:

| Required element | Example |
|---|---|
| What AI may do | Detect signals suggesting a traveler may need help |
| What AI may not do | Infer medical condition, eligibility, trustworthiness, or intent |
| Human decision | Decide whether and how to offer assistance |
| Review requirement | Confirm context directly with the traveler |
| Stop condition | Missing notice, poor confidence, bias indicator, complaint, or technical failure |
| Escalation route | Duty manager, privacy, legal, compliance, security, or accessibility lead |
| Accountable owner | Director of Traveler Experience |
| Challenge right | Traveler may decline, ask questions, request correction, or seek human assistance |

## 68.8 Prohibited-Practice Screening

Before any transparency notice is drafted, the use case must be screened for prohibition.

At minimum, the reviewer asks:

- Is the system used in a workplace or educational context to infer emotion?
- Is the purpose medical or safety-related, and is that exception genuinely applicable?
- Does the biometric categorisation infer or deduce sensitive characteristics?
- Could the system classify people by race, political opinion, trade-union membership, religion, philosophical belief, sex life, or sexual orientation?
- Is the system part of recruitment, employee assessment, education, law enforcement, migration, border control, or another high-impact context?
- Is the stated purpose different from the likely operational effect?
- Could the use become prohibited after a feature, model, or purpose change?

A failed prohibition screen results in rejection, suspension, or legal escalation—not a revised notice.

## 68.9 Notice Requirements

The notice should be:

- provided before or at the moment of exposure;
- prominent enough to be noticed;
- written in plain language;
- available in relevant languages;
- accessible to people with disabilities;
- specific to the actual system and purpose;
- separate from dense general terms and conditions;
- available through the same channel in which exposure occurs;
- supplemented by a longer explanation where needed.

At minimum, the notice should explain:

1. that an AI system is being used;
2. whether it recognizes emotion or performs biometric categorisation;
3. the purpose of the use;
4. what data or signals may be analyzed;
5. what the system may and may not influence;
6. whether a human reviews the result;
7. whether participation is optional;
8. how to obtain human assistance;
9. how to ask questions, challenge, or complain;
10. who is accountable for the deployment.

## 68.10 Layered Notice Model

### Layer 1 — Immediate notice

A short, prominent statement at the point of exposure.

Example:

> “AI-assisted voice analysis is active during this call to identify whether additional support may be helpful. It does not decide your booking outcome.”

### Layer 2 — Practical explanation

A concise explanation available through a link, button, QR code, spoken option, or agent script.

Example topics:

- signals analyzed;
- purpose;
- human review;
- retention;
- opt-out or alternative channel;
- complaint and correction route.

### Layer 3 — Full policy information

Detailed information for legal, privacy, regulatory, and audit purposes.

This layer should not be used as a substitute for immediate disclosure.

## 68.11 Human Oversight

A human reviewer must understand:

- the system’s intended purpose;
- uncertainty and confidence limitations;
- scientific-validity concerns;
- cultural and accessibility variation;
- the risk of automation bias;
- prohibited inferences;
- when not to rely on the result;
- how to override, disregard, or escalate;
- how to explain the outcome to the affected person.

The human reviewer must not simply confirm the AI output without independent context.

## 68.12 Scientific Validity and Performance

Emotion-recognition systems may produce outputs that appear precise while relying on weak, context-dependent, or contested assumptions.

GlobalWay therefore requires evidence addressing:

- intended population;
- operating environment;
- supported languages and accents;
- disability and neurodiversity effects;
- cultural variation;
- lighting, audio, camera, and device limitations;
- false-positive and false-negative rates;
- confidence thresholds;
- known failure modes;
- independent validation;
- vendor claims versus observed performance.

A polished dashboard is not proof that the inference is valid.

## 68.13 Fairness, Accessibility, and Vulnerable Persons

The review must consider whether the system may disadvantage:

- people with disabilities;
- neurodivergent people;
- people with speech differences;
- people using assistive technology;
- people from different cultural or linguistic backgrounds;
- children;
- older adults;
- distressed, ill, or fatigued travelers;
- people affected by trauma;
- people whose facial expression, voice, movement, or behavior differs from vendor assumptions.

The organization must provide a meaningful non-AI alternative where appropriate.

## 68.14 Data Protection and Retention

The organization should document:

- categories of biometric and related personal data processed;
- purpose and legal basis;
- whether special-category data is involved;
- retention period;
- access restrictions;
- security controls;
- cross-border transfer arrangements;
- processor and subprocessor roles;
- deletion and correction procedures;
- relationship to any DPIA or fundamental-rights impact assessment.

Data should not be retained merely because the system can collect it.

## 68.15 Vendor and Contract Controls

Contracts should address:

- exact system purpose and prohibited uses;
- model and feature descriptions;
- performance evidence;
- population and environmental limitations;
- notice capabilities;
- logging and traceability;
- data ownership and retention;
- subcontractors;
- security and breach notification;
- bias and performance monitoring;
- material-change notification;
- audit rights;
- suspension and termination rights;
- support for complaints, correction, and deletion.

A vendor’s statement that a product is “AI Act compliant” is not sufficient evidence.

## 68.16 Stop and Escalation Conditions

Normal use must stop when:

- required disclosure is missing or not functioning;
- the use case may be prohibited;
- the system is used for a new purpose;
- a model or feature change alters the inference;
- accuracy falls below the approved threshold;
- bias or unequal impact is detected;
- affected persons cannot obtain human assistance;
- staff begin using outputs for unauthorized decisions;
- data retention or security controls fail;
- complaints indicate deception, harm, or misunderstanding;
- the organization cannot explain what the system is doing.

## 68.17 Evidence

GlobalWay retains:

- system inventory record;
- role and applicability assessment;
- prohibited-practice screening;
- legal review;
- DPIA and fundamental-rights assessment where applicable;
- approved purpose statement;
- data-flow map;
- notice text and translations;
- screenshots, recordings, or photographs showing notice placement;
- accessibility test results;
- human-oversight plan;
- training records;
- performance and bias validation;
- vendor documentation;
- contracts and change notices;
- monitoring results;
- complaint and challenge records;
- incident records;
- stop-use and remediation decisions;
- management approvals.

## 68.18 Metrics

Management should review:

- number of emotion-recognition and biometric-categorisation systems inventoried;
- percentage with completed prohibition screening;
- percentage with approved notice and accessibility review;
- notice-delivery success rate;
- opt-out or alternative-channel usage;
- complaint rate;
- human-override rate;
- false-positive and false-negative trends;
- performance by language, population, and environment;
- unauthorized-use findings;
- material changes awaiting reassessment;
- time to suspend or correct a failed control.

Metrics must not reward low complaint numbers without checking whether people understood that the system was present.

## 68.19 Audit Test

An auditor should:

1. identify all systems that may infer emotion or categorize people using biometric data;
2. compare the inventory to procurement, security, privacy, and operational records;
3. verify that each use case completed prohibited-practice screening;
4. inspect the legal and role analysis;
5. observe the actual deployment point;
6. confirm that notice appears before or at exposure;
7. test whether the notice is prominent, understandable, localized, and accessible;
8. verify that the stated purpose matches actual use;
9. inspect human-review and escalation procedures;
10. sample decisions or interactions for unauthorized reliance;
11. test performance and bias evidence;
12. review complaints, incidents, overrides, and remediation;
13. trace vendor changes to reassessment;
14. confirm that suspended uses were actually disabled.

### Audit failure examples

- a small privacy-policy clause is the only notice;
- a camera performs emotion inference without signage;
- callers are analyzed before the recorded notice plays;
- employees use sentiment scores for performance evaluation;
- a prohibited use is defended by saying that people were informed;
- the organization cannot explain what biometric signals are analyzed;
- no accessible alternative exists;
- a vendor changes the model without reassessment;
- human reviewers treat a low-confidence inference as fact;
- complaints are recorded but do not trigger remediation.

## 68.20 Formal Process Graphic Specification

**Figure 68-1 — Emotion and Biometric Transparency Decision Flow**

Process:

`Proposed system identified → emotion/biometric definition assessed → prohibited-practice screen → legal and impact review → purpose and human boundary approved → notice designed and accessibility tested → deployment authorized → people informed before exposure → human review and alternative available → monitoring, complaints, and changes reassessed`

The graphic should use two parallel tracks:

- **Legality and governance track:** classify, prohibit or approve, document, monitor.
- **Human experience track:** inform, understand, choose, ask, challenge, obtain human help.

**Human concern shown beneath the process:**

> “Is this system judging how I feel without telling me?”

**Alt text:** A two-track decision flow showing that an organization must first identify and legally screen emotion-recognition or biometric-categorisation systems, then approve purpose and safeguards, provide accessible notice before exposure, preserve human assistance and challenge rights, and continuously monitor the system.

## 68.21 Original Workplace-Satire Graphic

**Figure 68-2 — “The Mood Dashboard”**

Scene: A manager points proudly to a dashboard that labels every traveler in the terminal as “calm.” Behind the manager, alarms are sounding, luggage is piled up, and a traveler is waving a cancelled boarding pass.

Caption:

> “The system says everyone is calm. The travelers have requested a second opinion.”

Control lesson: A confident label is not reliable evidence of a person’s emotional state. Human context, notice, challenge, and independent judgment remain essential.

**Alt text:** A manager trusts an AI dashboard showing every traveler as calm while visible disruption and frustrated travelers contradict the result. The cartoon illustrates false confidence in emotion-recognition output.

## 68.22 Management Review Questions

Senior management should ask:

- Where are we attempting to infer emotion or categorize people biometrically?
- Which uses were rejected as prohibited or disproportionate?
- Can affected people see and understand the notice before exposure?
- Can they use a non-AI alternative?
- What decisions could the output influence?
- Are staff using the result beyond the approved purpose?
- What evidence supports scientific validity?
- Which populations experience the highest error rates?
- How quickly can the system be suspended?
- Can we demonstrate the complete decision trail to an auditor or regulator?

## 68.23 Implementation Checklist

- [ ] Inventory all emotion-recognition and biometric-categorisation systems.
- [ ] Complete prohibited-practice screening before procurement or deployment.
- [ ] Document legal role, purpose, necessity, and proportionality.
- [ ] Define what AI may do and what remains a human decision.
- [ ] Complete privacy and fundamental-rights assessments where applicable.
- [ ] Design layered, accessible, multilingual notices.
- [ ] Provide a human-assistance and challenge route.
- [ ] Validate performance, bias, and scientific limitations.
- [ ] Train reviewers and frontline staff.
- [ ] Contract for vendor transparency, audit rights, and change notification.
- [ ] Monitor notice delivery, complaints, overrides, and performance.
- [ ] Suspend the system when legal, notice, performance, or safeguard controls fail.

## 68.24 Key Takeaway

Transparency begins before exposure, but compliance begins even earlier—with the decision whether the system may lawfully and responsibly be used at all.

A notice cannot legalize a prohibited use, validate an unreliable inference, or transfer accountability to a machine.

## 68.25 Official Sources

- Regulation (EU) 2024/1689, including Article 5, Article 50, and relevant definitions.
- European Commission, Guidelines on transparency obligations for providers and deployers of AI systems, published 20 July 2026.
- European Commission, Quick Facts: Transparency rules for AI systems.

> **Legal update note:** The legal baseline, application dates, definitions, and Commission guidance must be reverified against the current consolidated Regulation and official EU publications immediately before final publication or operational reliance.
