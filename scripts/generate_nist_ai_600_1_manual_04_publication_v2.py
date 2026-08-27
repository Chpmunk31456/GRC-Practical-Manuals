#!/usr/bin/env python3
"""Manual 04 publication generator v2: correct inherited figure provenance labels."""
from __future__ import annotations

import generate_nist_ai_600_1_manual_04_publication as adapter

core = adapter.core
_original_render = core.render_mermaid_memory_graphic
_original_alt = core.set_image_alt_text


def render_mermaid_memory_graphic(block: str, out_path, title: str) -> str:
    return _original_render(block, out_path, title.replace("Manual 03 memory graphic", "Manual 04 memory graphic"))


def set_image_alt_text(inline_shape, title: str, description: str):
    return _original_alt(
        inline_shape,
        title.replace("Manual 03 memory graphic", "Manual 04 memory graphic"),
        description.replace("Manual 03 memory graphic", "Manual 04 memory graphic"),
    )


core.render_mermaid_memory_graphic = render_mermaid_memory_graphic
core.set_image_alt_text = set_image_alt_text

if __name__ == "__main__":
    raise SystemExit(core.main())
