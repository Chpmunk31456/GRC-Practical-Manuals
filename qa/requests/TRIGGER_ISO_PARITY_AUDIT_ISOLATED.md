# Trigger isolated corrected ISO parity audit

Run only `.github/workflows/audit-iso-localized-parity-isolated.yml` against `production/multilingual-grc-editions`.

Refresh reason: final-section diagnostic confirmed sections 1, 17, 25, and 28 require a current parity recalculation before any source edit.

This trigger refreshes corrected section-parity evidence without modifying localized source content and must not be merged.
