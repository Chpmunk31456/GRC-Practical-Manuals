# Manual Release Operating Procedure

**Control status:** Mandatory repository-wide release procedure for all current and future manuals and companion publication packages.

## Purpose

Standardize manual production so work is pre-staged as far as safely possible, technical work does not wait unnecessarily on human review, and no manual is released without explicit human approval.

## Operating principle

For every manual, complete all non-human work that can be performed safely before asking for human action. Work on successor manuals may be pre-staged in parallel, but stacked branches must remain correctly ordered and no successor may bypass an unfinished predecessor.

Automated QA does not constitute human approval.

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
   - release fails closed unless explicit Final Human Release Approval is recorded for the current reviewed scope;
   - nothing is marked Completed or released before this approval.

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
- awaiting Final Human Release Approval.

## Parallel pre-staging rule

To minimize delay, successor manuals and companion toolkits should be pre-staged whenever safe. Permitted pre-staging includes source research, controlled outlines, evidence templates, localization/document QA gates, workflow scaffolding, terminology controls, accessibility requirements, and other work that does not falsely imply completion or human approval.

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