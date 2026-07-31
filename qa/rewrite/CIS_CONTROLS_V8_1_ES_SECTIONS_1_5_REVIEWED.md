# 1. Fundamentos de CIS Controls v8.1

*La versión vigente, su estructura, propósito y limitaciones.*

<img src="media/image1.png" style="width:6.15in;height:3.94164in" alt="Los Controles organizan 153 Salvaguardas en un programa defensivo práctico." />

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

<img src="media/image2.png" style="width:6.15in;height:3.39605in" alt="Cada Grupo de Implementación se apoya en el anterior; IG3 contiene todas las Salvaguardas." />

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

<img src="media/image3.png" style="width:6.15in;height:2.87986in" alt="La especificación oficial avanza desde entradas de datos definidas hasta operaciones, medidas, métricas y revisión de procedimientos." />

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
