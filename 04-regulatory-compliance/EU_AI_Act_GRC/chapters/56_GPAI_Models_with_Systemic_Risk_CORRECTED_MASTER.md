# Chapter 56 — GPAI Models with Systemic Risk

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 56 draft language.

## Requirement

A general-purpose AI model must be classified as a GPAI model with systemic risk when it has high-impact capabilities under Article 51 or when the Commission designates it as presenting equivalent capabilities or impact. Providers must monitor the classification criteria, notify the Commission when required, and comply with the additional obligations applicable to systemic-risk models.

## Plain-English explanation

Systemic-risk status can arise through a statutory presumption or a Commission decision. The current regulation presumes high-impact capabilities when cumulative training computation exceeds 10^25 floating-point operations, subject to future amendment. The threshold is not the only route: the Commission may designate a model based on the broader Annex XIII criteria.

## Classification and notification process

The provider must:

1. measure and document cumulative training computation;
2. assess model capabilities and impact using appropriate tools, benchmarks, and Annex XIII criteria;
3. monitor whether the threshold will be met before training completes;
4. notify the Commission without delay and no later than two weeks after the criterion is met or the provider knows it will be met;
5. include the information necessary to support the notification;
6. document any exceptional, substantiated argument that the model does not present systemic risk despite meeting the presumption;
7. track Commission designation, rejection, reassessment, or removal decisions;
8. activate Article 55 controls when systemic-risk classification applies.

## GlobalWay example

GlobalWay is not the provider of the third-party GPAI model used in its travel platform, but vendor due diligence confirms whether the provider has assessed systemic-risk status, completed required notifications, and supplied appropriate safety and security information to downstream customers.

## Control activity

The GPAI provider must maintain a documented systemic-risk classification process linked to training plans, compute records, evaluation results, Commission communications, and release gates. No qualifying model may be placed on the Union market while a required notification or Article 55 readiness action remains unresolved.

## Evidence

- training-compute calculation;
- capability and impact evaluations;
- Annex XIII analysis;
- threshold-monitoring records;
- Commission notification and timestamp;
- rebuttal submission, where used;
- Commission decision or correspondence;
- Article 55 readiness and compliance evidence.

## Audit test

Select a major GPAI model release. Recalculate or validate the training-compute figure, inspect the Annex XIII analysis, confirm the notification date where required, and verify that systemic-risk obligations were activated before release.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: Articles 51–52 and Annex XIII.
- European Commission GPAI provider guidelines, identified as non-binding guidance.
- Current consolidated EUR-Lex text controls over older summaries.
