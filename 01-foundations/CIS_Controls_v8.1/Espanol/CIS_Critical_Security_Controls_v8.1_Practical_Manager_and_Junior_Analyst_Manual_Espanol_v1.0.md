> **Estado de revisión:** Borrador de traducción asistida por máquina. Requiere revisión humana de terminología, significado, enlaces, formato y vigencia técnica antes de marcarse como edición final.

**CYBERSECURITY, PRIVACY &amp; COMPLIANCE SERIES**

**CIS Controles de Seguridad Crítica v8.1**

** Aplicación práctica, medición, evidencia y herramientas de código abierto**

*Un manual de trabajo para administradores, analistas juniores, estudiantes, cambiadores de carrera, asesores y equipos de seguridad*

**Alberto (Al) Leiva**

Primera edición • Julio 2026

| **Inside:** 18 Controles • 153 Salvaguardias • IG1, IG2, IG3 • medición • evidencia • herramientas • manual de gestión • laboratorios • preparación de la carrera |
|... |

# Publication and Use Notice

Autor: Alberto (Al) Leiva

Edición: Primera edición, Julio 2026

Este manual educativo independiente no es un Centro para la publicación, certificación, acreditación, informe de auditoría, opinión legal o garantía de seguridad o cumplimiento. Controles CIS y CIS Los parámetros son marcas comerciales del Centro de Seguridad de Internet. Utilice los recursos oficiales CIS para el contenido exacto y la orientación actual.

Los controles CIS son las mejores prácticas de ciberseguridad. No reemplazan las leyes, reglamentos, contratos, requisitos sectoriales, evaluación de riesgos o responsabilidad de gestión aplicables. Un mapeo muestra relaciones; no prueba automáticamente el cumplimiento de otro marco.

## Uso ético y autorizado

Utilice herramientas técnicas únicamente en activos, redes, aplicaciones, cuentas de nube, repositorios y datos que posee o está específicamente autorizado por escrito para evaluar. Use información sintética y sistemas aislados en laboratorios.

# Prefacio

*Una introducción práctica para priorizar la defensa cibernética y la medición basada en evidencia.*

Los Controles CIS convierten las necesidades defensivas comunes en salvaguardias focalizadas. Su fuerza es la priorización práctica: saber lo que posee, controlar software y datos, asegurar configuraciones e identidades, gestionar vulnerabilidades y registros, prepararse para perturbaciones y ataques, y probar si las defensas funcionan.

La versión 8.1 es la edición actual. Se trata de una actualización iterativa al v8 que realineed mappings to NIST CSF 2.0, definiciones ampliadas de plazo reserva, clases de activos revisados y cartografías de Salvaguardia, problemas menores corregidos, aclarar algunas Salvaguardias, e incorporar la función de seguridad de Govern en las cartografías. Los 18 Controles y 153 Salvaguardias siguen siendo la estructura central.

Una instalación de herramientas no es la implementación. La aplicación efectiva requiere un alcance definido, poblaciones completas, configuración segura, pruebas operativas, propietarios capacitados, manejo de excepciones, medición, corrección y retesting. Los administradores deciden prioridades y recursos; los analistas hacen que esas decisiones sean fiables mediante inventarios y pruebas precisos.

Cómo utilizar este manual

- Los administradores deben comenzar con los Capítulos 1-5 y 24–25.

- Los analistas juniores deben estudiar los 18 capítulos de Control, método de medición, herramientas, laboratorio y capítulo de entrevista.

- Los equipos técnicos deben conectar cada Salvaguardia a activos, datos, propietarios, procedimientos, configuración, monitoreo, manejo de excepciones y pruebas.

- Los evaluadores deben utilizar la Evaluación oficial de Controles CIS Especificación de insumos, operaciones, medidas, métricas, suposiciones y exámenes de procedimiento.

Contenido de la palabra:** Este documento contiene un campo de mesa de contenido de Word nativo. La guía del capítulo contendrá números de página verificados para esta edición. Después de editar, haga clic con el botón derecho en el contenido y elija el campo de actualización, luego actualice la tabla completa.
|. |

# Tabla de contenidos

