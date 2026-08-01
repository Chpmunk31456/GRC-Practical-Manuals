#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import json

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / '01-foundations/CIS_Controls_v8.1/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_v1.0.docx'
OUT = ROOT / 'review/cis-controls-v8.1-localized-figures'
OUT.mkdir(parents=True, exist_ok=True)

PT = {
1: ('Os 18 Controles Críticos de Segurança CIS', ['Inventário', 'Configuração', 'Acesso', 'Vulnerabilidades', 'Monitoramento', 'Resposta']),
2: ('Progressão dos Grupos de Implementação', ['IG1: higiene essencial', 'IG2: maturidade ampliada', 'IG3: proteção avançada']),
3: ('Estrutura de medição de salvaguardas', ['Entradas definidas', 'Operações', 'Medidas', 'Métricas', 'Revisão do procedimento']),
4: ('Ciclo de inventário de ativos e software', ['Descobrir', 'Reconciliar', 'Responder', 'Revisar']),
5: ('Ciclo de vida de proteção de dados', ['Descobrir', 'Classificar', 'Proteger', 'Reter', 'Eliminar']),
6: ('Ciclo de vida de identidade e acesso', ['Solicitar', 'Aprovar', 'Autenticar', 'Revisar', 'Revogar']),
7: ('Gestão contínua de vulnerabilidades', ['Cobertura', 'Priorizar', 'Corrigir', 'Verificar']),
8: ('Fluxo de monitoramento até resposta', ['Centralizar contexto', 'Detectar', 'Investigar', 'Responder']),
9: ('Preparação para resposta a incidentes', ['Papéis', 'Comunicação', 'Exercícios', 'Lições aprendidas']),
10: ('Caminho do analista júnior de Controles CIS', ['Aprender', 'Mapear salvaguardas', 'Medir evidências', 'Relatar lacunas', 'Criar portfólio honesto']),
}
ES3 = ('Estructura de medición de salvaguardias CIS', ['Datos definidos', 'Operaciones', 'Medidas', 'Métricas', 'Revisión del procedimiento'])


def font(size, bold=False):
    p = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    return ImageFont.truetype(p, size)


def wrap(draw, text, fnt, maxw):
    words, lines, current = text.split(), [], ''
    for w in words:
        test = (current + ' ' + w).strip()
        if draw.textbbox((0,0), test, font=fnt)[2] <= maxw:
            current = test
        else:
            if current: lines.append(current)
            current = w
    if current: lines.append(current)
    return lines


def render(size, title, stages, dest):
    w,h=size
    im=Image.new('RGB', size, 'white'); d=ImageDraw.Draw(im)
    margin=max(28,w//45); titlef=font(max(28,w//38),True); bodyf=font(max(20,w//58),True); small=font(max(16,w//75))
    d.rounded_rectangle((margin,margin,w-margin,h-margin), radius=max(18,w//80), outline='black', width=max(3,w//350))
    tw=d.textbbox((0,0),title,font=titlef)[2]; d.text(((w-tw)/2,margin*1.4),title,font=titlef,fill='black')
    n=len(stages); gap=max(18,w//100); usable=w-2*margin-gap*(n-1); bw=usable/n; y1=h*0.38; y2=h*0.67
    centers=[]
    for i,s in enumerate(stages):
        x1=margin+i*(bw+gap); x2=x1+bw; centers.append(((x1+x2)/2,(y1+y2)/2))
        d.rounded_rectangle((x1,y1,x2,y2), radius=max(12,w//120), outline='black', width=max(3,w//420))
        lines=wrap(d,s,bodyf,bw-24); total=len(lines)*(bodyf.size+5); yy=(y1+y2-total)/2
        for line in lines:
            lw=d.textbbox((0,0),line,font=bodyf)[2]; d.text(((x1+x2-lw)/2,yy),line,font=bodyf,fill='black'); yy+=bodyf.size+5
    for i in range(n-1):
        x1=centers[i][0]+bw/2; x2=centers[i+1][0]-bw/2
        d.line((x1,centers[i][1],x2,centers[i+1][1]),fill='black',width=max(3,w//420))
        d.polygon([(x2,centers[i+1][1]),(x2-14,centers[i+1][1]-9),(x2-14,centers[i+1][1]+9)],fill='black')
    note='Candidato de revisión localizado; requiere aprobación visual antes de promoción.' if 'Estructura' in title else 'Candidato de revisão localizado; requer aprovação visual antes da promoção.'
    nw=d.textbbox((0,0),note,font=small)[2]; d.text(((w-nw)/2,h-margin*2.0),note,font=small,fill='black')
    im.save(dest,'PNG')

with ZipFile(DOCX) as z:
    dims={}
    for i in range(1,11):
        data=z.read(f'word/media/image{i}.png')
        with Image.open(BytesIO(data)) as src: dims[i]=src.size

for i in range(1,11):
    render(dims[i], PT[i][0], PT[i][1], OUT/f'pt-BR-image{i}.png')
render(dims[3], ES3[0], ES3[1], OUT/'es-LATAM-image3.png')
(OUT/'manifest.json').write_text(json.dumps({'source_docx':str(DOCX.relative_to(ROOT)),'dimensions':{str(k):v for k,v in dims.items()},'files':['es-LATAM-image3.png']+[f'pt-BR-image{i}.png' for i in range(1,11)]},indent=2,ensure_ascii=False),encoding='utf-8')
print('Generated 11 CIS localized review candidates.')
