"""Conteo simple de ganado en un video."""

import argparse
import cv2
from ultralytics import YOLO


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--source", required=True)
    args = parser.parse_args()

    model = YOLO(args.model)
    cap = cv2.VideoCapture(args.source)

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        result = model.predict(frame, conf=0.5, verbose=False)[0]
        cattle_count = len(result.boxes)
        print(f"Ganado detectado: {cattle_count}")

    cap.release()


if __name__ == "__main__":
    main()
