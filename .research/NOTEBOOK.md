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

## 2026-10-19 — The decisive target (lead): everything now reduces to one statement about secondary spikes
Already in hand (PROVED unless noted):
- (a) Spike inequality: (1/2π)∫_{f > KM} f² >= (n/2)(1 − 2(1 + K)R²). If R -> 0, almost all of ‖f‖₂² sits in spikes
  far above M.
- (b) Filter 2, window-noise lemma (PROVED, Hölder applied inside P28). For every window m >= H and c > 0, with
  U = {|x| > c/H} (outside the window's own profile spike):
      M >= ½√(ν_m/κ_m),
  - ν_m = (1/2π)∫_U |L_m|² is the noise mass;
  - κ_m = (1/2π)∫_U |L_m|⁴ / ν_m² is the noise kurtosis (≈ 2 for Gaussian noise).
  So M >= c√n unless EVERY window's noise is spiky.
- (c) P31: the central profile peak plus front-loading is handled unless A is front-loaded at every scale.
- (d) E47: in every known family the central peak carries <= ~0.72 of the mass. Nobody has put mass into
  secondary spikes.
DECISIVE TARGET (P30 restated): secondary spikes far above M cannot carry the remaining >= 1 − ρ* ≈ 28% of ‖f‖₂².
- Each secondary spike at x₀ has a twisted profile that must be p.d. up to M/X (Turán/P29(b) at x₀).
- The profiles of different spikes are Fourier coefficients of the SAME 0/1 sequence.
- Missing piece (G3): a coupling inequality that loses no constant. Single-resolution Bessel (β -> 1) works.
  Multi-scale needs a joint budget.
Two concrete routes to try next:
- (R1) P31-style averaging instead of Bessel. P31 avoided Bessel entirely by integrating window inequalities over
  x₀. Do the same with a weight μ(x₀) >= 0 concentrated on the spike set S = {f > KM}:
      ∫(f + M)²(F² ∗ μ) <= ρ(L + 1)∫μ(x₀)(M + g(x₀))²dx₀,   g = f ∗ F.
  The left side sees spike mass. The right side is the low-pass value on S, whose Parseval budget is S_A. Question:
  can μ be chosen so the right side uses only part of the low budget, giving share < 1? First check: what μ does
  P31's proof implicitly use (uniform), and how much slack is there when spikes occupy measure <= 2π/K?
- (R2) Local P31 at each spike with a window of width matched to the spike's profile, then sum. The windows overlap
  only on a set of small measure (spikes cover <= 2π/K). Hope: the overlap error is O(1/K), not O(1), which is
  exactly what a multi-scale Bessel lacked.
Test sets for both: Bu q = 61–401, dense records, triangle-random, squares {k²} (linear M through Gauss-sum peaks).
Squares are the canonical locally deterministic, front-loaded family, and filter 3 must explain their negative peaks.
- (R3) Cross-scale spike support (lead, same day). This sharpens R2 and is the current best bet.
  Local P31 at x₀:
      (1/2π)∫F_w(x − x₀)²(f + M)² <= ρ(X + w + 1)(M + g(x₀))²,   g = f ∗ F_w.
  Integrate x₀ over E = (secondary spike set of f) + [−c/w, c/w], EXCLUDING |x₀| < C/w. This gives
      (1 − O(c^{−3}))·W·m_sec(f) <= ρ(X + w + 1)·(1/2π)∫_E (M + g)².
  - The central profile peak of g sits at |x| < C/w, so it no longer appears on the right. The front-loading
    obstruction to low-pass P31 came exactly from that peak.
  - The right side sees only g's NOISE on E. P29(b) says every secondary spike of f needs a matching spike of g.
  - Recursion: g >= −M with mean 0 obeys the same spike inequality at its own scale, with its own central share
    <= ρ*-type and its own noise.
  - Extreme case, full front A ⊇ [1, w]: g = (F_w − 1)/2 has no noise. Then f has (almost) no secondary spike mass,
    so f's noise (>= 1 − ρ* of ‖f‖² by the central-share bound) lies below K·M, and (a) forces M >~ √n.
    CANDIDATE PROOF for full-front sets.
  - General fronts (density d < 1 near 0): the low part carries noise mass ~ Σκ²d(1 − d) that can support f's
    secondary spikes. Need the constants across consecutive scales to give a contracting recursion, using the
    exact P31 constant (no Bessel loss) and the central-share bound at every scale.
  - FIRST CONCRETE STEP: write the two-scale inequality with all constants
        m_sec(f) <= [ρ(X + w + 1)/((1 − O(c^{−3}))W)]·[(1 + η) noise_E(g) + (1 + 1/η)M²|E|],
    and test it numerically on Bu, dense records and triangle-random: how much of g's noise actually lies on E?

## 2026-10-19 (cont.) — Per-spike contraction criterion, subgroup rigidity, and the self-reducibility conjecture (lead)
1. Per-spike contraction (from P32, profile model).
   - A secondary spike at x₀ with twisted profile ψ(t) (t = a/X) has m_f ≈ X∫|ψ|².
   - Its low-pass image has m_g ≈ X∫|ψ|²κ(tX)². So the P32 step multiplies spike mass by
         Γ(ψ) := (3ρ/2)(1 + X/w)·∫|ψ|²κ²/∫|ψ|².
   - Uniform |ψ| with w = εX: Γ = (ρ/2)(1 + ε) < 1. CONTRACTS.
   - Front-loaded ψ (mass near t = 0): Γ -> (3ρ/2)(1 + 1/ε) > 1. P31's obstruction, now per spike.
   - So the recursion can fail only through spikes whose twisted profiles are front-loaded: the FRONT A ∩ [1, εX]
     carries the twisted bias at x₀ disproportionately.
2. What front-loaded twisted profiles force.
   - x₀ = 2πr/q rational: A's front is biased mod q, and the spike sign condition (all large spikes positive, else
     M is linear) asks the local residue pattern P ⊂ Z_q to be (nearly) positive definite.
   - LEMMA (classical; PROVED). If 1_P on a finite abelian group G is positive definite with 0 ∈ P, then P is a
     subgroup.
     Proof: K(x, y) = 1_P(x − y) is PSD with unit diagonal and 0/1 entries. K(x, y) = 1 gives
     ‖e_x − e_y‖_K² = 0, so rows x and y agree. Hence x ~ y ⟺ x − y ∈ P is an equivalence relation.
   - Stability version = Sanders' dense-group Chowla theorem (0807.5104): near-p.d. dense patterns are close to
     subgroups. So locally A ≈ union of cosets of dZ_q: a LOCAL DILATION.
   - Irrational x₀: the analogue is Bohr-type patterns. Sharp Bohr windows give sinc-signed spikes (E46: linear M).
     Tapered windows need thinning, i.e. noise.
   - Unions of different progressions are not p.d. modulo the lcm (inclusion–exclusion puts negative spikes at the
     lcm frequencies). Nested chains collapse to one progression.
   - Pieces dZ ∩ [Y₁, Y₂] not starting near 0 rotate in phase (P29(b)), giving linear dips.
   So the arithmetic structure must be ONE dilation d, front-loaded from 0.
3. SELF-REDUCIBILITY CONJECTURE (SR). For every ε > 0 there are η(ε) -> 0 and c > 0 such that, if R(A) <= ε, then
   either:
   - (i) A is not front-loaded at some scale, so P31 gives R >= c (contradiction for small ε); or
   - (ii) all but an η-fraction of A lies in dZ for some d >= 2, and A' = (A ∩ dZ)/d has R(A') <= ε + η.
   Iterating (ii) raises the density by a factor d each time (max A' = X/d, |A'| ≈ |A|). Eventually density > 1/2 + ε,
   and P29 (Kolountzakis) gives linear M. Contradiction, hence Chowla (SR ⇒ Chowla, modulo summable η-losses).
   Ingredients:
   - P31/P32 (have);
   - per-spike contraction (above; profile model, to make rigorous);
   - Sanders-type local stability at rational spikes (cite + localize);
   - a Bohr-pattern analogue for irrational spikes (open);
   - control of the η-losses through the iteration (each junk element costs at most 1 in M: M(B ∪ T) >= M(B) − |T|).
4. Next concrete steps:
   - (a) make the per-spike contraction rigorous from P32, choosing E as a neighbourhood of ONE spike cluster at a time;
   - (b) state and prove a localized Sanders lemma: a spike at 2πr/q with height P >> M and a front-loaded twisted
     profile forces A's front to be near a union of cosets of a subgroup mod q, with explicit dependence;
   - (c) numerics: compute Γ(ψ) for the actual secondary spikes of Bu sets, dense records and arithmetic-front test
     sets (e.g. A = tapered(3Z ∩ [1, Y]) ∪ random tail).

## 2026-10-19 (late) — Strategic review: R3 killed; the P31 family is exhausted at "front-loading"; next mechanisms (lead)
1. R3 (P32 noise-transfer recursion) is KILLED.
   (a) Analytic. The bare recursion m_f <= Λ m_g <= … ends at a trivial bound. Each step costs
       Λθ = (3ρ/2)(1 + θ) > 1 for every θ, since ρ > 2/3. The chain grows.
   (b) E51. The P32 bound on secondary mass is B >= 1.7·(n/2) on every test set; Bu gives 2.7 at all n.
       τ ≈ 0.5–0.6 on Bu: g's mass really does sit on f's secondary spikes, since they come from the mod-3 dilation.
   The full-front step (STATE item) inherits P32's factor (1 + X/w). It only bites when R² << w₀/X, so it is useless for
   sparse fronts. Parked.
2. What the P31 family can and cannot give (all checked this session):
   - Statement. Any nonneg window Φ of degree D, and any PD reweighting ν̂ of f, give
         Σ_{a∈A}|Φ̂(a)|² >= (n/(ρ(X + D + 1)))·‖Φ̂‖² − 2M².
     This includes dilated Fejér windows (qZ), GAP windows J − J, Fejér×comb, L^p Nikolskii (p ≠ 2), 2-D lifting via
     triple products, and low-pass recursions.
   - Every such inequality is a FRONT-LOADING constraint:
     - A's weighted density near 0, along every PD pattern (APs qZ, Bohr/GAP sets), must be >= 2δ/ρ ≈ 2.6–2.9δ at
       every scale u in [3ρR²X, εX].
     - The low-pass recursion adds: front density is almost non-increasing in the scale, i.e. d(θw)/d(w) >= 0.97/(1 + θ).
   - Why the recursion cannot close. Each step multiplies the admissible density ratio by 2/(3ρ_eff(1 + θ)).
     It would force geometric growth, hence dense Chowla with M >= δ^C √n, iff the effective Nikolskii constant were
     < 2/3. But Fejér attains 2/3. A flat front makes the central window exactly Fejér-shaped, so eff -> (2/3)/(1 + θ)
     (E53). The gap 0.687 vs 2/3 cannot be closed by Nikolskii arguments alone. KILLED as a route to dense Chowla.
   - The constant 0.385 (0.344 numerical) is sharp for this method up to window-shape tweaks. The divisibility
     constraint (U vanishes at the (w+1)-th roots of unity) costs O(θ³) at small θ: no gain.
3. Front-loaded sets reduce to signed (Littlewood-type) problems.
   - Write f = P + N: P is the smooth profile part, N the fluctuation.
   - Smooth decreasing profiles have P >= −O(1). By Euler–Maclaurin the cosine transform is −φ'(0)/(Xx²) + …, plus
     the boundary term −φ(0)/2.
   - So all the difficulty sits in N, a SIGNED sum with two-valued coefficients {1 − p(a), −p(a)}.
   - Flat front of density 1/2: the low-pass fluctuation is a ±½ cosine sum with full support on [1, w]. Chowla for such
     fronts needs min <= −c√w for Littlewood-type cosine sums: Erdélyi's problem (his n^{1/3} claim has a gap, see
     LITERATURE).
   - This explains why window methods stall: they cannot see sign patterns.
4. Arithmetic is the only lever left. Two observations:
   - Bu saturates the dilation inequality exactly: M(A ∩ 3Z) <= M(A), |A ∩ 3Z| = n/2, R(D) = √2·R(A) = 1/√2 (E51).
   - Idealized SR. Suppose the spike set of f is a subgroup of order N_s ≈ R²X with spikes of height ≈ √n/R. Parseval
     on that subgroup gives Σ_c|A_c|² ≈ n/R², with A_c = A ∩ (c + N_s Z). This is (1/δ)× the equidistributed value, so
     A ≈ a union of δN_s FULL residue classes mod N_s. Spike signs force the class pattern P ⊂ Z_{N_s} to be PD. A PD
     0/1 pattern is a subgroup, so A ≈ dZ ∩ [1, X] with d = 1/δ: a dilated FULL interval, which P31 kills (M >> √n).
   - So in the idealized spike model, small R is contradictory. The real theorem needs a robust (Bohr / approximate-group)
     version. That is the SR program; the losses per step are the issue.
5. Active lines going forward (>= 3):
   - L1 (lower bound, structural): a robust SR₀. If many tall secondary spikes lie at rationals of one denominator q,
     then A is close to a union of residue classes mod q with a PD pattern. Combine with P31 on A_q.
     First derivation: a quantitative "near-PD 0/1 pattern on Z_q ⇒ near subgroup" lemma with √-loss, a localized
     Sanders. Test on Bu (pattern = {0} ∪ {1} mod 3 with weights).
   - L2 (construction): escape-class probes (E52, two-level profiles running), and a multiplicity-m generalisation of Bu.
     The counting bound for real-square identities ρ² with K terms and lag multiplicity m is R >= 1/(2√m), so m > 1 is
     REQUIRED to beat ½. Search for weighted Θ with all difference and sum multiplicities equal to m and aligned weights.
   - L3 (formalization): the Lean P31 chain. The conditional T3 is kernel-checked; T1 (Fejér–Riesz) is in progress.

## 2026-10-19 (late, cont.) — Construction track: dilation pinch, Bu as one step of a map, the BI-FLAT target (lead)
1. Dilation pinch (PROVED; elementary).
   - Statement. For every q >= 1: Σ_{j=0}^{q−1} f_A(2πj/q) = q|A ∩ qZ|, hence
         |A ∩ qZ| >= n/q − (1 − 1/q)M.
     A small-M set has at least its fair share in EVERY qZ, up to M.
   - An L² version (average (f + M)² over the q shifts, use Σg² <= (Σg)² for g >= 0) gives the weaker
     n <= q|A ∩ qZ| + 2(q − 1)M².
   - Consequences:
     - With A ∩ qZ = qD and E = A \ qZ: |E| <= (q − 1)|D| + (q − 1)M.
     - So R(A) >= R(D)/√q·(1 − o(1)): ONE dilation level gains at most √q.
     - Bu (q = 3, |E| = |D|) gains √2; the ceiling is √3.
2. The q = 3 geometry.
   - Write P(x) = f_D(3x) + M >= 0 and Z = Ẽ₁ + conj(Ẽ₂), with Ẽ_r the exponential sum over E ∩ (r + 3Z).
     Then f_A >= −M at x, x + 2π/3, x + 4π/3 iff Z(x) lies in the equilateral triangle {Re(ω^j z) >= −P(x)}: inradius
     P, circumradius 2P.
   - ‖Z‖² = |E|, since the cross term vanishes: positive vs negative frequencies.
   - Bu: Z = ½e^{ix}F(3x)² with F = F_S, so |Z| = P exactly. The incircle is safe for EVERY phase.
     Bu saturates the "phase-blind" bound |E| <= ‖P‖² = M² + |D|/2. For Sidon differences, M² = |D|/2, so |E| = |D|.
   - Beating the incircle needs phase control: Z near the vertices whenever |Z| > P. Polynomial phases are continuous, so
     exact vertex-locking is impossible; approximate locking is open.
3. Bu as a map, and the BI-FLAT target (precise).
   - Suppose V = Σ v_θ e^{iθy} satisfies, up to junk J₁, J₂:
         |V|² = 2M + 2f_D + J₁   (autocorrelation 1 on ±D, 0 elsewhere off 0)
         V²   = 2Ẽ_Σ + J₂       (autoconvolution 2 on Σ, 0 elsewhere).
   - Then A = 3D ∪ (3Σ + 1) has f_A = (Re(e^{ix/2}V(3x)))² − M − J₁(3x)/2 − ½Re(e^{ix}J₂(3x)).
     So M(A) <= M + (junk); Bu bounds the junk more cleverly than by ℓ¹.
   - Size: |Σ| = ‖½V²‖² = ∫P² = M² + |D|/2. Hence
         R(A)² = R(D)²/(1.5 + R(D)²).
     So R(A) < ½ iff R(D) < 1/√2.
   - Iterating, with every level admitting a bi-flat factor, gives R² -> 0 geometrically (factor 2/3 per level).
   - Known instance: Sidon S with v ≡ 1. Here R(D)² = k/(2(k − 1)) -> ½⁺ and R(A) -> ½ (Bu).
   - Obstruction to the naive iteration. A Bu set's natural factor is real/symmetric (ρ = Re(e^{ix/2}F)). Symmetric
     supports have autoconvolution = autocorrelation: ratio 1, but 2 is needed. The resulting next level is the
     (1 + cos x)-blow-up, with coefficients ½.
   - Counting. For a real v >= 0 with lag multiplicity m and aligned weights, R(A) >= ½√(‖v‖²/K) ~ 1/(2√m). So
     multiplicity m >= 2 is REQUIRED.
   - Small cases:
     - The parallelogram support {0, a, b, a + b} is infeasible: it forces v₀² + v₀^{−2} = 1.
     - Exact uniform multiplicity in Z is impossible for difference-set lifts: a difference set inside half the cyclic
       group would be a perfect Golomb ruler (K <= 4).
     - So any bi-flat V with m >= 2 must be APPROXIMATE, with Bu-style junk control.
4. NEXT (construction):
   - (a) Numerically search for approximate bi-flat V. Variables: complex v on a structured support (union of a Sidon
     set and its translate, GAP × Sidon, Singer-mod lifts with two weights). Objective: ℓ¹ deviation of the
     autocorrelation from {0, 1} plus that of the autoconvolution from {0, 2}, against ‖v‖²/Σ-count.
   - (b) Phase-locking: can Z = ½e^{ix}F² + δZ, with δZ supported on the class-2 frequencies, push |E| above ‖P‖²
     while staying in the triangle?

## 2026-10-19 (late, cont. 2) — Why the P31 family stops; the nonlinear requirement (lead)
- Meta-observation (rigorous in form). Every window/Nikolskii argument that integrates SECOND moments over x₀
  (P29, P31, P32, general PD windows Φ, PD reweightings, dilated windows) reduces, via Parseval and 1_A² = 1_A, to
  inequalities LINEAR in 1_A: W·|A| <= C·Σ_{a∈A}|Φ̂(a)|² + O(CM²). These are profile constraints.
  - The escape class satisfies them all, so any proof for it must use NONLINEAR information (additive structure).
  - E57: the first nonlinear upgrade (L⁴ window) is weaker than P31 on random-like profiles.
- Classical nonlinear facts for reference (third moment; probably folklore):
  - Cauchy–Schwarz (∫(f + M)²)² <= ∫(f + M)·∫(f + M)³ gives
        n²/4 <= M²n/2 + (3/4)M·T,   T = #{(a, b, c) ∈ A³ : a + b = c}.
  - So M >= min(½√n, n²/(6T)), and sum-free sets have M >= √(n/2).
  - A counterexample family needs T >= n^{3/2}/(6R): many Schur triples. This is automatic for dense sets, so it is no
    help there.
  - Cayley form: λ_min(Cay(Z, ±A)) = −2M. The neighbourhood of 0 must have edge density >= (1 − 2R²)/(2M).
- Dense small sets are where L⁴ helps (N50: 0.257 vs 0.208). A combined L²/L⁴ optimisation over windows could sharpen
  the dense constants. That is incremental, so it is parked.

## 2026-10-19 (late, cont. 3) — Weighted window inequality (a nonlinear certificate) and its spike-model reading (lead)
Statement (PROVED):
- Integrate P31's pointwise window bound Q(x₀) <= C·s(x₀)² (s = M + g) against the weight 1/s.
- Then use Jensen in the form ∫F²/s >= W²/(F² ∗ s).
- Result: with G := f ∗ Φ, Φ = F ∗ F²/W (nonneg, mass 1, degree <= w, so G >= −M),
      (1/2π)∫(f + M)²/(M + G) <= (C/W)·M,    C = ρ_L(L + 1),  C/W ≈ (3ρ/2)(1 + X/w).
- Nonlinear in A, because the weight depends on A through G.
Consequence (PROVED): f's L² mass on {G <= KM} is <= (K + 1)(C/W)M². So as R -> 0, all of f's L² sits where the
low-pass G is >> M. This is the P32 spike-support statement in one line, with constant (C/W)(K + 1).
Spike-model reading (HEURISTIC):
- For isolated spikes, Σ m_i/G_i ≈ (shape constant)·(X/w)·M. The inequality is again a per-spike SHAPE condition
  (L²/L¹ ratio of the spike against the kernel peak), so no contradiction as R -> 0.
- Spikes clustered within 1/w raise G and make the inequality EASIER. So the extremal configurations for evading it
  are clustered spike families, i.e. dilation-like structures again.
Status: a recorded tool, not a route. Parked.

