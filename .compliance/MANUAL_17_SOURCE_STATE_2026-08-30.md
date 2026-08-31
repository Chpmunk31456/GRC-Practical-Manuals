# Manual 17 — NIST Privacy Framework Source-State Watch

**Verification date:** 2026-08-30  
**State:** downstream source verification; not publication authorization

## Current NIST state

Fresh official NIST verification shows that **NIST Privacy Framework 1.1 is not yet a final publication**. NIST's Privacy Framework 1.1 project page, updated April 1, 2026, still labels the final Version 1.1 as **Coming soon** and identifies the April 14, 2025 release as the **Initial Public Draft (IPD)** whose public-comment period closed June 13, 2025.

The current official Privacy Framework landing page continues to expose Version 1.0 as the established framework while separately presenting the PF 1.1 IPD and its mapping resources.

Authoritative source-watch targets:

- https://www.nist.gov/privacy-framework/new-projects/privacy-framework-version-11
- https://csrc.nist.gov/pubs/cswp/40/nist-privacy-framework-11/ipd
- https://www.nist.gov/privacy-framework

## Controlled build consequence

Manual 17 must not describe Privacy Framework 1.1 as final while NIST continues to label it an Initial Public Draft / forthcoming final version. Safe controlled work may use:

- Privacy Framework 1.0 as the stable baseline;
- PF 1.1 IPD as clearly marked draft-change intelligence;
- the NIST PF 1.0-to-1.1 mapping as migration planning input; and
- CSF 2.0 alignment themes as forward-looking architecture guidance where explicitly labeled as draft-derived.

No draft Category, Subcategory, identifier, outcome, mapping or explanatory passage may be presented as a final NIST requirement or outcome. The manual must preserve the Privacy Framework's voluntary risk-management character and avoid implying certification.

## Anti-churn rule

Do not freeze Manual 17 publication binaries against the PF 1.1 IPD. Continue controlled English architecture, evidence-model, localization terminology, graphics, tooling, and QA preparation in parallel, but perform another official NIST source-state check before candidate freeze. If NIST publishes PF 1.1 final, reconcile the final release against the draft-derived architecture before localization and binary hash binding.

## Release gate

A final publication candidate requires an explicit source-state decision tied to the exact candidate: either (a) PF 1.1 final has been published and Manual 17 has reconciled to it, or (b) repository scope explicitly chooses the stable PF 1.0 baseline and clearly excludes draft 1.1 content from normative treatment. Any ambiguity is fail-closed for publication but does not halt downstream preparation.
