"""Gráficas de ocupación de ganado."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def plot_occupancy(csv_path: str | Path, output_path: str | Path) -> Path:
    data = pd.read_csv(csv_path)
    required = {"elapsed_seconds", "cattle_count"}
    missing = required.difference(data.columns)
    if missing:
        raise ValueError(f"CSV sin columnas requeridas: {sorted(missing)}")

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 5))
    plt.plot(data["elapsed_seconds"], data["cattle_count"], linewidth=1.5)
    plt.xlabel("Tiempo transcurrido (s)")
    plt.ylabel("Número de bovinos")
    plt.title("Ocupación del área de alimentación")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output, dpi=150)
    plt.close()
    return output