## 2026-10-19 (night) — P34: the one-sided Littlewood problem falls to P31; the escape class contains Bu (lead)
1. The P31 window chain only sees the coefficient-energy profile |b_j|². For T = Σ_{j<=n} cos(jt − θ_j) (unit amplitudes,
   any phases) the profile is flat, so the chain closes:
   - −min T >= 0.28√n (P31-E constant) and >= 0.189√n with the trivial Nikolskii constant;
   - the same for max T.
   Sharp order (Rudin–Shapiro). Erdélyi 2607.21877 (July 2026) claims n^{1/3}/60 for this exact class and records only the
   trivial two-sided √n. PROOFS P34, note .research/notes/littlewood_onesided_P34.md. E61: optimum ≈ 0.61√n.
   - Status: proved on paper. The 0/1 instance is kernel-checked. Next Lean task: the complex-coefficient form.
2. E60: Bu + 2–4 far Sidon outliers has front ratio up to 200 and R within +0.026 of Bu.
   - So the escape class contains near-Bu sets (numerically within 0.03 of Bu; R -> ½ PROVED in P37 modulo Bu et al.).
   - The P31 front-loading barrier says nothing about where good sets live. Profile methods are exhausted for Chowla,
     and any proof must handle front-loaded Bu (P16 does, structurally).
3. Strategic consequence.
   - Lower-bound line L1 (SR / arithmetic) remains the only Chowla route.
   - The window/Nikolskii technology is now best exported: it settles the one-sided Littlewood problem and the dense /
     flat-profile cases with general coefficients.
   - Next exports to check:
     (a) Erdélyi's Theorem 1.2-type sparse sums Σ A_j cos(λ_j t) under a flat-profile hypothesis (P31 criterion);
     (b) Littlewood-type polynomials with coefficients in a finite set (e.g. {0, ±1} with density);
     (c) multivariate / Steinhaus-random-phase versions.

## 2026-10-19 (night, cont.) — Frequency-localized P31 and why it is exactly critical (lead; PROVED, elementary)
1. **Localized window inequality (PROVED).** Let K >= 0 be a trigonometric polynomial with K̂(0) = 1 and spectrum Σ_K.
   For x₀ ∈ ℝ put h_{x₀} = [(f + M)·K_w(· − x₀)] ∗ K, which is >= 0 with spectrum ⊂ Σ_K. Let
   ρ(Σ) := sup{‖h‖²/ĥ(0)² : h >= 0, spec h ⊂ Σ}. Averaging over x₀ as in P31 gives
       M²Ψ(0) + ½Σ_{a∈A}Ψ(a) <= ρ(Σ_K)·(M² + ½S_A(w)),   Ψ := K̂² ∗ κ_w²,
   because ĥ(0) = M + g(x₀) as before, and avg_{x₀}‖h‖² = Σ_j|c_j|²Ψ(j) by orthogonality.
   - K = Fejér of degree D gives a P31 "at scale D" whose Nikolskii factor is ρ(D + 1), not ρ(X + w). This is the
     truncation-free localization.
   - It coincides with the low-pass recursion up to lower-order terms.
2. **No-go (exact criticality).** Suppose A is full on K's positive spectrum near 0 (A ⊇ [1, w] and A ⊇ Σ_K ∩ (0, ∞)
   on the support of Ψ). Then:
   - the left side is ≈ W_w‖K‖²/4;
   - the right side is >= ρ(Σ_K)·w/6 ≈ ρ(Σ_K)W_w/4;
   - and ‖K‖² <= ρ(Σ_K), since K is itself a competitor in the sup.
   So the inequality carries NO information for every choice of K:
   - single bands: Fejér attains 2/3, the extremal kernel attains ρ;
   - multi-band Riesz-product kernels: Nikolskii cost (3/2)^m against side-band weight Σ4^{−|S|} = (3/2)^m;
   - any spectrum.
   Physical reason: the low-pass of a locally full set IS a nearly nonnegative kernel (g = (K_D − 1)/2 for A ⊇ [1, D]).
   Low-passing genuinely destroys the information. This explains, in one line:
   - why the dense threshold ρ/2 = 0.4055 cannot be lowered by localization;
   - why the low-pass recursion was "killed by 0.687 vs 2/3";
   - why every window-shape tweak gains only O(θ³).
3. **Consequence for dense sets A ⊂ [1, Cn], C > 2.466.**
   - Window methods prove √n only when the profile is not front-loaded.
   - The front-loaded dense case needs information above every localization scale. Candidates are run/boundary structure
     (Bu et al. Prop. 9.1 gives n^{1/4} for all C) or P32-type spike support.
   - Target T-dense: λ_A >= c(C)√n for all A ⊂ [1, Cn].
     - Remark 9.8(iii) of Bu et al. leaves this open. We have it for C < 2.466 (kernel-checked).
     - Plan: dichotomy. Either the profile is not front-loaded (P31), or the front is dense at all scales and has
       long runs. Then bound run-tops Z-specifically (P27-style: long t = 1 runs in an interval-like front).

