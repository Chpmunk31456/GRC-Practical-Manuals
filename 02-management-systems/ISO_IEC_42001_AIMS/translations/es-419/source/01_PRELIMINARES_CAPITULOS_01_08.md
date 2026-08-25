# ISO/IEC 42001:2023

# SISTEMA DE GESTIÓN DE INTELIGENCIA ARTIFICIAL

Manual práctico para responsables del SGIA y analistas junior

| **Qué hace este manual:** Explica cómo establecer, implementar, operar, auditar, preparar para certificación y mejorar un sistema de gestión de inteligencia artificial. Desglosa las cláusulas 4–10, los nueve grupos de controles del Anexo A, la evaluación de riesgos e impactos, la Declaración de Aplicabilidad, la certificación, la evidencia, las herramientas, las decisiones de gestión y el trabajo del analista junior. |
|---|

**Alberto (Al) Leiva**

Primera edición • julio de 2026

> **Estado de localización:** Fuente localizada en español de América Latina (`es-419`). Esta parte cubre los preliminares y los capítulos 1–8 del maestro controlado en inglés. Debe utilizarse junto con las demás partes localizadas hasta que se genere el maestro consolidado y los artefactos DOCX/PDF. No constituye una traducción oficial de ISO.

# Prefacio

ISO/IEC 42001 ayuda a las organizaciones a gobernar la inteligencia artificial mediante un sistema de gestión de alcance organizacional. No certifica que cada resultado sea correcto ni que cada sistema de IA sea seguro. Exige liderazgo, contexto, planificación basada en riesgos, recursos, controles operacionales, evaluación del desempeño, acción correctiva y mejora continua en torno al desarrollo, provisión o uso responsable de sistemas de IA.

Este manual explica los conceptos con redacción original y no reproduce la norma protegida por derechos de autor. Obtenga una copia autorizada de ISO/IEC 42001:2023 y de cualquier norma que utilice para implementación o auditoría. La certificación, las leyes, los deberes sectoriales, los contratos y el riesgo técnico deben evaluarse frente al alcance y los hechos reales de la organización.

| **Nota sobre vigencia de la información:** Verificado el 14 de julio de 2026. ISO/IEC 42001:2023 continúa siendo la norma publicada de requisitos para SGIA. ISO/IEC 42005:2025 proporciona orientación para la evaluación de impacto de sistemas de IA. ISO/IEC 42006:2025 añade requisitos para los organismos que auditan y certifican SGIA. ISO 19011:2026 es la guía vigente para auditorías de sistemas de gestión. ISO/IEC 42003 e ISO/IEC 42007 continúan en desarrollo y aquí no se tratan como requisitos. |
|---|

## Cómo utilizar este manual

- Líderes y responsables del SGIA: comiencen por los capítulos 1–10, 16–20 y 29–31.
- Equipos de implementación y GRC: estudien el contenido en orden y utilicen todas las plantillas del capítulo 32.
- Equipos de IA, datos, producto, seguridad, privacidad y legal: concéntrense en los capítulos 6–15 y 20–28.
- Auditores internos: concéntrense en los capítulos 16–20 y 29, y después practiquen el laboratorio del capítulo 31.
- Analistas junior: aprendan la intención de las cláusulas, produzcan evidencia, redacten hallazgos y nunca afirmen una certificación ni autoridad de auditor que no posean.

# Tabla de contenido

El archivo fuente en Word contiene una tabla de contenido nativa y una guía permanente de capítulos con páginas. En esta edición Markdown localizada, la guía de capítulos conserva el orden del maestro controlado.

# Guía de capítulos

