# NIST Cybersecurity Framework 2.0

## GRC práctico, implementación, evidencia y herramientas de código abierto

*Manual de trabajo para gerentes, analistas junior, estudiantes, personas en transición profesional y equipos de ciberseguridad*

**Alberto (Al) Leiva**

Primera edición • Julio de 2026

| **Contenido:** Los 106 resultados del Núcleo del CSF • Perfiles • Tiers • GRC • cadena de suministro • evidencia • pruebas de controles • herramientas de código abierto • laboratorios • preparación profesional |
|---|

# Aviso de publicación y uso

Autor: Alberto (Al) Leiva

Edición: Primera edición, julio de 2026

Propósito: Ofrecer educación gratuita y práctica para gerentes, analistas junior, estudiantes, personas en transición profesional, profesionales de riesgos y especialistas en ciberseguridad.

## Aviso educativo

Este manual proporciona información educativa general. No constituye una certificación, cumplimiento legal, una opinión de auditoría ni una garantía de seguridad. Cada organización debe adaptar el NIST CSF a su misión, riesgos, obligaciones, apetito de riesgo, recursos, tecnologías y partes interesadas. Para tomar decisiones reales, utilice fuentes oficiales vigentes y asesoramiento cualificado en materia legal, de riesgos, privacidad, seguridad física, auditoría y tecnología.

## Uso ético y autorizado

Utilice herramientas técnicas únicamente en sistemas, aplicaciones, redes, cuentas en la nube y datos que le pertenezcan o para los cuales tenga autorización específica por escrito. En actividades de formación, utilice datos ficticios, sintéticos o aprobados. La capacidad técnica no constituye autorización.

# Prefacio

*Una introducción accesible a la gestión práctica del riesgo de ciberseguridad.*

El trabajo de ciberseguridad puede parecer una colección de productos, alertas, políticas y tareas técnicas. El NIST Cybersecurity Framework ofrece un lenguaje común para conectar esas actividades. Ayuda a los líderes a explicar qué resultados son importantes, a los gerentes a establecer prioridades y a los profesionales a relacionar el trabajo diario con el riesgo organizacional.

El CSF 2.0 es deliberadamente flexible. No exige que todas las organizaciones compren la misma herramienta, implementen el mismo control o alcancen el mismo Tier. Describe resultados. Un hospital, una empresa manufacturera, una escuela, un banco, una startup, una agencia gubernamental o una organización sin fines de lucro pueden utilizar el mismo Núcleo y, al mismo tiempo, elegir prioridades e implementaciones diferentes.

Este manual adopta un enfoque centrado primero en la metodología. Una hoja de cálculo de un marco solo es útil cuando el alcance es preciso. Un tablero en verde solo es útil cuando la evidencia es confiable. El resultado de un escáner solo es útil cuando alguien lo valida, prioriza, corrige y vuelve a probar. Los gerentes siguen siendo responsables de las decisiones; los analistas mejoran esas decisiones al reunir hechos completos y comunicarlos con claridad.

# Cómo utilizar este manual

Los gerentes deberían comenzar por los capítulos 1–3 y 10–17, además de las plantillas del capítulo 22.

Los analistas junior deberían estudiar los seis capítulos dedicados a las Funciones, el método de verificación, las herramientas, el laboratorio y la preparación para entrevistas.

Los equipos técnicos deberían relacionar los hallazgos con activos, riesgos, resultados del CSF, implementación, responsables, evidencia y acciones correctivas.

Los equipos legales, de privacidad, seguridad física, tecnología operacional y negocio deberían revisar las decisiones que afecten sus responsabilidades.

| **Tabla de contenido real de Word:** La guía de capítulos incluye números de página específicos de la edición una vez finalizada la representación. El documento también contiene un campo nativo de tabla de contenido de Word. Después de editar, haga clic con el botón derecho sobre el campo, seleccione **Actualizar campo** y luego **Actualizar toda la tabla**. |
|---|

# 1. Fundamentos del NIST CSF 2.0

*Qué es el marco, qué cambió y qué no afirma.*

<img src="media/image1.png" style="width:6.15in;height:3.39605in" alt="GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND y RECOVER funcionan como un sistema conectado." />

Figura 1. Las seis Funciones del NIST CSF 2.0

## 1.1 Qué es el CSF 2.0

NIST publicó el CSF 2.0 el 26 de febrero de 2024. Está diseñado para organizaciones de cualquier tamaño, sector y nivel de sofisticación técnica. Sus resultados son neutrales respecto del país, el sector y la tecnología. Una organización puede adoptarlo voluntariamente o porque una política, un contrato, un regulador, un cliente o una norma interna así lo requieran.

## 1.2 Qué cambió respecto del CSF 1.1

