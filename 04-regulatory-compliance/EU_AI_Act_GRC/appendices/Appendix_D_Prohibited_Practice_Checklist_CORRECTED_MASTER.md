# Appendix D — Prohibited-Practice Checklist

> **Legal status:** Corrected English master. Use the current consolidated Article 5 text, Regulation (EU) 2026/1744 where applicable, and any applicable national law. Every **Yes** or **Uncertain** answer requires qualified legal review. This checklist is an operational aid, not a substitute for the regulation, official consolidated text, authority interpretation, national law, or legal advice.

## Purpose

Use this checklist before approval, procurement, development, piloting, deployment, material modification, repurposing, or geographic expansion to identify AI practices that may be prohibited.

Do not classify a use solely from a technology label, vendor description, or policy statement. Test every relevant legal element, deployment fact, exception, safeguard, affected population, and reasonably foreseeable route to circumvention.

## Assessment information

| Field | Response |
|---|---|
| System or use case | |
| Inventory ID | |
| Business owner | |
| Technical owner | |
| Provider/vendor | |
| Actor role or roles | |
| Legal entities | |
| Jurisdictions | |
| Intended purpose | |
| Actual and reasonably foreseeable use | |
| Affected persons and vulnerable groups | |
| Version, configuration, prompts, tools, and integrations | |
| Deployment context | |
| Current official legal source and application date | |
| Assessor and date | |
| Evidence repository | |

## Instructions

For every screening question:

1. answer **Yes**, **No**, or **Uncertain**;
2. identify the exact Article 5 point and legal element being tested;
3. cite supporting facts and evidence;
4. record any claimed exception, limitation, authorization, and supporting evidence;
5. identify the reviewer, date, decision, restriction, and follow-up action;
6. assess proxy, workflow, configuration, and foreseeable repurposing routes.

A **No** answer must be supported by verified facts. “Vendor says compliant” is not sufficient evidence.

## A. Subliminal, purposefully manipulative, or deceptive techniques

| Question | Yes/No/Uncertain | Evidence and rationale |
|---|---|---|
| Does the system use subliminal techniques beyond a person’s consciousness, purposefully manipulative techniques, or deceptive techniques? | | |
| Does the technique have the objective or effect of materially distorting behaviour? | | |
| Does it appreciably impair the ability to make an informed decision? | | |
| Could it cause a person to take a decision they would not otherwise have taken? | | |
| Does the use cause, or is it reasonably likely to cause, significant harm? | | |
| Have persuasion, recommendation, personalization, interface design, and deceptive manipulation been distinguished factually? | | |
| Have vulnerable-user, accessibility, dark-pattern, and coercive-design risks been tested? | | |

**Evidence examples:** design records, prompts, interfaces, behavioural testing, harm analysis, user research, accessibility review, legal analysis.

## B. Exploitation of vulnerabilities

| Question | Yes/No/Uncertain | Evidence and rationale |
|---|---|---|
| Does the system exploit vulnerability due to age, disability, or a specific social or economic situation? | | |
| What feature, message, ranking, timing, targeting, or interaction mechanism performs the exploitation? | | |
| Could the use materially distort behaviour? | | |
| Does the use cause, or is it reasonably likely to cause, significant harm? | | |
| Have legitimate accessibility, assistance, accommodation, protection, or age-appropriate design been distinguished from exploitation? | | |

**Evidence examples:** population analysis, segmentation logic, targeting rules, accessibility review, harm scenarios, safeguards, user research.

## C. Social scoring

| Question | Yes/No/Uncertain | Evidence and rationale |
|---|---|---|
| Does the system evaluate or classify natural persons or groups over time based on social behaviour or known, inferred, or predicted personal or personality characteristics? | | |
| Does the score lead to detrimental or unfavourable treatment? | | |
| Is the treatment in a context unrelated to the context in which the data were generated or collected? | | |
| Is the treatment unjustified or disproportionate to the social behaviour or its gravity? | | |
| Are loyalty, fraud, safety, reputation, eligibility, or risk scores reused across contexts? | | |
| Can affected persons understand, challenge, and correct the score or underlying data? | | |

**Evidence examples:** feature inventory, scoring logic, original data context, downstream-use map, proportionality analysis, adverse-impact tests, appeal records.

## D. Individual criminal-offence risk prediction

