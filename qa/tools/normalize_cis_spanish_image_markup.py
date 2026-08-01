#!/usr/bin/env python3
"""Normalize only CIS Spanish Figures 4-8 from raw HTML to Markdown image syntax."""
from pathlib import Path
import re

SOURCE = Path(
    "01-foundations/CIS_Controls_v8.1/Espanol/"
    "CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md"
)

EXPECTED = {
    4: "El descubrimiento, la conciliación, la respuesta y la revisión mantienen actualizadas las poblaciones fundamentales.",
    5: "Descubrir, clasificar, proteger, conservar y eliminar datos según su sensibilidad y necesidad.",
    6: "Las cuentas y los privilegios requieren creación aprobada, autenticación sólida, revisión y revocación oportuna.",
    7: "La cobertura completa y la remediación verificada importan más que la producción de informes de escaneo.",
    8: "El contexto centralizado, la detección ajustada, la investigación humana y la respuesta crean una defensa útil.",
}

text = SOURCE.read_text(encoding="utf-8")
original = text

for number, alt in EXPECTED.items():
    pattern = re.compile(
        rf'<img src="media/image{number}\.png"[^>]*alt="{re.escape(alt)}"\s*/>'
    )
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise SystemExit(
            f"Expected exactly one raw HTML image tag for Figure {number}; found {len(matches)}."
        )
    replacement = f"![{alt}](media/image{number}.png)"
    text = pattern.sub(replacement, text, count=1)

for number in range(4, 9):
    marker = f"](media/image{number}.png)\n\nFigura {number}."
    if marker not in text:
        raise SystemExit(f"Figure {number} image/caption boundary is not intact after normalization.")

if text == original:
    raise SystemExit("No image markup was changed.")

SOURCE.write_text(text, encoding="utf-8")
print("Normalized CIS Spanish Figures 4-8 to Markdown image syntax.")
