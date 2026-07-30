# Appendix D — Prohibited-Practice Checklist

## Purpose

Use this checklist before approval, procurement, development, deployment, or material modification to identify AI practices that may be prohibited under Article 5 of Regulation (EU) 2024/1689, as amended. Escalate every **Yes** or **Uncertain** answer for qualified legal review. This checklist is an operational aid, not a substitute for the regulation, current consolidated text, applicable national law, or legal advice.

Do not classify a use solely from a technology label. Test every relevant legal element, exception, safeguard, and deployment fact.

## Assessment information

- System or use case:
- Inventory ID:
- Business owner:
- Technical owner:
- Provider/vendor:
- Actor role or roles:
- Legal entities and jurisdictions:
- Intended purpose:
- Actual and reasonably foreseeable use:
- Affected persons and vulnerable groups:
- Deployment context:
- Assessor and date:
- Evidence repository link:

## Instructions

For every question:

1. answer **Yes**, **No**, or **Uncertain**;
2. cite the supporting evidence;
3. identify the exact Article 5 point being tested;
4. record any claimed exception and its evidence;
5. document the reviewer, date, and disposition.

A **No** answer must be supported by facts. “Vendor says compliant” is not sufficient evidence.

## A. Manipulative, subliminal, and deceptive techniques

- Does the system use subliminal techniques beyond a person’s consciousness, purposefully manipulative techniques, or deceptive techniques?
- Does the technique have the objective or effect of materially distorting behaviour?
- Does it appreciably impair the ability to make an informed decision?
- Could it cause a person to take a decision they would not otherwise have taken?
- Does the use cause, or is it reasonably likely to cause, significant harm?
- Have persuasion, recommendation, personalisation, interface design, and deceptive manipulation been distinguished factually?
- Have vulnerable-user, accessibility, and dark-pattern risks been tested?

**Evidence:** design records, prompts, interfaces, behavioural testing, harm analysis, user research, legal review.

## B. Exploitation of vulnerabilities

- Does the system exploit vulnerability due to age, disability, or a specific social or economic situation?
- What feature, message, ranking, timing, or interaction mechanism performs the exploitation?
- Could the use materially distort behaviour?
- Does the use cause, or is it reasonably likely to cause, significant harm?
- Has legitimate accessibility, assistance, accommodation, or protective treatment been distinguished from exploitation?

**Evidence:** population analysis, segmentation logic, accessibility review, targeting rules, harm scenarios, safeguards.

## C. Social scoring

- Does the system evaluate or classify natural persons or groups over time based on social behaviour or known, inferred, or predicted personal or personality characteristics?
- Does the score lead to detrimental or unfavourable treatment?
- Is the treatment in a context unrelated to the context in which the data were generated or collected?
- Is the treatment unjustified or disproportionate to the social behaviour or its gravity?
- Are loyalty, fraud, safety, reputation, eligibility, or risk scores reused across contexts?
- Can affected persons understand, challenge, and correct the score or underlying data?

**Evidence:** feature inventory, scoring logic, original data context, downstream-use map, proportionality analysis, adverse-impact tests.

## D. Individual criminal-offence risk prediction

- Is the system used to assess or predict the risk that a natural person will commit a criminal offence?
- Is the prediction based solely on profiling or assessment of personality traits or characteristics?
- If AI supports a human assessment, is that assessment already based on objective and verifiable facts directly linked to criminal activity?
- Are area, group, event, or operational analytics being used as a proxy for an individual criminal-risk prediction?
- Are the role of AI and the independent human assessment documented in decision logs?

**Evidence:** input features, model purpose, objective-fact records, human workflow, profiling assessment, decision logs.

## E. Untargeted facial-image scraping

- Does the system create or expand a facial-recognition database?
- Are facial images obtained through untargeted scraping from the internet?
- Are facial images obtained through untargeted scraping from closed-circuit television footage?
- Are collection method, targeting criteria, scale, source, and database function documented?
- Has the organization independently verified supplier representations about training and reference-image sources?

**Evidence:** source register, acquisition method, crawler configuration, vendor attestations, technical tests, biometric-data assessment.

## F. Emotion recognition in workplaces and educational institutions

- Does the system infer emotions of natural persons?
- Is it deployed in a workplace?
- Is it deployed in an educational institution?
- Is a medical or safety exception claimed?
- Is the claimed medical or safety purpose genuine, necessary, proportionate, and documented?
- Could a system labelled sentiment, engagement, fatigue, attention, stress, or behavioural analytics perform emotion inference in practice?
- If the use is not prohibited, have high-risk, transparency, employment, education, privacy, and discrimination obligations been assessed?

