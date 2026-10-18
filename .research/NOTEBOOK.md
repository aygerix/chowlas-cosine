# NOTEBOOK (dated)

## 2026-10-17 Session 1 — orientation and first derivations
- Built evaluators E1/E2/E3; reproduced Sidon-difference identity (R -> 1/sqrt2).
- Read Bu et al. (1/2), Bedert v3 (1/5), Shankar (log-free 1/5), JMTZ (1/10). Summaries in LITERATURE.md.
- Derived reformulations P1–P3 (Fejér–Riesz / probabilistic / projection). Key consequence: R -> 0 iff the FR factor Q
  has M4/M2^2 -> infinity while |Q|^2 has flat {0,1/2} off-zero coefficients: "flat autocorrelation + heavy tail".
- Multiplicity analysis: in one square, bulk multiplicity m gives R ≈ 1/sqrt(2m). Symmetry caps m at 2 (P4).
  Products/sumsets B=S+C give multiplicity r_C(e) inherited from C (recursion, no gain). A_{k-1} roots give bulk m=4
  but a heavy structured defect (type (1,-1), coefficient ~4k along P itself); completing the square doubles the
  diagonal -> R -> 1/sqrt2. Weighted (conference-matrix) fixes force |sum c|^2 <= k lambda: kills the gain.
- Gaussian-chaos heuristic H1: set-ness = Wick ordering; only He_2 has a hard floor with good ratio; z^4-3 (R=0.2165)
  needs amplified lower chaos (multiplicities ~ block size) — impossible for sets. 1/2 barrier explained heuristically.
- Escapes from H1: (E1) bounded-size blocks (exact trigonometric, cube framework P7); (E2) arithmetic correlations
  (Fejér/AP structure gives heavy tails, as Bu's majorant does); (E3) chaos degree growing with N.
- Lower-bound side: P6 (energy/third moment) — sum-free => R >= 1/sqrt2; R -> 0 forces E(A)/N^2 -> inf.
