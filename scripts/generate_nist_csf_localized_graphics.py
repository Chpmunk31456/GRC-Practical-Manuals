from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
import re

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
FONT_REGULAR = (
    "C:/Windows/Fonts/arial.ttf"
    if Path("C:/Windows/Fonts/arial.ttf").exists()
    else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
)
FONT_BOLD = (
    "C:/Windows/Fonts/arialbd.ttf"
    if Path("C:/Windows/Fonts/arialbd.ttf").exists()
    else "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
)
HTML_IMAGE_RE = re.compile(
    r'<img\s+src="(?P<src>[^"]+)"\s+style="width:(?P<width>[^;"]+);'
    r'height:(?P<height>[^"]+)"\s+alt="(?P<alt>[^"]*)"\s*/?>',
    re.IGNORECASE,
)


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REGULAR, size)


def heading(draw, text):
    draw.text((W // 2, 40), text, font=font(48, True), fill=NAVY, anchor="ma")


def wrapped(draw, xy, text, width, text_font, fill=DARK, anchor="mm", spacing=6):
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
    draw.multiline_text(
        xy, "\n".join(lines), font=text_font, fill=fill,
        anchor=anchor, align="center", spacing=spacing
    )


def save(image, directory, filename, aliases=()):
    directory.mkdir(parents=True, exist_ok=True)
    image.save(directory / filename, optimize=True)
    for alias in aliases:
        image.save(directory / alias, optimize=True)


def figure1(lang, directory):
    labels = (["GOBERNAR", "IDENTIFICAR", "PROTEGER", "DETECTAR", "RESPONDER", "RECUPERAR"]
              if lang == "es" else
              ["GOVERNAR", "IDENTIFICAR", "PROTEGER", "DETECTAR", "RESPONDER", "RECUPERAR"])
    title = "Las seis Funciones del NIST CSF 2.0" if lang == "es" else "As seis Funções do NIST CSF 2.0"
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    heading(draw, title)
    cx, cy, outer, inner = 900, 545, 325, 150
    colors = [PURPLE, BLUE, TEAL, GOLD, ORANGE, GREEN]
    for index, color in enumerate(colors):
        start = -90 + index * 60
        draw.pieslice((cx - outer, cy - outer, cx + outer, cy + outer), start, start + 60,
                      fill=color, outline="white", width=6)
    draw.ellipse((cx - inner, cy - inner, cx + inner, cy + inner), fill="white", outline=NAVY, width=5)
    for index, label in enumerate(labels):
        angle = math.radians(-60 + index * 60)
        x, y = cx + 225 * math.cos(angle), cy + 225 * math.sin(angle)
        wrapped(draw, (x, y), label, 155, font(21, True), fill="white", spacing=3)
    core = "NÚCLEO" if lang == "es" else "NÚCLEO"
    draw.text((cx, cy), core, font=font(40, True), fill=NAVY, anchor="mm")
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
        x, top = 120 + index * 375, 690 - index * 115
        draw.rounded_rectangle((x, top, x + 315, 835), radius=20, fill=color, outline=NAVY, width=3)
        wrapped(draw, (x + 157, top + 65), label, 265, font(25, True), fill=DARK if index < 3 else "white")
    draw.line((115, 875, 1600, 300), fill=ORANGE, width=8)
    draw.polygon([(1575, 293), (1625, 282), (1600, 335)], fill=ORANGE)
    panel = (1250, 120, 1710, 265)
    draw.rounded_rectangle(panel, radius=18, fill=(248, 250, 253), outline=BLUE, width=2)
    for index, text in enumerate(side):
        draw.text((1480, 150 + index * 42), text, font=font(21, True), fill=NAVY, anchor="ma")
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
    cx, cy, radius = 900, 535, 250
    colors = [NAVY, BLUE, TEAL, GREEN, GOLD, ORANGE]
    points = []
    for index in range(6):
        angle = math.radians(-90 + index * 60)
        points.append((cx + radius * math.cos(angle), cy + radius * math.sin(angle)))
    for index in range(6):
        draw.line((*points[index], *points[(index + 1) % 6]), fill=(150, 160, 175), width=5)
    support_positions = [(900, 135), (1435, 285), (1460, 745), (900, 900), (340, 745), (335, 285)]
    for index, (label, support, color) in enumerate(zip(labels, supports, colors)):
        x, y = points[index]
        draw.ellipse((x - 98, y - 98, x + 98, y + 98), fill=color, outline="white", width=5)
        wrapped(draw, (x, y), f"{index + 1}. {label}", 155, font(20, True), fill="white", spacing=3)
        xo, yo = support_positions[index]
        wrapped(draw, (xo, yo), support, 280, font(17, True), fill=DARK, spacing=3)
    draw.ellipse((cx - 112, cy - 112, cx + 112, cy + 112), fill="white", outline=NAVY, width=5)
    center_text = "CICLO DE\nVIDA"
    wrapped(draw, (cx, cy), center_text, 180, font(32, True), fill=NAVY)
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
    box_width, box_height, gap = 300, 145, 30
    start_x, start_y = 120, 245
    for index, (label, color) in enumerate(zip(labels, colors)):
        row, col = divmod(index, 5)
        x = start_x + col * (box_width + gap)
        y = start_y + row * 280
        draw.rounded_rectangle((x, y, x + box_width, y + box_height), radius=18, fill=color)
        wrapped(draw, (x + box_width / 2, y + box_height / 2), label, box_width - 38,
                font(25, True), fill="white", spacing=4)
        if col < 4:
            draw.line((x + box_width, y + box_height / 2, x + box_width + gap - 8, y + box_height / 2),
                      fill=DARK, width=5)
            draw.polygon([(x + box_width + gap - 8, y + box_height / 2 - 10),
                          (x + box_width + gap + 7, y + box_height / 2),
                          (x + box_width + gap - 8, y + box_height / 2 + 10)], fill=DARK)
    draw.line((1590, 390, 1590, 500), fill=DARK, width=5)
    draw.polygon([(1580, 495), (1590, 512), (1600, 495)], fill=DARK)
    draw.arc((1050, 690, 1600, 930), 0, 180, fill=ORANGE, width=7)
    draw.text((1325, 900), "ciclo de mejora" if lang == "es" else "ciclo de melhoria",
              font=font(26, True), fill=ORANGE, anchor="mm")
    localized = "image6_es-419.png" if lang == "es" else "image6_pt-BR.png"
    alias = "image6_es.png" if lang == "es" else "image6_pt.png"
    save(image, directory, localized, aliases=(alias,))


def five_step_figure(lang, directory, number, labels, details, footer):
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    colors = [NAVY, BLUE, TEAL, GOLD, GREEN]
    box_width, box_height, gap = 300, 250, 30
    start_x, start_y = 65, 315
    for index, (label, detail, color) in enumerate(zip(labels, details, colors)):
        x = start_x + index * (box_width + gap)
        draw.rounded_rectangle(
            (x, start_y, x + box_width, start_y + box_height),
            radius=22,
            fill=color,
        )
        wrapped(
            draw,
            (x + box_width / 2, start_y + 92),
            label,
            box_width - 35,
            font(31, True),
            fill="white",
        )
        wrapped(
            draw,
            (x + box_width / 2, start_y + 175),
            detail,
            box_width - 35,
            font(23),
            fill="white",
        )
        if index < 4:
            arrow_y = start_y + box_height / 2
            draw.line(
                (x + box_width, arrow_y, x + box_width + gap - 8, arrow_y),
                fill=LINE,
                width=7,
            )
            draw.polygon(
                [
                    (x + box_width + gap - 8, arrow_y - 12),
                    (x + box_width + gap + 7, arrow_y),
                    (x + box_width + gap - 8, arrow_y + 12),
                ],
                fill=LINE,
            )
    wrapped(draw, (W // 2, 750), footer, W - 120, font(38, True), fill=NAVY)
    locale = "es-419" if lang == "es" else "pt-BR"
    save(image, directory, f"image{number}_{locale}.png")


def figure7(lang, directory):
    labels = (
        ["AUTORIZAR", "RECOPILAR", "VALIDAR", "CORREGIR", "VOLVER A PROBAR"]
        if lang == "es"
        else ["AUTORIZAR", "COLETAR", "VALIDAR", "CORRIGIR", "TESTAR NOVAMENTE"]
    )
    details = (
        ["Alcance escrito", "Resultado versionado", "Revisión humana", "Responsable + fecha", "Prueba de cierre"]
        if lang == "es"
        else ["Escopo escrito", "Resultado versionado", "Revisão humana", "Responsável + data", "Prova de encerramento"]
    )
    footer = (
        "Un informe de herramienta es una entrada, no prueba de que se logró un resultado del CSF"
        if lang == "es"
        else "Um relatório de ferramenta é uma entrada, não prova de que um resultado do CSF foi alcançado"
    )
    five_step_figure(lang, directory, 7, labels, details, footer)


def figure8(lang, directory):
    labels = (
        ["APRENDER", "MAPEAR", "PROBAR", "INFORMAR", "APLICAR"]
        if lang == "es"
        else ["APRENDER", "MAPEAR", "TESTAR", "RELATAR", "APLICAR"]
    )
    details = (
        ["Núcleo + riesgo", "Activos + resultados", "Controles + evidencia", "Brechas + acciones", "Rol júnior"]
        if lang == "es"
        else ["Núcleo + risco", "Ativos + resultados", "Controles + evidências", "Lacunas + ações", "Função júnior"]
    )
    footer = (
        "Un portafolio sólido demuestra alcance honesto, evidencia confiable, redacción clara y práctica segura"
        if lang == "es"
        else "Um portfólio sólido demonstra escopo honesto, evidências confiáveis, redação clara e prática segura"
    )
    five_step_figure(lang, directory, 8, labels, details, footer)


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
            'media/image3_ptbr.png': 'media/image3_pt-BR.png',
            'media/image4_pt.png': 'media/image4_pt-BR.png',
            'media/image4_ptbr.png': 'media/image4_pt-BR.png',
            'media/image5_pt.png': 'media/image5_pt-BR.png',
            'media/image5_ptbr.png': 'media/image5_pt-BR.png',
            'media/image6_pt.png': 'media/image6_pt-BR.png',
            'media/image6_ptbr.png': 'media/image6_pt-BR.png',
        }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = HTML_IMAGE_RE.sub(
        lambda match: (
            f'![{match.group("alt")}]({match.group("src")})'
            f'{{width={match.group("width")} height={match.group("height")}}}'
        ),
        text,
    )
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
        figure7(lang, media)
        figure8(lang, media)
        update_markdown(markdown[lang], lang)
    print("Generated 16 localized NIST CSF graphics and updated both Markdown editions.")


if __name__ == "__main__":
    main()
