# Chapter 135 — Transparency Readiness Roadmap

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 135 draft language.

## Purpose

This chapter provides a practical roadmap for identifying, designing, implementing, testing, and maintaining transparency obligations for AI systems and AI-generated or manipulated content.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations must identify which transparency duties apply to each system, actor, use case, output, and deployment context, then implement controls so required notices, disclosures, markings, and instructions are accurate, timely, accessible, understandable, technically effective, and consistent with actual system behaviour.

## Plain-English explanation

Transparency is not satisfied by placing a generic statement in a privacy policy. Duties differ by role and use and may include informing people that they are interacting with AI, providing information and instructions for high-risk systems, informing workers or affected persons where required, marking AI-generated or manipulated content, disclosing deepfakes or certain public-interest text, and informing persons exposed to emotion-recognition or biometric-categorisation systems.

## Phase 1: inventory transparency scenarios

Identify:

- systems that interact directly with natural persons;
- high-risk systems requiring instructions or deployer communications;
- emotion-recognition or biometric-categorisation uses;
- synthetic audio, image, video, and text generation;
- deepfake and manipulated-content scenarios;
- public-interest text and editorial-responsibility scenarios;
- employee, applicant, traveler, customer, supplier, and public interactions;
- channels, languages, jurisdictions, audience characteristics, and accessibility needs.

## Phase 2: determine the legal trigger and responsible actor

For each use case, document:

1. the applicable legal or policy basis;
2. the responsible provider, deployer, importer, distributor, product manufacturer, or other actor;
3. the intended recipient or affected audience;
4. when the information must be delivered;
5. required content, format, and channel;
6. exceptions, exclusions, and effective dates;
7. machine-readable or technical marking requirements;
8. supplier and downstream-information dependencies;
9. accountable owner, legal reviewer, and approver;
10. required evidence, monitoring, and reassessment triggers.

## Phase 3: design notices, disclosures, and instructions

Transparency measures should be:

- clear, concise, and factually accurate;
- distinguishable from unrelated terms and marketing language;
- presented early enough to influence the person's understanding or choice;
- appropriate to the audience and operating context;
- accessible to persons with disabilities;
- available in relevant languages and channels;
- consistent across interfaces, documents, and support channels;
- aligned with actual purpose, limitations, data use, oversight, and complaint routes;
- supported by a meaningful human-contact or escalation path where appropriate.

## Phase 4: implement technical and release controls

Implement as applicable:

- visible AI-interaction notices;
- persistent or readily accessible disclosure indicators;
- machine-readable marking of synthetic content where legally required and technically feasible;
- metadata and provenance controls;
- deepfake and manipulated-content labels;
- affected-person and worker communications;
- human-support and escalation options;
- lawful logging of notice presentation and system version;
- release gates that prevent deployment without approved transparency controls.

## Phase 5: test effectiveness

Test:

- notice timing, placement, and visibility;
- comprehension by intended audiences;
- accessibility and assistive-technology compatibility;
- language quality and localization accuracy;
- mobile, web, voice, document, and embedded-channel presentation;
- technical-marking persistence after normal processing or distribution;
- user ability to obtain human support or challenge where applicable;
- consistency between actual system behaviour and the approved disclosure;
- linkage between notices, markings, instructions, and the deployed version.

## Phase 6: monitor and maintain

Reassess after:

- model, interface, purpose, or workflow changes;
- new content-generation or manipulation functions;
- expansion to new countries, populations, or languages;
- complaints, accessibility defects, or evidence of user confusion;
- supplier or platform changes;
- changes in legal requirements, implementing acts, or authoritative guidance;
- reclassification, substantial modification, or new high-risk use.

## GlobalWay Travel Services example

GlobalWay maps its traveler chatbot, recruitment tool, synthetic marketing content, and call-centre emotion-analysis pilot. The chatbot displays an AI notice before the first response and provides a visible route to a human consultant. Applicant notices are reviewed against the actual recruitment workflow. Generated destination images receive required marking and disclosure controls.

Accessibility testing shows that one notice is not announced correctly by screen readers. Release is paused until the defect is corrected, retested, and linked to the approved production version. A supplier-change gate requires renewed transparency review whenever the underlying model or interface changes.

## Control activities

- Maintain a transparency applicability matrix and notice library.
- Distinguish actor-specific duties and effective dates.
- Approve notices, instructions, and technical markings before release.
- Test timing, comprehension, accessibility, localization, and technical persistence.
- Reconcile disclosures with actual functions, limitations, data use, and oversight.
- Maintain supplier evidence and downstream information.
- Monitor complaints, confusion, and disclosure failures.
- Trigger reassessment after material change.
- Preserve approved versions, implementation evidence, and corrective actions.

## Evidence

- transparency applicability matrix;
- legal-role and use-case analysis;
- approved notice, disclosure, and instruction text;
- user-interface, document, and content examples;
- accessibility, comprehension, and language tests;
- machine-readable marking and provenance test results;
- supplier and downstream documentation;
- deployment, release, and version records;
- human-escalation test results;
- change and reassessment history;
- complaint, defect, and remediation records.

## Audit tests

1. Select AI systems and verify transparency applicability was assessed using the current legal text.
2. Confirm the correct actor, recipient, timing, channel, and effective date were identified.
3. Compare approved disclosures and instructions with actual system behaviour and limitations.
4. Review accessibility, language, localization, and comprehension testing.
5. Test synthetic-content marking and disclosure persistence where applicable.
6. Verify human-support or escalation functions operate as represented.
7. Confirm supplier and version changes trigger reassessment and approval.
8. Verify non-binding guidance is not represented as a binding transparency duty.

## Metrics

- systems requiring transparency measures;
- approved notices and instructions implemented;
- accessibility, comprehension, or language defects;
- disclosure or marking failures;
- user complaints or documented confusion;
- systems changed without transparency reassessment;
- overdue remediation;
- human-escalation success rate;
- supplier changes awaiting review.

## Management checklist

- Have all applicable AI interactions and synthetic-content uses been identified?
- Is the responsible actor and legal trigger clear?
- Are notices timely, accurate, accessible, understandable, and localized?
- Do disclosures and instructions match actual system behaviour?
- Are machine-readable markings implemented and tested where required?
- Can users obtain meaningful human support where appropriate?
- Are transparency controls retested after material change?

## Figure specification — AI Transparency Readiness Journey

Create a journey from use-case identification and legal-trigger analysis through actor mapping, notice and instruction design, accessibility review, technical marking, implementation, production testing, release approval, user feedback, change review, and continuous monitoring.

**Alt text:** AI transparency readiness journey from identifying relevant interactions and content through actor analysis, approved notices and instructions, technical markings, accessibility testing, deployment, user feedback, change review, and ongoing monitoring.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable transparency and information duties, including Articles 13, 26, and 50, together with relevant definitions, exceptions, effective dates, and Annex IV documentation requirements.
- Regulation (EU) 2026/1744 where applicable.
- Applicable accessibility, consumer-protection, employment, privacy, media, and sector-specific law.
- Current consolidated EUR-Lex text controls over older summaries.