| Question | Yes/No/Uncertain | Evidence and rationale |
|---|---|---|
| Is the system used to assess or predict the risk that a natural person will commit a criminal offence? | | |
| Is the prediction based solely on profiling or assessment of personality traits or characteristics? | | |
| If AI supports a human assessment, is that assessment already based on objective and verifiable facts directly linked to criminal activity? | | |
| Are area, group, event, or operational analytics being used as a proxy for individual criminal-risk prediction? | | |
| Are the role of AI and the independent human assessment documented in decision logs? | | |

**Evidence examples:** input features, intended purpose, objective-fact records, human workflow, profiling analysis, decision logs.

## E. Untargeted facial-image scraping

| Question | Yes/No/Uncertain | Evidence and rationale |
|---|---|---|
| Does the system create or expand a facial-recognition database? | | |
| Are facial images obtained through untargeted scraping from the internet? | | |
| Are facial images obtained through untargeted scraping from closed-circuit television footage? | | |
| Are collection method, targeting criteria, scale, source, and database function documented? | | |
| Has the organization independently verified supplier representations about training and reference-image sources? | | |

**Evidence examples:** source register, acquisition method, crawler configuration, supplier evidence, technical testing, biometric-data assessment.

## F. Emotion recognition in workplaces and educational institutions

| Question | Yes/No/Uncertain | Evidence and rationale |
|---|---|---|
| Does the system infer emotions of natural persons? | | |
| Is it deployed in a workplace? | | |
| Is it deployed in an educational institution? | | |
| Is a medical or safety exception claimed? | | |
| Is the claimed medical or safety purpose genuine, necessary, proportionate, narrow, and documented? | | |
| Could a system labelled sentiment, engagement, fatigue, attention, stress, or behavioural analytics perform emotion inference in practice? | | |
| If the use is not prohibited, have high-risk, transparency, employment, education, privacy, consultation, and discrimination obligations been assessed? | | |

**Evidence examples:** capability description, deployment context, exception analysis, necessity assessment, worker/student consultation, transparency controls.

## G. Biometric categorisation using protected or sensitive characteristics

| Question | Yes/No/Uncertain | Evidence and rationale |
|---|---|---|
| Does the system categorise natural persons individually based on biometric data? | | |
| Does it deduce or infer a protected or sensitive characteristic listed in the current legal text? | | |
| Have biometric verification, identification, and categorisation been distinguished? | | |
| Is an exception claimed for labelling or filtering lawfully acquired biometric datasets in an applicable law-enforcement context? | | |
| Is the claimed treatment documented narrowly rather than treated as a general exemption? | | |
| If not prohibited, have high-risk classification and special-category-data restrictions been assessed? | | |

**Evidence examples:** biometric data flow, inferred-category list, outputs, downstream actions, exception analysis, GDPR assessment, fairness testing.

## H. Real-time remote biometric identification in publicly accessible spaces for law enforcement

| Question | Yes/No/Uncertain | Evidence and rationale |
|---|---|---|
| Does the system perform remote biometric identification? | | |
| Is the operation real-time rather than post-event? | | |
| Is it used in a publicly accessible space? | | |
| Is it used for law-enforcement purposes? | | |
| Is one of the narrowly permitted statutory objectives claimed? | | |
| Is strict necessity documented? | | |
| Are seriousness, probability, and scale of harm documented? | | |
| Are effects on rights and freedoms assessed? | | |
| Are temporal, geographic, and personal limits defined? | | |
| Is prior judicial or independent administrative authorization documented, subject only to the narrow emergency framework? | | |
| Are registration, fundamental-rights assessment, national-law conditions, logging, and post-use review complete? | | |

**Evidence examples:** operational concept, purpose, authorization, necessity and proportionality analysis, watchlist governance, accuracy testing, complete logs.

## I. Additional prohibitions introduced by Regulation (EU) 2026/1744

**Application-date control:** Assess adoption and application separately. Use the official amended text and verify the applicable **2 December 2026** date before relying on this checklist.

| Question | Yes/No/Uncertain | Evidence and rationale |
|---|---|---|
| Does the system generate non-consensual sexually explicit or intimate content involving an identifiable person? | | |
| Does the system generate child sexual abuse material within the amended statutory wording? | | |
| Are the two prohibited categories analysed separately? | | |
| Are consent, identity, age, source material, output purpose, and foreseeable misuse documented where relevant? | | |
| Does the product include technical, contractual, reporting, and enforcement controls preventing prohibited generation? | | |
| Is the use blocked rather than merely warned when the statutory prohibition is met? | | |

