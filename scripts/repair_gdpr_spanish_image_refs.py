#!/usr/bin/env python3
"""Replace four malformed Spanish GDPR image remnants with valid Markdown."""
from pathlib import Path

PATH = Path("04-regulatory-compliance/GDPR/Espanol/GDPR_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md")

REPLACEMENTS = {
    'יimg src="media/image1.png" style="width:6.15in;height:3.23744in" alt="Cuatro bloques conectados muestran personas, datos, propósito y control." /':
        '![Cuatro bloques conectados muestran personas, datos, propósito y control.](media/image1.png){width=6.15in height=3.23744in}',
    '■img src="media/image2.png" estilo="width:6.15in;height:3.34699in" alt="El ciclo de vida conecta la colección, el uso, el compartir, la retención y la eliminación." /':
        '![El ciclo de vida conecta la recolección, el uso, el intercambio, la retención y la eliminación.](media/image2.png){width=6.15in height=3.34699in}',
    '■img src="media/image3.png" estilo="Ancho:6.15in; Altura:3.34699in" alt="Un flujo de trabajo de cinco pasos cubre la ingesta a través del resultado registrado." /':
        '![Un flujo de trabajo de cinco pasos cubre la recepción hasta el resultado registrado.](media/image3.png){width=6.15in height=3.34699in}',
    '■img src="media/image4.png" style="width:6.15in;height:3.45654in" alt="Contener, evaluar, decidir y mejorar se muestran como un proceso vinculado." /':
        '![Contener, evaluar, decidir y mejorar se muestran como un proceso conectado.](media/image4.png){width=6.15in height=3.45654in}',
}

text = PATH.read_text(encoding="utf-8")
for old, new in REPLACEMENTS.items():
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"Expected exactly one occurrence, found {count}: {old[:60]}")
    text = text.replace(old, new)

PATH.write_text(text, encoding="utf-8")
print("Repaired four Spanish GDPR image references.")
