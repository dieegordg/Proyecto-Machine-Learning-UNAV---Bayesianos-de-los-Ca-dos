# Proyecto ML 23-F

Repositorio de trabajo del proyecto de Machine Learning sobre los documentos desclasificados del 23-F.

Este proyecto tiene como objetivo construir un **pipeline reproducible de análisis documental** que permita transformar un corpus histórico complejo en un sistema analítico interpretable mediante técnicas de NLP, Machine Learning, grafos y recuperación semántica.

El estado actual corresponde a una **entrega parcial consolidada**, donde:
- El corpus está completamente construido y validado.
- Se ha realizado un análisis exploratorio exhaustivo.
- Se ha definido en detalle la metodología y los mini casos para la entrega final.

---

## Dataset

- **Fuente principal**: buscador de documentos desclasificados del 23-F de RTVE (167 documentos).
- **Fuente complementaria**: relación oficial de La Moncloa para enriquecimiento institucional.

### Características del dataset

- 167 documentos con texto OCR completo.
- 155 documentos con correspondencia institucional (RTVE ↔ La Moncloa).
- Corpus altamente **heterogéneo**:
  - Informes, notas, transcripciones, documentos militares, etc.
- Dataset base:  
  `data/processed/rtve_corpus_clean_base.csv` (167 docs, 25 variables).

---

## Objetivo del proyecto

### Objetivo general
Desarrollar un sistema completo, reproducible e interpretable para analizar los documentos del 23-F mediante:
- NLP
- clasificación
- clustering
- grafos
- análisis temporal
- recuperación semántica

### Objetivos específicos

- Construir un dataset estructurado y trazable.
- Auditar la calidad del dato (OCR, duplicados, metadatos).
- Clasificar documentos por procedencia institucional.
- Detectar temas latentes.
- Modelar relaciones entre actores e instituciones.
- Desarrollar un sistema de búsqueda semántica.
- Generar representaciones documentales enriquecidas.

---

## Equipo

- Diego Rodrigo  
- Gabriel Rezola  
- Hugo Ramiro  
- Iñigo Martínez  

Máster: `Big Data Science`  

Repositorio:  
`https://github.com/dieegordg/Proyecto-Machine-Learning-UNAV---Bayesianos-de-los-Ca-dos`

---

## Estado de la entrega parcial

### Trabajo realizado

- Construcción completa del corpus RTVE (167 documentos).
- Extracción y validación del texto OCR.
- Descarga y trazabilidad de PDFs.
- Integración con La Moncloa (155 matches).
- Análisis exploratorio completo:
  - integridad
  - longitudes
  - calidad OCR
  - señal textual
- Generación del dataset base limpio (`text_clean_base`).
- Definición metodológica completa del proyecto.

---

## Mini casos (entrega final)

### 1. Clasificación automática de documentos
- Objetivo: predecir `moncloa_section`.
- Técnicas: TF-IDF + modelos lineales (LogReg, SVM).
- Dataset: 155 documentos etiquetados.

---

### 2. Clustering temático y topic modeling
- Objetivo: descubrir estructuras temáticas sin etiquetas.
- Técnicas:
  - TF-IDF / embeddings
  - K-Means / HDBSCAN
  - UMAP / PCA
- Evaluación: métricas internas + interpretación.

---

### 3. Grafo de actores, instituciones y lugares
- Objetivo: modelar relaciones mediante co-ocurrencias.
- Técnicas:
  - NER
  - NetworkX
  - análisis de centralidad y comunidades

---

### 4. Asistente documental semántico
- Objetivo: sistema de búsqueda sobre el corpus.
- Técnicas:
  - chunking de documentos largos
  - TF-IDF / embeddings
  - similitud coseno
- Output:
  - fragmentos relevantes
  - trazabilidad (doc_id, PDF)

---

### 5. Generación automática de fichas documentales
- Objetivo: enriquecer el corpus con resúmenes estructurados.
- Contenido:
  - resumen corto y extendido
  - actores
  - instituciones
  - fechas
  - temas
- Enfoque:
  - extractivo o generativo controlado

---

## Estado real por iniciativa

- `EDA documental`: implementado completamente  
- `Clasificación supervisada`: definido  
- `Clustering`: definido  
- `Grafo de entidades`: definido  
- `Asistente semántico`: definido (con análisis de longitud avanzado)  
- `Fichas documentales`: definido  

---

## Metodología

### Pipeline de trabajo

1. Ingesta y extracción  
2. Limpieza base (conservadora)  
3. Procesamiento NLP específico  
4. Feature engineering  
5. Modelado  
6. Evaluación e interpretación  

### Principios clave

- Reproducibilidad  
- Trazabilidad  
- Separación clara entre EDA y modelado  
- Evitar fuga de información  

