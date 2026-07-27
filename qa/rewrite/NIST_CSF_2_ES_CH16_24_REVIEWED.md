# NIST CSF 2.0 — Reescritura revisada en español latinoamericano

## Capítulos 16–24

**Estado:** contenido fuente revisado para integración.  
**Idioma:** español latinoamericano neutral.  
**Regla editorial:** conservar los identificadores NIST, los nombres propios de herramientas, las direcciones oficiales y los límites de autorización.

# 16. Herramientas de código abierto para trabajar con el CSF

*Enlaces oficiales, inicios rápidos seguros, apoyo posible al CSF, evidencia y limitaciones.*

<img src="media/image7_es-419.png" style="width:6.15in;height:3.39605in" alt="La autorización, la validación, la acción correctiva y la repetición de pruebas convierten los resultados técnicos en evidencia útil." />

Figura 7. Del resultado de una herramienta a evidencia útil

| **Herramienta** | **Propósito** | **Posible apoyo al CSF** |
|---|---|---|
| CISO Assistant | GRC, Perfiles, riesgos, controles y evidencia | GV, ID y presentación de informes |
| Wazuh | SIEM, monitoreo de endpoints e integridad | DE.CM, DE.AE y RS.MA |
| osquery | Inventario de endpoints y evidencia basada en consultas | ID.AM, PR.PS y PR.AA |
| OpenSCAP | Evaluación de configuración de Linux | PR.PS e ID.IM |
| Greenbone Community Edition | Evaluación de vulnerabilidades | ID.RA e ID.IM |
| Trivy | Análisis de código, imágenes, dependencias, secretos y configuración | ID.RA y PR.PS |
| OWASP ZAP | Evaluación autorizada de aplicaciones web | ID.RA e ID.IM |
| Keycloak | Identidad, roles, autenticación y MFA | PR.AA |
| DefectDojo | Recepción de hallazgos y seguimiento de remediación | ID.RA, ID.IM y GV.OV |
| Velociraptor | Visibilidad de endpoints y respuesta a incidentes | DE.CM y RS.AN |
| Open Policy Agent | Política como código | GV.PO, PR.AA y PR.PS |
| OpenSearch | Búsqueda, analítica, tableros y monitoreo de seguridad | DE.CM, DE.AE y GV.OV |

## 16.1 Lista de verificación para validar herramientas

- Aprobar el propósito, propietario, alcance, datos, sistemas, alojamiento, acceso de soporte y retención.
- Verificar la fuente oficial, versión, dependencias, integridad, método de actualización y configuración segura.
- Probar una condición conocida que la herramienta deba detectar o bloquear.
- Probar una condición permitida conocida para identificar fallas innecesarias.
- Comparar la cobertura con una población independiente de activos, agentes, repositorios o identidades.
- Restringir la administración, proteger credenciales e informes, registrar cambios y probar el respaldo o la recuperación de la herramienta.
- Definir validación humana, escalamiento, excepciones, corrección y repetición de pruebas.
- Revalidar después de actualizaciones importantes, cambios de integración o configuración, o fallas.

## 16.2–16.13 Guía común para las herramientas

Para CISO Assistant, Wazuh, osquery, OpenSCAP, Greenbone Community Edition, Trivy, OWASP ZAP, Keycloak, DefectDojo, Velociraptor, Open Policy Agent y OpenSearch:

1. Usar únicamente sistemas propios o expresamente autorizados por escrito.
2. Registrar versión, configuración, alcance, población objetivo, fecha, operador y revisor.
3. Conservar resultados sin procesar, decisiones, excepciones, acciones correctivas y repetición de pruebas.
4. Validar al menos una condición conocida y una condición permitida.
5. No presentar el resultado de una herramienta como certificación, cumplimiento legal, cobertura completa o conclusión de auditoría.

### Inicios rápidos revisados

