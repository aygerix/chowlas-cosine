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

## 2026-10-17 Session 1 (cont.) — barrier analysis, cube ILP, boundary-lemma caveat
### EXP-1 cube framework (P7) solved exactly by ILP (src/cube_ilp.py, HiGHS)
- max W = sum_J 2^{|S|} s.t. min_eps g_J >= -C0. Optimal R_cube over k<=8, C0<=24 (k<=6: C0<=32): **0.8165** (J = triangle
  {12,13,23}); larger budgets get worse (K_n pairs -> 1; higher-degree sets -> >1).
- Verdict: dissociated base frequencies + vertex bound cannot approach 1/2, let alone 0. Bu's 1/2 needs the curve
  x -> (alpha_j x) to AVOID bad torus regions (torus version of Bu has R=1). KILLED as a route; lesson recorded.
### Flatness vs heavy tail (the central conflict, heuristic but sharp)
- R small <=> FR factor Q has M4/M2^2 = 1 + 1/(2R^2) large (heavy tail) while r_Q is FLAT ({0,1/2}).
- Heavy tails come from additive structure (AP/GAP/Fejér peaks); flatness forces Sidon-like rigidity.
- With nearly aligned phases r_Q ∝ multiplicity mu_B, so flatness needs |B ∩ (B+γ)| ∈ {0,m} for most γ.
  m=2 via reversal symmetry (Bu). m>=3: symmetry impossible (P4); sumsets S+C inherit r_C (recursion);
  A_{k-1}-root squares have bulk m=4 but k^2 "short" differences of multiplicity 2(k-2) whose required cancellation
  forces |P(0)|^2 <= 2k*lambda (computed: CC*+C*C diagonal => ||C1||^2+||C*1||^2 = 2 lambda), killing the gain;
  allowing those coefficients = 1/2 still gives |P(0)|^2 <= k(lambda + k^2/4) << lambda^2. Dead.
- Quarter-integer trick: Re(P)^4+Im(P)^4 = (3/4)|P|^4 + (1/4)Re(P^4) has integer frequencies for P in 1/4+Z, uniform
  bulk coefficient 6 on A_diff ∪ A_sum (R≈0.612 before defects) but the (1,-1) defect again forces completing the
  square -> worse. Gaussian model: :X^4:+:Y^4: -> R≈1.22. Dead.
- Gaussian-chaos counting argument (strengthens H1): to realize z^4-3 (R=0.2165) the He_2(z)-chaos (only ~k^2
  available frequencies) must carry 3/4 of the L^2 mass vs ~k^4 He_4 frequencies; with 0/1 coefficients mass ∝ count,
  so impossible; sparsifying the 4-sums turns them into orthogonal noise. Escapes need NON-GAUSSIAN typical
  behaviour from structured (non-generic) base sets while keeping A a set.
### Fractional-decomposition bound (dead end, recorded)
- 1_A = w + sum kappa_i 1_{B_i} gives M(A) <= M(w) + sum kappa_i M(B_i); with B_i ⊂ A, cost >= S/(2 sqrt N) where S is
  the square mass, so R->0 needs S << N and w almost {0,1}-valued: circular.
### Dithered-Fejér idea (dead end, recorded)
- Linear taper over length l << L still has Dirichlet-type min ≈ -cL (dVP kernel 2F_{2n}-F_n has min ≈ -0.4n);
  only the full Fejér taper gives O(1), whose rounding noise has variance >= L/24 = N/12 with FRACTIONAL coefficients,
  so it cannot be a Bu-type square (integer coefficients). Beatty dithering creates bumps of size L/(2 pi m) at
  x = 2 pi m theta with odd profile => negative lobes ~ -cL. Dead.
### EXP-3 boundary sets (src/boundary.py)
- max_t |B_t| / K^2 <= 0.47 on all families (dense Sidon ≈0.27, Bu-type ≈0.2, intervals ≈ 2K).
- CAVEAT (important): |B_t| <= C K^2 is IMPLIED by Chowla (|B_t| <= n), so it can only fail for Chowla-violating sets;
  the data are therefore uninformative about it. Still a meaningful intermediate target: with Shankar's averaging it
  gives K >> n^{1/3}.
