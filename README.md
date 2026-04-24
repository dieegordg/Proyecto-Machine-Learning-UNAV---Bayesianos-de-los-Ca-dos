# Proyecto ML 23-F - Entrega parcial

Este repositorio contiene la propuesta y estructura inicial del proyecto de Machine Learning sobre los documentos desclasificados del 23-F.

## Datos
- Fuente principal: buscador RTVE de documentos desclasificados del 23-F.
- Fuente complementaria: relación oficial de La Moncloa.

## Estructura
- `notebooks/00_main_pipeline.ipynb`: notebook principal ejecutable.
- `src/`: módulos auxiliares.
- `data/raw/`: datos originales o ficheros descargados.
- `data/interim/`: datos intermedios.
- `data/processed/`: dataset final procesado.
- `outputs/`: figuras, tablas y modelos.
- `docs/`: informes y presentación.

## Mini casos propuestos
1. Auditoría y EDA documental.
2. Clasificación automática de documentos.
3. Clustering temático y topic modeling.
4. Grafo de actores, instituciones y lugares.
5. Análisis temporal y buscador semántico.

## Instrucciones previstas
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/00_main_pipeline.ipynb
```

## Pendiente antes de entregar
- Completar nombres del equipo.
- Pegar URL real del repositorio Git en el informe.
- Dar permisos de acceso al profesorado.
