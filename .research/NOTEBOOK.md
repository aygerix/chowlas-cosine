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
  -sigma would give R ≈ 0.29, real-square-shaped noise R ≈ 0.20. Singer differences are the dense TRIANGLE-profile
  (CORRECTED 2026-10-17: measured deciles 0.97,0.89,...,0.03 for q=101; NOT a sharp cutoff) example where structured antisymmetric noise E = sin(vx/2) * (odd poly) cancels Dirichlet lobes.

## 2026-10-17 (session 1, late) — dense regime data, gain identity, star lemma, conjecture C½
### Dense SA (src/dense_sa.py; toggle/swap SA over subsets of [1,X], free N, 4e5 iters) — arb-certified (E2)
| X | N | max | certified M <= | R <= |
|---|---|-----|----------------|------|
| 30 | 20 | 30 | 2.68817 | 0.6011 |
| 50 | 34 | 49 | 3.52350 | 0.6043 |
| 80 | 54 | 80 | 4.70460 | 0.6403 |
| 120 | 73 | 115 | 5.74899 | 0.6730 |
| 180 | 122 | 180 | 7.66634 | 0.6942 |
| 260 | 150 | 255 | 9.13501 | 0.7459 |
- Structure: interval [1, ~0.65X] with a few holes + sparse tail near t ≈ 2π/x1 (x1 = first Dirichlet lobe ≈ 4.49/L),
  e.g. N=34: [1,31]\{12,28} ∪ {40,42,45,49}. Tail elements resonate (cos(t x1) ≈ 1) with the first negative lobe.
- R grows with X under fixed SA budget (0.60 -> 0.75); budget-limited, not conclusive. Exact box MILP launched (below).
- Error diffusion of the Fejér profile is BAD (R = 1.1–2.4): first-order ΣΔ shapes the error to x ≈ π.
### Box MILP (src/box_ilp.py): maximise |A| s.t. A ⊂ [1,X], f_A >= -lam, cutting planes at violating x
- X=30, lam=2.7: optimal N=20, the SA set above, R = 0.6011 (exact box optimum for that lam, numerically verified).
### FR anatomy (src/fr_anatomy.py) and the gain identity
- For even f_A the minimum-phase factor is REAL. With Γ = Σ_{g≠0}|r(g)|^2 / Σ_{g≠0} w(g) and L = Σ|q|^4/λ^2:
  **Γ (1 - L) = N/(2λ^2) = 1/(2R^2)** for EVERY spectral factor (Γ, L depend on the factor; the product does not).
  So R < 1/2 iff every spectral factor has Γ(1-L) > 2 — P8 is the C–S step Γ <= μ̄. Min-phase factor of the N=20
  optimum: L = 0.35 (one spike q_X = 1.24), Γ = 2.13; the spike is an artefact of the root choice, not structure.
### Star / induced-subgraph lemma (P9, PROVED, elementary; the JMTZ framework at its simplest)
- For finite W ⊂ Z and v: W -> R, Σ_{u,w∈W} v_u v_w 1[u-w ∈ ±A] = ∫ 2 f_A |V|^2 >= -2M ||v||^2. Hence
  M(A) >= -λ_min(Cay(Z,±A)[W]) / 2. Corollaries: (i) I ⊂ ±A with (I-I) ∩ ±A = ∅ gives M >= sqrt|I|/2;
  (ii) a clique K and an independent I completely joined give M >~ sqrt(|K||I|)/2; (iii) Turán: M >= N/sqrt(S3 + 2N),
  S3 = #{(a,b,c) ∈ (±A)^3: a-b=c}. For Sidon differences (iii) gives only N^{1/4}; it is a localized third moment.
- Consequence for R -> 0 sets: every subset of ±A of size s >> M^2 has >= 2 s^{3/2} - 4Ms internal A-differences.
### CONJECTURE C½ (new working hypothesis; HEURISTIC + NUMERICAL evidence only)
  For every finite nonempty A ⊂ Z_{>0}:  M(A) >= sqrt(|A|)/2.  (Sharp: Bu et al. give R -> 1/2 from above.)
  Evidence: (a) exhaustive box optima N <= 17 (R >= 0.61); (b) SA / MILP dense optima N <= 150 (R >= 0.60);
  (c) certified Bu sets approach 1/2 from ABOVE, excess (M - k/2)/sqrt k ≈ 1.0–1.4 > 0; (d) P8: square certificates
  with support multiplicity <= 2 have R >= 1/2; (e) H1 Wick heuristic: degree-2 chaos optimum is exactly 1/2;
  (f) gain identity: R < 1/2 needs coherent multiplicity Γ(1-L) > 2 in every factor — never observed (max seen ≈1.39).
  Trivially true for N <= 4 (M >= 1 always: average f over x = (2j+1)π/max A).
  Falsification plan: any certified R < 1/2 at any N kills it (and would be a record). Implication: if C½ holds,
  Epoch's algorithm cannot exist and the lower-bound track is the correct direction; it does NOT by itself suggest a
  proof method (moments cannot give it: Bu ≈ centered chi-square, which moment constraints do not exclude).

## 2026-10-18 — landscape picture, multiplicity via consistent thinning, Hoffman/Motzkin remark
### Sidon lower-flatness (C½ on Sidon differences) — NUMERICAL
- R(D−D) < 1/2 ⟺ min_x |F_D|^2 > (1 − 1/√2)|D| ≈ 0.293|D|. SA over Sidon D: best min|F_D|^2/k = 0.103 (k=5), 0.096 (6),
  0.034 (8), 0.020 (10), 0.0041 (12), 0.0017 (16). Decreasing towards 0. P10 (B_3) / P11 (B_h) prove the dissociated case.
### Why dense optima are good at small N and (probably) not asymptotically (HEURISTIC)
- Dense A ⊂ [1,L]: low-x part of f is L·ρ̂(ξ) (profile ρ) and must be >= −c√L, so ρ̂ >= −c/√L: the positive-definiteness
  tolerance is LOOSE at small L (c/√L ≈ 0.1 at L=30), allowing near-0/1 profiles (interval + resonant tail, few
  rounding errors). As L grows the profile must become genuinely p.d. (cannot be flat-topped: |ρ(t+s)−ρ(t)|^2 <=
  2ρ(0)(ρ(0)−ρ(s))), forcing a constant fraction κ of rounding noise. Singer differences are the triangle-profile
  dense example with R = 1/√2. Expected: R_dense(N) rises from ≈0.60 (N≈20–34) towards ≈0.7, consistent with SA
  (0.64, 0.67, 0.69, 0.75 at N = 54, 73, 122, 150), while sparse Bu sets approach 1/2 from above only for N >~ 10^4.
  So the best known K(N)/√N is ≈0.6 at every scale tried, non-monotone in N; nothing points below 1/2.
