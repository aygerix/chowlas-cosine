# Recovered research index

Recovery documented on 20 October 2026. This is a new navigation aid for the
recovered materials, **not** a reconstruction of the original research indices
or Git history.

## Read this first

The recovered completed passes are documented in the appropriate
`.research/notes/` and `.research/experiments/` locations. The latest two passes
include their main reports, paper proofs, independent audits, reproduction
scripts and captured results.

The public repository and its history have now been restored through commit
`3873843090179751cb8732f5c0e9dcd21c1188bc`, including the earlier public baseline
`dfd51a19d0b094850f451d1cc82c88880be77b17`. The original public research indices,
`src/` and `examples/` are present. The six persistent ledgers have dated
source-linked updates: [STATE](STATE.md), [CSTAR](archive/handoffs-2026-10-23/CSTAR.md), [PROOFS](PROOFS.md),
[ROUTES](ROUTES.md), [NOTEBOOK](archive/handoffs-2026-10-23/NOTEBOOK.md) and [EXPERIMENTS](EXPERIMENTS.md).

This does **not** recover the unpublished local Git object
`446367d948fedba07c5e70e3fdf9d9fcd106b08b`, or establish that every uncommitted
historical file survived. Some early reports are available only as explicitly
labeled PDF-derived text. See the [recovery audit](RECOVERY_AUDIT.md) for the
exact coverage and remaining limitations, and [bundle import instructions](BUNDLE_IMPORT.md)
for safe use of the full-history bundle.

## Current mathematical status

Start with the [latest coupled-mode report](notes/cstar_coupled_mode_2026-10-20.md).
It proves, for one specially constructed Boolean integer-support family, that
the first-neighborhood, exterior-only and center-deleted full-W2 certificates
are all weak while the full coupled W2 certificate has normalized limit one.
Its [main proof](experiments/coupled_mode_2026-10-20/exterior/exterior_counterfamily.md),
[same-family companion](experiments/coupled_mode_2026-10-20/order/direct_union_order_audit.md)
and [independent audit](experiments/coupled_mode_2026-10-20/audit/FULL_W2_COMPANION_AUDIT.md)
are retained.

The [preceding groundstate-repair report](notes/cstar_groundstate_repair_2026-10-20.md)
separates the failure of a prescribed bottom-mode repair from the survival of
a square-root full-W2 certificate on that particular adversarial family.

**The universal full-W2 square-root conjecture and the universal Chowla target
remain open in this work.** Failure of a restricted trial space is not a
counterexample to full W2 or Chowla. A successful special-family certificate is
not a universal proof. Floating eigenvalues and FFT diagnostics are not
certified spectral enclosures. The retained independent audits are paper-proof
and algebraic reviews, not formal proof-assistant verification.

## Recovered pass sequence

Times below come from the archived checkpoint/manifest metadata. They identify
the recovered snapshots, not original commits or an exhaustive project history.

| Recovered pass | Main report | Proofs, scripts, data and audit navigation |
| --- | --- | --- |
| Structural campaign, initially 05:32 UTC and extended through 06:12 UTC | [06:01 synthesis, preserved version 0](notes/cstar_research_checkpoint_2026-10-20.md) and [06:12 addendum](notes/cstar_research_addendum_2026-10-20.md) | [Structural reproduction index](experiments/cstar_structural_2026-10-20/README.md); public repository inputs restored |
| Focused full-W2 falsification pass, 06:39 UTC | [Result report](notes/cstar_full_w2_falsification_2026-10-20.md) | [Reproduction index](experiments/full_w2_falsification_2026-10-20/README.md) and [independent audit](experiments/full_w2_falsification_2026-10-20/audit.md) |
| Groundstate-repair pass, sealed 07:40 UTC | [Result report](notes/cstar_groundstate_repair_2026-10-20.md) | [Reproduction index](experiments/groundstate_repair_2026-10-20/README.md) and [archive-time validation](experiments/groundstate_repair_2026-10-20/VALIDATION.md) |
| Coupled-mode pass, sealed 14:19 UTC | [Latest result report](notes/cstar_coupled_mode_2026-10-20.md) | [Reproduction index](experiments/coupled_mode_2026-10-20/README.md) and [archive-time validation](experiments/coupled_mode_2026-10-20/VALIDATION.md) |