**Evidence examples:** use-policy controls, model and filter tests, consent records where relevant, age and identity controls, blocked-output logs, incident response.

## J. Proxy, repurposing, and circumvention review

| Question | Yes/No/Uncertain | Evidence and rationale |
|---|---|---|
| Does the design indirectly achieve a prohibited outcome through proxies, combined features, workflow integration, or downstream use? | | |
| Could configuration, fine-tuning, prompt templates, plugins, agents, or user instructions enable a prohibited practice? | | |
| Could a lawful pilot be repurposed into a prohibited deployment context? | | |
| Has the supplier contractually restricted prohibited uses and provided enforceable technical controls? | | |
| Are attempted workarounds detected, logged, investigated, and blocked? | | |
| Can geographic, user, data, or feature restrictions be technically enforced? | | |

## Evidence reviewed

- intended-purpose statement;
- actual and reasonably foreseeable-use assessment;
- system, model, prompt, tool, and agent documentation;
- data sources, lineage, and feature list;
- user interfaces, instructions, workflows, and demonstrations;
- supplier documentation, testing rights, contracts, and change notices;
- independent testing and observed behaviour;
- deployment context and affected-population analysis;
- legal and fundamental-rights analysis;
- exceptions, authorizations, necessity, and proportionality records;
- monitoring, misuse, proxy, repurposing, and circumvention controls.

## Decision

- [ ] No prohibited practice identified on verified facts
- [ ] Additional evidence required
- [ ] Qualified legal review required
- [ ] Use must be redesigned or restricted
- [ ] Deployment prohibited
- [ ] Existing deployment suspended, withdrawn, or decommissioned

**Article point and exact elements assessed:**  
**Decision rationale:**  
**Exception, limitation, or authorization claimed:**  
**Supporting evidence:**  
**Restrictions or required redesign:**  
**Residual uncertainty:**  

## Mandatory escalation triggers

Escalate and do not approve when:

- any statutory element cannot be resolved from verified facts;
- a claimed exception, limitation, authorization, or safeguard lacks evidence;
- the provider will not disclose relevant functionality, data sources, or observed limitations;
- marketing descriptions conflict with observed capability;
- children, workers, students, migrants, criminal suspects, or other vulnerable groups are affected;
- national law may be stricter or impose separate conditions;
- the system could be repurposed into a prohibited practice;
- technical restrictions cannot reliably block prohibited use;
- a material change affects purpose, context, population, data, geography, capability, actor role, or output use.

## Required controls

- Record the exact legal basis, factual findings, and decision rationale.
- Apply technical, contractual, organizational, and access restrictions.
- Block prohibited configurations, workflows, users, jurisdictions, and outputs.
- Prevent unauthorized repurposing and detect circumvention attempts.
- Train developers, procurement, users, approvers, support, and incident personnel.
- Monitor for misuse, workarounds, material changes, and supplier updates.
- Preserve rejection, suspension, withdrawal, decommissioning, testing, and incident evidence.
- Reassess after changes to purpose, data, features, geography, provider, actor role, affected population, or law.

## GlobalWay Travel Services example

GlobalWay reviews an employee “engagement” tool that claims to measure fatigue and sentiment from voice and video. Testing shows that it infers emotional states in a workplace context. GlobalWay suspends the pilot, preserves supplier and test evidence, and escalates for qualified legal review. The supplier’s general compliance assurance is rejected as insufficient because the observed capability and deployment facts control the analysis.

## Approval

| Role | Name | Decision | Date |
|---|---|---|---|
| Qualified legal reviewer | | | |
| Compliance reviewer | | | |
| Technical reviewer | | | |
| Business owner | | | |
| Privacy/HR/Security reviewer, where applicable | | | |

**Conditions:**  
**Actions and due dates:**  
**Next review date or trigger:**  
**Evidence repository:**  
**Assessment version:**  

## Primary legal references

- Regulation (EU) 2024/1689, as amended: Article 5 and all applicable definitions, exceptions, safeguards, effective dates, and national-law conditions.
- Regulation (EU) 2026/1744 where applicable.
- Regulation (EU) 2016/679 and applicable employment, equality, accessibility, criminal-procedure, consumer-protection, child-protection, cybersecurity, product-safety, and national law.
- Current consolidated official texts control over this checklist and all earlier summaries.