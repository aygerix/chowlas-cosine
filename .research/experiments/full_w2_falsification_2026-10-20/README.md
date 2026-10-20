# Full-W2 falsification: reproducible text/code checkpoint

Captured 20 October 2026 at 06:39:39 UTC, after the independent audit and final bounded comparison were stable. This is a separate focused pass. Prior delivered reports and the prior ZIP are unchanged. Local-only: no PDF, commit or remote push.

Start with [the concise result note](../../notes/cstar_full_w2_falsification_2026-10-20.md) and [independent audit](audit.md). No vanishing K_W2/sqrt(N) family was found. Rigorous exclusions apply only to the stated tensor, axis, fixed-orbit and exact-fiber classes. Finite correlated-lift and rounding curves are not asymptotic theorems.

## Layout

- `analytic/`: full-operator tensor identities, axis-interval proof, and the final 18-case T=S+S versus W2 diagnostic.
- `multiscale/`: report, 84 full-matrix records, rounding/cluster constructors, direct sparse verification and interval-fiber checks.
- `correlated/`: residue-balanced lifts, histogram-preserving optimization, Singer differences and cuts, collapsed differences, exact bitset checks and dense validation.
- `audit.md`, `audit_checks.py/json`: independent algebraic/methodological review and separate finite checks.
- `manifest.json`: source hashes, capture time, copied-file hashes and support-export provenance.

The historical raw `rho` field in multiscale JSON means N/K^2, NOT the Perron eigenvalue called rho in the analytic proofs. Use actual N=2|A| throughout. K is for the symmetric exponential sum D=2f_A, not the cosine minimum M=K/2.

## Text support export instead of binary caches

All 84 original multiscale NPZ caches are omitted from this text/code checkpoint. Their exact positive support lists A, numerical K, W2 sizes and SHA-256 hashes of the original sorted W2 arrays are exported under `multiscale/supports/`. Original NPZ hashes are retained for provenance. Eigenvectors are omitted.

`multiscale/support_io.py` reconstructs W2 by exact integer pair sums and checks its stored cardinality/hash. `verify_sparse.py` now reads this JSON-based reconstruction instead of a binary cache. This is an archival input adaptation only; it uses the same support, matrix assembly and solver. The constructors can regenerate full operators and eigenvectors from these inputs. Rerunning `search.py` still writes fresh NPZ numerical caches locally; those generated binary files are not part of the archive.

At archival time, exact text reconstruction/hash checks were rerun for `dyadic_extended_J8`, `tri_cumulative_32`, and `symmetric_blowup_h0`. All passed. The independent `audit_checks.py` was also rerun successfully. The expensive full sparse eigensolve and all 84 searches were not rerun solely for packaging.

## Reproduction

Python with NumPy and SciPy is sufficient. No proprietary solver or external account is needed. Paths are resolved from the scripts, rather than the original machine. Run scripts in their own subdirectories or by full path. Use OPENBLAS_NUM_THREADS=1 to limit resource use.

Small independent audit:

    OPENBLAS_NUM_THREADS=1 python audit_checks.py

Exact correlated support verification:

    OPENBLAS_NUM_THREADS=1 python correlated/check_supports.py

The latter overwrites its own `support_checks.json` with the rerun. Other search scripts likewise regenerate output files, and multiscale `search.py` appends to `results.jsonl`; preserve originals or work in a copy. Some original logs were captured from command-line batch variants, so consult report descriptions and saved parameters before rerunning entire batches.

The sparse J8 validation has 21,587 rows and 7,695,116 nonzeros. The largest saved full-W2 run has 234,073 rows. Larger searches can need significant memory; start with the audit, not all scripts at once.

## What is certified and what is numerical

The subclass exclusions are paper proofs, independently audited. Integer set identities and bitset checks are exact. FFT rounding gaps and floating eigensolver residuals are numerical diagnostics, not interval certificates. A small residual does not prove that no lower eigenvalue was missed. The full operators, rather than a fixed trial space or a Fourier grid minimum, were used in the searches; this distinction does not turn their outputs into rigorous spectral upper bounds.

The source audit corrected two wording issues before this snapshot: the overlap maximum residual is below 6e-8, not 5e-8, and the FFT rounding comment is explicitly numerical. The archived sources include these corrections. No universal Chowla or W2 conclusion is asserted.