- **CISO Assistant:** crear una organización ficticia, seleccionar cinco resultados del CSF, asignar responsables, adjuntar evidencia depurada, registrar una brecha y crear un plan de acción.
- **Wazuh:** conectar un endpoint autorizado de laboratorio, generar un evento inocuo, revisar la alerta y conservar el evento y el ticket.
- **osquery:** consultar usuarios, software, servicios, cifrado o procesos en un endpoint de laboratorio y registrar consulta, host, hora, salida y revisión.
- **OpenSCAP:** evaluar un Linux autorizado contra un perfil adecuado, corregir una configuración aprobada y comparar informes antes y después.
- **Greenbone Community Edition:** analizar únicamente un objetivo autorizado, validar un hallazgo, corregirlo, volver a analizar y documentar limitaciones.
- **Trivy:** analizar una imagen fijada o repositorio de prueba, proteger el informe, validar un resultado, corregirlo y repetir el análisis.
- **OWASP ZAP:** usar una aplicación local de entrenamiento, comenzar con análisis pasivo y conservar alcance y resultados aprobados.
- **Keycloak:** crear un realm de laboratorio, usuarios, roles y MFA; probar privilegio mínimo, acceso fallido y eliminación.
- **DefectDojo:** importar un informe de laboratorio, validar y asignar un hallazgo, registrar la corrección, repetir la prueba y cerrar con evidencia.
- **Velociraptor:** usar un cliente aislado, recopilar un artefacto inocuo autorizado y registrar propósito, alcance, revisión y preservación.
- **Open Policy Agent:** escribir una regla de laboratorio que exija propietario, clasificación y ambiente aprobado; probar entradas permitidas y denegadas.
- **OpenSearch:** cargar eventos sintéticos, crear una búsqueda y un tablero, y documentar cobertura, acceso, retención y limitaciones.

## 16.14 Herramientas oficiales de NIST

- **Herramienta de referencia del CSF 2.0:** explorar y exportar el Núcleo oficial.
- **Perfiles Organizacionales:** usar la orientación y las plantillas oficiales de NIST.

# 17. Guía práctica del CSF para gerentes

## 17.1 Preguntas mensuales

- ¿Qué cambió en la misión, sistemas, datos, amenazas, obligaciones, proveedores o apetito de riesgo?
- ¿Qué riesgos superan la tolerancia y quién tiene autoridad para decidir?
- ¿Las conclusiones del Perfil actual están respaldadas por evidencia confiable?
- ¿Qué planes de acción están atrasados, bloqueados, subfinanciados o dependen de terceros?
- ¿Los proveedores críticos están monitoreados e incluidos en respuesta y recuperación?
- ¿Las fallas, incidentes, ejercicios, pruebas y cuasi incidentes generaron mejoras?
- ¿Los servicios críticos pueden recuperarse dentro de los objetivos aprobados?
- ¿Qué limitaciones debe comprender la dirección antes de confiar en el tablero?

## 17.2 Tablero

| **Área** | **Pregunta de gestión** | **Estado** |
|---|---|---|
| Gobernanza | ¿Estrategia, política, roles, recursos y supervisión están alineados con el riesgo? | Verde / Amarillo / Rojo |
| Perfil | ¿El alcance está actualizado y el Perfil objetivo está aprobado? | Verde / Amarillo / Rojo |
| Riesgo | ¿Qué riesgos residuales superan la tolerancia? | Verde / Amarillo / Rojo |
| Activos | ¿Se conocen activos, datos, flujos y proveedores críticos? | Verde / Amarillo / Rojo |
| Protección | ¿Funcionan los controles de identidad, datos, plataforma, formación y resiliencia? | Verde / Amarillo / Rojo |
| Detección | ¿El monitoreo es completo, revisado y conectado con criterios de incidente? | Verde / Amarillo / Rojo |
| Respuesta | ¿Los incidentes se clasifican, analizan, comunican, contienen y erradican? | Verde / Amarillo / Rojo |
| Recuperación | ¿Se ha demostrado la integridad de la restauración y los objetivos de servicio? | Verde / Amarillo / Rojo |
| Mejora | ¿Los hallazgos fueron corregidos y sometidos a nuevas pruebas independientes? | Verde / Amarillo / Rojo |

## 17.3 Errores comunes

- Tratar el CSF como lista de verificación de TI y no como trabajo de riesgo empresarial.
- Comenzar con herramientas antes que con misión, alcance, riesgo y resultados.
- Marcar resultados como logrados únicamente por existir una política.
- Usar una sola puntuación que oculte debilidades críticas y diferencias de alcance.
- Describir los Niveles como madurez sin considerar el contexto previsto por NIST.
- Copiar un Perfil objetivo sin adaptarlo al riesgo de la organización.
- Ignorar proveedores, nube, OT, datos, personas, instalaciones y dependencias.
- Cerrar hallazgos sin repetir las pruebas.
- Presentar la alineación con el CSF como cumplimiento legal o certificación de NIST.