**Evidence:** capability description, deployment context, exception analysis, necessity assessment, worker/student consultation, transparency controls.

## G. Biometric categorisation using protected or sensitive characteristics

- Does the system categorise natural persons individually based on biometric data?
- Does it deduce or infer a protected or sensitive characteristic listed in the current legal text?
- Have biometric verification, identification, and categorisation been distinguished?
- Is an exception claimed for labelling or filtering lawfully acquired biometric datasets in an applicable law-enforcement context?
- Is the claimed exception documented narrowly rather than treated as a general exemption?
- If not prohibited, have high-risk classification and special-category-data restrictions been assessed?

**Evidence:** biometric data flow, inferred-category list, outputs, downstream actions, exception analysis, GDPR assessment, fairness testing.

## H. Real-time remote biometric identification in publicly accessible spaces for law enforcement

- Does the system perform remote biometric identification?
- Is the operation real-time rather than post-event?
- Is it used in a publicly accessible space?
- Is it used for law-enforcement purposes?
- Is one of the narrowly permitted statutory objectives claimed?
- Is strict necessity documented?
- Are seriousness, probability, and scale of harm documented?
- Are effects on rights and freedoms assessed?
- Are temporal, geographic, and personal limits defined?
- Is prior judicial or independent administrative authorisation documented, subject only to the narrow emergency framework?
- Are registration, fundamental-rights assessment, national-law conditions, logging, and post-use review complete?

**Evidence:** operational concept, purpose, authorisation, necessity and proportionality analysis, watchlist governance, accuracy testing, complete logs.

## I. New prohibitions introduced by Regulation (EU) 2026/1744

**Application date control:** Assess adoption and application separately. The relevant amended prohibitions apply from **2 December 2026**.

- Does the system generate non-consensual sexually explicit or intimate content involving an identifiable person?
- Does the system generate child sexual abuse material within the amended statutory wording?
- Are the two prohibited categories analysed separately?
- Is consent, identity, age, source material, output purpose, and foreseeable misuse documented where relevant?
- Does the product include technical, contractual, reporting, and enforcement controls preventing prohibited generation?
- Is the use blocked rather than merely warned when the statutory prohibition is met?

**Evidence:** use-policy controls, model and filter tests, consent records where relevant, age and identity controls, blocked-output logs, incident response.

## J. Proxy, repurposing, and circumvention review

- Does the design indirectly achieve a prohibited outcome through proxies, combined features, workflow integration, or downstream use?
- Could configuration, fine-tuning, prompt templates, plugins, agents, or user instructions enable a prohibited practice?
- Could a lawful pilot be repurposed into a prohibited deployment context?
- Has the supplier contractually restricted prohibited uses and provided enforceable technical controls?
- Are attempted workarounds detected, logged, investigated, and blocked?

## Evidence reviewed

- intended-purpose statement;
- actual and foreseeable-use assessment;
- system design and model documentation;
- data sources, lineage, and feature list;
- user interfaces, instructions, prompts, and workflows;
- vendor documentation, testing rights, and contract;
- demonstrations and independent testing;
- deployment context and affected-population analysis;
- legal and fundamental-rights analysis;
- exceptions, authorisations, and safeguards;
- monitoring, misuse, and repurposing controls.

## Decision

Select one:

- No prohibited practice identified on the verified facts
- Additional evidence required
- Qualified legal review required
- Use must be redesigned or restricted
- Deployment prohibited
- Existing deployment suspended, withdrawn, or decommissioned

## Mandatory escalation triggers

Escalate and do not approve when:

- any statutory element cannot be resolved from verified facts;
- a claimed exception lacks evidence;
- the provider will not disclose relevant functionality or data sources;
- marketing descriptions conflict with observed capability;
- children, workers, students, migrants, criminal suspects, or other vulnerable groups are affected;
- national law may be stricter;
- the system could be repurposed into a prohibited practice;
- a material change affects purpose, context, population, data, geography, capability, or output use.

## Required controls

- Record the exact legal basis and decision rationale.
- Apply technical and contractual use restrictions.
- Block prohibited configurations and outputs.
- Prevent unauthorised repurposing.
- Train users, developers, procurement, and approvers.
- Monitor for misuse, workarounds, and material changes.
- Retain rejection, suspension, withdrawal, and decommissioning evidence.
- Reassess after changes to purpose, data, features, geography, provider, actor role, or affected population.

## Approval

**Qualified legal reviewer:**  
**Compliance reviewer:**  
**Technical reviewer:**  
**Business owner:**  
**Decision:**  
**Article and point assessed:**  
**Exception claimed and evidence:**  
**Conditions:**  
**Next review date or trigger:**  
**Evidence repository:**  
