# test/test_core.py

import math
import pytest
from sigma_spiral import compute_sigma_spiral, sigma_spiral_equation


def test_sigma_spiral_equation_close_to_zero():
    """Uji apakah persamaan mendekati nol pada nilai Σs."""
    sigma_val = compute_sigma_spiral()
    assert abs(sigma_spiral_equation(sigma_val)) < 1e-10


def test_sigma_spiral_positive():
    """Pastikan hasil Σs bernilai positif dan lebih besar dari e."""
    sigma_val = compute_sigma_spiral()
    assert sigma_val > math.e


def test_sigma_spiral_precision():
    """Pastikan hasil komputasi konsisten dengan nilai referensi."""
    sigma_val = compute_sigma_spiral()
    ref_val = 18.53493733204947
    assert math.isclose(sigma_val, ref_val, rel_tol=1e-12, abs_tol=1e-12)
