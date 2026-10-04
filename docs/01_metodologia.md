# Metodología propuesta

## 1. Captura
Cámaras fijas orientadas al corral o comedero y definición de zona de interés.

## 2. Dataset
Imágenes representativas de iluminación, posiciones, oclusiones y densidad. Cada vaca se etiqueta con bounding box.

## 3. Entrenamiento
Separar train/val/test y ajustar un modelo YOLO para la clase vaca.

## 4. Detección
Procesar imágenes o fotogramas y obtener cajas, confianza y clase.

## 5. Conteo
Contar detecciones dentro de la zona de interés. Para video, incorporar tracking para evitar doble conteo.

## 6. Monitoreo temporal
Registrar timestamp y cantidad detectada.

## 7. Análisis
Generar curvas de ocupación por hora y detectar periodos de alta concentración.

## 8. Evaluación
Comparar conteo automático con conteo manual usando MAE, RMSE y métricas de detección como mAP.
