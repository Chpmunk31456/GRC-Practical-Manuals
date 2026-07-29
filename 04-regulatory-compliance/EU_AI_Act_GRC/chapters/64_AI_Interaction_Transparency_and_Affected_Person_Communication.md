# 64. AI Interaction Transparency and Affected-Person Communication

**Status:** Draft for owner review  
**Primary legal basis:** Regulation (EU) 2024/1689, Article 50  
**Official implementation guidance:** European Commission Guidelines on transparency obligations for providers and deployers of AI systems, published 20 July 2026  
**Application date:** 2 August 2026, subject to the limited transitional rule applicable to certain marking obligations for systems placed on the market before that date

> **Core principle:** People should not have to guess whether they are interacting with AI, whether content was generated or manipulated by AI, or how to reach a qualified human when the interaction materially affects them.

## 64.1 Why transparency matters

Transparency is not a decorative notice added after a system has been built. It is a governance control that helps people understand what they are dealing with, calibrate their trust, avoid deception, and decide whether to rely on, question, or escalate an AI-supported interaction.

For an organization, transparency also creates evidence. A well-designed notice shows that the organization identified the applicable AI role, understood the interaction context, considered affected-person risks, approved the wording, tested accessibility, and monitored whether the notice remained effective after deployment.

A technically accurate notice can still fail if it is hidden, delayed, vague, unreadable, inaccessible, or contradicted by the interface. The practical test is simple:

> **Would a reasonably attentive person understand, at the right time, that AI is involved and what options remain available to them?**

## 64.2 Binding requirement

Article 50 establishes transparency obligations for specified providers and deployers of AI systems.

Relevant obligations include:

- providers must design certain AI systems that directly interact with natural persons so that those persons are informed that they are interacting with AI, unless this is obvious in the circumstances;
- providers of certain generative or synthetic-content systems must support reliable identification of AI-generated or manipulated content through machine-readable marking, subject to stated exceptions;
- deployers must disclose specified uses of emotion-recognition or biometric-categorisation systems;
- deployers must disclose deepfakes;
- deployers must disclose certain AI-generated or manipulated text published to inform the public on matters of public interest when it has not undergone human review or editorial control.

The legal assessment must be based on the actual facts, role, system design, deployment context, content type, and applicable exception. This chapter does not assume that every AI use requires the same notice.

## 64.3 Plain-language explanation

The organization must answer five questions before release:

1. **Is a person directly interacting with AI?**
2. **Is AI-generated or manipulated content being produced or published?**
3. **Is the organization acting as provider, deployer, or both?**
4. **Does a specific disclosure, marking, or labeling obligation apply?**
5. **Can the person understand the notice and reach a human when needed?**

The answer must not be left to a product team after launch. It should be documented during intake, classification, design, testing, and change management.

## 64.4 GlobalWay Travel Services example

GlobalWay operates a traveler-support assistant that answers itinerary questions, proposes alternative flights, explains baggage rules, summarizes supplier policies, and routes selected cases to human travel consultants.

When a traveler opens the assistant, the first interaction states:

> **You are chatting with GlobalWay’s AI travel assistant. It can help with routine travel questions and recommendations. For urgent, safety-related, accessibility, medical, disputed, or complex matters, request a human travel consultant.**

The interface provides a persistent **Talk to a person** option.

The assistant may:

- answer routine itinerary questions;
- summarize approved airline or hotel information;
- propose nonbinding options;
- gather information for a human consultant;
- route cases according to approved criteria.

A human must decide or intervene when the matter involves:

- traveler safety;
- accessibility or disability accommodation;
- medical needs;
- stranded minors;
- disputed refund or reimbursement decisions;
- denied boarding or significant disruption;
- contractual exceptions;
- suspected fraud requiring adverse action;
- low-confidence or conflicting information;
- a traveler request for human review.

## 64.5 Required control pattern

### Requirement

Determine which Article 50 obligations apply to each AI system and implement the required notice, marking, or disclosure before production use.

### Plain-language explanation

People must receive the right information at the right time. A notice is ineffective when it appears only in terms and conditions, disappears before the interaction begins, uses unclear language, or gives no practical way to challenge or escalate the outcome.

