#!/usr/bin/env python3
from pathlib import Path
import re

TARGET = Path('01-foundations/CIS_Controls_v8.1/Espanol/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md')

text = TARGET.read_text(encoding='utf-8')
original = text

patterns = {
    'image1.png': 'Los Controles organizan 153 Salvaguardas en un programa defensivo práctico.',
    'image2.png': 'Cada Grupo de Implementación se apoya en el anterior; IG3 contiene todas las Salvaguardas.',
    'image3.png': 'La especificación oficial avanza desde entradas de datos definidas hasta operaciones, medidas, métricas y revisión de procedimientos.',
    'image9.png': 'Los roles preparados, los mecanismos de reporte, la comunicación, los ejercicios y las revisiones reducen el impacto de los incidentes.',
    'image10.png': 'Aprenda el marco, relacione las Salvaguardas, mida la evidencia, informe las brechas y construya un portafolio honesto.',
}

for image, alt in patterns.items():
    html = re.compile(r'<img\s+src="media/' + re.escape(image) + r'"[^>]*?/?>', re.IGNORECASE)
    text = html.sub(f'![{alt}](media/{image})', text)

if text == original:
    raise SystemExit('No eligible CIS Spanish HTML image tags were found')

for image in ('image9.png', 'image10.png'):
    if f'](media/{image})' not in text:
        raise SystemExit(f'Expected normalized Markdown image reference missing: {image}')

TARGET.write_text(text, encoding='utf-8')
print('Normalized CIS Spanish image references for Pandoc DOCX embedding')
