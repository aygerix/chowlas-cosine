# Archive validation

20 October 2026. Research proof audits and finite numerical/script validation are separate checks.

## Paper-proof audits

- `audit/EXTERIOR_AXIS_UNION_AUDIT.md`: PASS on the exact exterior decomposition, W1 cone estimate, dependency-sensitive tapered selected-adjacency estimate, scalar Fourier bound, joint-event intersection and carry-free integer embedding.
- `audit/FULL_W2_COMPANION_AUDIT.md`: PASS on the enhanced same-family selection, noncentral bound, centered two-space certificate, full-W2 limiting ratio 1, unique negative outlier at fixed square-root thresholds, center mass 1/2 and vanishing exterior mass. Its final section 8 also proves the family-specific exact-interior correction; this text-only addition does not change any numerical algorithm or output.
- `audit/AUXILIARY_ROOT_ORBIT_AUDIT.md`: PASS on the optional root-difference projection obstruction and bouquet formulas, with the complex-conjugation/shift clarifications incorporated. It explicitly checks that the root family is not weak W1.

These are independent paper-proof/algebraic audits, not formal verification by a proof assistant. No literature-priority claim is made.

## Portable reruns

All six documented reproduction commands exited successfully from a separate copy, without depending on the original workspace paths:

1. `audit/check_axis_union.py`: exact exterior and full-W2 encoding assertions for 30 cases; exact three-color averaging for 16 Bernoulli endpoint patterns and 81 colorings per pattern. Recorded floating exterior spectral discrepancy is approximately 6.22e-15.
2. `exterior/check_axis_decomposition.py`: exact entrywise decomposition and full-W2 encoding checks for 14 controls, plus floating spectral/cone checks.
3. `order/verify_direct_union.py`: exact integer exterior blocks, integer encoding, centered trial Gram, center coupling and energy. In the captured sample N=36 and W2 has 517 rows; its floating spectrum is only diagnostic.
4. `multimode/root_orbit_response.py`: exact representative-root enumeration, detailed balance, symbolic neighbor-count interpolation, degree checks and explicit r=4 verification. Subsequent eigenvalues and spectral masses are floating diagnostics.
5. `multimode/axis_laguerre_diagnostic.py --input dependencies/laguerre_full_w2_diagnostic.json`: reproduced the k=1,...,10 limiting-matrix diagnostics, including the punctured level-k spectral masses. These are not finite-r or universal theorems.
6. `numeric/centered_taper_check.py`: reproduced the five seeded FFT samples t=2,...,6. These are not the exact selected theorem family and do not certify the simultaneous-event conditions.

The five JSON output structures and integer fields were compared to the captured files. Floating fields were checked with relative tolerance 1e-11 and absolute tolerance 1e-9; the comparison details are in `validation_results.json`. The exact assertions above do not use that floating tolerance.

The FFT support-filling checks use rounded floating convolutions. Their maximum recorded distance from an integer is approximately 1.46e-11; this is a diagnostic, not a rigorous exact-error bound. An additional small t=2 direct-convolution comparison found about 1.33e-14 coefficient error and 2.62e-14 energy error. Neither comparison is used in the proof.

## Environment and package checks

- Python 3.12.14; NumPy 2.3.5; SciPy 1.17.0; SymPy 1.14.0.
- Python syntax and JSON parsing checked for every archived script/data file.
- Relative file links in the report and archive checked; no absolute workspace paths remain in the package.
- Minimal imported dependencies are explicitly labeled in `dependencies/` and the manifest. The superseded partial proof and unfinished finite search were not copied.
- The source/archived SHA-256 manifest records path/commentary adaptations. The archive itself is checked for ZIP integrity and contains only this pass plus its labeled minimal dependencies.
- No PDF, unavailable repository/index reconstruction, Git commit or remote push was performed.
