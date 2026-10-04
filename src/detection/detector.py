"""Detector YOLO para ganado bovino."""

from ultralytics import YOLO


class CattleDetector:
    def __init__(self, model_path: str = "yolo11n.pt", confidence: float = 0.5):
        self.model = YOLO(model_path)
        self.confidence = confidence

    def predict(self, source):
        return self.model.predict(source=source, conf=self.confidence)
