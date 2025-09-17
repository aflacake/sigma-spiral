# tests/test_visualize.py

import matplotlib
matplotlib.use("Agg")
from sigma_spiral import plot_sigma_spiral

def test_plot_sigma_spiral_runs():
    """Uji apakah fungsi plot bisa dijalankan tanpa error."""
    try:
        plot_sigma_spiral(n_points=100, a=1.0, b=0.1)
    except Exception as e:
        assert False, f"plot_sigma_spiral gagal dijalankan: {e}"