| **Capítulo** | **Título** | **Página de inicio en el maestro inglés** |
|---:|---|---:|
| 1 | ISO/IEC 42001 y el sistema de gestión de inteligencia artificial | 5 |
| 2 | Arquitectura del SGIA y ciclo Planificar-Hacer-Verificar-Actuar | 6 |
| 3 | Aplicabilidad, funciones organizacionales y hoja de ruta de implementación | 7 |
| 4 | Cláusula 4: Contexto de la organización | 9 |
| 5 | Cláusula 5: Liderazgo | 10 |
| 6 | Cláusula 6.1: Acciones para abordar riesgos y oportunidades | 11 |
| 7 | Cláusula 6.1.2: Evaluación de riesgos de IA | 12 |
| 8 | Cláusula 6.1.3: Tratamiento del riesgo de IA y Declaración de Aplicabilidad | 14 |
| 9 | Cláusula 6.1.4: Evaluación de impacto de sistemas de IA | 15 |
| 10 | Cláusulas 6.2 y 6.3: Objetivos y planificación de cambios | 17 |
| 11 | Cláusula 7.1: Recursos | 18 |
| 12 | Cláusulas 7.2–7.4: Competencia, toma de conciencia y comunicación | 19 |
| 13 | Cláusula 7.5: Información documentada | 20 |
| 14 | Cláusula 8.1: Planificación y control operacional | 21 |
| 15 | Cláusulas 8.2–8.4: Riesgo operacional, tratamiento y evaluación de impacto | 22 |
| 16 | Cláusula 9.1: Seguimiento, medición, análisis y evaluación | 23 |
| 17 | Cláusula 9.2: Auditoría interna | 24 |
| 18 | Cláusula 9.3: Revisión por la dirección | 26 |
| 19 | Cláusula 10: No conformidad, acción correctiva y mejora continua | 27 |
| 20 | Anexos A–D y la Declaración de Aplicabilidad | 28 |
| 21 | Anexo A.2: Políticas relacionadas con IA | 29 |
| 22 | Anexo A.3: Organización interna | 30 |
| 23 | Anexo A.4: Recursos para sistemas de IA | 31 |
| 24 | Anexo A.5 e ISO/IEC 42005: Evaluación de impacto de sistemas de IA | 32 |
| 25 | Anexo A.6: Ciclo de vida del sistema de IA | 33 |
| 26 | Anexo A.7: Datos para sistemas de IA | 34 |
| 27 | Anexo A.8: Información para partes interesadas | 36 |
| 28 | Anexos A.9 y A.10: Uso responsable, proveedores y clientes | 38 |
| 29 | Certificación, ISO/IEC 42006:2025 y preparación para auditoría | 40 |
| 30 | Herramientas de código abierto para evidencia del SGIA y aseguramiento de IA | 42 |
| 31 | Guía práctica para responsables y analistas junior, laboratorio y entrevistas | 47 |
| 32 | Plantillas, glosario, índice y referencias oficiales | 51 |

# 1. ISO/IEC 42001 y el sistema de gestión de inteligencia artificial

*ISO/IEC 42001 especifica requisitos para que una organización establezca, implemente, mantenga y mejore continuamente un sistema de gestión de inteligencia artificial.*

| **Concepto** | **Significado sencillo** | **Pregunta de evidencia** |
|---|---|---|
| SGIA | Políticas, objetivos, procesos, funciones, controles y registros interrelacionados para una IA responsable | ¿El sistema funciona en todo el alcance definido? |
| Función de la organización | Desarrollador/proveedor, implementador/usuario, proveedor, cliente o varias funciones | ¿Qué responsabilidades están bajo control? |
| Sistema de IA | Personas, datos, modelos, software, infraestructura, procesos e interfaces utilizados para producir un resultado de IA | ¿Cuál es el límite completo? |
| Conformidad | Los requisitos se cumplen dentro del alcance certificado | ¿Qué cláusula, implementación, evidencia y resultado respaldan la afirmación? |
| Certificación | Evaluación independiente de tercera parte del SGIA frente a ISO/IEC 42001 | ¿Qué entidad, alcance, norma, organismo, fechas y estado están certificados? |

## 1.1 Lo que la certificación no demuestra

