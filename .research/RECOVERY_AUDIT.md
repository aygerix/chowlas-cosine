# Documentation and recovery audit

Audit date: 20 October 2026. Scope: the recovered `.research` delivery files.
This is a documentation, provenance, coverage and static-reproducibility audit;
it is **not** a new independent proof of every mathematical result.

## Verdict

The four recovered archive groups have substantive text reports and supporting
materials in appropriate locations. In particular, the groundstate-repair and
coupled-mode passes are present under `notes/`, with their proofs, independent
audits, scripts and captured data under separate `experiments/` directories.
The [recovery index](RECOVERY_INDEX.md) makes those relationships explicit.

The public Git repository and history were subsequently restored through
`3873843090179751cb8732f5c0e9dcd21c1188bc`, including public ancestor
`dfd51a19d0b094850f451d1cc82c88880be77b17`. Original public indices, `src/` and
`examples/` are present, resolving the initially identified historical input
and link gaps. The original public index content is preserved, with dated
supplements in STATE, CSTAR, PROOFS, ROUTES, NOTEBOOK and EXPERIMENTS.

It would still be inaccurate to claim recovery of every local historical
version. The unpublished object `446367d948fedba07c5e70e3fdf9d9fcd106b08b` is not
available, and original early Markdown/data cannot be recreated from PDFs.
These distinctions do not affect the retained completed-pass reports.

## 1. Coverage of the recovered completed passes

| Pass | Documentation and evidence present | Scope qualifications preserved |
| --- | --- | --- |
| Structural campaign and targeted addendum | 23 notes/supplements; reproduction README; Python, JSON and logs; exact subset and sharp-W2 certificate verifiers; product-Fejér and order-profile proof audits | Numerical searches are not universal proofs; sharp-constant failure does not refute every positive constant; non-Boolean countercontrols are labeled; historical public inputs are restored |
| Focused full-W2 falsification | [Main report](notes/cstar_full_w2_falsification_2026-10-20.md); analytic proofs; multiscale and correlated reports; [independent audit](experiments/full_w2_falsification_2026-10-20/audit.md); scripts, captured outputs and 84 support exports | No vanishing-ratio full-W2 family was found; exclusions concern stated subclasses only; residuals and FFT checks are numerical |
| Groundstate repair | [Main report](notes/cstar_groundstate_repair_2026-10-20.md); full-cost derivation; balanced-layer/implant and taper proofs; independent audits; finite scripts and outputs; README and validation record | Bottom-mode repair obstruction is not a full-W2 counterexample; translated and odd spaces are complementary, not nested; finite-r 1/22 theorem is distinct from floating Laguerre diagnostics |
| Coupled mode | [Main report](notes/cstar_coupled_mode_2026-10-20.md); axis-union proof and centered companion; three independent audits; optional root-orbit/bouquet work; exact finite checks and numerical diagnostics; README, validation and manifest | Main theorem uses the enhanced five-condition joint selection; seeded FFT samples are not that selected family; root-orbit obstruction is not a weak-W1 example; universal mixed-mode estimate remains unproved |

The four archives do not claim to contain every investigation ever performed.
An unfinished computation or superseded preliminary draft is not a missing
completed theorem merely because the archive explicitly excludes it.

### Latest two passes: traceability

Groundstate repair:

- [Main obstruction proof](experiments/groundstate_repair_2026-10-20/schur/groundstate_product_no_amplification.md)
  and [independent audit](experiments/groundstate_repair_2026-10-20/audit/groundstate_product_obstruction_audit.md).
- [Balanced-layer full-W2 certificate](experiments/groundstate_repair_2026-10-20/translation/balanced_layers_full_w2_certificate.md)
  and [independent finite-r audit](experiments/groundstate_repair_2026-10-20/audit/balanced_layers_full_w2_audit.md).
- [Taper weak-W1 proof](experiments/groundstate_repair_2026-10-20/obstructions/weak_w1_taper_proof.md)
  and [independent audit](experiments/groundstate_repair_2026-10-20/audit/weak_w1_taper_audit.md).
- [Odd-sector qualification](experiments/groundstate_repair_2026-10-20/translation/interval_implant_odd_sector_audit.md),
  [numerical results](experiments/groundstate_repair_2026-10-20/obstructions/RESULTS.md)
  and [archive-time validation](experiments/groundstate_repair_2026-10-20/VALIDATION.md).

Coupled mode:

- [Axis-union proof](experiments/coupled_mode_2026-10-20/exterior/exterior_counterfamily.md)
  and [independent exterior audit](experiments/coupled_mode_2026-10-20/audit/EXTERIOR_AXIS_UNION_AUDIT.md).
