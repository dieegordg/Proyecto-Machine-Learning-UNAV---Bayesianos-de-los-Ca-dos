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
- manifiesto preparado para descargar PDFs físicos.

El siguiente paso será descargar los PDFs en `data/raw/pdfs_rtve/` usando el manifiesto.
