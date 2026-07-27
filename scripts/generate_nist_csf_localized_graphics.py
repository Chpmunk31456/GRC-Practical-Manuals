from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

ROOT = Path(__file__).resolve().parents[1]
W, H = 1800, 1000
BG = (255, 255, 255)
NAVY = (17, 44, 86)
BLUE = (35, 108, 181)
TEAL = (25, 135, 125)
GREEN = (54, 139, 72)
GOLD = (224, 159, 31)
ORANGE = (220, 101, 30)
PURPLE = (111, 67, 148)
GRAY = (235, 239, 244)
DARK = (30, 35, 40)
LINE = (80, 90, 105)
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REGULAR, size)


def heading(draw, text):
    draw.text((W // 2, 40), text, font=font(48, True), fill=NAVY, anchor="ma")


def wrapped(draw, xy, text, width, text_font, fill=DARK, anchor="mm"):
    words = text.split()
    lines, current = [], ""
    for word in words:
        candidate = (current + " " + word).strip()
        if draw.textbbox((0, 0), candidate, font=text_font)[2] <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    draw.multiline_text(xy, "\n".join(lines), font=text_font, fill=fill,
                        anchor=anchor, align="center", spacing=6)


def save(image, directory, filename, aliases=()):
    directory.mkdir(parents=True, exist_ok=True)
    image.save(directory / filename, optimize=True)
    for alias in aliases:
        image.save(directory / alias, optimize=True)


def figure1(lang, directory):
    labels = ["GOBERNAR", "IDENTIFICAR", "PROTEGER", "DETECTAR", "RESPONDER", "RECUPERAR"]
    title = "Las seis Funciones del NIST CSF 2.0" if lang == "es" else "As seis Funções do NIST CSF 2.0"
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    heading(draw, title)
    cx, cy, outer, inner = 900, 535, 340, 155
    colors = [PURPLE, BLUE, TEAL, GOLD, ORANGE, GREEN]
    for index, color in enumerate(colors):
        start = -90 + index * 60
        draw.pieslice((cx - outer, cy - outer, cx + outer, cy + outer), start, start + 60,
                      fill=color, outline="white", width=6)
    draw.ellipse((cx - inner, cy - inner, cx + inner, cy + inner), fill="white", outline=NAVY, width=5)
    for index, label in enumerate(labels):
        angle = math.radians(-60 + index * 60)
        x, y = cx + 238 * math.cos(angle), cy + 238 * math.sin(angle)
        wrapped(draw, (x, y), label, 190, font(24, True), fill="white")
    draw.text((cx, cy), "NÚCLEO", font=font(42, True), fill=NAVY, anchor="mm")
    localized = "image1_es-419.png" if lang == "es" else "image1_pt-BR.png"
    save(image, directory, localized, aliases=("image1.png",))


def figure2(lang, directory):
    title = "Jerarquía del Núcleo del CSF" if lang == "es" else "Hierarquia do Núcleo do CSF"
    labels = (["FUNCIONES", "CATEGORÍAS", "SUBCATEGORÍAS", "RESULTADOS DE CIBERSEGURIDAD"]
              if lang == "es" else
              ["FUNÇÕES", "CATEGORIAS", "SUBCATEGORIAS", "RESULTADOS DE CIBERSEGURANÇA"])
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    heading(draw, title)
    y_values = [210, 390, 570, 750]
    widths = [700, 980, 1260, 1540]
    colors = [NAVY, BLUE, TEAL, GREEN]
    for index, (y, width, label, color) in enumerate(zip(y_values, widths, labels, colors)):
        x = (W - width) // 2
        draw.rounded_rectangle((x, y, x + width, y + 120), radius=24, fill=color)
        wrapped(draw, (W // 2, y + 60), label, width - 80, font(36, True), fill="white")
        if index < 3:
            draw.polygon([(W // 2 - 24, y + 135), (W // 2 + 24, y + 135), (W // 2, y + 170)], fill=DARK)
    localized = "image2_es-419.png" if lang == "es" else "image2_pt-BR.png"
    save(image, directory, localized, aliases=("image2.png",))


def figure3(lang, directory):
    title = "Del Perfil actual al plan de acción" if lang == "es" else "Do Perfil atual ao plano de ação"
    texts = (["PERFIL ACTUAL", "PERFIL OBJETIVO", "BRECHAS PRIORIZADAS", "PLAN DE ACCIÓN BASADO EN RIESGOS"]
             if lang == "es" else
             ["PERFIL ATUAL", "PERFIL-ALVO", "LACUNAS PRIORIZADAS", "PLANO DE AÇÃO BASEADO EM RISCOS"])
    items = (["Responsables", "Financiamiento", "Hitos", "Medidas"] if lang == "es" else
             ["Responsáveis", "Recursos financeiros", "Marcos", "Medidas"])
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    heading(draw, title)
    xs = [160, 520, 880, 1240]
    colors = [GRAY, BLUE, GOLD, GREEN]
    text_colors = [DARK, "white", DARK, "white"]
    for index, (x, text, color, text_color) in enumerate(zip(xs, texts, colors, text_colors)):
        draw.rounded_rectangle((x, 250, x + 300, 460), radius=26, fill=color, outline=NAVY, width=3)
        wrapped(draw, (x + 150, 355), text, 250, font(32, True), fill=text_color)
        if index < 3:
            draw.line((x + 300, 355, x + 350, 355), fill=DARK, width=10)
            draw.polygon([(x + 350, 335), (x + 390, 355), (x + 350, 375)], fill=DARK)
    for index, item in enumerate(items):
        x, y = 310 + index * 320, 610
        draw.rounded_rectangle((x, y, x + 250, y + 120), radius=18, fill=(245, 247, 250), outline=BLUE, width=3)
        wrapped(draw, (x + 125, y + 60), item, 210, font(28, True), fill=NAVY)
        draw.line((1390, 460, x + 125, y), fill=LINE, width=3)
    localized = "image3_es-419.png" if lang == "es" else "image3_pt-BR.png"
    alias = "image3_es.png" if lang == "es" else "image3_pt.png"
    save(image, directory, localized, aliases=(alias,))


def figure4(lang, directory):
    title = "Niveles de Implementación del CSF" if lang == "es" else "Níveis de Implementação do CSF"
    levels = (["Nivel 1 - Parcial", "Nivel 2 - Informado por el riesgo", "Nivel 3 - Repetible", "Nivel 4 - Adaptable"]
              if lang == "es" else
              ["Nível 1 - Parcial", "Nível 2 - Informado pelo risco", "Nível 3 - Repetível", "Nível 4 - Adaptável"])
    side = (["Rigor de la gobernanza", "Prácticas de gestión de riesgos", "Mejora continua"]
            if lang == "es" else
            ["Rigor da governança", "Práticas de gestão de riscos", "Melhoria contínua"])
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    heading(draw, title)
    colors = [GRAY, (194, 220, 244), (112, 181, 214), GREEN]
    for index, (label, color) in enumerate(zip(levels, colors)):
        x, top = 140 + index * 390, 690 - index * 125
        draw.rounded_rectangle((x, top, x + 330, 840), radius=20, fill=color, outline=NAVY, width=3)
        wrapped(draw, (x + 165, top + 60), label, 290, font(27, True), fill=DARK if index < 3 else "white")
    draw.line((120, 885, 1600, 285), fill=ORANGE, width=10)
    draw.polygon([(1575, 278), (1625, 268), (1600, 320)], fill=ORANGE)
    for index, text in enumerate(side):
        draw.text((1420, 180 + index * 55), text, font=font(24, True), fill=NAVY, anchor="ma")
    localized = "image4_es-419.png" if lang == "es" else "image4_pt-BR.png"
    alias = "image4_es.png" if lang == "es" else "image4_pt.png"
    save(image, directory, localized, aliases=(alias,))


def figure5(lang, directory):
    title = ("Ciclo de vida de la ciberseguridad de la cadena de suministro" if lang == "es" else
             "Ciclo de vida da cibersegurança da cadeia de suprimentos")
    labels = (["Planificar", "Seleccionar", "Contratar", "Supervisar", "Responder y recuperar", "Finalizar la relación"]
              if lang == "es" else
              ["Planejar", "Selecionar", "Contratar", "Monitorar", "Responder e recuperar", "Encerrar a relação"])
    supports = (["Responsabilidades de seguridad definidas", "Debida diligencia", "Requisitos contractuales",
                 "Monitoreo continuo", "Gestión de incidentes", "Retiro de accesos y datos"]
                if lang == "es" else
                ["Responsabilidades de segurança definidas", "Devida diligência", "Requisitos contratuais",
                 "Monitoramento contínuo", "Gestão de incidentes", "Remoção de acessos e dados"])
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    heading(draw, title)
    cx, cy, radius = 900, 535, 270
    colors = [NAVY, BLUE, TEAL, GREEN, GOLD, ORANGE]
    points = []
    for index in range(6):
        angle = math.radians(-90 + index * 60)
        points.append((cx + radius * math.cos(angle), cy + radius * math.sin(angle)))
    for index in range(6):
        draw.line((*points[index], *points[(index + 1) % 6]), fill=(150, 160, 175), width=5)
    for index, (label, support, color) in enumerate(zip(labels, supports, colors)):
        angle = math.radians(-90 + index * 60)
        x, y = points[index]
        draw.ellipse((x - 105, y - 105, x + 105, y + 105), fill=color, outline="white", width=5)
        wrapped(draw, (x, y), f"{index + 1}. {label}", 170, font(22, True), fill="white")
        xo, yo = cx + (radius + 185) * math.cos(angle), cy + (radius + 185) * math.sin(angle)
        wrapped(draw, (xo, yo), support, 250, font(18), fill=DARK)
    draw.ellipse((cx - 120, cy - 120, cx + 120, cy + 120), fill="white", outline=NAVY, width=5)
    wrapped(draw, (cx, cy), "CICLO DE\nVIDA", 190, font(34, True), fill=NAVY)
    localized = "image5_es-419.png" if lang == "es" else "image5_pt-BR.png"
    alias = "image5_es.png" if lang == "es" else "image5_pt.png"
    save(image, directory, localized, aliases=(alias,))


def figure6(lang, directory):
    title = "Cadena del resultado a la evidencia" if lang == "es" else "Cadeia do resultado à evidência"
    labels = (["Resultado del CSF", "Riesgo", "Control", "Implementación", "Evidencia operativa", "Prueba",
               "Excepción", "Acción correctiva", "Reprueba", "Conclusión"]
              if lang == "es" else
              ["Resultado do CSF", "Risco", "Controle", "Implementação", "Evidência operacional", "Teste",
               "Exceção", "Ação corretiva", "Novo teste", "Conclusão"])
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    heading(draw, title)
    colors = [NAVY, BLUE, TEAL, GREEN, GOLD, ORANGE, PURPLE, BLUE, TEAL, GREEN]
    start_x, y, box_width, gap = 80, 420, 145, 25
    for index, (label, color) in enumerate(zip(labels, colors)):
        x = start_x + index * (box_width + gap)
        draw.rounded_rectangle((x, y, x + box_width, y + 170), radius=18, fill=color)
        wrapped(draw, (x + box_width / 2, y + 85), label, box_width - 20, font(22, True), fill="white")
        if index < 9:
            draw.line((x + box_width, y + 85, x + box_width + gap - 5, y + 85), fill=DARK, width=5)
            draw.polygon([(x + box_width + gap - 5, y + 75), (x + box_width + gap + 10, y + 85),
                          (x + box_width + gap - 5, y + 95)], fill=DARK)
    draw.arc((950, 620, 1510, 920), 0, 180, fill=ORANGE, width=6)
    draw.text((1230, 880), "ciclo de mejora" if lang == "es" else "ciclo de melhoria",
              font=font(26, True), fill=ORANGE, anchor="mm")
    localized = "image6_es-419.png" if lang == "es" else "image6_pt-BR.png"
    alias = "image6_es.png" if lang == "es" else "image6_pt.png"
    save(image, directory, localized, aliases=(alias,))


def update_markdown(path, lang):
    text = path.read_text(encoding="utf-8")
    if lang == "es":
        replacements = {
            'media/image1.png': 'media/image1_es-419.png',
            'alt="GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND y RECOVER funcionan como un sistema conectado."':
                'alt="Las Funciones Gobernar, Identificar, Proteger, Detectar, Responder y Recuperar operan como un sistema conectado."',
            'media/image2.png': 'media/image2_es-419.png',
            'media/image3_es.png': 'media/image3_es-419.png',
            'media/image4_es.png': 'media/image4_es-419.png',
            'media/image5_es.png': 'media/image5_es-419.png',
            'media/image6_es.png': 'media/image6_es-419.png',
        }
    else:
        replacements = {
            'media/image1.png': 'media/image1_pt-BR.png',
            'alt="GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND e RECOVER funcionam como um sistema conectado."':
                'alt="As Funções Governar, Identificar, Proteger, Detectar, Responder e Recuperar operam como um sistema conectado."',
            'media/image2.png': 'media/image2_pt-BR.png',
            'media/image3_pt.png': 'media/image3_pt-BR.png',
            'media/image4_pt.png': 'media/image4_pt-BR.png',
            'media/image5_pt.png': 'media/image5_pt-BR.png',
            'media/image6_pt.png': 'media/image6_pt-BR.png',
        }
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


def main():
    editions = {
        "es": ROOT / "01-foundations/NIST_CSF_2/Espanol",
        "pt": ROOT / "01-foundations/NIST_CSF_2/Portugues_BR",
    }
    markdown = {
        "es": editions["es"] / "NIST_CSF_2_Practical_GRC_and_Junior_Analyst_Manual_Espanol_v1.0.md",
        "pt": editions["pt"] / "NIST_CSF_2_Practical_GRC_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md",
    }
    for lang, edition in editions.items():
        media = edition / "media"
        figure1(lang, media)
        figure2(lang, media)
        figure3(lang, media)
        figure4(lang, media)
        figure5(lang, media)
        figure6(lang, media)
        update_markdown(markdown[lang], lang)
    print("Generated 12 localized NIST CSF graphics and updated both Markdown editions.")


if __name__ == "__main__":
    main()
