"""Ejecuta detección, tracking, conteo, registro y visualización."""
from __future__ import annotations

import argparse
from pathlib import Path

import cv2
import numpy as np
import yaml

from src.counting.roi import cattle_in_roi
from src.monitoring.recorder import OccupancyRecorder
from src.tracking.cattle_tracker import CattleTracker
from src.visualization.plots import plot_occupancy


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Conteo de ganado con cámara fija.")
    parser.add_argument("--source", required=True)
    parser.add_argument("--config", default="configs/default.yaml")
    parser.add_argument("--model", default=None)
    parser.add_argument("--output-video", default=None)
    parser.add_argument("--no-display", action="store_true")
    return parser.parse_args()


def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}


def main() -> None:
    args = parse_args()
    config = load_config(args.config)
    model_path = args.model or config["model"]
    confidence = float(config.get("confidence", 0.45))
    tracker_name = config.get("tracker", "bytetrack.yaml")
    cattle_class_id = int(config.get("cattle_class_id", 0))
    sample_interval = float(config.get("sampling_interval_seconds", 1.0))
    if sample_interval <= 0:
        raise ValueError("sampling_interval_seconds debe ser mayor que 0.")

    roi = config.get("roi") or []
    outputs = config.get("output", {})
    csv_path = Path(outputs.get("csv", "results/metrics/occupancy.csv"))
    video_path = Path(args.output_video or outputs.get("video", "results/predictions/tracked.mp4"))
    plot_path = Path(outputs.get("plot", "results/plots/occupancy.png"))

    tracker = CattleTracker(model_path, confidence, tracker_name, cattle_class_id)
    recorder = OccupancyRecorder(csv_path)

    capture = cv2.VideoCapture(args.source)
    if not capture.isOpened():
        raise RuntimeError(f"No se pudo abrir la fuente de video: {args.source}")

    fps = capture.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 30.0
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    if width <= 0 or height <= 0:
        capture.release()
        raise RuntimeError("La fuente no reportó dimensiones válidas.")

    video_path.parent.mkdir(parents=True, exist_ok=True)
    writer = cv2.VideoWriter(
        str(video_path), cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height)
    )
    if not writer.isOpened():
        capture.release()
        raise RuntimeError(f"No se pudo crear el video de salida: {video_path}")

    polygon = [(int(p[0]), int(p[1])) for p in roi]
    frame_index = 0
    last_recorded_second = -1
    crowding_threshold = config.get("crowding_threshold")

    try:
        while True:
            ok, frame = capture.read()
            if not ok:
                break

            result = tracker.track(frame)
            detections = cattle_in_roi(result, polygon, cattle_class_id)
            track_ids = {d["track_id"] for d in detections if d["track_id"] is not None}
            all_have_ids = len(track_ids) == len(detections)
            count = len(track_ids) if all_have_ids else len(detections)

            annotated = frame.copy()
            if len(polygon) >= 3:
                cv2.polylines(
                    annotated, [np.asarray(polygon, dtype=np.int32)], True,
                    (255, 0, 0), 2
                )

            for item in detections:
                x1, y1, x2, y2 = item["bbox"]
                label = (
                    f"Vaca ID {item['track_id']}"
                    if item["track_id"] is not None else "Vaca"
                )
                cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(
                    annotated, label, (x1, max(20, y1 - 8)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2
                )

            status = f"Bovinos en zona: {count}"
            if crowding_threshold is not None and count >= int(crowding_threshold):
                status += " | POSIBLE AGLOMERACION"
            cv2.putText(
                annotated, status, (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                (0, 0, 255) if "AGLOMERACION" in status else (255, 255, 255), 2
            )
            writer.write(annotated)

            elapsed = frame_index / fps
            current_second = int(elapsed / sample_interval)
            if current_second != last_recorded_second:
                recorder.record(frame_index, elapsed, count)
                last_recorded_second = current_second

            if not args.no_display:
                cv2.imshow("Conteo de ganado", annotated)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            frame_index += 1
    finally:
        capture.release()
        writer.release()
        cv2.destroyAllWindows()

    plot_occupancy(csv_path, plot_path)
    print(f"Video: {video_path}")
    print(f"CSV: {csv_path}")
    print(f"Gráfica: {plot_path}")


if __name__ == "__main__":
    main()
