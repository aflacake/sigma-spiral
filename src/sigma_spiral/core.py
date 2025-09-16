"""
core.py
--------
Fungsi utama untuk menghitung konstanta Sigma Spiral (Σs).
"""

import math
from typing import Callable


def sigma_spiral_equation(x: float) -> float:
    """
    Persamaan Sigma Spiral:
        (x - 1) * sqrt(1 + (ln x)^2) - x * ln(x) = 0

    Args:
        x (float): input nilai

    Returns:
        float: hasil persamaan (harus mendekati 0 jika x ≈ Σs)
    """
    return (x - 1) * math.sqrt(1 + (math.log(x) ** 2)) - x * math.log(x)


def compute_sigma_spiral(
    initial_guess: float = 10.0,
    tol: float = 1e-12,
    max_iter: int = 1000
) -> float:
    """
    Hitung konstanta Sigma Spiral (Σs) menggunakan metode Newton-Raphson.

    Args:
        initial_guess (float): tebakan awal
        tol (float): toleransi konvergensi
        max_iter (int): iterasi maksimum

    Returns:
        float: nilai aproksimasi Σs
    """
    x = initial_guess
    for _ in range(max_iter):
        f = sigma_spiral_equation(x)
        # turunan numerik
        h = 1e-8
        f_prime = (sigma_spiral_equation(x + h) - sigma_spiral_equation(x - h)) / (2 * h)

        if f_prime == 0:
            raise ValueError("Turunan nol, metode Newton gagal.")

        x_new = x - f / f_prime
        if abs(x_new - x) < tol:
            return x_new
        x = x_new

    raise ValueError("Metode Newton tidak konvergen dalam batas iterasi.")


if __name__ == "__main__":
    sigma = compute_sigma_spiral()
    print(f"Σs ≈ {sigma:.15f}")