[Notificación de publicación y uso [2](#publication-and-use-notice)](#publication-and-use-notice)

[Uso electrónico y autorizado [2] (#ethical-and-authorized-use)](#ethical-and-authorized-use)

[Prefacio [3] (#preface)](#preface)

[Cómo utilizar este manual [4](#how-to-use-this-manual)](#how-to-use-this-manual)

[Tabla de contenidos [4](#table-of-contents)](#table-of-contents)

[1. CIS Controls v8.1 Foundations [7](#cis-controls-v8.1-foundations)](#cis-controls-v8.1-foundations)

[2. Grupos de aplicación y prioridades [8](#implementation-groups-and-prioritization)](#implementation-groups-and-prioritization)

[3. Gobernanza, alcance y propiedad [9](#governance-scope-and-ownership)](#governance-scope-and-ownership)

[4. Medición con la Evaluación de CIS Especificación [10](#measurement-with-the-cis-assessment-specification)](#measurement-with-the-cis-assessment-specification)

[5. Implementation Roadmap [11](#implementation-roadmap)](#implementation-roadmap)

[6. Control 1 - Inventario y Control de Activos Empresarios [12](#control-1-inventory-and-control-of-enterprise-assets)](#control-1-inventory-and-control-of-enterprise-assets)

[7. Control 2 — Inventario y control de activos de software [13](#control-2-inventory-and-control-of-software-assets)](#control-2-inventory-and-control-of-software-assets)

[8. Control 3 — Data Protection [14](#control-3-data-protection)](#control-3-data-protection)

[9. Control 4 — Configuración segura de activos y software de la empresa [16](#control-4-secure-configuration-of-enterprise-assets-and-software)](#control-4-secure-configuration-of-enterprise-assets-and-software)

[10. Control 5 — Account Management [18](#control-5-account-management)](#control-5-account-management)

[11. Control 6 — Access Control Management [19](#control-6-access-control-management)](#control-6-access-control-management)

[12. Control 7 - Gestión continua de la vulnerabilidad [21](#control-7-continuous-vulnerability-management)](#control-7-continuous-vulnerability-management)

[13. Control 8 — Audit Log Management [23](#control-8-audit-log-management)](#control-8-audit-log-management)

[14. Control 9 — Email and Web Browser Protections [24](#control-9-email-and-web-browser-protections)](#control-9-email-and-web-browser-protections)

[15. Control 10 — Malware Defenses [25](#control-10-malware-defenses)](#control-10-malware-defenses)

[16. Control 11 — Data Recovery [26](#control-11-data-recovery)](#control-11-data-recovery)

[17. Control 12 — Network Infrastructure Management [27](#control-12-network-infrastructure-management)](#control-12-network-infrastructure-management)

[18. Control 13 — Network Monitoring and Defense [28](#control-13-network-monitoring-and-defense)](#control-13-network-monitoring-and-defense)

[19. Control 14 — Security Awareness and Skills Training [30](#control-14-security-awareness-and-skills-training)](#control-14-security-awareness-and-skills-training)

[20. Control 15 — Service Provider Management [31](#control-15-service-provider-management)](#control-15-service-provider-management)

[21. Control 16 — Application Software Security [32](#control-16-application-software-security)](#control-16-application-software-security)

[22. Control 17 — Gestión de la respuesta de incidentes [34] (#control-17-incident-response-management)](#control-17-incident-response-management)

[23. Control 18 — Penetration Testing [36](#control-18-penetration-testing)](#control-18-penetration-testing)

[24. Open-Source Tools [37](#open-source-tools)](#open-source-tools)

[24.1 CIS Controls Navigator [37](#cis-controls-navigator)](#cis-controls-navigator)

[24.2 CIS Controls Assessment Specification [37](#cis-controls-assessment-specification)](#cis-controls-assessment-specification)

[24.3 CIS-CAT Lite [37](#cis-cat-lite)](#cis-cat-lite)

[24.4 CISO Assistant [38](#ciso-assistant)](#ciso-assistant)

[24.5 Wazuh [38](#wazuh)](#wazuh)

[24.6 osquery [38](#osquery)](#osquery)

[24.7 OpenSCAP [38](#openscap)](#openscap)

[24.8 Lynis [38](#lynis)](#lynis)

[24.9 Nmap [39](#nmap)](#nmap)

[24.10 Greenbone Community Edition [39](#greenbone-community-edition)](#greenbone-community-edition)

[24.11 Trivy [39](#trivy)](#trivy)

[24.12 OWASP ZAP [39](#owasp-zap)](#owasp-zap)

[24.13 Suricata [39](#suricata)](#suricata)

[24.14 Keycloak [39](#keycloak)](#keycloak)

[24.15 DefectDojo [40](#defectdojo)](#defectdojo)

[24.16 Velociraptor [40](#velociraptor)](#velociraptor)

[25. Manual de los Controles CIS para gerentes [41](#managers-cis-controls-playbook)](#managers-cis-controls-playbook)

[26. Guía de la carrera de analista junior [42](#junior-analyst-career-guide)](#junior-analyst-career-guide)

[26.1 Trabajo junior típico [42](#typical-junior-work)](#typical-junior-work)

[27. Laboratorio de Ficción y Cartera [44](#fictional-laboratory-and-portfolio)](#fictional-laboratory-and-portfolio)

[28. Plan de aprendizaje de 30 días [45] (#thirty-day-learning-plan)](#thirty-day-learning-plan)

[29. Preparación de entrevistas [46](#interview-preparation)](#interview-preparation)

[29.1 ¿Cuáles son los controles CIS? [46](#what-are-the-cis-controls)](#what-are-the-cis-controls)

[29.2 ¿Qué es IG1? [46](#what-is-ig1)](#what-is-ig1)

[29.3 ¿Se ajusta IG1 a cada requisito? [46](#does-ig1-fit-every-requirement)](#does-ig1-fit-every-requirement)

[29.4 ¿Cómo mide una Salvaguardia? [46](#how-do-you-measure-a-safeguard)](#how-do-you-measure-a-safeguard)

[29.5 ¿Por qué son importantes los inventarios? [46](#why-are-inventories-important)](#why-are-inventories-important)

[29.6 Vulnerability scan versus penetración test? [46](#vulnerability-scan-versus-penetration-test)](#vulnerability-scan-versus-penetration-test)

[29.7 ¿Una asignación marco demuestra el cumplimiento? [46](#does-a-framework-mapping-prove-compliance)](#does-a-framework-mapping-prove-compliance)

[29.8 ¿Qué puede concluir un analista junior? [46](#what-can-a-junior-analyst-conclude)](#what-can-a-junior-analyst-conclude)

[29.9 Preguntas para hacer al empleador [46](#questions-to-ask-the-employer)](#questions-to-ask-the-employer)

[30. Plantillas, Glosario, Índice y Referencias [48](#templates-glossary-index-and-references)](#templates-glossary-index-and-references)

[30.1 Documentos de trabajo de medición de seguridad [48](#safeguard-measurement-workpaper)](#safeguard-measurement-workpaper)

[30.2 Registro de hallazgos y nuevas pruebas [48](#finding-and-retest-record)](#finding-and-retest-record)

[30.3 Glosario [48](#glossary)](#glossary)

[30.4 Índice de asunto [49](#subject-index)](#subject-index)

[30.5 Referencias oficiales [49](#official-references)](#official-references)

# 1. Fundamentos de CIS Controls v8.1

*La versión vigente, su estructura, propósito y limitaciones.*

![Los Controles organizan 153 Salvaguardas en un programa defensivo práctico.](media/image1.png)

Figura 1. Los 18 Controles Críticos de Seguridad de CIS

- CIS Controls v8.1 se publicó en junio de 2024 y continúa siendo la edición vigente en julio de 2026.

- Los Controles son buenas prácticas priorizadas diseñadas para defender sistemas y redes frente a ataques frecuentes.

- El marco contiene 18 Controles y 153 Salvaguardas.

- Las Salvaguardas se relacionan con clases de activos, funciones de seguridad y Grupos de Implementación.

- La versión 8.1 alinea su correspondencia con NIST CSF 2.0 e incorpora la función Gobernar.

- Existen correspondencias oficiales con diversos marcos, pero la implementación debe verificarse por separado para cada requisito aplicable.

| **Capa** | **Propósito** |
|---|---|
| Control | Resultado defensivo amplio, como el inventario de activos o la respuesta a incidentes |
| Salvaguarda | Acción específica que puede asignarse, implementarse y medirse |
| Clase de activo | Tipo de elemento afectado, como dispositivos, software, datos, red, usuarios o documentación |
| Función de seguridad | Correspondencia con Gobernar, Identificar, Proteger, Detectar, Responder o Recuperar |
| Grupo de Implementación | Priorización recomendada según el perfil de riesgo y los recursos |
| Medida de evaluación | Entradas, operaciones, medidas, métricas y revisión de procedimientos utilizadas para evaluar una Salvaguarda |

# 2. Grupos de Implementación y priorización

*Cómo IG1, IG2 e IG3 ayudan a las organizaciones a elegir un punto de partida realista.*

![Cada Grupo de Implementación se apoya en el anterior; IG3 contiene todas las Salvaguardas.](media/image2.png)

Figura 2. Progresión de los Grupos de Implementación

| **Grupo** | **Salvaguardas** | **Situación habitual** | **Objetivo** |
|---|---:|---|---|
| IG1 | 56 | Recursos y experiencia de seguridad limitados, menor sensibilidad y alta necesidad de continuidad básica | Higiene cibernética esencial frente a ataques comunes |
| IG2 | IG1 + 74 | Varias áreas, mayor complejidad, información sensible y mayor dependencia operativa | Gestionar el aumento del riesgo y de la complejidad operativa |
| IG3 | IG1 + IG2 + 23 = 153 | Especialistas en seguridad, datos sensibles o regulados, servicios críticos y amenazas sofisticadas | Reducir el impacto de ataques dirigidos y avanzados |

- Según la orientación de CIS, toda organización debe comenzar con IG1.

- Seleccione un Grupo de Implementación considerando la sensibilidad de los datos, los servicios críticos, la exposición a amenazas, las obligaciones legales y contractuales, la tolerancia empresarial, la tecnología, el personal y la experiencia.

- Un Grupo de Implementación es una ayuda de priorización, no una autorización para ignorar un riesgo material o un requisito obligatorio.

- Documente las adiciones adaptadas, la secuencia, las excepciones, la aceptación del riesgo, los responsables y las fechas.

- Utilice CIS Controls Navigator para filtrar las Salvaguardas de v8.1 y revisar las correspondencias oficiales.

# 3. Gobernanza, alcance y responsabilidades

*La base de gestión necesaria para que las Salvaguardas funcionen de manera consistente.*

- Defina los objetivos empresariales, los servicios críticos, los datos sensibles, las obligaciones legales y contractuales, el perfil de amenazas, la tolerancia al riesgo y el Grupo de Implementación elegido.

- Cree inventarios completos de activos empresariales, software, datos, cuentas, sistemas de autenticación, infraestructura de red, registros, proveedores, aplicaciones y recursos de recuperación.

- Asigne una persona responsable de rendir cuentas por cada Salvaguarda y responsables operativos para cada plataforma o proceso afectado.

- Defina alcance, aplicabilidad, dependencias, responsabilidades de proveedores, excepciones permitidas, autoridad de aprobación y factores que activan una revisión.

- Planifique financiación, personal, competencias, tecnología, tiempo y gestión del cambio.

- Defina métricas e informes antes de la implementación para que la cobertura y los fallos sean visibles.

- Mantenga un ciclo de gobernanza: priorizar, implementar, medir, corregir, repetir pruebas y mejorar.

| **Rol** | **Decisión o responsabilidad** |
|---|---|
| Patrocinador ejecutivo | Dirección, tolerancia al riesgo, financiación, escalamiento y rendición de cuentas |
| Responsable del control | Diseño de la Salvaguarda, alcance, procedimiento, medición, excepciones y mejora |
| Responsable del activo o servicio | Inventario exacto, uso aprobado, configuración, impacto empresarial y remediación |
| Operaciones de seguridad | Monitoreo, alertas, investigación, respuesta y evidencia |
| TI / Ingeniería | Implementación, control de cambios, aplicación de parches, configuración y recuperación |
| GRC / Analista | Correspondencias, evidencia, medición, hallazgos, seguimiento de acciones e informes |
| Auditoría interna / evaluador | Criterios objetivos, pruebas, limitaciones y conclusiones |
| Proveedor de servicios | Controles contratados, evidencia, incidentes, cambios y apoyo para la salida |

# 4. Medición con la Especificación para la Evaluación de Controles de CIS

*Un método repetible para determinar si las Salvaguardas están implementadas.*

![La especificación oficial avanza desde entradas de datos definidas hasta operaciones, medidas, métricas y revisión de procedimientos.](media/image3.png)

Figura 3. Estructura de medición de las Salvaguardas de CIS

| **Elemento** | **Pregunta** |
|---|---|
| Metadatos de la Salvaguarda | ¿Cuál es la Salvaguarda exacta, la clase de activo, la función de seguridad y el Grupo de Implementación? |
| Dependencias | ¿Qué otras Salvaguardas o poblaciones deben existir primero? |
| Supuestos | ¿Qué condición aceptada afecta la medición? |
| Entradas | ¿Qué datos completos y fiables se requieren? |
| Operaciones | ¿Qué análisis debe realizarse sobre las entradas? |
| Medidas | ¿Qué conteos, listas, fechas, configuraciones o resultados se obtienen? |
| Métricas | ¿Cómo se calculan e interpretan las medidas? |
| Revisión del procedimiento | ¿Existe un proceso documentado y contiene los elementos requeridos? |

- Defina la Salvaguarda exacta y la población incluida en el alcance.

- Obtenga las entradas requeridas y valide su integridad, exactitud, oportunidad, responsabilidad y fiabilidad de la fuente.

- Siga las operaciones oficiales de medición o documente un método equivalente y fiable.

- Conserve los cálculos de las medidas y la población subyacente de excepciones, no solo un porcentaje.

- Evalúe si la Salvaguarda está implementada y qué tan bien funciona.

- Asigne una acción correctiva para la cobertura faltante, la configuración incorrecta, la revisión vencida, las excepciones o los datos poco fiables.

- Repita las pruebas con los mismos criterios y una población actualizada.

- Informe alcance, resultado, excepción, limitación, responsable, acción y fecha.

# 5. Hoja de ruta de implementación

*Una secuencia práctica desde los inventarios hasta una resiliencia comprobada.*

1. Elija y documente el Grupo de Implementación inicial y cualquier adición requerida.

2. Construya y concilie las poblaciones principales: activos, software, datos, cuentas, sistemas de autenticación, red, proveedores, aplicaciones y registros.

3. Implemente las Salvaguardas de IG1 con responsables, procedimientos, métricas de cobertura, excepciones y evidencia.

4. Proteja identidades, configuraciones, vulnerabilidades, correo electrónico, navegadores, defensas contra malware, copias de seguridad y monitoreo esencial.

5. Ejercite la respuesta a incidentes y la recuperación antes de una emergencia real.

6. Mida cada Salvaguarda aplicable mediante entradas fiables y operaciones repetibles.

7. Corrija la cobertura incompleta y los fallos repetidos; verifique las correcciones mediante nuevas pruebas.

8. Avance hacia IG2 o IG3 según el riesgo, las obligaciones, la madurez y la exposición a amenazas.

9. Utilice las correspondencias oficiales para coordinar otros marcos sin tratarlas como cumplimiento automático.

| **Principio de implementación:** Un grupo más pequeño de Salvaguardas totalmente definido, operado, medido y mejorado es más defendible que una lista extensa marcada como completa sin evidencia fiable. |
|---|

# 6. Control 1 - Inventario y Control de Activos Empresarios

*Las 5 Salvaguardias, significado claro, enfoque de verificación y evidencia de ejemplo*.

■img src="media/image4.png" style="width:6.15in;height:3.38991in" alt="Descubrimiento, reconciliación, respuesta y revisión mantienen a las poblaciones fundacionales actuales."

Figure 4. Asset and software inventory cycle

| ** Objetivo de control:** Fortalecer la empresa mediante la aplicación y medición de las salvaguardias para el inventario y el control de los activos institucionales. |
|... |

| **** | ** Salvaguardia** | **Significado claro** | ** Enfoque de la verificación**
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.1 | Establecer y Mantener Inventario de Activos Empresarios detallados | Poner en marcha un proceso de repetibilidad, propiedad o control técnico para establecer y mantener inventario de activos institucionales detallados, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de activos, propietarios, estado de aprobación, descubrimiento activo/pasivo, registros DHCP/IPAM, entradas de activos no autorizados |
| 1.2 | Dirección Activos no autorizados Ponga en marcha un proceso repetible, de propiedad o control técnico para abordar los activos no autorizados, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de activos, propietarios, estado de aprobación, descubrimiento activo/pasivo, registros DHCP/IPAM, entradas de activos no autorizados |
| 1.3 | Utilizar una herramienta de descubrimiento activo Ponga en marcha un proceso repetible, de propiedad o control técnico para utilizar una herramienta Active Discovery, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de activos, propietarios, estado de aprobación, descubrimiento activo/pasivo, registros DHCP/IPAM, entradas de activos no autorizados |
| 1.4 | Uso DHCP Iniciar sesión para actualizar Inventario de Activos Empresarios | Ponga en marcha un proceso repetible, propiedad o control técnico para utilizar DHCP Logging para actualizar Inventario de Activos Empresarios, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de activos, propietarios, estado de aprobación, descubrimiento activo/pasivo, registros DHCP/IPAM, entradas de activos no autorizados |
Ø 1.5 Ø Utilizar una herramienta de descubrimiento de activos pasivos Ponga en marcha un proceso repetible, de propiedad o control técnico para utilizar una herramienta Passive Asset Discovery Tool, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de activos, propietarios, estado de aprobación, descubrimiento activo/pasivo, registros DHCP/IPAM, entradas de activos no autorizados |

Utilice la guía oficial CIS Controls v8.1 y Evaluación de Controles Especificación para el lenguaje exacto de Salvaguardia, clase de activos, función de seguridad, Grupo de Implementación, dependencias, insumos, operaciones, medidas, métricas y revisión procesal.

# 7. Control 2 - Inventario y control de activos de software

*Las 7 Salvaguardias, significado claro, enfoque de verificación y evidencia de ejemplo*.

| ** Objetivo de control:** Fortalecer la empresa mediante la aplicación y medición de las salvaguardias para el inventario y el control de los activos informáticos. |
|... |

| **** | ** Salvaguardia** | **Significado claro** | ** Enfoque de la verificación**
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
TEN 2.1 | Establecer y mantener un inventario de software | Poner en marcha un proceso repetible, propiedad o control técnico para establecer y mantener un inventario de software, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de software, estado de apoyo, lista aprobada, resultados de descubrimientos, excepciones, políticas de habilitación y eventos
| 2.2 | Garantizar que el Software Autorizado está actualmente respaldado | Ponga en marcha un proceso repetible, de propiedad o control técnico para asegurar que el Software Autorizado esté actualmente respaldado, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de software, estado de apoyo, lista aprobada, resultados de descubrimientos, excepciones, políticas de habilitación y eventos
| 2.3 | Dirección Software no autorizado Ponga en marcha un proceso repetible, de propiedad o control técnico para abordar el software no autorizado, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de software, estado de apoyo, lista aprobada, resultados de descubrimientos, excepciones, políticas de habilitación y eventos
| 2.4 | Utilizar herramientas de inventario de software automatizado Ponga en marcha un proceso repetible, de propiedad o control técnico para utilizar las herramientas de inventario de software automatizadas, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de software, estado de apoyo, lista aprobada, resultados de descubrimientos, excepciones, políticas de habilitación y eventos
| 2.5 Silencioso Software autorizado Ponga en marcha un proceso repetible, de propiedad o control técnico para permitir el Software Autorizado, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de software, estado de apoyo, lista aprobada, resultados de descubrimientos, excepciones, políticas de habilitación y eventos |
| 2.6 | Allowlist Bibliotecas Autorizadas | Poner en marcha un proceso de repetibilidad, propiedad o control técnico para permitir Bibliotecas Autorizadas, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de software, estado de apoyo, lista aprobada, resultados de descubrimientos, excepciones, políticas de habilitación y eventos
| 2.7 | Autorizado Scripts Ponga en marcha un proceso repetible, de propiedad o control técnico para permitirlistas scripts autorizados, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de software, estado de apoyo, lista aprobada, resultados de descubrimientos, excepciones, políticas de habilitación y eventos

Utilice la guía oficial CIS Controls v8.1 y Evaluación de Controles Especificación para el lenguaje exacto de Salvaguardia, clase de activos, función de seguridad, Grupo de Implementación, dependencias, insumos, operaciones, medidas, métricas y revisión procesal.

8. Control 3 - Protección de datos

*Todas las 14 Salvaguardias, significado claro, enfoque de verificación y evidencia de ejemplo*.

יimg src="media/image5.png" style="width:6.15in;height:3.39605in" alt="Descubrir, clasificar, proteger, retener y disponer de datos de acuerdo a la sensibilidad y la necesidad."

Gráfico 5 Ciclo de vida de protección de datos

| ** Objetivo de control:** Fortalecer la empresa mediante la aplicación y medición de salvaguardias para la protección de datos. |
|... |

| **** | ** Salvaguardia** | **Significado claro** | ** Enfoque de la verificación**
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
TEN 3.1 | Establecer y mantener un proceso de gestión de datos | Poner en marcha un proceso repetible, propiedad o control técnico para establecer y mantener un proceso de gestión de datos, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de datos, clasificación, flujos, LCA, retención, eliminación, encriptación, DLP y registros de acceso
TEN 3.2 | Establecer y mantener un inventario de datos ANTEPóngase en marcha un proceso repetible, de propiedad o control técnico para establecer y mantener un inventario de datos, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de datos, clasificación, flujos, LCA, retención, eliminación, encriptación, DLP y registros de acceso
| 3.3 | Configurar Listas de control de acceso de datos Ponga en marcha un proceso repetible, de propiedad o control técnico para configurar listas de control de acceso de datos, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de datos, clasificación, flujos, LCA, retención, eliminación, encriptación, DLP y registros de acceso
TEN 3.4 TENCIÓN DE LOS RECURSOS DE EJECUCIÓN DE LOS Datos TENIENTES Ponga en marcha un proceso repetible, de propiedad o control técnico para hacer cumplir la Retención de Datos, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de datos, clasificación, flujos, LCA, retención, eliminación, encriptación, DLP y registros de acceso
TENCIÓN 3.5 TENIENDO EL DISPONIBLE DE LOS Datos Ponga en marcha un proceso repetible, de propiedad o control técnico para disponer de datos de forma segura, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de datos, clasificación, flujos, LCA, retención, eliminación, encriptación, DLP y registros de acceso
tención 3.6 ← Encrypt Data on End-User Devices tención Ponga en marcha un proceso repetible, de propiedad o control técnico para cifrar datos sobre dispositivos de usuario final, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de datos, clasificación, flujos, LCA, retención, eliminación, encriptación, DLP y registros de acceso
| 3.7 | Establecer y mantener un plan de clasificación de datos | Poner en marcha un proceso de repetición, propiedad o control técnico para establecer y mantener un plan de clasificación de datos, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de datos, clasificación, flujos, LCA, retención, eliminación, encriptación, DLP y registros de acceso
| 3.8 | Document Data Flows | Ponga en marcha un proceso repetible, de propiedad o control técnico para documentar los flujos de datos, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de datos, clasificación, flujos, LCA, retención, eliminación, encriptación, DLP y registros de acceso
TEN 3.9 | Datos de cifrado en medios extraíbles ANTEPonga un proceso repetible, de propiedad o control técnico en su lugar para cifrar datos en medios extraíbles, luego verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de datos, clasificación, flujos, LCA, retención, eliminación, encriptación, DLP y registros de acceso
| 3.10 | Encrypt Sensitive Data in Transit ← Ponga en marcha un proceso repetible, de propiedad o control técnico para cifrar datos sensibles en tránsito, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de datos, clasificación, flujos, LCA, retención, eliminación, encriptación, DLP y registros de acceso
| 3.11 | Encrypt Sensitive Data At Rest Ponga en marcha un proceso repetible, de propiedad o control técnico para cifrar datos sensibles en reposo, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de datos, clasificación, flujos, LCA, retención, eliminación, encriptación, DLP y registros de acceso
| 3.12 | Segment Data Processing and Storage Based on Sensitivity TEN Poner en marcha un proceso repetible, de propiedad o control técnico para segmentar el procesamiento de datos y almacenamiento basado en la sensibilidad, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de datos, clasificación, flujos, LCA, retención, eliminación, encriptación, DLP y registros de acceso
| 3.13 | Implementar una solución de prevención de la pérdida de datos Ponga en marcha un proceso repetible, de propiedad o control técnico para desplegar una solución de prevención de la pérdida de datos, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de datos, clasificación, flujos, LCA, retención, eliminación, encriptación, DLP y registros de acceso
| 3.14 | Log Sensitive Data Access Ponga en marcha un proceso repetible, de propiedad o control técnico para registrar el acceso de datos sensibles, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de datos, clasificación, flujos, LCA, retención, eliminación, encriptación, DLP y registros de acceso

Utilice la guía oficial CIS Controls v8.1 y Evaluación de Controles Especificación para el lenguaje exacto de Salvaguardia, clase de activos, función de seguridad, Grupo de Implementación, dependencias, insumos, operaciones, medidas, métricas y revisión procesal.

# 9. Control 4 — Configuración segura de activos y software empresarial

*Las 12 Salvaguardias, significado claro, enfoque de verificación y evidencia de ejemplo*.

| ** Objetivo de control:** Fortalecer la empresa mediante la aplicación y medición de las salvaguardias para la configuración segura de los activos y programas institucionales. |
|... |

| **** | ** Salvaguardia** | **Significado claro** | ** Enfoque de la verificación**
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Ø 4.1 tención Establecer y mantener un proceso de configuración segura ← Poner en marcha un proceso repetible, de propiedad o control técnico para establecer y mantener un proceso de configuración segura, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. estándares de configuración, resultados de referencia, cortafuegos, cerraduras de sesión, protocolos de administración, predeterminados, servicios y configuración móvil
Ø 4.2 tención Establecer y mantener un proceso de configuración segura para infraestructura de red ← Poner en marcha un proceso repetible, de propiedad o control técnico para establecer y mantener un proceso de configuración segura para infraestructura de red, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. estándares de configuración, resultados de referencia, cortafuegos, cerraduras de sesión, protocolos de administración, predeterminados, servicios y configuración móvil
| 4.3 | Configure Automatic Session Locking on Enterprise Assets ← Ponga en marcha un proceso repetible, de propiedad o control técnico para configurar el bloqueo automático de sesión en activos empresariales, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. estándares de configuración, resultados de referencia, cortafuegos, cerraduras de sesión, protocolos de administración, predeterminados, servicios y configuración móvil
| 4.4 ← Implementar y administrar un cortafuegos en servidores ← Poner en marcha un proceso repetible, de propiedad o control técnico para implementar y administrar un cortafuegos en servidores, luego verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. estándares de configuración, resultados de referencia, cortafuegos, cerraduras de sesión, protocolos de administración, predeterminados, servicios y configuración móvil |
| 4.5 ← Implementar y administrar un cortafuegos en dispositivos de usuario final ← Poner en marcha un proceso repetible, de propiedad o control técnico para implementar y administrar un cortafuegos en dispositivos de usuario final, luego verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. estándares de configuración, resultados de referencia, cortafuegos, cerraduras de sesión, protocolos de administración, predeterminados, servicios y configuración móvil |
| 4.6 | Gestionar de forma segura los activos y el software de la empresa ← Poner en marcha un proceso repetible, propiedad o control técnico para gestionar de forma segura los activos y software de la empresa, a continuación, verificar la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. estándares de configuración, resultados de referencia, cortafuegos, cerraduras de sesión, protocolos de administración, predeterminados, servicios y configuración móvil
| 4.7 | Manage Default Accounts on Enterprise Assets and Software tención Ponga en marcha un proceso repetible, de propiedad o control técnico para gestionar Cuentas Predeterminadas en Activos y Software Empresarial, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. estándares de configuración, resultados de referencia, cortafuegos, cerraduras de sesión, protocolos de administración, predeterminados, servicios y configuración móvil
| 4.8 | Desinstalar o desactivar servicios innecesarios en activos y software de la empresa | Ponga un proceso repetible, propiedad o control técnico en su lugar para desinstalar o desactivar servicios innecesarios en activos y software de la empresa, a continuación, verifique la cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. estándares de configuración, resultados de referencia, cortafuegos, cerraduras de sesión, protocolos de administración, predeterminados, servicios y configuración móvil
| 4.9 | Configure Trusted DNS Servers on Enterprise Assets tención Ponga en marcha un proceso repetible, de propiedad o control técnico para configurar Trusted DNS Servers on Enterprise Assets, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. estándares de configuración, resultados de referencia, cortafuegos, cerraduras de sesión, protocolos de administración, predeterminados, servicios y configuración móvil
| 4.10 Ø Enforce Automatic Device Lockout on Portable End-User Devices Ponga en marcha un proceso repetible, de propiedad o control técnico para hacer cumplir el bloqueo automático de dispositivos en dispositivos portátiles de usuario final, a continuación, verifique la cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. estándares de configuración, resultados de referencia, cortafuegos, cerraduras de sesión, protocolos de administración, predeterminados, servicios y configuración móvil |
| 4.11 | Enforce Remote Wipe Capability on Portable End-User Devices Ponga en marcha un proceso repetible, de propiedad o control técnico para hacer cumplir la Capacidad de Wipe remota en dispositivos portátiles de usuario final, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. estándares de configuración, resultados de referencia, cortafuegos, cerraduras de sesión, protocolos de administración, predeterminados, servicios y configuración móvil
| 4.12 ← Espacios de trabajo para empresas separadas en dispositivos móviles de usuario final TENIENDO un proceso repetible, de propiedad o control técnico en el lugar para separar espacios de trabajo empresariales en dispositivos móviles de usuario final, luego verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. estándares de configuración, resultados de referencia, cortafuegos, cerraduras de sesión, protocolos de administración, predeterminados, servicios y configuración móvil |

Utilice la guía oficial CIS Controls v8.1 y Evaluación de Controles Especificación para el lenguaje exacto de Salvaguardia, clase de activos, función de seguridad, Grupo de Implementación, dependencias, insumos, operaciones, medidas, métricas y revisión procesal.

Control 5 - Gestión de Cuentas

*Todas las 6 Salvaguardias, significado claro, enfoque de verificación y evidencia de ejemplo*.

| ** Objetivo de control:** Fortalecer la empresa mediante la aplicación y medición de las salvaguardias para la gestión de las cuentas. |
|. |

| **** | ** Salvaguardia** | **Significado claro** | ** Enfoque de la verificación**
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 5.1 | Establecer y mantener un inventario de cuentas | Poner en marcha un proceso repetible, propiedad o control técnico para establecer y mantener un inventario de cuentas, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. poblaciones, propietarios, fechas, política de contraseñas, acciones de cuenta inactiva, inventarios de administración y de cuenta de servicios
TEN 5.2 | Use Contraseñas Únicas ANTEPóngase en marcha un proceso repetible, de propiedad o control técnico para usar Contraseñas Únicas, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. poblaciones, propietarios, fechas, política de contraseñas, acciones de cuenta inactiva, inventarios de administración y de cuenta de servicios
| 5.3 | Cuentas de Dormant Desactivados Ponga en marcha un proceso repetible, de propiedad o control técnico para deshabilitar Cuentas Dormant, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. poblaciones, propietarios, fechas, política de contraseñas, acciones de cuenta inactiva, inventarios de administración y de cuenta de servicios
tención 5.4 Silencioso Administrador de Restricciones Privilegios a Cuentas Administradoras Dedicadas Poner en marcha un proceso repetible, de propiedad o control técnico para restringir los privilegios del Administrador a las Cuentas de Administrador Dedicado, a continuación, verificar la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. poblaciones, propietarios, fechas, política de contraseñas, acciones de cuenta inactiva, inventarios de administración y de cuenta de servicios
TEN 5.5 | Establecer y mantener un inventario de cuentas de servicio | Poner en marcha un proceso repetible, propiedad o control técnico para establecer y mantener un inventario de cuentas de servicio, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. poblaciones, propietarios, fechas, política de contraseñas, acciones de cuenta inactiva, inventarios de administración y de cuenta de servicios
| 5.6 | Centralizar Gestión de Cuentas Poner en marcha un proceso repetible, de propiedad o control técnico para centralizar la gestión de cuentas, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. poblaciones, propietarios, fechas, política de contraseñas, acciones de cuenta inactiva, inventarios de administración y de cuenta de servicios

Utilice la guía oficial CIS Controls v8.1 y Evaluación de Controles Especificación para el lenguaje exacto de Salvaguardia, clase de activos, función de seguridad, Grupo de Implementación, dependencias, insumos, operaciones, medidas, métricas y revisión procesal.

# 11. Control 6 — Access Control Management

*Las 8 Salvaguardias, significado claro, enfoque de verificación y evidencia de ejemplo*.

יimg src="media/image6.png" style="width:6.15in;height:3.03192in" alt="Las cuentas y privilegios requieren la creación aprobada, la autenticación fuerte, la revisión y la revocación oportuna".

Gráfico 6 Identidad y acceso ciclo de vida

| ** Objetivo de control:** Fortalecer la empresa mediante la aplicación y medición de las salvaguardias para la gestión del control del acceso. |
|... |

| **** | ** Salvaguardia** | **Significado claro** | ** Enfoque de la verificación**
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
TEN 6.1 TEN Establezca un proceso de concesión de acceso | Ponga en marcha un proceso repetible, de propiedad o control técnico para establecer un proceso de concesión de acceso, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. Entradas de subvención/revocación, cobertura del MFA, inventario del sistema de autenticación, funciones, derechos y exámenes de acceso
| 6.2 | Establezca un proceso de revocación de acceso | Ponga en marcha un proceso de repetición, propiedad o control técnico para establecer un proceso de revocación de acceso, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. Entradas de subvención/revocación, cobertura del MFA, inventario del sistema de autenticación, funciones, derechos y exámenes de acceso
TEN 6.3 | Require MFA for Externally-Exposed Applications TEN Ponga en marcha un proceso repetible, de propiedad o control técnico para requerir MFA para Aplicaciones Expuestas Externamente, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. Entradas de subvención/revocación, cobertura del MFA, inventario del sistema de autenticación, funciones, derechos y exámenes de acceso
| 6.4 | Requiere MFA para el acceso a redes remotas Ponga en marcha un proceso repetible, de propiedad o control técnico para requerir MFA para acceso remoto a redes, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. Entradas de subvención/revocación, cobertura del MFA, inventario del sistema de autenticación, funciones, derechos y exámenes de acceso
tención 6.5 Silencioso Consultar MFA para el acceso administrativo Poner en marcha un proceso repetible, de propiedad o control técnico para exigir el MFA de Acceso Administrativo, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. Entradas de subvención/revocación, cobertura del MFA, inventario del sistema de autenticación, funciones, derechos y exámenes de acceso
| 6.6 | Establecer y mantener un inventario de sistemas de autenticación y autorización | Poner en marcha un proceso repetible, propiedad o control técnico para establecer y mantener un inventario de sistemas de autenticación y autorización, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. Entradas de subvención/revocación, cobertura del MFA, inventario del sistema de autenticación, funciones, derechos y exámenes de acceso
| 6.7 | Centralizar control de acceso Ponga en marcha un proceso repetible, de propiedad o control técnico para centralizar el control de acceso, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. Entradas de subvención/revocación, cobertura del MFA, inventario del sistema de autenticación, funciones, derechos y exámenes de acceso
| 6.8 | Definir y mantener el control de acceso basado en roles Ponga en marcha un proceso repetible, de propiedad o control técnico para definir y mantener el control de acceso basado en roles, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. Entradas de subvención/revocación, cobertura del MFA, inventario del sistema de autenticación, funciones, derechos y exámenes de acceso

Utilice la guía oficial CIS Controls v8.1 y Evaluación de Controles Especificación para el lenguaje exacto de Salvaguardia, clase de activos, función de seguridad, Grupo de Implementación, dependencias, insumos, operaciones, medidas, métricas y revisión procesal.

Control 7 - Gestión continua de la vulnerabilidad

*Las 7 Salvaguardias, significado claro, enfoque de verificación y evidencia de ejemplo*.

■img src="media/image7.png" estilo="width:6.15in;height:3.14547in" alt="Cobertura completa y materia de remediación verificada más que producir informes de escaneo." /

Gráfico 7 Gestión continua de la vulnerabilidad

| ** Objetivo de control:** Fortalecer la empresa mediante la aplicación y medición de las salvaguardias para la gestión continua de la vulnerabilidad. |
|... |

| **** | ** Salvaguardia** | **Significado claro** | ** Enfoque de la verificación**
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 7.1 | Establecer y mantener un proceso de gestión de vulnerabilidades | Poner en marcha un proceso repetible, de propiedad o control técnico para establecer y mantener un proceso de gestión de vulnerabilidades, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. procesos, alimentaciones, cobertura de activos, escaneos autenticados, resultados de parches, excepciones, boletos de remediación y rescans
TEN 7.2 | Establecer y mantener un proceso de rehabilitación | Poner en marcha un proceso de repetición, propiedad o control técnico para establecer y mantener un proceso de rehabilitación, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. procesos, alimentaciones, cobertura de activos, escaneos autenticados, resultados de parches, excepciones, boletos de remediación y rescans
| 7.3 | Perform Automatizado Sistema Operativo Manejo de parche Ponga en marcha un proceso repetible, de propiedad o control técnico para realizar Automated Operating System Patch Management, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. procesos, alimentaciones, cobertura de activos, escaneos autenticados, resultados de parches, excepciones, boletos de remediación y rescans
| 7.4  Perform Automated Application Patch Management Ponga en marcha un proceso repetible, de propiedad o control técnico para realizar Automated Application Patch Management, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. procesos, alimentaciones, cobertura de activos, escaneos autenticados, resultados de parches, excepciones, boletos de remediación y rescans |
| 7.5 | Perform Automated Vulnerability Scans of Internal Enterprise Assets tención Ponga en marcha un proceso repetible, de propiedad o control técnico para realizar escáneres de vulnerabilidad automatizados de activos de empresa interna, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. procesos, alimentaciones, cobertura de activos, escaneos autenticados, resultados de parches, excepciones, boletos de remediación y rescans
TEN 7.6 ANTE Perform Automated Vulnerability Scans of Externally-Exposed Enterprise Assets TEN Ponga en marcha un proceso repetible, de propiedad o control técnico para realizar escáneres de vulnerabilidad automatizados de activos de empresas externamente expuestas, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. procesos, alimentaciones, cobertura de activos, escaneos autenticados, resultados de parches, excepciones, boletos de remediación y rescans
| 7.7 | Remediate Detected Vulnerabilities ← Poner en marcha un proceso repetible, de propiedad o control técnico para remediar Vulnerabilidades Detectadas, luego verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. procesos, alimentaciones, cobertura de activos, escaneos autenticados, resultados de parches, excepciones, boletos de remediación y rescans

Utilice la guía oficial CIS Controls v8.1 y Evaluación de Controles Especificación para el lenguaje exacto de Salvaguardia, clase de activos, función de seguridad, Grupo de Implementación, dependencias, insumos, operaciones, medidas, métricas y revisión procesal.

# 13. Control 8 — Audit Log Management

*Las 12 Salvaguardias, significado claro, enfoque de verificación y evidencia de ejemplo*.

| ** Objetivo de control:** Fortalecer la empresa mediante la aplicación y medición de salvaguardias para la gestión de registros de auditoría. |
|... |

| **** | ** Salvaguardia** | **Significado claro** | ** Enfoque de la verificación**
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
tención 8.1 | Establecer y mantener un proceso de gestión de los registros de auditoría ← Poner en marcha un proceso repetible, de propiedad o control técnico para establecer y mantener un proceso de gestión de los registros de auditoría, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. requisitos de registro, inventario de fuentes, almacenamiento, configuración del tiempo, registros detallados, plataforma central, revisiones y retención
| 8.2 | Recopilar los registros de auditoría Ponga en marcha un proceso repetible, de propiedad o control técnico para recopilar los registros de auditoría, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. requisitos de registro, inventario de fuentes, almacenamiento, configuración del tiempo, registros detallados, plataforma central, revisiones y retención
| 8.3 | Asegurar Adequate Audit Log Storage Ponga en marcha un proceso repetible, de propiedad o control técnico para garantizar el almacenamiento adecuado de registros de auditoría, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. requisitos de registro, inventario de fuentes, almacenamiento, configuración del tiempo, registros detallados, plataforma central, revisiones y retención
| 8.4 ← Normalizar la sincronización del tiempo ← Poner en marcha un proceso repetible, de propiedad o control técnico para estandarizar la sincronización del tiempo, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. requisitos de registro, inventario de fuentes, almacenamiento, configuración del tiempo, registros detallados, plataforma central, revisiones y retención |
| 8.5 | Recopilar Registros de Auditoría detallados | Ponga en marcha un proceso repetible, de propiedad o control técnico para recoger los registros de auditoría detallados, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. requisitos de registro, inventario de fuentes, almacenamiento, configuración del tiempo, registros detallados, plataforma central, revisiones y retención
| 8.6 | Collect DNS Query Audit Logs Ponga en marcha un proceso repetible, de propiedad o control técnico para recoger los registros de auditoría de consultas DNS, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. requisitos de registro, inventario de fuentes, almacenamiento, configuración del tiempo, registros detallados, plataforma central, revisiones y retención
| 8.7 | Collect URL Request Audit Logs ← Ponga en marcha un proceso repetible, de propiedad o control técnico para recopilar URL Solicitar registros de auditoría, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. requisitos de registro, inventario de fuentes, almacenamiento, configuración del tiempo, registros detallados, plataforma central, revisiones y retención
| 8.8 | Coleccion Command-Line Audit Logs Ponga en marcha un proceso repetible, de propiedad o control técnico para recoger los registros de auditoría de Command-Line, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. requisitos de registro, inventario de fuentes, almacenamiento, configuración del tiempo, registros detallados, plataforma central, revisiones y retención
| 8.9 | Centralizar los registros de auditoría Poner en marcha un proceso repetible, de propiedad o control técnico para centralizar los registros de auditoría, a continuación, verificar la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. requisitos de registro, inventario de fuentes, almacenamiento, configuración del tiempo, registros detallados, plataforma central, revisiones y retención
| 8.10 | Retener los registros de auditoría Poner en marcha un proceso repetible, de propiedad o control técnico para retener los registros de auditoría, verificar la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. requisitos de registro, inventario de fuentes, almacenamiento, configuración del tiempo, registros detallados, plataforma central, revisiones y retención
| 8.11 | Realizar Auditorías Reseñas Ponga en marcha un proceso repetible, de propiedad o control técnico para realizar revisiones de los registros de auditoría, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. requisitos de registro, inventario de fuentes, almacenamiento, configuración del tiempo, registros detallados, plataforma central, revisiones y retención
| 8.12 | Collect Service Provider Logs Ponga en marcha un proceso repetible, de propiedad o control técnico para recoger registros de proveedores de servicios, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. requisitos de registro, inventario de fuentes, almacenamiento, configuración del tiempo, registros detallados, plataforma central, revisiones y retención

Utilice la guía oficial CIS Controls v8.1 y Evaluación de Controles Especificación para el lenguaje exacto de Salvaguardia, clase de activos, función de seguridad, Grupo de Implementación, dependencias, insumos, operaciones, medidas, métricas y revisión procesal.

# 14. Control 9 - Protección de correo electrónico y navegador web

*Las 7 Salvaguardias, significado claro, enfoque de verificación y evidencia de ejemplo*.

| ** Objetivo de control:** Fortalecer la empresa mediante la implementación y medición de salvaguardias para las protecciones de correo electrónico y navegador web. |
Respuesta

| **** | ** Salvaguardia** | **Significado claro** | ** Enfoque de la verificación**
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
TEN 9.1 TENCIÓN Asegurar el uso de sólo navegadores completos y clientes de correo electrónico | Poner en marcha un proceso repetible, propiedad o control técnico para garantizar el uso de sólo navegadores completos y clientes de correo electrónico, a continuación, verificar la cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN navegador e inventarios de correo electrónico, estado de soporte, filtrado DNS/URL, política de extensión, DMARC y controles de apego
TEN 9.2 | Utilizar DNS Filtrar Servicios ANTEPóngase en marcha un proceso repetible, de propiedad o control técnico para utilizar DNS Filtering Services, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN navegador e inventarios de correo electrónico, estado de soporte, filtrado DNS/URL, política de extensión, DMARC y controles de apego
| 9.3 | Mantener y Forzar Filtros de URL basados en la red Ponga en marcha un proceso repetible, de propiedad o control técnico para mantener y ejecutar filtros de URL basados en red, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN navegador e inventarios de correo electrónico, estado de soporte, filtrado DNS/URL, política de extensión, DMARC y controles de apego
| 9.4 | Restringir Extensiones innecesarias o no autorizadas de navegador y correo electrónico de clientes | Ponga un proceso repetible, propiedad o control técnico en su lugar para restringir Extensiones innecesarias o no autorizadas de navegador y cliente de correo electrónico, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN navegador e inventarios de correo electrónico, estado de soporte, filtrado DNS/URL, política de extensión, DMARC y controles de apego
TEN 9.5 | Implement DMARC ANTEPonga un proceso repetible, de propiedad o control técnico en marcha para implementar DMARC, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN navegador e inventarios de correo electrónico, estado de soporte, filtrado DNS/URL, política de extensión, DMARC y controles de apego
TEN 9.6 | Bloquear Tipos de archivo innecesarios Ponga en marcha un proceso repetible, de propiedad o control técnico para bloquear los tipos de archivos innecesarios, a continuación, verifique la cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN navegador e inventarios de correo electrónico, estado de soporte, filtrado DNS/URL, política de extensión, DMARC y controles de apego
| 9.7 | Despliegue y Mantenga el Servidor de Email Anti-Malware Protecciones Ponga en marcha un proceso repetible, de propiedad o control técnico para implementar y Mantener Protecciones Anti-Malware del Servidor de Email, a continuación, verifique la cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN navegador e inventarios de correo electrónico, estado de soporte, filtrado DNS/URL, política de extensión, DMARC y controles de apego

Utilice la guía oficial CIS Controls v8.1 y Evaluación de Controles Especificación para el lenguaje exacto de Salvaguardia, clase de activos, función de seguridad, Grupo de Implementación, dependencias, insumos, operaciones, medidas, métricas y revisión procesal.

# 15. Control 10 — Malware Defenses

*Las 7 Salvaguardias, significado claro, enfoque de verificación y evidencia de ejemplo*.

| ** Objetivo de control:** Fortalecer la empresa mediante la implementación y medición de salvaguardias para defensas de malware. |
|... |

| **** | ** Salvaguardia** | **Significado claro** | ** Enfoque de la verificación**
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 10.1 | Deploy y Mantener el Software Anti-Malware Ponga en marcha un proceso repetible, de propiedad o control técnico para desplegar y mantener el software antimalware, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. cobertura de endpoint, configuración anti-malware, actualizaciones, controles de medios extraíbles, alertas de comportamiento y tickets de respuesta
| 10.2 | Configure Actualizaciones automáticas de firmas antimalware Ponga en marcha un proceso repetible, de propiedad o control técnico para configurar Actualizaciones automáticas de firmas antimalware, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. cobertura de endpoint, configuración anti-malware, actualizaciones, controles de medios extraíbles, alertas de comportamiento y tickets de respuesta
TEN 10.3 | Autorun deshabilitado y Autoplay para medios extraíbles TENIENDO Poner en marcha un proceso repetible, propiedad o control técnico para desactivar Autorun y Autoplay para medios extraíbles, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. cobertura de endpoint, configuración anti-malware, actualizaciones, controles de medios extraíbles, alertas de comportamiento y tickets de respuesta
| 10.4 | Configure Automatic Anti-Malware Scanning of Removable Media Ponga en marcha un proceso repetible, de propiedad o control técnico para configurar el escaneado automático antimalware de medios extraíbles, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. cobertura de endpoint, configuración anti-malware, actualizaciones, controles de medios extraíbles, alertas de comportamiento y tickets de respuesta
| 10.5 | Activar las características anti-Explotación Ponga en marcha un proceso repetible, de propiedad o control técnico para habilitar las funciones de antiexplotación, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. cobertura de endpoint, configuración anti-malware, actualizaciones, controles de medios extraíbles, alertas de comportamiento y tickets de respuesta
| 10.6 | Gestión Central del Software Anti-Malware Ponga en marcha un proceso repetible, de propiedad o control técnico para administrar centralmente el software antimalware, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. cobertura de endpoint, configuración anti-malware, actualizaciones, controles de medios extraíbles, alertas de comportamiento y tickets de respuesta
| 10.7 | Utilizar software antimalware basado en el comportamiento Ponga en marcha un proceso repetible, de propiedad o control técnico para utilizar el software antimalware basado en el comportamiento, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. cobertura de endpoint, configuración anti-malware, actualizaciones, controles de medios extraíbles, alertas de comportamiento y tickets de respuesta

Utilice la guía oficial CIS Controls v8.1 y Evaluación de Controles Especificación para el lenguaje exacto de Salvaguardia, clase de activos, función de seguridad, Grupo de Implementación, dependencias, insumos, operaciones, medidas, métricas y revisión procesal.

# 16. Control 11 — Data Recovery

*Las 5 Salvaguardias, significado claro, enfoque de verificación y evidencia de ejemplo*.

| ** Objetivo de control:** Fortalecer la empresa mediante la aplicación y medición de salvaguardias para la recuperación de datos. |
|... |

| **** | ** Salvaguardia** | **Significado claro** | ** Enfoque de la verificación**
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
TEN 11.1 | Establecer y mantener un proceso de recuperación de datos | Poner en marcha un proceso repetible, de propiedad o control técnico para establecer y mantener un proceso de recuperación de datos, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. Plan de recuperación, cobertura de copia de seguridad, copias protegidas y aisladas, pruebas de restauración, resultados, brechas y retests |
| 11.2 | Perform Automated Backups Ponga en marcha un proceso repetible, de propiedad o control técnico para realizar copias de seguridad automatizadas, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. Plan de recuperación, cobertura de copia de seguridad, copias protegidas y aisladas, pruebas de restauración, resultados, brechas y retests |
| 11.3 | para proteger los datos de recuperación Ponga en marcha un proceso repetible, de propiedad o control técnico para proteger los datos de recuperación, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. Plan de recuperación, cobertura de copia de seguridad, copias protegidas y aisladas, pruebas de restauración, resultados, brechas y retests |
TEN 11.4 | Establecer y mantener una instalación aislada de datos de recuperación | Poner en marcha un proceso repetible, propiedad o control técnico para establecer y mantener una instalación aislada de datos de recuperación, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. Plan de recuperación, cobertura de copia de seguridad, copias protegidas y aisladas, pruebas de restauración, resultados, brechas y retests |
TEN 11.5 | Recuperar Datos de Prueba | Poner en marcha un proceso repetible, propiedad o control técnico para probar la recuperación de datos, luego verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. Plan de recuperación, cobertura de copia de seguridad, copias protegidas y aisladas, pruebas de restauración, resultados, brechas y retests |

Utilice la guía oficial CIS Controls v8.1 y Evaluación de Controles Especificación para el lenguaje exacto de Salvaguardia, clase de activos, función de seguridad, Grupo de Implementación, dependencias, insumos, operaciones, medidas, métricas y revisión procesal.

Control 12 - Gestión de la infraestructura de red

*Las 8 Salvaguardias, significado claro, enfoque de verificación y evidencia de ejemplo*.

| ** Objetivo de control:** Fortalecer la empresa mediante la aplicación y medición de las salvaguardias para la gestión de la infraestructura de red. |
Respuesta

| **** | ** Salvaguardia** | **Significado claro** | ** Enfoque de la verificación**
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Enviado |
| 12.1 | Garantizar que la infraestructura de red esté actualizada Ponga en marcha un proceso repetible, de propiedad o control técnico para asegurar que la infraestructura de red esté actualizada, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de red, versiones, arquitectura, diagramas, vías de administración, AAA, protocolos seguros, VPN y estaciones de trabajo de administración
| 12.2 | Establecer y mantener una arquitectura de red segura ← Poner en marcha un proceso repetible, propiedad o control técnico para establecer y mantener una arquitectura de red segura, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de red, versiones, arquitectura, diagramas, vías de administración, AAA, protocolos seguros, VPN y estaciones de trabajo de administración
| 12.3 ← Gestión segura de la infraestructura de red Ponga en marcha un proceso repetible, de propiedad o control técnico para gestionar de forma segura la infraestructura de red, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de red, versiones, arquitectura, diagramas, vías de administración, AAA, protocolos seguros, VPN y estaciones de trabajo de administración |
TEN 12.4 | Establecer y mantener los diagramas de arquitectura | Poner en marcha un proceso repetible, propiedad o control técnico para establecer y mantener los diagramas de arquitectura, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de red, versiones, arquitectura, diagramas, vías de administración, AAA, protocolos seguros, VPN y estaciones de trabajo de administración
| 12.5 | Centralizar Autenticación, Autorización y Auditoría de la Red | Poner en marcha un proceso repetible, de propiedad o control técnico para centralizar la autenticación, Autorización y Auditoría de la Red, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de red, versiones, arquitectura, diagramas, vías de administración, AAA, protocolos seguros, VPN y estaciones de trabajo de administración
TEN 12.6 | Utilizar protocolos de gestión y comunicación de redes seguras Ponga en marcha un proceso repetible, de propiedad o control técnico para utilizar protocolos de gestión y comunicación de redes seguras, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de red, versiones, arquitectura, diagramas, vías de administración, AAA, protocolos seguros, VPN y estaciones de trabajo de administración
| 12.7 | Garantizar dispositivos remotos Utilice una VPN y Enterprise AAA | Ponga en marcha un proceso repetible, de propiedad o control técnico para asegurar dispositivos remotos Use una VPN y Enterprise AAA, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de red, versiones, arquitectura, diagramas, vías de administración, AAA, protocolos seguros, VPN y estaciones de trabajo de administración
| 12.8 | Mantener los recursos de computación dedicados para el trabajo administrativo Poner en marcha un proceso repetible, de propiedad o control técnico para mantener los Recursos de Computación Dedicada para el Trabajo Administrativo, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario de red, versiones, arquitectura, diagramas, vías de administración, AAA, protocolos seguros, VPN y estaciones de trabajo de administración

Utilice la guía oficial CIS Controls v8.1 y Evaluación de Controles Especificación para el lenguaje exacto de Salvaguardia, clase de activos, función de seguridad, Grupo de Implementación, dependencias, insumos, operaciones, medidas, métricas y revisión procesal.

# 18. Control 13 — Network Monitoring and Defense

*Todas las 11 Salvaguardias, significado claro, enfoque de verificación y evidencia de ejemplo*.

■img src="media/image8.png" estilo="width:6.15in;height:3.20094in" alt="Contexto centralizado, detección sintonizada, investigación humana y respuesta crean defensa útil".

Figure 8. Monitoring-to-response workflow

| ** Objetivo de control:** Fortalecer la empresa mediante la implementación y medición de salvaguardias para el monitoreo y defensa de redes. |
|... |

| **** | ** Salvaguardia** | **Significado claro** | ** Enfoque de la verificación**
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 13.1 | Centralizar Seguridad Evento Alertar | Ponga en marcha un proceso repetible, de propiedad o control técnico para centralizar la alerta de eventos de seguridad, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. cobertura SIEM, detección de host/network, segmentación, mandos remotos, registros de flujo, sistemas de prevención y alerta de afinación
| 13.2 | Despliegue una Solución de Detección de Intrusión Basada en Host Ponga en marcha un proceso repetible, de propiedad o control técnico para desplegar una Solución de Detección de Intrusión Basada en Host, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. cobertura SIEM, detección de host/network, segmentación, mandos remotos, registros de flujo, sistemas de prevención y alerta de afinación
| 13.3 | Despliegue una Solución de detección de intrusiones de red Ponga en marcha un proceso repetible, de propiedad o control técnico para implementar una Solución de Detección de Intrusión de Red, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. cobertura SIEM, detección de host/network, segmentación, mandos remotos, registros de flujo, sistemas de prevención y alerta de afinación
| 13.4 | Realizar filtración de tráfico entre Segmentos de red Ponga en marcha un proceso repetible, de propiedad o control técnico para realizar el Filtro de tráfico entre segmentos de red, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. cobertura SIEM, detección de host/network, segmentación, mandos remotos, registros de flujo, sistemas de prevención y alerta de afinación
| 13.5 | Manage Access Control for Remote Assets Ponga en marcha un proceso repetible, de propiedad o control técnico para gestionar el control de acceso para activos remotos, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. cobertura SIEM, detección de host/network, segmentación, mandos remotos, registros de flujo, sistemas de prevención y alerta de afinación
| 13.6  Collect Network Traffic Flow Logs Ponga en marcha un proceso repetible, de propiedad o control técnico para recoger los Logs de flujo de tráfico de red, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. cobertura SIEM, detección de host/network, segmentación, mandos remotos, registros de flujo, sistemas de prevención y alerta de afinación |
| 13.7 | Despliegue una solución de prevención de la intrusión basada en el hogar Ponga en marcha un proceso repetible, de propiedad o control técnico para desplegar una solución de prevención de la intrusión basada en el host, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. cobertura SIEM, detección de host/network, segmentación, mandos remotos, registros de flujo, sistemas de prevención y alerta de afinación
| 13.8 | Despliegue una Solución de Prevención de Intrusiones de Redes | Ponga en marcha un proceso repetible, de propiedad o control técnico para implementar una Solución de Prevención de Intrusiones de Red, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. cobertura SIEM, detección de host/network, segmentación, mandos remotos, registros de flujo, sistemas de prevención y alerta de afinación
| 13.9 Ponga en marcha un proceso repetible, de propiedad o control técnico para desplegar Port-Level Access Control, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. cobertura SIEM, detección de host/network, segmentación, mandos remotos, registros de flujo, sistemas de prevención y alerta de afinación |
| 13.10 | Perform Application Layer Filtering Ponga en marcha un proceso repetible, de propiedad o control técnico para realizar el Filtro de capa de aplicaciones, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. cobertura SIEM, detección de host/network, segmentación, mandos remotos, registros de flujo, sistemas de prevención y alerta de afinación
| 13.11 | Seguridad de la Tune Alerta de eventos Ubica un proceso repetible, de propiedad o control técnico en su lugar para sintonizar Security Event Alerting Thresholds, luego verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. cobertura SIEM, detección de host/network, segmentación, mandos remotos, registros de flujo, sistemas de prevención y alerta de afinación

Utilice la guía oficial CIS Controls v8.1 y Evaluación de Controles Especificación para el lenguaje exacto de Salvaguardia, clase de activos, función de seguridad, Grupo de Implementación, dependencias, insumos, operaciones, medidas, métricas y revisión procesal.

# 19. Control 14 - Capacitación en conciencia de seguridad y habilidades

*Las 9 Salvaguardias, significado claro, enfoque de verificación y evidencia de ejemplo*.

| ** Objetivo de control:** Fortalecer la empresa mediante la aplicación y medición de las salvaguardias para la sensibilización en materia de seguridad y la capacitación en aptitudes. |
|... |

| **** | ** Salvaguardia** | **Significado claro** | ** Enfoque de la verificación**
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
TEN 14.1 | Establecer y mantener un programa de conciencia de seguridad | Poner en marcha un proceso de repetición, propiedad o control técnico para establecer y mantener un programa de conciencia de seguridad, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. programa tención, población laboral, programa de trabajo, finalización, simulaciones, evaluación, excepciones y seguimiento
| 14.2 | Entrenar a los miembros de la fuerza de trabajo para reconocer ataques de ingeniería social ← Poner en marcha un proceso repetible, propiedad o control técnico para capacitar a los miembros de la fuerza de trabajo para reconocer ataques de ingeniería social, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. programa tención, población laboral, programa de trabajo, finalización, simulaciones, evaluación, excepciones y seguimiento
TEN 14.3 | Entrenar a los miembros de la fuerza de trabajo sobre la autenticación Buenas Prácticas | Poner en marcha un proceso repetible, de propiedad o control técnico para capacitar a los miembros de la fuerza de trabajo sobre las mejores prácticas de autenticación, luego verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. programa tención, población laboral, programa de trabajo, finalización, simulaciones, evaluación, excepciones y seguimiento
| 14.4 | Train Workforce on Data Handling Best Practices TEN Poner en marcha un proceso repetible, propiedad o control técnico para capacitar a Workforce en Data Handling Best Practices, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. programa tención, población laboral, programa de trabajo, finalización, simulaciones, evaluación, excepciones y seguimiento
| 14.5 | Entrenar a los miembros de la fuerza de trabajo sobre las causas de la exposición de datos no intencionales ¦ Ponga en marcha un proceso repetible, de propiedad o control técnico para capacitar a los miembros de la fuerza de trabajo sobre las causas de la exposición de datos no intencionales, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. programa tención, población laboral, programa de trabajo, finalización, simulaciones, evaluación, excepciones y seguimiento
| 14.6 | Entrenar a los miembros de la fuerza de trabajo para reconocer y denunciar incidentes de seguridad ← Poner en marcha un proceso repetible, de propiedad o control técnico para capacitar a los miembros de la fuerza de trabajo en reconocer y denunciar incidentes de seguridad, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. programa tención, población laboral, programa de trabajo, finalización, simulaciones, evaluación, excepciones y seguimiento
| 14.7 | Train Workforce para identificar e informar Actualizaciones de Seguridad Desaparecidas | Ponga en marcha un proceso repetible, de propiedad o control técnico para capacitar a Workforce para identificar y reportar actualizaciones de seguridad desaparecidas, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. programa tención, población laboral, programa de trabajo, finalización, simulaciones, evaluación, excepciones y seguimiento
TEN 14.8 | Capacitación Fuerza de Trabajo sobre Riesgos de Redes Inseguras | Poner en marcha un proceso repetible, de propiedad o control técnico para capacitar a Workforce en Riesgos de Redes Inseguras, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. programa tención, población laboral, programa de trabajo, finalización, simulaciones, evaluación, excepciones y seguimiento
TEN 14.9 | Conduct Rol-Specific Security Awareness and Skills Training TENGA un proceso repetible, de propiedad o control técnico en su lugar para llevar a cabo el entrenamiento de conciencia y habilidades de seguridad del papel-espejo, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. programa tención, población laboral, programa de trabajo, finalización, simulaciones, evaluación, excepciones y seguimiento

Utilice la guía oficial CIS Controls v8.1 y Evaluación de Controles Especificación para el lenguaje exacto de Salvaguardia, clase de activos, función de seguridad, Grupo de Implementación, dependencias, insumos, operaciones, medidas, métricas y revisión procesal.

# 20. Control 15 — Service Provider Management

*Las 7 Salvaguardias, significado claro, enfoque de verificación y evidencia de ejemplo*.

| ** Objetivo de control:** Fortalecer la empresa mediante la aplicación y medición de las salvaguardias para la gestión de proveedores de servicios. |
|... |

| **** | ** Salvaguardia** | **Significado claro** | ** Enfoque de la verificación**
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
TEN 15.1 | Establecer y mantener un inventario de proveedores de servicios | Poner en marcha un proceso repetible, propiedad o control técnico para establecer y mantener un inventario de proveedores de servicios, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario, clasificaciones, políticas, contratos, evaluaciones, vigilancia, incidentes y pruebas de descomposición
| 15.2 | Establecer y mantener una Política de Gestión de Proveedores de Servicios ← Poner en marcha un proceso repetible, propiedad o control técnico para establecer y mantener una Política de Gestión de Proveedores de Servicios, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario, clasificaciones, políticas, contratos, evaluaciones, vigilancia, incidentes y pruebas de descomposición
| 15.3 Ponga en marcha un proceso repetible, de propiedad o control técnico para clasificar a los proveedores de servicios, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario, clasificaciones, políticas, contratos, evaluaciones, vigilancia, incidentes y pruebas de descomposición |
| 15.4 | Garantizar Contratos de Proveedor de Servicios Incluir Requisitos de Seguridad | Poner en marcha un proceso de repetibilidad, propiedad o control técnico para garantizar contratos de Proveedor de Servicios Incluir Requisitos de Seguridad, luego verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario, clasificaciones, políticas, contratos, evaluaciones, vigilancia, incidentes y pruebas de descomposición
| 15.5 Silenciosos Proveedores de Servicios | Ponga en marcha un proceso repetible, de propiedad o control técnico para evaluar a los Proveedores de Servicios, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario, clasificaciones, políticas, contratos, evaluaciones, vigilancia, incidentes y pruebas de descomposición
| 15.6 Poner en marcha un proceso repetible, de propiedad o control técnico para supervisar a los proveedores de servicios, verificar la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario, clasificaciones, políticas, contratos, evaluaciones, vigilancia, incidentes y pruebas de descomposición |
| 15.7 | Proveedores de Servicio de Decomiso Seguro Ponga en marcha un proceso repetible, de propiedad o control técnico para desactivar de forma segura los proveedores de servicios, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. inventario, clasificaciones, políticas, contratos, evaluaciones, vigilancia, incidentes y pruebas de descomposición

Utilice la guía oficial CIS Controls v8.1 y Evaluación de Controles Especificación para el lenguaje exacto de Salvaguardia, clase de activos, función de seguridad, Grupo de Implementación, dependencias, insumos, operaciones, medidas, métricas y revisión procesal.

Control 16 - Seguridad del Software de Aplicación

*Todas las 14 Salvaguardias, significado claro, enfoque de verificación y evidencia de ejemplo*.

| ** Objetivo de control:** Fortalecer la empresa mediante la aplicación y medición de las salvaguardias para la seguridad de los programas de aplicación. |
|... |

| **** | ** Salvaguardia** | **Significado claro** | ** Enfoque de la verificación**
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 16.1 | Establecer y mantener un proceso de desarrollo de aplicaciones seguras ← Poner en marcha un proceso de repetición, propiedad o control técnico para establecer y mantener un proceso de desarrollo de aplicaciones seguras, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN seguro SDLC, proceso de divulgación, causa raíz, inventario de componentes, severidad, endurecimiento, entrenamiento, pruebas y modelos de amenaza |
| 16.2 | Establecer y mantener un proceso para aceptar y abordar Vulnerabilidades de Software | Poner en marcha un proceso repetible, propiedad o control técnico para establecer y mantener un proceso para aceptar y abordar vulnerabilidades de software, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN seguro SDLC, proceso de divulgación, causa raíz, inventario de componentes, severidad, endurecimiento, entrenamiento, pruebas y modelos de amenaza |
| 16.3 | Realizar análisis de causa raíz sobre vulnerabilidades de seguridad | Ponga en marcha un proceso repetible, de propiedad o control técnico para realizar análisis de causa raíz sobre vulnerabilidades de seguridad, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN seguro SDLC, proceso de divulgación, causa raíz, inventario de componentes, severidad, endurecimiento, entrenamiento, pruebas y modelos de amenaza |
| 16.4 | Establecer y administrar un inventario de componentes de software de terceros ¦Ponga un proceso repetible, propiedad o control técnico en su lugar para establecer y administrar un inventario de componentes de software de terceros, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN seguro SDLC, proceso de divulgación, causa raíz, inventario de componentes, severidad, endurecimiento, entrenamiento, pruebas y modelos de amenaza |
| 16.5 ← Utilizar componentes de software de terceros actualizados y confiados Ponga en marcha un proceso repetible, de propiedad o control técnico para utilizar componentes de software de terceros actualizados y confiados, a continuación, verifique la cobertura y las excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN seguro SDLC, proceso de divulgación, causa raíz, inventario de componentes, severidad, endurecimiento, entrenamiento, pruebas y modelos de amenaza |
| 16.6 | Establecer un sistema de puntuación de la gravedad y proceso para aplicaciones Vulnerabilidades | Poner en marcha un proceso repetible, de propiedad o control técnico para establecer un sistema de puntuación de la gravedad y el proceso para aplicaciones Vulnerabilidades, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN seguro SDLC, proceso de divulgación, causa raíz, inventario de componentes, severidad, endurecimiento, entrenamiento, pruebas y modelos de amenaza |
TEN 16.7 | Use Plantillas de endurecimiento estándar para infraestructura de aplicaciones | Ponga en marcha un proceso repetible, de propiedad o control técnico para utilizar plantillas de endurecimiento estándar para infraestructura de aplicaciones, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN seguro SDLC, proceso de divulgación, causa raíz, inventario de componentes, severidad, endurecimiento, entrenamiento, pruebas y modelos de amenaza |
| 16.8 | Sistemas de Producción Separada y No Producción Poner en marcha un proceso repetible, de propiedad o control técnico para separar los sistemas de producción y no producción, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN seguro SDLC, proceso de divulgación, causa raíz, inventario de componentes, severidad, endurecimiento, entrenamiento, pruebas y modelos de amenaza |
| 16.9 | Desarrolladores de Tren en Seguridad de Aplicaciones y Codificación Asegunda Ponga en marcha un proceso repetible, propiedad o control técnico para capacitar a Desarrolladores en Seguridad de Aplicaciones y Codificación Aseguida, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN seguro SDLC, proceso de divulgación, causa raíz, inventario de componentes, severidad, endurecimiento, entrenamiento, pruebas y modelos de amenaza |
| 16.10 | Aplicar Principios de Diseño Seguro en Arquitecturas de Aplicaciones | Ponga en marcha un proceso repetible, de propiedad o control técnico para aplicar Principios de Diseño Seguro en Arquitecturas de Aplicaciones, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN seguro SDLC, proceso de divulgación, causa raíz, inventario de componentes, severidad, endurecimiento, entrenamiento, pruebas y modelos de amenaza |
TEN 16.11 | Utilizar Módulos o Servicios Vetted para componentes de seguridad de aplicaciones TEN Poner en marcha un proceso repetible, de propiedad o control técnico para utilizar módulos o servicios para componentes de seguridad de aplicaciones, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN seguro SDLC, proceso de divulgación, causa raíz, inventario de componentes, severidad, endurecimiento, entrenamiento, pruebas y modelos de amenaza |
| 16.12 | Implementar Controles de Seguridad del Code-Level Ponga en marcha un proceso repetible, de propiedad o control técnico para implementar los controles de seguridad de Code-Level, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN seguro SDLC, proceso de divulgación, causa raíz, inventario de componentes, severidad, endurecimiento, entrenamiento, pruebas y modelos de amenaza |
| 16.13 | Conducir Aplicación Pruebas de Penetración Ponga en marcha un proceso repetible, de propiedad o control técnico para llevar a cabo pruebas de penetración de aplicaciones, a continuación, verifique cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN seguro SDLC, proceso de divulgación, causa raíz, inventario de componentes, severidad, endurecimiento, entrenamiento, pruebas y modelos de amenaza |
| 16.14 | Conduct Threat Modeling | Poner en marcha un proceso repetible, de propiedad o control técnico para llevar a cabo la Modelación de Amenazas, a continuación, verificar cobertura y excepciones. tención Confirme alcance definido, población, propiedad, implementación, frecuencia, cobertura, excepciones, corrección y retest. TEN seguro SDLC, proceso de divulgación, causa raíz, inventario de componentes, severidad, endurecimiento, entrenamiento, pruebas y modelos de amenaza |

Utilice la guía oficial CIS Controls v8.1 y Evaluación de Controles Especificación para el lenguaje exacto de Salvaguardia, clase de activos, función de seguridad, Grupo de Implementación, dependencias, insumos, operaciones, medidas, métricas y revisión procesal.

# 22. Control 17 — Gestión de la respuesta a incidentes

*Las nueve Salvaguardas, su significado en lenguaje claro, el enfoque de verificación y ejemplos de evidencia.*

![Los roles preparados, los mecanismos de reporte, la comunicación, los ejercicios y las revisiones reducen el impacto de los incidentes.](media/image9.png)

Figura 9. Preparación para la respuesta a incidentes

| **Objetivo del control:** Fortalecer la organización mediante la implementación y medición de Salvaguardas para la gestión de la respuesta a incidentes. |
|---|

| **ID** | **Salvaguarda** | **Significado en lenguaje claro** | **Enfoque de verificación** | **Ejemplos de evidencia** |
|---|---|---|---|---|
| 17.1 | Designar al personal responsable de gestionar los incidentes | Implementar un proceso repetible, con un responsable definido, para designar al personal encargado de gestionar los incidentes; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | responsables de incidentes, contactos, mecanismos de reporte, plan, roles, comunicaciones, ejercicios, revisiones y umbrales |
| 17.2 | Mantener información de contacto para reportar incidentes de seguridad | Implementar un proceso repetible, con un responsable definido, para mantener la información de contacto utilizada para reportar incidentes de seguridad; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | responsables de incidentes, contactos, mecanismos de reporte, plan, roles, comunicaciones, ejercicios, revisiones y umbrales |
| 17.3 | Mantener un proceso organizacional para reportar incidentes | Implementar un proceso repetible, con un responsable definido, para mantener un proceso organizacional de reporte de incidentes; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | responsables de incidentes, contactos, mecanismos de reporte, plan, roles, comunicaciones, ejercicios, revisiones y umbrales |
| 17.4 | Establecer y mantener un proceso de respuesta a incidentes | Implementar un proceso repetible, con un responsable definido, para establecer y mantener un proceso de respuesta a incidentes; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | responsables de incidentes, contactos, mecanismos de reporte, plan, roles, comunicaciones, ejercicios, revisiones y umbrales |
| 17.5 | Asignar roles y responsabilidades clave | Implementar un proceso repetible, con un responsable definido, para asignar roles y responsabilidades clave; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | responsables de incidentes, contactos, mecanismos de reporte, plan, roles, comunicaciones, ejercicios, revisiones y umbrales |
| 17.6 | Definir mecanismos de comunicación durante la respuesta a incidentes | Implementar un proceso repetible, con un responsable definido, para definir mecanismos de comunicación durante la respuesta a incidentes; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | responsables de incidentes, contactos, mecanismos de reporte, plan, roles, comunicaciones, ejercicios, revisiones y umbrales |
| 17.7 | Realizar ejercicios periódicos de respuesta a incidentes | Implementar un proceso repetible, con un responsable definido, para realizar ejercicios periódicos de respuesta a incidentes; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | responsables de incidentes, contactos, mecanismos de reporte, plan, roles, comunicaciones, ejercicios, revisiones y umbrales |
| 17.8 | Realizar revisiones posteriores a los incidentes | Implementar un proceso repetible, con un responsable definido, para realizar revisiones posteriores a los incidentes; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | responsables de incidentes, contactos, mecanismos de reporte, plan, roles, comunicaciones, ejercicios, revisiones y umbrales |
| 17.9 | Establecer y mantener umbrales para los incidentes de seguridad | Implementar un proceso repetible, con un responsable definido, para establecer y mantener umbrales para los incidentes de seguridad; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | responsables de incidentes, contactos, mecanismos de reporte, plan, roles, comunicaciones, ejercicios, revisiones y umbrales |

Utilice la guía oficial de CIS Controls v8.1 y la Especificación para la Evaluación de Controles para consultar el lenguaje exacto de cada Salvaguarda, la clase de activo, la función de seguridad, el Grupo de Implementación, las dependencias, las entradas, las operaciones, las medidas, las métricas y la revisión de procedimientos.

# 23. Control 18 — Pruebas de penetración

*Las cinco Salvaguardas, su significado en lenguaje claro, el enfoque de verificación y ejemplos de evidencia.*

| **Objetivo del control:** Fortalecer la organización mediante la implementación y medición de Salvaguardas para las pruebas de penetración. |
|---|

| **ID** | **Salvaguarda** | **Significado en lenguaje claro** | **Enfoque de verificación** | **Ejemplos de evidencia** |
|---|---|---|---|---|
| 18.1 | Establecer y mantener un programa de pruebas de penetración | Implementar un proceso repetible, con un responsable definido, para establecer y mantener un programa de pruebas de penetración; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | reglas de compromiso aprobadas, alcance, evaluadores cualificados, informes, remediación, repetición de pruebas y evidencia de validación |
| 18.2 | Realizar pruebas periódicas de penetración externa | Implementar un proceso repetible, con un responsable definido, para realizar pruebas periódicas de penetración externa; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | reglas de compromiso aprobadas, alcance, evaluadores cualificados, informes, remediación, repetición de pruebas y evidencia de validación |
| 18.3 | Corregir los hallazgos de las pruebas de penetración | Implementar un proceso repetible, con un responsable definido, para corregir los hallazgos de las pruebas de penetración; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | reglas de compromiso aprobadas, alcance, evaluadores cualificados, informes, remediación, repetición de pruebas y evidencia de validación |
| 18.4 | Validar las medidas de seguridad | Implementar un proceso repetible, con un responsable definido, para validar las medidas de seguridad; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | reglas de compromiso aprobadas, alcance, evaluadores cualificados, informes, remediación, repetición de pruebas y evidencia de validación |
| 18.5 | Realizar pruebas periódicas de penetración interna | Implementar un proceso repetible, con un responsable definido, para realizar pruebas periódicas de penetración interna; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | reglas de compromiso aprobadas, alcance, evaluadores cualificados, informes, remediación, repetición de pruebas y evidencia de validación |

Utilice la guía oficial de CIS Controls v8.1 y la Especificación para la Evaluación de Controles para consultar el lenguaje exacto de cada Salvaguarda, la clase de activo, la función de seguridad, el Grupo de Implementación, las dependencias, las entradas, las operaciones, las medidas, las métricas y la revisión de procedimientos.

# 24. Herramientas de código abierto

*Enlaces oficiales, inicios rápidos seguros, evidencia y limitaciones.*

| **Herramienta** | **Propósito** | **Controles posibles** |
|---|---|---|
| CIS Controls Navigator | Seleccionar Grupos de Implementación y explorar correspondencias oficiales | Todos |
| CIS Controls Assessment Specification | Orientación oficial para la medición | Todos |
| CIS-CAT Lite | Evaluación de determinados CIS Benchmarks | 4 |
| CISO Assistant | Controles, riesgos, evidencia y hallazgos | Todos |
| Wazuh | Monitoreo de endpoints, SIEM, FIM y alertas | 1, 4, 8, 10, 13, 17 |
| osquery | Consultas sobre activos, software, cuentas y configuración | 1, 2, 4, 5, 8 |
| OpenSCAP | Evaluación de configuración segura en Linux | 4, 7 |
| Lynis | Auditoría de seguridad en Linux | 4, 7 |
| Nmap | Descubrimiento autorizado de activos y servicios | 1, 12 |
| Greenbone Community Edition | Evaluación de vulnerabilidades | 7 |
| Trivy | Repositorios, imágenes, dependencias, secretos e infraestructura como código | 2, 4, 7, 16 |
| OWASP ZAP | Pruebas autorizadas de seguridad web | 16, 18 |
| Suricata | Detección de intrusiones en red y visibilidad del tráfico | 8, 13, 17 |
| Keycloak | Identidades, roles, MFA, sesiones y eventos | 5, 6, 8 |
| DefectDojo | Ingesta de hallazgos, deduplicación, remediación y repetición de pruebas | 7, 16, 18 |
| Velociraptor | Visibilidad de endpoints y respuesta a incidentes | 1, 8, 13, 17 |

| **Limitación crítica:** Una herramienta puede respaldar una o más Salvaguardas, pero no puede seleccionar por sí sola el Grupo de Implementación de una organización, definir su tolerancia al riesgo, garantizar una cobertura completa, sustituir los procedimientos y la revisión humana, autorizar pruebas de penetración ni demostrar por sí sola el cumplimiento de otro marco. |
|---|

# 25. Manual de los Controles CIS para gerentes

*Preguntas, tablero, responsabilidades y decisiones que la dirección debe controlar.*

1. ¿El Grupo de Implementación seleccionado sigue siendo apropiado para los datos sensibles, los servicios críticos, la exposición a amenazas, las obligaciones, la escala y las capacidades disponibles?

2. ¿Las poblaciones fundamentales están completas, actualizadas, tienen un responsable y se concilian con fuentes independientes de descubrimiento?

3. ¿Qué Salvaguardas de IG1 presentan cobertura incompleta, revisiones vencidas, datos de entrada poco fiables o excepciones recurrentes?

4. ¿Se escalan el acceso administrativo, los sistemas expuestos externamente, el software sin soporte, las vulnerabilidades críticas y los fallos de recuperación?

5. ¿Las alertas generan investigación y respuesta, o solo volumen en los tableros?

6. ¿Se comprenden las responsabilidades de los proveedores de servicios, la evidencia, las obligaciones ante incidentes, los subcontratistas y los planes de salida?

7. ¿Las pruebas de penetración y los ejercicios están autorizados de forma segura, tienen un alcance adecuado, se realizan con independencia cuando corresponde y se siguen hasta la repetición de pruebas?

8. ¿Qué financiación, personal, tiempo de ingeniería o decisión empresarial está bloqueando la corrección?

| **Área** | **Pregunta para la dirección** | **Estado** |
|---|---|---|
| IG y alcance | ¿Están documentadas la priorización, las adiciones, las exclusiones y las obligaciones? | Verde / Amarillo / Rojo |
| Inventarios | ¿Están completos los activos, el software, los datos, las cuentas, los proveedores, las aplicaciones y los registros? | Verde / Amarillo / Rojo |
| Protección | ¿Funcionan los controles de configuración, acceso, parches, correo electrónico, malware y datos? | Verde / Amarillo / Rojo |
| Detección | ¿La cobertura de registros y red está completa y se revisan las alertas? | Verde / Amarillo / Rojo |
| Recuperación | ¿Las copias de seguridad protegidas y las restauraciones se prueban frente a las necesidades del negocio? | Verde / Amarillo / Rojo |
| Respuesta | ¿Están actualizados los roles, contactos, umbrales, ejercicios y revisiones? | Verde / Amarillo / Rojo |
| Medición | ¿Los datos de entrada son fiables y se corrigen las poblaciones con excepciones? | Verde / Amarillo / Rojo |
| Aseguramiento | ¿Las pruebas, limitaciones, hallazgos y repeticiones de pruebas son sustentables? | Verde / Amarillo / Rojo |

# 26. Guía profesional para analistas junior

*Una ruta práctica hacia trabajos de controles, vulnerabilidades, aseguramiento, GRC y operaciones de seguridad.*

![Aprenda el marco, relacione las Salvaguardas, mida la evidencia, informe las brechas y construya un portafolio honesto.](media/image10.png)

Figura 10. Ruta para analistas junior de Controles CIS

Analista junior de controles de seguridad

Analista de GRC

Analista de gestión de vulnerabilidades

Analista de aseguramiento de seguridad

Analista de operaciones de seguridad

Analista de cumplimiento de TI

Analista de riesgos de terceros

Analista de programas de ciberseguridad

## 26.1 Trabajo típico de nivel junior

- Mantener inventarios de activos, software, datos, cuentas, sistemas de red, proveedores, aplicaciones, hallazgos y evidencia.

- Recopilar evidencia sin alterar los registros fuente y validar la integridad de las poblaciones.

- Mapear Salvaguardas con responsables, sistemas, procedimientos, configuraciones, evidencia, métricas, excepciones y acciones.

- Ejecutar herramientas autorizadas de descubrimiento, configuración, vulnerabilidades, registros o seguridad de aplicaciones conforme a procedimientos aprobados.

- Calcular métricas de cobertura y excepciones mediante la estructura oficial de evaluación.

- Dar seguimiento al software sin soporte, activos no autorizados, problemas de acceso, vulnerabilidades, copias de seguridad fallidas, brechas de alertas y hallazgos de proveedores hasta la repetición de pruebas.

- Redactar conclusiones claras sin afirmar autoridad ni certeza más allá de lo que respalda la evidencia.

| **Competencia** | **Evidencia para el portafolio** |
|---|---|
| Marco | Explicar los 18 Controles, los IG, las clases de activos y las funciones |
| Inventarios | Conciliar dos fuentes independientes y explicar las diferencias |
| Medición | Mostrar entradas, operaciones, medidas, métrica, lista de excepciones y conclusión |
| Conocimientos técnicos | Interpretar evidencia de configuración, identidad, escaneo, registros, recuperación y aplicaciones |
| Remediación | Relacionar el hallazgo con el responsable, la fecha límite, la corrección y la repetición de pruebas verificada |
| Comunicación | Redactar un resumen de una página para la dirección y un documento de trabajo detallado |
| Ética | Utilizar datos sintéticos, autorización, límites de alcance y afirmaciones honestas |

# 27. Laboratorio y portafolio ficticios

*Un entorno seguro de práctica con datos sintéticos y sistemas de laboratorio autorizados.*

| **Regla del laboratorio:** Utilice organizaciones ficticias, datos sintéticos, sistemas aislados y autorización escrita. Nunca ataque objetivos públicos, use credenciales reales ni publique resultados sensibles de herramientas. |
|---|

1. Cree una empresa ficticia de 50 personas con portátiles, servidores, servicios en la nube, una aplicación web, personal remoto y cinco proveedores.

2. Seleccione IG1 y documente tres adiciones basadas en riesgos provenientes de IG2 o IG3.

3. Cree inventarios de activos empresariales, software, datos, cuentas, sistemas de autenticación, red, proveedores, aplicaciones y fuentes de registros.

4. Utilice Nmap y osquery en un laboratorio aislado para conciliar los inventarios de activos y software.

5. Utilice OpenSCAP o Lynis en un equipo de laboratorio; documente hallazgos de configuración, excepciones, correcciones y reevaluación.

6. Utilice Greenbone en objetivos de laboratorio aprobados; valide la cobertura, los hallazgos, la remediación y el nuevo escaneo.

7. Utilice Wazuh o Suricata para generar e investigar una alerta de prueba segura.

8. Utilice Trivy o ZAP sobre un repositorio o una aplicación de capacitación y registre la corrección y la repetición de pruebas.

9. Redacte una prueba de restauración de copias de seguridad y un registro de ejercicio de mesa para incidentes.

10. Cree cinco documentos de trabajo basados en la Especificación para la Evaluación de Controles CIS, con entradas, operaciones, medidas, métricas, listas de excepciones y conclusiones.

11. Publique únicamente artefactos depurados e indique claramente que el proyecto es ficticio y no constituye una evaluación formal de CIS.

| **Artefacto** | **Qué demuestra** |
|---|---|
| Memorando de selección del IG | Priorización y razonamiento basado en riesgos |
| Conciliación de inventarios | Integridad de la población y capacidad analítica |
| Documento de trabajo de una Salvaguarda | Estructura oficial de medición y evidencia |
| Reevaluación de configuración | Hallazgo técnico, corrección y repetición de pruebas |
| Informe de vulnerabilidades | Cobertura, priorización, excepción y remediación |
| Caso de detección | Validación, investigación y respuesta ante alertas |
| Prueba de restauración | Evidencia de disponibilidad y recuperación |
| Tablero para la dirección | Comunicación clara de riesgos y acciones |

# 28. Plan de aprendizaje de treinta días

*Un cronograma concentrado para desarrollar capacidades útiles de nivel junior.*

| **Días** | **Enfoque** | **Entregable** |
|---|---|---|
| 1–4 | Marco, 18 Controles, 153 Salvaguardas, IG, clases de activos y funciones | Mapa conceptual del marco y memorando del IG |
| 5–8 | Activos, software, datos, cuentas y acceso | Cuatro inventarios conciliados |
| 9–12 | Configuración, vulnerabilidades, correo electrónico y malware | Documento de trabajo de configuración y vulnerabilidades del laboratorio |
| 13–16 | Registros, monitoreo y defensa de red | Mapa de fuentes de registros y caso de alerta segura |
| 17–19 | Recuperación y respuesta a incidentes | Prueba de restauración y registro de ejercicio de mesa |
| 20–22 | Proveedores y seguridad de aplicaciones | Evaluación de proveedor y lista de comprobación de desarrollo seguro |
| 23–25 | Especificación para la Evaluación de Controles | Cinco mediciones completas de Salvaguardas |
| 26–28 | Laboratorios autorizados con herramientas y remediación | Dos memorandos de corrección y repetición de pruebas |
| 29–30 | Portafolio y entrevistas | Portafolio depurado y cinco historias STAR |

# 29.1 ¿Cuáles son los Controles CIS?

Un conjunto priorizado de mejores prácticas defensivas organizadas en 18 Controles y 153 Salvaguardias enfocadas.

## 29.2 ¿Qué es IG1?

El punto de partida esencial de la higiene cibernética 56-Safeguard que CIS recomienda que cada empresa comience.

## 29.3 ¿Importa IG1 cada requisito?

Es una base de referencia de priorización. El riesgo material, los contratos, las leyes, los clientes o los servicios críticos pueden requerir salvaguardias adicionales.

## 29.4 ¿Cómo mide una Salvaguardia?

Utilizar criterios oficiales, dependencias, hipótesis, aportaciones completas, operaciones definidas, medidas, métricas, revisión de procedimientos, excepciones y pruebas.

## 29.5 ¿Por qué son importantes los inventarios?

Definen a las poblaciones que deben cubrir los controles de configuración, vulnerabilidad, registro, recuperación y respuesta.

## 29.6 Vulnerability scan versus penetración test?

Un escaneo identifica principalmente debilidades conocidas; la prueba de penetración utiliza el análisis humano calificado y la explotación controlada para evaluar el impacto y la resiliencia.

## 29.7 ¿Una cartografía de marco demuestra el cumplimiento?

No. Identifica las relaciones, pero la organización debe probar el requisito y la evidencia exacta aplicable.

## 29.8 ¿Qué puede concluir un analista junior?

Sólo lo que el alcance definido y el soporte de evidencia confiable, con muestreo y limitaciones claramente reveladas.

## 29.9 Preguntas para hacer al empleador

¿Qué grupo de implementación y adiciones están en alcance?

¿Cómo se crean y reconcilian las poblaciones de inventarios?

¿Qué Salvaguardias tienen la cobertura más incompleta?

¿Cómo se revisan los datos de medición y las excepciones?

¿Qué herramientas de código abierto y comerciales son aprobadas?

¿Cómo se priorizan, financian y prueban los resultados?

¿Cómo revisará el trabajo de los funcionarios superiores?

# 30. Plantillas, Glosario, Índice y Referencias

* Estructuras de trabajo reutilizables, términos importantes y puntos de partida autorizados.*

## 30.1 Documentos de trabajo de medición de salvaguardia

|** |
|. |
"La Salvaguardia de la Vida" y la IG "Antes"
"Escopia y clase de activos"
"Principal y sistemas de vida"
Las dependencias y las suposiciones de la vida
Inputs y validación de la vida
"Operaciones en la vida"
"Las medidas de la vida"
"Metric and interpretation |"
Excepciones y limitaciones de la vida
La acción, el dueño, la fecha y la prueba de la vida

## 30.2 Registro de hallazgos y nuevas pruebas

|** |
|... |
Los Criterios de la vida siguen adelante.
"Acondicionamiento y evidencia de vida"
La población afectada está en peligro.
"El riesgo y el impacto en la vida"
| Cause TENED \ \ \ \ \ \ \ \ \ \ \      \ \ \  \ \   \   \                                                                                                                                                                                                            |
"La protección provisional en la vida"
Corrección y propietario de la vida
La fecha de su muerte es la siguiente.
"El procedimiento de la prueba de mentiras"
Resultado final de la vida útil

## 30.3 Glosario

|** |
|. |
| Clase Asset | Categoría afectada por una Salvaguardia, como dispositivos, software, datos, red, usuarios o documentación. |
| CIS Benchmark ← Recomendaciones de configuración segura para una tecnología específica. |
tención CIS Control | Una de las 18 amplias áreas defensivas.
confidencialidad CIS Salvaguardia | Una acción enfocada y implementable dentro de un Control. ←
TENCIÓN TENIDA Compartir de la población aplicable en la que se implementa adecuadamente la Salvaguardia. |
| IG1 tención 56 salvaguardas esenciales de la higiene cibernética. |
| IG2 | IG1 más 74 Salvaguardias adicionales.
TENIDA IG3 TENIDA IG1 e IG2 más 23 Salvaguardias adicionales; todos 153.
TENCIÓN | Una cuenta, lista, fecha, configuración o resultado producido por operaciones de evaluación. |
| | Cálculo o interpretación construido a partir de medidas.
| Población | Completo conjunto de registros, activos, personas, sistemas o eventos aplicables.
tención Revisión de procedimiento tención Evaluación manual de si existe un proceso necesario y contiene los elementos necesarios. |
Función de seguridad permanente ← Govern, Identificar, Proteger, Detectar, Responder o Recuperar la cartografía.

## 30.4 Índice de asunto

Subjeto**
|... |
Silenciosos Cuentas
| para la seguridad de la aplicación |
Silencioso inventario de activos
Silenciosos registros de auditoría
| Protección de datos |
| Evidencia y medición | 4
Silenciosos Grupos de Aplicación
| Respuesta del incidente |
Silencioso analista junior
| | |
Silencioso Silencioso
Silencioso en la Red 17-18
| Herramientas de código abierto | 24 |
pruebas de Penetración Silencioso
Silencioso de recuperación
proveedores de servicios | 20 |
Silencioso Inventario de software
TEN TERRITORIO TERRITORIO TERRITORIO
TEN TERRITORIO DE Vulnerabilidad ANTE LAS 12

## 30.5 Referencias oficiales

[ ]](https://www.cisecurity.org/controls/v8-1 Controles v8.1

[Nota de Controles CIS](https://www.cisecurity.org/controls/cis-controls-list)

[ ]](https://www.cisecurity.org/controls/implementation-groups)

[Seguido](https://www.cisecurity.org/controls/cis-controls-assessment-specification)

[Seguido](https://cas.docs.cisecurity.org/en/latest/)

[Seguido](https://www.cisecurity.org/controls/cis-controls-navigator)

[ ]u]CIS Controles cartografías y cumplimiento efectuados/u título](https://www.cisecurity.org/cybersecurity-tools/mapping-compliance/mapping-and-compliance-with-the-cis-controls)

| **Recuerdo final:** Cambio de marcos, mapas, herramientas, productos, amenazas, leyes, contratos y riesgos organizativos. Confirme los recursos oficiales actuales y las obligaciones aplicables antes de una aplicación o evaluación reales. |
Respuesta
