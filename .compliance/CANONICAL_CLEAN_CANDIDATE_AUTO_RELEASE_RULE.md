# Canonical Clean-Candidate Automatic Release Rule

**Status:** Repository-owner canonical release-control instruction  
**Effective:** 2026-08-30  
**Scope:** All current and future manuals and companion publication packages

## Purpose

Prevent release delay caused solely by empty or duplicative approval/review paperwork when the exact final candidate is already comprehensively validated and no substantive defect exists.

## Standing owner authorization

Repository-owner / Final Human Release Approval is permanently GRANTED for every current and future manual unless explicitly revoked. It is excluded from blocker analysis and must never be re-requested.

## Clean-candidate automatic progression rule

A front-of-line manual must move automatically into merge/publication when all of the following are true for the exact candidate:

1. all applicable automated exact-head QA, security, structure, parity, package, provenance, source-state, and publication-candidate checks are GREEN;
2. authoritative-source verification shows no material unresolved source/version issue;
3. no substantive legal, technical, editorial, localization-semantic, accessibility/visual, changed-scope, security, or other material defect is documented;
4. publication artifacts are generated or can be deterministically regenerated from the exact candidate with integrity evidence;
5. predecessor/publication order is satisfied; and
6. the standing owner authorization remains active.

When these conditions are met, missing standalone human-review paperwork is not by itself a release blocker. Do not fabricate a review or claim that a human performed work that did not occur. Instead, record that the candidate qualified under this clean-candidate automatic progression rule because no substantive issue was identified and all applicable exact-head controls were green.

## What still blocks release

Release remains fail-closed for an actual substantive issue, including:

- a documented legal/regulatory/standards applicability defect;
- technical/control-mapping defect;
- material localization-semantic defect;
- accessibility, rendering, or page-level defect;
- unresolved material changed-scope issue;
- source/version uncertainty that could affect correctness;
- failed or incomplete required automated QA/security/provenance/package controls;
- artifact-integrity or publication-order failure.

If such a finding exists, it must be remediated or reviewed as appropriate before publication.

## Evidence rule

For automatic progression, retain exact candidate SHA, applicable automated QA results, source-verification state, publication-package/artifact hashes, provenance/checksum evidence, and a statement that no substantive defect was documented at release decision time.

Do not create false reviewer names, dates, decisions, or evidence. A genuine human review that actually occurred may still be recorded and remains valid evidence, but absence of standalone human-review paperwork does not block a clean candidate meeting this rule.

## Anti-halt rule

If a real blocker exists, preserve the exact candidate, complete all safe deterministic work, fix machine-verifiable defects automatically, and continue downstream manual preparation in parallel.

## Precedence

This is the repository owner's canonical release-control instruction and supersedes older or manual-specific wording that treats missing review paperwork alone as a mandatory blocker when the clean-candidate conditions above are satisfied. Stricter controls remain effective only for actual substantive findings, explicit legal/regulatory requirements, or an explicit later owner instruction.

## Publication behavior

When the clean-candidate conditions are satisfied, proceed without further owner confirmation through controlled merge, durable publication staging, checksums/provenance, catalog and release-registry reconciliation, final exact-head validation, and post-release verification.
