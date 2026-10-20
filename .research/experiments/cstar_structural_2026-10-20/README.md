# C* structural research checkpoint, 2026-10-20

Checkpoint captured at 2026-10-20 05:32:53 UTC. Research is ongoing. No universal Chowla/C* bound or universal W2 square-root inequality has been proved. The latter remains under test. This bundle is text-only; it does not create a PDF, commit, or push. The manifest records the exact source versions and their modification times, not a promise that the evolving sources will remain unchanged.

## Mathematical notes

- [Hereditary ratio minimality and exact integrality countercontrol](../../notes/cstar_subset_minimal_2026-10-20.md).
- [Fixed-cardinality attainment and strict-record reduction](../../notes/cstar_extremizer_compactness_2026-10-20.md).
- [Collective exterior optimization and all-face axes repair](../../notes/cstar_collective_boundary_2026-10-20.md).
- [Order-sensitive matrix identities and root-difference refutation](../../notes/cstar_order_matrix_2026-10-20.md).
- [Second-neighborhood E99c localization](../../notes/cstar_double_neighborhood_2026-10-20.md).

The existing universal L1/fixed-depth floor route remains closed in its previously stated scope. The exact-minimizer reduction does not reopen it or prove a quantitative replacement. All new entries are unnumbered supplements to avoid changing existing P/E identifiers.

## Reproduction

Requires Python, NumPy, SciPy, and SymPy. Run from any working directory using the script path. Scripts resolve inputs and outputs relative to this directory and the enclosing repository. Set OPENBLAS_NUM_THREADS=1 for repeatable resource use. Output-generating scripts overwrite only their corresponding JSON in this directory. Existing repository inputs are read-only.

- `python verify_subset_certificate.py`: independent exact verification of the saved certificate, including all 254 subsets, witness membership in [-1,1], exact rational inequalities, full-set Sturm positivity, and fractional half-mass feasibility. No floating roots are used.
- `python subset_certificate.py`: regenerate the certificate using floating roots only to propose exact rational witnesses, then verify exact inequalities. Independently run the verifier above afterward.
- `python double_neighborhood_taper.py`: regenerate the three E99c samples and FFT-based W2/interval Rayleigh evaluations. Reads the repository file [examples/e99/e99c.jsonl](../../../examples/e99/e99c.jsonl). Seed and full generation order are retained.
- `python verify_double_bitsets.py`: independently compute W2 membership using arbitrary-precision bitsets. This is exact combinatorics; Rayleigh values in the preceding script are floating point, not interval-certified.
- `python root_double_moments.py`: floating evaluation of the fixed-degree moment formula and generalized eigenvalues; not an exact numerical certificate.
- `python adversarial_w2_lifts.py`: finite centered/random Jedwab–Li and quadric lift tests. Extracts only the `jl_set` function from [src/e114_cp_group.py](../../../src/e114_cp_group.py). The recorded 18 cases and residuals are numerical evidence only, not a universal theorem or proof of absence of counterexamples.
- `order_test.py`, `order_test2.py`, `krylov.py`, and `matrix_controls.py`: historical exhaustive/random odd-matrix and harmonic-vector tests. The spectral-energy candidate they initially supported was subsequently REFUTED analytically; do not infer an open conjecture from these older outputs.
- `check_neighborhood.py`, `anneal_neighborhood.py`, and `sphere_neighborhood.py`: first-neighborhood controls. Their small-case behavior does not override the E99c obstruction. The sphere script can require substantial dense-matrix memory.

The saved JSON files are source results, not all rerun during checkpointing. At checkpoint, both subset scripts were run successfully; all Python files parsed, all JSON files parsed, and `git diff --check` passed. The exact verifier independently checked all witnesses and the full-set polynomial. No new kernel/Lean verification is claimed.

## Scope of the numerical evidence

W2 = {0} union S union (S+S), S = A union (-A). The E99c family is handled analytically by interval filling of A-A plus the independent-rounding L1 argument localized to a finite principal section. Arbitrary selected or correlated Boolean supports need not have either ingredient. The axes repair and root-difference parity repair are model-specific. The root moment enhancement is an existing higher-moment mechanism localized to W2. These results keep actual research open rather than declaring completion.

See [manifest.json](manifest.json) for source names, source hashes, checkpoint paths and checkpoint hashes. Absolute scratch paths and coordination text were removed for portable mathematical use.

## Extended checkpoint: W2 campaign and analytic deductions

