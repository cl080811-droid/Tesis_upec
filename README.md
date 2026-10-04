# Detección y Conteo de Ganado usando Cámaras Fijas

Proyecto de tesis para detectar y contar ganado bovino mediante visión artificial, utilizando YOLO y procesamiento de imágenes/video.

## Objetivo
Desarrollar un sistema que detecte vacas en corrales o zonas de alimentación, contabilice los individuos y registre la ocupación a lo largo del tiempo.

## Flujo
Cámara fija → video/fotogramas → detección YOLO → bounding boxes → conteo → registro temporal → gráficas → análisis.

## Estructura
- `data/`: datasets y configuración.
- `src/`: código fuente.
- `scripts/`: entrenamiento, evaluación e inferencia.
- `notebooks/`: experimentación.
- `results/`: métricas y gráficas.
- `docs/`: metodología.
- `tests/`: pruebas.

## Próximos pasos
1. Incorporar el dataset real y sus anotaciones.
2. Entrenar y evaluar YOLO.
3. Implementar tracking y conteo robusto por zona.
4. Registrar ocupación temporal y generar gráficas.
5. Validar el sistema contra conteo humano.