- No garantiza que cada resultado de IA sea preciso, imparcial, protegido frente a amenazas, lícito, seguro para las personas o explicable.
- No certifica individualmente productos de IA salvo que el alcance del SGIA certificado y el esquema respalden explícitamente esa afirmación.
- No sustituye las pruebas de producto, el análisis legal, la evaluación de impacto, los controles de privacidad y seguridad, la validación de dominio ni la supervisión humana.
- No transfiere la rendición de cuentas de la organización al organismo de certificación ni al proveedor.

# 2. Arquitectura del SGIA y ciclo Planificar-Hacer-Verificar-Actuar

*El SGIA sigue la estructura armonizada de los sistemas de gestión y un ciclo continuo Planificar-Hacer-Verificar-Actuar (PHVA).* 

<img src="../../../assets/es-419/media/image1.png" style="width:6.15in;height:3.23274in" alt="Las cláusulas interactúan de forma continua; la norma no es una lista lineal que se completa una sola vez." />

Figura 1. Ciclo PHVA del SGIA

> **Explicación accesible:** La figura muestra que el SGIA opera como un ciclo. La organización planifica el contexto, los riesgos, los impactos y los objetivos; ejecuta controles y procesos; verifica el desempeño mediante medición, auditoría interna y revisión por la dirección; y actúa sobre no conformidades y oportunidades de mejora antes de reiniciar el ciclo.

| **Etapa PHVA** | **Trabajo de ISO/IEC 42001** | **Resultado típico** |
|---|---|---|
| Planificar | Contexto, liderazgo, riesgo/oportunidad, evaluación, tratamiento, objetivos y recursos | Alcance, política, métodos, registro de riesgos, proceso de impacto, Declaración de Aplicabilidad y objetivos |
| Hacer | Competencia, comunicación, documentación, controles operacionales y evaluaciones | Procedimientos, registros del sistema, aprobaciones y evidencia de proveedores y ciclo de vida |
| Verificar | Seguimiento, medición, análisis, auditoría interna y revisión por la dirección | Métricas, evaluación, informe de auditoría y decisiones de revisión |
| Actuar | No conformidad, corrección, causa raíz, acción correctiva y mejora | Registros de acciones, pruebas de eficacia y actualización de riesgos, controles y objetivos |

## 2.1 Integración con sistemas existentes

- Reutilice los procesos de gobierno, control documental, riesgo, auditoría, acción correctiva, proveedores, seguridad, privacidad, calidad y continuidad cuando su alcance y controles sean adecuados para el riesgo de IA.
- Cree adiciones específicas de IA para evaluación de impacto, ciclo de vida de modelos y datos, uso responsable, transparencia, supervisión humana y responsabilidades de la cadena de valor.
- Mantenga una sola fuente de verdad y mapéela a ISO 27001, ISO 9001, privacidad, obligaciones legales, NIST AI RMF y deberes sectoriales en vez de duplicar registros.

# 3. Aplicabilidad, funciones organizacionales y hoja de ruta de implementación

*Una implementación útil comienza con control organizacional, un inventario de IA exacto, funciones responsables y una hoja de ruta por etapas.*

<img src="../../../assets/es-419/media/image2.png" style="width:6.15in;height:3.23274in" alt="El alcance debe describir con honestidad los límites organizacionales, las funciones de IA, los sistemas, los datos, los proveedores y las exclusiones." />

Figura 2. Cadena para construir el alcance

> **Explicación accesible:** La figura representa la construcción del alcance desde la organización y sus funciones de IA hasta los sistemas, datos, proveedores, interfaces y exclusiones. Cada límite debe tener una justificación que no evite requisitos aplicables.

