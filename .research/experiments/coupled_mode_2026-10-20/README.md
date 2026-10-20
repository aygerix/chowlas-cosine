# Coupled W2 mode: reproducible text/code checkpoint

20 October 2026. Start with the [result report](../../notes/cstar_coupled_mode_2026-10-20.md). This archive contains only the current research pass and three explicitly labeled small dependencies from the previous pass. No PDF, unavailable repository-index reconstruction, commit, or remote push.

## Exact conclusion

An explicitly defined jointly selected tapered axis-union family of Boolean integer supports satisfies

    K_W1/sqrt(N) -> 0,
    K_E/sqrt(N) -> 0,
    K_(W2 minus {0})/sqrt(N) -> 0,
    K_W2/sqrt(N) -> 1.

For every fixed 0<c<1, eventually exactly one full-W2 eigenvalue is below -c sqrt(N). A normalized bottom eigenvector has center mass tending to 1/2 and exterior squared norm tending to zero, while the exterior remains energetically essential. The main theorem, joint-event quantifier and spectral corollaries passed independent paper-proof audit. An additional audited energy argument keeps the original support coefficients exactly one, with an exterior correction of squared norm O(alpha N) and energy o(N^(3/2)), on this family only. They are not formal kernel-verified proofs or a literature-priority claim.

The theorem uses the enhanced five-condition selection in `exterior/exterior_counterfamily.md`, section 3, for every t>=8. The old three-condition selection would prove only upper bounds; it is not substituted for the enhanced selection. The displayed rationalized thresholds give n comparable to t^6, N comparable to t^7 and h=O(t^3 log t). The sharper asymptotic selection in `order/direct_union_order_audit.md`, section 8, is separately stated.

This refutes the universal exterior-only W1-or-E dichotomy, not the full-W2 conjecture or Chowla. A universal mixed/coupled Boolean certificate remains open.

## Contents

- `exterior/`: exact axis-union decomposition, weak W1/exterior/noncentral bounds, explicit enhanced deterministic selection, and full-W2 companion. Exact finite matrix/encoding checks on 14 controls and their outputs.
- `order/`: independent same-family centered Fejer-noise certificate, matching upper bound, refined joint selection, and an exact integer Gram/energy assembly check.
- `audit/`: independent exterior/taper audit, full-W2 and localization audit, and auxiliary root-orbit audit. The exact axis/encoding check covers 30 cases and the signclass-color identity covers 16 endpoint patterns with 81 colorings each.
- `numeric/`: illustrative seeded tapered FFT samples t=2,...,6. These are not the lexicographically selected family, do not establish all joint conditions, and do not compute the full-W2 minimum eigenvalue. Rounded FFT support tests and two-space values are numerical diagnostics, not exact certificates.
- `multimode/`: exact generic bouquet/Schur identities and a separately audited root-difference low-spectral-cost projection obstruction; it is not a weak-W1 example. Includes exact orbit-count calculations and floating diagnostics. Balanced-layer/Laguerre tests are lower-bound diagnostics, not universal or finite-r theorems.
- `dependencies/`: prior three-color taper proof and audit, and exact limiting Laguerre matrix JSON needed by the optional diagnostic. No other historical pass is bundled.
- `VALIDATION.md`: archive-time reruns, exact/numerical distinctions and portability checks.
- `manifest.json`: source labels, original and archived SHA-256 hashes, and documented adaptations.

Superseded `AXIS_UNION_PARTIAL.md`, an unrelated unfinished finite search, temporary coordination notes and duplicate preliminary logs are deliberately not included. Source prose was made portable and stripped of coordination attribution; no proof or numerical algorithm was replaced.

## Reproduction

Python 3 with NumPy, SciPy and SymPy. The commands below work from this directory. Scripts that write JSON overwrite the captured outputs, so rerun in a copy if preserving the original capture matters.

    OPENBLAS_NUM_THREADS=1 python audit/check_axis_union.py
    OPENBLAS_NUM_THREADS=1 python exterior/check_axis_decomposition.py
    OPENBLAS_NUM_THREADS=1 python order/verify_direct_union.py > order/verify_direct_union_results.json
    OPENBLAS_NUM_THREADS=1 python multimode/root_orbit_response.py
    OPENBLAS_NUM_THREADS=1 python multimode/axis_laguerre_diagnostic.py --input dependencies/laguerre_full_w2_diagnostic.json
    OPENBLAS_NUM_THREADS=1 python numeric/centered_taper_check.py

The last command uses FFT arrays for X up to 1,679,616 and may need several hundred MB of RAM. No network, private source tree or external repository is needed. The cited matrix Bernstein theorem is an imported mathematical result, not a runtime dependency.

Exact assertions in the scripts check finite identities and assembly. Floating eigenvalues, FFTs and plots are not used as proofs of an infinite-family limit. No finite diagnostic should be read as a spectral enclosure or a solution of the universal problem.
