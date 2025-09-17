# src/sigma_spiral/visualize.py

"""
visualize.py
------------
Fungsi untuk membuat visualisasi spiral logaritmik dan menandai Σs.
"""

import numpy as np
import matplotlib.pyplot as plt
from .core import compute_sigma_spiral


def plot_sigma_spiral(n_points: int = 2000, a: float = 1.0, b: float = 0.2) -> None:
    """
    Plot spiral logaritmik sederhana dengan parameter (a, b).
    Spiral logaritmik: r(θ) = a * exp(bθ)

    Args:
        n_points (int): jumlah titik pada spiral
        a (float): skala spiral
        b (float): faktor pertumbuhan spiral
    """
    theta = np.linspace(0, 4 * np.pi, n_points)
    r = a * np.exp(b * theta)

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label="Spiral Logaritmik", color="blue")

    # Tandai konstanta Σs pada grafik
    sigma_val = compute_sigma_spiral()
    plt.scatter([sigma_val], [0], color="red", zorder=5, label=f"Σs ≈ {sigma_val:.5f}")

    plt.title("Visualisasi Spiral Logaritmik dan Konstanta Σs")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.axis("equal")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    plot_sigma_spiral()