| **Función** | **Responsabilidad principal** |
|---|---|
| Órgano de gobierno / ejecutivos | Supervisión, dirección, recursos, apetito de riesgo y decisiones materiales |
| Líder del SGIA | Coordinar el sistema de gestión, desempeño, auditorías y mejora |
| Propietario de negocio/sistema de IA | Propósito, resultado, proceso afectado, riesgo, aprobación y seguimiento |
| Modelo/datos/producto/ingeniería | Requisitos, diseño, datos, evaluación, despliegue y cambio |
| Seguridad/privacidad/legal/cumplimiento/seguridad funcional | Requisitos especializados, revisión, cuestionamiento e incidentes |
| Compras/gestor de proveedores | Debida diligencia, asignación de responsabilidades, contratos, evidencia, seguimiento y salida |
| Auditoría interna | Evaluación independiente y objetiva sin ser propietaria de los controles |

## 3.1 Hoja de ruta de implementación

- Autorice el programa y obtenga las normas; defina propósito, patrocinador, recursos y gobierno.
- Inventaríe sistemas de IA y funciones; realice análisis de contexto y partes interesadas; redacte el alcance y la política.
- Defina procesos de riesgo, impacto, tratamiento, Declaración de Aplicabilidad, objetivos, documentos, competencia, comunicación y operación.
- Implemente los controles del Anexo A y controles adicionales según el riesgo; recopile evidencia durante la operación real.
- Mida el desempeño; complete la auditoría interna y la revisión por la dirección; corrija no conformidades y verifique la eficacia.
- Seleccione un organismo de certificación competente; complete Etapa 1 y Etapa 2; mantenga vigilancia y mejora.

# 4. Cláusula 4: Contexto de la organización

*La cláusula 4 establece por qué existe el SGIA, quién importa, qué cubre y cómo interactúan sus procesos.*

## 4.1 Cuestiones internas y externas

- Estrategia, cultura, gobierno, apetito de riesgo, recursos, competencia, madurez de datos, arquitectura tecnológica, sistemas de gestión existentes y cambio organizacional.
- Leyes, regulación, expectativas sectoriales, contratos, requisitos de clientes, normas, confianza pública, preocupaciones sociales, mercados, proveedores, amenazas, cambios tecnológicos o de modelos y cuestiones climáticas cuando sean pertinentes para los resultados previstos del SGIA.
- Registre por qué cada cuestión es relevante, su responsable, el efecto sobre el SGIA, la respuesta y el disparador de revisión.

## 4.2 Partes interesadas y requisitos

- Identifique a las personas y grupos afectados por la IA, aunque no sean usuarios ni clientes directos.
- Incluya, según corresponda, reguladores, clientes, trabajadores, usuarios, titulares de datos, proveedores, socios, comunidades, accionistas, auditores, aseguradoras y público.
- Separe necesidades y expectativas de las obligaciones de cumplimiento vinculantes; registre autoridad/fuente, sistema/proceso, responsable, evidencia y seguimiento de cambios.
- Determine qué requisitos abordará la organización mediante el SGIA.

## 4.3 Declaración de alcance

| **Elemento del alcance** | **Claridad requerida** |
|---|---|
| Organización | Entidades legales, unidades de negocio, ubicaciones y funciones |
| Función de IA | Desarrollador/proveedor, implementador/usuario, servicio/proveedor o combinación |
| Productos/servicios/procesos | Ofertas habilitadas por IA y usos internos |
| Tecnología y datos | Sistemas, modelos, entornos, interfaces y conjuntos de datos clave |
| Límites/dependencias | Servicios compartidos, proveedores, clientes y exclusiones |
| Justificación | Por qué los límites son válidos y no eluden requisitos aplicables |

## 4.4 Procesos del SGIA

- Defina propósito del proceso, entradas, salidas, secuencia, interacción, propietario, criterios, controles, recursos, registros, medidas, riesgos y mejora.
- Un mapa de procesos debe conectar inventario, riesgo, impacto, tratamiento, objetivos, ciclo de vida, datos, proveedores, uso, seguimiento, incidentes, auditoría, revisión y acción correctiva.

# 5. Cláusula 5: Liderazgo

*La alta dirección debe asumir la responsabilidad del SGIA, la política, la integración, los recursos, la comunicación, el desempeño y las funciones responsables.*

