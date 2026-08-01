from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT=Path('01-foundations/CIS_Controls_v8.1/Espanol/media'); OUT.mkdir(parents=True,exist_ok=True)
W,H=1600,900
try:
 T=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',44); B=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',27)
except OSError:T=B=ImageFont.load_default()

def fig(n,title,labels):
 im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im)
 tw=d.textbbox((0,0),title,font=T)[2]; d.text(((W-tw)/2,45),title,font=T,fill='black')
 count=len(labels); gap=35; bw=(W-140-gap*(count-1))/count; y1,y2=330,570
 for i,label in enumerate(labels):
  x1=70+i*(bw+gap); x2=x1+bw
  d.rounded_rectangle((x1,y1,x2,y2),24,fill='#e8f2f8',outline='black',width=3)
  words=label.split(); lines=[]; line=''
  for w in words:
   test=(line+' '+w).strip()
   if d.textbbox((0,0),test,font=B)[2] <= bw-30: line=test
   else: lines.append(line); line=w
  if line: lines.append(line)
  yy=y1+(y2-y1-len(lines)*36)/2
  for line in lines:
   lw=d.textbbox((0,0),line,font=B)[2]; d.text((x1+(bw-lw)/2,yy),line,font=B,fill='black'); yy+=36
  if i<count-1:
   d.line((x2+5,450,x2+gap-5,450),fill='black',width=5); d.polygon([(x2+gap-5,450),(x2+gap-25,438),(x2+gap-25,462)],fill='black')
 im.save(OUT/f'image{n}.png',optimize=True)

fig(1,'Los 18 CIS Critical Security Controls',['Activos','Software','Datos','Configuración','Cuentas','Acceso'])
fig(2,'Progresión de los Grupos de Implementación',['IG1: 56','IG2: +74','IG3: +23 = 153'])
fig(4,'Ciclo de inventario de activos y software',['Descubrir','Conciliar','Responder','Revisar','Actualizar'])
fig(5,'Ciclo de vida de protección de datos',['Descubrir','Clasificar','Proteger','Conservar','Eliminar'])
fig(6,'Ciclo de vida de identidad y acceso',['Solicitar','Aprobar','Provisionar','Revisar','Revocar'])
fig(7,'Ciclo de gestión de vulnerabilidades',['Inventariar','Evaluar','Priorizar','Corregir','Verificar'])
fig(8,'Flujo de gestión y análisis de registros',['Fuentes','Recopilar','Normalizar','Analizar','Responder'])
fig(9,'Ciclo de respuesta a incidentes',['Preparar','Detectar','Analizar','Contener','Recuperar','Mejorar'])
fig(10,'Ciclo de mejora de CIS Controls',['Priorizar','Implementar','Medir','Corregir','Repetir pruebas'])
for n in range(1,11):
 p=OUT/f'image{n}.png'
 if not p.exists() or p.stat().st_size==0: raise SystemExit(f'Missing figure {n}')
print('Complete CIS Spanish figure set is present.')
