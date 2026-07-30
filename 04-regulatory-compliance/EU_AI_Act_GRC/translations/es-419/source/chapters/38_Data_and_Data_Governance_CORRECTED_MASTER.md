# Capítulo 38 — Gobernanza de los datos

> **Estatus legal:** Corregido Maestro Inglés para la consolidación. Este archivo controla el lenguaje de borrador anterior del Capítulo 38 en conflicto.

## Requisito

Cuando un sistema de IA de alto riesgo utilice conjuntos de datos de formación, validación o ensayo, el proveedor deberá aplicar los requisitos de gobernanza de datos y de datos del artículo 10 del Reglamento (UE) 2024/1689, en su versión modificada.

## Explicación en lenguaje sencillo

El objetivo legal no es datos perfectos, es una gobernanza de datos disciplinada y documentada adecuada al propósito y riesgo previstos, el proveedor debe entender de dónde provienen los datos, por qué son adecuados, cómo se preparó, qué limitaciones o errores existen, si los grupos afectados están adecuadamente representados y si el sistema puede crear o reforzar sesgos.

El artículo 10 no crea de manera independiente una base legal para el tratamiento de datos personales o de categorías especiales. El RGPD y otros requisitos de privacidad aplicables deben evaluarse por separado.

## Ámbitos de gobernanza necesarios

El proveedor debe documentar, según proceda:

1. opciones de diseño de datos y procesos de recogida;
2. origen, procedencia y finalidad original de los datos;
3. preparación de datos, anotación, etiquetado, limpieza, enriquecimiento y agregación;
4. suposiciones sobre lo que los datos miden o representan;
5. disponibilidad, cantidad e idoneidad de los conjuntos de datos;
6. el examen de posibles sesgos y sus efectos en la salud, la seguridad o los derechos fundamentales;
7. medidas para detectar, prevenir y mitigar los sesgos;
8. pertinencia, representatividad, exhaustividad y características de error;
9. las propiedades estadísticas y la idoneidad para las personas, grupos, geografía, contexto y condiciones de uso previstos;
10. controles de las lagunas de datos, la deriva, las fugas, la duplicación, la contaminación y el uso no autorizado;
11. separación y gobernanza de los conjuntos de datos de formación, validación y ensayo, cuando proceda;
12. excepciones, limitaciones y riesgos residuales documentados.

## Ejemplo de GlobalWay

GlobalWay desarrolla un sistema de selección de contrataciones utilizando datos históricos de aplicaciones y contrataciones. La revisión de gobernanza de datos identifica una representación insuficiente en ciertas familias de empleos, etiquetas históricas inconsistentes, variables proxy para características protegidas y diferencias geográficas. GlobalWay elimina características inapropiadas, mejora la documentación, prueba el desempeño de subgrupos, limita el uso previsto y requiere revisión humana.

## Actividad de control

El proveedor debe aprobar un plan de gobernanza de datos específico del sistema antes del desarrollo de modelos o readiestramiento de materiales. Las versiones de conjuntos de datos, transformaciones, controles de calidad, análisis de sesgos, controles de acceso y aprobaciones deben ser rastreables a la versión del modelo o sistema liberada.

## Pruebas

- el plan de gobernanza de los datos;
- registro de datos y registros de procedencia;
- procedimientos de tratamiento y anotación de datos;
- análisis de la calidad y representatividad de los datos;
- pruebas de sesgo y subgrupo;
- la privacidad y la evaluación de las bases legales;
- historial de la versión del conjunto de datos;
- acceso y cambio de registros;
- limitaciones y registro de riesgos residuales;
- los registros de aprobación.

## Prueba de auditoría

Seleccione una versión del sistema de IA de alto riesgo publicada y tracela a los conjuntos de datos exactos de entrenamiento, validación y pruebas. Confirme que la idoneidad, procedencia, calidad, representatividad, sesgo, privacidad, transformaciones y limitaciones fueron evaluadas y aprobadas antes de su lanzamiento.

## Referencias jurídicas primarias

- Reglamento (UE) 2024/1689, modificado: artículo 10.
- El RGPD y la legislación aplicable del Estado miembro o del sector siguen siendo de aplicación independiente.
- Los actuales controles consolidados de texto EUR-Lex sobre los resúmenes antiguos.