# 18. De principiante a analista junior

<img src="media/image8_es-419.png" style="width:6.15in;height:3.20335in" alt="Aprender, mapear, probar, informar y postularse con evidencia honesta de portafolio." />

Figura 8. Ruta hacia el puesto de analista junior

## 18.1 Puestos de nivel inicial

Analista junior de GRC; analista de riesgo de ciberseguridad; analista de cumplimiento; analista de controles de seguridad; analista de riesgo de terceros; analista de aseguramiento de seguridad; analista de programas de ciberseguridad; analista junior de seguridad; analista de preparación para auditorías.

## 18.2 Trabajo que puede realizar un analista junior

- Mantener inventarios de activos, datos, sistemas, riesgos, obligaciones, proveedores y evidencia.
- Recopilar y organizar evidencia para resultados del CSF con alcance definido.
- Revisar muestras de acceso, vulnerabilidades, formación, registros, respaldos, proveedores e incidentes.
- Documentar estado del Perfil, brechas, limitaciones, responsables y planes de acción.
- Dar seguimiento a acciones correctivas, excepciones, aceptaciones de riesgo y nuevas pruebas.
- Preparar tableros claros sin ocultar incertidumbre.
- Apoyar ejercicios, cronologías de incidentes, lecciones aprendidas y actualizaciones de planes.
- Proteger información confidencial y respetar los límites de autorización.

## 18.3 Evidencia de portafolio

| **Competencia** | **Elemento ficticio de portafolio** |
|---|---|
| Alcance | Declaración de alcance y supuestos del Perfil |
| Mapeo del Núcleo | Matriz de aplicabilidad y evidencia de todos los resultados |
| Gestión de activos | Inventario de sistemas, datos, proveedores y flujos |
| Riesgo | Registro con apetito, tolerancia, respuesta y decisión residual |
| Perfiles | Perfiles actual y objetivo con brechas priorizadas |
| Pruebas | Hojas de prueba de acceso, vulnerabilidades, respaldos, registros y proveedores |
| Respuesta a incidentes | Cronología sintética, registro de evidencia, comunicaciones y lecciones |
| Comunicación ejecutiva | Tablero de una página y declaración ejecutiva de riesgo |

# 19. Laboratorio ficticio y portafolio

Harbor Light Services es una organización ficticia. Toda persona, cuenta, dirección, activo, evento, registro de cliente y proveedor es inventado.

- **Proyecto 1 — Alcance y contexto:** misión, partes interesadas, obligaciones, servicios críticos, dependencias, exclusiones y responsables.
- **Proyecto 2 — Mapa de activos y datos:** inventarios y diagrama autorizado de flujo de datos.
- **Proyecto 3 — Riesgo:** registro de amenazas, vulnerabilidades, probabilidad, impacto, tratamiento y riesgo residual.
- **Proyecto 4 — Perfiles:** Perfil actual basado en evidencia y Perfil objetivo basado en riesgo.
- **Proyecto 5 — Controles y pruebas:** pruebas ficticias de acceso, vulnerabilidades, registros, respaldos y proveedores.
- **Proyecto 6 — Incidente:** analizar eventos sintéticos, declarar incidente, preservar evidencia, contener, erradicar, restaurar y aprender.
- **Proyecto 7 — Herramientas:** usar tres herramientas del Capítulo 16 en laboratorio aislado y registrar autorización, versión, alcance, corrección y repetición de pruebas.
- **Proyecto 8 — Informe ejecutivo:** tablero, riesgos principales, plan de acción, decisiones y limitaciones.

> **Ética del portafolio:** identificar todo como entrenamiento ficticio. Nunca publicar información real de empleadores, clientes, pacientes, empleados, proveedores, arquitecturas, vulnerabilidades, credenciales o incidentes sin autorización expresa.

# 20. Plan de aprendizaje de treinta días

| **Semana** | **Enfoque** | **Producto requerido** |
|---|---|---|
| 1 | Propósito del CSF, Núcleo, seis Funciones, contexto y activos | Memo de alcance, mapa de partes interesadas e inventario de activos y datos |
| 2 | Riesgo, Perfiles, Niveles, gobernanza y cadena de suministro | Registro de riesgos, Perfiles actual y objetivo, clasificación de proveedores |
| 3 | Salvaguardas, monitoreo, respuesta, recuperación, evidencia y pruebas | Cinco pruebas de control, archivo de incidente y evidencia de recuperación |
| 4 | Herramientas, informes, portafolio y entrevistas | Portafolio depurado, tablero y respuestas practicadas |

