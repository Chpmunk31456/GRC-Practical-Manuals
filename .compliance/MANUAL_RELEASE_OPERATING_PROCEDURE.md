# Manual Release Operating Procedure

**Control status:** Mandatory repository-wide release procedure for all current and future manuals and companion publication packages.

## Purpose

Standardize manual production so work is pre-staged as far as safely possible, technical work does not wait unnecessarily on human review, and no manual is released without human release authorization.

## Operating principle

For every manual, complete all non-human work that can be performed safely before human action is required. Work on successor manuals may be pre-staged in parallel, but stacked branches must remain correctly ordered and no successor may bypass an unfinished predecessor.

Automated QA does not constitute human review or substitute for required human evidence.

## Reviewer-readiness lead rule

To prevent human review from being delayed by repository cleanup, artifact generation, stale evidence, or avoidable rendering defects, the release train must maintain reviewer readiness ahead of the front-of-line manual.

At minimum:

- the **front-of-line manual** is the active publication target;
- the **next manual** must already be reviewer-ready before the front manual completes substantive human review;
- the **following manual** should be preflighted as far as safely possible so its remaining work is known before it becomes next in line.

Reviewer-ready means, as applicable to the manual:

- exact durable publication artifacts already exist;
- reviewed artifact identities and SHA-256 hashes are recorded;
- a consolidated human-review packet identifies only the substantive human gates still open;
- rendered/document preflight has already been completed to catch machine-detectable or AI-detectable layout/localization defects before human review;
- localization semantic/terminology review scope is explicit;
- technical/editorial/legal/security review scope is explicit where required;
- changed-scope review criteria are explicit and tied to artifact identity;
- provenance, page QA, metadata, release manifests, checksums and repository/security evidence are already pre-staged wherever possible;
- standing Final Human Release Approval is recognized so no repeated owner-approval prompt becomes a release delay.

A manual must not reach the front of the release queue with machine-fixable preparation work that could reasonably have been completed while its predecessor was under review.

## Slack-time learning and adaptation rule

When the active publication target is waiting on a genuine human gate, available production capacity must be used to improve downstream readiness rather than remain idle.

Permitted and expected slack-time work includes:

- rendered/document preflight of successor publication candidates;
- localization and terminology cleanup;
- exact-hash reviewer-packet preparation;
- provenance/checksum/manifest reconciliation;
- dependency and ancestry reconciliation;
- source-state verification and watch preparation;
- workflow/security hardening;
- durable package preparation;
- regression testing and defect-family analysis.

When a defect is discovered, the preferred response is:

1. confirm whether the finding is real rather than disabling the gate;
2. repair the root cause at the highest safe reusable abstraction level;
3. add or improve a fail-closed regression control when the defect class is machine-detectable;
4. validate the fix on the affected manual;
5. cascade proven hardening forward through the dependency chain without overwriting manual-specific content;
6. proactively prevent the same defect in later manuals rather than waiting for repeated failures.

The objective is to evolve the process from **detect and repair** to **prevent and verify**, while preserving all substantive human-review boundaries.

### Standing Final Human Release Approval authorization

The repository owner has issued a standing **Final Human Release Approval** authorization for all current and future manuals and companion publication packages. This standing authorization applies only when every other mandatory gate for the exact final candidate is green and the required review evidence is recorded.

Accordingly:

- no additional prompt, confirmation, or repeated approval request to the repository owner is required at the Final Human Release Approval step;
- once all preceding mandatory gates are green for the exact candidate, the standing authorization satisfies the final release-permission step and the controlled merge/publication sequence should proceed automatically;
- the standing authorization does **not** substitute for source, technical, editorial, legal, localization-semantic, accessibility, rendered-document, changed-scope, security, provenance, or other required review evidence;
- a material change reopens the affected substantive review gates but does not by itself revoke the standing Final Human Release Approval authorization;
- only an explicit owner revocation or replacement instruction suspends this standing authorization.

## Mandatory release sequence

Every manual must use the following controlled sequence unless a stricter manual-specific rule applies:

1. **Authoritative-source verification**
   - verify current official sources and publication/revision status;
   - record source date/status and material revision risk;
   - fail closed on unexpected source-status change.