## 5.1 Demostración de liderazgo

- Haga que los objetivos del SGIA sean compatibles con la estrategia y los compromisos de IA responsable.
- Integre los requisitos del SGIA en procesos de negocio, producto, compras, datos, tecnología, personas, riesgo y cambio.
- Proporcione personas competentes, tiempo, herramientas, datos, infraestructura, presupuesto, cuestionamiento independiente y autoridad.
- Comunique que la gestión eficaz de IA y la conformidad son importantes, incluso cuando la presión de entrega entre en conflicto con los controles.
- Revise el desempeño y apoye a las personas que contribuyen a la mejora o plantean preocupaciones.
- Asegure que se logren los resultados previstos en lugar de tratar la certificación como el único resultado.

## 5.2 Política de IA

- Declare propósito, principios, compromisos con requisitos aplicables, IA responsable basada en riesgos, objetivos y mejora continua.
- Adapte la política a las funciones de IA, contexto, cultura, impacto, ley, productos y apetito de riesgo de la organización.
- Alinee seguridad, privacidad, calidad, datos, ética, RR. HH., compras, producto, registros, seguridad funcional e incidentes.
- Apruebe al nivel adecuado, comunique a las personas pertinentes, póngala a disposición según corresponda y revísela a intervalos planificados y después de cambios materiales.

## 5.3 Funciones, responsabilidades y autoridades

- Defina la responsabilidad por el SGIA y por informar su desempeño a la alta dirección.
- Asigne propietarios para cada sistema de IA, riesgo, impacto, fuente de datos, modelo, proveedor, control, métrica, incidente, cambio y acción correctiva.
- Defina autoridad de aprobación y escalamiento; evite conflictos donde el mismo equipo crea, valida, acepta y audita riesgos de alto impacto sin cuestionamiento suficiente.

# 6. Cláusula 6.1: Acciones para abordar riesgos y oportunidades

*La planificación convierte el contexto en riesgos, oportunidades, controles, objetivos y cambios gestionados.*

## 6.1 Entradas de planificación

- Contexto y requisitos de partes interesadas; alcance y procesos del SGIA.
- Inventario de IA, funciones del sistema, etapa del ciclo de vida, personas afectadas, datos, modelos, proveedores, integraciones y condiciones de uso.
- Beneficios y oportunidades estratégicas, junto con amenazas, fallas, daños, incertidumbre y uso indebido razonablemente previsible.
- Obligaciones legales, regulatorias, contractuales, de seguridad, privacidad, seguridad funcional, calidad, registros, accesibilidad, empleo, propiedad intelectual, consumo y sectoriales aplicables.

## 6.1.1 Acciones sobre riesgos y oportunidades

- Planifique acciones proporcionales al efecto sobre los resultados del SGIA; intégrelas en los procesos en lugar de mantener únicamente un registro separado.
- Defina acción, propietario, recurso, fecha, medida, evidencia, dependencia, decisión residual y evaluación de eficacia.
- Las oportunidades pueden incluir mejor supervisión, calidad de datos, transparencia, evaluación, competencia, eficiencia, confianza de partes interesadas e innovación.
- Evite que los controles previstos creen nuevos riesgos, como vigilancia excesiva, avisos inaccesibles o sobrecarga de revisión.

# 7. Cláusula 6.1.2: Evaluación de riesgos de IA

*El proceso de evaluación de riesgos de IA debe utilizar criterios definidos y repetibles para identificar, analizar, evaluar y priorizar riesgos.*

<img src="../../../assets/es-419/media/image3.png" style="width:6.15in;height:3.23274in" alt="Registre evidencia e incertidumbre para que distintos evaluadores puedan llegar a conclusiones comparables." />

Figura 3. Flujo de evaluación de riesgos de IA

> **Explicación accesible:** La evaluación parte de un escenario de riesgo definido, analiza contexto, probabilidad, consecuencias, incertidumbre y controles existentes, compara el resultado con criterios establecidos, selecciona tratamiento y conserva evidencia para una decisión residual autorizada y una futura reevaluación.

