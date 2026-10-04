"""Inferencia sobre una imagen o video."""

import argparse
from ultralytics import YOLO


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="runs/detect/train/weights/best.pt")
    parser.add_argument("--source", required=True)
    parser.add_argument("--conf", type=float, default=0.5)
    args = parser.parse_args()

    model = YOLO(args.model)
    model.predict(source=args.source, conf=args.conf, save=True)


if __name__ == "__main__":
    main()
