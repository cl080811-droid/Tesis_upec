"""Registro CSV de ocupación del área."""
from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path


class OccupancyRecorder:
    HEADER = ["timestamp", "frame", "elapsed_seconds", "cattle_count"]

    def __init__(self, csv_path: str | Path) -> None:
        self.path = Path(csv_path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._write_header_if_needed()

    def _write_header_if_needed(self) -> None:
        if not self.path.exists() or self.path.stat().st_size == 0:
            with self.path.open("w", newline="", encoding="utf-8") as file:
                csv.writer(file).writerow(self.HEADER)

    def record(self, frame: int, elapsed_seconds: float, cattle_count: int) -> None:
        with self.path.open("a", newline="", encoding="utf-8") as file:
            csv.writer(file).writerow(
                [
                    datetime.now(timezone.utc).isoformat(),
                    int(frame),
                    round(float(elapsed_seconds), 3),
                    int(cattle_count),
                ]
            )