## 2026-10-19 (night, cont. 2) — Exact identities for real-square identities (Bu's class); where ½ comes from (lead)
Setting:
- h(x) = Σ_{u∈U} c_u cos(b_u x), real c_u ≠ 0, distinct b_u > 0.
- Suppose the off-diagonal part of h² is exactly f_A: every |b_u − b_{u'}| and every b_u + b_{u'} (u ≠ u') carries total
  coefficient 1 on its frequency, the difference and sum frequencies are disjoint, and both are disjoint from {2b_u}.
1. **Identity (trivial).** f_A(x) = h(x)² − E(x), where E(x) := Σ_u c_u² cos²(b_u x).
   - So M(A) = max_x (E − h²).
   - mean E = mean h² = Σc²/2.
   - M >= max over real zeros z of h of E(z).
2. **Count identity (PROVED, exact).** |A| = (Σc_u²)² − Σc_u⁴.
   Proof: write Q = Σ_{u≠u'} c_u c_{u'}. Then |A_diff| = |A_sum| = Q/2. The weighted additive energy is
   - difference side: (Σc²)² + Q;
   - sum side: 2Q + Σc⁴, since the diagonal sums 2b_u are disjoint from the off-diagonal ones.
   Equating gives Q = (Σc²)² − Σc⁴. Bu: k(k − 1) ✓.
3. **Consequence.** R = max_x(E − h²)/√((Σc²)² − Σc⁴) ≈ max(E − h²)/Σc².
   - Generic zeros of h sit at E ≈ Σc²/2. That is the ½.
   - It is not a multiplicity effect: with uniform multiplicities μ_d (differences) and μ_s (sums), the energy identity
     forces μ_d + 1 = 2μ_s. So equal coefficients force μ = 1. Uniform multiplicity >= 2 is impossible for REAL squares,
     independently of P4's Z-lift obstruction. P8's sub-½ scenario (μ >= 2) is therefore void in this class.
   - Complex squares (differences only) have no such identity: R = 1/√(2μ) with uniform difference multiplicity μ.
     Their obstruction is only Z-specific (unique extreme differences, P4, triangle multiplicity profiles of lifts).
     Note: δ₀ + (μ/K)1_S is p.d. with |S| = K(K − 1)/μ, so Chowla itself forces μ = O(1) for them.
4. **What beating ½ in the real-square class needs.** E(z) <= (1 − γ)Σc²/2 at EVERY zero z of h. In other words, every
   zero of h must be a near-common zero of the terms.
   - Bu's half-integer frequencies b = 3s + ½ = odd·½ make x = π a common zero (E = 0). All other zeros are generic
     (P16: large sieve gives E ≈ Σc²/2 at some zero).
   - Forcing all zeros to be common, h = cos(βy)·P(cos βy) with P > 0, needs Σ_{u} sin((m_u + ½)ψ) >= 0 on (0, π) for a
     Sidon-like set {m_u}. That is a Chowla-type positivity for half-integer sine sums, false generically.
   - Status: the real-square class is pinned at ½ by "generic zeros" (P16 for Bu's family). A general P16 for all
     ±-Sidon frequency sets would need many well-spaced zeros of h. "Few-zero" h is the only loophole, and E63/E52
     give no hint it is realizable.

## 2026-10-19 (night, cont. 3) — One Bu step with D fixed: triangle locking, phase-blind optimum, E64/E65 (lead)
Setting: A = 3D ∪ E with E ∩ 3Z = ∅. Write P(x) = f_D(3x) + Mt and Z(x) = e^{ix}W(3x), where W is a 0/1 Laurent
polynomial: frequency m ↔ e = |3m + 1|. Then f_A >= −Mt ⟺ Z(x) ∈ T(P(x)), the equilateral triangle with inradius P,
circumradius 2P and vertices at 2P·{1, ω, ω²}. λ := |E|/|D|; R(A)² = Mt²/(|D|(1 + λ)).
- (T1) Ceiling. Full vertex locking means f_A + Mt = 3P·χ_Ω with Ω a 3-tile. Parseval then gives exactly
  |E| = 4Mt² + 2|D|, i.e. λ = 2 + 4R(D)².
  - The pinch |E| <= 2|D| + 2Mt is the vertex condition at y = 0, where W(0) = |E| <= 2P(0).
  - Linear tests (∫ f_A K >= −Mt K̂(0) with K >= 0) cannot beat the pinch: any smoothing of the two-point measure at
    2π/3, 4π/3 loses on 3D and E alike.
- (T2) Phase-blind optimum. |Z| <= P everywhere gives |E| <= ‖P‖² = Mt² + |D|/2, i.e. λ <= R(D)² + ½. Equality holds
  iff W = V² with |V|² = P: a BI-FLAT V, with autocorrelation ½ on ±D and autoconvolution 0/1.
  - Iterating phase-blind optimal steps would give R² -> R²/(1.5 + R²) -> 0.
  - Sidon D: V = F/√2 and W = ½F², which is Bu (λ = 1), up to the diagonal junk ½F(2y).
- (T3) Local vs global locking.
  - Stationarity at a vertex touch point (|W| = 2P) needs (arg W)' = −1/3 there. At y = 0 this means the mean
    W-frequency is −1/3: possible for 0/1 W.
  - Globally, the winding of e^{iy/3}W is 2π(1/3 + w), so the phase must cross a sector boundary, where |W| <= P.
    That is only a measure-zero obligation, so there is NO topological obstruction to λ near 2.
  - Exact locking is impossible: zW³ >= 0 would force a symmetric support with 3a + 1 = −(3b + 1).
- (T4) "F²·u" designs are killed. W = ½F²·Σ_{j∈J} z^{m_j}, with disjoint shifted sumsets, gives λ = |J|.
  - |J| >= 3 violates the pinch.
  - |J| = 2 needs phase control of F. That forces S to be symmetric about a centre c, but a symmetric S is not Sidon:
    the sum 2c has multiplicity k/2.
  - Even granting phase control (m = −1 − 6c, drift α = m/6, vertices hit at the lobe centres), the LINEAR phase drift
    violates the triangle. The worst violation is by the factor max_φ 2cos φ·cos(π/3 − φ/3) = 1.1255 at φ ≈ 0.405, and
    the triangle is violated for |φ| < 0.785, with an excess ∝ P.
- (T5) Exact Mt = M(D) forces E = ∅ generically. At the minimisers x* of f_D(3x) we have P = 0, so Z(x*) = 0 and
  (from the double zero of P) W(y*) = W'(y*) = 0. A 0/1 polynomial cannot vanish at an algebraically generic point.
  E64: D = the N24 optimum at Mt = M(D) gives E = ∅, proved optimal by Gurobi.
- (T6) Paired sub-class E = 3M₊ + {1, 2}. Here f_A(x) = f_D(3x) + cos(x/2)R(3x), with R(y) = 2Σ_{m∈M₊} cos((m + ½)y).
  The constraint is −P/cos(y/6) <= R <= P/cos(π/3 − y/6) on [0, 2π]: an asymmetric band, up to 2P at y = 0 and down
  to −2P at y = 2π. This is a 1-D real formulation, kept for later.
- Experiments: E64 (Gurobi exact class optimum, small k and dense D) and E65 (annealing at k = 12–24, Singer)
  measure λ(k) at Bu's M. They discriminate between "λ -> 1: incircle barrier" and "λ > 1: approximate locking".
- (T7) General q (PROVED; elementary). Let A = qD ∪ E with E ∩ qZ = ∅ and λ = |E|/|D|.
  - The q-coset values g_j = f_A(x + 2πj/q) + M >= 0 have DFT (qP, ĝ(1), …).
  - Pinch: λ <= q − 1 + (q − 1)M/|D|.
  - Phase-blind ball: by Cauchy–Schwarz, g >= 0 holds whenever Σ_{r≠0}|ĝ(r)|² <= (qP)²/(q − 1). This gives
    λ <= (1 + 2R(D)²)/(q − 1). For q = 3 that is R² + ½, as in (T2).
  - q = 2: the pinch reads |E| <= |D| + M. So a BINARY step has λ <= 1 + M/|D|, and the "Bu-q2" set
    2D ∪ {2(s + s') + 1 : s < s'} attains λ = 1. Its proof: f_E = ½Re(e^{ix}(F(2x)² − F(4x))), and
    |Re(e^{ix}F²)|/2 <= ½|F|² = P.
  - So q = 2 is pinned at λ = 1 by the pinch. q = 3 is the first modulus with room between phase-blind (λ = 1 at
    R(D)² = ½) and the pinch (λ = 2). Larger q have a smaller phase-blind ball (2/(q − 1)) but more room up to q − 1.
  - Efficiency of a step is log(1 + λ)/log q: Bu has log 2/log 3 = 0.63.
- (T8) Where locking occurs naturally.
  - At x = 0, Z(0) = |E| is real and positive, so it always points at a vertex, with |Z(0)|/P(0) = |E|/(|D| + M).
  - A set equidistributed mod 3 has λ ≈ 2. Its central spike (and the spikes at other rationals) are vertex
    configurations, so the locked excess Λ := ∫(|Z|² − P²)₊ is >= c·n²/X, a constant fraction for dense sets.
  - Bu's sets are 3-ADICALLY BIASED: |A ∩ 3Z| = |A|/2 instead of |A|/3. Their Z sits on the incircle at y = 0 and
    has no locking.
- A 3-adic recursion would follow from a locking bound. If Λ <= η·|D| at every 3-adic level, then
  n <= 1.5|D| + M² + Λ, which gives R(A)² >= R(D)²/(1.5 + η + R(D)²) level by level. With J ≈ log₃ X levels this is
  M >= √n·X^{−c(η)}. That is weak, and Λ is NOT small for dense sets (by T8), which P31 handles anyway. Parked as a
  possible sparse-regime tool.

## 2026-10-19 (night, cont. 4) — Test-set (B-test) form of the dual certificate (lead; reformulation, classical in spirit)
- Setup. For finite B ⊂ Z and a low-pass multiplier 0 <= K̂_H <= 1 with K̂_H(0) = 1, the measure
  ν = |F_B|²(1 − K̂_H) is nonnegative. Testing f_A >= −M against it gives
      M >= (1/(|B| − Σ_m r_B(m)κ_H(m)))·Σ_{a∈A} [(r_B ∗ κ_H)(a) − r_B(a)],
  where r_B(a) = #{b − b' = a} and κ_H is the coefficient sequence of K̂_H.
  So a certificate for M >= c√n is a set B with a FINE-SCALE DEFICIT of A-differences of c√n per element, relative to
  its own smoothed difference profile.
- Special cases:
  - B independent in Cay(Z, ±A) (A-avoiding) gives Hoffman's M >= n·dens(B).
  - B = A gives the localized third moment (fine Schur-triple deficit).
  - B = an interval of length ≈ 0.48n with H killing the main lobe gives the linear bound for A = [1, n], since the
    first sidelobe sits on the minimiser 4.49/n.
- Chowla ⟸ every A admits such a B. The weighted relaxation (Delsarte/theta, arbitrary weights on A) is FALSE in
  general (weighted Fejér sub-intervals; Belov–Konyagin multisets). So any B-construction must use that all weights
  are equal to 1.
- Status: reformulation only. No canonical B(A) is known beyond the three special cases.
- (T9) Central-spike locking for Sidon D (HEURISTIC barrier λ <= 1 + O(σ/k) + o(1), where σ = Mt − k/2 is the slack).
  - The pinch allows W(0) up to 2P(0) ≈ k², while Bu uses k²/2.
  - The central spike is the one region where Z points at a vertex for free (T8). P's spike is ½|F|² ≈
    ½(k/N)²|D_N(y)|² (Singer, N ≈ k²). It is Fejér-shaped and merges with the chi-square bulk (~k/2) at |y| ≈ k^{−3/2}.
  - Extra Δ = W − ½F² must satisfy |Δ| <~ P on that profile AND |Δ| <~ σ near the zeros of F (P ≈ σ there).
    - Interval-like Δ: the Dirichlet tails 1/|y| reach k^{3/2} ≫ P at |y| ≈ k^{−3/2}.
    - Fejér-shaped Δ: the coefficients are ≈ ½·(triangle), so it is not 0/1. Dithering to 0/1 adds noise ≈ k/2 ≫ σ
      near the zeros of F.
    - Δ = ½F̃² for another Sidon set: |Δ| ≈ k/2 at the zeros of F.
    - Δ ∝ F²·z^m: this is T4.
  - So every route to λ > 1 must beat "W vanishes doubly at the zeros of F", and the 0/1 constraint forbids the
    needed smooth spectral shapes.
  - Prediction for E64/E65: λ(k) -> 1 at Mt = M_Bu. The small-k excess comes from σ/k ≈ 0.3.
- (T10) Slack budget for beating ½ in the one-step class (HEURISTIC; quantifies T9).
  - Take Mt = k(½ + ε) and |E| = (1 + f)|D| with |D| ≈ k²/2. Then R(A)² = (½ + ε)²/(1 + f/2), so R(A) < ½ needs
    f > 8ε + 8ε²: the gain must be LINEAR in the slack.
  - Extra elements Δ (m = f·k²/2 terms beyond Bu) must have |Δ| <~ σ ≈ εk at the near-zeros of F in the bulk.
    - A generic (random-like) 0/1 Δ has bulk size ≈ √m = k√(f/2), so f <= 2ε², far short of 8ε.
    - Edge (Dirichlet) tails 1/|y| exceed εk on |y| < 1/(εk), which contains ≈ k/ε near-zeros of F.
    - A structured Δ ∝ F²: this is T4.
  - The central-spike locking seen in E64 at small k is real: P's central spike carries ≈ 1/3 of ∫P² for Singer S
    (k⁴/(6N) with N ≈ k²), so full central locking alone would give λ up to 2. But it is paid for by the transition
    region k^{−3/2} <~ |y| <~ 1/(εk).
  - Prediction: R_opt(k)/R_Bu(k) -> 1 in the one-step class. E64 ratios: 0.80 (k = 6), 0.84 (k = 7), 0.94 (k = 8,
    under-optimised).

## 2026-10-19 (session 3, late) — T-dense agent results verified; the third-moment line and its limits
Verification (lead):
- TD1: re-derived line by line; it is P38.
- TD3: Bernstein/moment certificate reproduced by an independent Fraction script (src/scratch_lm/lead_td3_check.py):
  min coefficients 1/90 and 7/396; E, m1, m2 identical.
- TD4: closed form for W_q equals the direct rational Fourier cube; 0 mismatches (src/scratch_lm/lead_td4_check.py).
Physical-space form (P39). With g_q = 2·1_S − 1_{S+q} − 1_{S−q}:
- V_q = (‖g_q‖² − 4a_q)/16 (corrected; the zero-frequency term g_q(0) = −2a_q is the mean);
- Δ_q = ½·T₃(g_q), the signed Schur-triple count of g_q;
- W_q = (third moment of (1 − cos qx)f).
- LM asks for one q at which the second difference of S is large while its signed Schur count is <= B·‖g‖³.
- 6th differences of the triple count kill quadratic pieces. Intervals and single Bohr sets are fine at
  q ≈ (scale)/4: Δ = 0 to leading order for σ = step/scale <= 1/3.
- For the step function 1_{[−1,1]}, the 6th difference 10p(0) − 15p(σ) + 6p(2σ) − p(3σ) of the triple density is
  NEGATIVE for σ ∈ (1/3, ≈0.77) (−0.047 at σ = ½, −0.075 at 0.6) and positive beyond (3.75·… as σ → ∞).
Obstructions (P39-O):
- (i) Multi-dilate interval unions ∪ p·[1, L_p] kill every multiplier of degree < P/3. This is for general sets of
  density ~1/log n, where M is linear anyway.
- (ii) Unions of J ~ log X/log log X independent Bohr sets kill every single (1 − cos qx) on dense sets. Pure
  excesses are positive and cannot be cancelled; the Pólya envelope is >= 0 for convex decreasing profiles.
- So LM-dense (one q) is very probably false. The family has M >= √n by other means (anti-spikes, or random
  rounding noise).
- Product filters Π_{i<=J}(1 − cos q_i x) kill all components but lose (3/8)^{J/2} in √V, i.e. n^{−O(1/log log n)}.
Spike-truncation (P40, Bhatia–Davis) is the TRUE criterion:
- A counterexample must be spike-dominated for every H.
- Equivalently, 1_A is ℓ²-close to its projection onto a set U of characters of measure <= ε^{3/2}.
- The third moment is only a computable surrogate. It fails exactly when tall positive spikes (structure) coexist
  with a Gaussian-like bulk (rounding noise). Truncation would see the bulk; the third moment sees the spikes.
Failed idea (recorded): physical-space approximate-group argument from f ⊛ f = ½f.
- With φ = f₊ one gets |φ⊛φ − ½φ| <= 2M² + M pointwise (exact).
- But spike heights relevant to a counterexample are only >= √(n/ε) ≪ M² = ε²n once n > ε^{−5}. The constant floor
  swamps the identity, so no "U + U ≈ U" can be extracted at that resolution.
- The identity is equivalent to f̂ ∈ {0, ½} and gives nothing beyond it without positivity at the spike scale.
Hoffman bound (recorded, weak): M(A) >= n·δ*(A)/(1 − δ*(A)), where δ*(A) is the largest upper density of a set with no
difference in A (Hoffman on Følner pieces of Cay(Z, ±A)). For A = [1, n] it gives only M >= 1. Useful only when A
avoids a positive-density "independent" set.
Strategic decision:
- Continue the multiplier line, but with ADAPTIVE multipliers.
  - Each independent structure gets its own factor.
  - The statistic must see the bulk behind tall spikes: e.g. Stieltjes/Hankel conditions with 5–7 moments of the
    filtered T, or truncation-like polynomials.
- Discriminating question for the next agent:
  - (a) Make P39-O(ii) rigorous at a computable size, or refute it.
  - (b) Decide whether 5th/7th-moment Stieltjes certificates recover a constant on Bohr unions.
  - (c) Extend P38 from cumulative to bounded-local-discrepancy rounding (agent line 3).

## 2026-10-19 (late) — P41 (curved cumulative rounding) and what it says about the escape class
- P41 (PROOFS) is the first theorem driven by P40 (spike truncation) rather than by a computable moment.
  - For cumulative rounding, β = s(m−1) − s(m) with s = {σ + Φ} − ½ exactly.
  - Vaaler plus van der Corput make the curved part's transform uniformly O(√(KX)): a BULK of energy
    Σp(1−p) ≍ X that no spike can hide.
  - Front-loading is irrelevant. E66: curved profiles have R ≈ 1.4–3.0 (irrational start density included);
    kinked or oscillating profiles have linear M.
- What escapes P41 inside cumulative rounding: rounding energy on FLAT pieces (Sturmian words of fixed slope α), whose
  energy sits on the spikes 2πkα (height ≈ L/(πk), width 1/L).
- P41+ (CONJECTURED extension, plausible): flat pieces can be EXCLUDED rather than counted against the bulk.
  - Remove W/L-neighbourhoods of the first K spikes of each flat piece: total measure ~ K·W/L.
  - Off-spike, a flat piece is uniformly <= L·log K/W <= √X for W = √X·log K, with L² ~ (log K)²L/W.
  - So any cumulative rounding with an η-fraction of its rounding energy on curved pieces should satisfy
    M >= c(η)√n, whatever its flat pieces are.
  - Gap: the Vaaler truncation on a flat piece needs equidistribution of mα at scale 1/K. α near a rational with
    denominator <= K needs the exact periodic expansion instead. This is Diophantine bookkeeping, not a new idea.
- Remaining cumulative-rounding core: staircase profiles with few steps (all energy flat).
  - The steps give kink sidelobes ~0.22·Δα·m_step (linear M unless compensated; E52), and compensation by later steps
    is hard because wider steps have narrower lobes.
  - With >= √X steps the staircase acts like a chirp (bulk).
  - HEURISTIC: no cumulative rounding beats √n.
- Round-2 agent: TD5 (in progress) disproves LM-dense rigorously by random rounding of a positive Fejér mixture with
  J ≍ log X bumps; M >= √n/128 at x = π.
  - P40 (spike truncation) still gives √n on that family: the noise Z is a bulk off the bumps.
  - So the failure is specific to the third-moment certificate, not to the spike/bulk mechanism.
- Conjecture SB (spike–bulk; implies Chowla by P40): there are K, c > 0 with ∫_{f_A <= K√n} f_A² >= c·n for every A.
  - Intervals satisfy it through their negative sidelobes; Bu/Singer sets through their Exp-distributed bulk.
  - A violator must put almost all of its L² mass on tall positive spikes with no negative sidelobes, i.e.
    1_A ≈ Σ_j w_j(m)e^{−imx_j} with every twisted envelope w_j positive-definite (front-loaded) AND 1_A ∈ {0,1}.
  - The rounding of such a sum must itself be spike-dominated (else bulk), recursively.
  - First derivation to attempt: a two-level version. ρ = front-loaded profile times a q-periodic pattern; show its
    0/1 rounding has either bulk >= cn or a kink sidelobe >= c√n. This generalizes P38 + P41 to arbitrary
    (non-cumulative) roundings of a two-level structure.

## 2026-10-19 (late night) — P41-B, the spike-comb heuristic for SB, and why physical-space SB proofs leak √n
- P41-B (CONJECTURED extension, proof sketch): cumulative rounding of Bohr-modulated profiles p(m) = P(m/X, mα), with
  P smooth on [0,1] × T^d, α Diophantine, and the θ-average P₀ curved (|P₀'| >= c₁ where the energy lives).
  - Φ(m) = Φ₀(m) + ω(m/X, mα) + o(1), with Φ₀'' = P₀'/X and ω the bounded solution of the cohomological equation.
  - e(kΦ) = e(kΦ₀)·Σ_j c_{k,j}(m/X)e(jmα). Van der Corput with partial summation in each term keeps the curved part
    O(√(KX)) uniformly.
  - The profile's Bohr spikes at 2πlα are excluded like flat pieces (P41+).
  - So deterministic cumulative roundings of TD5-type positive-mixture profiles satisfy Chowla.
  - The hard sets are non-cumulative roundings whose errors are themselves structured.
- Why SB resists physical-space proofs (recorded failures):
  - (a) With φ = f1_U (the spike part, ∫φ <= M) and r = f1_{U^c}, the identity f⊛f = ½f gives
    ½∫_U f² = T(φ,φ,φ) + 2T(φ,φ,r) + T(φ,r,r). The error terms are bounded only by ‖φ‖₁·‖φ‖₂‖r‖₂ ~ M·√δ·n, which
    exceeds n by a factor ε√(δn).
  - (b) Dually, φ̂ ≈ ½1_S in ℓ², but the Toeplitz error operator has norm sup|r| ~ K√n. Positive-definiteness of φ̂
    therefore loses exactly the √n we need.
  - (c) P25 localization controls local sums at m-scale H, i.e. x-resolution 1/H ≫ 1/X (the spike width), so it
    cannot see fine spikes.
  - Every route so far loses exactly at the √n scale. The missing ingredient must be exact at that scale (like
    P41's exponential sums for a specific rounding), not a stability or regularity argument.
- Spike-comb heuristic (why SB should hold):
  - A violator has f ≈ −M + Σ_j h·φ((x − x_j)/w) with positive bumps φ, so f̂(k) = hw·φ̂(kw)·Σ_j e^{−ikx_j}.
  - φ >= 0 forces φ̂ to decay (triangle-like). Flat 0/1 coefficients then force |Σ_j e^{−ikx_j}| to GROW toward the
    band edge on S and to vanish on [−1/w, 1/w] \ S: about 4X vanishing conditions with N_s ~ ε²X points.
  - Coset (rational) point sets vanish for free but have flat moduli on their dilate lattices: the wrong shape, giving
    exactly the Dirichlet sidelobes.
  - A quantitative "positive-bump uncertainty principle" along these lines is a candidate missing ingredient.

## 2026-10-19 (late night) — CORRECTION: SB is P30; P40 restates E47's identity
- The spike–bulk conjecture SB (∫_{f <= K√n} f² >= cn) is the session-2 conjecture P30 (spike share above K·M
  bounded by ρ < 1) with the threshold moved from K·M to K√n.
- P40 is the Bhatia–Davis form of the identity share_{>KM} >= 1 − 2(1+K)R² used in E47.
- The twisted-profile, Bessel-budget and "front-full forbids twisted peaks" heuristics in today's entries repeat
  NOTEBOOK items 756–830 (P30 heuristic support; DECISIVE TARGET G3, a coupling inequality without constant loss;
  route R1).
- What is NEW today on this line:
  - P41 (first theorem obtained from the spike/bulk mechanism, via exact exponential sums);
  - E67: the bulk fraction equals the rounding-energy share for curved/random roundings; SB/P30 minimised by
    intervals;
  - E68 (Pareto front).
- Lesson: re-read the NOTEBOOK index before re-deriving a reformulation.

## 2026-10-19 (night) — P47: the high-pass window; escape class = front-loaded LOCAL VARIANCE (lead)
1. P47 (PROOFS) in one line: apply the P31 chain to T = H_h·f_A, with H_h = 1 − K_h/K_h(0) ∈ [0,1].
   - T >= −M, and T's coefficients are the high-pass residual r = 1_A − κ̃_h ∗ 1_A (even extension).
   - So the window inequality reads W(m² + ‖r‖²/2) <= ρ(L+1)(m² + S_w(r)/2), with L = X + h + w.
   - P31 is the IDENTITY-multiplier case (r = 1_A; it is not H_0, which vanishes; agent correction). The
     model/fluctuation split in P47's proof only COMPUTES ‖r‖² and S_w(r):
     for bounded-discrepancy roundings, ‖r‖² = Σp(1 − p) + O(D₀(1 + V) + XD₀/h) by a² = a.
   - Consequence: Chowla holds unless, at EVERY scale h, the local variance of A,
     v_h(j) = (1_A(j) − (κ̃_h ∗ 1_A)(j))², is front-loaded (front mean >= ~2.6 × global mean).
     For h = 0 this is P31's front-loaded density; h = 1 is the q = 1 denominator filter.
2. What the escape class looks like.
   - Front-loaded density AND front-loaded variance means the front has density strictly inside (0,1) (dense fronts have
     no variance), and the tail is sparse with variance <= ~0.385 × the front's.
   - Interval + taper sets (E68 anatomy: [1,52] plus a sidelobe-filling tail) are NOT in the escape class: e = 0 at the
     front. P47 covers their bounded-discrepancy versions.
   - Remaining picture: front F ⊂ [1, θX] with density in (0,1) and a sparse far tail B ⊂ [θX, X].
     - M(F) >= c√|F| by P31 (F is not front-loaded at its own length).
     - The tail must cancel F's dips: f_B >= c√|F| on D_F = {f_F <= −c√|F|}, so |B|/2 = ∫f_B² >= c²|F|·|D_F|
       (normalized measure), i.e. |B| >= 2c²|D_F||F|, up to the M-slack.
     - A sparse tail can therefore only cancel dips confined to small measure (negative spikes of f_F). If f_F is
       Gaussian-like, |D_F| ≍ 1 and the tail is not sparse: contradiction.
   - Discriminating question: can a front with density in (0,1) have its √|F|-dips confined to measure o(1)?
3. Macroscopic picture (P48 + P52). Every set has a macroscopic budget e = p(1 − p). Macroscopic atoms with PD
   continuous profiles can absorb part of it. The residual must be mesoscopic spikes or bulk.
   The open core is unchanged: mesoscopic spikes (√n << height << X), which neither P48 nor any window sees.
4. Round-3 agent results recorded as P48–P51 (TD9–TD14). TD10/P49: fixed fractional flat pieces give LINEAR M.

## 2026-10-19 (night, cont.) — P53 macro-SB, and the descent it suggests (lead)
1. P53 (PROOFS) is the joint, all-atoms form of P48.
   - Put the local pattern density g(t,ω) on [0,1] × K, K = the dual of a countable group of angle sequences. Then the
     reflected g̃ has a nonnegative Fourier transform at EVERY (y,θ) by P48.
   - So g̃ is continuous and PD. A continuous {0,1}-valued function that vanishes for |t| >= 1 is 0.
   - Hence M = o(X) ⇒ the local spectrum is not purely atomic, i.e. ∫∫g(1 − g) > 0.
   - The 0/1 constraint enters exactly once, as "g ∈ {0,1}", i.e. a² = a at the level of local patterns.
2. Checks.
   - TD10/P49 (flat pieces): g jumps at flat/curved junctions, hence linear M.
   - Bohr-window sets {m : {mα} ∈ E(m/X)} and residue-pattern sets: g ∈ {0,1}, hence linear M. Consistent with E52
     (staircases/kinks linear) and E46 (ball-shaped Bohr sets killed).
   - Random sets: g = p(t), so P53 is silent. CORRECTION (round-4 agent): Bu sets have a macroscopic residue atom,
     f_A(2π/3) = n/4 (3-adic structure, T8). Their local pattern on Z_3 is fractional, not 0/1, so P53 is still silent.
3. Why this matters for √n. Every macroscopically structured mechanism is dead. A counterexample needs a positive
   share of its local spectral mass in structure of height o(X).
   - Descent question (D): does the same argument run one level down?
     - At a mesoscopic level the spikes have height H with K√n << H << X. Their "twisted profiles" have amplitude H/X
       → 0, so the 0/1 constraint is invisible at that normalization.
     - The constraint must instead come from Bessel: Σ_atoms|q|² = ∫g² <= ∫g at the finest level (integers), propagated
       up through the scales.
   - Candidate quantitative statement (QD): for every C there are δ, c > 0 such that every A ⊂ [1, Cn] with
     M <= δX carries >= cX of local spectral energy in structure of height <= δX.
     - QD should follow from P53 plus compactness, once a finite-X notion of "energy in atoms of height >= δX" is fixed
       (e.g. the largest local twisted energy captured by <= 1/δ² frequency windows of width K/X).
     - QD is iterable only if the lower level again satisfies a P53-type rigidity. That needs a mesoscopic P48 for the
       coherent part of spikes of height >> √n. This is the precise next lemma.
4. E70 (P47 high-pass family on the zoo): every set has best bound >= 0.106√n. The window family captures 33–52% of M
   on near-optimal sets. Bu/Singer best/√n drifts 0.29 (q=7) to 0.237 (q=31); E70b (q up to 127) is running to see
   whether it levels off.

## 2026-10-19 (night, cont. 2) — Descent analysis: what 0/1 does below macroscopic scale; TL1 (lead)
1. Bohr-window sets are spike-dominated in the POSITIVE-part sense: harmonics k·α have heights X|sin(πkp)|/(πk), and
   the energy at heights <= K√n is only ~K√n/π. They still satisfy SB, because their non-PD profiles create NEGATIVE
   atoms (P53 ⇒ linear M).
   Lesson: below macroscopic scale the 0/1 constraint acts through two channels.
   - (i) PD rigidity: a positive atom needs a PD profile, else it is a negative atom.
   - (ii) Leakage: a 0/1 pattern cannot keep its variance on a "level-1" set of frequencies, so it leaks to
     combinations and harmonics, whose heights decay, eventually into the bulk.
2. TL1 (CONJECTURED; E71 numerics up to S = 3 plus the Gaussian limit): for E ⊂ T^S, the Fourier mass of 1_E on the
   characters e^{±iω_s} is <= (8/π²)|E|(1 − |E|).
   - Proof route at p = ½: W¹ = E[1_E L] <= ½E|L| <= ½c_K‖L‖, with c_K = sup E|L|/‖L‖₂ over cosine sums. This needs
     c_K = 2√2/π (attained at S = 1).
   - General p: sup_L Λ_p(L)²/‖L‖², with Λ_p the top-p superquantile.
   - Use: a 0/1 local pattern relative to S independent spike frequencies keeps <= 81% of its variance on those
     spikes; >= 19% goes to combination frequencies Σk_s x_s or to continuous spectrum.
     - If the spike set is dissociated and the spikes have amplitude δ (height δX), level-2 combinations have
       amplitude ~δ². They reach the bulk once δ² <= K√n/X.
     - So a counterexample's tall-spike set must be approximately additively CLOSED (combinations of spikes are spikes):
       a Bohr/approximate-group structure. Then PD rigidity (P53-type) applies to that structure. This is session 2's
       SR/Sanders line, now with a concrete mechanism.
   - Caveat: TL1 needs the window to equidistribute in T^S, so it serves only for few, tall spikes. Many small spikes
     are "random-like" and need a bulk argument instead (Bu sets live there).
3. Decision: the round-4 agent pursues QD/MP48 (quantitative P53, mesoscopic PD). The lead keeps TL1 + additive
   closure as the structured half of the descent.
- UPDATE (same night): TL1 is PROVED (PROOFS P54) for any set of characters on which a real grading ψ is ≡ 1.
  - Proof: the Steinhaus rotation trick, Re Z = |Z|cos Φ, plus the concave envelope of sin²(πx).
  - Constant 8/π², sharp at p = ½ with one coordinate.
  - Torsion characters are excluded, and must be: a Z_2 dictator has 100% level-1 weight.

## 2026-10-19 (night, cont. 3) — The TL1 dichotomy: a counterexample's spike set must be additively structured (lead)
1. Goal statement (TL1-finite, CONJECTURED; the bridge from P54 to actual sets).
   - Setting: a ∈ {0,1}^Y with mean p; frequencies x_1..x_S; â(x) = (1/Y)Σ_m a_m e^{imx}.
   - Graded D-dissociation at scale Y: every UNBALANCED combination Σ_{i<=j} x_{s_i} − Σ_{i<=k} x_{r_i} with j ≠ k,
     j + k <= D, has ‖·‖ >= 1/(ηY). Every balanced cross term x_s − x_r (s ≠ r) also has ‖·‖ >= 1/(ηY).
   - Claim: Σ_s |â(x_s)|² <= (8/π² + o_{D→∞, η→0}(1))·p(1 − p).
   - Proof route (P54's, made finite):
     - L_m = Re Σ_s c_s e^{imx_s} with c_s = conj(â(x_s)). Then Σ|â(x_s)|² ≈ (1/Y)Σ a_m L_m <= the top-p superquantile
       of L over the window.
     - Balanced separation gives ‖L‖² ≈ ½Σ|c_s|².
     - Unbalanced separation makes the empirical law of Z_m = Σc_s e^{imx_s} rotation-invariant in all moments of
       degree <= D. Moment matching then gives a superquantile within o(1) of the rotation-invariant bound.
2. Consequence (HEURISTIC until TL1-finite is proved). Let Λ be the tall-spike set of a counterexample (heights >= λ,
   P40). Apply TL1 to Λ in windows of length Y.
   - If Λ is D-dissociated, at least 19% of the local variance lies off Λ, i.e. in the bulk. Then SB holds with
     c ≈ 0.19·(rounding energy), contradicting P40.
   - So Λ must carry short unbalanced relations: either
     - (I) torsion: rational spikes 2πr/q with q <= D, i.e. residue-class structure, the SR/pinch route; or
     - (II) additive relations x_s + x_r ≈ x_u, etc.: approximate-group/Bohr structure, the localized-Sanders route.
3. In case (II) with bounded rank r, the local pattern is a 0/1 function on [0,1] × T^r. The P53 limit object then
   keeps it 0/1, so it contradicts M = o(X), whatever the box sizes are.
   - The only escapes are growing rank r_X → ∞, or windows E_X(t) ⊂ T^r with features at scale → 0 (perimeter → ∞).
     Both make the limit non-0/1, and both push variance into fine harmonics of decaying height.
   - So a counterexample must be MULTISCALE Bohr with growing complexity. Each level costs a fixed fraction: TL1 leakage
     19%, PD defect >= t²/4 (agent's quantitative P53).
   - The open question is whether these costs sum to a contradiction before the heights reach √(n/ε). This is the
     precise form of the descent.
4. Next: TL1-finite (a clean, provable lemma), then the case (I)/(II) structure lemmas. Candidate for the round-5 agent.

## 2026-10-19 (night, cont. 4) — Reduction: T-dense ⟸ (A) finite TL1 + (B) the structured case (lead)
Ingredients now available:
- R1 (round-4 agent, Task 2B, PROVED, ineffective): for fixed C, J, K there are η, X0 such that M <= ηX ⇒ the energy
  outside ANY J windows of width K/X is >= X/(48C³).
  - With J = 1 (the central lobe): non-central energy >= X/(48C³) for every A ⊂ [1, Cn] with M <= ηX, X >= X0.
  - Limit form: the P53 defect b >= m³/12, from the pointwise bound g <= 1 − t²/4 (Krein/Gram inequality).
- P40: if M <= ε√n, all but O(√ε)n of the energy is at heights >= λ = √(n/ε).
- P54 (TL1): in the limit object, Σ_{θ∈Λ}|q_θ(t)|² <= (8/π²)p(t)(1 − p(t)) for every graded Λ, for [0,1]-valued g too.
Reduction (HEURISTIC until (A) is proved with explicit errors):
- Suppose M <= ε√n with ε small and X large. Let Λ be the non-central tall-spike frequency set (heights >= λ).
  - By R1 and P40, Λ carries >= X/(48C³) − O(√ε)X of energy.
  - (A) Finite TL1: if Λ's weighted unbalanced relation count U_D is small, Λ carries <= (0.81 + ε_D) of the local
    rounding variance. The rest, >= 0.19·X/(48C³) − errors, is bulk. That contradicts P40 for ε < ε₀(C).
  - (B) Hence U_D(Λ) is large: the tall spikes carry many unbalanced relations. This is torsion (residue
    classes) or additive relations x_s + x_r ≈ x_u (approximate-group/Bohr structure). The structured case must then
    be killed by P53-type rigidity (the defect b >= m³/12, extended to the extracted structure), or by recursion.
- This is the precise form of the missing ingredient. It replaces "SB for arbitrary A" by two separate,
  attackable statements: an analytic inequality (A) and an inverse-theorem step (B).
- Round-5 agent brief (.research/agents/tdense5_brief.md): (A) first, then (B).

## 2026-10-19 (night, cont. 5) — QD-½: the sharp scale-invariant form of SB (lead; CORRECTED same night)
Measure form. For A with |A| = n and μ ∈ (0,1], put E_out(A; μ) = inf_{|U| <= μ} ∫_{U^c} f_A².
Conjecture QD-½: there are c, c' > 0 with M(A) <= c√(n/μ) ⇒ E_out(A; μ) >= c'n, for all A ⊂ [1, Cn] and all μ.
- μ ≍ J/X (J windows of width K/X): this is the round-4 agent's fixed-J theorem (ineffective, J fixed). At J = O(1)
  it is P53.
- μ = 1: E_out = 0, so QD-½ contains Chowla. It is a STRENGTHENING (Chowla with energy localization), not a reduction
  to something weaker.
- Sharpness: Singer/Bu difference sets have M ≍ √n and E_out(1) = 0, i.e. M ≍ √(n/μ) at μ = 1. The exponent ½ is
  optimal, and the extremal family sits exactly on the threshold.
What T-dense actually needs:
- P40 gives U = {f > λ} with |U| <= ε^{3/2} and E_out(A; ε^{3/2}) <= O(√ε)n. So T-dense follows from QD at the single
  scale μ = μ₀ (any fixed small constant) with ANY constant c_{μ₀} >= c₀ > 0: "energy outside some set of measure μ₀
  is < c'n ⇒ M >= c₀√n". This is SB/P30 again.
- In window language: QD at J ≍ μ₀X/K, i.e. J PROPORTIONAL TO X. The agent's fixed-J theorem is far from that.
- CORRECTION: an earlier draft of this entry claimed a window-counting lemma (tall energy lives in <= εX/K windows of
  fixed width K/X). That is unproved. The reproducing-kernel bound gives a far-field term ~X/√K (Dirichlet) or
  ~X/K^{1.5} (de la Vallée-Poussin), which swamps λ ≍ √(n/ε). Use the measure form only.
Meaning.
- The useful content is the interpolation: P53 (μ ~ 1/X, linear M) → QD-½ → Chowla (μ ~ 1). It suggests a
  multiscale induction on μ. A loss of a constant factor per dyadic scale would cost ~ log n, so the losses must be
  summable.
- Routes: (A)+(B) of cont. 4 (TL1 + structure), or a finite, J-uniform version of the Krein/Gram argument.

## 2026-10-19 (night, cont. 6) — Round 4 recorded (P55); HBCG = window QD-½; TL1 answers the agent's obstruction (lead)
- The window-counting step withdrawn in cont. 5 is RESTORED with radius-1/X windows by the agent's separated cover
  J <= 3πXn/H². The window form of QD-½ (= the agent's HBCG) therefore implies T-dense via P40.
- The agent's saturating joint-PD system shows what any descent must use: the binary bound 0 <= g <= 1, not just PD
  plus Bessel. That system has 100% level-1 mass. P54 (TL1) caps level-1 mass at 81% for [0,1] patterns. So the round-5
  task is a finite, J-uniform TL1 inside HBCG:
  - graded-dissociated tall spikes ⇒ >= 19% residual ⇒ HBCG;
  - otherwise unbalanced phase-coherent relations ⇒ structure.
- (cont. 6, E72) RETRACTED same night: the E72 optima shrink max A to <= 2.9n (mostly < 2.466n), so they do not test
  C = 3. Whether the P47 family closes T-dense beyond 2.466 is open; E72c tests box ratios 4, 6, 10. Candidate theorem: "P31 + P47 ⇒ T-dense for C < C₁", with an explicit C₁ > 2.466.
  - Proof sketch needed: if every high-pass window fails, A is front-loaded in density (P31) AND in local variance
    at every scale h.
  - Fronts with density near 1 have no variance. A structured (blocky) tail lowers the tail variance only for h below
    the block length.
  - Case analysis on the tail structure is required. Worth a separate attack: it would be the first extension of the
    kernel-checked dense theorem.
- (cont. 6) Explicit escape set for the whole P31 + P47 window family (HEURISTIC computation, idealized local
  variances).
  - Construction: front F = random half of [1, φX], tail = random of density d_t on [φX, X].
  - With φ = 0.2 and d_t = 0.05 (C ≈ 7), every window fails:
    - θ → 0: P47 needs φ/4 + (1−φ)d_t <= 0.385/4, and 0.09 <= 0.096 holds. P31 needs φ/2 + (1−φ)d_t <= 0.19, and
      0.14 holds.
    - θ = 2φ: (4φ/3)(0.09) = 0.12 <= 0.77(1 + 2φ)(7φ/12)(¼) = 0.157 holds.
  - Yet M >= c√|F|: the front's Gaussian dips have measure ≍ 1, and a sparse tail cannot fill them, since that needs
    |B| >= 2c²|D_F||F|.
  - So the window family cannot prove T-dense beyond C ≈ 4–7. The escape is real but not a small-R mechanism.
  - The "dip filling" argument is exactly an HBCG-type statement (energy not concentrated). This is consistent with
    HBCG being the right target.

## 2026-10-19 (night, cont. 7) — Round-5 interim check: FTL1 correct; CY2 relation branch uninformative; uniform law-level TL1 (lead)
Interim verification of .research/agents/tdense5_report.md (agent still running; final record later):
- FTL1 (finite TL1, error 32R/(πD) + relation term R·U_D) is CORRECT. Lead re-checked every step:
  - hinge coefficients |a_d| <= 4R/(πd²) (TV of the θ-derivative <= 4R);
  - CVaR comparison via the degree-D Chebyshev majorant;
  - centering W = E(aL) − pE L <= Λ_p(L) + pR|Δ_1|.
- CY1 (cyclic padding, Y > 2X, a = 1_{A∪−A}): 2W >= p(1−p) − (4/Y)(HM + 2M²) − T_N. CORRECT. Bhatia–Davis on the grid
  gives even (4/Y)HM.
- SG (stable Gram: h <= 1 − t²/4 + 2δ, b >= m³/12 − 2δm) CORRECT (RKHS triangle inequality + bathtub).
- The interval example (E_out(μ) <= C/μ for A = [1, n]) correctly kills every QD exponent β > 1/2.
Two problems make CY2's "unbalanced relation" alternative uninformative as a structure statement:
- (P1) Profile / central lobe. In the padded model, A ∪ −A sits in [−X, X] ⊂ Z/Y, so b contains the macroscopic
  profile part b_prof ≈ p(|m|/X)·1_{[−X,X]} − p.
  - Its analytic signal sits near −p/2 on >= 3/4 of Z/Y, so it is far from rotation invariant (it is not graded).
  - It carries a fixed fraction (≈ δ) of p(1−p), and its spectrum (the central lobe, |k| <~ K₀Y/X) is an AP full of
    unbalanced relations with all c_k > 0 (no cancellation).
  - Its third moment alone already makes E L³ ≍ δ²p, which is the size the relation branch asks for.
  - So the dichotomy "graded ⇒ 81% ⇒ contradiction, else relations" always lands in "relations" via the profile. It
    says nothing about the ROUNDING spikes. Fix: apply TL1 to the local pattern minus its local mean (block-local, as in
    P53/P54's limit object), never to the globally padded indicator.
- (P2) The central lag. On the grid all c_k > 0, so L = Re Z is positive definite with L(0) = R = Σ_Λ c_k ≈ M (spike
  mass). Hence:
  - (E|Z|^D)^{1/D} >= R·Y^{−1/D};
  - for mesoscopic spikes of height h, R ≈ n/(2h) ≫ √W;
  - so the agent's radial-moment branch ((E|Z|^D)^{1/D} > L0√(DW)) holds AUTOMATICALLY for fixed D >= 3 as X → ∞.
  This is P45's "moments are blind behind spikes" in m-space: the cubic count is ≈ R³/Y (the random baseline from
  m ≈ 0) plus the structured excess. The same R is why FTL1's degree must be D >~ R/p.
New (lead, PROVED): uniform LAW-LEVEL TL1 by radial truncation (no moment or tail hypothesis, no S or R dependence).
- Setting: same as FTL1 (any probability space, 0 <= a <= 1, E a = p, b = a − p, Z complex, L = Re Z, W = E[bL]).
- Write Z = ρe^{iθ}, and let a_d(ρ; λ) be the cosine coefficients in θ of h(ρ, θ) = (ρ cos θ − λ)₊, with
  |a_d| <= 4ρ/(πd²). Then for every T > 0, D >= 1 and |λ| <= T:
      E(L − λ)₊ − E(L* − λ)₊ <= 2E|Z|²/T + 4T/(πD) + Σ_{d<=D} |E[a_d(|Z|;λ) cos(dθ); |Z| <= T]|,
  where L* = Re(e^{iΦ}Z). (On {ρ > T}: |h − θ-average| <= 2ρ; tail beyond D: Σ_{d>D}|a_d| <= 4T/(πD).)
- If T² > E|Z|²/(2 min(p, 1−p)), the CVaR minimiser of L* lies in [−T, T]. Take T² = πD·E|Z|²/2 (needs
  D > 1/(π min(p, 1−p))). With P54:
      W <= k_p √(W + B) + 4√(2(W + B)/(πD)) + A_D + p|E L|,   k_p = √env(p)/π,
  where A_D = sup_{|λ|<=T} Σ_{d<=D}|E[a_d(|Z|;λ) cos(d·arg Z); |Z| <= T]| <= (4/π) Σ_{d<=D} d^{−2}·δ_d, and
  δ_d = sup_{|g|<=1 radial} |E[g(|Z|)|Z| e^{id arg Z}; |Z| <= T]| is the d-th angular harmonic of the law of Z,
  truncated to the disk of radius T ≍ √(DW).
- Effect: the error is 4√(2/(πD)) relative to √W, uniform in the spike count, R and the tails. The central lag (|Z| ≈ R)
  is a probability-1/Y event and drops out.
- Cyclic consequence: the gap √(p(1−p)/2) − k_p >= 0.0705√(p(1−p)). So D ≈ 2100/(p(1−p)) (≈ 1.7·10⁴·C after
  padding) forces A_D >= c·p in any counterexample. This is the uniform D = D(C) the brief asked for, but at the
  level of the LAW of Z (phase coherence), not of polynomial relation counts.
- Caveats.
  - (P1) applies here too: in the padded model the profile alone produces the angular defect, so this must be run
    block-locally with the local mean removed.
  - The missing bridge is "truncated angular defect of the local spike signal ⇒ exploitable structure". Polynomial
    relation counts cannot serve, because of (P2).
Where this leaves the finite TL1 programme (lead assessment):
- Block-local framework. Blocks of length ℓ (1 ≪ ℓ ≪ X). The local spike signal Z_B consists of the spikes merged at
  resolution 1/ℓ; frequencies within 1/ℓ of 0 are profile.
  - P40 transfers to the blocks: Σ_B ℓ·W_B ≈ global spike energy, because P_U b is locally Σ_s w_s(t_B)e^{−imx_s}.
  - FTL1-rad then gives a uniform local angular defect on a positive proportion of blocks.
- Remaining exact gap (one statement): a local [0,1] pattern whose spike signal has a truncated angular defect >= c
  must carry structure that P53/SG can use with negative-mass bounds independent of the number of spikes (HBSC-type).
  - Rotation invariance of the law ⟸ approximate alignment shifts (τ with τ x_s ≈ φ for most spike weight;
    bounded rank) or Gaussianity (GTL1; high rank, small energies).
  - The mixed, mesoscopic, growing-complexity regime is exactly where no regularity lemma reaches.

## 2026-10-19 (night, cont. 8) — Strategic review after round 5; dimension barrier; HBSC accounting (lead)
1. PD ⇒ Wiener budget (limit object, PROVED there; P53's mechanism made quantitative).
   - If every character profile ĥ_χ(t) of the local pattern is PD in t, then ĥ_χ(0) >= 0, and Fejér positivity at
     θ = 0 gives Σ_χ ĥ_χ(0) <= h(0, 0) <= 1.
   - PD also gives ĥ_χ(0) >= |ĥ_χ(t)| >= (average amplitude) ≈ h_χ/X. Energy gives S·h²/X ≈ n/2, so
     Σ_χ ĥ_χ(0) >~ n/(2h).
   - So PD at ALL levels forces h >~ n/2: every spike is macroscopic. Mesoscopic spikes cannot all be PD-profiled.
2. Finite version ("front Riesz test", PROVED identity). For ψ(m) = Π_{s<=S}(1 + λcos(m x_s)) and Fejér weights
   κ_w:
       Σ_{ε∈{−1,0,1}^S} (λ/2)^{|ε|} (f ∗ K_w)(ε·x) = Σ_m a_m κ_w(m) ψ(m) ∈ [0, Σ_m κ_w(m)ψ(m)].
   - With (g ∗ K_w)(y) >= 0, where g = f + M, this gives
         λ Σ_s (g ∗ K_w)(x_s) <= (w/2)(1 − p_front) + M[(1 + λ)^S − 1] + (non-dissociation error).
   - The M(1 + λ)^S term is the price of combinations where g ≈ 0. It is a real loss, not slack: in a counterexample
     g ≈ 0 on most of the circle.
   - So the finite Wiener budget only controls O(log(w/M)) dissociated spikes. The quadratic test |u_0 + Σu_s e^{imx_s}|²
     reproduces only Bessel.
   - DIMENSION BARRIER: ℓ¹ (Wiener) budgets need positivity at all combination levels, with cost exponential in the
     number of characters. The dimension-free tools (TL1 rotation, SG Krein/Gram, P40) are ℓ²/law-level and do not
     combine to give it.
3. HBSC accounting (lead, HEURISTIC-rigorous).
   - Near each spike χ, f ≥ −M gives ν_χ(y) >= −M/X only on its dominated region |y| <= Y_χ, where
     Σ_χ Y_χ <= πX (disjoint windows).
   - Hence the natural bound on the lift's negative mass is δ <= M (in units where h ∈ [0,1]). The radius-1/X windows
     of HBCG give δ <~ 3εM.
   - HBSC demands δ <= B·M/H = Bε^{3/2}, which is smaller by a factor ≍ √n·√ε. That is massive cancellation that no
     known constraint supplies.
   - HBSC may be false as stated, or as hard as T-dense. Round 6 tests this adversarially.
4. Global reflection (skill §3).
   - Distance. The lower-bound track is reduced to one mesoscopic statement (HBCG/HBSC). Rounds 3–5 produced correct
     tools (P47, P53, SG, TL1, FTL1, FTL1-rad, CY1), and each sharpened the same gap without closing it.
   - Theory of success. Needed: a dimension-free mechanism converting collective PD-ness of many mesoscopic spikes into
     a binary contradiction. None of the known mechanisms is dimension-free at the ℓ¹ level.
   - Construction line. E73 kills the simplest growing-rank Bohr class. E72c shows escaping the window family is cheap
     (C ≈ 5) but small R is not (R ≈ 1).
   - Decision.
     - (i) Round 6 is ADVERSARIAL: build a "formal escape", i.e. an object satisfying every proved constraint (binary
       local patterns, P40 spike domination, local PD to depth −M/X on dominated regions, TL1, SG, Bessel) with
       mesoscopic spikes and M ≪ √n. If one exists, the missing constraint is identified and it becomes a
       construction lead. If the constraints are inconsistent, that is a proof.
     - (ii) The lead looks at alternative mechanisms: averaged run-tops in Z (Bu et al. Prop. 9.7: λ³‖f‖₁ ≳ n/C; any
       K^{3−δ}μ on AVERAGE over t gives a dense exponent > 1/4), and Cayley translation rigidity (cliques through 0
       come in |B| translates). JMTZ cap at 1/6 for general graphs; Paley in Z_q shows graph theory alone cannot
       separate Z.
     - (iii) Keep the construction line alive through (i).

## 2026-10-19 (night, cont. 9) — Run-tops closed as a T-dense route; the zero-set strengthening is false; round 7 = C₁ programme (lead)
1. E76 verdict (Bu et al. §9 split, averaged).
   - On Bu/Singer sets ‖1̂_{B_t}‖₁ ≈ 0.24K ≈ 0.7√|B_t|: no Fourier concentration of the run-top sets.
   - So for the clipping split, Σ_t Kμ‖Q1_t‖₁² ≈ 0.45·nK³μ with no decay in K. Round 6's averaged sufficient inequality
     (a power saving K^{3−η}) is FALSE for that split on the sets nearest the conjectured extremum.
   - The actual |B_t| ≈ 0.13K² uses only 0.2%–8% of the per-t budget. The loss is the factor Kμ inside the per-t
     inequality, not a missing average.
2. The averaged run-top statement is T-dense itself (PROVED, one line). |B_t| = r(t) − T₃(t), where r(t) = #{a ∈ A' :
   a − t ∈ A'} and T₃(t) = #{a : a − t, a, a + t ∈ A'}. Hence Σ_{t>0}|B_t| = N(N−1)/2 − T₃ ∈ [n², N²/2].
   - "mean_{t<=2X}|B_t| <= cK²" is equivalent to K² >~ n/C up to the T₃ slack, i.e. to T-dense.
   - E74's mean|B_t|/K² <= 0.32 is the statement R >~ 1/√(8C·0.32) in disguise.
   - Only PER-t bounds carry content. Per-t RT2 contains OR(2)-weak (NOTEBOOK 2026-10-18: A = S ∪ (S + t) has
     |B_t| = 2|S|), so it is Chowla-hard on that class. Bedert's per-t K⁴ gives M >~ (#maximal t-runs of length >= 2
     in A)^{1/4} for every t. That corollary is old (OR(2) analysis), not new.
   - Decision: run-tops are CLOSED as a T-dense route. They remain the literature's mechanism for sparse exponents
     (1/5); any Z-specific per-t gain must prove OR(2)-weak first.
3. Zero-set reformulation (lead; REFUTED as a strengthening, E77).
   - G(z) = Σ_{a∈A} z^a maps the disk into {Re w > −M} (minimum principle). So μ + G is zero-free in |z| < 1 for
     μ >= M. Put S(A) := sup{μ : −μ ∈ G(D)} = sup{μ : μ + G has a zero in D} <= M(A).
   - By the argument principle, #zeros = winding of G(e^{ix}) around −μ. "Chowla-S" (S >= c√n) would imply Chowla.
   - FALSE. For A = [1, n], Im G = sin((n+1)x/2) sin(nx/2)/sin(x/2). At its nontrivial zeros x = 2πj/(n+1),
     Re G = −1 EXACTLY. So the curve meets the negative axis only at −1 (and at 0), and S([1, n]) = 1 while
     M ≈ 0.217n. E77 confirms S = 1.000 (n = 64, 256; numpy.roots: 64 zeros inside at 0.98S, 0 at 1.02S).
   - Also small: evens ∪ {1} gives S ≈ 2.6; random C = 1.5 gives S/M = 0.22.
   - Observation (NUMERICAL): on every near-extremal set (small-N optima, Bu, Singer, E68, E72c), S/M = 0.95–1.00.
     The extremal minimum is attained where G(e^{ix}) crosses the negative real axis (Im G = 0 at the minimiser).
     That is a shift-stationarity property: A → A + s multiplies G by e^{isx}.
   - Classical by-products, recorded only for completeness:
     - Littlewood subordination G ≺ 2Mz/(1 − z) gives M >= Mahler(G)/2 and M >= ‖G‖_p/(2c_p^{1/p}) for p < 1.
     - Similarly S >= Mahler(G)/4 (subordination to the Koebe slit map).
     - Szegő's sum rule for the measure (1 + f/M)dx/2π (moments 1_A(k)/(2M)): −∫log(1 + f/M) = Σ −log(1 − |α_k|²).
       This needs control of ∫log(f + M), which spiky counterexamples need not have.
4. Strategic decision (skill §3).
   - Closed this night: run-top averaging (circular in the dense regime), the zero-set strengthening (false), and
     natural/binary-faithful HBSC lifts (round 6).
   - Open sufficient lemmas: HBSC (existential), WGC, OBSF. These are the deep, multiscale form of the gap.
   - Round 7 takes the CONCRETE milestone first: extend the kernel-checked dense theorem (P31, C <= 2.44) to C <= 3,
     the "C₁ programme" proposed in cont. 6.
     - θ → 0 computation (lead): at C = 3, escaping P31 forces p(0) >= 0.866. Then e(0) <= 0.116, and escaping P47
       forces ē <= 0.0447. A front + tail escape needs φ >= 0.369 and a tail of <= ~0.002X elements, i.e. a
       near-interval front, where linear sidelobes should win.
     - At C ≈ 4–7 the window family genuinely fails (cont. 6). So the reach C₁ of "windows + near-0/1 lemma" is
       plausibly between 3 and 4.8.
   - The round also computes the reach C₁* and its extremal profile with Gurobi. The escaping sets at C₁* are the
     next test objects for both tracks.
   - Brief: .research/agents/tdense7_brief.md.

## 2026-10-19 (night, cont. 10) — Round 7 verified: T-dense(4.4393). The macroscopic method's reach is ≈ 6.05 (lead)
1. Verification (PROOFS P58).
   - Every step of the compactness proof re-checked by hand: PD limit profile, exact high-pass diagonal, windows on
     f and on H_h f, P17(a), the optimisation over a.
   - Exact certificates re-run on the VM (algebra.py; witness.py certify 48).
   - The one genuinely new idea is the EXACT HIGH-PASS DIAGONAL. Multiplying f by H_h = 1 − K_h/(h+1) ∈ [0,1] keeps
     f >= −M. Its coefficients a − k_h∗a carry energy profile p(1 − p) exactly in the limit, because a² = a. This
     gives P47's rounding-energy window for ARBITRARY sets, with no model, discrepancy or block hypothesis.
   - The PD L²/L¹ gap is our own P17(a) (session 2), which was "recorded so the constant is not re-derived" and is now
     load-bearing.
2. Structure of the result. T-dense(C) holds whenever C < (2/r)(1 + √(1 − ρ*))², with r the asymptotic Nikolskii
   constant and ρ* = sup ∫w²/(w(0)∫w) over doubly-positive w.
   - Proved: r = 4/(3√3), ρ* <= 0.90565, so C < 4.4393.
   - Numerical: ρ* ≈ 0.7239 (E78: 29 random/structured starts in the autocorrelation class all converge to 0.72387,
     slightly above the half-sine autocorrelation's π²/24 + 5/16 = 0.72373; the general PWL Gurobi class gives
     0.7230–0.7232 at B = 24/40). So the sharp ρ* gives C ≈ 6.046.
   - The exact PD/all-window witness (1/d = 6.0539) shows the macroscopic method cannot pass ≈ 6.05.
3. Why ≈ 6.05 is a genuine barrier for MACROSCOPIC arguments (lead analysis; HEURISTIC but sharp).
   - The witness's realisations are killed by other proved results: random rounding by P40 (its residual, 52.5% of
     the energy, is bulk) and cumulative rounding by the P41/P49 regime (Sturmian atoms).
   - In the macroscopic limit both look identical to a counterexample. The limit only sees p, the twisted atoms and
     the residual's total local energy.
   - A counterexample at C >= 6.05 must put essentially ALL of the residual energy (b ≈ 0.525d, about half of the total)
     into spikes of height >= √(n/ε). This is P40 applied to the high-passed T itself: T >= −M, so T's bulk energy is
     <= √(n/ε)·M = √ε·n. Whatever is not carried by macroscopic twisted atoms must therefore be MESOSCOPIC spikes
     (heights in [√(n/ε), o(X)]).
   - Mesoscopic spikes are invisible in the macroscopic limit. So T-dense beyond ≈ 6.05 is EXACTLY the mesoscopic
     problem (HBSC/OBSF) and cannot be avoided.
   - Band-pass generalisation (lead, PROVED in outline): for every mesoscopic filter H ∈ [0,1] (degree o(X)), H·f >= −M.
     So the windows apply to every spectral portion. In the limit, the local spectral measures σ_t of the pattern obey
     σ_{0+} >= (2/r)∫_0^1 σ_t dt as measures.
     - This collapses to the scalar window when σ_t = e(t)ν with a t-independent shape ν, which is exactly the witness
       family. So it adds nothing against the witness.
     - |mean(H f)| <= 2M, so the window error stays O(M²).
4. Where the programme stands.
   - Dense range proved (paper, ineffective): C < 4.4393. Kernel-checked effective range: C <= 2.44 (P31).
   - Next: (i) sharpen ρ* toward 0.724, which reaches C ≈ 6.04, the full macroscopic reach; (ii) an effective
     finite-scale version, i.e. explicit c(C) and Lean-formalisable; (iii) the mesoscopic theory beyond 6.05, now with a
     concrete adversary (the witness profile) and the new band-pass/high-pass window tool.
   - Also check whether other √n-scale inequalities survive in the macroscopic limit and could kill the witness:
     P32 local windows on f and on filtered T; L⁶ Nikolskii (third-moment) windows; product windows on
     (f + M)(f(· + θ) + M) >= 0. If one does, the macroscopic reach exceeds 6.05.

## 2026-10-19 (night, cont. 11) — Round 8 verified: energy-PD lifts the "barrier"; T-dense(6.156); explicit c(3) (lead)
1. Correction of cont. 10. I called ≈ 6.05 "a genuine barrier for MACROSCOPIC arguments" because the limit "only sees
   p, atoms and total residual energy". That was wrong.
   - The limit sees the residual energy PROFILE e(t). The trivial product window (autocorrelation of g + m >= 0) makes
     e PD. That kills the round-7 witness: its a = 0.656 > ½ is impossible.
   - Lesson: before declaring a limit-object barrier, list ALL positivity statements that survive the limit, not just
     the windows already in use. Every filtered function H f (0 <= H <= 1) gives two: its P31 window, and its
     autocorrelation positivity.
2. What the macroscopic limit sees now (lead synthesis).
   - Objects: p (PD); the local spectral measures σ_t of the residual (σ_t(T) = e(t) = p − p²); macroscopic atoms.
   - For every continuous 0 <= H <= 1 on T: t ↦ H(0)²p(t)² + ∫H²dσ_t is PD (product window) and front-loaded
     (P31 window).
   - Taking H with H(0) = 0: σ is PD as a measure-valued function (every σ_t(U) is PD in t) and front-loaded.
   - For the shape-independent family σ_t = e(t)ν, everything reduces to: p PD, e PD, and windows on p and e.
   - E80 estimates that class's reach. The ρ*-extremal shape already fails energy-PD (E79), so the reach is above 6.63.
3. Simple consequences worth keeping.
   - a = p(0) <= ½ ALWAYS (any dense counterexample sequence).
   - Density window plus a <= ½ gives T-dense(C) for C < 4/r = 5.196 with no doubly-positive input. This is the
     mechanism of the explicit c(3) proof.
   - With ρ*: C < 4(2 − ρ)/r. That is 6.156 with the certified ρ = 0.8153, and ≈ 6.63 with the numerical ρ* = 0.7239.
4. Effective proof (P59.6). The compactness diagonal is replaced by a pigeonhole over geometric Gaussian scales, and
   the limit e-PD by a finite (EM) inequality. Its constant 10^{−6000005} is absurd, but it is explicit, finite and
   formalisable, with only P31-E (kernel-checked) as a non-elementary input.
5. Distance and direction.
   - The dense range went 2.44 (effective, kernel-checked) → 4.44 (round 7) → 6.156 (round 8), with an explicit
     constant at C = 3.
   - A macroscopic counterexample must have a <= ½, both p and p(1 − p) PD, and front-loaded p and e. Beyond the
     enlarged reach, the residual's mesoscopic spike structure is the only remaining freedom.
   - Next:
     - (i) the exact reach of the enlarged class, with certificates (E80 → T-dense(C₈) with C₈ maybe ≈ 7);
     - (ii) effective constants on the whole proved range, plus a Lean round for the effective theorem (c(3), then
       c(5.19));
     - (iii) mesoscopic: aggregated PD of every filtered marginal plus P40 spike domination, against the new extremal
       profile.

## 2026-10-19 (night, cont. 12) — Round 9 verified; complete positivity made exact: the second-order reach is 1/D ≈ 8.571 (lead)
1. Round 9 verified (PROOFS P60; E81 re-checks every certificate by exact-rational Taylor models, a method different
   from the agent's).
   - T-dense(C) for C < 6.9366, from the Catalan parametrisation, the scalar reduction d <= rκ/4, and κ <= 0.749089.
   - The density windows are redundant.
   - The two-profile class has a witness at 1/d = 7.26740.
   - The agent found that the residual covariance kernels must be COMPLETELY POSITIVE (CP), and that CP is strictly
     stronger than doubly nonnegative (Horn witness).
2. Missing ingredient identified and derived: the exact form of complete positivity (PROOFS P61).
   - The Gabor/STFT identity  avg_u |(h·ψ(· − u))^|² = |ĥ|² ⋆ |ψ̂|²  holds for h = g + m >= 0 and any band-limited
     window ψ >= 0.
   - So the smoothed residual energy profile is EXACTLY an average of |ŝ_u|². Each ŝ_u is a Hermitian PD function
     supported in [−1 − ε, 1 + ε] (the transform of a nonnegative function).
   - Since φ(x) = (1 − √(1 − x))/2 is convex, Jensen reduces the extremal problem to ONE generator.
   - Hence: in every dense counterexample limit, d <= D := sup_{w PD, supp [−1,1], w(0)=1} ∫_0^1 φ(|w|²).
   - T-dense(C) holds for C < 1/D. Windows, Beckner, ρ* and κ are not needed. They are consequences, used only to
     bound D rigorously.
3. Sharpness. For every such w, the round-9 weighted Fejér-packet escape (packet shape with transform w) is a genuine
   positive polynomial with min >= −o(√X) and binary first and second moment profiles (p = φ(w²), e = w²/4).
   - So 1/D is the EXACT reach of every "positivity + two moments" argument.
   - The rounds 7–9 classes were relaxations, missing CP: 6.05 (windows only), ≈ 7.21–7.27 (two-profile).
4. Numbers (E82). D ≈ 0.1166747, so 1/D ≈ 8.5708.
   - The optimiser is a symmetric bump keeping 38% of its height at the ends. Every start converges to it at every
     resolution.
   - The triangle gives 9.3196.
   - Companion constants: sharp L⁴ constant N₂ = sup ∫_0^1 w² ≈ 0.34349 (Beckner: 0.3849); κ_w ≈ 0.3557.
   - Split certificates (κ_w × N₂) can reach at most ≈ 8.2 even with sharp N₂, and ≈ 7.3 with Beckner. To get near
     8.57 rigorously we need a certificate that couples the support with the convexity.
5. Strategic review (skill §3).
   - Distance:
     - rigorous T-dense: 6.9366 (ineffective);
     - truth of second order: 8.571;
     - T-dense for ALL C needs THIRD-or-higher binary information, provably (the escapes satisfy every positivity
       statement).
   - Theory of success beyond 8.571: binary versus positive spectral structure. Facts:
     - (i) A {0,1}-valued PD function on a group is the indicator of a SUBGROUP (3×3 Gram: b_k = b_l = 1 ⇒ b_{k+l} = 1).
     - (ii) Bohr / cut-and-project binarisations of packets need PD window indicators, hence subgroups. Macroscopic
       twisted atoms (P48/P53) need W_θ(0) >= |W_θ(t)| real, which is impossible for 1_W with 0 < |W| < 1.
     - (iii) Random rounding of an escape adds Θ(X) bulk error energy, so M ~ √(X log X) (P40).
     - (iv) Coefficient skew Σr_k³ ≈ X∫p(1 − p)(1 − 2p) needs ~J^{3/2} near-resonant centre triples θ_a ± θ_b ± θ_c ≈ 0.
       An AP of centres gives ~J², too many. The needed skew profile e(1 − 2p) = (w²/4)√(1 − w²) vanishes as w → 1,
       whereas one packet family's skew scales like w³. So several families, with tuned cross-resonances, are needed.
   - Kill / pivot / continue:
     - The macroscopic second-order line is DONE as a theory. What remains there is certificate work: a rigorous
       D₁ → 1/D₁ toward 8.57.
     - PIVOT the main research effort to the BINARISATION question. Either (Track C, dense) build binary sequences
       whose residual is a sum of positive packets, or (Track L) prove that binary + positive packets forces a
       contradiction beyond 1/D. These are the same question.
   - Bias check: T-dense is only the dense regime. Bu-type extremisers are sparse (X ~ n²). The sparse regime stays
     open in the record, and a full Chowla proof needs it too.
6. Next.
   - Round 10 (one codex agent):
     - (T1) adversarial check of P61;
     - (T2) rigorous D₁: target C >= 7.5, ideally 8;
     - (T3) the third-order / binarisation problem: moment hierarchy of positive-packet escapes, the subgroup
       lemma, and the reach of "positivity + 3 moments". Construct, or prove an obstruction.
   - Lean later: P61(a) needs Bochner/Gabor on R; P59.6 / P60.7 for the effective range.

## 2026-10-19 (night, cont. 13) — Binarisation beyond 1/D: four heuristics tested, what survives (lead)
While round 10 runs. Setting: dense counterexample limit, residual r_k = a_k − q_k, h = g + m >= 0 with ĥ(k) = r_k/2.
1. SUBGROUP heuristic — FAILED for mesoscopic structure (kept as a precise boundary).
   - Each tall spike has a PD twisted profile W_θ, real and positive at t = 0. So near k ≈ 0 the residual is
     r_k ≈ Σ_θ 2W_θ(0)cos kθ with nonnegative amplitudes, i.e. b − a + Q(0)δ_0 is PD on Z, with Q(0) = Σ 2W_θ(0).
   - If Q(0) < √2 − 1, then {0,1}-valued PD forces a subgroup (3×3 Gram) and the recursion A ∩ qZ gives a′ = 1 > ½,
     a contradiction. So purely MACROSCOPIC atoms near t = 0 are impossible.
   - But Q(0) = 2M + O(1): "b − a + Q(0)δ_0 PD" is literally f_A >= −M again. Mesoscopic spikes (Q(0) → ∞) evade it.
     Circular for the real problem.
2. COEFFICIENT-SQUARE HIERARCHY — LIMITED.
   - A = h ⋆ h̃ >= 0 has coefficients |ĥ(k)|² = r_k²/4. For binary a, its high-pass residual is ≈ r_k(1 − 2q_k)/4, with
     energy profile e(1 − 4e)/16.
   - Energy-PD for A needs (mean of A)²/X = m⁴/X → 0, i.e. M = o(n^{1/4}). Then e(1 − 4e) is PD, so e(0) <= ⅛,
     a <= (1 − 1/√2)/2 = 0.146 and C >= 17.7.
   - This is only an n^{1/4}-type statement, dominated by Bu et al. Prop. 9.7 (M >> n^{1/4} for EVERY C). The next level
     needs M = o(n^{1/8}). Useless for √n: each coefficient-wise power squares the mean.
3. ANCHORED versus TRANSLATION-INVARIANT information (structural).
   - Binary identities beyond second order (a^j = a) enter only single-index ("anchored") sums Σ_k r_k^j ψ(k/X).
   - Gabor/translation-invariant statistics of order >= 3 see them only in lower-order diagonal terms (X versus X³
     quadruples).
   - Positivity bounds anchored cubic sums only from BELOW: (h ⋆ h ⋆ h)(0) >= 0 gives Σ_{k≠0}ĥ(k)³ >= −m³. Binary needs
     POSITIVE skew, so no contradiction.
   - Positive packets centred on an AP produce skew Σr³ ≈ 0.09√J·X (Dirichlet-type resonances a + b = c). So the
     round-9 cubic target "Σr³ <= B·M² + o(X)" is FALSE as a positivity-only inequality. Any proof of it must use
     |r_k| <= 1 or binarity itself.
4. SPIKINESS ⇔ ADDITIVE ENERGY (survives; a construction target).
   - P40 (all residual energy in spikes of height >= √(n/ε)) gives ∫g⁴ >= (n/ε)∫g², so the residual's additive
     energy satisfies E(r) := Σ_{k1+k2=k3+k4} r r r r >~ X²/(Cε). Gaussian / random-sign residuals have ≈ 3e²X².
   - So a dense counterexample needs about J ~ M² large Fourier coefficients of A, each of size ~X/√J, every one with
     REAL POSITIVE anchored phase, carrying ALL the residual energy.
   - Square / difference-set constructions are the opposite: Sidon forces minimal additive energy (flat |F_B|²), so
     their residual is bulk with m ~ √n. That is the P8/P11/P16 multiplicity obstruction seen from this side.
   - Chang's lemma gives no constraint at this scale (J large coefficients versus dimension bound ~J log(1/d)).
Precise open question (for both tracks): is there A ⊂ [1, Cn], C > 1/D, whose large spectrum carries ALL of
‖1_A − q‖² with real-positive anchored phases? A construction disproves Chowla. An obstruction needs a binary-specific
inequality about the PHASES of large Fourier coefficients of 0/1 sequences, which positivity alone cannot see.
E83 (VM, running) probes it numerically: binary sets seeded from the D-extremal escape versus random seeds.
5. (cont. 13, added) The IDEMPOTENT view of binarity, and rigidity attempts.
   - For locally constant density p, b² = b is equivalent, in x-space, to h ⋆ h = c₁ + c₂h away from x = 0, with
     c₂ ∝ (1 − 2p) (the Fourier dual of r² = (1 − 2p)r + p(1 − p)).
   - With h = spikes on Θ plus a small background, the J² pair sums θ_a + θ_b must land in Θ (weight ∝ c₂W_θ), or else
     spread EXACTLY uniformly (the constant c₁). So the weighted spike measure must be a WEIGHTED PARTIAL DIFFERENCE
     SET: σ ⋆ σ = c₂σ + c₁·Haar + c₀δ_0.
   - Random spike positions are not enough: background fluctuations give Σ(b_k² − b_k)² = Θ(K), i.e. O(1)
     non-binarity per coefficient, for every J (computed: fluctuation √(J²/K)·K²/J = K^{3/2} per frequency). So random
     packets can never be rounded cheaply. This is the precise reason the E83-type seeds fail.
   - Exact subgroup case (c₁ = 0): σ is Haar on a finite subgroup, every spike's profile is ∝ (1 − 2p(t)), which
     INCREASES in t, so it is not PD. Contradiction (clean, but exact case only).
   - Cyclic sparse PDS (J = o(K), eigenvalues ≈ ±√J): binary b on Z_K with M ≈ √J/4 = o(√K). Easy on Z_K, where
     Z_K \ {0} already works. The interval forces PD profiles W_θ(t).
   - Slick rigidity attempt FAILED. "F(t, k) := p(t) + Σ_θ 2Re W_θ(t)e^{ikθ} continuous in t and binary ⇒ constant" is
     false, because binarity is needed only on the diagonal t = k/X. Freezing the amplitudes stays accurate only over
     k-windows of length ~X/M, since Σ_θ|W_θ| ≈ 2M. So the spike configuration may reorganise on the scale X/M.
   - Finitely many macroscopic atoms ⇒ locally a Bohr set ⇒ atoms at all ℓ·θ with non-summable amplitudes.
     Self-destructs, so binary residuals are necessarily of mesoscopic type, consistent with Q(0) = 2M.
   - Construction target: a family of weighted PDS spike measures σ_t, constant on k-windows of length << X/M, with
     PD envelopes in t and the D-profile. Obstruction target: show that weighted-PDS rigidity forbids PD envelopes.

## 2026-10-19 (night, cont. 14) — Round 10 verified: T-dense(7.5); three moments are free; the DC barrier for higher-order positivity (lead)
1. Verified (PROOFS P62; E84 is an independent Arb re-check).
   - D <= 1333/10000, so T-dense(C) holds for every C < 7.5019. Rigorous now 7.50; numerical second-order truth 8.571.
   - P61 audited, with (b) repaired for complex w.
   - Third-order sharpness: sparse gadgets z_k = L^{1/3}s^{1/3} on LZ (L = X^{4/5}) add any cubic profile at ℓ¹ cost
     X^{7/15}. So positivity + three moment profiles still stops at 1/D. The fourth moment is where things break.
2. NEW lead observation — the DC BARRIER (why every higher-order positivity argument stalls at n^{1/j}).
   - Binarity beyond second order lives in ANCHORED single-index statistics Σ_k τ(k)ĥ(k)^j (cont. 13.3). To have
     a positive integrand in x-space (h^{*j} >= 0 tested against τ̌), τ must be doubly positive, so τ(0) >= max τ >= 1/ℓ.
   - The k = 0 term τ(0)m^j >= m^j/ℓ then swamps the O(1) signal from k ≠ 0, unless m^j << ℓ <= X, i.e.
     M << n^{1/j}.
     - j = 2: M << √n, which is exactly our regime. This is why P61 works.
     - j = 3: n^{1/3}. j = 4: n^{1/4}, which is the Bu et al. Prop. 9.7 exponent (and our cont. 13.2 hierarchy).
   - Translation-invariant higher-order forms (Gabor polyspectra) avoid the DC term but do not see binarity.
   - Consequence (heuristic meta-statement, to be tested in round 10's successor): in the √n regime, positivity is
     effective only at second order. Any proof of T-dense beyond 1/D must apply second-order positivity to
     BINARY-DERIVED auxiliary objects, or use non-positivity (arithmetic) structure.
3. Binary-derived positive objects available.
   - (i) SUBGROUP RESTRICTIONS: f_{A∩qZ} = q⁻¹Σ_j f_A(x + 2πj/q) >= −M, so A_q = (A ∩ qZ)/q is again a dense
     counterexample (when |A ∩ qZ| >= cn).
   - In the limit, its profile is p_q = p + Σ_{j≠0}W_{2πj/q} (rational macroscopic atoms). Applying P59 and P61 to A_q:
     a + Σ_{j≠0}W_{2πj/q}(0) <= ½ and ∫p_q <= D.
   - Consequence: if a = ½ (the D-extremal value), ALL rational macroscopic atoms vanish (each W(0) >= 0 and PD).
   - The escapes have no atoms, so this does not move the reach. It does constrain how binary sets could fix their
     kurtosis.
4. KURTOSIS heuristic (the fourth-moment layer).
   - Binary local kurtosis is 1/e − 3: equal to 1 at e = ¼, below 3 for e > 1/6.
   - Positive-amplitude cosine structures have kurtosis >= 1.5 (all additive quadruples count with weight >= 0; the
     minimum is a single cosine), unless rational (subgroup) atoms are present.
   - Mesoscopic positive structures tend to 3 − o(1) in "excess over random". But the DC barrier says the anchored
     fourth moment is swamped by m⁴/ℓ, so this is NOT a proof; it needs m << X^{1/4}.
   - Near t = 0 with a = ½, binary needs an almost two-valued ±½ residual, and item 3 forbids the π-atom. So the
     two-valuedness must come from mesoscopic structure. Is it possible?
     - Cyclic analogue: sparse partial difference sets give two-valued sequences with min ≈ −√J/4.
     - In Z_p, nontrivial PDS are essentially Paley only (Ma), which is NOT sparse.
     - So the integer problem beyond 1/D may hinge on a Ma-type rigidity in Z.
5. Strategic review.
   - Done: the second-order theory, both reach and certificate machinery (7.50 proven, 8.571 the truth). The
     third-order layer is free.
   - Live:
     - (a) the certificate push 7.5 → 8.5 (bounded, mechanical);
     - (b) the fourth-moment / approximate-binarity layer: either a weighted escape with four Bernoulli moments (then
       its rounding cost is the last gap to a dense counterexample), or a second-order inequality on a binary-derived
       object forcing d < D;
     - (c) arithmetic rigidity (A ∩ qZ, PDS in Z).
   - Theory of success: a counterexample needs a weighted-PDS spike structure with PD envelopes. A proof needs to show
     its impossibility. Both are now concrete.
   - Bias check: we have only ever found R >= ~0.55 numerically, and every rounding attempt failed by bulk energy. But
     the DC barrier means the analytic tools we have cannot see this obstruction, so absence of a proof is expected,
     not evidence of a counterexample.
6. (cont. 14, added while round 11 runs) ROUNDING REDUCTION: boundedness is the binary-sensitive core.
   - Let c ∈ [0,1]^X with min Σc_k cos kx >= −M and variance V := Σ_k c_k(1 − c_k).
   - Random rounding (b_k ~ Bernoulli(c_k), independent): at each of 4X grid points the error is a sum of independent
     centred terms with variance <= V. A union bound plus the Bernstein/Marcinkiewicz grid bound for degree-X
     polynomials gives max_x |Σ(b_k − c_k)cos kx| = O(√(V log X)) w.h.p.
   - Better: first freeze the coordinates within ε of {0,1}, then use partial-colouring discrepancy (Spencer,
     Lovett–Meka) on the F = O(V/ε) remaining coordinates, at cost O(√(F log(N/F)))). This is polylog-lossy at worst.
   - Hence: a [0,1]-valued "escape" with M = o(√X) and V = o(X/polylog X), at density >= 1/C, yields a BINARY dense
     counterexample. Conversely binary sets have V = 0. So, up to logarithms:
         binary problem ⟺ positivity + coefficients in [0,1] + approximate integrality.
   - For c ∈ [0,1], c² <= c, so "second-moment profile = first" already forces approximate integrality (Bhatia–Davis
     equality ⇒ two-point law). The FOUR-moment layer of round 10 is therefore NOT a relaxation: with boundedness it is
     the binary problem itself.
   - The P61 escapes fail precisely by being UNBOUNDED (Gaussian r_k, |r| > ½ with probability about 32% at p = ½).
   - So any proof of T-dense beyond 1/D must use coefficient BOUNDEDNESS (a convex constraint) together with the
     second-moment identity. Any construction must produce a bounded (two-point-law) residual made of positive packets,
     i.e. weighted-PDS spike structure.
   - This sharpens round 11's Task 2. The cleanest obstruction target is now: positivity + |r_k| <= max(p, 1 − p) +
     e = p(1 − p) ⇒ d <= D' < D. Bounded random variables with the Bhatia–Davis maximal variance are two-point, so the
     residual's local law is forced.

## 2026-10-19 (night, cont. 15) — While round 11 runs: front rigidity, taper coupling, and what binarisation really needs (lead)
Context: round 11 (report, partial) has D₁ = 259/2000 (pending lead verification), the quantified DC barrier, the
full-Haar kurtosis inequality, and the Paley boundary (positive packets at quadratic-residue positions give a two-valued
residual off qZ, but half the variance sits on the exceptional class qZ with unbounded values).
1. Kurtosis is the wrong proxy; two-pointness is the right one (HEURISTIC + elementary checks).
   - One bounded packet r_k = W(k/X)cos(kθ) is a positive configuration with m = O(1) and local kurtosis 3/2.
     J equal incommensurable packets give 3 − 3/(2J). So bounded positive configurations can be platykurtic.
   - What they cannot be is TWO-POINT. A finite non-order-2 positive configuration has kurtosis >= 3/2 (full-Haar), and
     binary at p = ½ needs 1. The order-2 character (−1)^k is the only exception, and it is the θ = π rational atom.
2. Front rigidity in the exact (macroscopic) model (PROVED in that model; consistent with P53, different emphasis).
   - Model: the local residual at t is 1_{E_t} − p_t on a compact abelian H (closure of k ↦ (kθ)_θ), Haar-equidistributed
     windows, with expansion Σ_θ a_θ m_θ(t) χ_θ, a_θ >= 0 (positive spikes), m_θ continuous PD in t, m_θ(0) = 1.
   - t = 0: ĝ >= 0 for g = 1_{E_0}. Fejér summation gives Σĝ = g(0) <= 1, so g is continuous, E_0 is clopen and 0 ∈ E_0.
     A {0,1}-valued continuous PD function with g(0) = 1 is the indicator of an open subgroup H_0 (|g(x+z) − g(z)|² <=
     2(1 − g(x))). So a_θ = (1/ℓ)·1[θ ∈ H_0^⊥], ℓ = 1/p_0.
   - t > 0: the spectrum of 1_{E_t} lies in the finite group H_0^⊥, so E_t is a union of H_0-cosets and p_t ∈ (1/ℓ)Z.
     Continuity forces p_t ≡ 1/ℓ. But energy-PD makes e = p(1 − p) PD with support [−1, 1], so e(1) = 0 and p(1) = 0.
     Contradiction.
   - At p_0 = ½ the subgroup has index 2: the pattern is (−1)^k, a θ = π atom of weight ½. This also contradicts round
     11's total rational-atom budget Σ W_θ(0) <= ½ − a at a = ½.
3. The Z-specific lever is the TAPER COUPLING (Fourier domination).
   - All local patterns share one spike set, and the envelopes are PD, so |m_θ(t)| <= 1. Hence |1̂_{E_t}(θ)| <=
     1̂_{E_0}(θ) for every θ ≠ 0 and every t. The binary pattern at every frequency position is Fourier-dominated, with the
     same signs, by the front pattern.
   - Z_p has no analogue. Embedding (round 11): Z_p-Chowla at density δ ⇒ T-dense(1/δ). The cyclic problem is HARDER,
     since Sanders 0807.5104 Thm 1.2 has only exponent 1/3 for half-sets. The taper is what makes Z easier, and
     second-order theory already exploits it up to 1/D.
4. Mesoscopic version: what a proof beyond 1/D must supply.
   - The front step needs "ε-approximately PD indicator ⇒ near open subgroup" in the mesoscopic closure group. The
     tolerance is ε·N ≈ M = o(√N) in eigenvalue normalization (N ≈ X resolvable points), i.e. a √-strength Sanders
     dichotomy at density ½. That is open even for Z_p.
   - Either the coupling (3) substitutes for √-Sanders, or the front must have p(0) < ½ for a different reason.
   - Candidate lemma (TD-COUPLE, CONJECTURED). Let E_0 ⊂ G (|G| = N) have density ½ and λ_min(E_0) >= −K. Let E_t,
     t ∈ [0, 1], be sets with 1̂_{E_t} = 1̂_{E_0}·m(t), each m(·, θ) PD in t, and |E_1| = 0. Then K >= c√N.
     - The coupling alone (no taper) is vacuous.
     - Falsification test: cyclic G = Z_q with E_0 = Paley. Ask whether any dominated family tapers to density 0 with
       PD envelopes up to tolerance o(√q)/q.
5. Staircase-taper cost (HEURISTIC). Consider a residue-pattern family A = {k : k mod q ∈ E_{k/X}}, q <= X, built by
   removing residues one at a time.
   - Each spike's envelope Ê_t(r) is a staircase of about q steps of size about 1/q. Its Dirichlet tails at offset y
     add up to about √q/(q|y|) for random removal times, which is X/√q at y ≈ 1/X.
   - So uncoordinated binary tapers cost M ≳ X/√q >= √X. Single-modulus mesoscopic designs need COORDINATED removal
     times across all spikes. That is the integer form of the coupling in (3).
6. Capacity check (elementary): binary completion of round 11's Paley escape fails.
   - The QNR spikes of the binary pattern on Z∖qZ have height about −X/(2√q).
   - The only compensator at primitive positions 2πs/q is A ∩ qZ, whose spike height is <= |A ∩ qZ| <= X/q.
   - Hence M >= X/(2√q) − X/q, i.e. R ≳ const for every q <= X. In general, a position s with gcd(s, N) = g has capacity
     about gX/N.
Decision: the binarisation layer is a coupled (taper + front) problem, not a free cyclic one. Round 12 candidates:
(a) TD-COUPLE in Z_q and in mesoscopic Bohr models (prove or construct); (b) quantify (2) with tolerances (a finite
P53 at the front with explicit √-type loss); (c) continue certificate tightening only if cheap.

## 2026-10-19 (night, cont. 16) — Round 11 verified (T-dense(7.72)); FRONT-½ and its cyclic barrier; Parseval roughness (lead)
Round 11: P63 and E85 (independent check: 22615 leaves, 0 failures). D₁ = 259/2000 ⇒ T-dense(C < 7.7220). The four-moment
alternative is unresolved. The dilation/support-line certificate family saturates near 0.129 (discovery), so 8.57 needs a
new relaxation, not finer grids.
1. FRONT-½ is the cleanest binary target.
   - P61 step 9 gives d <= 4a(1 − a)D with a = p(0) (φ(sx) <= sφ(x)).
   - So any universal a* < ½ with a <= a* in binary limits gives T-dense(C < 1/(4a*(1 − a*)D)), BEYOND the
     second-order reach 1/D.
   - The exact reach under p(0) <= a* is 1/sup_w ∫φ(4a*(1 − a*)w²).
   - Thresholds (HEURISTIC, macroscopic full-Haar model): binary kurtosis 1/e − 3 < 3/2, the minimum for positive
     finite configurations, exactly when p > 1/3. The Gaussian kurtosis 3 threshold is p > 0.211.
2. The front object (PROVED reduction, lead).
   - Let a = ½ and ε > 0 be small, Y = εX and s_k = 2·1_A(k) − 1 (k <= Y).
   - The Fejér low-pass of h = g + m >= 0 at scale Y gives
         S(x) := Σ_{k<=Y} (1 − k/Y) s_k cos kx >= −4m − o(√Y)   on Y^{−1/2} <= |x| <= π.
     The profile mismatch (½ − local average) is smooth and lives at |x| <~ 1/h.
   - The torsion budget (P63.4) at a = ½ says s has no macroscopic rational atoms.
   - Hence FRONT-½ ⟸ TBS (tapered balanced sign lemma): every locally balanced sign sequence on [1, Y] without
     macroscopic rational atoms has min_{|x| >= Y^{−1/2}} S(x) <= −c√Y.
     - Untapered TBS is TRUE with no atom hypothesis: P34 (one-sided Littlewood, kernel-checked) gives 0.28√Y.
     - The Fejér taper admits s ≡ 1 and s = (−1)^k (rational atoms), so the hypothesis is essential.
3. CYCLIC BARRIER (PROVED, lead): TBS ⇒ cyclic half-set Chowla.
   - Let q be prime and S ⊂ Z_q a symmetric half-set with λ_γ >= −K (γ ≠ 0). Put s_c = 2·1_S(c) − 1 and repeat it L
     times (Y = Lq, L fixed).
   - Then S(x) = (1/(2q))Σ_γ λ_γ F_Y(x − 2πγ/q) ∓ ½, since the floor terms sum to −s_0/2.
     - Fejér peaks have width ≈ 1/Y < 2π/q, and their tails cost O(K/L). Hence S >= −O(KL) − O(1).
     - Correlations with any fixed rational a/b (b < L) are O(q^{−1/2}(b/L)²) -> 0, so there are no macroscopic
       atoms.
   - So K = o(√q) would give a TBS counterexample.
   - Consequence: proving a < ½ from the FRONT ALONE would prove the √-strength cyclic half-set conjecture, which is
     open (Sanders 0807.5104v2 Thm 1.2: exponent 1/3).
   - Any proof of FRONT-½ must use the TAPER COUPLING (cont. 15.3). Conversely, cyclic half-set counterexamples (if
     they exist) are admissible fronts. The open question is then whether they can be tapered.
4. Parseval roughness: the taper's price for periodic fronts.
   - Model: a locally N-periodic family, A ∩ window = {k : k mod N ∈ E_t}, with E_t ⊂ Z_N nested and N << window << X.
   - Then f_A(2πs/N + ξ/X) ≈ X·C_s(ξ), with C_s(ξ) = ∫_0^1 1̂_{E_t}(s)cos(ξt)dt.
   - Parseval on Z_N with nestedness (|E_t ∩ E_t'| = N p(max(t, t'))) gives the EXACT identity
         Σ_{s≠0}|∫1̂_{E_t}(s)e^{iξt}dt|² = ∫(−p'(u))·4sin²(ξu/2)/ξ² du − |p̂(ξ)|²  ≈ 2p(0)/ξ²   (ξ >> 1).
     So the spike envelopes are forced to be Hölder-½ rough ("Brownian"), whatever the removal order.
   - The values v_s = X·C_s(ξ) have mean O(X/(Nξ)) and RMS ≈ X√(p(0)/N)/ξ, with v_s <= Xd.
   - From min >= −M: Σv² <= max(v)·Σ|v| gives M >~ X p(0)/(N d ξ²) (PROVED in this model). So periodic structure with
     N << √X is impossible.
   - HEURISTIC: M >~ X√(p(0)/N), unless the roughness concentrates on few characters with large POSITIVE values
     (structured coset removals). This would exclude every periodic front with N << X.
   - Fronts with N ≈ X are not periodic within the front, so item 3's embedding does not survive a taper. This is the
     coupling in action.
5. Decision for round 12: the coupled front problem.
   - (T1) FRONT-½ via coupling (Fourier domination, PD envelopes, Parseval roughness, torsion budget, the full-Haar
     bound), with the cyclic barrier as a guard rail.
   - (T2) The rigorous Parseval-roughness theorem (quantitative P53 for locally periodic families) and its structured
     evasions.
   - (T3) A construction probe: Paley-type fronts (q ≈ X) with coordinated tapers, measuring R on the VM. This is
     Track C: if coupled tapers of strong fronts beat 1/D numerically, that is the first escape signal.
6. (cont. 16, added while round 12 runs) Two structural remarks (lead).
   - (a) The coupled object IS the original problem in product coordinates.
     - Joint structure: for each spike θ, W_θ(·) is PD in t (P48); for each t, W_·(t) is the transform of the
       two-valued local pattern. Together these say exactly that G(y, t) = 1_{E_t}(y) is PD on H × R.
     - The exact version is P53: a PD indicator is an open subgroup, which is impossible with t ∈ [−1, 1].
     - The mesoscopic version (H ≈ Z_N, N ≈ X) is "Chowla for E ⊂ Z_N × [−1, 1]". Via k ↦ (k mod N, k/X), E is just
       A. So beyond second order there is no further Z-specific lever except the subgroup restrictions (P63.4).
     - Everything else is binary Chowla itself. Hence T-dense beyond 1/D sits at the level of dense (cyclic/product)
       Chowla, with FRONT-½ as its cleanest instance.
   - (b) Partial-period lemma (PROVED, lead; used in the round-12 brief). Let S ⊂ Z_q be a symmetric half-set with
     λ_γ >= −K (γ ≠ 0), s_c = 2·1_S(c) − 1 and Y < q. Then for all x,
         Σ_{k<=Y}(1 − k/Y)s_k cos kx >= −K/2 − ½.
     Proof: S(x) = (1/(2q))Σ_γ λ_γ F_Y(x + 2πγ/q) − s_0/2 with Fejér F_Y >= 0, and Σ_γ F_Y(x + 2πγ/q) = q when Y < q;
     also λ_0 + K >= 0. So a cyclic counterexample restricted to ANY initial segment shorter than q, with Fejér taper,
     is a weighted integer near-counterexample (weights (1 − k/Y)·1_S(k)). Binarising the taper is the whole difficulty.
   - (c) P61 for sparse sets (sketch, lead).
     - Statement. Let n -> ∞ with M = o(√n), and let X* be the trimmed top scale (drop an o(√n) tail). The only binary
       input of P61(a) is the diagonal; for sparse sets the energy profile is the normalized density. So the limit
       profile π (when regular at 0) is PD (energy-PD) and satisfies ∫_0^1 φ(π/π(0)) <= D.
     - Example: π ∝ (1 − t)^β is excluded for β < β*, where ∫_0^1 φ(u^β)du = D. Since β = 1 gives 1/6 and β = 2 gives
       0.1073, β* ∈ (1, 2).
     - It is a sharp second-order front-loading criterion for ALL sets, ineffective. It sharpens P31/P47 qualitatively.
     - It says nothing about sets whose front lives at scales << X* (an atom of the limit at t = 0).
     - Status: SKETCH. Not recorded in PROOFS until the sparse normalization of every P61 step is written out.
7. (cont. 16) The cyclic barrier is robust under every positive operation (lead, PROVED-level remarks).
   - Positive convolutions are exactly "PD weight × front taper".
     - Any K >= 0 on T has a PD coefficient sequence κ with |κ_k| <= κ_0. Writing K = ν ⋆ F_Y (ν >= 0) gives
       κ_k = τ_k ν̂(k).
     - So positive convolutions access individual binary coefficients only as PD-weighted FRONT tapers: Fejér fronts,
       subgroup combs (A_q), and Bohr-tapers ν̂(k) = τ'(kθ).
     - Away from the front, binary information beyond second order is reachable only through x-space localization
       (Gabor), and is CLT-aggregated or DC-anchored (P63.2).
   - The partial-period lemma (6b) transfers to each of these.
     - Subgroup restriction of a cyclic pattern is again cyclic (q prime, so dilation permutes the spectrum).
     - Bohr-tapers in Z_q are dilated-interval tapers, and the same root-of-unity filter applies.
     - Multi-scale fronts (all Y <= q at once) are covered as well.
   - So every positive-operation route to binary information beyond 1/D meets the cyclic half-set problem.
   - Separately, by the embedding with q ≈ 2X + 1: cyclic dense Chowla at density 1/C ⇒ T-dense(C).
   - Strategic reading.
     - Beyond 1/D, T-dense lies between "second-order + taper" (exhausted) and cyclic dense Chowla (sufficient, open).
     - Unless a genuinely non-positive, Z-specific mechanism appears, the next lever is the CYCLIC DENSE PROBLEM itself
       (improve Sanders' exponent).
     - The alternatives are to finish the second-order program rigorously (8.57, effective constants, Lean).

## 2026-10-19 (night), cont. 17 — after round 12: where the missing ingredient sits
1. Round 12 verified (PROOFS P64; E89). Unconditional T-dense is unchanged at C < 7.722. Two exact reductions now pin
   the missing ingredient:
   - integer side: CSFG(20), a uniform front gap for support-restricted cyclic sets ⇒ T-dense beyond 1/D (R12-B);
   - cyclic side: TBS ⇒ cyclic half-set √-Chowla (R12-H plus the root filter). The scalar barrier R12-S shows that
     any proof must use the full off-zero convolution (binarity), not moments.
2. Why weak limits cannot finish the cyclic problem (lead).
   - Positivity algebra in Z_q: (r + Kδ_0) is PD, and so is its k-th Schur power. The cost is
     (1 + K)^k − 1 against q. So order-k information survives a weak limit only for K = o(q^{1/k}).
   - At order 2 (K = o(√q)), the limit objects at half density are consistent: p ≡ ½ (R12-H). Order 3 would need
     K = o(q^{1/3}), Sanders' range.
   - Hence a √q proof must be QUANTITATIVE at finite q. Parseval gives Λ >= (q/4 − K²)/K exactly, so √q follows from
     a peak lemma Λ <= CK (PK(1)). PK(η) for any η > 0 beats Sanders.
   - The finite second-order identity at γ = 2 gives only Λ <= √(2q)K (exponent 1/4; P64.12). The loss is the bound
     |Σ mixed pairs| <= 2KΣλ⁺, tight only if the large positive spectrum pairs with near-threshold negative values
     at 2 − β for every β. The next derivation must show that this pairing cannot hold at every γ at once.
3. Arithmetic view (lead remark, not yet used).
   - For prime q, {λ(γ)} is the Galois orbit of α = λ(1) ∈ Z[ζ + ζ⁻¹]. α + K is a totally positive algebraic integer
     whose trace/degree is K − ½. The Schur–Siegel–Smyth trace bound gives only K >= 2.27.
   - The power sums Σλ^k = q·T_k(B) − λ(0)^k are additive k-counts. Moments up to k = 3 cannot beat 1/3 (R12-S).
   - OPEN, and the first test for round 13: do the k >= 4 power-sum constraints, i.e. integrality and actual counts,
     already kill the R12-S fake?
4. Construction side (Track C, dormant since E42). P61 is sharp for positivity plus two binary moments.
   - So the WEIGHTED escapes at density up to D exist; the only open question is binarization.
   - A binary realization with M = o(√X) at density d < D would disprove Chowla. A realization with M ≈ c√X and small
     c would lower the record R.
   - Round 11's Paley escapes binarize badly: nearest rounding costs (X/8)∫w², and deleting qZ costs X/√q.
   - Not tried: structured binary local laws such as dilated near-intervals or sub-Paley sets (E41 optima) under a
     PD envelope, with error diffusion done in the spectral domain. Round 13 Task 2 probes this.
5. Plan.
   - Round 13 (codex): Task 1, PK(η) through full convolution, tested on exact cyclic optima. Task 2, a bounded probe
     of binary escapes.
   - Lead, foreground: write P61 for sparse sets in full (cont. 16.6c). It is a second-order front-loading criterion
     for ALL sets, the first T-dense-type statement with no density hypothesis.
6. (cont. 17) P61 for sparse sets, written out (lead). It is second-order TRIVIAL apart from the front shape.
   - Setting.
     - A_j with n -> ∞, M = o(√n), X = max A.
     - ν_j = (1/n)Σ_{a∈A}δ_{a/X} -> ν weakly. Assume ν has a bounded density near 0 (the regular case).
     - High-pass energy measures ε_j = (1/n)Σ_m r_m²δ_{m/X} -> ε, along a subsequence, with r = a − k_h⋆a as in P58.3.
   - Then:
     - (i) ν̂ >= 0 (the limit of f_A(y/X)/n >= −M/n). Gaussian testing plus the bounded density at 0 gives ν̂ ∈ L¹.
       So ν = π dt with π continuous and PD, π(0) = max π.
     - (ii) r² <= a + q² <= a + q, and the smoothed q has the same limit ν. So ε <= 2ν, and ε is regular at 0 too.
     - (iii) P61 steps 4–8 verbatim (normalize by √n instead of √X; the only input is m² <= M² = o(n)) give
           ẽ/ẽ(0) ∈ 𝒦 := closed conv{|w|² : w ∈ 𝒲},
       where ẽ is the density of ε. Jensen's φ step is one consequence; the convex-hull statement is the full content.
   - Sparse case: if also max_m q_m -> 0 (no locally dense clumps), then r² = a − 2aq + q² gives ε = ν. So
         π/π(0) ∈ 𝒦.
   - Consequences.
     - ∫_0^1 π/π(0) <= N₂ := sup_{w∈𝒲}∫_0^1|w|² ≈ 0.34349 (E82). So, with ∫_0^1 π = 1, π(0) >= 1/N₂ ≈ 2.911.
       This is EXACTLY P31(iii): ρ_∞ = 2N₂, since ρ_L's continuum form is sup∫_{−1}^{1} w² over w = v⋆ṽ/‖v‖²,
       v >= 0. The E48 value 0.687 = 2 × 0.3435 is consistent.
     - Example: the triangle profile π ∝ 1 − t has ∫ π/π(0) = ½ > N₂, so it is excluded.
   - SHARPNESS (P61(b) at sparsity δ). The packets give E r = 0 and E r² = cw². Adding the PD smooth part δw² gives
     first moment = second moment = δw². So sparse weighted escapes exist for every profile w² ∈ 𝒦, with
     M = O(√J), J = X^{0.9}, which is o(√(δX)) when δ >> X^{−0.1}.
   - OBSTRUCTION (preserved).
     - For sparse sets, second-order information is exhausted by the front-shape constraint 𝒦.
     - Binary coefficients have r^k = r for all k, while packet escapes are Gaussian. Third moments are free
       (DC barrier, P63.2).
     - So any sparse Chowla proof must use binarity at order >= 4, the same layer as T-dense beyond 1/D and as
       Bedert's run-tops (P20–P22, where group-agnostic arguments cap at 1/5).
   - Status: PROVED on paper (lead), modulo the regularity hypotheses stated above. Not recorded in PROOFS as a theorem,
     because its scalar content is P31(iii) and the rest is a shape constraint.
7. (cont. 17) Lead side observations while round 13 runs.
   - (a) PROVED (elementary). Scale-independence forces linear M ("2-D obstruction").
     - Setting: A = {v1 + L·v2 : (v1, v2) ∈ V}, V ⊂ [0, N)² with |V| >= δN², L >> N.
       - The curve x ↦ (x, Lx) mod 2π resolves T² at scale 1/N. So f_A >= −M gives
         F(θ) = Σ_V cos(v·θ) >= −M − o(n) on all of T².
       - The coefficient profile p on [0,1]², evenly extended, lives in the two opposite quadrants O+ ∪ O−. If
         M = o(n), it is PD on R².
       - A bounded PD density is continuous with p(0) = max p > 0, so it is positive on a full neighbourhood of 0.
         O+ ∪ O− contains no such neighbourhood. Contradiction.
     - Hence M >= c(δ)n: LINEAR.
     - Same for d >= 2 independent lacunary scales. More generally, M is additive over lacunary-separated dilates
       (cf. P27).
     - Meaning: a counterexample is "one-dimensional at every scale". Its mass must sit at a single scale or across
       dependent scales.
     - The dangerous regime is single-scale density below D ≈ 0.117, i.e. C > 8.57. Bu's sets live there (C ≈ 25,
       R -> ½).
   - (b) Dilation-deficit form of the cyclic problem.
     - For every dilate t and Fejér scale h: K >= (h/2 − Σ_{c∈B}ψ_h(tc))·q/(q − h), by P29 on Z_q.
     - So K is at least the one-sided, Fejér-smoothed discrepancy of g = 2·1_B − 1 over homogeneous progressions
       t·[−h, h]. These are exactly the rank-1 Bohr tests.
     - Paley: these deficits are smoothed character sums, of size ≍ √q·|L(1, χ)|. So rank-1 tests are tight up to
       L(1, χ).
     - Over all t the deficits have mean ≈ 0 and second moment ≈ (4/3)hq plus multiplicative correlations
       Σ_r Φ_h(r)·Σ_c g(c)g(rc).
     - The one-sided issue reappears: deficits are bounded below by −K, but positive deviations (biased dilates)
       are free.
   - (c) Correction of a slip, recorded so it is not repeated. Comparing Gaussian moments (2k−1)!!‖ν⁺‖^{2k} of the
     positive spectrum with the binary side does NOT improve with k. The c = 0 spike contributes (2K)^{2k}/q, so order
     2k gives only K >~ q^{1/(2k)}. The best is k = 2: q^{1/4}, the kurtosis route; the round-13 agent reached the same
     conclusion independently.
8. (cont. 17) Second-order sharpness holds at BOUNDED M (lead, PROVED, elementary). So weak-limit methods give no
   exponent below density D.
   - P61(b) used J = X^{0.9} packets; J = 1 suffices for the two-moment profiles. Take
         E_X = Σ_{k>=1} φ(w(k/X)²)cos kx + c[S_X(x − θ) + S_X(x + θ) − 2],   c = 1/√32,
     with θ ∉ πQ and S_X(x) = Σ_{|k|<=X} w(k/X)e^{ikx} >= 0.
   - Then E_X >= −¼ − 2c > −0.61 for every X.
   - Coefficients: φ(w²) + 4c·w·cos kθ. Their windowed first moment is p = φ(w²); the second is p² + 8c²w² =
     p² + w²/4 = p. These are exactly P61's binary profiles, with |coefficients| <= 1.21.
   - Consequence. "Positivity + two moment profiles" cannot force M -> ∞ at any density below D, let alone M >= n^θ.
     Every exponent result for C > 1/D (Bu ¼, Sanders/JMTZ cyclic) must use finite binary structure, not weak
     second-order limits.
   - Third order: P62's gadget costs X^{7/15}. A PD gadget z_{jL} = v·σ(jL/X) (σ PD, L ~ v³) costs only v/2, but
     its third profile v³σ³/L lies in the PD cone.
   - OPEN, small: under M = o(X^{1/3}), must the third-profile defect s = e(1 − 2p) lie in the PD cone generated by
     cubes? If that is forced and fails for the E82 optimizer, it would give a reach D_3 < D for counterexamples with
     M = o(n^{1/3}), i.e. T-dense at exponent 1/3 beyond 8.57. That is a density-limited partial result; it does not
     cover all C.
9. (cont. 17) THE CUBIC FRONT CAP (lead) — PROOFS P66, the first positive result of this block.
   - Under M = o(X^{1/3}), the Schur cube of the high-pass coefficient sequence is PD with error 4m³/X -> 0. So the
     binary cubic profile g(p) = p(1 − p)(1 − 2p) is PD.
   - With p continuous from a down to 0, this forces a <= u* = (3 − √3)/6. Then P61 at σ = 2/3 gives
     d <= (2/3)·259/2000.
   - Result: M >= c(C)n^{1/3} for C < 9(1 + √3)/2 = 12.294 rigorously (Beckner: d <= u*·2/(3√3) = (√3 − 1)/9),
     and C ≈ 15.6 numerically (E93b).
   - The same DC barrier that blinds cubic information at exponent ½ opens it at exponent 1/3. It is the order
     hierarchy read the other way: order j costs m^j/X.
   - Next:
     - (i) a rigorous D_{2/3} certificate (P63 machinery with φ(2x/3), plus the cubic PD constraint), to move
       11.58 towards 15.6;
     - (ii) codex adversarial check of P66;
     - (iii) in the cyclic setting, the same cubic-profile argument needs K = o(q^{1/3}). Does it give anything for
       Sanders-type half-sets? There is no taper (p ≡ ½ is allowed), so no.

## 2026-10-19 (cont. 18) — round 14 read, rigorous range of P66 widened, and the moment-method ceiling for θ > ¼
1. P66 range widened (E94b, RIGOROUS, computer-assisted).
   - Mix the two rigorous bounds on 𝒲 pointwise: φ(2x/3) <= α1φ(x) + α2x on [0, 1].
   - Exact-rational bisection certificate with α1 = 0.233809 and α2 = 0.117344 gives D_{2/3} <= 0.0754440, hence
     exponent 1/3 for C < 13.2548.
   - A dedicated D_{2/3} Schur-test LP (E95; P63 code with φ(σx²)) saturates at 0.0723 (C ≈ 13.8). The family
     overshoots the truth by 9%, as at σ = 1. Certifying it would gain only 0.5 in C, so it is left for an agent.
2. WHY no moment method gives θ > ¼ for all C (lead; argument, not a theorem about all methods).
   - At exponent θ > ¼ only Schur orders j <= 3 are affordable, since order j costs m^j/X.
   - At small density every binary moment profile is ≈ p: e = p(1 − p) ≈ p and g(p) ≈ p. So every order-<=3 profile
     constraint is satisfied by a small multiple of any PD bump. Low density can never be contradicted by profiles.
   - The reach of every profile method at θ > ¼ is therefore the third-order reach C_3 (≈ 15.6 numerically, E93b,
     before dilation-coupled third-order constraints). This is the exact analogue of the second-order bounded-M
     sharpness (cont. 17.8).
   - Rescaling does not help either. Fejér tapers at a smaller scale Y give profiles w^j·(moment) with
     w = (1 − |t|)₊. Constant densities pass at every scale because every power of w is Pólya-convex, hence PD. The
     contradiction is intrinsically the HARD boundary at X.
3. Ideas tried and parked (lead, quick).
   - (a) Bu's Prop. 9.7 gives M³‖f‖₁ >~ n/C. If ‖f‖₁ <= M^{1−δ} this gives exponent 1/(4 − δ) for all C. The
     complementary case is spread negativity, |{f < −M^{1−δ}/4}| >~ M^{−δ}, and no lever was found for it.
     Littlewood (McGehee–Pigno–Smith) gives ‖f‖₁ >~ log n, so the first branch alone never reaches 1/3.
   - (b) Galois. For integer k >= K, λ + k is totally positive in Q(ζ + ζ̄). The Schur–Siegel–Smyth trace bound gives
     only k >= 2.3. Resultant and capacity constraints are scale-free and too weak at |λ| ~ √q.
   - (c) Cyclic small-spectrum branch, with S the positive mass. L ≈ ½ + S/q, Λ <~ K(S/q)², and Parseval gives
     ΛS >~ q²/8. Eliminating S again gives K⁴ >~ q. Round 14 (P67.3) found the same wall: an estimate better than
     Λ = O(KL²) is required.
4. Strategic review after round 14.
   - Proved this session:
     - T-dense at exponent ½ for C < 7.722;
     - exponent 1/3 for C < 13.25.
   - Barriers: second-order sharpness (bounded M); the third-order ceiling (item 2); P67 for Sanders-type transfers;
     R12-S/R13 for scalar cyclic arguments.
   - Every route to "beyond ¼ at all densities" or "beyond 8.57 at ½" now runs through ONE missing estimate: a
     one-sided Boolean peak bound better than second order (QU(β > 1)). In the integer setting this is the FRONT gap.
   - Next round: independent adversarial verification of P66 (our new theorem), together with the third-order
     sharpness question that would make item 2 a theorem.
   - The QU wall stays the long-term main line. Its next attack should use the integer TAPER (absent in cyclic
     half-sets): CSFG-type statements, where the set is confined to |c| <= q/4.
5. (cont. 18) The EQUALITY CASE of the cyclic ¼ argument, fully worked out (lead, half-sets; paper reasoning, labeled).
   - Write b − ½ = P̌ − Ň, with P = λ⁺ and N = λ⁻ on γ ≠ 0, so both P̌ and Ň are PD.
   - Equality in "Λ <= √(2q)K together with ΛK >= q/4" forces all of the following.
     - (i) N ≈ K on almost all γ, so Ň ≈ K·δ_0. The c = 0 spike holds all of Ň's L² mass.
     - (ii) The positive spectrum Π has |Π| ≈ 4K² ≈ √q·const, with heights ≈ q/(4K).
     - (iii) Off x = 0, P̌ = b − ½ = ±½ EXACTLY, and P̌ has nonnegative Fourier coefficients c_γ ≈ 1/(4K) on Π.
     - (iv) Then P̌² ≡ ¼ off 0, so for every ξ ≠ 0: Σ_{γ+β=ξ} c_γc_β = (K'² − ¼)/q with K' = P̌(0). Π + Π must cover
       Z_q UNIFORMLY (a weighted symmetric perfect difference set), so |Π|² >= q − 1. This recovers K >~ q^{1/4}
       exactly.
   - Galois check.
     - All λ(γ) are conjugates of α = λ(1). Exactly two values force α into Q(√q), with EQUAL multiplicities (Paley,
       K ≈ √q/2).
     - So the ¼-extremal configuration must be near-two-valued with very UNEQUAL multiplicities (|Π| ~ √q against
       q/2).
     - Small-q optima (E41) look nothing like it: they are dilated near-intervals with one giant peak Λ ≈ 0.27q.
   - Target (stability): prove that deviation from (i)–(iv) improves the second-order bound quantitatively, and that
     (iii)–(iv) cannot hold approximately. The second part should use positivity of c (no cancellation in P̌²),
     flatness and Galois / unequal multiplicities.
   - This is a concrete route past ¼ that the R13 fakes need not satisfy. They are not Boolean, so (iii) is unavailable
     to them.
6. (cont. 18) CORRECTION to item 5 (lead, same night). Item 5(i) drops the NN term of the identity at 2γ₀; the
   original item 5 is kept above.
   - Exact form, with Q = N⋆N (unnormalized):
         ΣPP' + Q(2γ₀) = 2ΣP(β)N(2γ₀ − β) + λ(2γ₀),   sums over β ∉ {0, 2γ₀}.
   - For x, y ∈ [0, K] we have xy >= K(x + y) − K². So, with T = ΣN = S + m,
         Q(2γ₀) >= 2K(T − qK/2)₊.
   - Hence Λ² <= 2K(min(T, qK/2) − m) + Λ. With Parseval (Λ >= (q²/4 − KT)/(T − m)) this gives K⁴ >= q/16, i.e.
     K >= ½q^{1/4} (crude constant). Item 5's "N ≈ K a.e." is not the equality case.
   - Equality now needs:
     - N ≈ K on a symmetric set 𝒩 of density about ½;
     - 𝒩 ∩ (2γ − 𝒩) ≈ ∅ for every peak γ carrying the Parseval mass;
     - λ ≈ 0 on most of the rest;
     - about K² peaks of height ≈ q/(2K).
   - HEURISTIC consequence. Two non-opposite peaks γ, γ' force 𝒩 ≈ 𝒩 + 2(γ − γ'): approximate translation
     invariance in Z_q. With several peaks this pushes towards ONE dilation direction d.
     - 𝒩 ≈ d·{|y| < q/4};
     - the peaks cluster at y ≈ ±q/4 within a window J << q;
     - the spectrum of B carries a MACROSCOPIC profile along d.
   - If made rigorous, this "profile along a dilation direction" structure is where integer-type taper/PD arguments
     (P58–P66) could enter the cyclic problem. This should be the next step after round 15, unless the agent finds
     it first.
7. (cont. 18, HEURISTIC; lead) Following item 6's clustered configuration to the physical side.
   Dilate so the direction is d = 1, and write y for frequency and x for position.
   - Spectrum model:
     - λ ≈ −K on |y| < q/4 (the set 𝒩);
     - λ ≈ 0 on |y| > q/4;
     - K² positive peaks of height ≈ q/(2K) in a window of width J around y = ±q/4.
   - Inverse transform of each part:
     - step part: −(K/q)·D_{q/4}(x), with D the Dirichlet kernel. It vanishes at even x and is ≈ ∓K/(πx) at odd
       x: a period-2 front of amplitude K/|x|.
     - peak part: Re e(x/4)·A(x), with envelope A(x) = Σ_j c_j e(jx/q), c_j >= 0 and A(0) = Σc ≈ S/q.
   - Flatness b − ½ = ±½ (x ≠ 0) has two consequences.
     - (a) Away from x = 0, |A(x)| ≈ 1/√2. A positive-coefficient sum of constant modulus is a single term (its
       autocorrelation would have to vanish off 0). So one peak, Λ ~ q, linear K: a contradiction.
     - (b) Near x = 0, the envelope spike A(0) ≈ K must be cancelled by the step part, which decays like K/x. A
       positive window gives A(x) ≈ Λ/(πx), so cancellation needs Λ ≈ K, i.e. q/(2K) ≈ K and K ≈ √(q/2).
   - So the configuration that the second-order argument cannot rule out is internally inconsistent for K << √q.
     NOT a proof.
   - Rigorous version needed:
     - (1) peaks with Parseval mass force 𝒩 to nearly avoid 2γ − 𝒩, hence approximate translation invariance and a
       single dilation direction;
     - (2) a stability form of "c >= 0 and |A| ≈ const ⇒ one dominant term", in L² with explicit errors;
     - (3) control of the x ≈ 0 front.
   - Candidate main task for round 16, if round 15 does not already reach it.
8. (cont. 18) CORRECTION to item 7(a) (lead, immediately).
   - "A positive-coefficient sum of constant modulus off 0 is a single term" is FALSE.
     - |A|² constant off 0 means c⋆c̃ = αδ + β·1. Singer difference sets (0/1 coefficients) realize this exactly in Z_v.
     - In a window of width J it is approximately realizable by Golomb-ruler/difference-set-like clusters.
   - So 7(a) gives no contradiction. The peak cluster must itself look like a (windowed) difference set Π' with
     |A(x)|² ≈ |Π'| − λ' + (Fejér bump of height ≈ |Π'|² and width q/J at 0).
   - 7(b) (front cancellation near x = 0) needs redoing with this envelope. The bump height |Π'|²c₀² must match the
     step part's K/|x| profile over |x| <~ q/J. This is unresolved.
   - Net: the clustered extremal configuration reduces to "windowed difference set of peaks + half-interval of −K
     values + period-2 front". It is NOT yet shown inconsistent. Item 6's rigorous part (K >= ½q^{1/4}) stands.

## 2026-10-19 (cont. 19) — FULL CHOWLA: architecture from scratch, and the single core statement (lead)
Labels: HEURISTIC unless marked. Purpose: replace the cyclic-only view (rounds 12–16) with an all-sets architecture.
1. Exact reformulations (PROVED, elementary). For finite symmetric S = ±A ⊂ Z \ {0} with N = |S| = 2n, set K = 2M.
   - (a) ν := (1 + D_S/K)dx/2π, with D_S = Σ_{k∈S} e^{ikx}, is a PROBABILITY measure iff min D_S >= −K. Its Fourier
     coefficients are 1/K on S and 0 elsewhere off 0. Booleanity is equivalent to
         ν⋆ν = (1/K)ν + (1 − 1/K)·Haar.
     Every convolution power is a mixture of ν and Haar (an "exact-mixing" step distribution).
   - (b) ‖dν/dx‖₂² = 1 + N/K². So Chowla (N <= CK²) is equivalent to "exact-mixing probability measures have bounded
     L² density".
   - (c) Equivalently, P = Π_0 + (1/K)Π_S (Π_S the Fourier projection onto S) is positivity preserving iff
     min D_S >= −K. Chowla says rank Π_S <= CK² for such P. P^{⋆2} = (1/K)P + (1 − 1/K)Π_0: a continuous "strongly
     regular" Markov operator (cyclic analogue: partial difference sets; Paley is the extremal case there).
   - (d) Graph form: λ_min(Cay(Z, S)) <= −c√N. For general groups the group-agnostic structure threshold is
     exponent ¼ (JMTZ; F_p^4 quadric complements have K = 3p ~ N^{1/4}, P20/P21). Beyond ¼ the argument MUST use
     the absence of subgroups: torsion-freeness and order in Z, primality in Z_q.
2. Architecture (spectrum of A at resolution 1/X, X = max A).
   - (i) SPREAD part ⇒ √ (P28 quantified, PROVED form).
     - M >= (1/4π√(X+1)) ∫ √(Φ_H(x)) dx, with Φ_H = Σ_{m>=H}|V(m,x)|² the K_H²-smoothed power spectrum (RMS over
       windows ≤ sup).
     - Hence M >~ √(η_eff·n), where η_eff = (∫√Φ)²/(2π∫Φ) is the effective spectral measure. A counterexample needs
       η_eff -> 0: SPIKY spectrum. (Consistent with E45: P28 gives ~0.21√n on non-deterministic sets.)
   - (ii) SPIKES must be Gibbs-free (first-order local argument; extends P29(b)).
     - Near a spike x₀ with |F_A(x₀)| = R₀ >> M: f(x₀ + y/X) ≈ R₀ Re Ψ̂_{x₀}(y), where ψ_{x₀} is the twisted profile
       (weak limit of e^{iax₀}1_A(a) at scale X).
     - f >= −M forces the HERMITIAN extension of ψ_{x₀} to be positive definite.
     - Consequences: ψ_{x₀}(0) is REAL and >= |ψ_{x₀}(t)|. EVERY spike is visible at the front of A with a real
       positive amplitude.
     - Example: 1-dim Bohr/Beatty sets 1[{kθ} ∈ S_{k/X}] force the front window S_0 to have nonnegative Fourier
       coefficients on the circle. A PD indicator is a subgroup, so these sets are never counterexamples.
   - (iii) The FRONT B = A ∩ [1, ηX] is L²-approximated (error <~ the spread part) by
         φ(k) = Σ_j c_j e^{−ikx_j},   c_j >= 0 (the spike amplitudes):
     φ is positive definite and φ ≈ 1_B.
     - m₀ := φ(0) = Σc_j satisfies 1 <~ m₀ <~ M, since ∫(tapered front)⁺ = ∫(tapered front)⁻ <= 2πM.
   - (iv) FEW-SPIKE regime (PROVED in the pointwise form). ψ = m₀ − Re φ is conditionally negative definite, so √ψ is
     subadditive. If |φ − 1_B| <= δ pointwise and m₀ < 4/3 − 5δ/3, then B is closed under ±, i.e. B = dZ ∩ window.
     - Then A' = (A ∩ dZ)/d has M(A') <= M(A) (P13a) and front density ≈ 1, contradicting the second-order front
       cap a <= ½ (P59.1) when A' is dense.
     - Needs an L² (Freiman-type) robust version. Since m₀ <~ M, this regime only matters for M = O(1); it closes the
       AP/subgroup alternative.
   - (v) MANY-SPIKE regime (m₀ >> 1): the CORE.
3. THE CORE (one statement; it is cyclic WRS/QU in integer form). "A {0,1}-function of density a <= ½ on a window
   of length Y, L²-approximated by a NONNEGATIVE combination φ of characters, must have φ(0) >~ √(aY), unless it is
   close to an AP."
   - Equivalently: 1_B + m₀δ_0 ≈ positive definite forces m₀ >~ √|B|.
   - The reduction is TIGHT: the front of a counterexample is again a near-counterexample. So no machinery avoids the
     core; it must be proved directly with a tool that sees the absence of subgroups:
     - robust uncertainty principles (Tao/Chebotarev in Z_p; sign-uncertainty);
     - Freiman 3k−4 / Vosper-type linear structure in Z and Z_p (sharp precisely because there is no torsion);
     - multiplicative / Gauss-sum structure (round 16).
   - The AP alternative is self-limiting: renormalization pushes the front density to 1 > ½.
4. Decision: the core is the only missing ingredient for full Chowla in this architecture. Items 2(i), 2(ii) and 2(iv)
   are to be written as precise lemmas. Round 17 attacks the core with the no-subgroup tools above if round 16 (WRS
   via adaptive displacements + Gauss sums) does not land.
5. Three new exact tools (lead, 2026-10-19; elementary; PROVED unless marked). Notation: S = ±A, d = |S| = 2n,
   K = 2M, G = K + D_S >= 0, p = G/K (probability density for dx/2π), X = max A.
   - (a) SUB-MULTIPLICATIVITY OF SPIKES (uses Booleanity). p⋆p = p/K + (1 − 1/K)Haar. Hence for all x, y and r > 0:
         p(B(x, r/2))·p(B(y, r/2)) <= p(B(x + y, r))/K + r/π.
     Proof: P(Y + Y' ∈ B(x+y, r)) >= P(Y ∈ B(x, r/2))P(Y' ∈ B(y, r/2)).
     Meaning: spikes of mass τ >> √r at x and y force mass >= K(τ² − r/π) at x + y. The spike set must be an
     approximate subgroup of T. At resolution 1/R the inequality is non-trivial only at frequency scales R >~ C²K²
     for dense sets of density 1/C. For Sidon-difference sets this is exactly borderline.
   - (b) BOUNDARY (TORSION-FREE) CONSTRAINT: ∫ log G dx/2π >= 0, i.e. ∫ log(M + f_A) >= −log 2.
     Proof: G = |U|² with U outer of degree X. The top coefficient gives u_X·conj(u_0) = 1, and |u_0| >= |u_X|
     because all roots have modulus >= 1. So 2 log|u_0| >= 0.
     Equivalent form: in L²(G dx/2π) the distance from e_0 to span{e_j : j >= 1} is >= 1 (Szegő–Kolmogorov). The
     Toeplitz inverse corner satisfies (T_N^{-1})_{00} <= 1 for every N.
     There is NO analogue in Z_q (no top frequency). This is the first constraint in the record that uses the ORDER
     of Z. Consequence: |{G <= ε}| <= log K/log(1/ε). Weak alone.
   - (c) GRAPH / GRAM FORM. KI + A_S is the Gram matrix of the characters e_k in L²(G). The star vector Σ_{s∈S} e_s
     gives d² <= K(dK + T), with T = #{(s, s') ∈ S² : s − s' ∈ S}. So T >= d²/K − dK: a counterexample has
     neighbourhoods of edge density >~ 1/K (many additive triples). Same content as the local star bound.
6. Round 16 (P69) closed the "heavy-core sumset" route with an exact fake. Decision: the next mechanism must use 5(a)
   + 5(b) together: spikes form an approximate group (a), and Z has no finite subgroups, so the dual Bohr set has a
   BOUNDARY; (b) is the boundary constraint.
   CONJECTURED "Bohr-boundary Gibbs lemma": a set S whose exact-mixing measure has its L² excess on an approximate
   subgroup of rank r must have min D_S <= −c·√d, with c independent of r.
   - First discriminating experiment: LIFT the F_p^4 elliptic-quadric complement (K ~ |S|^{1/4} in F_p^4, P20/E31) to
     Z through a rank-4 GAP/Bohr embedding, with and without tapered boundaries. Measure M/√n.
     - If the boundary costs only o(√n), we have a construction lead (Epoch track).
     - If the cost is >~ √n, the mechanism is identified for the lower-bound track.
7. (lead, after E99) C½ IS A SEMICIRCLE EDGE. HEURISTIC, with two PROVED inequalities.
   - Heuristic: if the self-difference graph H = Cay(Z,±A)[A] looks like a density-α random graph, its bottom edge is
     −2√(α(1−α)n). At α = ½ this is −√n, i.e. exactly M = √n/2 (C½). The star/sum-free extreme (P9) gives the same
     √n/2. E99 confirms a soft edge at ≈ −0.72√n on every near-extremal set, with delocalized bottom vectors.
   - (a) PROVED (Bhatia–Davis). Let H be any finite real symmetric matrix with tr H = 0 (e.g. Cay[W] for any W). Fix
     τ > 0; let μ_τ, v_τ be the mean and variance of the eigenvalues <= τ. Then
         −λ_min(H) >= v_τ/(τ + |μ_τ|) + |μ_τ|.
     (Those eigenvalues lie in [λ_min, τ], with μ_τ <= 0.) With P9, 2M >= the same quantity.
     So a √n-scale BULK — eigenvalues of size ~√n carrying a constant fraction of ‖H‖_F² = 2e — forces M >= c√n.
   - (b) PROVED (trace split). If λ_min(H) >= −K and tr H = 0, write H = P − N (spectral split). Then ‖N‖ <= K,
     tr P = tr N <= nK, and
         ‖H − P‖_F² <= nK².
     If K = ε√n, then H is ε-close in normalized Frobenius norm to a PSD matrix of trace <= εn^{3/2}; its effective rank
     is <= ε²n/α. So a counterexample's self-difference graph is, up to o(n²) entries, a PSD Gram matrix of vectors of
     squared norm <= εn^{1/2} on average, with inner products in {0,1}: a near-"clique-cover / Hoffman" structure.
   - Dichotomy to prove:
     - NOISE (a √n-scale bulk) ⇒ (a) ⇒ √n.
     - Otherwise (b) ⇒ near-PSD Boolean structure ⇒ approximate-group (clique) clusters ⇒ Gibbs (AP-type, P27/P29).
     - The AP is exactly the clique extreme: H = J − I.
8. Stabilizer heuristic, WITH ITS CORRECTION.
   - Translation-invariant linear spaces on Z: lines are translates of finite types L_j, and every finite set has
     trivial stabilizer. So each point lies on r = Σ|L_j| lines and d = Σ|L_j|(|L_j| − 1) <= r·max|L_j| <= r².
   - In groups with subgroups, cosets have stabilizer L, so lines per point = #types. That is how the F_p^4 quadric
     cone (a union of p² + 1 lines through 0) reaches K ~ d^{1/4}.
   - CORRECTION: λ_min = −r + min_θ Σ_j |F_{L_j}|², so λ_min >= −K does NOT give r <= K once K -> ∞. Hoffman theory
     gives r <= K only for BOUNDED K, which is the qualitative M -> ∞.
   - Exact model kept: S = ⊔_j (L_j − L_j)∖0 (a perfect difference family). There K = r − min Σ_j |F_{L_j}|², and
     Chowla ⟺ the sum of squared moduli dips >~ √(Σ|L_j|²) below its mean.
9. Clean falsifiable lemma (CONJECTURED, round 17), CLIQUE-S: every clique C of Cay(Z, S) (C − C ⊂ S ∪ {0}) satisfies
   |C| <= c₁K + c₂.
   - Tight examples: Sidon differences (B is a clique of size k = K) and Bu sets (3B is a clique, K ≈ k).
   - CLIQUE-S alone does not give Chowla. It is the rigidity input the structured branch of item 7 needs.
10. CORRECTIONS to items 7–9 (lead, 2026-10-19, after external review and round-17 interim findings). The originals
    are kept above; these supersede them.
    - (a) The BULK-vs-PSD dichotomy of item 7 is FALSE as stated, in three independent ways.
      - SPARSE (external review): ‖Cay[A]‖_F² = αn², so a √n-bulk of mass βn² needs β <= α. For random sum-free
        A ⊂ (N, 2N], Cay[A] = 0, and the trace split's "structured" branch is vacuous (P = 0). Their certificate is the
        star on {0} ∪ ±A: M >= √(n/2) (P9).
      - INTERMEDIATE (lead): random A of density α has bulk edge ≈ 2√(αn) and star certificate ≈ 1/α (the star couples
        to the top eigenvector αn). Both are ~n^{1/3} at α ~ n^{−1/3}. So P9 on A, {0} ∪ A and {0} ∪ ±A certifies only
        ~n^{1/3} there; this is the same exponent as the moment cap R12-S. The true M ~ √(n log n) comes from P28
        (Fourier spread). Check: E99b.
      - LARGE-M (round 17, PROVED): shifted intervals {m+1, …, 3m} have bipartite Cay[A] with macroscopic negative
        spectrum, an o(n²) √n-bulk, and Frobenius distance >~ n from the PSD cone. The dichotomy must be conditioned
        on λ_min >= −ε√n.
    - (b) CLIQUE-S (item 9) is FALSE (round 17; certified at L = 4096: clique/K >= 6.67; ~21 numerically at
      L = 262144). Smooth PD-profile roundings with a forced prefix interval of length L^{5/6}: cliques >> K. A
      cluster inside a smooth taper costs nothing. The structured branch needs a boundary-SHARPNESS condition, not
      clique size.
    - (c) "C½ is a semicircle edge" is DOWNGRADED to a suggestive analogy.
      - The measured edge −0.72√n certifies 0.36√n, not ½.
      - Simple random-matrix theory overshoots on Singer–Bu by 12–25%.
      - About 40% of M comes from vertices outside A.
    - (d) Corrected programme: a FOUR-WAY COVER under M = ε√n.
      - Mechanisms: (i) P28 spread; (ii) star/moment (P9 on {0} ∪ ±A, T₃); (iii) bulk (P9 on A + Bhatia–Davis);
        (iv) PD-profile/Gibbs with a sharpness condition.
      - Either their joint necessary conditions are inconsistent for small ε, or there is an explicit family on which
        all four are o(√n). The search for the latter (minimize the max of the four certificates, not M) is the
        decisive experiment.
    - (e) Process failure, recorded so it is not repeated. Before launching round 17 the lead did not adversarially
      test items 7–9 against:
      - the trivial cases (an empty graph, P = 0);
      - the Frobenius budget αn²;
      - the sparse rows of E99 itself (they were read for M, not for certificate strength);
      - the project's own smooth-profile roundings (E66), which already contained the CLIQUE-S counterexample shape.
      CLAUDE.md requires this step.
11. CORRECTION of item 10(a) "INTERMEDIATE" (E99b, E99c; NUMERICAL).
    - P9 on W2 = {0} ∪ ±A certifies roughly max(1/α, c(φ)αn, 3√(αn)) on random sets of density α with profile
      shape φ:
      - 1/α is the star;
      - c(φ)αn is a macroscopic negative eigenvalue (the graphon of W2 is ρ(|x − y|) on [−1, 1]); c(φ) > 0 iff φ is
        not PD (Gibbs in graph form; the boundary at max A);
      - 3√(αn) is the noise bulk.
    - FLAT profile: >~ √n at every density (E99b, n <= 16000: W2/√n ≈ 0.9 at α = n^{−1/2} and n^{−1/3}, up to 2.6 at
      α = n^{−1/4}). So item 10(a)'s "only n^{1/3} on {0} ∪ ±A" was WRONG for flat sets. It holds only for W = A and
      {0} ∪ A.
    - PD-TAPERED profile (triangle) at α = n^{−1/3}: W2/n^{1/3} = 3.30, 3.09, 3.09 at n ≈ 1000, 4000, 16000, while
      W2/√n = 1.04, 0.78, 0.62. So the gap is REAL, at exponent 1/3, but only for PD-tapered sets.
      - The true M of these sets is R ≈ 2.6–3.6 (Fourier fluctuations; P28 covers them).
      - Optimizing α, the worst case is ≈ 2.2n^{1/3} at α ≈ 0.45n^{−1/3}.
    - Refined adversary target: a PD-tapered set at density ~n^{−1/3} WITH a spiky spectrum (to defeat P28) and no
      sharp-boundary clusters.

## 2026-10-19 (cont. 20) — Lead's own derivation of the tapering core: POSITIVITY versus RESOLUTION
(Process change, user 2026-10-19: the lead does the core derivation; agents only falsify, verify and side-compute.)
1. IDENTIFICATION (lead; no new mathematics, but it fixes the target).
   - The Bhatia–Davis "bulk" route of cont. 19.7 is the graph analogue of P40 (spike truncation).
   - P40(c), applied to S = ±A: under M <= ε√n, 1_S keeps >= (1 − O(√ε))|S| of its ℓ² mass on the spike set
     U = {f > √(n/ε)}, with |U| <= ε^{3/2}.
   - So the tapering core is exactly: BOOLEAN + ONE-SIDED + BAND-LIMITED TO A SMALL SET U ⇒ contradiction. Round 17's
     four conditions are this statement plus bookkeeping.
2. PROVED (standard PD Cauchy–Schwarz, via GNS). For every positive-definite g on an abelian group and all x, y:
       |g(y) − g(y − x)|² <= 2g(0)(g(0) − Re g(x)).
   Consequences:
   - A PD window that is nearly Boolean is nearly invariant under translation by its own near-maximal set {g ≈ g(0)}.
   - On a CONNECTED torus, positivity plus a fat near-maximal set forces near-invariance under everything, i.e. the
     window is ≈ the full torus.
   - Fine structure is possible only through finite subgroups. Those reduce by dilation (P13a) or lower the rank.
3. MODEL CONSTANT (E100, E100b; NUMERICAL from exact series and searches).
   - For an arc Ω = [−ρ, ρ] ⊂ T = R/Z, all coefficients for 1 <= k <= L are >= 0 iff ρ <= 1/(2L). At ρ = 1/(2L),
     the fraction δ_L of ‖1_Ω‖² carried by |k| > L is 0.09717–0.09718 for L = 10 … 10⁴. Smaller arcs are worse
     (0.226 at ρ = 1/(4L), 0.53 at ρ = 1/(8L)).
   - SLSQP search over symmetric unions of <= 6 arc pairs with |Ω| <= ½, L = 16: the minimum is δ = 0.0947.
     Minimizers are DILATES of a single arc: the period-1/11 half-density pattern, i.e. the L' = 1 case,
     δ = ½ − 4/π² = 0.0947. Pairs at {0, ½} give 0.09713.
   - CONJECTURED PR(r = 1). If Ω = −Ω ⊂ T has 1̂_Ω(k) >= 0 for 1 <= k <= L and |Ω| <= ½, then δ_L(Ω) >= c* with
     c* = ½ − 4/π² ≈ 0.0947. Finite-subgroup windows reduce to this by dilation.
   - CONJECTURED PR(r): the same on T^r with c*_r > 0. Uniformity in the rank r is UNKNOWN and is the first danger.
4. ARCHITECTURE (how PR would close Chowla), with each step's status:
   - (a) [PROVED, P40(c)] Counterexample ⇒ 1_S band-limited to U up to O(√ε) relative ℓ² error.
   - (b) [MISSING: the inverse step] Band-limited Boolean ⇒ Bohr model: S ≈ {s : sθ ∈ Ω}·env(s/X'), with θ ∈ T^r,
     resolution L, and an absolutely continuous envelope at a chosen scale X'. Errors must be o(1) in relative ℓ².
   - (c) [PROVED in the dense case (P29(b), P48, P53); needs the density-normalized version] At every RESOLVED spike
     kθ, the twisted profile is PD, so 1̂_Ω(k) >= −O(ε/√n).
   - (d) [CONJECTURED PR(r)] Positivity on all resolved k leaves >= c*_r of Ω's mass unresolved, unless Ω ≈ T^r or Ω
     is invariant under a subtorus (lower the rank) or a finite subgroup (dilate). Unresolved mass contradicts (a)
     once √ε << c*_r.
   - (e) Ω ≈ T^r means no fine structure: S is a rounding of env alone. Then:
     - env ∈ {0,1} gives a sharp boundary (P70.2);
     - otherwise the rounding is not band-limited — contradicting (a) — or it is covered by P41 (deterministic) or
       P70.3 (independent).
   - The levels do NOT regress: a multi-level hierarchy of Bohr structures is ONE Bohr frame of higher rank. The cost
     moves into the rank.
5. HONEST RISK ASSESSMENT.
   - Step (b) is the hard part. P40 gives |U| <= ε^{3/2}, but U can consist of ~ε^{3/2}X narrow spikes with no
     additive structure. Spike sub-multiplicativity (cont. 19.5(a)) forces approximate-group structure only when
     individual spike masses are >~ 1/√K.
   - So the Bohr frame may have rank growing with n, and PR(r) must then be rank-uniform. If c*_r -> 0 with r, this
     route reduces to bounded-rank structure and FAILS for high-rank spike sets.
   - The first test is c*_r for r = 2, 3, 4 (balls, boxes, anisotropic windows).
6. Next derivations, by the lead:
   - (i) a paper proof of PR(1) with an explicit constant, via item 2 plus the Bernstein smoothness of the degree-L
     projection;
   - (ii) compute c*_r for small r (does it decay?);
   - (iii) state the density-normalized version of (c) precisely for the Bohr model;
   - (iv) attack (b) for spike sets of bounded "spike count per unit mass".
   An agent may adversarially test PR(r) and (iii) once the lead has stated them.