- **GOVERN** se convirtió en la sexta Función, colocando el liderazgo, la política, el riesgo empresarial y la rendición de cuentas en el centro del marco.
- La ciberseguridad de la cadena de suministro recibió mayor énfasis.
- El lenguaje se amplió más allá de la infraestructura crítica para que el marco sirva claramente a todo tipo de organizaciones.
- Los Perfiles, los Tiers, los Ejemplos de Implementación, las Referencias Informativas y las Guías de Inicio Rápido forman ahora una cartera más amplia de recursos del CSF.
- Algunas numeraciones de Subcategorías contienen espacios intencionales porque ciertos contenidos del CSF 1.1 se trasladaron dentro del CSF 2.0.

## 1.3 Qué no es el CSF 2.0

- No es, por sí mismo, una ley.
- No es un catálogo único de controles ni una lista obligatoria de tecnologías.
- No proporciona una puntuación universal de aprobado o reprobado.
- NIST no certifica organizaciones, productos, consultores ni evaluadores con respecto al CSF.
- Un Tier alto no es automáticamente el objetivo adecuado para todos los alcances.
- Relacionar una práctica con un resultado del CSF no demuestra que ese resultado se haya alcanzado.

# 2. Núcleo, Perfiles, Tiers y recursos de apoyo

*Los componentes del CSF 2.0 y cómo se relacionan entre sí.*

<img src="media/image2.png" style="width:6.15in;height:2.6593in" alt="Las Funciones contienen Categorías, y las Categorías contienen Subcategorías específicas centradas en resultados." />

Figura 2. Jerarquía del Núcleo del CSF

| **Componente** | **Propósito** | **Uso práctico** |
|---|---|---|
| Núcleo | Jerarquía de seis Funciones, 22 Categorías y 106 Subcategorías | Describir los resultados de ciberseguridad deseados |
| Perfil Organizacional | Resultados actuales y/o objetivo para un alcance definido | Comparar la postura, priorizar brechas y planificar el trabajo |
| Perfil Comunitario | Línea de base compartida de resultados para un sector, tecnología, amenaza o caso de uso | Utilizarla como insumo para el Perfil Objetivo de una organización |
| Tiers | Contexto sobre el rigor de las prácticas de gobernanza y gestión de riesgos | Caracterizar las condiciones del Perfil Actual y del Perfil Objetivo |
| Ejemplos de Implementación | Acciones orientativas que pueden ayudar a alcanzar resultados | Generar ideas, adaptarlas y validarlas |
| Referencias Informativas | Correspondencias con normas, guías, regulaciones y otras fuentes | Seleccionar prácticas y controles más detallados |
| Guías de Inicio Rápido | Orientación breve y práctica sobre usos específicos del CSF | Iniciar trabajos sobre Perfiles, Tiers, ERM, cadena de suministro y pequeñas empresas |

| **Cifras importantes:** El CSF 2.0 contiene 6 Funciones, 22 Categorías y 106 Subcategorías. Las Subcategorías describen resultados; no exigen productos específicos ni implementaciones idénticas. |
|---|

# 3. Hoja de ruta práctica de implementación

*Una forma repetible de pasar del lenguaje del marco a mejoras financiadas.*

- Designe un patrocinador ejecutivo y un responsable del programa.
- Defina el alcance del Perfil: empresa, unidad de negocio, producto, servicio, sistema, región o ecosistema de proveedores.
- Reúna información sobre la misión, las partes interesadas, las obligaciones legales y contractuales, los riesgos, activos, amenazas, incidentes, auditorías, personal y proveedores.
- Seleccione los resultados del CSF aplicables y cree un Perfil Actual utilizando evidencia confiable.
- Defina un Perfil Objetivo basado en el riesgo, teniendo en cuenta los Perfiles Comunitarios y las obligaciones aplicables.
- Analice brechas, dependencias, costos, viabilidad y reducción del riesgo.
- Cree un plan de acción aprobado con responsables, recursos, hitos, métricas y medidas de protección provisionales.
- Implemente controles y procedimientos operativos.
- Pruebe la eficacia del diseño y la eficacia operativa utilizando poblaciones completas y muestras representativas.
- Informe sobre riesgos, decisiones, excepciones, avances y limitaciones.
- Actualice los Perfiles después de cambios importantes, incidentes, ejercicios, revisiones o variaciones del riesgo.

| **Comience con un alcance pequeño sin perder integridad:** Una organización pequeña puede empezar por un servicio crítico o un proceso de alto riesgo. Mantenga un alcance transparente, documente las exclusiones y amplíelo de forma deliberada. |
|---|

---

**Estado editorial:** Este bloque sustituye el contenido defectuoso equivalente y ha sido revisado para terminología, significado, estructura Markdown y uso latinoamericano. Debe integrarse en el archivo completo antes de regenerar DOCX/PDF.