## 20.1 Hábito diario

Leer una sección oficial de NIST o un grupo de resultados; explicarlo en lenguaje sencillo sin alterar el significado; crear una evidencia ficticia; comprobar integridad, alcance, fecha, propiedad y confiabilidad; escribir una conclusión, acción correctiva o lección.

# 21. Preparación para entrevistas

- **¿Qué es NIST CSF 2.0?** Un marco flexible y orientado a resultados para comprender, evaluar, priorizar y comunicar el riesgo de ciberseguridad mediante el Núcleo, los Perfiles, los Niveles y recursos de apoyo.
- **¿Cuáles son las seis Funciones?** Gobernar, Identificar, Proteger, Detectar, Responder y Recuperar.
- **¿Por qué se añadió Gobernar?** Para hacer explícitas la responsabilidad de liderazgo, política, estrategia de riesgo, integración con ERM, supervisión y riesgo de cadena de suministro.
- **¿Qué es un Perfil actual?** Una descripción de los resultados que un alcance definido logra o intenta lograr actualmente, incluyendo cómo y en qué medida.
- **¿Qué es un Perfil objetivo?** Los resultados priorizados seleccionados para un estado futuro según misión, riesgo, obligaciones, partes interesadas y recursos.
- **¿Qué son los Niveles?** Contexto para el rigor de gobernanza y gestión del riesgo: Parcial, Informado por el riesgo, Repetible y Adaptativo.
- **¿El CSF certifica cumplimiento?** No. La alineación no crea cumplimiento legal ni certificación de NIST.
- **¿Cómo se verifica un resultado?** Definir alcance y criterios, evaluar diseño, obtener población completa, muestrear por riesgo, inspeccionar y repetir, registrar excepciones, corregir, volver a probar y concluir con evidencia.
- **¿Cómo deben utilizarse las herramientas?** Solo con autorización y como una fuente de evidencia; validar cobertura y resultados, proteger salidas, corregir brechas y repetir pruebas.
- **¿Cómo priorizar brechas?** Según impacto en la misión, amenaza, probabilidad, criticidad, obligaciones, exposición, dependencias, controles existentes, costo, viabilidad y apetito de riesgo.

> **Respuesta de 60 segundos para gerentes:** Uso el CSF 2.0 para conectar la ciberseguridad con el riesgo empresarial. Definimos alcance y partes interesadas, seleccionamos resultados aplicables, construimos Perfiles actual y objetivo, priorizamos brechas, financiamos planes, probamos evidencia operativa, incluimos proveedores y comunicamos decisiones y limitaciones. Las herramientas apoyan el trabajo, pero las personas siguen siendo responsables del alcance, juicio, corrección y riesgo residual.

# 22. Plantillas y listas de verificación

## 22.1 Registro de Perfil

Alcance, propósito, responsable, patrocinador, partes interesadas, fecha, activador de revisión; identificador de Función, Categoría y Subcategoría; aplicabilidad; estado actual; implementación; evidencia; prueba; excepción; limitación; estado objetivo; prioridad; brecha; riesgo; acción; protección provisional; recursos; fecha; dependencia; repetición de prueba; contexto de Nivel; aprobación e historial de versiones.

## 22.2 Registro de riesgos

Objetivo, activo, servicio, datos, proveedor y responsable; amenaza, vulnerabilidad, escenario y resultados afectados; controles y evidencia; probabilidad, impacto y riesgo inherente; respuesta, acción, recursos y fecha; riesgo residual, comparación con apetito/tolerancia y autoridad de aceptación; indicador, activador de revisión, vencimiento de excepción y repetición de prueba.

## 22.3 Hoja de prueba de control

Resultado, riesgo, control, responsable, frecuencia, sistemas, ubicaciones y periodo; criterios de diseño; evidencia esperada; población completa; comprobación de integridad; método de muestra; procedimiento; evidencia inspeccionada; repetición; excepciones; causa; impacto; acción; protección provisional; nueva prueba; conclusión; limitaciones; revisor y aprobación.

## 22.4 Revisión de proveedores