### Travel-agency example

GlobalWay displays an AI-interaction notice when the traveler enters the support assistant. If the assistant generates a proposed customer-facing disruption message, the message is either human-reviewed before release or clearly handled according to the applicable synthetic-content and disclosure rules.

### Control activity

The product owner, legal or compliance reviewer, privacy reviewer, accessibility reviewer, and business owner jointly approve a documented Transparency Assessment before launch.

The assessment must identify:

- the AI system and intended purpose;
- provider and deployer roles;
- affected persons;
- interaction and content types;
- applicable Article 50 paragraph;
- applicable exception or transitional rule;
- required notice, marking, or label;
- placement, timing, language, and accessibility requirements;
- human-contact or escalation route;
- evidence owner;
- review frequency;
- change triggers.

### Evidence

- approved Transparency Assessment;
- legal and compliance review record;
- notice and label wording history;
- interface screenshots or recordings;
- accessibility test results;
- localization review results;
- machine-readable marking test evidence, where applicable;
- human-escalation test records;
- deployment approvals;
- monitoring data;
- complaints, incidents, and corrective actions;
- change-management records.

### Audit test

The auditor should:

1. select a sample of traveler-facing AI systems;
2. verify the organization’s provider/deployer role determination;
3. inspect the applicable Article 50 assessment;
4. observe the live interaction from a user’s perspective;
5. confirm the notice appears at the appropriate time;
6. test whether the notice is understandable and accessible;
7. test the human-contact route;
8. verify machine-readable marking or labeling controls where applicable;
9. trace evidence to current production versions;
10. inspect complaints, changes, and corrective actions.

## 64.6 Notice design standard

An effective AI-interaction notice should be:

- **timely:** presented before or at the start of the interaction;
- **clear:** written in plain language;
- **specific:** identifying the nature of the AI involvement;
- **visible:** not buried in legal text or hidden behind multiple clicks;
- **persistent or recoverable:** available again during the interaction;
- **accessible:** usable with assistive technologies and across relevant devices;
- **localized:** reviewed for language accuracy and cultural clarity;
- **actionable:** explaining how to obtain human assistance when appropriate;
- **consistent:** aligned across web, mobile, chat, voice, email, and other channels;
- **version-controlled:** linked to approved wording and deployment evidence.

## 64.7 Human communication and escalation

Article 50 transparency and human oversight should operate together.

The notice should not create the false impression that every AI interaction automatically receives human review. The organization must state the actual operating model accurately.

Where human review is available, the process should define:

- how a person requests it;
- expected response route;
- urgency classification;
- required reviewer competence;
- authority to correct or override;
- evidence retained;
- fallback when automated escalation fails.

For urgent travel events, the escalation route must not depend entirely on the AI system whose performance is in question.

## 64.8 Affected-person concerns

The chapter should directly answer the questions a traveler, employee, applicant, supplier, or other affected person may reasonably ask:

- Am I speaking with a person or an AI system?
- Is this recommendation final?
- Will a qualified person review this before it affects me?
- Can I correct inaccurate information?
- Can I challenge the outcome?
- Can I ask for a human?
- Is this image, audio, video, or text authentic?
- Was this content generated or materially altered by AI?
- Who is responsible for the result?
- What happens if the AI is wrong?

## 64.9 Prohibited design patterns

The organization should prohibit:

- hiding the AI notice in terms and conditions;
- presenting a human name or avatar in a misleading way;
- making a human-contact option functionally unavailable;
- using a label that disappears before the person can read it;
- relying only on color to communicate AI involvement;
- using technical language such as “algorithmic orchestration layer” instead of plain language;
- claiming human review when none occurs;
- labeling all content generically without assessing the actual legal requirement;
- removing notices during interface redesign without reassessment;
- treating a vendor statement as sufficient evidence without testing the deployed implementation.

## 64.10 Control objectives

