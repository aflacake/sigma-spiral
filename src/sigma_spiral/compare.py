# src/sigma_spiral/compare.py

"""
compare.py
----------
Perbandingan nilai konstanta Sigma Spiral dengan konstanta terkenal.
"""

import math
from .core import compute_sigma_spiral


def get_constants() -> dict:
    """
    Kembalikan daftar konstanta matematika penting beserta Σs.

    Returns:
        dict: nama konstanta -> nilai
    """
    sigma_val = compute_sigma_spiral()

    return {
        "Sigma Spiral (Σs)": sigma_val,
        "Pi (π)": math.pi,
        "Euler's number (e)": math.e,
        "Golden ratio (φ)": (1 + math.sqrt(5)) / 2,
        "Euler-Mascheroni (γ)": 0.5772156649015329,
    }


def print_comparison() -> None:
    """
    Cetak tabel perbandingan konstanta.
    """
    constants = get_constants()

    print("Perbandingan Konstanta Matematika:")
    print("-" * 45)
    for name, value in constants.items():
        print(f"{name:25} ≈ {value:.15f}")


if __name__ == "__main__":
    print_comparison()
