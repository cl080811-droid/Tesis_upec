"""Entrenamiento base de YOLO."""

from ultralytics import YOLO


def main():
    model = YOLO("yolo11n.pt")
    model.train(data="data/cattle.yaml", epochs=100, imgsz=640)


if __name__ == "__main__":
    main()