Servicio, responsable, criticidad, acceso, datos, ubicaciones, subcontratistas, dependencias y alternativas; debida diligencia, autenticidad, desarrollo seguro, vulnerabilidades, resiliencia, historial de incidentes y situación financiera/operativa; requisitos contractuales, derechos de evidencia, notificación, recuperación, devolución/destrucción y salida; monitoreo, hallazgos, excepciones, acciones, ejercicios, incidentes, cambios, renovación y terminación.

## 22.5 Lista de preparación para gerentes

Patrocinador, roles, recursos, política y estrategia aprobados; alcance, partes interesadas, obligaciones, servicios críticos, dependencias y proveedores actualizados; poblaciones reconciliadas; Perfiles respaldados y aprobados; plan financiado; evidencia probada; controles de proveedores operando; métricas vinculadas a riesgo; excepciones, aceptaciones, limitaciones y nuevas pruebas visibles.

# 23. Glosario e índice temático

**Categoría:** grupo de resultados relacionados dentro de una Función.  
**Perfil de la comunidad:** línea base publicada para necesidades compartidas de un sector, tecnología, amenaza o caso de uso.  
**Núcleo:** jerarquía de Funciones, Categorías y Subcategorías.  
**Perfil actual:** resultados que un alcance logra o intenta lograr actualmente.  
**Riesgo de ciberseguridad:** posible efecto de la incertidumbre sobre información, tecnología y objetivos organizacionales.  
**Función:** nivel más alto del CSF.  
**Ejemplo de implementación:** ilustración orientada a acciones de una posible forma de apoyar un resultado.  
**Referencia informativa:** mapeo entre un resultado y otra norma, guía, regulación o fuente.  
**Perfil Organizacional:** mecanismo para describir la postura actual y/o objetivo.  
**Riesgo residual:** riesgo que permanece después de considerar controles y respuestas.  
**Apetito de riesgo:** cantidad y tipo amplio de riesgo que una organización está dispuesta a perseguir o retener.  
**Tolerancia al riesgo:** variación aceptable respecto de objetivos específicos.  
**Subcategoría:** resultado específico dentro de una Categoría.  
**Perfil objetivo:** resultados seleccionados y priorizados que un alcance pretende alcanzar.  
**Nivel:** contexto del rigor de gobernanza y gestión del riesgo.

## 23.1 Índice temático

| **Tema** | **Capítulos** | **Tema** | **Capítulos** |
|---|---:|---|---:|
| Control de acceso | 6, 15–16, 22 | Métricas | 14, 17 |
| Inventario de activos | 5, 15, 22 | Herramientas de código abierto | 16 |
| Preparación para auditoría | 14–15, 22 | Perfiles Organizacionales | 2–3, 10 |
| Cumplimiento | 1, 15 | Proteger | 6 |
| Núcleo | 2, 4–9 | Recuperar | 9 |
| Detectar | 7 | Apetito de riesgo | 4, 12 |
| Evidencia | 14–16 | Evaluación de riesgos | 5, 12, 22 |
| Gobernar | 4, 12–13, 17 | Cadena de suministro | 4, 13, 15, 22 |
| Identificar | 5 | Niveles | 2, 11 |
| Respuesta a incidentes | 8, 15, 19 | Verificación | 14–16 |
| Analista junior | 18–21 | Gestión de vulnerabilidades | 5, 15–16 |

# 24. Referencias oficiales y estudio adicional

- NIST Cybersecurity Framework 2.0 — CSWP 29
- Sitio oficial del NIST Cybersecurity Framework
- Herramienta de referencia del CSF 2.0
- Preguntas frecuentes del CSF 2.0
- Perfiles del CSF 2.0
- Referencias informativas del CSF 2.0
- SP 1299 — Guía de recursos y visión general
- SP 1301 — Guía rápida de Perfiles Organizacionales
- SP 1302 — Guía rápida de Niveles
- SP 1303 — Guía rápida de gestión de riesgos empresariales
- SP 1300 — Guía rápida para pequeñas empresas
- NIST SP 800-53 Rev. 5
- NIST SP 800-61 Rev. 3 — Respuesta a incidentes
- NIST SP 800-218 — Secure Software Development Framework
- NIST NICE Workforce Framework

> **Recordatorio final:** el Núcleo del CSF es estable, pero los ejemplos de implementación, referencias informativas, guías, mapeos, amenazas, tecnologías y obligaciones pueden cambiar. Verificar siempre las fuentes oficiales vigentes de NIST y los requisitos específicos de la organización antes de actuar.
