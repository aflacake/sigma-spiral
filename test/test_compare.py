# tests/test_compare.py

from sigma_spiral import get_constants, print_comparison

def test_constants_contains_sigma():
    """Pastikan dictionary konstanta mengandung Sigma Spiral."""
    constants = get_constants()
    assert "Sigma Spiral (Σs)" in constants
    assert isinstance(constants["Sigma Spiral (Σs)"], float)

def test_print_comparison_runs(capsys):
    """Pastikan fungsi print_comparison bisa dijalankan dan ada outputnya."""
    print_comparison()
    captured = capsys.readouterr()
    assert "Sigma Spiral (Σs)" in captured.out
    assert "Pi (π)" in captured.out
