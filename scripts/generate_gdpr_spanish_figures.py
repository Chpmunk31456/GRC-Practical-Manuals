#!/usr/bin/env python3
"""Generate the four missing Latin American Spanish GDPR figures.

The diagrams preserve the authoritative source concepts, sequence, and target
canvas dimensions recorded in the image-provenance inventory.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path("04-regulatory-compliance/GDPR/Espanol/media")
BLUE = "#0B5CAD"
DARK = "#18324A"
LIGHT = "#EAF3FB"
MID = "#B9D7F0"
WHITE = "#FFFFFF"
GRAY = "#5B6770"
GREEN = "#2E7D32"
ORANGE = "#C56A00"
RED = "#B3261E"


def font(size: int, bold: bool = False):
    names = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    ]
    for name in names:
        if Path(name).exists():
            return ImageFont.truetype(name, size)
    return ImageFont.load_default()


def centered(draw, xy, text, fnt, fill=DARK):
    x, y = xy
    box = draw.multiline_textbbox((0, 0), text, font=fnt, align="center", spacing=6)
    draw.multiline_text((x - (box[2]-box[0])/2, y - (box[3]-box[1])/2), text, font=fnt, fill=fill, align="center", spacing=6)


def arrow(draw, start, end, fill=BLUE, width=7):
    draw.line([start, end], fill=fill, width=width)
    x2, y2 = end
    x1, y1 = start
    import math
    a = math.atan2(y2-y1, x2-x1)
    s = 20
    p1 = (x2 - s*math.cos(a-0.55), y2 - s*math.sin(a-0.55))
    p2 = (x2 - s*math.cos(a+0.55), y2 - s*math.sin(a+0.55))
    draw.polygon([end, p1, p2], fill=fill)


def header(draw, width, title):
    draw.rounded_rectangle((55, 35, width-55, 130), radius=22, fill=BLUE)
    centered(draw, (width/2, 82), title, font(36, True), WHITE)


def save(img, name):
    OUT.mkdir(parents=True, exist_ok=True)
    img.save(OUT / name, "PNG", optimize=True)


def figure1():
    w, h = 1628, 857
    img = Image.new("RGB", (w, h), WHITE); d = ImageDraw.Draw(img)
    header(d, w, "GDPR como programa práctico de gestión")
    labels = [
        ("PERSONAS", "Titulares de los datos", 230, 390),
        ("DATOS", "Datos personales", 610, 390),
        ("PROPÓSITO", "Uso definido y lícito", 1018, 390),
        ("CONTROL", "Gobernanza y evidencia", 1398, 390),
    ]
    for i, (title, sub, x, y) in enumerate(labels):
        d.rounded_rectangle((x-155, y-120, x+155, y+120), radius=28, fill=LIGHT, outline=BLUE, width=6)
        centered(d, (x, y-24), title, font(31, True), BLUE)
        centered(d, (x, y+48), sub, font(23), DARK)
        if i < 3:
            arrow(d, (x+160, y), (labels[i+1][2]-165, y))
    d.rounded_rectangle((230, 665, 1398, 780), radius=26, fill="#F5F8FA", outline=MID, width=4)
    centered(d, (814, 720), "La rendición de cuentas conecta a las personas, los datos, el propósito y el control.", font(27, True), DARK)
    save(img, "image1.png")


def figure2():
    w, h = 1628, 886
    img = Image.new("RGB", (w, h), WHITE); d = ImageDraw.Draw(img)
    header(d, w, "Ciclo de vida de los datos personales")
    items = [
        ("1", "RECOLECCIÓN", "Obtener solo lo necesario"),
        ("2", "USO", "Usar para fines definidos"),
        ("3", "INTERCAMBIO", "Compartir con control"),
        ("4", "RETENCIÓN", "Conservar por un plazo"),
        ("5", "ELIMINACIÓN", "Eliminar o anonimizar"),
    ]
    xs = [170, 492, 814, 1136, 1458]
    y = 410
    for i, ((num, title, sub), x) in enumerate(zip(items, xs)):
        d.ellipse((x-88, y-88, x+88, y+88), fill=LIGHT, outline=BLUE, width=7)
        centered(d, (x, y-24), num, font(34, True), BLUE)
        centered(d, (x, y+28), title, font(22, True), DARK)
        d.rounded_rectangle((x-135, 565, x+135, 690), radius=18, fill="#F7FAFC", outline=MID, width=3)
        centered(d, (x, 627), sub, font(20), DARK)
        if i < 4:
            arrow(d, (x+94, y), (xs[i+1]-94, y))
    arrow(d, (1458, 515), (1458, 770), GRAY, 5)
    arrow(d, (1458, 770), (170, 770), GRAY, 5)
    arrow(d, (170, 770), (170, 515), GRAY, 5)
    centered(d, (814, 815), "Revisar la base legal, la minimización, la seguridad y la evidencia en cada etapa.", font(25, True), DARK)
    save(img, "image2.png")


def figure3():
    w, h = 1628, 886
    img = Image.new("RGB", (w, h), WHITE); d = ImageDraw.Draw(img)
    header(d, w, "Flujo de trabajo de derechos de los titulares")
    steps = [
        ("1", "RECIBIR", "Registrar la solicitud"),
        ("2", "VERIFICAR", "Confirmar identidad y alcance"),
        ("3", "BUSCAR", "Localizar datos y propietarios"),
        ("4", "EVALUAR", "Aplicar derechos y excepciones"),
        ("5", "RESPONDER", "Entregar y registrar el resultado"),
    ]
    xs = [170, 492, 814, 1136, 1458]
    for i, ((num, title, sub), x) in enumerate(zip(steps, xs)):
        d.rounded_rectangle((x-140, 285, x+140, 575), radius=28, fill=LIGHT, outline=BLUE, width=6)
        d.ellipse((x-38, 315, x+38, 391), fill=BLUE)
        centered(d, (x, 353), num, font(29, True), WHITE)
        centered(d, (x, 445), title, font(26, True), DARK)
        centered(d, (x, 515), sub, font(19), DARK)
        if i < 4:
            arrow(d, (x+145, 430), (xs[i+1]-145, 430))
    d.rounded_rectangle((170, 680, 1458, 800), radius=24, fill="#F5F8FA", outline=MID, width=4)
    centered(d, (814, 738), "Control transversal: plazo, identidad, búsqueda, revisión legal, entrega segura y pista de auditoría.", font(25, True), DARK)
    save(img, "image3.png")


def figure4():
    w, h = 1628, 915
    img = Image.new("RGB", (w, h), WHITE); d = ImageDraw.Draw(img)
    header(d, w, "Flujo de trabajo ante una violación de datos personales")
    stages = [
        ("CONTENER", "Detener la exposición y preservar evidencia", RED),
        ("EVALUAR", "Confirmar hechos, datos, personas y riesgo", ORANGE),
        ("DECIDIR", "Documentar notificación a autoridad y personas", BLUE),
        ("MEJORAR", "Corregir causas y fortalecer controles", GREEN),
    ]
    xs = [240, 620, 1008, 1388]
    y = 405
    for i, ((title, sub, color), x) in enumerate(zip(stages, xs)):
        d.rounded_rectangle((x-165, y-135, x+165, y+135), radius=30, fill="#F8FAFC", outline=color, width=7)
        d.rounded_rectangle((x-135, y-95, x+135, y-25), radius=16, fill=color)
        centered(d, (x, y-60), title, font(29, True), WHITE)
        centered(d, (x, y+54), sub, font(21), DARK)
        if i < 3:
            arrow(d, (x+170, y), (xs[i+1]-170, y), BLUE)
    d.rounded_rectangle((210, 660, 1418, 825), radius=25, fill=LIGHT, outline=BLUE, width=4)
    centered(d, (814, 705), "Preguntas de decisión", font(28, True), BLUE)
    centered(d, (814, 765), "¿Existe una violación?  •  ¿Hay riesgo?  •  ¿Hay alto riesgo?  •  ¿Qué debe notificarse y cuándo?", font(24), DARK)
    save(img, "image4.png")


if __name__ == "__main__":
    figure1(); figure2(); figure3(); figure4()
    print(f"Generated four Spanish GDPR figures in {OUT}")
