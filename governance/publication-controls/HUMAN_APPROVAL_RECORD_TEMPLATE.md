# Human Approval Record Template

Use one record per manual release candidate and language set. Do not mark a human-review gate complete without a completed record.

## Identification

- Manual number and title:
- Repository:
- Branch:
- Pull request:
- Candidate Git commit SHA:
- Version / edition:
- Languages in scope:
- Review date:

## Reviewer

- Reviewer name:
- Reviewer role / competence basis:
- Organization (if applicable):
- Independence or conflict considerations:

## Scope reviewed

Mark each item `PASS`, `PASS WITH EXCEPTION`, `CHANGES REQUIRED`, or `NOT APPLICABLE`.

| Review area | Status | Evidence / notes |
|---|---|---|
| English controlled-source meaning |  |  |
| es-419 semantic review |  |  |
| pt-BR semantic review |  |  |
| Controlled terminology |  |  |
| Normative-strength preservation |  |  |
| Risk vs. impact distinctions |  |  |
| Audit/evidence language |  |  |
| Graphics and visible labels |  |  |
| Alt text and accessible explanations |  |  |
| Accessibility audit results |  |  |
| Cross-language parity |  |  |
| Release metadata and provenance |  |  |

## Exceptions and unresolved items

For every exception record:

- ID:
- Description:
- Severity:
- Affected language/file/page/figure:
- Risk if accepted:
- Compensating action:
- Owner:
- Due date, if any:
- Approval authority:

## Approval decision

Select exactly one:

- [ ] APPROVED FOR NEXT RELEASE GATE
- [ ] APPROVED WITH DOCUMENTED EXCEPTIONS
- [ ] CHANGES REQUIRED
- [ ] REJECTED / NOT READY

### Approval statement

I confirm that the review scope above was performed to the extent stated, that unresolved items are recorded rather than hidden, and that this approval does not by itself establish legal compliance, ISO conformity/certification, or an audit opinion.

- Reviewer signature/name:
- Date:
- Evidence location:

## Change control

Any substantive change after approval invalidates the affected approval scope and requires targeted re-review before release.