2. **Controlled English master**
   - complete the controlled English implementation content;
   - preserve legal, regulatory, standards, technical, audit, and assurance boundaries;
   - include practical workflows, evidence expectations, decision points, escalation/stop conditions, and implementation paths appropriate to the subject.

3. **Learning graphics and accessibility source controls**
   - include graphics where they materially improve human understanding or retention;
   - provide meaningful alt text or equivalent accessible explanation;
   - ensure graphics do not change, overstate, or contradict controlled text.

4. **Controlled localization**
   - prepare Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) editions where the manual series requires them;
   - preserve the English master as the controlled source language unless formally changed;
   - maintain chapter/section/figure/table/reference parity;
   - localized editions remain drafts until semantic/terminology review is complete.

5. **Automated repository and content QA**
   - manual-specific QA;
   - structure and catalog validation;
   - workflow-security validation;
   - trilingual parity where applicable;
   - regression checks against already released manuals;
   - release-package/schema controls.

6. **Publication artifact generation**
   - generate accessible DOCX and PDF QA candidates from controlled source material;
   - preserve source-to-artifact traceability;
   - do not treat generated artifacts as final merely because conversion succeeds.

7. **Document and visual QA**
   - inspect DOCX semantics/accessibility;
   - inspect PDF content, links, fonts, metadata, reading order, tables, figures, and pagination as applicable;
   - perform page-level visual QA;
   - resolve high/critical findings before release.

8. **Provenance and release evidence**
   - generate SHA-256 or equivalent integrity evidence for release artifacts;
   - prepare release manifest/provenance records using repository schemas;
   - record source commit, artifact identities, language editions, QA status, and known limitations.

9. **Human review gates**
   - record reviewer, date, decision, evidence, findings, and remediation where applicable;
   - include source/technical/editorial/legal/accessibility/semantic review appropriate to the manual;
   - material changes after approval reopen the affected review gate.

10. **Final Human Release Approval**
   - release fails closed unless Final Human Release Approval authorization applies to the current reviewed scope;
   - the standing repository-owner authorization above satisfies this step automatically after all preceding mandatory gates are green for the exact final candidate;
   - no additional owner prompt or repeated confirmation is required while the standing authorization remains active;
   - nothing is marked Completed or released before all preceding mandatory gates are complete.

11. **Merge and publication**
   - merge only in controlled stack order;
   - do not bypass protected `main` or branch protections;
   - publish only the approved artifact set tied to the reviewed commit/provenance record.

12. **Post-release monitoring and correction**
   - monitor authoritative-source changes and material defects;
   - use controlled correction/withdrawal procedures when required;
   - a material post-release change starts a new reviewed release cycle.

## Fail-closed conditions

A manual must not be released when any mandatory gate is:

- missing;
- incomplete;
- rejected;
- awaiting remediation;
- invalidated by a material change;
- based on stale or materially changed authoritative sources;
- technically failing required QA;
- missing required publication/provenance evidence;
- awaiting Final Human Release Approval **when no active standing or candidate-specific owner authorization applies**.

## Parallel pre-staging rule

To minimize delay, successor manuals and companion toolkits should be pre-staged whenever safe. Permitted pre-staging includes source research, controlled outlines, evidence templates, localization/document QA gates, workflow scaffolding, terminology controls, accessibility requirements, reviewer packets, exact artifact hashes, rendered preflight, provenance/checksum preparation, and other work that does not falsely imply completion or human approval.

Parallel work must not:

- merge out of order;
- mutate protected `main` directly;
- conceal stale ancestry;
- treat automated QA as approval;
- carry obsolete parent-branch content into a successor;
- weaken a stricter manual-specific release gate.

## Assurance boundary

Passing repository QA or this release procedure does not itself establish legal compliance, certification, conformity, trustworthy-AI status, security assurance, or an audit opinion. Those claims require their own applicable evidence and authority.

## Reuse requirement

This procedure applies to all future manuals and companion publication/toolkit work unless superseded by a formally reviewed stricter control. Manual-specific release-readiness records should reference this procedure and add only subject-specific gates rather than recreating the entire release process.