### Multiplicity > 2 via consistent thinning — obstruction (HEURISTIC, extends P4 / Bu §8)
- Bu's thinning works because every A-frequency has ONE representation per symmetry orbit: Bernoulli thinning keeps
  coefficients in {0,1}. For multiplicity m >= 3 the m representations must survive/die together ("consistent
  thinning"), which needs a group of order m acting on the support and preserving differences: only translations and
  the reversal exist (P4). Translation copies S ∪ (S+t): within-copy classes get 2σ^2 and cross classes σ^2 (2:1);
  forcing cross classes to multiplicity 2 needs S−S ≈ invariant under 2t, i.e. a product S0 + T0, whose T0-diagonal
  classes have multiplicity |T0| (tent / diagonal dominates). Every such attempt reproduces the non-uniform diagonal.
### Hoffman / Motzkin / lonely-runner remark (PROVED, standard)
- Cay(Z_X, ±A) has λ_min >= −2M for every X > 2 max A, so Hoffman gives: every I ⊂ Z with (I−I) ∩ ±A = ∅ has upper
  density <= M/(N+M); equivalently M >= N μ(A)/(1 − μ(A)), μ(A) = Motzkin density of A-avoiding sets. Corollaries:
  if ||aθ|| >= δ for all a ∈ A (some θ) then M >= Nδ/(1−δ); if A has no multiple of q then M >= N/(q−1) (i.e. small-R
  sets contain >= (N − (q−1)M)/q multiples of q for every q). One-directional (intervals have μ = 1/(N+1)); no new
  general bound.
### C½ as a spectral statement (remark)
- Adjacency of the distance graph Cay(Z, ±A) has spectrum {2 f_A(x)}, degree d = 2N, λ_min = −2M. C½ ⟺ λ_min <= −sqrt(d/2)
  (1 − o(1)). Paley graphs (p ≡ 1 mod 4) have d = (p−1)/2, λ_min = −(1+√p)/2 ≈ −sqrt(d/2): Bu's constant 1/2 is exactly the
  conference-graph value. So C½ says "distance graphs on Z are never spectrally better than Paley graphs". In finite groups
  subgroups/complete graphs beat Paley (λ_min = −1), so any proof must use torsion-freeness (cf. P4), not only spectral
  graph theory; JMTZ (2509.03490) is the closest general-graph statement (cliques at |λ_min| <= d^γ, γ small).
### Finite cyclic analog beats 1/2 (E10) — what it teaches
- Cyclotomic classes H ⊂ Z_p^* of index m with aligned Gauss sums have nontrivial Fourier values ((m−1)√p, −√p,...)/m,
  giving grid-ratio 1/sqrt(2m) (verified 0.416, 0.368, 0.313 for m = 3, 4, 6). These are DENSE (d = p/m) and their
  Z-lifts fail: off-grid values are sinc-interpolations of pseudo-randomly arranged periods (size ~ sqrt(p/m)·sqrt(log)),
  and tapered multi-period lifts give coherent major-arc dips of size (X/q)·√q/m. Bu/Singer survive lifting only because
  the certificate (|F_D|^2 >= 0, ρ^2 − diag) is an identity on all of R, not a mod-p statement.
- Research question this isolates: is there a Gauss-sum-type phase alignment realizable by an R-identity (a square or
  sum of squares in the continuous variable)? Without it, C½ stands; with it, the cyclotomic 1/sqrt(2m) mechanism could
  give R -> 0 (Epoch direction).
### Distributional formulation of the frontier (HEURISTIC, organising principle)
- Let ν_A = law of f_A(x), x uniform on the circle: mean 0, variance N/2, min −M. Then R = M/sqrt N = β/(sqrt2 σ) with
  β = −min, σ = sd. Sidon differences: ν ≈ (k/2)(Exp(1) − 1) ⇒ R = 1/sqrt2. Bu: ν ≈ (k/2)(χ²_1 − 1) ⇒ R = 1/2. PSD
  degree-2 Gaussian chaos Σ λ_i (Z_i^2 − 1): R = Σλ_i/(2 sqrt(Σλ_i^2)) >= 1/2 (H1, rigorous in P12 for dissociated
  frequencies). Two-point law (−β w.p. 1−p, α−β w.p. p): R = sqrt(p/(2(1−p))) -> 0 as p -> 0; this is what aligned
  cyclotomic periods realise in Z_p (E10: p = 1/m). Non-Wick quartics such as (Z^2−1)^2 − 2 would give R ≈ 0.19.
- So R < 1/2 requires a NON-WICK value distribution (strongly skewed, nearly two-valued) — "f_A ≈ α 1_E − β" for a
  scattered set E of measure ≈ 2R^2. Obstruction in Z: a 0/1-coefficient polynomial cannot approximate a step function
  (Gibbs overshoot ~0.09α ≫ β), so E must be a union of many tiny pieces around a quasi-subgroup of T, i.e. a
  Meyer/model-set-like configuration whose exponential sums are two-valued. Candidate source to examine next: cut-and-
  project (model) sets and their duals (Meyer's harmonious sets) — the continuous analogue of self-dual cyclotomic sets.
- First check of the model-set lead (derivation, not yet numerics): A = {n : {nθ} ∈ W_n} with a tapered symmetric
  window W_n = (−w(n/X)/2, w(n/X)/2) gives f_A ≈ Σ_m (bump at x = ∓2πmθ with profile c_m(t) = sin(π m w(t))/(π m)).
  For m <~ sqrt X the bumps have amplitude ~X/m and their shapes are p.d. only if c_m(t) is p.d. in t, which fails
  (oscillating in t for large m). Flat (Gauss-sum-like) amplitudes would need a window with flat Fourier coefficients —
  the same problem one level up. Lead weakened, not killed (fractal / arithmetic windows untested).
### SNZ for Singer sets — mechanism (HEURISTIC; possible theorem via Katz-type equidistribution)
- Grid values G(l) = F_D(2πl/v) have |G(l)|^2 = q (l ≠ 0). Interpolation (exact up to O(1/v)):
  F_D(2π(l+s)/v) = Σ_m G(m) D_v(l+s−m), D_v(n+s) ≈ (e^{2πis} − 1)/(2πi(n+s)). At s = 1/2:
  F_D ≈ (i/π) Σ_n G(l−n)/(n+1/2): the pairs (G(l−n), G(l+1+n)) enter with weights ±1/(n+1/2) and cancel when the phase
  sequence is locally symmetric about l+1/2. With equidistributed, roughly independent phases, J matched pairs occur
  for some l once v >~ ε^{−J}, leaving a tail of size ~ sqrt(q/J): min|F_D|^2 <~ q/ log v -> 0 (slowly).
- Rigorous route: joint equidistribution of (G(l), ..., G(l+J)) over l (Gauss/Kloosterman-type sums over F_{q^3};
  Katz monodromy) would give SNZ for Singer sets, hence R -> 1/sqrt2 for Singer differences and, through P13, a
  lower bound M(A(S)) >= k/2 − o(k) for Bu's own Singer-based sets.
### The constructive question in its sharpest form (synthesis of P8, E10, consistent thinning)
- In Z_p the R < 1/2 examples (E10) are cyclotomic association schemes: the difference multiplicity of H is CONSTANT on
  each cyclotomic class (coherent multiplicity, exactly the P8 escape) and Gauss-sum alignment makes the spectrum
  two-valued. In Z the same object would be a "torsion-free association scheme": a support B ⊂ Z whose difference
  multiplicities are (nearly) constant on a partition of Z\{0} into classes, with the target classes forming A.
  P4 forbids exactness (extreme differences have multiplicity 1); Bu's tent-thinning repairs the boundary only for
  multiplicity 1 (Bernoulli keeps 0/1), and consistent thinning for m >= 3 needs a difference-preserving group of
  order m (impossible). An R -> 0 construction must therefore absorb boundary defects of the lifted scheme with an
  error budget o(sqrt N) while m -> ∞ — the precise quantitative target for the Epoch track.

## 2026-10-18 (session 1, cont.) — averaged boundary route closed; dense-profile theory; P16 (C½ for the Bu class)
- Averaged Bedert–Shankar (agent, P14): averaging cannot help because, after localisation, source (a) of Bedert's K^4 is
  t-independent: L(A) = ∫_{F<181K^3}(F+K)^2. Exponent gain ⟺ "no middle layer" (or non-saturation) + averaged (b).
  Lead: the no-middle-layer statement FAILS in Z_N (unions of subgroups of sizes r^3 and r^10), so it needs torsion-
  freeness — same status as C½. Route parked: it needs a structural decomposition of A along level sets of F.
- Small-N exhaustive (agent): new best certified R = 0.56481 (N = 36). Box MILP confirms N=24 optimum in [1,40].
- Dense-profile theory (E16/E17): f_A = X ŵ(xX) + E(x), main term needs ŵ >= 0 up to O(1/√X); with σ_E^2 = (1−ρ)N/2,
  R = c_E sqrt((1−ρ)/2) where ρ = ∫w^2/∫w <= ρ* ≈ 0.7239 for doubly-positive profiles (numerical sup, new constant to
  identify). Symmetric (arcsine) rounding errors give c_E >= √2 ⇒ R >~ 0.5255. Measured c_E ∈ [1.43, 1.87]. So dense sets
  beat 1/2 only if their rounding errors are positively skewed — the same non-Wick requirement as before, one level down.
  Bu sets are the sparse end (ρ ≈ 0, c_E = 1/√2). Finite-N gains come from the O(1/√X) non-p.d. tolerance, which vanishes.
- P15: Bu's sum is f_{A(S)} = P^2 − k/2 − C/2 with P = Σcos((3s+1/2)x) = C(x/2): i.e. f_{A(S)}(2u) = C(u)^2 − C(2u)/2 − k/2
  for the single Sidon cosine sum C(u) = Σcos((6s+1)u). Excess = (C/2 − P^2) at near-zeros of P (E19).
- P16 (main new theorem of the day): R(A(S)) >= 1/2 − O((L/k^3)^{1/6}) for every Sidon S ⊂ [−L, L]. Mechanism: Q = Σcos^2
  concentrates at k/2 (4th moment of C exact by Sidon), while a positive bump test plus Sidon counting forces P to come
  within sqrt(ηk/2) of 0 in every window of length ~5/(ηk); at those points f ≈ −Q, and a Lipschitz/Chebyshev count
  rules out C <= −ηk at all of them. First unconditional proof that Bu's construction cannot beat 1/2 (P12 needed
  dissociation, P13 needed SNZ). Review + Lean agents launched.
- Next questions this raises: (i) does the same "visit + concentration" scheme prove SNZ-weak (min|F_D|^2 <= 0.29k) for
  Sidon differences? The obstacle is that |F_D|^2 needs a 2-D visit (P_c, P_s both small); a bump test only gives 1-D
  visits. Idea to try: rotate, f_{D−D} = (|F|^2 − k)/2 and use Re(e^{−iθ(x)}F) with a locally linear phase θ.
  (ii) Can P16's scheme be made universal: for an ARBITRARY A, write f_A = P^2 − Q + (rest) via a Fejér–Riesz factor?
  The gain identity (Γ(1−L) = 1/(2R^2)) says every spectral factor carries the same information; a "visit" lemma for the
  factor + concentration of its diagonal could give a universal lower bound with the right exponent in special classes.
- Correction to the dense-profile reading: R = c_E sqrt((1−ρ)/2) is an identity (σ_E^2 = (1−ρ)N/2 by Parseval), so
  "raise ρ and keep Bu's skew" is not a free knob. Measured on sparse Bu sets: ρ ≈ 0.03, σ_E/√N = 0.698 =
  sqrt((1−ρ)/2) exactly. For a Bu set built on a Sidon S with density profile σ, the difference profile is σ⋆σ (doubly
  positive, ρ <= ρ*), but P16 still pins R >= 1/2 − o(1): the skew c_E adjusts. The heuristic's only content is
  ρ <= ρ* plus whatever lower bound on c_E a mechanism gives.
- 2-D visits (the missing lemma V2 behind SNZ-weak and behind the "two squares" route): soft arguments cannot prove it.
  A bump test only controls 1-D projections, and the planar curve (P_1, P_2) can spin (|θ'| ~ L/√η) while staying
  outside a disk — exactly what Kahane's ultraflat unimodular polynomials do. So V2 must use the 0/1 + Sidon arithmetic.
  For Singer sets the arithmetic is explicit: midpoint values are a discrete Hilbert transform of Gauss-type sums
  (E20: exponential-like law at θ = 1/2). Route recorded, not pursued further today.
- Dense regime is the LIVE candidate against C½ (not against Chowla). Anatomy of the N=36 optimum: M = 3.389 = (E part
  2.606) + (main part 0.783 at x*). As N grows the O(1) main part vanishes relative to √N (−0.13 in R), but the profile
  must become positive-definite (tolerance ~1/√X), pushing ρ from 0.79 to <= ρ* = 0.724 and σ_E/√N up by
  sqrt(0.276/0.21) ≈ 1.15–1.17. Holding c_E at its N=36 value gives R_∞ ≈ 0.434·1.16 ≈ 0.50–0.51. So the dense limit is
  undecided at the level of this heuristic: R_∞ < 1/2 iff the optimal rounding error keeps c_E below ≈ 1.35 while the
  profile becomes p.d. Discriminating experiment: good dense sets at N = 100–1000 (exhaustive is out of reach; LNS from
  random starts is too weak (0.60–0.62 at N=36), so a structured optimizer is needed: interval core [1, 0.6X] + exact
  tail MILP (src/lns_milp.py mode 3), X ≈ 1.38N).
- Conceptual synthesis (why Z_p beats 1/2 and Z apparently cannot): the Z_p winners (E10) need "Gauss sums" that are
  deterministic — constant modulus and aligned phase on the whole grid — making the spectrum two-valued. On Z the analogous
  objects (exponential sums of Sidon/Singer sets) are functions of a continuous variable: E20 shows a Singer set exactly
  flat on its own grid (|F|^2 = q) becomes exponential-like at the half-shifted points. Continuity forces the
  "Gauss-sum-like" quantities through small values (the P16 visit lemma is the rigorous 1-D instance), and small values of
  the square factor are exactly where f_A ≈ −(diagonal) ≈ −k/2. Spectral form: Bu's Cayley graph on Z is a "Paley graph
  on Z" (λ_min = −√(d/2)·(1+o(1)), P16), and C½ says no distance graph on Z beats Paley.

## 2026-10-18 (session 1, late) — the quadratic class: why Bu's single square is extremal (Smith's theorem)
- Setting (HEURISTIC + one standard theorem). For half-integer frequencies b_s with all |b_s ± b_t| distinct and a graph G on
  S, the set A_G = {|b_s ± b_t| : st ∈ E(G)} has f_{A_G} = c^T Adj(G) c with c_s = cos(b_s x), N = 2|E|. Write
  Adj = Σ μ_i v_i v_i^T, T := Σ_{μ>0} μ_i = Σ_{μ<0}|μ_i| (trace 0), N = Σ μ_i^2. In the Gaussian model (c ≈ N(0, I/2) at a
  typical x) the most negative values occur where all p positive components vanish, giving M ≈ T/2 + (fluctuation of the
  negative chi-square part). Since Σ_{μ>0} μ_i^2 <= T^2, R >~ (T/2)/sqrt(T^2 + Σ_{μ<0} μ_i^2) -> 1/2 at best, with
  equality only if (i) p = 1 (then Σ_{μ>0}μ^2 = T^2 exactly) and (ii) the negative spectrum is flat (Σ_{μ<0}μ^2 = o(T^2)).
- Smith (1970): a graph has exactly one positive eigenvalue iff its non-isolated vertices form a complete multipartite
  graph. So the p = 1 class is f = P^2 − Σ_i P_i^2 (blocks B_i), and condition (ii) forces blocks of size o(k): K_k = Bu.
  For p >= 2 the positive part must avoid simultaneous vanishing, i.e. be lower-flat (p = 2 with complex F is the Sidon-
  difference class, which needs min|F|^2 >= 0.29k: SNZ-weak; numerics E8/E12/E15 say c -> 0).
- E22 tests the p = 1 class beyond K_k: even blocks of size 2 cost ≈ +0.35k in M (the within-block sum is not engineered,
  so its extreme values at the zeros of P add up). So inside the quadratic ("square-identity") paradigm Bu is extremal,
  and P16 proves it rigorously for K_k with L = o(k^3). This sharpens Bu et al.'s Remark 8.4 ("below 1/2 needs an idea
  outside the square-identity paradigm") into: quadratic forms in Sidon-type cosines cannot beat 1/2 unless the cosines
  are non-Gaussian (additive structure among the b_s, which creates collisions) or the positive part is lower-flat.
- Higher chaos is worse: Bu = He_2. For the full degree-m elementary symmetric construction, R -> |min He_m|/sqrt(2·m!)
  (m = 2: 1/2; m = 4: 6/sqrt 48 = 0.866; m = 6: 2.72). Sparse sub-families add Gaussian noise at the k^{m/2} scale.

## 2026-10-18 (session 2) — reformulations and failed attacks recorded so they are not repeated
- Probability-measure form of Chowla (PROVED, trivial but clarifying). A = −A ⊂ Z\{0}, F = 1̂_A >= −K. Then
  ν := (F + K)/K is a probability density with ν̂(n) ∈ {0, 1/K} (n ≠ 0), and ν∗ν = (1/K)ν + (1 − 1/K)λ (λ = Haar): two
  independent ν-samples sum to a ν-sample with probability 1/K, else to a uniform one. ||ν||_2^2 = 1 + |A|/K^2, so
  Chowla ⟺ every such "1/K-idempotent" density has ||ν||_2^2 <= C. Bu: ν ≈ 2P^2/k (chi-square law), ||ν||_2^2 ≈ 3, the
  Gaussian kurtosis that the Sidon property pins. Consequences tried: ν∗ν >= 1 − 1/K pointwise (spread condition);
  popular sums of {F >= H} land in {F >= (H|E_H|)^2/4} — the level drops to <= K^2/4, i.e. the K^2 threshold of Bedert's
  (S'). No new leverage found today.
- 2-D visit via locally linear/chirp phase (the STATE "next step"): if |F_D|^2 >= βk on [c−h, c+h] and the phase were
  linear (resp. quadratic), the triangle (resp. chirped-triangle) test gives √(βk) <= Σ_d |window transform(d − ω)|
  <~ C/√h by Sidon counting, so h <~ C^2/(βk). But for ultraflat-type behaviour the phase coherence length is ~X^{-1/2}
  (polynomial phase of order m: ~X^{-1}β^{1/2m}), far below 1/(βk) since X >> k. The test cannot close without an a
  priori bound on the phase derivatives of F, which is exactly the arithmetic input that is missing. Recorded as failed.
- Singer sets, midpoint moments (idea, not pursued): on any shifted grid x_j = 2π(j+θ)/v, Σ_j |F|^2 = vk and
  Σ_j |F|^4 = v(2k^2 − k) exactly (Singer sets are Sidon mod v; in Z the defect d1+d2−d3−d4 ∈ {0, ±v} only for trivial
  solutions). A moment test (m2 − β)^2 > (1 − β)(m3 − βm2) would force min |F|^2 < βk, but the main term near x = 0
  dominates m3 (~k^6 vs k^5 bulk); removing it needs weights |1 − e^{ix}|^{2s}, whose moments are signed relation
  counts of Singer sets lifted to Z (not algebraic; would need Weil/Deligne-type equidistribution). Low value.
- Dense regime, where could positive skew come from? (HEURISTIC + one classical lemma.) A positive spike of G = f_A − T
  at a nonzero rational 2πj/q with a p.d. envelope needs the local residue pattern u: Z_q → {1−w, −w} (mean 0) to have
  REAL, nonnegative Fourier coefficients (an imaginary part produces the odd sine-transform of the profile, which takes
  both signs at full spike size). Lemma (classical, via |φ(r) − φ(r+s)|^2 <= 2φ(0)(φ(0) − φ(s)) for p.d. φ): if
  1_S − c is positive definite on a finite abelian group with 0 ∈ S and c < 1, then S is a subgroup. So such spikes force
  local sublattice structure dZ of FIXED density, whose amplitude must then be modulated by a fractional p.d. profile —
  which needs rounding at the next level, passing >= (1 − ρ*) of the L^2 mass on. A hierarchy of modulated sublattices
  is the only shape of a positively skewed dense rounding; at the finest level the modulation is a 0/1 step function
  (non-p.d.), whose Dirichlet defects add incoherently to Gaussian-size noise. This is a heuristic reason why the skew of
  the exhaustive optima fades with N (E21). Fixed-profile experiment E23 (src/profile_rounding.py): sigma-delta
  roundings of p.d. profiles have c_E ≈ 2.1–3.8 and growing with X (tri, gauss, fejer2 at X = 100–1600).
- (S') in peak language (HEURISTIC analysis, session 2). With φ = F + K, ∫∫φ(u)φ(v)ψ(u+v) = ∫φψ + (K^2−K)∫ψ for every ψ.
  If u, v sit in peaks of φ of height >= H and width w, then φ(u+v) >= H^2·w − K^2, so sums of peaks are high once
  H^2 w >> K^2. For the extremal 1/5 configuration (middle layer: height K^3, total measure K^{-2}, n ≈ K^5) closure needs
  w >> K^{-4}; but a peak of height H has width w <~ 1/H (the coherent part A' of A has |A'| >~ H inside an interval of
  length ~1/w), so middle-layer peaks have w <= K^{-3} and narrow ones (w < K^{-4}) are not excluded by idempotence alone.
  Middle-middle pair mass ≈ (K^3)^4 (K^{-2})^2 = K^8 = nK^3 is exactly the (S') threshold. So (S') ⟺ "middle-layer
  peaks are wide (w >> K^{-4}) or additively closed"; a narrow middle peak means a set A' ⊂ A of size ≈ K^3 spread over
  length > K^4 that is coherent with one frequency — the next thing to try to exclude using F >= −K on A' alone
  (Chowla for A' gives M(A') >= |A'|^{1/5}, too weak; one needs the interaction of A' with the rest of A).
- Singer–Bu (E25) anatomy. For f = P^2 − k/2 − C/2 with b_s = 3s+½: at x = π/3 + t, (6s+1)π/3 ≡ π/3 so C ≈ Re(e^{iπ/3}
  e^{it} F_S(6t)) ≈ +k/2 near t = 0, while P(π/3) = cos(π/6)(#even − #odd). So the only dangerous special points are
  x ≡ ±π/3 (C ≈ +k/2), and they are neutralised iff the parity imbalance e − o of S satisfies roughly (e−o)^2 >~ 0.8k
  (P's main lobe is twice as wide as C's). Bu et al. buy this with a deleted odd "parity block"; a cyclic shift of a
  full Singer set does it for free (the best shifts have large |e − o|). At x ≡ π, C = −k and P = 0 (f = P^2 >= 0); at
  ±2π/3, C = −k/2, P = k/2. Elsewhere the excess over k/2 is the generic fluctuation of −C/2 at near-zeros of P,
  ≈ 0.95√k in E25 — the term P16 shows cannot be made negative of order k.
- SNZ-weak via rotating visits (PROVED consequence, no contradiction found). If |F_D|^2 >= βk everywhere (D Sidon), apply
  the P16 visit lemma to every G_θ = Re(e^{−iθ}F_D) (all are cosine sums with the same Sidon frequency counting): each
  window of length 2h, h ≈ 5/(ηk), contains x with |cos(ψ(x) − θ)| < sqrt(η/(2β)), ψ = arg F_D. Hence ψ sweeps an angle
  >= π − O(sqrt(η/β)) inside EVERY such window: lower-flat Sidon polynomials must wind at speed >~ ηk uniformly, i.e.
  have >~ ηk zeros inside the unit disk, angularly equidistributed at scale 1/(ηk). Upper bounds on winding available
  from |ψ'| <= |F'|/|F| are ~X/√β >> ηk, so no contradiction; a proof of SNZ-weak needs a reason why 0/1 Sidon
  polynomials cannot have that zero geometry (their zeros' radial distribution is the natural place to look).
- Synthesis after E24/E24b/E26 (HEURISTIC picture, session 2). Writing f + λ = |H|^2 (Fejér–Riesz), a real cosine sum
  has a REAL factor H, and the question "how skewed can the error be" becomes: minimise ||h||^2 over sequences whose
  aperiodic autocorrelation is two-valued (±½, or {−w, 1−w}) at every lag. With complex h (free phases, |a(j)| = ½) the
  optimum is flat at ≈ 0.9·sqrt(X/2) (E26); with real h (±1 cosine sums) the optimised ratio rises 1.17 → 1.58 over
  X = 50 → 800 (two optimisers), plausibly toward the Rudin–Shapiro value 2 (an upper bound for every X). If the real
  constant tends to c_∞ >= ~1.6, dense 0/1 sets have R_∞ ≈ c_E·sqrt((1−ρ*)/2) >= ~0.6 (consistent with LNS 0.66 at
  N = 80), so asymptotically the dense regime loses to Bu (-> 1/2). The only mechanism producing sub-arcsine skew on Z
  is then multiplicative: a square of a Sidon-type cosine sum (Bu, χ²_1 law, ratio 1/√2), pinned at 1/2 by P16. This
  is the most coherent account so far of why C½ should hold; it is not a proof.
  Conjecture (new, testable): c_±(X) := min_{ε ∈ {±1}^X} (−min_x Σ ε_n cos nx)/sqrt(X/2) satisfies liminf c_± >= 1.5.
- Min–max tradeoff (PROVED, two lines; the correct core of Erdélyi's attempt). For a real trig polynomial
  L = Σ_{n<=X} a_n cos(nx) with L >= −M: πΣ n^2 a_n^2 = ||L'||_2^2 <= ||L'||_∞ ||L'||_1 <= (X·max|L|)(X·2πM) (Bernstein in
  sup and in L^1 for L + M >= 0), so M·max|L| >= Σ n^2 a_n^2 / (2X^2). For ±1 full support: M·max|L| >= X/6, i.e.
  upper-flat ±1 cosine polynomials (max|L| <= C√X, e.g. BBMST) have −min >= √X/(6C), and a small minimum forces spikes
  of height >= X/(6M). Level-set refinements cannot do better: spikes of height B, width 1/X, total L^1 mass <= 2πM carry
  derivative energy up to 2πX^2 BM, exactly the budget. For 0/1 sets the spike at x = 0 (height N) makes it trivial.
- Adding structure to a Bu set does not help asymptotically (HEURISTIC). (i) A = A(S) ⊔ B with B a dense p.d. rounding
  (|B| = βk^2): at the zeros of P the excess is −C/2 + G_B, of variance k/8 + (1−ρ)βk^2/2, so R ≈ (1/2 + z sqrt((1−ρ)β/2))
  / sqrt(1+β) with z ~ sqrt(2 log #zeros): the √β cost beats the β/4 gain for small β, and large β is the dense regime.
  (ii) Adding the diagonal frequencies {6s+1 : s ∈ S'} for half of S turns −C/2 into −(C_{S\S'} − C_{S'})/2, same
  variance; N grows by k/2, gain O(1/k) in R. The diagonal term can be re-signed but not removed.

## 2026-10-18 (session 2, cont.) — P18 test, P16′ kernel-checked, ρ* reappears for Sidon differences
- P16′ (exponent 1/5) KERNEL-CHECKED (Gallagher form; PROOFS). Formalization caught a window-folding error in the
  lead's Gallagher sketch (windows must sit in ONE period window) — conclusion unaffected.
- P18 (dense min–max) is qualitatively right but numerically empty at N <= 1e4 (E28): the spike at 0 needs
  W_0 >= 2N/X, and the Bernstein chain loses ≈ 10x. Closed as a probe.
- Sidon differences D(B): R(D(B)) = (1 − c)/√2 with c = min|F_B|²/k, so beating 1/2 ⟺ c > 1 − 1/√2 ≈ 0.293. New
  structural observation (HEURISTIC, profile level): write F_B = D + Z with D(x) = k ŵ(xL) the profile part (B ⊂ [0,L),
  L = λk², profile w a probability density on [0,1]). The Sidon property, smoothed, says k²(w⋆w̃)(s)/L <= 1, i.e.
  w⋆w̃ <= λ. The spike's share of E|F|⁴ = 2k² − k is ∫|D|⁴/(2k²)·... = c_w/(2λ)·2 with c_w = ∫(w⋆w̃)² <=
  ρ*·(w⋆w̃)(0)·∫w⋆w̃ <= ρ*λ, where ρ* ≈ 0.7239 is EXACTLY the doubly-positive constant of E16/P17 (w⋆w̃ is doubly
  positive). Hence E|Z|⁴ >= (2 − ρ*)k² ≈ 1.28k² while E|Z|² ≈ k: the off-spike fluctuation of a Sidon sum is flatter than
  Gaussian (kurtosis 4/3 for uniform profiles, >= 2 − ρ* always) but never ultraflat. The same constant ρ* bounds the
  dense regime (R = c_E√((1−ρ)/2)) — a common obstruction: macroscopic profiles can absorb at most a ρ* fraction of the
  fourth moment / energy. Lower-flatness (c > 0.293) is not excluded by moments; E8/E12/E15/E29 all give c -> 0.
- Where Bedert's K^4 (Prop 7.3, 2509.05260v3 §7) comes from — and a small barrier (PROVED, elementary). Setting:
  A = −A, F = 1̂_A, G = F + K >= 0, a_m = 1_A(m), B_t = {m ∈ A : m − t ∈ A, m + t ∉ A} (tops of maximal t-runs).
  Bedert: (38) |φ_t| <= ψ_t + O(K^2) with φ̂_t >= 4+√2 on B_t > sup ψ̂_t = 4 + 1/√2 (a coefficient GAP), built from
  f_t ∗ f_t where f_t = 2(1 + sin 2πtx)F >= −4K; tested against H∗H, H = |Q_1|, 1̂_{B_t} = Q_1 + Q_2, |Q_1| <= 4G,
  ||Q_2||_2 << K^2 (Lemma 7.1). Losses: O(K^2)·||H||_1^2 <= 16K^4 and K^2|B|^{1/2} from Q_2; both give |B_t| << K^4.
  BARRIER (degree 1 cannot give a gap): for any nonnegative multiplier m(x) = Σ_j c_j e(jtx), the coefficient of m·F at m is
  Λ(ε) = Σ_j c_j ε_j, ε_j = a_{m−jt}. On B_t-patterns (ε_0 = ε_1 = 1, ε_{−1} = 0, others free) min |Im Λ| <= |Im c_1|
  (take ε_j = 0 for |j| >= 2) <= |c_1| <= c_0 <= max over patterns of Re Λ. So the odd part can never strictly dominate
  the even part's coefficients: some nonlinearity (degree >= 2 in the pattern) is forced, and every degree costs one
  factor K in the additive constant (functions built linearly from G have L^1 ≈ K per unit coefficient). Hence within
  "pointwise gap inequality + nonnegative test function" the bound is |B_t| <~ K^2·||H||_1^2; K^3 (=> exponent 1/4)
  needs a test H >= |Q|, Q̂ ≈ 1 on B_t in L^2, with ||H||_1 <~ K^{1/2} — e.g. if run-top sets B_t had small Fourier
  L^1 norm relative to K. Not pursued further now; recorded so the next attempt starts from the right bottleneck.
- Bu's construction in dense-profile coordinates (PROVED at profile level, elementary; HEURISTIC only in reading c_E as
  the residual's skew). For a dense Sidon S ⊂ [−v/2, v/2] (k² ≈ v, profile u on S), A(S) has a p.d. profile W with
  period-3 structure: on n ≡ 0 (mod 3) density w_d(n/3v) = (u⋆ũ)-profile (positive differences), on n ≡ 1, 2 density
  w_s/2 (sums s+t, unordered pairs; sign of 3(s+t)+1 sorts m >= 0 / m < 0 into residues 1 / 2). Since ŵ_d = |û|², ŵ_s = û²,
  ∫w_d² = ∫w_s² = ∫|û|⁴ and
      ρ_Bu = ΣW²/ΣW = (3/4)·∫(u⋆ũ)²/((u⋆ũ)(0)∫u⋆ũ) <= (3/4)ρ*_{h>=0} ≈ 0.543;   uniform u (Singer): ρ_Bu = 1/2 exactly.
  With σ_E² = (1−ρ)N/2 and P16 (M >= (1/2 − o(1))k, N = k(k−1)), the residual skew constant is FORCED:
      c_E = M/σ_E = 1/√(2(1−ρ)) + o(1)       (= 1 for Singer, i.e. the residual ≈ P² − k/2 dips exactly one σ).
  So squares realise the curve R = 1/2 for every attainable ρ, and C½ is EQUIVALENT (tautologically, via R = c_E√((1−ρ)/2))
  to the skew–profile tradeoff  c_E >= 1/√(2(1−ρ))  for every decomposition f_A = profile + residual. Records: dense box
  optima sit above the curve (N=36: ρ ≈ 0.83?, c_E ≈ 1.6–1.8 — re-measure ρ with the same convention before using).
  Beating 1/2 = finding residual skew below the square curve; the dense SA/MILP optima never did, P16 forbids it for
  squares at any profile. Note also that Bu's profile has spikes at x = ±2π/3 (φ̂(±1) = 1/2 > 0): mod-3 structure is
  harmless because the period-3 pattern (1, 1/2, 1/2) is p.d. on Z_3.
- Hermite-mixture constructions are blocked by Parseval noise (HEURISTIC, Wick model H1; computations exact). For a
  frequency set B with all signed d-sums distinct, the full d-set family gives f_{A_d} = 2^{d−1}e_d(cos b_s x) ≈
  c_d k^{d/2} He_d(z), z = P/√(k/2): d = 2: (k/2)He_2, min −k/2, N ≈ k², R = 1/2; d = 4: (k²/12)He_4, min He_4 = −6,
  N ≈ k⁴/3, R = √3/2. A MIXED residual q(z) = He_2 + t·He_4 is far more skewed: |min q|/||q||_2 = (1 − 3t)/√(2 + 24t²)
  decreases from 0.707 (t = 0) to 0.306 at t = 1/6 (q = z⁴/6 − 1/2, the shape of a 4th power). But with 0/1
  coefficients the relative weight is FORCED, t = k/6 for full families; t = 1/6 needs a sub-family of 4-sets of density
  ε = 1/k, whose cosine sum has L² norm √(ε|A_4|/2) ≈ 0.41k^{3/2} by Parseval while its component along He_4(z) is only
  ≈ ε·||(k²/12)He_4|| ≈ 0.4k: noise dominates (and is Gaussian-like, min ~ −k^{3/2}√log). Structured sub-families
  (e.g. Σs ≡ 0 mod k) are the same: the j ≠ 0 twists contribute independent He_4's of total size ≈ k^{3/2}. So within
  the Wick/elementary-symmetric world only pure degrees are realisable and degree 2 (Bu, R = 1/2) is optimal;
  a sub-1/2 construction must leave this world (non-dissociated, genuinely arithmetic structure).
- Run-top agent result (P19): Bedert's K^4 is SHARP for every argument using F >= −K only through A-independent
  degree-2 (or degree-r) convolution inequalities — random relaxed sets satisfy all of them with K_* ≍ (N log N)^{1/4}
  and |B_t| ≍ N. Exponent 1/4 therefore REQUIRES degree-1 input (pointwise F >= −K, ||F||_1 <= 2K, or the domination
  |1̂_{B_t}| <= 4G + |Q_2| used beyond norms). Exact target: Lemma S, ∫min(|1̂_{B_t}|, K³)² << K^{4−δ}. Cheapest
  discriminating experiment: search finite groups (F_3^d, Z_m^d, ±-combinations of a few cosets) for |B_t| >> K^{2+ε}.
- FAILED (lead, checked exactly): a finite-group "counterexample" to P19's group question. Γ = Z_3 × H, t = (1,0); fibres
  A_h ⊂ Z_3 with |A_h| = 2 (D: one run-top each, so |B_t| = |D|) carry phase g_1 = −ω^{i0} (odd 6th roots), |A_h| = 1 (E)
  carry +ω^{i1}. Choosing u = Σ_{i∈A_h}ω^i = ζ_6^{λ(h)} for a hom λ: H → Z_6 makes every j = 1, 2 character value >= 0,
  but the j = 0 values are the fibre-size transform ĉ with c = 1 + 1_D, and D = {λ odd} is an index-2 coset, so
  ĉ = −|H|/2 at the parity character: K = 4, 19, 109 for H = Z_6, Z_6², Z_6³ (|B_t| = 3, 18, 108 ≈ K). Patching with full
  /empty fibres re-creates the −|H|/4 at the same character. Mechanism: aligning D-phases with a character forces D to
  be a coset, which is penalised at degree 0. Consistent with the agent's evidence that groups give |B_t| <~ K².
- Conjecture G in Z_3 × H, slice form (PROVED reductions, lead). With t = (1,0) and fibre functions q_j(h) =
  Σ_{i∈A_h} ω^{ij}: F(j,ψ) = q̂_j(ψ), q_2 = conj q_1, so only j = 0 (fibre sizes c) and j = 1 (u := q_1, values in μ_6 ∪ {0},
  u(−h) = conj u(h)) matter. u ∈ −μ_3 exactly on 2-point fibres D (run-tops), u ∈ μ_3 on singletons E, u = 0 on empty/full;
  u³ = 1_E − 1_D. If K >= −min û and u(0) = 0, then w = û + K >= 0 and the threefold convolution gives
      0 <= Σ_{ψ1ψ2ψ3=1} w(ψ1)w(ψ2)w(ψ3) = |H|²(Σ_h u³ + K³) = |H|²(|E| − |D| + K³),   i.e.   |D| <= |E| + K³.
  So run-tops exceed singletons by at most K³. Not sufficient: |E| is unbounded at K = 1 (A = graph of a homomorphism on
  a subgroup), and degree-3 positivity alone is capped (P19). A proof of G needs to rule out D-fibres while E-fibres
  carry the compensation — the same "boundary vs bulk" structure as run-tops in Z.

## 2026-10-18 (session 2, late) — Conjecture G refuted (P20); what survives for Z
- Agent conjG: Conjecture G is FALSE in groups. P20 Theorem 1: |B_t| = K²(K−1) in F_p^{1+3a}. Lead re-verified with an
  independent, simpler set (E31): A = {x ∈ F_p^4 : x1x2 + x3² − d x4² ≠ 0}, t = e1. Q is affine along t-lines (t isotropic),
  so each line with x2 ≠ 0 loses exactly one point (one run, one top: p²(p−1) tops); lines with x2 = 0 are FULL
  ((x3,x4) ≠ 0) or empty, and these full lines repair the degree-0 slice. Spectrum {−p, p(p−1), |A|}: K = p.
- Theorem 2 (agent, lead checked): ord t = 3 ⇒ |D| − |E| <= (K + u0)³ via U³ = ρ(1_E − 1_D) and Schur cubes of the p.d.
  fibre transform. Barrier: singleton fibres E always count +1 in any positive combination of fibre monomials; and
  monomials U^aŪ^b c^d (a ≡ b mod 3, a + b odd) give 2^d|D| <= |E| + (K+u0)^{a+b}(K+c0)^d — |D| <= ε|E| + C_ε K^{β(ε)},
  never |D| alone (E is unbounded at K = 1: subgroup graphs).
- Z version of the fibre transform (PROVED, lead; elementary). A = −A ⊂ Z\{0}, F >= −K, t >= 1, A_y = {k : y + kt ∈ A}
  (0 <= y < t), S_y(z) = Σ_{k∈A_y} z^k. For φ ∈ R, U^φ(y) := e(yφ/t)S_y(e(φ)) has DFT_j = F((φ+j)/t) on Z_t, so U^φ + Kδ0
  is p.d. on Z_t. Schur products: for any z_1..z_r ∈ T with Πz_i = 1,
      Σ_{y=1}^{t−1} Π_i S_y(z_i) + Π_i (S_0(z_i) + K) >= 0.
  In correlation form: Σ_d μ̂(d)·N_r(d) >= −(K-terms), N_r(d) = #{a : a, a + d_1t, .., a + d_{r−1}t ∈ A} — positivity of
  the t-direction correlations. With z_i = ω this is exactly the Z_{3t} multiset statement: S_y(ω) only sees A_y mod 3
  (a run contributes a unit or 0 by its length mod 3; the pair {0,2} contributes −1 like a 2-run, {0,3} contributes 8).
  So in Z the cube identity "U³ = ±ρ on 2-point fibres" has no analogue: fibres are long and alias mod 3. The order-3
  mechanism does not transfer; I have no Z-specific replacement yet.
- What Z inherits that Theorem 1 violates (NEW refined finite model). The transfer Z -> Z_N (A ⊂ [−N/4, N/4]) never has
  a ⟨t⟩-coset inside A (choose N prime: the only coset is Z_N). Theorem 1 needs full cosets (r = 0 fibres; Lemma 3 and
  Theorem 4 both use the degree-0 repair). Conjecture G_noFull: |B_t| <= C K² whenever A contains no ⟨t⟩-coset.
  It would imply exponent 1/3 in Z; its K³ version exponent 1/4. Evidence so far: anisotropic quadric level sets
  {Q = c} (lines meet in <= 2 points: no full cosets) give ratio exactly 1. Next: exhaustive test over all
  Stab(t)-invariant sets A = {x : (Q(x), B(x,t)) ∈ S} in F_p^n (line patterns follow the affine dynamics
  (q, b) -> (q + b + Q(t), b + 2Q(t)) on F_p²); restrict to no-full and measure max |B_t|/K² versus p, n.
- Strategic review (skill §3). Distance: the run-top route is now mapped: degree-2 Fourier methods <= K⁴ (P19, sharp,
  exponent 1/5); group-agnostic methods >= K³ (P20; at best exponent 1/4). A proof of K^{3−δ} must use torsion-free /
  interval structure; G_noFull is the minimal such input that kills the known extremal mechanism. Kill: Conjecture G,
  "Paley optimal", group-form Lemma S. Continue: G_noFull probe (cheap, discriminating); P16-type C½ for further
  classes; dense-regime exhaustive. Construction track: no live sub-1/2 mechanism; every known one is pinned.
- G_noFull REFUTED (P21, lead, elementary). In F_p^4: bulk lines x2 ≠ 0 as in E31; lines x2 = 0 also miss exactly one
  point, at τ2 = x3x4² (odd). All fibres have p − 1 points ⇒ degree-0 slice ≡ 0; the x2 = 0 part adds −ĝ_j(c) with
  ĝ_j(c) = p·Σ_{v4: jv4² = −c3} e_p(c4v4) ∈ [−2p, 2p]. K = 3p, |B_t| = p³ = K³/27 exactly (E33, p = 3..23). E32 (exhaustive
  O(Q)_t-invariant sets, p = 3: n <= 8; p = 5: n <= 6): no-full invariant sets never exceed ratio 1 — the invariant class
  is too small (P21's τ2 is not invariant). So K³ in groups needs neither full nor singleton cosets.
- Diagnosis: negative-definite fibres. Both K³ mechanisms use fibres F_p\{τ}, whose transform along t is −e_p(jτ) at
  EVERY j ≠ 0. Lemma (PROVED, P21): a fibre with transform <= 0 at all j ≠ 0 (after translation) has |I| >= ord(t)/2 —
  its run is longer than half the cycle. In Z/Z_N-transfer every t-run is < ord(t)/2.
- Torsion-free mechanism (HEURISTIC, lead). In Z write θ = (j + φ)/t. Fibre transforms S_y(e(φ)) depend on a CONTINUOUS
  φ; near φ = 0, F((j+φ)/t) = ĉ(j) + φ·H_j'(0) + O(φ²), H_j'(0) = (2πi/t)Σ_{a∈A} a e(ja/t), and since F is even,
  H_{−j}'(0) = −H_j'(0): the first-order term has OPPOSITE signs at j and −j, so one of F((±j+φ)/t) is pushed down.
  Groups have no small φ (φ ∈ (1/p)Z), so no such term. Model class where this can be made quantitative: one run per
  residue class, equal length ℓ: A = S + t·[0, ℓ) (S has one element per class mod t), F(θ) = D_ℓ(tθ)·F_S(θ). With
  centred run positions b_y (odd in y), G_φ(j) := F_S((φ+j)/t) ≈ (2πiφ/t)·b̂(j) for φ <~ 1/ℓ, odd in j; Parseval
  Σ_j |b̂(j)|² = tΣ b_y² ≈ t²X²/3 (X ≈ ℓt/2) gives max_j |G_{1/(2ℓ)}(j)| >~ √t/4, times D_ℓ(1/(2ℓ)) ≈ 2ℓ/π:
  K >~ 0.16·ℓ√t = 0.16·√(ℓ|A|). Candidate Lemma OR (one-run classes): M(A) >= c·√(ℓ|A|) for A = S + t[0,ℓ), S a
  transversal mod t. Second-order error ~ 1/4 of the main term at φ = 1/(2ℓ): needs an honest proof, then a test.
  If OR holds, the group extremal shape (every t-coset = one long run) is impossible in Z at small K; the general case
  (fibres with many runs) is what a Z-run-top bound must handle.

## 2026-10-18 (evening) — λ-fold rulers: the one live construction mechanism with a path to R -> 0
- Statement (PROVED, elementary). Let D ⊂ Z, |D| = k, r(d) = #{(u,v) ∈ D² : u − v = d}. Suppose r(d) ∈ {0, λ} for all d > 0
  except a defect set Δ, and put W := Σ_{d∈Δ, d>0} 2r(d) (defect weight). Let A = {d > 0 : r(d) = λ}. Then
      2λ f_A(x) = |F_D(x)|² − k − E(x),   E(x) = Σ_{d∈Δ, d>0} 2r(d) cos(dx),   |E| <= W,
  so M(A) <= (k + W)/(2λ) and λ|A| = k(k−1)/2 − W/2, hence R(A) <= (1 + W/k)/√(2λ) · (1 + o(1)) whenever W = O(k).
  λ = 1: Sidon differences (R <= 1/√2); λ = 2 with W = k: Bu's construction (R -> 1/2, P16 shows it is sharp there);
  λ = 3 needs W < 0.22k for R < 1/2; fixed W/k and λ -> ∞ would give R -> 0, i.e. an Epoch solution if effective.
- Known constraints: P4 — exact (W = 0) is impossible for λ >= 2 (the extreme difference has r = 1); symmetric copies
  (translations, reflections) give coherent multiplicity at most 2, and translates create diagonals of multiplicity k
  (NOTEBOOK 2026-10-18 "consistent thinning"). P8 is consistent with R ≈ 1/√(2λ). So λ >= 3 needs ALGEBRAIC coincidences
  (no symmetry), with defects O(k) — e.g. near the extremes, where few pairs exist, defects seem unavoidable.
- Open questions (both outcomes valuable): (Q1) do λ = 3 near-rulers with W <= 0.2k exist for some k? (Q2) prove
  W >= c(λ)·k^{1+δ} for λ >= 3 (that would kill this mechanism, a C½-type obstruction for all uniform-multiplicity
  difference constructions). First test: exact/SAT/ILP search over D ⊂ [0, L] for small k (C code), minimizing W at
  λ = 3; compare with the extreme-difference counting lower bound on W.
- E35 result (same evening): SA finds λ = 2 coherent sets at once (φ = 1 − 1/(k−1)) but for λ = 3, 4 the best exact
  fraction DECREASES with k (λ = 3: 0.80 at k = 10 → 0.57 at k = 30); all candidates have actual R >= 0.68 because E
  concentrates where |F_D| is small. Sharper criterion than φ > 2/3: M(A) = max_x (k + E(x) − |F_D(x)|²)/(2λ), so E
  must be small exactly on the near-zero set of F_D (Bu achieves this only because E = 2C is a half-frequency copy of
  the square root P — P16's mechanism). Next on this line, if pursued: (i) homometric-triple constructions D = U ∪ V ∪ W
  (pairwise homometric Sidon sets give multiplicity 3 on within-part differences; cross families U−V, V−W, W−U must
  then coincide up to translation); (ii) a proof that coherent multiplicity >= 3 forces W >= c·k^{1+δ}. Line demoted to
  low priority pending a structural idea.

## 2026-10-18 (night) — G3 is false (P22): the run-top route is capped at exponent 1/5 for group-agnostic methods
- Agent g3: Theorem O4 (GR(4,a) Teichmüller relative difference set; every unit coset a 2-run; K = 2^{(a+1)/2},
  |B_t| = K⁴/4 − K²/2). Lead: paper proof re-derived step by step (Lemma T, Lemma S, the three slices, O4⁺) and an
  independent implementation (E36: naive lift, brute-force Teichmüller set, dot-product pairing) reproduces K, |B_t| and
  the full spectrum for a = 3, 5, 7. Recorded as P22. Upper side: O4⁺ (fourth Schur power, any group, ord t = 4) and
  Bedert's group-valid K⁴. So the group window [3, 4] of P20/P21 closes at 4.
- E36b (lead, new): the A-AVERAGE of |B_t| in O4 is K⁴/8 − O(K²) (= |A|/4: run-tops as frequent as in a random set of
  density 1/2). In O4 Shankar's averaging inequality Σ_{t∈A}|B_t| >= T/3 HOLDS (|A|²/4 >= T/3 with T ≈ |A|²/2), and Roth's
  T >= n²/K − nK holds. So in groups the chain's ONLY failing step is the run-top bound, and it fails also on average.
- Strategic review (skill §3; triggered by a landscape-changing worker result).
  Distance: the run-top lower-bound route is now completely mapped. Degree-2 methods cap at K⁴ even in Z (P19); every
  group-agnostic method caps at K⁴ (P22), per t and on average. Exponent > 1/5 by this route needs a run-top bound that
  uses Z itself (order, interval structure, no torsion) AND goes beyond degree 2. In Z, Chowla itself would give
  |B_t| <= |A| <= CK², so the needed lemma is a genuine weakening of Chowla — no shortcut.
  Theory of success: the only Z-specific mechanisms identified are (i) the continuous t-offset φ — which on inspection is
  the Bernstein/derivative effect F((j+φ)/t) ≈ F(j/t) + (φ/t)F′(j/t), quantitatively weak (P18 was empty on records);
  (ii) the macroscopic Gibbs constraint (sets with small K must have an approximately positive-definite density profile;
  E34 shows it dominates structured "one-run-per-class" families). Neither yields a run-top inequality yet.
  Kill: all group-agnostic run-top work (G3 line closed once the agent's write-up lands). Keep the barrier note as the
  deliverable (it explains why Bedert/Shankar stop at 1/5).
  Continue: Z-specific lower bounds only with a concrete mechanism. Candidate sharpened by O4: the class
  A = S ∪ (S + t) (one 2-run per residue class, S a transversal mod t) is exactly the Z-analogue of O4, and
      F_A(θ) = 4cos(πtθ)·f_{S+t/2}(θ)     (symmetric form; f = cosine sum),
  so small K forces sign(f_{S+t/2}) = sign(cos πtθ) wherever |f_{S+t/2}| >~ K. In Z_4 × GR(4,a) this is achievable with
  K ~ |A|^{1/4} (Gauss-sum phases); in Z it must hold for all real θ. Lemma OR(ℓ = 2): M(S ∪ (S+t)) >= c√t for every
  transversal S. Both a proof (Chowla for an O4-shaped class) and a Z-construction in the class would be informative.
  Bias check: the last five lower-bound items (P19–P22) were all run-top barriers — a single template. Next lower-bound
  effort must be different (e.g., Lemma OR(2) as a test case for a Z-only argument), and the construction track needs time.

## 2026-10-18 (night, cont.) — attempts recorded so they are not repeated
- **Galois rigidity for split coprime groups (FAILED as a new constraint).** Let ord t = 3, Γ = Z_3 × H, χ₀(t) = ω, and
  write U = a + bω pointwise (a, b integer functions on H).
  - Then F(1,φ) = â + ωb̂ and F(2,φ) = â + ω²b̂. Both are real and ≥ −K, so with V := 2a − b, W := b:
        V̂(φ) + 2K >= √3·|Ŵ(φ)|   for all φ.
  - Squaring and Parseval give |D_±| + |E_±| <= 2(|D_0| + |E_0|) + 2K² + 4Ku₀. Here D_0, E_0 are the cosets whose
    special point lies in H (phase 0) and D_±, E_± the other phases. This holds in EVERY split group, not only coprime
    ones.
  - In the coprime case (3 ∤ |H|), Galois gives F(2,φ) = σF(1,φ). But A = −A already gives F(2,φ) = F(1,φ̄), and the two
    identities coincide. So Galois adds only "values are algebraic integers" (norm >= 1), which is constant-size
    information: it shifts K by about 1.
  - Also: ‖1_A‖_{A(Γ)} <= 2K + 1 in any group (Σ_χ F = 0 and F >= −K). Green–Sanders then gives a tower-type structure,
    the group form of the MPS log bound. It is not polynomial.
  - So any "cyclic groups are better" phenomenon (E37) must come from the scarcity of subgroups and bent functions
    (Schmidt field descent for flat mixed sums Σ_y ω^{τ(y)}φ(y) with 3 ∤ |H|), not from Galois positivity.
- **Quartic chaos with 0/1 coefficients (re-check of the "non-Wick quartic" lead; FAILED, confirms P8).**
  - Set f = (P² − c)²/3 − const with P = Σ_{s∈S} cos(sx) and S B_4-dissociated. Generic 4-sums then have coefficient
    24/8/3 = 1, as required.
  - 2-sums have coefficient (3(k−1) − 2c)/3. Making it 0 or 1 forces c ≈ 3k/2, and then (P² − c) ≈ (k/2)(Z² − 3).
  - So f ≈ (k²/12)·He_4(Z), whose minimum −6 against L² norm √24 gives R ≈ √3/2 ≈ 0.87.
  - The skewed He_4 + 4He_2 of R ≈ 0.19 would need 2-sum coefficients of order k, i.e. coherent multiplicity: P8 again.
  - Defect terms (sums with a repeated element) are only O(k^{3/2}) in sup, so they are not the issue; the coefficient
    cap is.
- **Cyclotomic window lifts A = W ∩ π_p^{-1}(A_p)** (A_p an aligned cyclotomic class in Z_p, W ⊂ Z a Chowla-good window):
  F_A(θ) = Σ_r c_r F_W(θ − r/p) exactly, with c_0 = 1/m and c_r = (Gauss period)/p.
  - Grid values pick up the distribution of W mod p. Unless #{n ∈ W : n ≡ a} is constant on cyclotomic classes, the
    fluctuation term is ~ √(|A_p|·|W|/p) = √n.
  - So W must be H-invariant mod p, and the only such Z-sets known are periodic lifts, which bring back the
    single-period lift problem (off-grid sinc excursions ~ √(p/m)·√log; product with a coarse window multiplies them).
  - Same conclusion as E10/E11, now with the exact formula and the precise requirement (H-invariance of W mod p).
- **E37 partial result (exact ILP, K <= 3–4) — CORRECTED the same night: the "coprime ⟹ small" reading is NOT supported.**
  Max |B_t| at K₀ = 3, ord t = 3 (all solver-optimal unless noted):
  - F_3^4: 18 (bent mechanism, P20 Theorem 1).
  - Z_9², Z_3×Z_27: 6.
  - Z_81: 3 / 4 / 5 for t of order 3 / 9 / 81.
  - Coprime H: Z_3×F_2^5 6, Z_3×F_5² 4, **Z_3×Z_4²×Z_2: 12**.
  - The last is a Lemma-3 configuration in Z_3 × Z_4²: full cosets on the index-4 subgroup {y1 + y2 ≡ 0}, 2-point
    cosets on the other 12 classes, K = 3. That is |B_t| = (4/3)K² with H of order prime to 3, so coprimality alone does
    not keep run-tops small at this size.
  - At order 64, K₀ = 4: Z_64 gives 11 (t of order 4) and 14 (t of order 64), against Z_4³ 16 and Z_8² 15. The cyclic
    deficit is mild there.
  - Larger instances (Z_243, Z_240, Z_231, Z_3×Z_81, Z_125, Z_3×Z_32, Z_3×Z_7²) hit the 900 s limit with weak dual bounds:
    inconclusive.
  - Reading:
    - Only F_3^4 (the bent mechanism, needs elementary abelian 3-rank) stands out, and cyclic Z_81 is the most
      restrictive.
    - At K <= 4 these numbers cannot distinguish exponent 2 from 3.
    - Conjecture CP below remains a reformulation of the Z problem, with only weak support from E37.
  - Observation kept: the Z_N transfer with N = t·q (q prime > 4X/t) is exactly a split coprime group Z_q × Z_t with
    ord t = q. So Conjecture CP, "|B_t| <= C K^β (β < 4) when Γ = Z_ℓ × H, ℓ prime, ℓ ∤ |H|", would transfer to Z.
    For large ℓ the fibres hold many runs, Galois adds nothing beyond integrality, and E37 shows CP needs more than
    coprimality at small K.
- **Kurtosis form of C½ (reformulation, PROVED identity).** With exact Fejér–Riesz f_A + M = |Q|², the autocorrelation r
  of Q's coefficients has r(0) = M, r(±a) = 1/2 on A and 0 elsewhere. Hence ‖Q‖_4^4/‖Q‖_2^4 = 1 + N/(2M²) = 1 + 1/(2R²).
  So C½ ⟺ every polynomial whose aperiodic autocorrelation is {0, 1/2}-valued off the origin has kurtosis <= 3 + o(1)
  (real-Gaussian value; Bu = real cosine sum). Sidon gives complex-Gaussian kurtosis 2 (R = 1/√2). Epoch ⟺ kurtosis
  unbounded. This is the opposite of merit-factor problems: two-valued off-peak autocorrelation with MANY nonzero values.
  - Strong form, consistent with all data (exhaustive N <= 42 min 0.5648; Bu decreasing to 1/2 from above): R(A) > 1/2
    for EVERY finite nonempty A. Recorded as a conjecture (C½-strong). Not assumed.

## 2026-10-18 (night, cont.) — Lemma OR(2), the O4-shaped class in Z: energy form and the reformulation through levels
- **Setting.** A = S ∪ (S+t), S a transversal mod t, s_y = y + t·k_y, s'_y = s_y + t/2. Then f_A(x) = 2cos(tx/2)·g(x) with
  g = Σ_y cos(s'_y x), and f_A(x + 2πj/t) = 2cos(tx/2)·w_j(x) where w_j = Re v̂_x(j) and v_x(y) = e^{i s'_y x}.
- **Energy form (lead; proof sketch, constants unoptimized).** For x in the "good" set G (cos(tx/2) >= 1/2 and
  Σ_y cos((s'_y + s'_{−y})x) >= −t/2), every w_j >= −M.
  - Then Σ_j w_j = t·cos(s'_0 x) and Σ_j w_j² >= t²/4.
  - Write P = Σ w^+ <= t(M + 1) and Q₂ = Σ_{w>0} w² >= t²/4 − tM². Hölder (Σw² <= (Σw)^{2/3}(Σw⁴)^{1/3}) gives
    Σ_j |v̂_x(j)|⁴ >= Q₂³/P² >= t⁴/(512(M+1)²) when M² <= t/8.
  - Integrate over x, using ∫Σ_j|v̂_x(j)|⁴ = t·E(S) (additive energy). This gives (M + 1)² >= |G|·t³/(512·E(S)).
  - So the class satisfies M >~ √(t³/E(S)): Chowla when S is near-Sidon (E(S) = O(t²)), exponent δ when
    E(S) <= t^{3−2δ}.
  - **Gap:** |G| >= c needs care when the m_y = s'_y + s'_{−y} cluster at small multiples of t. It holds in the examples
    checked by hand (all m_y = t or 2t). Not yet written as a full proof.
- **Meaning.** This is the pseudo-random half of a dichotomy; it is standard in flavor (energy instead of Schur triples).
  The structured half (E(S) >= t^{3−δ}, S near a GAP) is exactly where O4 lives in groups: a graph of a level function
  k: Z_t → Z with Gauss-sum phases. That half is where torsion-freeness must enter.
- **Level reformulation of the structured half.** At x = 2π(j + φ)/t: v_x(y) = e^{2πi(j+φ)(y + t/2)/t}·e^{2πi k_y φ}. So for
  every φ the vector y ↦ e^{2πi k_y φ}·e^{2πiφ y/t} (DFT index j) needs DFT real parts >= −M/(2cos πφ), uniformly in φ.
  - At φ = 1/4 the factors are i^{k_y}: this is O4's condition, except for the slow twist e^{2πiy/(4t)} that Z adds.
  - At other φ the levels rotate with speeds k_y.
  - Groups see only φ ∈ (1/4)Z. Z must satisfy the condition at every φ. A proof in the structured case should show that
    no level function k (with S near a GAP) keeps the DFT of e^{2πi k_y φ} one-sided for a positive measure of φ.
- **E38 consistent:** under equal search effort the class is 0.04–0.08 worse than unrestricted sets, and the gap grows
  with N.

## 2026-10-18 (late night) — Branch 2: where torsion-freeness enters the O4-shaped class (cohomological view)
- **Setup.** A transversal S = {s_y = y + t·k_y : y ∈ Z_t} is a set-theoretic section of Z → Z_t. Its additive defect
      d(y₁,y₂) := (s_{y₁} + s_{y₂} − s_{y₁+y₂})/t = k_{y₁} + k_{y₂} − k_{y₁+y₂} + carry(y₁,y₂) ∈ Z
  is a 2-cocycle, cohomologous to the carry cocycle. The extension 0 → Z →(×t) Z → Z_t → 0 does not split, because Z is
  torsion-free, so d ≡ 0 is impossible. In O4 the corresponding extension of Z_4 by GR(4,a) is torsion: sections with
  zero defect exist, and the Gauss-sum phases ride on top of them. **This is the precise point where Z differs.**
- **Averaging identity (PROVED, one line).** For each y₁, Σ_{y₂ ∈ Z_t} d(y₁,y₂) = s_{y₁}. So the mean defect in row y₁ is
  k_{y₁} + y₁/t: spread-out levels force large defects on average.
- **Third moment of the twisted function (PROVED computation).**
  - Write H := ψ·Re G, where G = Σ_y e^{i s'_y x}, s'_y = s_y + t/2 and ψ = sign cos(tx/2). The condition f_A >= −M
    reads H >= −M/(2|cos(tx/2)|).
  - ψ has frequencies at the odd multiples (2d+1)t/2, with coefficients (4/π)(−1)^d/(2d+1). Hence
        ∫ ψ (Re G)³ = (3/8)·(4/π)·Σ_{y₁+y₂ ≡ y₃} (−1)^{d}/(2d+1) + (all-plus terms),   d = d(y₁,y₂).
  - The third moment is therefore a weighted count of pairs with SMALL defect (weights ~ 1/|d|).
- **Dichotomy (proof plan, not a proof).**
  - (a) Levels confined to a range L: the macroscopic profile of A is a step function in L blocks of length t. Its
    transform is ≈ 2(sin θ/θ)·Σ_ℓ n_ℓ cos((ℓ+1)θ), with θ = tx and n_ℓ = #{y : k_y = ℓ}. A nonnegative-coefficient
    cosine polynomial with no constant term dips to about −t/L, so M >~ t/L (heuristic Gibbs; needs a rigorous
    version).
  - (b) Defects typically large (few pairs with |d| <= J): the third moment is <~ t²/J, the Roth-type argument gives
    M >~ √t once t²/J <~ t^{3/2}, and the energy form above is the same mechanism.
  - (c) The hard middle: many small-defect pairs with a large level range. Example: linear levels k_y = ⌊βy⌋, which give
    d ∈ {0, −1} on the pairs without wrap-around (about half) and d ≈ βt + 1 on the others. Then S is essentially an AP
    with step 1 + βt, and A = AP ∪ (AP + t) has a Dirichlet lobe, M ~ t.
  - So case (c) should reduce to "a large small-defect set forces Bohr/AP structure (rank 1, since Z_t is cyclic), and
    rank-1 structure forces a Gibbs lobe". The cyclic source Z_t is what should make this rank-1, unlike the high-rank
    Galois-ring sections of O4.
- **Next derivation.** Make (c) quantitative in the simplest form: if #{(y₁,y₂) : d(y₁,y₂) ∈ {0,−1}} >= δt², show that S
  has a subset of size >= δ^{O(1)} t lying in an AP of length O_δ(t) and common difference q ≡ 1 (mod t)
  (BSG-type for sections). Then show that such a piece costs M >~ δ^{O(1)}·t via a localized Fejér test function on the
  frequency 1/q-scale. Check case (a)'s Gibbs bound rigorously. If both hold, Lemma OR(2) (Chowla for transversal 2-run
  sets) follows with polynomial losses in δ. That would be the first lower bound that genuinely uses torsion-freeness.

## 2026-10-18 (late night, cont.) — Branch 2 reassessed: OR(2) is not a simplification; the dense regime is the common crux
- **E40** (EXPERIMENTS) tested the dichotomy on transversal 2-run sets. Uniform level profiles give M ≈ 0.44·t for every
  level range L: a Gibbs lobe from the flat profile. Tapered random levels drop to M ≈ 5–6·√t (fluctuation scale).
  The O4-like Z_4 quadratic levels give M ∝ t in Z.
- **The energy half is the standard energy bound (no new content).** Since E(S ∪ (S+t)) <= 16·E(S), the factorized
  argument M >~ t^{3/2}/(√E(S)·log t) is the general bound M >~ |A|^{3/2}/√E(A) with an extra log. Demoted.
- **The structured half contains the dense-profile problem.** A transversal with level range L is a dense subset of
  [0, (L+1)t). E40's tapered random levels sit at the fluctuation scale, exactly like dense sets in Z. So proving OR(2)
  needs Chowla for (special) dense sets, the regime the construction track calls live.
- **Rotation sweep: C½ holds in the dilated sub-family (PROVED, elementary).**
  - Let Y be a full section of Z_t, q ≡ 1 (mod t) with q >> t², S = qY and A = S ∪ (S+t). Then exactly
        f_A(x) = 2cos(α)·Re(e^{iα} F_Y(qx)),   α = tx/2.
  - As x moves through a window of width 2π/q, θ = qx covers a full period while α changes by πt/q. Hence
        M(A) = max_θ (|F_Y(θ)| − f_Y(θ)) + O(t²/q)   (choose 2α = π − arg F_Y(θ)).
  - So M(A) >= max_θ |Im F_Y(θ)| >= ‖Im F_Y‖_2 = √((t − [0∈Y])/2), and R(A) = M/√(2t) >= 1/2 − o(1).
  - The slowly rotating phase exposes the sine sum. Groups have only finitely many phases (φ ∈ (1/4)Z in O4), so they
    escape this; it is a genuine continuum effect.
  - In general S is not periodic and the sweep is not free. Any OR(2) proof must find a substitute for it.
- **Strategic review (skill §3).**
  - Distance: branch 2 aimed to isolate torsion-freeness in the O4-shaped class. Every route through OR(2) lands either
    in the standard energy bound or in the dense-profile problem. E10 already showed that "no subgroups" (Z_p prime)
    does not give C½ in the sparse regime (cyclotomic classes reach grid-R ≈ 0.31). The decisive Z-feature is
    continuity: all x, not one grid.
  - Kill: OR(2) as the branch-2 vehicle. It stays a test case (the rotation sweep above is its one clean output).
  - Pivot: **line D — the dense regime as the common crux of both tracks.**
    - Lower-bound side: Chowla for dense sets is open even in the cleanest finite model. For symmetric A ⊂ Z_p with
      |A| = (p+1)/2, Sanders (Israel J. Math. 179 (2010), arXiv 0807.5104v2, Thm 1.2 and the remark after it) proves
      M >= c·p^{1/3}; Spencer gives O(p^{1/2}); Sanders: "It seems interesting to try to close this gap."
    - For general density α, Sanders' Thm 4.1 gives exponent α/5 only. Bedert (2509.05260v3) cites only Sanders' dense
      result. Dense A ⊂ [1, X] embed into Z_p, so lower bounds transfer to Z. Constructions do not transfer (off-grid
      values).
    - Construction side: the dense FR-support regime is the live candidate (construction agent running).
- **Line D, first formulation (PROVED identities).**
  - Let A ⊂ Z_p^* be symmetric with |A| = (p ± 1)/2, g = 2·1_A − 1 (a ±1 function) and λ = 2M_p(A). Unnormalized DFT:
    ĝ(0) = ±1, ĝ(γ) = 2·1̂_A(γ) >= −λ for γ ≠ 0.
  - Since g² = 1, Σ_γ ĝ(γ)ĝ(δ−γ) = p²·[δ = 0]. With h := ĝ + λ >= 0 this says that h*h is constant off the origin:
        (h*h)(δ) = pλ(λ + 2)·(1 + O(1/λ)) for δ ≠ 0,  Σh = p(1 + λ) + O(1),  Σh² = p² + O(pλ²).
    So h is a nonnegative weighted difference set in Z_p. In the exactly two-valued case h = c·1_D, D would be a
    symmetric (p, λ², λ⁴/p)-type difference set with real character values ±λ. Paley (λ ≈ √p) is the 3-valued
    near-instance.
  - **Elementary p^{1/4} (PROVED).** Let Λ = max_{γ≠0} ĝ(γ). From Σ_{γ≠0}ĝ² = p² − 1 and Σ|ĝ| <= p + 2λp we get
    Λ >= (p² − 1)/(p(1 + 2λ)). The identity at δ = 2γ₁ (with ĝ(γ₁) = Λ) bounds the mixed-sign terms by 2λΣĝ⁺ and gives
    Λ² <= 2λ + 2λp(1 + λ). Together: λ⁴ >~ p/8, i.e. M_p >= (1/2)(p/8)^{1/4}(1 − o(1)).
    Sanders' 1/3 needs his r-fold boolean convolutions (Lemma 3.2, r = 2⌈1/α⌉).
  - Single-coefficient and energy (E(h·1_Γ)) refinements reproduce p^{1/4} and no more. A random level set
    Γ = {h >= p^{2/3}} of size p^{2/3} is consistent with all the second-order constraints at λ = p^{1/3}. To beat 1/3,
    one must use that h*h is EXACTLY constant (difference-set rigidity) or higher boolean structure.
- **E41 (started).** Exact min M_p over half-sets of Z_p by branch and bound (src/zp_half.c). For p <= 53:
  - The optima are Paley for p = 13, 17, 29.
  - From p = 37 on, the optima are dilates of near-intervals with a tail. This is the anatomy of the dense Z optima.
  - M/√p falls from 0.72 (p = 11) to 0.519 (p = 47) and 0.543 (p = 53), already below Paley's (1 + √p)/(2√p).
  - Discriminating question: does M_p/√p level off near 1/2 (dense Chowla plausible in Z_p) or keep falling towards the
    Sanders scale p^{−1/6}? Near-intervals in Z_p are exactly the grid shadows of dense Z sets. So the same question
    decides whether off-grid (continuum) information is needed even in the dense case.
- **E41 completed to p = 89 (exact) and p = 797 (heuristic).**
  - Exact half-set optima in Z_p go below grid-R 1/2 at p = 71, 79, 83, 89 (0.491 at p = 89). They are dilated near-intervals with tails:
    one giant profile coefficient and a flat floor.
  - Heuristics stay sub-Paley up to p = 197 and are search-limited beyond.
  - So in Z_p, C½ fails for dense sets too (as E10 showed for sparse cyclotomic classes). Z_p only constrains the
    critically sampled frequencies; the full circle in Z does not allow this.
  - For Sanders' question (p^{1/3} vs p^{1/2}) the data are consistent with both a + b/√p (a ≈ 0.35) and p^{−0.2}
    decay of M_p/√p. Not decided.
  - Decision: line D's numerical half has delivered what it can cheaply. The theoretical half (exponent > 1/3 via
    difference-set rigidity) stays open but is a side question for Z; the Z-relevant content is the anatomy (profile
    plus tail), which matches the Z dense optima.
- **Where a Z-specific run-top bound must come from (reductions, PROVED-trivial; recorded to stop re-deriving them).**
  - (i) The chain needs Σ_{t∈A}|B_t| <= n·K^{4−δ}. Since |B_t| <= |A ∩ (A+t)|, it suffices that
    max_t |A ∩ (A+t)| <= K^{4−δ}.
  - Restricted to sets made of t-runs of length exactly 2 (A = S ∪ (S+t), S ∩ (S + jt) = ∅ for j = ±1, ±2), both
    statements are the same: "OR(2)-weak", M(S ∪ (S+t)) >= c|S|^{1/4+δ}. Groups violate it (O4: every run is a
    2-run, K ~ |A|^{1/4}). Numerically Z is far from violating it (E38: R ≈ 0.6; E40: M ≈ 5√t).
    So OR(2)-weak is the minimal Z-statement any improvement of the run-top route must contain.
  - (ii) The natural group formulation, G_arc with all t-runs of length <= η·ord(t) and η -> 0, is the Z problem
    itself via the Z_N transfer (N >> max A makes η arbitrarily small). It is not a reduction.
  - (iii) The one Z-feature expressible in finite groups is localization: A sits in an arc of length X << N in Z_N.
    That allows localizing x at any scale 1/H with H <= X, hence local profiles (Gibbs at every scale and location).
    O4 spreads over its whole group and has no scale.
  - (iv) A local rotation sweep (S inside a window of width w << t) gives M >~ 2|F_S(x₀)| under a Diophantine condition
    on c/t. That is large only when S is dense in a short window, the trivial (Dirichlet) regime. The dilated case
    worked because F_{qY}(x) = F_Y(qx) is 2π/q-periodic (Bohr structure).
  - Conclusion: the next lower-bound attempt should combine localization (local profiles at scale H with 1 << H << t)
    with the 2-run structure; there is no shortcut through group statements.
- **P24 (localization lemma, PROVED, one line):** |Σ_a (1 − |a−m|/H)_+ e^{iax₀}| <= 2M + 2N(H) for all m >= H and all
  x₀. Corollaries: A ⊂ [Y, 2Y] ⟹ M >= |A|/4; small M forces a multiplicative spread >= √n/(4c); shell growth
  N(2H) <= 9N(H) + 8M; local Fourier uniformity at every scale. It is the rigorous macroscopic-Gibbs tool. It holds in
  Z_N only for localized sets, so it is genuinely Z-specific. It is far from √n by itself (Singer/Bu satisfy it
  easily). Next: combine P24 at scale H << t with the 2-run structure (OR(2)-weak) and with Roth's triple count.

## 2026-10-18 (late night, after the Gurobi switch) — dual view, two-scale decoupling, line-D reformulation
- Process change (user, 2026-10-18): computations are fire-and-forget; foreground time goes to math. A codex agent
  works OR(2)-weak in parallel (.research/agents/or2_brief.md).
- **Every valid inequality is an average.** M = max over probability measures μ of −∫f dμ (Herglotz duality).
  P24/P25 use weights F_H(y)(1 + cos(my + φ)). The k-term generalisation F_H(y)|Σ_j c_j e^{im_j y}|² gives:
  for each x₀, the H-decimated local-sum sequence k ↦ L_{kH}(x₀), Hermitian-extended with diagonal
  2(g_H(x₀) + M), is positive definite. That captures the Gibbs lobes (interval: M >~ 0.1X). But its spectral density
  is an interpolation of f on the coset x₀ + (2π/H)Z, i.e. again an average of f >= −M. A fixed family of weights
  can only reproduce f >= −M; a √n bound needs weights chosen ADAPTIVELY from A (max-cut / signing view of
  Cay(Z, ±A)). JMTZ do exactly that via cliques and are capped at 1/6. Räty–Sudakov–Tomon (arXiv 2311.02070,
  positive discrepancy and MaxCut) bound λ₂, not λ_min, so they do not apply directly.
- **P25 (sharpened localization, PROVED):** |L_m(x₀)| <= 2M + 2(f ∗ F_H)(x₀). Corollaries:
  - flat-minimum rigidity;
  - an L² form that random dense sets saturate.
  Missing mechanism, stated precisely: show that the energy of A ∩ [2H, X] (smoothed at 1/H) cannot concentrate on
  Pos_H = {f ∗ F_H > 0}, a set determined by A ∩ [1, H].
  - If it is spread, P25 gives M² >~ (1 − ρ)nH/X, i.e. dense Chowla.
  - If it concentrates, high and low parts are aligned (B + P-type product structure). Aligned examples (sumsets with
    progressions) have linear M via the Dirichlet lobe.
  So a dichotomy "aligned ⇒ large M via rotation" is the target. Not yet proved; it is the dense analogue of OR(2).
- **P26 (PROVED):** symmetric half-sets of Z_p ⟺ symmetric u >= 0 with u ⋆ u = δ₀ + ε (weighted near-planar sets);
  2M_p = Σu ∓ 1. The elementary p^{1/4} is the non-symmetric planar bound. Natural Singer-based symmetric weights are
  killed by the E41 exact data (2M_p ≈ √p at p = 13, 31, 73).
- Gurobi A/B (E43/E44): MIPNODE user cuts slow node throughput ~4x and lose. Plain lazy-cut model kept.

## 2026-10-19 — Turán constraints, the scale they act on, and the spike-share reformulation (lead)
1. P29 (PROVED, PROOFS): Fejér-grid weights give X·M >= h·n − (X + h)(h − 1)/2, hence M >= (n − X/2)²/(2X).
   - Density > 1/2 in [1, max A] forces linear M. This is the discrete Turán bound (∫φ <= φ(0) for p.d. φ on [−1, 1]).
   - P29(b), twisted form: f_A(x₀) <= ((X + h)/h)(f ∗ F_h)(x₀) + (X/h)M. Peaks must be front-loaded.
   - Consequence: near-extremal sets have density <= 1/2 + O(n^{−1/4}). The dense records (0.69–0.74 at X <= 72)
     are pre-asymptotic.
2. Scale of Turán. Every fixed or Fejér-type weight constrains the local (twisted) profile only up to error M/X.
   - For a TYPICAL set, √n-scale noise has profile size √n/X ≍ M/X, so Turán says nothing. That is why P29/P25-type
     inequalities are blind to the noise.
   - For a COUNTEREXAMPLE the situation reverses (elementary, PROVED):
         (1/2π)∫_{f > KM} f² >= (n/2)(1 − 2(1 + K)R²),
     from ∫_{f <= KM} f² <= (K + 1)M·∫f⁻ and ∫f⁻ <= 2πM.
   - So R -> 0 puts almost all of ‖f‖₂² on spikes of height >= K·M with K -> ∞. Their profiles have size >> M/X:
     exactly the regime where the Turán/p.d. constraints bite with relative error -> 0.
3. P30 (CONJECTURED; sufficient for Chowla). There are K and ρ < 1 such that for every A,
       share_{>KM}(A) := (1/2π)∫_{f_A > K·M(A)} f_A² / (|A|/2) <= ρ.
   It implies R(A)² >= (1 − ρ)/(2(1 + K)) for all A. Example: K = 4, ρ = 1/2 would give R >= 0.22.
   Heuristic support (profile model, NOT proved):
   - A spike at x₀ of height P >> M has a twisted profile φ_{x₀}(t) whose Hermitian extension must be p.d. up to M/X.
   - Bessel in the internal variable: Σ_{x₀} |φ_{x₀}(t)|² <= φ_0(t).
   - p.d. gives |φ_{x₀}(t)| <= φ_{x₀}(0). Turán gives ∫ φ_0 <= φ_0(0)/2.
   - Triangle shapes give total spike share <= 2/3. Optimal shapes give the doubly-positive constant ρ* ≈ 0.72
     (P17: <= 0.9057 proved for one profile).
   - At the threshold density φ_0(0) = 1 the Bessel identity even forbids all twisted peaks.
   Exact gaps:
   - (G1) a rigorous multi-scale profile decomposition: spikes can have different widths, and blocks far from 0
     rotate (front-loading, P29(b)).
   - (G2) error accumulation over at most ~R²X peaks (looks harmless).
   - (G3) turning "p.d. up to M/X for every test w >= 0" (which, per peak, is a tautology: it is f >= −M) into a
     JOINT constraint across peaks, via the {0,1}-valuedness / Bessel coupling. G3 is the real content.
   Test: E47 (src/e47_spike_share.py) measures share_{>KM} on records, Bu sets and random sets.
4. E47 result (EXPERIMENTS): share_{>KM} at large K plateaus at the CENTRAL profile peak.
   - Singer–Bu q = 61..401: 0.505–0.545.
   - Dense records: 0.66–0.78 at K = 8.
   - Triangle-tapered random set: 0.65 (triangle prediction ∫φ²/∫φ = 2/3).
   - Bu's non-central mass sits at levels below 4M.
   So a construction with R -> 0 must move the >= 1 − ρ* ≈ 28% "noise" mass into SECONDARY spikes far above M.
   None of our families does this.
5. Heuristic DENSE-CHOWLA argument in Z (the joint constraint G3 made explicit).
   Peak profiles ψ_{x₀} are Hermitian, p.d. up to relative O(1/K), supported in [−1, 1]. Let c_{x₀} = ψ_{x₀}(0),
   c₀ = ψ_0(0) <= 1 (density near 0), s = ∫_{−1}^{1} ψ_0 = 2δ.
   Inputs:
   - central: ∫ψ_0² <= ρ*·c₀·s (doubly positive);
   - twisted: ∫|ψ_{x₀}|² <= ‖|u|⋆|ũ|‖² <= ρ*·c_{x₀}² (ψ = u⋆ũ, supp u of length <= 1);
   - Turán: s <= c₀;
   - Bessel at t = 0 with constant β: c₀² + Σ_{x₀≠0}|c_{x₀}|² <= β·c₀.
   Conclusion: share <= ρ*[c₀s + βc₀ − c₀²]/s, maximized at c₀ = (s + β)/2, giving ρ*(s + β)²/(4s).
   - β = 1, ρ* = 0.724 (numerical): share < 1 for δ > 0.16.
   - β = 1, ρ* <= 0.9057 (P17, proved): share < 1 for δ > 0.29.
   Then R² >= (1 − share)/(2(1 + K)), i.e. CHOWLA FOR DENSE SETS in Z. P29 already covers δ > 1/2.
   Sensitivity: the argument dies if β >= 1.38 (with ρ* = 0.724, at δ = 1/2) or β >= 1.10 (with 0.9057).
   BOTTLENECK, a two-scale Bessel inequality:
   - For one resolution it is fine. With triangle-smoothed values at t = 0 (half-width N) and peaks δ-separated,
     duality gives the Gram bound β <= 1 + 6.6/(Nδ)² (PROVED: off-diagonal Fejér decay).
   - The covering of {f > KM} needs separation ~ resolution, so Nδ ~ 1 and β ~ 2.
   - Wide peaks (narrow profiles, i.e. structure in A ∩ [1, ℓX]) have smoothed values << their true ψ(0). Their
     mass <= ρ*c²ℓ is small, but summing dyadic scales with SEPARATE budgets loses a factor 2.
   - Needed: one joint budget across scales.
   Candidate fix: profiles of width ℓ use the Bessel budget only on t ∈ [0, ℓ]. Peaks wider than the resolution
   could then be charged to the low part A ∩ [1, ℓX], whose total budget is |A ∩ [1, ℓX]| <= ℓX.
   That is a multi-scale large sieve with p.d. weights. Not attempted further today.
   Status: HEURISTIC with the gap located precisely. Novelty of the dense-Z question: to check before investing
   days (Z_p dense is open: Sanders p^{1/3} vs p^{1/2}).
