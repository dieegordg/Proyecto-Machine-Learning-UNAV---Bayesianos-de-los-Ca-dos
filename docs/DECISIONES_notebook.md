# DECISIONES_notebook.md

## Objetivo del archivo

Este documento recoge las decisiones principales tomadas durante la construcción del notebook de fuentes de datos.  
Su finalidad es facilitar después la redacción del informe del proyecto.

---

## Decisión 1 — Reiniciar el notebook de datos

Se decide crear un notebook nuevo desde cero porque el notebook anterior no seguía un flujo suficientemente claro para la fase actual del proyecto.

El nuevo notebook se centra primero en responder:

> ¿Qué se puede analizar realmente con estos documentos?

Antes de plantear modelos, se considera necesario construir una base documental fiable, con inventario, textos completos y enlaces a los documentos originales.

---

## Decisión 2 — Usar RTVE como fuente principal del corpus

Se decide utilizar el Buscador RTVE 23-F como fuente principal del dataset porque permite obtener:

- el listado completo de documentos;
- título;
- número de páginas;
- resumen;
- palabras clave;
- texto completo;
- enlace al documento original en PDF.

La página visible de RTVE funciona como entrada al buscador, pero la aplicación real se encuentra en:

`https://23fbuscador.rtve.es/`

---

## Decisión 3 — Construir el inventario con `page_size=200`

Se comprueba que la aplicación del Buscador RTVE permite mostrar todos los documentos usando:

`https://23fbuscador.rtve.es/?page_size=200`

Con esta opción se obtienen los 167 documentos en una sola página, lo que permite construir el inventario documental completo de RTVE.

---

## Decisión 4 — Usar `doc_id` como clave del proyecto

Se decide crear un identificador interno llamado `doc_id`.

Este identificador permite relacionar de forma estable:

- inventario documental;
- textos completos;
- enlaces a PDF;
- futuros resultados de limpieza, EDA y modelado.

No se usa el título como clave porque algunos documentos tienen títulos repetidos o muy parecidos.

---

## Decisión 5 — No eliminar documentos con títulos repetidos

Se detectan títulos repetidos en el inventario, pero no se eliminan porque no son duplicados reales.

Cada documento tiene:

- `doc_id` distinto;
- URL de detalle distinta;
- resumen distinto;
- palabras clave distintas;
- PDF distinto.

Por tanto, el criterio de unicidad será `doc_id`, no el título.

---

## Decisión 6 — Extraer el texto completo desde las páginas de detalle

Se comprueba que cada página de detalle de RTVE contiene el texto completo directamente en HTML.

Esto permite extraer los textos sin depender de OCR local ni de extracción desde PDF.

Resultado obtenido:

- 167 documentos procesados;
- 167 textos completos extraídos correctamente.

---

## Decisión 7 — Obtener los enlaces a PDF desde las páginas de detalle

Se comprueba que cada página de detalle contiene un enlace al original digitalizado.

En los 167 casos, ese enlace redirige a un PDF válido.

Por tanto, se obtienen también los 167 enlaces finales a PDF desde la fuente principal de RTVE.

---

## Decisión 8 — Separar los datos en tres salidas

Se decide separar la información en tres archivos:

1. `inventory_rtve.csv`  
   Metadatos documentales y enlace final al PDF.

2. `document_texts_rtve.csv`  
   Texto completo, métricas básicas y enlace rápido al PDF.

3. `pdf_manifest_rtve.csv`  
   Archivo de control para descargar físicamente los PDFs de forma ordenada.

Esta separación evita mezclar metadatos, textos largos y control de archivos en una sola tabla.

---

## Decisión 9 — Mantener La Moncloa como fuente de contraste

La Moncloa se mantiene como fuente institucional de contraste.

Su función será comprobar si existe algún documento oficial que no aparezca en el corpus obtenido desde RTVE.

No se descargarán todos los PDFs de La Moncloa para evitar duplicar documentos. Solo se considerará hacerlo si se detecta algún documento presente en La Moncloa y ausente en RTVE.

---

## Estado actual del bloque de fuentes RTVE

Hasta este punto se ha conseguido:

- inventario RTVE completo: 167 documentos;
- textos completos extraídos: 167 documentos;
- enlaces finales a PDF: 167 documentos;
- manifiesto de descarga de PDFs creado;
- PDFs físicos descargados correctamente: 167 documentos;
- errores de descarga: 0.

Los PDFs se han guardado localmente en `data/raw/pdfs_rtve/` y también se ha creado un ZIP local. No se suben al repositorio Git porque ocupan aproximadamente 255 MB. Se conservarán para la entrega final o para compartirlos externamente si el equipo lo necesita.

---

## Decisión 10 — Usar La Moncloa solo como contraste institucional

Se construye un inventario de La Moncloa para comprobar si contiene documentos oficiales no cubiertos por RTVE.

El inventario de La Moncloa contiene 156 enlaces PDF detectados. Uno corresponde al BOE, por lo que se excluye de la comparación documental principal.

Resultado de la comparación:

- 155 documentos comparables de La Moncloa.
- 155 documentos cubiertos por RTVE.
- 150 coincidencias automáticas de alta confianza.
- 5 coincidencias aceptadas tras revisión manual.
- 12 documentos presentes en RTVE sin equivalente directo detectado en Moncloa.

Se decide no descargar documentos adicionales desde La Moncloa porque no se detectan documentos comparables ausentes en RTVE.

---

## Decisión 11 — Mantener RTVE como fuente principal y más completa para el proyecto

Tras la validación con La Moncloa, se mantiene RTVE como fuente principal del corpus de trabajo.

Motivos:

- RTVE proporciona los 167 documentos del corpus.
- Permite extraer metadatos, texto completo y PDF.
- Cubre los 155 documentos comparables de La Moncloa.
- Aporta 12 registros adicionales no detectados en el inventario comparable de La Moncloa.

La Moncloa queda como fuente institucional de contraste, no como fuente principal de extracción.

---

## Estado actual tras la comparación con La Moncloa

Se han generado las siguientes salidas adicionales:

- `inventory_moncloa.csv`: inventario de enlaces PDF detectados en La Moncloa.
- `source_comparison.csv`: comparación final entre Moncloa y RTVE.
- `rtve_not_matched_by_moncloa.csv`: documentos presentes en RTVE sin equivalente directo detectado en Moncloa.

Resultado final de cobertura:

- RTVE: 167 documentos.
- La Moncloa: 156 enlaces PDF detectados.
- La Moncloa comparable: 155 documentos, excluyendo el BOE.
- Documentos comparables de La Moncloa cubiertos por RTVE: 155.
- Coincidencias automáticas de alta confianza: 150.
- Coincidencias aceptadas tras revisión manual: 5.
- Documentos RTVE sin equivalente directo detectado en Moncloa: 12.

La comparación no se ha realizado PDF a PDF ni byte a byte. Se ha hecho mediante títulos, nombres de archivo, fechas extraídas, similitud textual y revisión manual de los casos dudosos.

Conclusión operativa: RTVE se mantiene como fuente principal del corpus porque cubre los documentos comparables de La Moncloa y además aporta registros adicionales con texto completo, metadatos y PDF asociado.
