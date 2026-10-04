"""Funciones básicas de conteo de detecciones."""

def count_detections(results) -> int:
    """Devuelve el número de cajas detectadas en un resultado YOLO."""
    if results is None:
        return 0
    return sum(len(result.boxes) for result in results)
