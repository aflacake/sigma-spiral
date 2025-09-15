# Sigma Spiral (Σs)
**Sigma spiral** adalah konstanta matematika baru yang muncul dari spiral logaritmik dengan bentuk lebih kompleks, tapi alami, definisi lebih teknis: busur spiral 1 radian = radius akhir, dengan rumus:

`(Σs - 1) * sqrt(1 + (ln Σs)^2) = Σs * ln Σs`

Hasil numerik:

`Σs ≈ 18.53493733204947`

> Catatan: proyek ini bersifat **eksperimental** dan terbuka untuk kolaborasi.
> Tujuannya bukan klaim final, melainkan eksplorasi numerik, visualisasi, dan dokumentasi.

## Fitur
- Perhitungan Sigma Spiral dengan Python.
- Visualisasi spiral logaritmik.
- Perbandingan Σs dengan konstanta terkenal adalah π, e, dan φ.
- Unit test dan workflow otomatis.
- Open collaboration.

## Instalasi
```
pip install sigma-spiral
```

## Contoh Penggunaan
```py
from sigma_spiral.core import compute_sigma_spiral

print(compute_sigma_spiral())
# 18.53493733204947
```

## Lisensi
[Apache-2.0](https://github.com/aflacake/sigma-spiral/blob/main/LICENSE)
