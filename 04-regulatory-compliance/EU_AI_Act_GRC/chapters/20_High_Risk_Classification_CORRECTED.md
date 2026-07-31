# Chapter 20 — High-Risk Classification

## Publication status

**Legally corrected English master text.** This chapter supersedes conflicting high-risk classification language in earlier drafts until all source files are reconciled.

## Purpose

This chapter explains how to determine whether an AI system is high-risk under Article 6 of Regulation (EU) 2024/1689, as amended by Regulation (EU) 2026/1744.

## Requirement

Organizations must perform and document a current high-risk classification for each material AI system before deployment and after relevant changes.

Classification must distinguish:

- Article 6(1) systems connected to products covered by Annex I Union harmonisation legislation;
- Article 6(2) systems used for Annex III purposes;
- systems that appear within Annex III but may qualify for the Article 6(3) exception, where applicable;
- systems outside Article 6 that may still have transparency, GPAI, privacy, employment, consumer, safety, cybersecurity, or sector obligations.

## Plain-English explanation

“High-risk” is a legal classification, not a general description of a system that seems important or dangerous. The analysis must follow the Article 6 pathway and the relevant annex.

A system may be operationally critical without being high-risk under Article 6. Conversely, a system may be legally high-risk even when the organization believes its internal risk score is moderate.

## Classification pathway

### Step 1 — Confirm the system and intended purpose

Document:

- the AI system and model components;
- intended purpose;
- users and affected persons;
- decisions or outputs supported;
- deployment countries and sectors;
- provider and deployer roles;
- product integration;
- material vendor dependencies.

### Step 2 — Test Article 6(1) and Annex I

Assess whether the AI system:

- is intended to be used as a safety component of a product covered by Annex I; or
- is itself a product covered by Annex I;
- and is required to undergo a third-party conformity assessment under the applicable product legislation.

The amended application date for the Chapter III, Sections 1–3 requirements governing Article 6(1)/Annex I systems is **2 August 2028**. This delayed date must not be used to postpone independently applicable obligations.

### Step 3 — Test Article 6(2) and Annex III

Assess whether the intended purpose falls within an Annex III category, including the current amended categories and conditions.

The amended application date for the Chapter III, Sections 1–3 requirements governing Article 6(2)/Annex III systems is **2 December 2027**.

### Step 4 — Assess any Article 6(3) exception

Where legally available, determine whether the system does not pose a significant risk of harm to health, safety, or fundamental rights because it does not materially influence the outcome of decision-making and meets the statutory conditions.

Do not apply this exception when the system performs profiling of natural persons where the Act excludes reliance on the exception.

The organization must retain a reasoned assessment and be prepared to provide it to a competent authority.

### Step 5 — Record the outcome

Use one of these controlled outcomes:

- Article 6(1)/Annex I high-risk;
- Article 6(2)/Annex III high-risk;
- Annex III use with documented Article 6(3) exception;
- not high-risk under Article 6 but subject to other AI Act duties;
- classification deferred pending legal or technical evidence;
- deployment prohibited or suspended.

## Effective-date rule

The later high-risk dates apply narrowly to the relevant Chapter III, Sections 1–3 requirements. They do not automatically delay:

- AI-literacy duties;
- prohibited-practice restrictions;
- GPAI obligations;
- transparency obligations;
- governance and authority provisions;
- GDPR, employment, equality, consumer, safety, cybersecurity, or sector-law duties;
- contractual commitments;
- internal risk controls required to prevent harm.

## GlobalWay Travel Services example

GlobalWay assesses a recruitment-screening system intended to rank applicants for employment decisions. The intended purpose falls within an Annex III employment category. GlobalWay classifies the system as Article 6(2) high-risk and maps the amended 2 December 2027 date to the applicable Chapter III requirements.

GlobalWay does not treat the date as permission to defer privacy, discrimination, employment-law, AI-literacy, vendor, security, or human-review controls. Those controls remain governed by their own legal and operational dates.

## Control activities

- Require a documented Article 6 classification before approval.
- Link the assessment to the current Annex I and Annex III text.
- Require Legal approval for Article 6(3) exceptions.
- Record intended purpose and prevent unapproved repurposing.
- Reassess after model, data, workflow, vendor, jurisdiction, product, or user changes.
- Map classification outcomes to the correct implementation date.
- Retain evidence supporting non-high-risk determinations.

## Evidence

- intended-purpose statement;
- Article 6 worksheet;
- Annex I and Annex III mapping;
- product-law analysis;
- Article 6(3) assessment, if applicable;
- legal approval;
- deployment restrictions;
- change and reassessment history;
- article-to-control mapping.

## Audit tests

1. Trace selected systems through each Article 6 classification step.
2. Verify Annex I and Annex III references use the amended text.
3. Review Article 6(3) exception evidence and legal approval.
4. Confirm profiling systems are not incorrectly excluded.
5. Verify the 2027 and 2028 dates are applied only to the relevant requirements.
6. Confirm non-high-risk systems are still assessed for other obligations.
7. Test whether changes trigger reclassification.

## Management checklist

- Is the intended purpose documented accurately?
- Have Article 6(1) and Article 6(2) both been tested?
- Is any Article 6(3) exception fully supported?
- Are the 2027 and 2028 dates used narrowly?
- Are other legal duties tracked independently?

## Figure specification — High-Risk Classification Path

Create a decision tree beginning with intended purpose, then separate Article 6(1)/Annex I and Article 6(2)/Annex III paths, followed by the Article 6(3) exception analysis, controlled classification outcomes, and reassessment triggers.

**Alt text:** High-risk AI classification decision tree testing Article 6(1) and Annex I product systems, Article 6(2) and Annex III use cases, the Article 6(3) exception, final classification outcomes, implementation dates, and reassessment triggers.