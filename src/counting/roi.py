"""Funciones para determinar qué animales están dentro de una zona de interés."""
from __future__ import annotations

from typing import Iterable, Sequence

import cv2
import numpy as np


Point = tuple[int, int]


def normalize_polygon(polygon: Iterable[Sequence[int | float]]) -> list[Point]:
    """Convierte coordenadas de configuración a puntos enteros."""
    return [(int(point[0]), int(point[1])) for point in polygon]


def point_in_polygon(point: tuple[float, float], polygon: Iterable[Point]) -> bool:
    """Devuelve True si el punto está dentro o sobre el borde."""
    points = normalize_polygon(polygon)
    if len(points) < 3:
        return True
    contour = np.asarray(points, dtype=np.int32)
    return cv2.pointPolygonTest(
        contour, (float(point[0]), float(point[1])), False
    ) >= 0


def cattle_in_roi(result, polygon, cattle_class_id: int = 0) -> list[dict]:
    """Extrae detecciones bovinas cuyo centro está dentro del ROI."""
    if result is None or result.boxes is None:
        return []

    boxes = result.boxes
    xyxy = boxes.xyxy.cpu().numpy()
    classes = boxes.cls.cpu().numpy().astype(int)
    ids = boxes.id.cpu().numpy().astype(int) if boxes.id is not None else None

    detections: list[dict] = []
    for index, box in enumerate(xyxy):
        if classes[index] != cattle_class_id:
            continue

        x1, y1, x2, y2 = box.tolist()
        center = ((x1 + x2) / 2.0, (y1 + y2) / 2.0)
        if not point_in_polygon(center, polygon):
            continue

        detections.append(
            {
                "track_id": int(ids[index]) if ids is not None else None,
                "bbox": (int(x1), int(y1), int(x2), int(y2)),
                "center": center,
            }
        )

    return detections
