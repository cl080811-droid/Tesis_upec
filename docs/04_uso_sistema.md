# Uso del sistema

## Instalación
Crear un entorno virtual e instalar requirements.txt.

Windows: .venv\\Scripts\\activate
Linux/macOS: source .venv/bin/activate

## Modelo
Por defecto se espera runs/detect/train/weights/best.pt. Este archivo debe proceder del entrenamiento real de YOLO con el dataset de ganado.

## Zona de alimentación
Editar configs/default.yaml. Si roi está vacío, se cuenta todo el cuadro. Para la tesis debe reemplazarse por un polígono que corresponda al comedero y ajustarse a la resolución real de la cámara.

## Ejecución
python scripts/run_system.py --source datos/video.mp4 --no-display

Se puede sobrescribir el modelo con --model.

## Resultados
Se generan video anotado, CSV de ocupación y gráfica. El CSV registra una medición por intervalo configurado.

## Aglomeraciones
crowding_threshold debe establecerse después de conocer la capacidad real del área. El sistema marca una posible aglomeración cuando el conteo alcanza el umbral.

## Limitación
El conteo estable depende de IDs de tracking. Si no hay IDs en un cuadro, se usa el número de detecciones de ese cuadro como respaldo. La evaluación debe comparar el conteo automático con un conteo manual de referencia.