- Derived (test vector on {±t} ∪ B_t ∪ -B_t): |B_t|^2 <= K (2 e(B_t) + K |B_t|), e = edges inside B_t in Cay(Z, A').
  So |B_t| <= K^2 + K * avgdeg_{B_t}; obstacle: B_t may be internally dense (Roth forces density >= 1/K anyway).
- Note: avg_{t in A'} |B_t| <= C K for all A would imply Chowla (via Shankar + Roth); for Sidon differences the
  average is Θ(K) (tight), so "average" and "max" differ by a factor ≈ K there.

### Bedert v3 Prop 7.3 bookkeeping (verified from arXiv HTML) and an averaging remark
- r_t = (1 - cos(2 pi t x + pi/4)) (f_t * f_t), f_t = 2(1+sin 2pi t x) F >= -4K, f̂_t(0)=0 => f_t*f_t >= -16K^2, r_t >= -32K^2;
  (38) |phi_t| <= psi_t + 32K^2.  X = ∫(psi_t + 32K^2)(H*H), H = |Q1|, ||H||_1 <= 4K, ||Q1||_2 <= |B|^{1/2}+O(K^2).
- Upper: X <= (4+1/sqrt2)||Q1||_2^2 + 32K^2 ||H||_1^2.  Lower: X >= (4+sqrt2)|B| - O(|B|^{1/2}||Q2||_2 + ||Q2||_2^2).
  K^4 sources: (a) 32K^2 * ||H||_1^2 <= 512 K^4;  (b) ||Q2||_2^2 << K^4.
- First-order multipliers W(tx) >= 0 cannot create the odd/even coefficient gap (|w_1| < w_0 for W >= 0 and the
  even coefficient at interior points of long t-progressions equals W(0) >= w_0), so at least one self-convolution
  (cost: one factor K in the one-sided error) is needed; rescaling G does not change the relative error.
- NEW (averaging over t ∈ A', as in Shankar): the T1*(e(t.)T2)-type parts of Q2 satisfy
  sum_{t∈A'} ||T1 * (e(t.)T2)||_2^2 <= ||T1||_2^2 ||T2||_2^2 <= n * K^2  (Parseval; ||T2||_2^2 <= ||T2||_inf ||T2||_1 <= K^2),
  i.e. average K^2 instead of K^4.  But (a) remains: on average one still needs avg_t ||1̂_{B_t}||_1^2 << K^{2-δ}
  to beat 1/5 by this route.  Open sub-question: is avg_{t∈A'} ||Q_{1,t}||_1^2 << K^{2-δ}?  (Sidon diffs: B_t
  ~ size K random-like => ||1̂_{B_t}||_1 ~ sqrt K: consistent with K, i.e. δ=1.)
### Exhaustive small-N optima (agent, interim): dense near-intervals inside [1,40], R_cert ≈ 0.61–0.64 for N=10..17
  (e.g. {1..11,15} R=0.6391; N=16: {1..8,10,11,13..17,21} R=0.6137). Different regime from Sidon/Bu. See E5.
### Dense regime heuristic
- A ⊂ [1,L] dense needs a positive-definite macroscopic density profile (no jumps: a 0/1 profile with a jump gives
  Dirichlet lobes ~ -cL; positive-definite profiles cannot have flat tops). Best simple profile = triangle; then the
  rounding noise has L^2-mass >= N/12 (1/6 of total). Gaussian noise => R ~ sqrt(log L) (bad); a noise with floor
  -sigma would give R ≈ 0.29, real-square-shaped noise R ≈ 0.20. Singer differences are the dense flat-profile
  (sharp cutoff!) example where structured antisymmetric noise E = sin(vx/2) * (odd poly) cancels Dirichlet lobes.
