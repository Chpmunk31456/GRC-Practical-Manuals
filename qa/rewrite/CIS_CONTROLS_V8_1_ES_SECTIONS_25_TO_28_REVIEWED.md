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

<img src="media/image10.png" style="width:6.15in;height:2.99481in" alt="Aprender el marco, mapear Salvaguardas, medir evidencia, reportar brechas y construir un portafolio honesto." />

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
