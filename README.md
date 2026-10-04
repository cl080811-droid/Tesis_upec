# Detección y Conteo de Ganado usando Cámaras Fijas

Proyecto de tesis para detectar y contar ganado bovino mediante visión artificial, utilizando YOLO, ByteTrack y procesamiento de imágenes/video.

## Objetivo

Desarrollar un sistema que detecte vacas en corrales o zonas de alimentación, mantenga la identidad temporal de cada animal, contabilice los individuos dentro de una zona de interés y registre la ocupación a lo largo del tiempo.

## Flujo implementado

Cámara fija → video/fotogramas → YOLO → ByteTrack → filtro de clase bovino → zona ROI → conteo de IDs → CSV → video anotado → gráfica.

## Estructura

- data/: datasets y configuración.
- src/: código fuente de detección, tracking, conteo, monitoreo y visualización.
- scripts/: entrenamiento, inferencia y ejecución del sistema.
- configs/: parámetros reproducibles del sistema.
- notebooks/: experimentación.
- results/: métricas y gráficas.
- docs/: metodología, arquitectura y uso.
- tests/: pruebas automáticas.

## Ejecución principal

Con el modelo entrenado y un video real:

python scripts/run_system.py --source datos/video.mp4 --no-display

La configuración se encuentra en configs/default.yaml.

## Resultados

El sistema prepara:
- video anotado con cajas e IDs;
- conteo de bovinos dentro del ROI;
- registro temporal en CSV;
- gráfica de ocupación;
- aviso de posible aglomeración cuando se configure un umbral basado en la capacidad real.

## Validación

El repositorio incluye pruebas unitarias y validación automática de sintaxis mediante GitHub Actions. La validación automática no sustituye la evaluación experimental con videos reales.

## Datos reales

No se deben inventar resultados de detección, conteos, métricas ni pesos de YOLO. La evaluación final debe realizarse con el dataset y los videos reales de la investigación y compararse contra un conteo manual de referencia.