| Control ID | Control objective | Owner | Frequency | Evidence |
|---|---|---|---|---|
| EUAI-TR-01 | Identify Article 50 applicability for every relevant AI system | AI Governance | At intake and change | Transparency Assessment |
| EUAI-TR-02 | Approve clear and timely AI-interaction notices | Product Owner | Before release | Approved wording and screenshots |
| EUAI-TR-03 | Implement required synthetic-content marking or labeling | Technical Owner | Continuous | Technical test results |
| EUAI-TR-04 | Provide accessible and localized notices | Accessibility and Content Owners | Before release and annually | Accessibility and language review |
| EUAI-TR-05 | Provide effective human escalation where required by policy or risk | Business Owner | Continuous | Escalation tests and logs |
| EUAI-TR-06 | Monitor notice effectiveness, complaints, and failures | Compliance | Quarterly | Metrics and issue records |
| EUAI-TR-07 | Reassess transparency after material changes | Change Advisory Authority | Per change | Change assessment |

## 64.11 Metrics

Useful indicators include:

- percentage of relevant systems with an approved Transparency Assessment;
- percentage of notices passing accessibility testing;
- percentage of sampled interactions displaying the approved notice;
- human-escalation success rate;
- average time to reach a human for high-priority cases;
- number of complaints alleging deception or unclear AI use;
- number of production changes that required notice reassessment;
- number of synthetic-content outputs failing marking or labeling tests;
- number of localization defects;
- number of corrective actions overdue.

Metrics should not be treated as proof of compliance by themselves. A 100% completion rate is meaningless if the assessments are superficial or the live interface does not match the approved design.

## 64.12 Original explanatory cartoon concept

**Title:** *The Human Option*

**Scene:** A traveler stands at an airport help desk facing three screens. The first says, “AI Assistant.” The second says, “Human Assistance.” The third says, “AI Assistant Explaining Why Human Assistance Is Currently Unavailable.” A tired human travel consultant stands behind the screens holding a handwritten sign: “I’m right here.”

**Caption:** “The escalation path passed every design review.”

**Concept explained:** A documented human-escalation control is ineffective when the person cannot realistically reach the human reviewer.

**Alt text:** Single-panel workplace cartoon showing a traveler blocked by several automated support screens while an available human consultant stands visibly behind them.

**Use restriction:** The cartoon supports the control explanation but does not replace the formal process diagram, notice standard, or audit procedure.

## 64.13 Formal process graphic

The corresponding formal process diagram should show:

**AI use identified → role and Article 50 assessment → notice/marking requirement determined → wording and technical design approved → accessibility and localization tested → production deployment → monitoring and complaints → reassessment after change**

The graphic must include decision points for:

- direct human interaction;
- AI-generated or manipulated content;
- provider versus deployer role;
- applicable exception;
- human-review or editorial-control status;
- required disclosure, marking, or label;
- escalation and corrective action.

## 64.14 Management review questions

Senior management should ask:

1. Which of our AI systems interact directly with people?
2. Which systems generate or manipulate customer-facing content?
3. Have we documented our provider and deployer roles?
4. Can affected people reliably reach a qualified human?
5. Are notices accessible in every supported channel and language?
6. Have we tested the live implementation rather than only reviewing policy text?
7. How do we detect removed, broken, or outdated notices?
8. How do we monitor complaints alleging deception or unclear AI use?
9. What changes trigger reassessment?
10. Who is accountable when the notice or escalation path fails?

## 64.15 Publication control

Before final publication, verify this chapter against:

- the current consolidated text of Regulation (EU) 2024/1689;
- the European Commission’s final Article 50 transparency guidelines;
- the current Code of Practice on Transparency of AI-Generated Content and its official adequacy status;
- any binding amendment, implementing act, court decision, or supervisory guidance affecting Article 50.

### Official sources

- Regulation (EU) 2024/1689: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- European Commission Article 50 guidelines: https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems
- Commission transparency overview: https://digital-strategy.ec.europa.eu/en/policies/guidelines-transparency-ai-generated-content
- Quick facts on transparency rules: https://digital-strategy.ec.europa.eu/en/factpages/quick-facts-transparency-rules-ai-systems

---

**Drafting note:** Legal requirements, official guidance, and recommended organizational practices must remain clearly distinguished during final editorial review.
