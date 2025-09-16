"""
Sigma Spiral (Σs)
=================

Package ini berisi perhitungan, visualisasi, dan perbandingan
konstanta Sigma Spiral (Σs).

Contoh penggunaan:

>>> from sigma_spiral import compute_sigma_spiral
>>> compute_sigma_spiral()
18.53493733204947
"""

from .core import compute_sigma_spiral, sigma_spiral_equation
from .visualize import plot_sigma_spiral
from .compare import get_constants, print_comparison

__all__ = [
    "compute_sigma_spiral",
    "sigma_spiral_equation",
    "plot_sigma_spiral",
    "get_constants",
    "print_comparison",
]