The source campaign's finite searches are complete, but the general research remains active. Neither a universal positive W2 constant nor a Chowla bound has been established. The sharp local inequality K_W2 >= sqrt(|S|/2) is now rigorously refuted, which does not refute an unspecified positive constant.

- [Full W2 adversarial tests and restricted graph-certificate obstructions](../../notes/cstar_w2_universal_2026-10-20.md): all 65,535 nonempty supports in [1,16], seeded fixed/variable-cardinality searches, and the exact 50-frequency counterexample. Exploratory eigensolver outputs remain numerical.
- [W2 dual identities, strict enlargement and weak effective gap](../../notes/cstar_w2_dual_2026-10-20.md): doubled-maximum compression, its positive exterior-cost obstruction, partial translations, and strict finite-support leakage. The proved effective gap is far smaller than square-root scale.
- [Idempotent mixing and contact countercontrols](../../notes/cstar_idempotent_mixing_2026-10-20.md): absolute L1 mixing tolerance cannot bound energy, even with actual zero, evenness and nonnegative Fourier coefficients. Relative L2 defect and accumulated spectral error have different valid consequences. This is a non-Boolean countercontrol, not a Chowla counterexample.

### Exact local sharp-constant certificate

`w2_exact_certificate.py`, `.json` and `.log` preserve the original exact integer computation for 50 H + 353 I, where H is the adjacency on all 267 W2 rows. `verify_w2_exact_certificate.py` independently reconstructs W2 from the saved support, reverses row order, checks every fraction-free division and all 267 positive leading minors, and matches the saved determinant. It passed in approximately 5.2 seconds; see `verify_w2_exact_certificate.log`. Thus K_W2 < 353/50 < sqrt(50) is exact, not an inference from the floating eigenvalue. The original generator selects a support from the existing repository N50 results; the independent verifier does not depend on that selection order.

### Additional reproduction files

- `w2_exhaustive.py`, `w2_exhaustive16.py`, `w2_anneal.py`, `w2_targeted.py`, `w2_warm.py`, `w2_variable.py`, and matching logs: full-W2 integer support membership with floating eigensolver exploration.
- `w2_operator.py`: common FFT/principal-section operator and Jedwab–Li constructor extraction. `product_fejer_w2.py`, `depth_w2.py`, `adversarial_w2_lifts.py` and corresponding JSON preserve product-Fejer and lifted finite-group tests.
- `root_shell_w2.py`, `d_root_w2.py` and JSON: structured root-shell tests.
- `taper_two_step_krylov.py` and JSON, `krylov_exhaust.py`: kernel-leakage/exterior-cost diagnostics, not universal bounds.
- `project_deleted_edges.py` and JSON: projected deleted-edge diagnostics on lifted finite-group examples. These are floating-point computations and do not supply an exact general certificate.

Large structured tests can require substantial memory. They were preserved, not all rerun during this checkpoint. Source hashes and per-file capture times are recorded in the updated manifest; earlier unchanged files retain their first snapshot hashes. Internal coordination and absolute scratch paths are omitted from copied notes and scripts.

[Near-realization and adaptive cross-Gram continuation](../../notes/cstar_w2_near_realization_2026-10-20.md) records the completed structured tests, an exact order-|S| deletion-operator obstruction for one-representative finite-group lifts, and an exact counterexample to inferring a square-root background-projection gain. It also records numerical two-vector repairs on the three E99c samples. Large deletion norm cannot be converted to a negative eigenvalue without additional information; the projection shortcut is refuted, not the full W2 conjecture.

## Positive model-specific theorem checkpoint, 05:56 UTC

[Product-Fejer W2 theorem](../../notes/cstar_product_fejer_asymptotic_2026-10-20.md), with [independent audit](../../notes/cstar_product_fejer_independent_audit_2026-10-20.md): for independent symmetric Bernoulli rounding of the product profile on U=[-2,2]^d, put v=3^d-(19/9)^d. Then

    P(K_W2 >= 1+sqrt(v)/6)
      >= 1 - 5^d exp(-((10/9)^d-3)/6) - 12/sqrt(v) - 728/v.

The failure bound tends to zero; it need not be useful in small dimensions. This excludes that particular family as an asymptotic W2 counterexample and transfers exactly to base-11 integer encodings. It is a proved model-specific result, not a universal Chowla or W2 advance. The general positive-definite rounding lemma uses six-wise independence for its spectral moments; support filling is a separate hypothesis. Its exponential sufficient filling estimate requires full independence.