- [Same-family full-W2 companion](experiments/coupled_mode_2026-10-20/order/direct_union_order_audit.md)
  and [independent full-W2/localization audit](experiments/coupled_mode_2026-10-20/audit/FULL_W2_COMPANION_AUDIT.md).
- [Optional root-orbit obstruction](experiments/coupled_mode_2026-10-20/multimode/root_orbit_low_cost_obstruction.md)
  and [independent auxiliary audit](experiments/coupled_mode_2026-10-20/audit/AUXILIARY_ROOT_ORBIT_AUDIT.md).
- [Reproduction commands and content map](experiments/coupled_mode_2026-10-20/README.md)
  and [archive-time validation](experiments/coupled_mode_2026-10-20/VALIDATION.md).

## 2. Checks actually performed for this recovery audit

The following inventory describes the 312 recovered files present before this
audit's new documentation and any separate early-PDF text recovery were added:

- 26 main notes/supplements.
- 80 files in the structural experiment directory.
- 138 files in the full-W2 falsification directory.
- 41 files in the groundstate-repair directory.
- 27 files in the coupled-mode directory.
- By extension: 58 Markdown files, 78 Python files, 147 JSON files, 28 logs and
  one JSONL file.

All 78 Python files passed in-memory Python compilation. All 147 JSON files
parsed successfully, as did all 84 nonempty records in the JSONL file. These
are syntax/data-format checks, not execution, import-dependency or numerical
correctness checks.

Before portability edits, all 313 archived-file SHA-256 declarations found in the four manifests matched
the recovered bytes, covering 304 distinct files. This includes main
`files` arrays, verification/output arrays, synthesis/addendum entries,
generated-file entries and the coupled report entry. Duplicate declarations
were checked too. The per-manifest declaration counts were:

| Manifest | Matching archived digest declarations |
| --- | ---: |
| Structural | 108 |
| Full-W2 falsification | 138 |
| Groundstate repair | 40 |
| Coupled mode | 27 |

Original `source_sha256` values were not treated as hashes of adapted archive
copies: the unavailable source versions cannot be independently verified here.
The four manifests themselves, the structural README, two earlier boundary/
cyclotomic notes and the groundstate main report have no individual archived
digest declaration in those four manifests. Their absence from those digest
lists is not evidence that they are absent from the recovered tree.

The initial Markdown path check found 106 actual relative file-link
occurrences in the 312-file archive collection. Two initially unresolved links
were to `examples/e99/e99c.jsonl` and `src/e114_cp_group.py`; both now resolve
after restoration of the public repository. Two additional regex matches in
indented mathematical expressions, `1_[u,u+X](t)`, are not document links.
The latest two main reports and their experiment documentation have no
unresolved relative file links. All new ledger/recovery links were checked;
no missing source was replaced with an invented link. The final archived-hash
check again passed all 313 current declarations after the two documented path
edits; all 78 archived Python files still compile. Importing the profile helper
confirmed that its new root resolves to the repository.

A broader scan of the restored public history also found old machine-specific
absolute links in `.research/agents/*final*.md` and one unresolved relative
link to `.research/agents/tdense18_scratch/final_audit.json` in
`tdense18_report.md`. Those older public summaries were not rewritten in this
limited recovery. Thus this audit does not claim every historical link or
scratch artifact in the entire public project is complete or portable.

The archived `VALIDATION.md` files describe checks executed at original
packaging time. In addition, this recovery actually reran eight representative
scripts in a disposable copy, all with exit code 0:

1. `cstar_structural_2026-10-20/verify_w2_exact_certificate.py`.
2. `cstar_structural_2026-10-20/verify_subset_certificate.py`.
3. `cstar_structural_2026-10-20/audit_product_fejer.py`.
4. `cstar_structural_2026-10-20/audit_order_profile_asymptotic.py`.
5. `full_w2_falsification_2026-10-20/audit_checks.py`.
6. `groundstate_repair_2026-10-20/audit/check_groundstate_obstruction.py`.
7. `coupled_mode_2026-10-20/audit/check_axis_union.py`.
8. `coupled_mode_2026-10-20/order/verify_direct_union.py`.

All paths in this list are relative to `experiments/`. Execution results and
stdout/stderr are retained in the [recovery validation record](validation/recovery_2026-10-20/README.md)
and [machine-readable results](validation/recovery_2026-10-20/results.json).
Captured archive outputs were not overwritten. These reruns validate the
assertions actually implemented, not every paper argument or a universal
conjecture. Large sweeps and every historical experiment were not rerun.

