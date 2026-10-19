## Large near-extremal spectral audit

NUMERICAL STOCHASTIC estimates: 10 Rademacher probes, seed 20261019, 24 explicitly computed positive outliers, fully reorthogonalized Lanczos of depths 48 and 96 on their orthogonal complement. Standard errors are sampling estimates, not certified enclosures; the depth comparison assesses quadrature sensitivity. The bottom eigenvalue is separately computed by FFT-Lanczos. These rows do not prove any spectral inequality.

| q | n | B1 depth96 | standard error | B1 depth48 | B2 | Dpsd | BD/sqrt n | eff rank | bottom/sqrt n |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 61 | 3782 | 0.1710084 | 0.00113 | 0.1705054 | 0.1887643 | 0.2853629 | 0.1936002 | 286.9391 | 0.7385915 |
| 101 | 10302 | 0.1686774 | 0.000742 | 0.1674636 | 0.1902772 | 0.2851436 | 0.1940062 | 762.5305 | 0.7317691 |
| 151 | 22952 | 0.1633835 | 0.000415 | 0.1629349 | 0.1968091 | 0.2817233 | 0.1954105 | 1800.584 | 0.7115075 |
| 199 | 39800 | 0.1666182 | 0.000648 | 0.1684674 | 0.192762 | 0.2823096 | 0.1920134 | 2977.88 | 0.7211983 |

NUMERICAL STOCHASTIC moment and trace audit, same probes. Values and raw standard errors for cutoff means, variances, positive/negative square masses and traces are in large_spectra.json.

| q | alpha | tr3/n³ | tr4/n⁴ | residual4/n³ | traceP/n^(3/2) | cutoff mean | cutoff variance |
|---|---:|---:|---:|---:|---:|---:|---:|
| 61 | 0.561539 | 0.1953883 | 0.1094103 | 2.707032 | 0.190991 | -1.522481 | 654.3752 |
| 101 | 0.5462349 | 0.1806542 | 0.09858119 | 6.748812 | 0.1854592 | -2.824255 | 1759.631 |
| 151 | 0.5142496 | 0.1510025 | 0.07739594 | 13.07237 | 0.1848361 | -5.272878 | 3814.522 |
| 199 | 0.5334667 | 0.1683433 | 0.08969219 | 24.92756 | 0.184438 | -5.420791 | 6738.956 |
