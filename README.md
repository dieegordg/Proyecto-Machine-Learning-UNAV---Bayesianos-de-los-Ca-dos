# Proyecto ML 23-F

Análisis inteligente de los documentos desclasificados del 23-F mediante Machine Learning, NLP, grafos y recuperación documental.

Pipeline reproducible que transforma 167 documentos históricos en un sistema analítico interpretable.

---

## Equipo

| Nombre | Máster |
|---|---|
| Diego Rodrigo | Big Data Science |
| Gabriel Rezola | Big Data Science |
| Hugo Ramiro | Big Data Science |
| Iñigo Martínez | Big Data Science |

**Repositorio:** `https://github.com/dieegordg/Proyecto-Machine-Learning-UNAV---Bayesianos-de-los-Ca-dos`

---

## Dataset

- **Fuente principal:** buscador de documentos desclasificados del 23-F de RTVE (167 documentos).
- **Fuente complementaria:** relación oficial de La Moncloa (contraste institucional).

| Variable | Valor |
|---|---|
| Documentos totales | 167 |
| Documentos con etiqueta institucional | 155 (Defensa / Interior / Exteriores) |
| Documentos sin etiqueta | 12 |
| Mediana de longitud | 579 palabras |
| Documento más largo | 95.293 palabras |
| Dataset base | `data/processed/rtve_corpus_clean_base.csv` (167 docs, 25 columnas) |

---

## Ejecución

```bash
# 1. Instalar dependencias
pip install -r requirements.txt
python -m spacy download es_core_news_sm

# 2. Ejecutar el pipeline completo desde la raíz del repositorio
jupyter notebook notebooks/00_main_pipeline.ipynb
```

El notebook `00_main_pipeline.ipynb` valida la estructura del repositorio, carga el corpus limpio y presenta los resultados integrados de los cinco casos de uso. El desarrollo técnico de cada caso se encuentra en su notebook específico.

Todos los notebooks usan **rutas relativas** y pueden ejecutarse desde la raíz del repositorio o desde la carpeta `notebooks/` sin modificar ninguna ruta.

---

## Estructura del repositorio

```
proyectoML/
├── notebooks/
│   ├── 00_main_pipeline.ipynb              # Punto de entrada e integración
│   ├── 01_data_sources_and_dataset.ipynb   # Fuentes, inventario, RTVE y Moncloa
│   ├── 02_eda_documental_rtve.ipynb        # Análisis exploratorio del corpus
│   ├── 03_limpieza_general_corpus.ipynb    # Limpieza base conservadora
│   ├── 04_caso_uso1_clasificacion_institucional.ipynb
│   ├── 05_caso_uso2.ipynb                  # Clustering temático
│   ├── 06_caso_uso3.ipynb                  # Grafo de entidades
│   ├── 07_caso_uso4_asistente_semantico.ipynb
│   └── 08_caso_uso5_fichas_documentales.ipynb
├── data/
│   ├── raw/pdfs/                           # PDFs desclasificados (no versionados)
│   ├── interim/                            # Inventarios y comparaciones intermedias
│   └── processed/                          # Dataset base limpio y outputs procesados
├── outputs/
│   ├── figures/                            # Figuras de los casos de uso
│   └── tables/                             # Tablas de resultados por caso
├── docs/                                   # Informes de entrega
├── requirements.txt
└── README.md
```

---

## Resultados por caso de uso

### Fase común — Fuentes, EDA y limpieza

- Corpus RTVE completo: 167 documentos con texto OCR, metadatos y PDF.
- Correspondencia RTVE ↔ La Moncloa: 155 matches (150 automáticos + 5 manuales).
- 12 documentos RTVE sin equivalente directo en Moncloa.
- Dataset base generado: `data/processed/rtve_corpus_clean_base.csv`.

---

### Caso 1 — Clasificación institucional

Predice la procedencia institucional (`moncloa_section`) a partir del texto limpio.

| Modelo | Accuracy | Balanced Acc | F1-macro |
|---|---|---|---|
| Baseline mayoría | 0.697 | 0.333 | 0.274 |
| TF-IDF + Logistic Regression | 0.897 | 0.845 | 0.859 |
| **TF-IDF + Linear SVM** | **0.903** | **0.832** | **0.866** |

- Validación: StratifiedKFold 5 folds.
- 15 errores totales: 9 `interior→defensa`, 3 `exteriores→defensa`, 3 `defensa→interior`.
- 12 documentos sin etiqueta clasificados como `exteriores`.

---

### Caso 2 — Clustering temático

Agrupación no supervisada del corpus mediante K-Means sobre TF-IDF.

| Cluster | Documentos | Interpretación |
|---|---|---|
| 0 | 48 | Vista oral, Tejero, documentación judicial-militar |
| 1 | 66 | Informes generales, situación interior, contexto del golpe |
| 2 | 6 | Documentación exterior, Casa Real, mensajes institucionales |
| 3 | 19 | Exteriores con dimensión internacional y prensa extranjera |
| 4 | 28 | Justicia militar, Consejo Supremo, documentación procesal |

- K=5 seleccionado (silhouette coseno: 0.082).
- Visualización bidimensional mediante TruncatedSVD.

---

### Caso 3 — Grafo de entidades

Red de coaparición entre personas, organizaciones y lugares extraídos con spaCy.

| Métrica | Valor |
|---|---|
| Nodos | 436 |
| Aristas | 6.728 |
| Densidad | 0.071 |
| Componentes | 4 |

- Entidades más centrales: `Congreso`, `Guardia Civil`, `España`, `Madrid`, `General Armada`, `CESID`.
- Las aristas representan coaparición documental, no relaciones causales directas.

---

### Caso 4 — Asistente documental semántico

Buscador por similitud coseno sobre fragmentos del corpus.

| Parámetro | Valor |
|---|---|
| Chunks generados | 1.998 (de 167 docs) |
| Tamaño de chunk | 220 palabras, 40 solapamiento |
| Vocabulario TF-IDF | 52.850 términos |
| Recall@1 | 1.0 |
| Recall@3 | 1.0 |
| Recall@5 | 1.0 |

- Búsqueda por consulta libre y recomendación de documentos similares.
- Trazabilidad completa: `doc_id`, título, fragmento de evidencia, score y enlace al PDF.

---

### Caso 5 — Generación automática de fichas documentales

Resúmenes estructurados por documento mediante método híbrido y capa LLM opcional.

| Estado | Documentos |
|---|---|
| Generado con LLM (GitHub Models / gpt-4.1-mini) | 112 |
| Fallback híbrido (semilla + evidencias extractivas) | 55 |
| **Total con resumen completo** | **167** |

- El `summary` original (303 caracteres, truncado) se usa solo como semilla temática.
- Output: `resumen_corto` (~90 palabras) + `resumen_extendido` (~230 palabras) por documento.
- Dataset final: `data/processed/rtve_documentary_summaries_case5.csv`.

---

## Reproducibilidad

- Todas las rutas son relativas a la raíz del repositorio.
- El notebook `00_main_pipeline.ipynb` valida automáticamente estructura, archivos y ausencia de rutas absolutas.
- Sin intervención manual para ejecutar de principio a fin.
- PDFs originales (~255 MB) no versionados en Git; disponibles bajo petición.
