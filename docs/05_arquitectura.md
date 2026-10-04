# Arquitectura implementada

Cámara o video
↓
YOLO
↓
ByteTrack
↓
Filtro por clase bovino
↓
Filtro por zona ROI
↓
Conteo de IDs activos
↓
Registro temporal CSV
↓
Video anotado y gráfica

## Tracking
Contar cajas de cada frame por separado puede producir conteos inconsistentes. ByteTrack mantiene una identidad temporal y permite contar IDs activos dentro de la zona.

## ROI
Solo se contabiliza una vaca cuando el centro de su bounding box está dentro del polígono de interés.

## Reproducibilidad
El repositorio contiene código y configuración, pero no contiene videos privados, imágenes de cámaras ni pesos entrenados. No se deben reemplazar esos elementos por datos ficticios.

## Evaluación
La evaluación final debe comparar el conteo automático con un conteo manual de referencia. Se recomienda calcular MAE, RMSE, error porcentual y, para detección, Precision, Recall y mAP.
