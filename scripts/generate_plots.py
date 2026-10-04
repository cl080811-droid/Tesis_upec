"""Genera una gráfica de ocupación a partir de un CSV."""

import argparse
import pandas as pd
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="results/plots/ocupacion.png")
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    plt.figure(figsize=(10, 5))
    plt.plot(df["timestamp"], df["cattle_count"])
    plt.xlabel("Hora")
    plt.ylabel("Número de vacas")
    plt.title("Ocupación del área de alimentación")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(args.output, dpi=150)


if __name__ == "__main__":
    main()
