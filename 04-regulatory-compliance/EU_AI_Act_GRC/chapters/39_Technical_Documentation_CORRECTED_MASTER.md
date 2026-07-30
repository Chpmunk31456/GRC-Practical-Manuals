# Chapter 39 — Technical Documentation

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 39 draft language.

## Requirement

Before a high-risk AI system is placed on the market or put into service, the provider must prepare and maintain technical documentation demonstrating compliance with the applicable requirements. The documentation must address Article 11 and Annex IV of Regulation (EU) 2024/1689, as amended, and remain current throughout the lifecycle.

## Plain-English explanation

Technical documentation is the evidence package that explains what the system is, how it was developed, what data and methods were used, how it performs, what risks and limitations exist, how human oversight works, and why the provider believes the legal requirements are met. It must be specific enough for authorities, notified bodies where applicable, and internal reviewers to assess conformity.

Model cards, system cards, architecture documents, and test reports can support the package, but none of them alone necessarily satisfies Annex IV.

## Required documentation areas

The package should cover, as applicable:

1. a general description, intended purpose, system version, and provider information;
2. system architecture, components, dependencies, interfaces, and computational resources;
3. design and development methods;
4. data requirements, datasets, provenance, preparation, and governance;
5. model or algorithm choices, parameters, and relevant assumptions;
6. validation and testing methods, metrics, thresholds, environments, and results;
7. risk-management process and residual-risk conclusions;
8. human-oversight measures;
9. accuracy, robustness, cybersecurity, and foreseeable limitations;
10. logging capabilities and recordkeeping arrangements;
11. conformity-assessment pathway, standards, common specifications, and deviations;
12. post-market monitoring, incident, and corrective-action arrangements;
13. changes, updates, and version history;
14. instructions for use and other information supplied to operators.

## GlobalWay example

For its high-risk recruitment-screening system, GlobalWay maintains an Annex IV index linking the intended purpose, architecture, datasets, subgroup testing, performance limits, human-review workflow, cybersecurity testing, risk controls, conformity records, and post-market monitoring plan to the exact production release.

## Control activity

The provider must maintain a controlled technical-documentation repository with an approved Annex IV index. No release may proceed unless required documents are complete, internally consistent, version-linked, reviewed, and approved. Material changes must trigger documentation review and update.

## Evidence

- Annex IV documentation index;
- system description and architecture;
- development and data documentation;
- test plans, metrics, and results;
- risk-management file;
- human-oversight plan;
- cybersecurity and robustness evidence;
- instructions for use;
- conformity records;
- post-market monitoring plan;
- version and change history;
- review and approval records.

## Audit test

Select a production high-risk AI-system version. Confirm that the technical-documentation package existed before release, addresses the applicable Annex IV elements, agrees with the deployed configuration, and was updated after relevant changes or new post-market information.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: Article 11 and Annex IV.
- Current consolidated EUR-Lex text controls over older summaries.