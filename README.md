# Proyecto ML 23-F

Repositorio de trabajo del proyecto de Machine Learning sobre los documentos desclasificados del 23-F.

El estado actual del repositorio corresponde a una entrega parcial avanzada: la construcción del corpus y el análisis exploratorio documental están ya desarrollados, y el resto de iniciativas queda definido y encaminado para la entrega final.

## Dataset

- Fuente principal: buscador RTVE de documentos desclasificados del 23-F.
- Fuente de contraste institucional: relación oficial de La Moncloa.

## Equipo

- Diego Rodrigo
- Gabriel Rezola
- Hugo Ramiro
- Iñigo Martinez

Máster: `Big Data Science`

Repositorio: `https://github.com/dieegordg/Proyecto-Machine-Learning-UNAV---Bayesianos-de-los-Ca-dos`

## Estado de la entrega parcial

### Trabajo ya realizado

- Construcción del inventario RTVE con 167 documentos.
- Extracción del texto completo desde las páginas de detalle RTVE.
- Validación y trazabilidad de enlaces a PDF.
- Descarga controlada y manifiesto de PDFs.
- Construcción del inventario de La Moncloa.
- Comparación RTVE vs La Moncloa para validar cobertura documental.
- Análisis exploratorio documental del corpus.
- Generación de un dataset base listo para los siguientes mini casos.

### Mini casos definidos para la entrega final

1. Auditoría y EDA documental del corpus.
2. Clasificación automática de documentos por sección institucional.
3. Clustering temático y exploración de topics.
4. Grafo de actores, instituciones y lugares.
5. Análisis temporal y prototipo de recuperación semántica.

### Estado real por iniciativa

- `EDA documental`: implementado en gran medida.
- `Clasificación supervisada`: definido, pendiente de implementar.
- `Clustering/topic modeling`: definido, pendiente de implementar.
- `Grafo de entidades`: definido, pendiente de implementar.
- `Análisis temporal aplicado / buscador semántico`: definido, con análisis preliminar temporal ya iniciado.

## Estructura del repositorio

- `notebooks/00_main_pipeline.ipynb`: punto de entrada y cuaderno de seguimiento global de la entrega parcial.
- `notebooks/01_data_sources_and_dataset.ipynb`: construcción del corpus y validación de fuentes.
- `notebooks/02_eda_documental_rtve.ipynb`: análisis exploratorio documental y generación del dataset base.
- `src/`: módulos auxiliares para consolidar lógica reusable.
- `data/raw/`: documentos originales y PDFs descargados.
- `data/interim/`: tablas intermedias de inventario, extracción y contraste.
- `data/processed/`: datasets preparados para modelado.
- `outputs/`: figuras y tablas exportadas.
- `docs/`: informe intermedio y documentación de apoyo.

## Flujo de trabajo previsto

1. Construcción y validación del corpus documental.
2. Limpieza y enriquecimiento del dataset base.
3. Desarrollo de mini casos sobre el corpus procesado.
4. Evaluación, interpretación y redacción del informe final.

## Cómo revisar el proyecto

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/00_main_pipeline.ipynb
```

## Documentación clave

- [docs/informe_intermedio.pdf](docs/informe_intermedio.pdf)
- [docs/ENTREGA_PARCIAL_ESTADO.md](docs/ENTREGA_PARCIAL_ESTADO.md)
- [DECISIONES_notebook.md](DECISIONES_notebook.md)

## Pendiente antes de enviar la entrega parcial

- Confirmar externamente los permisos de acceso al profesorado.
- Revisar la exportación final del informe actualizado a PDF.
- Revisar que el informe y el repositorio usen exactamente los mismos mini casos.
