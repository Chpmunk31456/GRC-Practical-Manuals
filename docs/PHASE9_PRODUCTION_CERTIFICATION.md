# Phase 9 — Production certification and controlled release

Phase 9 converts the production-readiness machinery from Phase 8 into evidence
that can support an exact controlled release. It remains fail-closed.

## Improvement 54 — immutable production environment contract

The production build contract is now pinned to:

- Python 3.12.14;
- linux/amd64;
- Docker Official Image `python:3.12.14-slim-bookworm`;
- exact amd64 manifest digest
  `sha256:1aaa65a85fda306ffb8b910824d4e93bdce61e212c7e87168123ea3073b41a1a`;
- no Python package dependencies;
- no network package installation inside the production build image.

The dependency contract is
`config/production_dependency_lock.json`. Its exact SHA-256 is
`de09ea78579a73a8236914019c13d3e7b7a8b83829209e770bf8dc424cd7e656`.

`Dockerfile.production` pins the exact base manifest. The PDF inspection
toolchain remains a separate contract because the Phase 8 hosted-CI Poppler
baseline must not be silently reinterpreted as an immutable production image.

Run:

`python scripts/production_environment_certification.py --output phase9-production-environment.json`

A valid contract is not certification. Phase 9 remains blocked until CI actually
builds/inspects the production image and separately supplies the immutable PDF
toolchain digest and reproducibility evidence. The script never changes
`production_toolchain.json` to `VERIFIED` by itself and never authorizes
publication.


### Runtime/source separation

The immutable production container contains the runtime/toolchain only. Repository
content is mounted into `/workspace` at execution time. This prevents
`config/production_toolchain.json` from being copied into the image whose digest
that same file records, eliminating a self-referential certification loop.

The environment image uses `SOURCE_DATE_EPOCH=0` during certification so its
content-addressed ID depends on the environment definition, not the source commit
timestamp.


## Improvement 55 — immutable PDF toolchain certification

The production PDF inspection environment is now isolated from the runtime image
and independently reproduced.

The contract pins:

- linux/amd64;
- the same exact Python 3.12.14 Bookworm base manifest used by the runtime;
- Debian Bookworm `poppler-utils 22.12.0-2+deb12u3`;
- `pdftotext 22.12.0`;
- `pdfinfo 22.12.0`.

Two isolated BuildKit jobs reproduced the same OCI manifest:

`sha256:9f922bcc7e1b2bd81f309821a89ff8a5f148f07dd38f729940985eef81d48c8b`

The PDF dependency contract SHA-256 is:

`12efcb06b4f31629c4bdcb97e99b280873fde34462d6d3e9854dea874a077faf`

The first unnormalized attempt produced different manifests and was rejected.
Timestamp/log normalization was then corrected and reproducibility was rerun
until both independent builds matched. No mismatching digest was promoted.

With both the runtime image and PDF-toolchain image independently reproduced,
`config/production_toolchain.json` may now be `VERIFIED`. This is technical
production-environment certification only; it does not satisfy human review or
authorize publication.
