#!/usr/bin/env python3
"""Promote reviewed Spanish HIPAA figures and repair seven Markdown references."""
from pathlib import Path
import shutil

REVIEW = Path("review/hipaa-spanish-figures")
MEDIA = Path("04-regulatory-compliance/HIPAA/Espanol/media")
MARKDOWN = Path("04-regulatory-compliance/HIPAA/Espanol/HIPAA_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md")

REPLACEMENTS = {
    '■img src="media/image1.png" estilo="width:6.15in;height:2.9808in" alt="Privacy, Security, Breach Notification, and Enforcement are connected." /':
        '![Privacidad, Seguridad, Notificación de Violaciones y Cumplimiento están conectados.](media/image1.png){width=6.15in height=2.9808in}',
    '■img src="media/image2.png" estilo="width:6.15in;height:3.27065in" alt="PHI es creado, utilizado, compartido, almacenado y destruido a través de su ciclo de vida." /':
        '![La PHI se crea, utiliza, comparte, almacena y destruye durante su ciclo de vida.](media/image2.png){width=6.15in height=3.27065in}',
    'لimg src="media/image3.png" style="width:6.15in;height:3.33266in" alt="Las salvaguardias administrativas, físicas y técnicas dependen del análisis de riesgos." /':
        '![Las salvaguardias administrativas, físicas y técnicas dependen del análisis de riesgos.](media/image3.png){width=6.15in height=3.33266in}',
    '■img src="media/image4.png" estilo="Ancho:6.15in; Altura:3.45654in" alt="Descubrimiento, contención, evaluación, notificación y mejora de un proceso." /':
        '![El descubrimiento, la contención, la evaluación, la notificación y la mejora forman un solo proceso.](media/image4.png){width=6.15in height=3.45654in}',
    'Altura:3.56987in" alt="Empieza con el requisito y el alcance, prueba el control, las excepciones correctas y la prueba antes de concluir." / Propiedad':
        '![Comience con el requisito y el alcance, pruebe el control, corrija las excepciones y vuelva a probar antes de concluir.](media/image5.png){width=6.15in height=3.56987in}',
    '■img src="media/image6.png" style="width:6.15in;height:3.31039in" alt="Aprendizaje, mapeo, pruebas, documentación y aplicación de empleo forman una trayectoria profesional". /':
        '![Aprender, mapear, probar, documentar y aplicar el trabajo forman una trayectoria profesional.](media/image6.png){width=6.15in height=3.31039in}',
    '"Un informe no es prueba, autorización, validación, remediación y retesting crear la cadena de evidencia" (No es una prueba única).':
        '![Un informe aislado no es prueba; la autorización, la validación, la remediación y una nueva prueba crean la cadena de evidencia.](media/image7.png){width=6.15in height=3.45654in}',
}

MEDIA.mkdir(parents=True, exist_ok=True)
for number in range(1, 8):
    source = REVIEW / f"image{number}.png"
    if not source.is_file():
        raise SystemExit(f"Missing reviewed candidate: {source}")
    shutil.copy2(source, MEDIA / source.name)

text = MARKDOWN.read_text(encoding="utf-8")
for old, new in REPLACEMENTS.items():
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"Expected exactly one occurrence of repair target, found {count}: {old[:80]}")
    text = text.replace(old, new, 1)

for number in range(1, 8):
    reference = f"](media/image{number}.png)"
    if text.count(reference) != 1:
        raise SystemExit(f"Expected one repaired reference for image{number}.png")

MARKDOWN.write_text(text, encoding="utf-8")
print("Promoted seven Spanish HIPAA figures and repaired seven Markdown references.")