`audit_product_fejer.py` and its local `.log` verify the cubic coefficients and all filling graphs exactly in dimensions 1–3. The general proof and constants were independently audited; the finite script is a reproducible check, not a replacement for that proof. At this checkpoint the script was rerun successfully. `verify_parity_moments.py` was also rerun for all four dimension-one and 4096 dimension-two symmetric subsets; its rounded-FFT qualification is retained.

Additional stable notes:
- [Integral-SOS and cancellation-free positive-factor rank cases](../../notes/cstar_rank_positive_polynomial_2026-10-20.md), with an exact small obstruction to a general integral-SOS bridge. No universal factorization or rank conclusion is asserted.
- [Residue-fiber centering](../../notes/cstar_alias_centering_2026-10-20.md), including the exact refutation of the proposed positive-spectrum cap.
- [Alias-mode numerical results and abstract matching countermodel](../../notes/cstar_alias_modes_results_2026-10-20.md), with `alias_modes.py/json` and `alias_signed_energy.py/json`. The two-copy countermodel is not an actual integer W2 graph.
- [Exact parity mixed-moment formulas](../../notes/cstar_parity_mixed_moments_2026-10-20.md), with `parity_mixed_expectation.py/json`, `verify_parity_moments.py/json`, and `product_fejer_d6.py/json`. The failed parity expectation shortcut is superseded for this model by the positive theorem above; it is not a refutation of W2.

Further positive-definite profile work remains active outside this stable snapshot. No unfinished result is promoted to a theorem, and no ongoing research task is marked complete.

## Consolidated synthesis and deterministic-profile checkpoint

[Self-contained research synthesis](../../notes/cstar_research_checkpoint_2026-10-20.md) summarizes the exact extremizer reduction, sharp local counterexample, audited product-Fejer proof, approximate-idempotence countercontrols and remaining universal gap. It includes a compact numerical profile table with explicit normalization and qualifications.

[Deterministic positive-profile fitting](../../notes/cstar_profile_certificate_2026-10-20.md) is recorded with `profile_certificate.py/results.json/.log`, `profile_two_fejer.py/results.json/.log`, and the base-5 and base-7 root-difference result/log files. These are numerical Rayleigh and eigensolver evaluations, not interval-certified bounds; base-7 checks agree with the displayed root-control values. The reproducible source names and hashes are in the manifest. The separate positive-factor branch is not declared complete by this synthesis.

## Final targeted archival follow-on, 06:12 UTC

The delivered [main synthesis](../../notes/cstar_research_checkpoint_2026-10-20.md) is preserved byte-for-byte as **version 0**, SHA-256 `02f83e2e222ba412c4919ca25ab66d3e921842f0098c3a856aa4e4394c2ab209`. Later findings are recorded in a [separate short addendum](../../notes/cstar_research_addendum_2026-10-20.md), not silently inserted into that report.

- [Order-profile asymptotic obstruction](../../notes/cstar_order_profile_asymptotic_2026-10-20.md), with [independent audit](../../notes/cstar_order_profile_asymptotic_independent_audit_2026-10-20.md): the fixed span {1,D,|F_A|²/|A|-1} has K_3=(21630/241+o_p(1))n^(1/3) under the stated E99c-type taper. This rigorously refutes a universal square-root guarantee for that restricted profile space, not full W2, adaptive profiling or Chowla. Finite samples through 100,000 still have K_3/sqrt(2|A|) near 0.93; no observed collapse is claimed. `order_profile_asymptotic.py`, `_results.json`, `.log` preserve those samples. `audit_order_profile_asymptotic.py` independently computes the exact shape integrals and constant; its successful archival rerun is saved in `.log`.
- [Variable central mass, §7.1](../../notes/cstar_product_fejer_asymptotic_2026-10-20.md): p_0=h gives spectral threshold h+sqrt(v)/6 and failure 12h/sqrt(v)+728/v, with filling separate. The original product theorem is unchanged. Six-wise spectral independence must not be confused with the full independence used for exponential filling.
- [Positive-factor endpoint energy](../../notes/cstar_positive_factor_energy_2026-10-20.md), with `positive_factor_search.py/json`: an exact E<1 inequality, small-support consequences, and a central-binomial obstruction to an endpoint-only extension. The nonlinear search is local numerical optimization, not exhaustive certification; the outer-lag countercontrol has fractional other lags and is not a Boolean counterexample.

This archives the requested targeted follow-on without declaring the universal problem solved or all research directions exhausted. No PDF, commit or push was created.
