#!/usr/bin/env python3
"""Generate Batch 4 review figures using the validated localized reconstruction engine."""

from __future__ import annotations

from pathlib import Path

import generate_iso27001_pci_localized_review_figures as engine

ROOT = Path(__file__).resolve().parents[1]
engine.OUTPUT = ROOT / "review/nist-rmf-incident-response-localized-figures"
engine.FAMILIES = ("NIST RMF / SP 800-53", "Incident Response / BCDR")
engine.EXPECTED_TOTAL = 20

if __name__ == "__main__":
    engine.main()
