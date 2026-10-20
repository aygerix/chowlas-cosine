# Groundstate repair: reproducible text/code checkpoint

20 October 2026. Start with the [result report](../../notes/cstar_groundstate_repair_2026-10-20.md). Only this completed proof attempt is archived here; prior research files are not replaced. No PDF, commit or remote push.

## Exact conclusion

Explicit balanced-layer supports have weak W1. An interval implant gives a unique bottom vector whose translated trial space is weak, and separately whose entire coupled odd W2 sector is weak. Yet the same implanted family has a square-root full-W2 certificate from independent even directions: K_W2(S)>=sqrt(|T|)/22 and |S|/|T|->1. The base finite-r theorem holds for k>=1, r>=4k^2. All these statements, and the separate random tapered weak-W1 theorem, passed independent paper-proof audit. This is not formal verification or a literature-priority claim.

This refutes universal single-bottom-mode repair, not full W2, all-mode Schur or Chowla. The remaining universal multimode/adaptive certificate is unproved. The odd and translated spaces are complementary, not nested; historical wording suggesting containment is superseded by the odd-sector audit.

## Files

- `schur/`: full-cost translated compression and main interval-implant/balanced-layer proof; finite implant check.
- `translation/`: independent layer and odd-sector checks; exact two-layer full-W2 theorem; partial-translation gap; integer Laguerre diagnostic.
- `obstructions/`: three-color tapered proof, numerical translated-space/controls data and scripts, exact small energy counterexample.
- `audit/`: independent main proof, taper and finite-r full-W2 audits, with finite check data/scripts. In particular `balanced_layers_full_w2_audit.md` records the final PASS on the 1/22 theorem and implant transfer.
- `inputs/singer_results.json`: small text input needed by the numerical controls script.
- `manifest.json`: original-source and archived SHA-256 hashes. Scripts use script-relative paths instead of machine-specific absolute paths; copied prose removes coordination attribution and updates the proved weak-W1 premise. No solver or mathematical changes were made.

## Reproduction

Python 3 with NumPy, SciPy and SymPy. Run from this directory or invoke scripts by path; outputs go beside the scripts and overwrite the corresponding reproduced JSON. For preserving the captured outputs, rerun in a copy.

Small independent checks:

    OPENBLAS_NUM_THREADS=1 python audit/check_groundstate_obstruction.py
    OPENBLAS_NUM_THREADS=1 python translation/balanced_sign_weak_w1_check.py
    OPENBLAS_NUM_THREADS=1 python obstructions/exact_groundstate_energy.py
    OPENBLAS_NUM_THREADS=1 python obstructions/verify_translated.py
    OPENBLAS_NUM_THREADS=1 python translation/laguerre_full_w2_diagnostic.py

`schur/check_interval_implant.py` and `obstructions/implant_check.py` run additional finite numerical controls. The `translated_kernel*` scripts reproduce progressively larger dense or FFT experiments, potentially expensive. `test_leakage.py` exhausts small supports and is not needed to prove the main theorem. The beta=.45 target-8192 translated solve was interrupted after groundstate diagnostics; the supplied JSON contains only completed records, and rerunning its script attempts both targets.

Archive-time validation is recorded in `VALIDATION.md`. Small checks validate identities and implementation; the asymptotic and uniform conclusions rest on the paper proofs. Floating-point eigensolver outputs, including Laguerre minima, are not certified spectral enclosures.
