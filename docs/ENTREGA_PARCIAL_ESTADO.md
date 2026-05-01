# Estado de la Entrega Parcial

Este documento deja cerrada la situación actual del proyecto para la entrega parcial y sirve como guía de trabajo hasta la entrega final.

## Equipo y repositorio

- Equipo: Diego Rodrigo, Gabriel Rezola, Hugo Ramiro e Iñigo Martinez.
- Máster: Big Data Science.
- Repositorio: `https://github.com/dieegordg/Proyecto-Machine-Learning-UNAV---Bayesianos-de-los-Ca-dos`

## 1. Objetivo de la entrega parcial

La entrega parcial no exige tener todos los mini casos terminados, pero sí exige que el proyecto esté bien encaminado, que el corpus de trabajo sea sólido y que las iniciativas finales estén definidas con claridad.

En este repositorio ya se ha avanzado de forma real en la base de datos documental y en el análisis exploratorio. Lo pendiente se encuentra metodológicamente definido.

## 2. Qué está hecho

### 2.1 Construcción del corpus

- Se ha identificado RTVE como fuente principal del corpus.
- Se ha construido un inventario de 167 documentos RTVE.
- Se ha extraído el texto completo de los 167 documentos desde las páginas de detalle.
- Se han validado y almacenado los enlaces a PDF.
- Se ha generado un manifiesto de descarga de PDFs.

### 2.2 Contraste institucional

- Se ha construido un inventario de La Moncloa con 156 enlaces PDF detectados.
- Se ha depurado el inventario comparable.
- Se ha comparado RTVE frente a La Moncloa para validar cobertura documental.
- Se ha documentado qué documentos aparecen solo en RTVE.

### 2.3 Análisis exploratorio del dato

- Se ha validado la integridad entre inventario y textos.
- Se ha estudiado la longitud documental.
- Se han creado indicadores básicos de calidad OCR.
- Se ha enriquecido el corpus con información institucional.
- Se ha realizado análisis léxico, n-gramas y TF-IDF exploratorio.
- Se ha iniciado un análisis temporal preliminar a partir de los títulos.
- Se ha generado un dataset base para las siguientes fases.

## 3. Artefactos ya disponibles en el repositorio

### Datos intermedios

- `data/interim/inventory_rtve.csv`
- `data/interim/document_texts_rtve.csv`
- `data/interim/pdf_manifest_rtve.csv`
- `data/interim/inventory_moncloa.csv`
- `data/interim/source_comparison.csv`
- `data/interim/rtve_not_matched_by_moncloa.csv`

### Datos procesados

- `data/processed/rtve_corpus_eda_ready.csv`

### Outputs de análisis

- Figuras en `outputs/figures/`
- Tablas en `outputs/tables/`

### Notebooks principales

- `notebooks/01_data_sources_and_dataset.ipynb`
- `notebooks/02_eda_documental_rtve.ipynb`
- `notebooks/00_main_pipeline.ipynb`

## 4. Mini casos definitivos

Para la entrega final se trabajará con cinco iniciativas. El mínimo exigido por el enunciado es cuatro; se dejan cinco definidas para tener margen de ajuste.

### Mini caso 1. Auditoría y EDA documental

- Pregunta: cómo es el corpus, qué calidad tiene y qué sesgos o limitaciones presenta.
- Estado: ya desarrollado en gran medida.
- Datos de entrada: inventario RTVE, textos completos y contraste con La Moncloa.
- Salidas: tablas descriptivas, figuras, flags de calidad y dataset base.

### Mini caso 2. Clasificación automática de documentos

- Pregunta: se puede predecir la sección institucional de un documento a partir de su contenido.
- Estado: definido, pendiente de implementación.
- Datos de entrada: `rtve_corpus_eda_ready.csv`.
- Variables previstas: texto completo, título, longitud, indicadores de calidad y features textuales.
- Modelos previstos: baseline, TF-IDF con Naive Bayes y Regresión Logística.
- Evaluación prevista: accuracy, macro F1, matriz de confusión y análisis de errores.

### Mini caso 3. Clustering temático y topics

- Pregunta: qué agrupaciones temáticas emergen del corpus sin supervisión.
- Estado: definido, pendiente de implementación.
- Datos de entrada: texto limpio y representaciones vectoriales.
- Métodos previstos: TF-IDF o embeddings con clustering y, si da tiempo, BERTopic.
- Evaluación prevista: silhouette, separación cualitativa e interpretación temática.

### Mini caso 4. Grafo de actores, instituciones y lugares

- Pregunta: qué relaciones aparecen entre actores e instituciones en la documentación.
- Estado: definido, pendiente de implementación.
- Datos de entrada: texto completo y entidades extraídas.
- Métodos previstos: NER, normalización de entidades, coocurrencias por documento y métricas de centralidad.
- Evaluación prevista: interpretación de nodos centrales, comunidades y coherencia del grafo.

### Mini caso 5. Análisis temporal y recuperación semántica

- Pregunta: cómo se distribuyen documentos y temas en el tiempo y cómo recuperar documentos relevantes por similitud.
- Estado: definido; la parte temporal tiene una exploración preliminar.
- Datos de entrada: títulos, fechas detectadas, texto documental y embeddings si se implementan.
- Evaluación prevista: utilidad interpretativa del timeline y ejemplos de recuperación semántica.

## 5. Metodología común ya definida

Todos los mini casos consumirán un dataset base común y seguirán un pipeline compartido:

1. Revisión del corpus y control de calidad.
2. Limpieza textual y normalización.
3. Feature engineering según el caso de uso.
4. Aplicación del método correspondiente.
5. Evaluación cuantitativa o cualitativa.
6. Interpretación de resultados.
7. Documentación de errores, limitaciones y mejoras.

## 6. Qué falta para la entrega final

- Implementar los módulos pendientes de clasificación, clustering, grafo y análisis temporal.
- Consolidar el preprocesamiento reutilizable en `src/`.
- Convertir `00_main_pipeline.ipynb` en notebook final ejecutable de principio a fin.
- Ejecutar y evaluar al menos cuatro mini casos completos.
- Redactar el informe final con resultados y conclusiones.
- Preparar la presentación y los ZIPs de entrega.

## 7. Qué debe revisarse antes de enviar la parcial

- El informe debe usar los mismos mini casos que aparecen en el repositorio.
- Deben revisarse por última vez los datos del equipo y la URL del repositorio ya incorporados.
- El repositorio debe verse ordenado y coherente con el informe.
- Debe quedar claro qué está ya hecho y qué queda planificado.
- Deben concederse externamente los permisos de acceso al profesorado.

## 8. Resumen ejecutivo del estado actual

La entrega parcial puede sostenerse con solidez porque la fase más crítica para el resto del proyecto, la construcción de un corpus documental fiable y analizable, ya está realizada. El trabajo pendiente no es de definición, sino de desarrollo e integración de los mini casos restantes sobre una base de datos ya construida.