The later pass supersedes narrower proposed mechanisms; it does not erase the
earlier reports or turn their explicitly numerical findings into proofs.
Statements such as “no commit” or “this pass only” inside the archived reports
describe their original delivery scope, not any later recovery packaging.

## Earlier reports recovered from PDFs

The [early-report provenance index](notes/recovered_early/README.md) links full
readable transcriptions and page-delimited extraction records for the
[negative-sublevels report](notes/recovered_early/negative_sublevels_report_2026-10-20.recovered.md)
and [research handoff](notes/recovered_early/research_handoff_2026-10-20.recovered.md).
The handoff includes the advisor-attributed L1 strengthening on source page 6.
These are historical PDF-derived reconstructions, not original Markdown; chart
images and the complete original numerical arrays are not recovered from text.
The fixed-kernel/fractional-padding obstruction keeps its stated scope and must
not be confused with a universal Chowla theorem. Later reports control current
status.

## Structural-note directory

These links cover all 23 structural/supplementary note files, in addition to
the three later main reports linked above.

### Earlier boundary and arithmetic controls

- [Boolean boundary tests and the high-rank control](notes/cstar_boolean_boundary_tests_2026-10-20.md).
- [Growing-order cyclotomic and determinant test](notes/cstar_cyclotomic_determinants_2026-10-20.md).
- [Collective boundary optimization](notes/cstar_collective_boundary_2026-10-20.md).
- [Order-sensitive boundary matrices](notes/cstar_order_matrix_2026-10-20.md).
- [Second-neighborhood continuation](notes/cstar_double_neighborhood_2026-10-20.md).

### Extremizer reductions and local W2 tests

- [Fixed-cardinality attainment and record reduction](notes/cstar_extremizer_compactness_2026-10-20.md).
- [Hereditary ratio minimality and exact certificates](notes/cstar_subset_minimal_2026-10-20.md).
- [Sharp-constant counterexample and full-W2 searches](notes/cstar_w2_universal_2026-10-20.md).
- [Full-cost W2 dual identities and the remaining cost](notes/cstar_w2_dual_2026-10-20.md).
- [Near-realization, projection and cross-Gram tests](notes/cstar_w2_near_realization_2026-10-20.md).

### Positive profiles, restricted theorems and obstructions

- [Idempotent mixing and non-Boolean countercontrols](notes/cstar_idempotent_mixing_2026-10-20.md).
- [Product-Fejér theorem and general rounding lemma](notes/cstar_product_fejer_asymptotic_2026-10-20.md).
- [Independent product-Fejér audit](notes/cstar_product_fejer_independent_audit_2026-10-20.md).
- [Parity mixed moments](notes/cstar_parity_mixed_moments_2026-10-20.md).
- [Residue-fiber centering](notes/cstar_alias_centering_2026-10-20.md).
- [Alias-mode results and abstract countermodel](notes/cstar_alias_modes_results_2026-10-20.md).
- [Rank and positive-polynomial factorization cases](notes/cstar_rank_positive_polynomial_2026-10-20.md).
- [Single positive-factor endpoint energy](notes/cstar_positive_factor_energy_2026-10-20.md).
- [Deterministic profile numerical tests](notes/cstar_profile_certificate_2026-10-20.md).
- [Fixed order-profile asymptotic obstruction](notes/cstar_order_profile_asymptotic_2026-10-20.md).
- [Independent order-profile audit](notes/cstar_order_profile_asymptotic_independent_audit_2026-10-20.md).
- [Structural synthesis, version 0](notes/cstar_research_checkpoint_2026-10-20.md).
- [Separate later addendum](notes/cstar_research_addendum_2026-10-20.md).

## Provenance and reproduction

The four experiment directories retain their original delivery manifests:

- [Structural manifest](experiments/cstar_structural_2026-10-20/manifest.json).
- [Full-W2 falsification manifest](experiments/full_w2_falsification_2026-10-20/manifest.json).
- [Groundstate-repair manifest](experiments/groundstate_repair_2026-10-20/manifest.json).
- [Coupled-mode manifest](experiments/coupled_mode_2026-10-20/manifest.json).

These distinguish original source hashes from adapted archived-file hashes.
They do not recreate unavailable originals. Reproduction commands that write
results should be run in a disposable copy so the captured evidence is retained.
The [recovery audit](RECOVERY_AUDIT.md) records the checks performed on the
recovered files and the remaining coverage/portability gaps.
