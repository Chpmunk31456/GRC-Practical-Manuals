#!/usr/bin/env python3
"""Generate missing CIS Controls v8.1 Spanish figures deterministically."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path('01-foundations/CIS_Controls_v8.1/Espanol/media')
OUT.mkdir(parents=True, exist_ok=True)
W, H = 1476, 820
INK, LINE, PALE, BLUE = '#1f2937', '#4b5563', '#e5e7eb', '#dbeafe'
REG = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FONT = ImageFont.truetype(REG, 30)
SMALL = ImageFont.truetype(REG, 24)
TITLE = ImageFont.truetype(BOLD, 40)


def box(draw, xy, label, fill=PALE, font=FONT):
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, radius=20, fill=fill, outline=LINE, width=3)
    lines = label.split('\n')
    heights = [draw.textbbox((0, 0), line, font=font)[3] for line in lines]
    y = (y1 + y2 - sum(heights) - 7 * (len(lines) - 1)) / 2
    for line, height in zip(lines, heights):
        width = draw.textbbox((0, 0), line, font=font)[2]
        draw.text(((x1 + x2 - width) / 2, y), line, font=font, fill=INK)
        y += height + 7


def arrow(draw, start, end):
    draw.line([start, end], fill=LINE, width=6)
    x, y = end
    draw.polygon([(x, y), (x - 18, y - 11), (x - 18, y + 11)], fill=LINE)


def flow(number, title, subtitle, labels):
    image = Image.new('RGB', (W, H), 'white')
    draw = ImageDraw.Draw(image)
    draw.text((55, 38), title, font=TITLE, fill=INK)
    draw.text((55, 96), subtitle, font=SMALL, fill=LINE)
    margin, gap = 58, 26
    width = (W - 2 * margin - gap * (len(labels) - 1)) // len(labels)
    y1, y2 = 270, 570
    for index, label in enumerate(labels):
        x1 = margin + index * (width + gap)
        x2 = x1 + width
        box(draw, (x1, y1, x2, y2), label, BLUE if index % 2 == 0 else PALE, SMALL)
        if index < len(labels) - 1:
            arrow(draw, (x2 + 3, 420), (x2 + gap - 4, 420))
    image.save(OUT / f'image{number}.png', optimize=True)


def figure1():
    image = Image.new('RGB', (W, H), 'white')
    draw = ImageDraw.Draw(image)
    draw.text((55, 38), 'Los 18 CIS Critical Security Controls', font=TITLE, fill=INK)
    draw.text((55, 96), 'Una estructura priorizada de 153 Salvaguardas', font=SMALL, fill=LINE)
    columns = 6
    x0, y0, width, height, gx, gy = 75, 195, 190, 125, 40, 42
    for number in range(1, 19):
        row, column = divmod(number - 1, columns)
        x1 = x0 + column * (width + gx)
        y1 = y0 + row * (height + gy)
        box(draw, (x1, y1, x1 + width, y1 + height), f'Control {number}', BLUE if row % 2 == 0 else PALE, SMALL)
    image.save(OUT / 'image1.png', optimize=True)


def figure2():
    image = Image.new('RGB', (W, H), 'white')
    draw = ImageDraw.Draw(image)
    draw.text((55, 38), 'Progresión de los Grupos de Implementación', font=TITLE, fill=INK)
    draw.text((55, 96), 'Cada grupo se apoya en el anterior', font=SMALL, fill=LINE)
    groups = [
        (105, 305, 430, 555, 'IG1\n56 Salvaguardas'),
        (575, 250, 900, 610, 'IG2\nIG1 + 74'),
        (1045, 195, 1370, 665, 'IG3\nIG1 + IG2 + 23\n153 en total'),
    ]
    for index, (x1, y1, x2, y2, label) in enumerate(groups):
        box(draw, (x1, y1, x2, y2), label, BLUE if index != 1 else PALE, FONT)
        if index < 2:
            arrow(draw, (x2 + 8, 430), (groups[index + 1][0] - 8, 430))
    image.save(OUT / 'image2.png', optimize=True)


def figure10():
    image = Image.new('RGB', (W, H), 'white')
    draw = ImageDraw.Draw(image)
    draw.text((55, 38), 'Ruta para analistas junior de Controles CIS', font=TITLE, fill=INK)
    draw.text((55, 96), 'Aprender, medir, comunicar y construir un portafolio honesto', font=SMALL, fill=LINE)
    roles = [
        'Controles\nde seguridad', 'GRC', 'Vulnerabilidades', 'Aseguramiento',
        'Operaciones\nde seguridad', 'Cumplimiento\nde TI', 'Riesgo de\nterceros', 'Programas de\nciberseguridad'
    ]
    columns, x0, y0, width, height, gx, gy = 4, 70, 205, 300, 185, 45, 55
    for index, role in enumerate(roles):
        row, column = divmod(index, columns)
        x1 = x0 + column * (width + gx)
        y1 = y0 + row * (height + gy)
        box(draw, (x1, y1, x1 + width, y1 + height), role, BLUE if row == 0 else PALE, SMALL)
    image.save(OUT / 'image10.png', optimize=True)


figure1()
figure2()
flow(4, 'Ciclo de inventario de activos y software', 'Descubrimiento, conciliación y actualización continua', ['Descubrir', 'Conciliar', 'Responder', 'Revisar', 'Actualizar'])
flow(5, 'Ciclo de vida de protección de datos', 'Medidas según sensibilidad y necesidad', ['Descubrir', 'Clasificar', 'Proteger', 'Conservar', 'Eliminar'])
flow(6, 'Ciclo de vida de identidad y acceso', 'Creación aprobada, autenticación sólida y revocación oportuna', ['Solicitar', 'Aprobar', 'Provisionar', 'Revisar', 'Revocar'])
flow(7, 'Gestión continua de vulnerabilidades', 'Cobertura completa y remediación verificada', ['Inventariar', 'Evaluar', 'Priorizar', 'Corregir', 'Verificar'])
flow(8, 'Monitoreo y defensa de la red', 'Contexto centralizado, investigación humana y respuesta', ['Recopilar', 'Centralizar', 'Detectar', 'Investigar', 'Responder'])
flow(9, 'Preparación para la respuesta a incidentes', 'Roles, reporte, comunicación, ejercicios y revisión', ['Preparar', 'Reportar', 'Coordinar', 'Ejercitar', 'Revisar', 'Mejorar'])
figure10()

if not (OUT / 'image3.png').is_file():
    raise SystemExit('Reviewed Figure 3 is missing; refusing to replace it automatically.')
for number in range(1, 11):
    path = OUT / f'image{number}.png'
    if not path.is_file() or path.stat().st_size < 1000:
        raise SystemExit(f'Figure generation failed: {path}')
print('Generated Figures 1, 2, and 4-10; preserved reviewed Figure 3.')