## 7.1 Método de riesgo

- Defina alcance, unidad de análisis, categorías de riesgo, dimensiones de impacto, probabilidad, gravedad, escala, duración, reversibilidad, grupos afectados, incertidumbre, agregación, tolerancia y autoridad de decisión.
- Identifique escenarios de riesgo sobre uso previsto, uso indebido previsible, falla, ataque, datos, modelo, comportamiento humano, proveedores, entorno, ley y efecto social.
- Analice el riesgo inherente y los controles existentes con evidencia; distinga riesgo actual, objetivo y residual.
- Evalúe frente a criterios; priorice el tratamiento según las consecuencias para personas y negocio, no mediante una sola puntuación técnica.
- Asegure resultados coherentes, válidos y comparables y conserve la evaluación como información documentada.
- Reevalúe a intervalos planificados y después de cambios materiales, incidentes, nuevos grupos afectados, actualizaciones de modelos/proveedores, deriva, cambios legales o fallas de control.

| **Registro de riesgo** | **Detalle mínimo** |
|---|---|
| Escenario | Causa/actor, condición vulnerable, evento/acción, comportamiento del sistema, parte afectada y consecuencia |
| Contexto | Uso, personas, geografía, escala, datos, modelo/versión, herramientas, proveedor y supuestos |
| Análisis | Probabilidad, dimensiones de impacto, incertidumbre, evidencia y eficacia de controles existentes |
| Tratamiento | Evitar/reducir/compartir/aceptar, controles, propietario, fecha, medida y riesgo residual |
| Decisión | Aprobador autorizado, justificación, condiciones, vencimiento, seguimiento y disparador de revisión |

# 8. Cláusula 6.1.3: Tratamiento del riesgo de IA y Declaración de Aplicabilidad

*El tratamiento del riesgo selecciona controles, los compara con el Anexo A, produce la Declaración de Aplicabilidad y obtiene aprobación del riesgo residual.*

## 8.1 Proceso de tratamiento

- Elija opciones de tratamiento: evitar, cambiar/reducir, compartir/transferir, aceptar dentro de la autoridad o realizar un piloto estrictamente limitado para reducir incertidumbre.
- Determine los controles necesarios a partir de requisitos legales y contractuales, resultados de riesgo e impacto de IA, arquitectura, partes interesadas y objetivos.
- Compare los controles seleccionados con el Anexo A para verificar que no se haya omitido ningún control de referencia pertinente.
- Añada controles más allá del Anexo A cuando sean necesarios para seguridad, privacidad, seguridad funcional, calidad, evaluación técnica, accesibilidad, resiliencia u obligaciones sectoriales.
- Cree y apruebe un plan de tratamiento y obtenga autorización para el riesgo residual.
- Conserve los resultados y cambios del tratamiento como información documentada controlada.

## 8.2 Campos de la Declaración de Aplicabilidad

| **Campo** | **Propósito** |
|---|---|
| Referencia/título del control | Identidad del control del Anexo A o adicional |
| ¿Aplicable? | Incluido o excluido para el alcance definido del SGIA |
| Justificación | Riesgo, obligación, objetivo, arquitectura o razón de exclusión |
| Implementación | Política/proceso/sistema y propietario responsable |
| Estado | Implementado, parcial, planificado o no aplicable |
| Evidencia/prueba | Evidencia actual y resultado de eficacia operacional |
| Dependencias/brechas | Controles compartidos de proveedor/cliente y hallazgos |
| Revisión | Última/próxima revisión y disparadores de cambio |

| **Advertencia sobre la Declaración de Aplicabilidad:** No es una lista de verificación copiada. Debe concordar con el alcance vigente, las evaluaciones de riesgo e impacto, el plan de tratamiento, la implementación real, la evidencia y las decisiones de riesgo. |
|---|
