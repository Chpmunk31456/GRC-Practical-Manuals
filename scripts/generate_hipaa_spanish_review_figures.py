#!/usr/bin/env python3
"""Generate seven review-only Latin American Spanish HIPAA figure candidates.

These candidates preserve the verified concepts and target dimensions from the
repository provenance inventory. They are written to a review directory and
must not be copied into the manual media directory without owner approval.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

OUT = Path("review/hipaa-spanish-figures")
BLUE = "#0B5CAD"
DARK = "#18324A"
LIGHT = "#EAF3FB"
MID = "#B9D7F0"
WHITE = "#FFFFFF"
GRAY = "#5B6770"
GREEN = "#2E7D32"
ORANGE = "#C56A00"
RED = "#B3261E"
PURPLE = "#6A3FA0"


def font(size: int, bold: bool = False):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    ]
    for path in paths:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def centered(draw, xy, text, fnt, fill=DARK):
    x, y = xy
    box = draw.multiline_textbbox((0, 0), text, font=fnt, align="center", spacing=6)
    draw.multiline_text((x - (box[2]-box[0])/2, y - (box[3]-box[1])/2), text,
                        font=fnt, fill=fill, align="center", spacing=6)


def arrow(draw, start, end, fill=BLUE, width=7):
    draw.line([start, end], fill=fill, width=width)
    x2, y2 = end
    x1, y1 = start
    angle = math.atan2(y2-y1, x2-x1)
    size = 20
    p1 = (x2 - size*math.cos(angle-0.55), y2 - size*math.sin(angle-0.55))
    p2 = (x2 - size*math.cos(angle+0.55), y2 - size*math.sin(angle+0.55))
    draw.polygon([end, p1, p2], fill=fill)


def header(draw, width, title):
    draw.rounded_rectangle((55, 35, width-55, 130), radius=22, fill=BLUE)
    centered(draw, (width/2, 82), title, font(36, True), WHITE)


def save(img, name):
    OUT.mkdir(parents=True, exist_ok=True)
    img.save(OUT / name, "PNG", optimize=True)


def figure1():
    w, h = 1828, 886
    img = Image.new("RGB", (w, h), WHITE); d = ImageDraw.Draw(img)
    header(d, w, "Áreas principales de cumplimiento HIPAA")
    labels = [
        ("PRIVACIDAD", "Uso y divulgación de PHI", BLUE),
        ("SEGURIDAD", "Salvaguardas para ePHI", GREEN),
        ("NOTIFICACIÓN DE VIOLACIONES", "Evaluación y comunicación", ORANGE),
        ("CUMPLIMIENTO", "Investigación y medidas correctivas", PURPLE),
    ]
    xs = [240, 690, 1138, 1588]
    for i, ((title, sub, color), x) in enumerate(zip(labels, xs)):
        d.rounded_rectangle((x-185, 285, x+185, 585), radius=30, fill=LIGHT, outline=color, width=7)
        d.rounded_rectangle((x-150, 320, x+150, 405), radius=18, fill=color)
        centered(d, (x, 362), title, font(26, True), WHITE)
        centered(d, (x, 495), sub, font(22), DARK)
        if i < 3:
            arrow(d, (x+190, 435), (xs[i+1]-190, 435))
    centered(d, (w/2, 745), "Las cuatro áreas forman un programa integrado de cumplimiento HIPAA.", font(28, True))
    save(img, "image1.png")


def figure2():
    w, h = 1666, 886
    img = Image.new("RGB", (w, h), WHITE); d = ImageDraw.Draw(img)
    header(d, w, "Ciclo de vida de la información de salud protegida (PHI)")
    steps = ["CREAR", "USAR", "COMPARTIR", "ALMACENAR", "DESTRUIR"]
    subs = ["Captura y generación", "Atención y operaciones", "Divulgación autorizada", "Retención protegida", "Eliminación segura"]
    xs = [160, 497, 833, 1169, 1506]
    y = 430
    for i, (title, sub, x) in enumerate(zip(steps, subs, xs)):
        d.ellipse((x-92, y-92, x+92, y+92), fill=LIGHT, outline=BLUE, width=7)
        centered(d, (x, y-18), str(i+1), font(32, True), BLUE)
        centered(d, (x, y+36), title, font(22, True), DARK)
        d.rounded_rectangle((x-125, 590, x+125, 705), radius=18, fill="#F7FAFC", outline=MID, width=3)
        centered(d, (x, 648), sub, font(20), DARK)
        if i < 4:
            arrow(d, (x+98, y), (xs[i+1]-98, y))
    centered(d, (w/2, 800), "La privacidad, la seguridad, la necesidad mínima y la evidencia aplican en cada etapa.", font(25, True))
    save(img, "image2.png")


def figure3():
    w, h = 1635, 886
    img = Image.new("RGB", (w, h), WHITE); d = ImageDraw.Draw(img)
    header(d, w, "Salvaguardas de la Regla de Seguridad HIPAA")
    centered(d, (w/2, 250), "ANÁLISIS DE RIESGOS", font(32, True), BLUE)
    d.rounded_rectangle((565, 190, 1070, 310), radius=28, fill=LIGHT, outline=BLUE, width=7)
    groups = [
        ("ADMINISTRATIVAS", "Políticas, funciones, capacitación y gestión de riesgos", BLUE),
        ("FÍSICAS", "Instalaciones, estaciones de trabajo y dispositivos", GREEN),
        ("TÉCNICAS", "Acceso, auditoría, integridad y transmisión", PURPLE),
    ]
    xs = [280, 818, 1355]
    for (title, sub, color), x in zip(groups, xs):
        d.rounded_rectangle((x-220, 470, x+220, 720), radius=30, fill="#F8FAFC", outline=color, width=7)
        centered(d, (x, 530), title, font(28, True), color)
        centered(d, (x, 625), sub, font(21), DARK)
        arrow(d, (w/2, 315), (x, 465), color, 6)
    centered(d, (w/2, 810), "Las medidas seleccionadas deben responder a riesgos documentados y revisarse periódicamente.", font(24, True))
    save(img, "image3.png")


def figure4():
    w, h = 1628, 915
    img = Image.new("RGB", (w, h), WHITE); d = ImageDraw.Draw(img)
    header(d, w, "Flujo de trabajo ante una violación HIPAA")
    stages = [
        ("DESCUBRIR", "Confirmar el evento", RED),
        ("CONTENER", "Limitar la exposición", ORANGE),
        ("EVALUAR", "Analizar naturaleza y riesgo", BLUE),
        ("NOTIFICAR", "Autoridades y personas cuando corresponda", PURPLE),
        ("MEJORAR", "Corregir causas y volver a probar", GREEN),
    ]
    xs = [145, 475, 814, 1153, 1483]
    for i, ((title, sub, color), x) in enumerate(zip(stages, xs)):
        d.rounded_rectangle((x-125, 295, x+125, 600), radius=28, fill="#F8FAFC", outline=color, width=7)
        d.rounded_rectangle((x-105, 325, x+105, 405), radius=16, fill=color)
        centered(d, (x, 365), title, font(24, True), WHITE)
        centered(d, (x, 500), sub, font(19), DARK)
        if i < 4:
            arrow(d, (x+130, 450), (xs[i+1]-130, 450))
    d.rounded_rectangle((180, 700, 1448, 835), radius=24, fill=LIGHT, outline=BLUE, width=4)
    centered(d, (814, 765), "Documentar decisiones, plazos, comunicaciones, evidencia y acciones correctivas.", font(26, True))
    save(img, "image4.png")


def figure5():
    w, h = 1628, 945
    img = Image.new("RGB", (w, h), WHITE); d = ImageDraw.Draw(img)
    header(d, w, "Ciclo de verificación del cumplimiento")
    stages = [
        ("REQUISITO Y ALCANCE", "Definir qué se debe cumplir"),
        ("PROBAR EL CONTROL", "Obtener evidencia suficiente"),
        ("CORREGIR EXCEPCIONES", "Asignar responsables y plazos"),
        ("VOLVER A PROBAR", "Confirmar eficacia"),
        ("CONCLUIR", "Registrar resultado y riesgo residual"),
    ]
    xs = [170, 492, 814, 1136, 1458]
    y = 430
    for i, ((title, sub), x) in enumerate(zip(stages, xs)):
        d.rounded_rectangle((x-140, y-125, x+140, y+125), radius=28, fill=LIGHT, outline=BLUE, width=6)
        centered(d, (x, y-30), title, font(22, True), BLUE)
        centered(d, (x, y+55), sub, font(19), DARK)
        if i < 4:
            arrow(d, (x+145, y), (xs[i+1]-145, y))
    arrow(d, (1458, 570), (1458, 760), GRAY, 5)
    arrow(d, (1458, 760), (170, 760), GRAY, 5)
    arrow(d, (170, 760), (170, 570), GRAY, 5)
    centered(d, (814, 835), "La verificación es iterativa: una excepción no se cierra hasta que la corrección se valida.", font(25, True))
    save(img, "image5.png")


def figure6():
    w, h = 1646, 886
    img = Image.new("RGB", (w, h), WHITE); d = ImageDraw.Draw(img)
    header(d, w, "Trayectoria de un analista HIPAA junior")
    stages = [
        ("APRENDER", "Reglas, terminología y ética"),
        ("MAPEAR", "PHI, procesos, sistemas y terceros"),
        ("PROBAR", "Controles y evidencia"),
        ("DOCUMENTAR", "Hallazgos, riesgos y decisiones"),
        ("APLICAR", "Proyectos y trabajo supervisado"),
    ]
    xs = [165, 494, 823, 1152, 1481]
    for i, ((title, sub), x) in enumerate(zip(stages, xs)):
        d.rounded_rectangle((x-135, 300, x+135, 600), radius=28, fill="#F8FAFC", outline=BLUE, width=6)
        d.ellipse((x-40, 330, x+40, 410), fill=BLUE)
        centered(d, (x, 370), str(i+1), font(29, True), WHITE)
        centered(d, (x, 475), title, font(24, True), BLUE)
        centered(d, (x, 545), sub, font(19), DARK)
        if i < 4:
            arrow(d, (x+140, 450), (xs[i+1]-140, 450))
    centered(d, (w/2, 760), "La práctica ética y documentada convierte el conocimiento en experiencia demostrable.", font(26, True))
    save(img, "image6.png")


def figure7():
    w, h = 1628, 915
    img = Image.new("RGB", (w, h), WHITE); d = ImageDraw.Draw(img)
    header(d, w, "De la salida de una herramienta a la evidencia de cumplimiento")
    stages = [
        ("SALIDA DE LA HERRAMIENTA", "Reporte, alerta o resultado", GRAY),
        ("AUTORIZACIÓN", "Uso aprobado y alcance definido", BLUE),
        ("VALIDACIÓN", "Confirmar exactitud y contexto", ORANGE),
        ("REMEDIACIÓN", "Corregir y documentar", RED),
        ("NUEVA PRUEBA", "Verificar eficacia", GREEN),
        ("EVIDENCIA", "Cadena completa y trazable", PURPLE),
    ]
    xs = [130, 404, 678, 952, 1226, 1500]
    for i, ((title, sub, color), x) in enumerate(zip(stages, xs)):
        d.rounded_rectangle((x-112, 300, x+112, 610), radius=25, fill="#F8FAFC", outline=color, width=6)
        d.rounded_rectangle((x-95, 330, x+95, 410), radius=15, fill=color)
        centered(d, (x, 370), title, font(19, True), WHITE)
        centered(d, (x, 500), sub, font(18), DARK)
        if i < 5:
            arrow(d, (x+117, 455), (xs[i+1]-117, 455))
    d.rounded_rectangle((200, 715, 1428, 835), radius=24, fill=LIGHT, outline=BLUE, width=4)
    centered(d, (814, 775), "Un reporte aislado no prueba cumplimiento; la cadena de decisiones y validaciones sí.", font(26, True))
    save(img, "image7.png")


if __name__ == "__main__":
    figure1(); figure2(); figure3(); figure4(); figure5(); figure6(); figure7()
    print(f"Generated seven review-only HIPAA Spanish candidates in {OUT}")
