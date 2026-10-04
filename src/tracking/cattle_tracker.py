"""Tracking de ganado con YOLO y ByteTrack."""
from __future__ import annotations

from ultralytics import YOLO


class CattleTracker:
    """Ejecuta detección y tracking persistente sobre cuadros de video."""

    def __init__(
        self,
        model_path: str,
        confidence: float = 0.45,
        tracker: str = "bytetrack.yaml",
        cattle_class_id: int = 0,
    ) -> None:
        self.model = YOLO(model_path)
        self.confidence = float(confidence)
        self.tracker = tracker
        self.cattle_class_id = int(cattle_class_id)

    def track(self, frame):
        """Procesa un cuadro y devuelve el resultado de Ultralytics."""
        results = self.model.track(
            source=frame,
            persist=True,
            tracker=self.tracker,
            conf=self.confidence,
            verbose=False,
        )
        return results[0] if results else None