## 3. Recovered public context versus unavailable local history

The public repository supplies the original `STATE.md`, `CSTAR.md`, `PROOFS.md`,
`ROUTES.md`, `NOTEBOOK.md` and `EXPERIMENTS.md`, plus its source, examples and
other tracked research files. The recovered completed-pass archives were
integrated without a differing-content collision with the public baseline.
The new dated ledger supplements preserve the earlier contents and P/E
numbering while putting current outcomes and remaining questions up front.
Historical job-status statements below those supplements do not mean those
jobs are presently running.

The exact unpublished local commit named in an early handoff was not recovered.
Nor was the exact source Markdown for `negative_sublevels_2026-10-20.md` and
`negative_sublevels_2026-10-20_appendix.md`. The two surviving PDFs instead supply
[clearly labeled historical transcriptions](notes/recovered_early/README.md),
with source hashes, page boundaries and extraction caveats. The L1 strengthening
is present on handoff source page 6. The transcriptions are not replacements for
the original files, charts, full numerical data, or commit identities.

Generic old references such as `joint_boundary`/“prior boundary note” are not
specific enough to establish an exact original target; no destination or
numbered statement is invented for them. The public P/O/E ledger can now be
consulted directly, but unpublished later changes to that ledger remain unknown.

## 4. Historical inputs restored and path-only portability fixes

Every concrete missing input found in the initial archive-only audit is now
present in the restored public repository:

- `examples/e99/e99c.jsonl`.
- `src/e114_cp_group.py`.
- `examples/dense_runs/X30_s0.json`.
- `examples/construct/N50_certified.json`.
- `src/e99c_tapered.py` and `src/e99_selfgraph.py`.

This resolves the input gap in `double_neighborhood_taper.py`,
`adversarial_w2_lifts.py`, `w2_operator.py` and its importers, the N50 generator
and warm/variable searches, and the profile scripts. It establishes file
availability, not a promise that all long computations have been rerun.

Two unambiguous path-only edits were made in the structural archive:

- `profile_certificate.py`: `ROOT` now uses the already-defined script-relative
  `REPO` rather than `/workspace/shared/chowlas-cosine/`.
- `profile_two_fejer.py`: its helper search path now uses `HERE` rather than
  `/workspace/shared/cstar-active`.

Their original `source_sha256` values remain untouched. The structural manifest
records each prior archived hash as `pre_recovery_checkpoint_sha256`, the new
archived hash, and the specific recovery adaptation. No mathematical formula,
solver, parameter, seed, or captured result was changed. All other delivered
reports/proofs/scripts/data retain their original recovered bytes. Statements
about absent Git indices or “no commit” inside the original delivery prose are
historical packaging statements, not a claim about the final combined recovery.

## 5. Deliberate exclusions and numerical boundaries

- The full-W2 falsification archive deliberately omits 84 binary NPZ caches
  and their eigenvectors. It retains text support exports, sizes, numerical
  values and hashes, plus code to reconstruct the row sets/operators. This is
  a documented delivery choice, not a claim that the binary caches were recovered.
- The groundstate pass records an interrupted beta=.45 target-8192 translated
  solve after groundstate diagnostics. It does not claim a completed translated
  certificate for that run.
- The coupled pass deliberately excludes the superseded `AXIS_UNION_PARTIAL.md`,
  an unfinished finite search and duplicate preliminary material. Its three
  minimal prior dependencies are explicitly labeled.
- Finite exact matrix/set assertions, paper proofs, independent paper audits,
  floating eigenvalue output, residuals and FFT rounding checks retain distinct
  statuses. None is relabeled as formal or interval-arithmetic certification.
- The universal full-W2 and Chowla conclusions remain unproved. The latest
  restricted obstructions and special-family positive certificates do not
  change that status.

## 6. Remaining limits and safe description

The full public history is retained and the documented completed passes are
integrated, cross-indexed and supported by proof/audit/script/data files.
Import guidance is in [BUNDLE_IMPORT](BUNDLE_IMPORT.md). No remote push was
performed as part of this documentation work.

To recover the exact old local state, obtain the unpublished commit/object
`446367d948fedba07c5e70e3fdf9d9fcd106b08b` or the original local repository, plus
any early source Markdown/data not present in public history or delivered
archives. Reconcile those originals with existing P/E/O records before claiming
that every historical file or local revision survived.

The accurate description is: **restored public repository history plus the
recovered completed research passes and explicitly labeled early report text,
with current ledgers and documented limitations**. It is not an invented
replacement for the unrecovered local commit, not recovery of every omitted
binary cache, and not a solution of the universal problem.
