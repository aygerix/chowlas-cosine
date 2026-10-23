# Certificates

## 2026-10-23 — dense one-third theorem for every C<400/29

The new cubic-profile support-cap envelope has a paper proof using
P66's actual Boolean limit profile BEFORE Gabor-Jensen. It avoids
assuming the cubic constraint for individual mixture generators.

Exact rational producer and independent verifier both reportPROVED:
815 pointwise leaves, including75 tangent leaves;127 CF support caps;
188 rederived support lines;64 continuum Schur cells. The target is
D=29/400, with strictly positive minimum Schur margin
251243300521/1966080000000000. The verifier independently rebuilds
both radical/tangent inequalities, checks cap rounding and complete
leaf coverage, proves the long lines by Sturm and reconstructs Schur
polynomials by direct exact integrals. Both use FLINT rationals.

Together with the audited mixture argument, this proves that for
every fixed0<C<400/29 there is ineffectivec(C)>0 with
M(A)>=c(C)|A|^(1/3) whenevermaxA<=C|A|, for ALL genuine finite
positive-integer supports. No endpoint equality, unrestricted exponent
gain, full Chowla, external priority or Lean/kernel claim. The earlier
P66/P68 certificate for1000/73 remains preserved.

[Complete proof](notes/cubic_profile_cap_2026-10-23.md),
[certificate](experiments/cubic_cap_2026-10-23/certificate.json),
[independent verification and hashes](experiments/cubic_cap_2026-10-23/independent_verification.json),
[sole-advisor audit](notes/advisor_two_block_gram_2026-10-23.md).

## 2026-10-23 — certified real-factor branch budgets and exact local traps

A={8,16,24} actualM=(17+7sqrt7)/27 is proved by exactcubic
factorization. ALL16realbranches have rigorousArb coefficient,
centroid,mass andvarianceenclosures. Independentrealquadratic/
complexlinearfactorizations agree at192/256bits. Meanmass exceeds
S/8, butsame-marginalcorrelatedcost<1. Strictbadlocalminima ofthe
jointcost are certified by rational comparisons againsteveryneighbor.
Thisexampleisimprimitive; gcdnormalization avoidsit.

PrimitiveA={1,7,8} has actualM3/2 by a squareidentitywithzeroat
primitivecuberoots. Itsdegree6 residual roots areproposednumerically
then certified in sixdisjointdisks by explicitRouche inequalities,
coveringthedegree. ALL8realbranches are evaluated at256bits,
withindependentcomplexlinearbudgetchecks. Meanmassalonepasses;
8meanmass/S+6meannegativevariance/V>27/20 invalidates the
unbiasedjointcertificate forEVERYC,r. Existinggoodbranchesremain.
No sampled minimum, universalChowla implication fromfinitecases,
kernelcheck or noveltyclaim. [Proof and data](notes/run_and_root_ensemble_2026-10-23.md),
[advisor audit](notes/advisor_run_multiplier_2026-10-23.md).

## 2026-10-23 — exact endpoint energy and transferred global bound

The existing triangular pilot enlarged by frequency65536 has
n32788,B65536 size10921 and exactH146387604. Direct integer
boundary-pair summation and full-polynomial integer autocorrelation
agree. Its global cosine floor follows analytically from the old
all-circleM<=75623/180 certificate and |cos(65536x)|<=1, giving
M<=75803/180. No grid minimum is used or recomputed. This proves
H/(actualK*|B|)>15 for that explicit set. Parent artifact hashes and
derived set hashes are saved in the verification JSON.

The separate asymptotic integer obstruction to EVERY linear-K
energy constant has a paper concentration/derivative proof; it is
not inferred from the finite ratio. New true endpoint cancellation
localizes the weaker quadratic-K energy question to an intermediate
spectral band. P22, with explicit admissibility repair, refutes its
group analogue, not the integer statement. Neither statement is
Lean/kernel checked; no full Chowla resolution or priority claim.
[Proof and artifacts](notes/ordered_boundary_2026-10-23.md),
[verification](experiments/ordered_boundary_2026-10-23/verification.json),
[independent internal review](notes/advisor_joint_boundary_2026-10-23.md).

## 2026-10-23 — quadratic convolution-loss family and independent finite bounds

The asymptotic theorem uses exact Boolean Fourier identities, a
piecewise-quadratic lens integral, the verified Spencer real-matrix
theorem, eight conditional affine-rounding stages, and Bernstein's
derivative inequality. It proves all-circleK=Theta(sqrtQ) and a
negative modulated SELF-convolution point of orderQ for every
sufficiently large Qdiv8. No sampled minimum or independence of
the final dependent bits enters the proof.

The separate finite Bernoulli candidate has exact coefficients/sets,
two ball point evaluators, and two all-circle upper arguments with
different remainder proofs (Taylor versus mean/noise Bernstein).
Both arithmetic implementations use Arb, not independent backends.
Best saved M upper is75623/180. Exact point intervals, all frequencies,
seed and proof constants are preserved in the artifacts.

[Proof and statuses](notes/modulated_triangle_2026-10-23.md),
[pilot](experiments/modulated_triangle_2026-10-23/pilot.json),
[independent checks](experiments/modulated_triangle_2026-10-23/verification.json),
[advisor audit](notes/advisor_modulated_convolution_2026-10-23.md).
Paper proof/internal scrutiny and exact finite certificates only;
no Lean/kernel verification, novelty certification or Chowla solution.

## 2026-10-23 — odd-zero disk phase certificates, paper scope only

An odd-zero disk of lambda+f_A gives an explicit positive lower
bound on conjugate-reversal energy for every complex polynomial
factor and every integer dilation. Multiple disks combine with
an exact finite-dimensional sampling Gram norm. These are paper
certificates; no numerical root-disk bounds were computed here.

The entire nonnegative-weight disk class cannot yield the proposed
universal n/M-scale bound: a band-limited vector majorant proves
the optimized functional too small on actual Bu supports. This
does not prove scalar factors close to real squares.
[Proof and independent audit](notes/odd_zero_phase_stability_2026-10-23.md).
No kernel verification or new finite-minimum claim.

## 2026-10-23 — exhaustive finite square checks and an all-degree paper theorem

For all8190 first-half bit vectors at even root degrees2..24,
src/boolean_reciprocal_square.py reconstructs signed rational h,
checks every off-center coefficient of h² in{0,1}, and independently
checks h autocorrelations. Only24 singleton/two-harmonic patterns
survive; exact Chebyshev/Sturm checks prove their unit-circle zeros
and actual M1or9/8. Artifact boolean_square_2026-10-23/enumeration.json
is terminal/PASS on Dirichlet. These are exact all-circle finite
certificates, not numerical minima or a degree-unrestricted proof.

The all-degree, all-real-power rigidity theorem is separately
proved on paper and internally audited in
[the proof note](notes/boolean_power_rigidity_2026-10-23.md).
No kernel verification or universal Chowla conclusion is asserted.

## 2026-10-23 — exact weighted phase countermodel, not a Boolean construction

Q2=(1+z18)[(1+z²)^4+z(z²-1)^3]/sqrt180 has exact
|Q2(e^(ix))|²=1+sum_(a=1)^13 c_a*cos(2ax), with positive
c=[82,68,14,2,1,7,34,41,90,41,34,7,1]/90. Nonnegativity
and the zero at x=pi/18 certify actual weighted M1 globally
(undoubled cosine convention minimizes at pi/9). Direct integer
autocorrelation and Fraction geometry give qmax²1/5,N/S1/4,
alpha21/127,delta0. This certifies a prescribed-factor phase
shortcut fails in the WEIGHTED relaxation; it is not a Boolean
A or an existential stable-branch falsifier.
[Proof and exact artifact](notes/joint_factor_budget_2026-10-23.md).
Verifier src/joint_factor_identities.py terminal/PASS13 on
Dirichlet. General inequalities remain independently reviewed
paper proofs, not Lean/kernel-checked statements.

## 2026-10-23 — rational contraction certifies an optimal n5 factor

For A=[1,5], the saved center/radius and rational inverse R certify
that x-RF(x) maps its closed rational box strictly into itself and
has derivative norm<1. Exact rank of R is5. Banach therefore gives
a true zero of the five autocorrelation polynomials in the box.
The corresponding Q has positive coefficients and includes
z²-2cz+1 with |c|<1. Exact coefficient matching gives
|Q|²=lambda+f_A; the unit-circle zero proves M(A)=lambda globally.
No cosine sample is used as an optimality premise.

The independent checker rebuilds Q by convolution and uses dual
interval derivatives rather than expanded SymPy polynomials. Both
use the same Fraction interval primitive, so independence is in
construction/differentiation, not the arithmetic backend. Additional
cubic root/discriminant gates exhaust real spectral branches and
prove all nonnegative optimal branches have qmax>1. The same saved
box certifies a signed branch satisfying the signed-centroid C1
conditions. [Complete statement/proof and source paths](notes/optimal_endpoint_n5_2026-10-23.md).
Status: interval-certified finite existence plus paper all-circle
and branch proofs, independently AI-reviewed; not Lean-checked and
not a universal factor-selection theorem.

## 2026-10-23 — exact all-class multiplicity/l1 upper and its barrier

For a k-point integer B, retain every nonzero positive difference
as A and let E_r=sum|r_d-r|. The exact identity
2r*f_A=|F_B|²-k+2sum(r-r_d)cos(dx) certifies
M(A)<=k/(2r)+E_r/r on the entire circle. No angular quadrature
is needed: verify distinctness, pair counts and the l1 remainder.
src/multiplicity_l1_pilot.py independently matches direct pair counts
to exact polynomial autocorrelation; saved final M_upper757/2 and
R_upper²=573049/4544 are rational, though weak.

A new internally reviewed paper theorem proves E_r>=((r-2)k+2r)/6
and this particular R_cert>1/2 for every k>=2,r>=2. The certificate
therefore cannot give a vanishing construction. It does not assert
actual M>sqrt(N)/2. [Full proof and signed-error scope](notes/multiplicity_centroid_2026-10-23.md).
The code/artifact are reproducible failed-mechanism records, not a
recommended new search or an Epoch solution.

## 2026-10-20 — selective reference and matching-window certificates

For fixed actual A, average the mixed positive moment matrix over equal-cardinality references; use Q_bar=2a_bar. Freezing only the short reference fibers keeps actual targets in the ruling cubic. Pairwise completion gives p^3 log^4 cost, while an exact primitive-relation/lattice bound gives off-left O(X^2U^2 log U). This yields deterministic square-root lower bounds for the stated cyclic-Sidon and windowed architectures, without a law on actual choices. References in a window are trimmed/padded within a Sidon curve to match cardinality. [All hypotheses and proof](notes/cstar_sidon_deterministic_2026-10-20.md). Six finite mixed certificates have exact rational positivity checks; full direct four-coordinate recounts at X64 and the two concrete base385 examples. The latter also have square-identity all-circle UPPER bounds. Data in `experiments/sidon_cutoff_2026-10-20/`; source-scoped verification limits remain explicit. No universal Chowla or Lean claim.

## 2026-10-20 — exact mixed cubic positivity on Sidon fibers

For q=D_A-D_B, mean-zero and real, let a=<D_A,q>, Q=||q||_2^2, H=<D_A,q^2>, K=2M(A). The moment matrix of (D_A+K)(s+tq)^2 is positive, so QK^2+HK-a^2>=0. A rational k with Qk^2+Hk-a^2<0 certifies M(A)>k/2 on the WHOLE scalar circle. Rank-one ruling inclusion-exclusion computes H exactly with integer polynomial/sparse convolutions; encoding kernel gap>3X prevents scalar aliases. Three finite certificates have ratio>0.313; X64 is independently recounted in four coordinates. These are negative-minimum lower bounds, not all-phase construction upper bounds. [Full statement, asymptotic sampler theorem and verification limits](notes/cstar_sidon_mixed_2026-10-20.md), data `experiments/sidon_fibers_2026-10-20/`.

## 2026-10-20 — positive Gaussian and residue-average lower certificates

[Statements, exact hypotheses and proofs](notes/cstar_wide_parity_2026-10-20.md). The nine disk-lens mean certificates use exact parity counts/rational CRT error; six also have positive periodic-Gaussian certificates with an explicit alias tail, independently rechecked at192 bits. Three changed center laws have exact mass/parity checks and independent endpoint-pair negative-point certificates, without global upper claims. The GL2(F_p) positive-average identity gives M(A)>=n/(8B^2) for ANY short-right-factor rank-one selection under the stated CRT encoding; it does not require enumerating all scalar phases. Two actual incomplete-fiber Boolean supports have separate192-bit scalar point checks, matching direct scalar and matrix-residue conventions. Data and rational witnesses: `experiments/wide_mean_2026-10-20/`. These are lower bounds on negative minima; no Epoch-valid all-circle upper bound, unrestricted Chowla proof, or Lean check is claimed.

## Method E2 (src/chowla.py: certify_lower_bound)
g(t) = f_A(2 pi t). Grid t_j = j/L (L power of 2 >= 16 max A). FLINT acb.dft (ball arithmetic, prec 96) encloses
g, g', g'', g''' at all grid points. For |s| <= 1/(2L): g(t_j+s) >= cubic Taylor polynomial - S4 (1/(2L))^4/24,
S4 = (2pi)^4 sum a^4. Cubic minimized exactly on the cell (endpoints + stable critical points); ball radii and a
1e-14 relative + 1e-12 absolute float pad subtracted. Output: rigorous lower bound for min f_A (modulo correctness of
FLINT and of the float-padding argument, which is documented inline).
## Method E3 (sturm_certify): exact integer polynomial P(y) = B_den sum T_a(y) + B_num, PARI polsturm on [-1,1].

## Dense-regime sets (2026-10-18) — examples/dense_certified.json
Method E2 (src/chowla.py certify_lower_bound: arb ball DFT of a^0..a^3 weights on 2L-grid, cubic Taylor per cell,
4th-order remainder S4 (π/2L)^4/24, float pads). Best: X30_s1 N=20 max 30, f_A >= −2.68817 for all real x, R <= 0.6011;
X50_s0 N=34 max 49, f_A >= −3.52350, R <= 0.6043. Re-verify: `.venv/bin/python -c "import sys,json;sys.path.insert(0,'src');
from chowla import certify_lower_bound as c;d=json.load(open('examples/dense_certified.json'));print(c(d['X50_s0']['A']))"`.

## C-N36 (2026-10-18): best finite set known to us, R(A) <= 0.564795
A = [1..11, 13..23, 25..31, 34, 35, 37, 44, 45, 48, 50]  (N = 36, max 50; examples/smallN_best.json key "36";
exhaustive optimum of the box [1,52], small-N agent).
Certificate 1 (lead): src/chowla.certify_lower_bound(A, oversample=64): arb ball-arithmetic DFT on L = 4096 points +
  4th-order Taylor remainder 4.3e−7 ⇒ min_x f_A(x) >= −3.3887702 ⇒ M(A) <= 3.3887702, R <= 0.564795.
Certificate 2 (agent): PARI/GP Sturm sequences on Σ T_a(t) + B over t ∈ [−1,1] bracket M(A) ∈ [3.3887696, 3.3887699].
Status: INTERVAL-CERTIFIED finite case (two independent methods). Says nothing about any limit.
Also certified (same method): N=35 (max 48) R <= 0.567674; N=34 (max 48) R <= 0.574135.

## C-SB (2026-10-18): Bu sums on full Singer sets (E25), examples/singer_bu/certified.json (S, shift, N, max, bound)
Method: src/chowla.certify_lower_bound(A, oversample=16) — arb ball DFT of f, f', f'', f''' on L = 2^⌈log2(16 max A)⌉
points + 4th-order Taylor remainder (rigorous lower bound on min over ALL real x). One method only (no Sturm check: degree
~1.9e5 is beyond the exact route); status INTERVAL-CERTIFIED (single method).
   q = 61: N = 3782, max 10707, min f >= −37.1485, R <= 0.60406
   q = 101: N = 10302, max 30575, min f >= −59.7566, R <= 0.58874
   q = 151: N = 22952, R <= 0.57770;  q = 199: N = 39800, R <= 0.56630;  q = 251: N = 63252, max 189688, R <= 0.56272
   q = 307: N = 94556, max 278751, min f >= −171.2117, R <= 0.55679;  q = 401: N = 161202, max 483272, R <= 0.55476
   (q = 307, 401 certified 2026-10-18 on the laptop with chowla.certify_lower_bound_blocked(A, oversample=16, blocks=64):
   same arb-DFT + Taylor certificate computed in 64 decimated residue blocks; validated bit-identical to the unblocked
   certifier on q = 61, 101 and N = 45. q = 401: grid estimate 0.55358, certificate loses 0.0012 to the Taylor remainder
   at oversample 16 — rerun at oversample 32 to tighten.)
   Tightened 2026-10-18 (certify_lower_bound_blocked, oversample 32, 128 blocks, L = 2^24, ~220 s each):
   q = 307: min f >= −171.184725, R <= 0.556699;  q = 401: min f >= −222.292595, **R <= 0.553656** (N = 161202).

## C-N45 (2026-10-18): N = 45, max 61 (E27; examples/milp/N45_best.json)
A = [1..13, 15..35, 37, 39, 40, 41, 45, 50, 52, 57, 58, 60, 61].
Certificate 1: chowla.certify_lower_bound(A, oversample=64) ⇒ min_x f_A >= −3.8360448 (arb ball DFT + Taylor).
Certificate 2: chowla.sturm_certify(A, 38360448, 10^7): PARI/GP Sturm count, Σ T_a(y) + 3.8360448 has no root in [−1,1]
  (True, 0); with 3.8360432 it has 2 roots. Hence M(A) ∈ [3.8360432, 3.8360448], R(A) <= 0.571844.
Status: INTERVAL-CERTIFIED finite case, two independent methods.

## C-N50 (2026-10-18 night): N = 50 structured-class records (E42; examples/construct/N50_certified.json)
A72 = [1..26, 28..40, 43, 44, 47, 49, 50, 52, 54, 60, 68, 69, 72] (max 72).
A68 = [1..18, 20..37, 39..42, 47, 48, 50, 52, 57, 61, 62, 64, 65, 68] (max 68).
Certificate 1: chowla.certify_lower_bound(A, oversample=64):
  - A72: min f >= −4.0309358;
  - A68: min f >= −4.0483108.
Certificate 2: chowla.sturm_certify(A, B, 10^7), PARI/GP 2.15.4 on dirichlet:
  - A72: Σ T_a + 4.0309358 has no root in [−1,1]; with 4.0309354 it has 2 roots.
  - A68: Σ T_a + 4.0483108 has no root in [−1,1]; with 4.0483104 it has 2 roots.
Hence M(A72) ∈ [4.0309354, 4.0309358] and **R <= 0.5700604**; M(A68) ∈ [4.0483104, 4.0483108] and R <= 0.5725176.
Status: INTERVAL-CERTIFIED finite case, two independent methods.
Reproduce with `src/dirun.sh -c 1 python .research/agents/construct_scratch/cert_n50.py`.

## KERNEL-CHECKED: P31 chain and the dense theorem (2026-10-19; Lean agent, lead-audited)
Files: lean/ChowlaCosine/P31/*.lean (2764 lines): WindowMoments, Averaging, Fejer, WindowBound, FejerRiesz, Main,
ElementaryConstant, ElementaryConvolution, AnalyticNikolskii, Corollaries.
Lead audit:
- `lake env lean` on a separate file, using the built .oleans as of 22:05. Every theorem below depends only on
  [propext, Classical.choice, Quot.sound].
- grep finds no sorry / axiom / admit / native_decide in the P31 sources.
Theorems (statements read by the lead):
- `finite_fejerRiesz (L) : FejerRiesz L`. Every real h whose complexification is a trigonometric polynomial of degree
  <= L and which is >= 0 everywhere equals |Σ_{j<=L} u_j e^{ijx}|² for some u ∈ C^{L+1}. This is the FULL finite
  Fejér–Riesz theorem, including zeros on the circle; the local mathlib has no version.
- `elementary_convolution_bound`: v >= 0 on Fin (L+1), Σv² = 1 ⇒ Σ_k (v∗v)_k² <= (811/1000)(L + 1) + 71/300
  (Lemma P31-E). The integral constant is certified by a 32-term geometric expansion with exact tail.
- `elementary_analyticNikolskii`: the same bound for all complex analytic coefficient vectors, as circle means of
  |U|⁴ and |U|².
- `p31_elementary` (Theorem 1 with the elementary constant). For every w, every finite A ⊂ N with all a > 0, and
  every M with ∀ real x, −M <= Σ_{a∈A} cos(ax):
      windowMass w·(|A|/2 + M²) <= ((811/1000)(max A + w + 1) + 71/300)·(M² + windowEnergy w A/2).
- `dense_elementary`. Same hypotheses plus (41/100)·max A <= |A| ⇒ √|A|/1000 <= M. Holds at every finite size (the
  small-X case uses the earlier checked bound M >= ½).
Meaning: Chowla's conjecture is KERNEL-VERIFIED for all sets of density >= 0.41 in [1, max A], with c₀ = 1/1000.
The constants are not optimized; the paper constants are in .research/notes/dense_chowla_P31.md (C3).

## 2026-10-19 (night) Beckner track T5 (Lean, codex agent; lead-audited)
Lead audit:
- `lake build` passes (8739 jobs).
- `lake env lean AxiomCheck.lean` gives 272/272 entries, each depending only on [propext, Classical.choice, Quot.sound].
- 0 sorryAx, and grep finds no sorry/axiom/native_decide in ChowlaCosine/Beckner or ChowlaCosine/P31.
KERNEL-CHECKED:
- `Beckner.young_finite`: Young's convolution inequality on ℝ for complex L^p functions. Every finite admissible triple
  1/p + 1/q = 1 + 1/r, constant 1.
- `young_conjugate`: the L^∞ boundary.
- `young_four_thirds`: L^{4/3} ∗ L^{4/3} ⊂ L², constant 1.
- Gaussian computations: `integral_gaussian_rpow`, `gaussian_convolution`, and exact attainment of 4/(3√3) by Gaussians,
  i.e. the sharpness lower bound.
- M4 infrastructure (51 declarations): heat-flow time/space derivatives, the heat equation for heat-flow
  convolutions, score/moment bounds, the weighted-frame variance identity, and the pointwise frame heat-defect
  nonnegativity (`frame_heat_defect_nonneg`).
NOT done:
- The sharp Young / Beckner upper bound (the global Brascamp–Lieb monotonicity application, the rescaling limits and
  density passage).
- M5 and the sinc P31-N constant.
- Consequently P31-N (Beckner constant 4/(3√3)≈0.76980) is still a paper result. The kernel-checked chain uses P31-E (0.811).
Report: .research/agents/lean_p31_report.md.

## 2026-10-19 (night) P34 + P33 + dilation pinch — KERNEL-CHECKED (codex Lean agent; lead-audited)
Lead audit:
- `lake build` passes (8745 jobs).
- `lake env lean AxiomCheck.lean` gives 321/321 entries, each depending only on [propext, Classical.choice, Quot.sound],
  with 0 sorryAx. 49 entries are new P34-namespace declarations.
- grep finds no sorry/axiom/native_decide in lean/ChowlaCosine/P34.
- Definitions checked: trigSum A b x = Σ_{j∈A} Re(b_j e^{ijx}); energy = Σ‖b_j‖²; windowFreq n = [1, n];
  littlewoodSum n ε x = Σ_{j=0}^n ε_j cos(jx).
Headline statements (exact; lean/ChowlaCosine/P34/):
- `p34_elementary` (Main.lean). For A ⊂ [1, n] positive, ‖b_j‖² <= 1 and ∀x, −M <= trigSum A b x:
  windowMass w·(M² + energy/2) <= elementaryC(n + w)·(M² + (windowMass w − 1)/4).
  `p34_main` is the general version, with explicit Fejér–Riesz/Nikolskii hypotheses.
- `p34_A` (Corollaries.lean). n >= 1, ‖b_j‖² = 1 on [1, n], ∀x, −M <= trigSum ⇒ √n/4 <= M.
- `p34_A_phases` (RealForm.lean). n >= 1, any θ : ℕ → ℝ, ∀x, −M <= Σ_{j=1}^n cos(jx − θ_j) ⇒ √n/4 <= M.
- `p34_B` (Littlewood.lean). n >= 1, ε_j ∈ {−1, 1} ⇒ (∃x, Σ_{j=0}^n ε_j cos jx <= 1 − √n/4) ∧
  (∃x, Σ_{j=0}^n ε_j cos jx >= √n/4 − 1).
- `p34_C` (Corollaries.lean). ‖b_j‖² <= 1, energy >= (41/100)n, ∀x, −M <= trigSum ⇒ √n/1000 <= M.
- `p33_ratio` (Secondary.lean). A nonempty, 1 <= m <= a <= X for all a ∈ A, ∀x, −M <= cosSum A x ⇒ |A|·m/X <= M.
- `dilation_pinch` (Secondary.lean). q >= 1, ∀x, −M <= cosSum A x ⇒ |A|/q − (1 − 1/q)M <= |A ∩ qℕ|.
Report: .research/agents/lean_p34_report.md.

## 2026-10-19 P36 truncation at gaps — KERNEL-CHECKED (codex Lean agent; lead-audited); Beckner M4 partial
Lead audit:
- `lake build` passes (8753 jobs).
- AxiomCheck gives 384/384 entries, all [propext, Classical.choice, Quot.sound], with 0 sorryAx.
- grep finds no sorry/axiom/native_decide in P36/ or Beckner/.
Statements (lean/ChowlaCosine/P36/Main.lean; cosSum A x = Σ_{a∈A} cos(a x)):
- `p36_truncation`. A positive, D >= 1, ∀x, −M <= cosSum A x ⇒
  ∀x, −(M + (1 − cos(π/(D+2)))·Σ_{a∈A, a<=D} a²) <= cosSum (A.filter (· <= D)) x.
  This is the exact sine kernel, with no fallback constant.
- `p36_gap`. Y <= D and no a ∈ A in (Y, D] ⇒ the error is <= (1 − cos(π/(D+2)))·Y²·|A ∩ [1, Y]|.
- `p36_gap_pi`. The same bound with error (π²/2)(Y/(D+2))²·|A ∩ [1, Y]|.
Beckner M4 (partial, NOT the sharp Young theorem):
- `geometricHeatProduct_integral_monotone`: monotone product integral for compact-support positive-mass data.
- `tendsto_sqrt_mul_heatFlow`: scalar large-time Gaussian asymptotic for every signed L¹ datum.
- Remaining: the product large-time limit, the initial-time passage, density, and the 2×2 frame algebra
  (.research/agents/lean_next_report.md).

## 2026-10-19 Geometric Brascamp–Lieb (planar, rank one) — KERNEL-CHECKED (codex Lean agent; lead-audited)
Lead audit: `lake build` passes (8757 jobs); AxiomCheck gives 422/422 standard-axiom entries, 0 sorryAx; no forbidden
tokens in Beckner/.
- `ChowlaCosine.Beckner.geometric_brascamp_lieb` (HeatFlowDensity.lean:211). Hypotheses: E is a real inner-product
  space with an orthonormal basis b : Fin 2; ι finite; f_i >= 0 integrable on ℝ; c_i >= 0; ‖u_i‖ = 1; and the frame
  identity Σ_i c_i⟨u_i, x⟩⟨u_i, y⟩ = ⟨x, y⟩ for all x, y. Conclusion: z ↦ Π_i f_i(⟨u_i, z⟩)^{c_i} is integrable on ℝ²
  and ∫ Π_i f_i(⟨u_i, z⟩)^{c_i} dz <= Π_i (∫ f_i)^{c_i}.
  There are no support, continuity or positive-mass hypotheses. This is the Ball–Barthe geometric Brascamp–Lieb
  inequality in the plane, proved by heat flow: large-time limit, initial-time Fatou passage and L¹ density.
- `youngFrame_isWeightedFrame`, `youngFrameMatrix_det` (= √a√b√d) and `youngFrame_sharp_factor`. These give the
  explicit Young frame for interior exponents and the exact Beckner factor Π A_{p_i}.
- NOT yet: the Lp change-of-variables passage to the sharp Young inequality, M5, P31-N
  (.research/agents/lean_m4_report.md).

## 2026-10-19 Beckner's sharp Young inequality on ℝ — KERNEL-CHECKED (codex Lean agent; lead-audited); M5
Lead audit:
- `lake build` passes (8759 jobs). AxiomCheck gives 447/447 entries, all [propext, Classical.choice, Quot.sound],
  with 0 sorryAx and no forbidden tokens.
- The P31-N drafts lean/ChowlaCosine/P31/FourierL2.lean and SincInterpolation.lean are NOT imported or audited, and
  are left uncommitted (agent stopped mid-task by user request).
Statements (lean/ChowlaCosine/Beckner/YoungSharp.lean, YoungSharpSpecial.lean):
- `sharp_young`. For p, q, r ∈ [1, ∞] (ℝ≥0∞) with 1/p + 1/q = 1 + 1/r and f ∈ L^p(ℝ; ℂ), g ∈ L^q(ℝ; ℂ):
  f ∗ g ∈ L^r and ‖f ∗ g‖_r <= A_p A_q A_{r'} ‖f‖_p ‖g‖_q, with A_p = becknerA p = (p^{1/p}/p'^{1/p'})^{1/2}
  (becknerFactor (1/p)). All endpoints are included.
- `sharp_autocorrelation` (M5). For h ∈ L^{4/3}(ℝ; ℂ), the sharp autocorrelation bound with constant
  A_{4/3}⁴ = 4/(3√3) (`becknerFactor_three_quarters_fourth`). Interval-support corollaries:
  `sharp_interval_selfConvolution`, `sharp_interval_autocorrelation`.
- Proof route: heat-flow geometric Brascamp–Lieb → explicit Young frame → planar change of variables →
  duality/domination.
- Correction found by the agent: the constant previously recorded as "0.7698" is a rounding of 4/(3√3) =
  0.7698003589… and is NOT itself a valid exact upper bound. All records now say 4/(3√3) ≈ 0.76980. The thresholds
  derived from it are unchanged at displayed precision.

## C-R7 (2026-10-19) Exact certificates for P58 (T-dense(4.4393)) and its obstruction witness
Archived copies are in examples/r7_certificates/. The originals, runnable from the repo root on the VM, are in
.research/agents/tdense7_scratch/.
- moment_gap.py/json (Fraction arithmetic). C = 44393/10000 with r = 0.769801 (r² > 16/27) and ρ = 0.905646 (ρ > P17's
  (1 + √17)/(4√2)): the quadratic Ca² − (C + 2ρ/r)a + 2/r > 0 for all a, margin 3.3e-6. Also C = 4.213 with r = 0.811,
  margin 1.4e-4.
- algebra.py/json: R7-T's C = 3 contradiction, margin 640985/3409625664.
- envelope_exact.py: the C = 4.164/4.331 Carathéodory–Fejér route (the large JSON output is not archived; regenerate).
- witness.py + witness_B48.json: the 6.0539 obstruction profile (48-cell rational PWL).
  - PD by exact Sturm count (sympy, flint ground types).
  - Both window failures for all θ ∈ (0,1] by exact Bernstein coefficients per cell (r = 3849/5000).
  - The lead re-ran `witness.py certify 48` on the VM (2026-10-19): PD_proved true; every density/energy cell ok.
- point_certificates.json: 192-bit Arb point evaluations f_A(x) + r√n < 0 for the 16 adversarial/realised sets.
  These prove R >= 1.82 for the realised witness sets; they are point certificates, not global minima.

## C-R8 (2026-10-19) Exact certificates for P59 (ρ* <= 0.815276; T-dense(6.156)); archived in examples/r8_certificates/
- potential_g4_d8_exact.json (degree 8) and potential_g4_d4_exact.json (degree 4, fallback ρ = 0.815371): Bernstein
  coefficients of the increasing potential β and the per-region polynomial checks.
- verify.py → independent_verification.json:
  - SymPy (QQ) reconstruction, Sturm root counts 0 on all four intervals, positive endpoints;
  - exact T-dense reach checks: 4(2 − ρ) − (1539/250)r = 261/250000000 > 0 with r = 0.769801;
  - the round-7 witness's energy-PD violation at t = 7/48.
- effective_checks.py/json: exact Fraction comparisons for the explicit c(3) proof (P59.6), plus float sanity checks
  of the Gaussian identities (the float checks are not proofs).
- Lead's independent re-check (E79, src/e79_r8_checks.py): ρx − x² + β(y_min(x)) − β(x)/2 >= 0 on a 2·10⁵-point float
  grid and a 2001-point exact-rational grid (minimum 0 at x = 0), and β' > 0.

## C-R9 (2026-10-19) Exact certificates for P60 (κ <= 0.749089; T-dense(6.9366)); archived in examples/r9_certificates/
- long_gram.py → long_gram_bounds.json: 18 rational supporting lines q(2t) >= m q(t) + b, each with its Chebyshev
  certificate (λ_3..λ_24 >= 0).
- long_scalar_d24_exact.json: κ = 749089/10⁶, a degree-24 increasing β (Bernstein and power forms), 21 branches, 29
  leaves in u = √(1 − x).
- long_verify.py → long_independent_verification.json: the agent's QQ/Sturm/Bernstein checks.
- exact_witness.py → witness_B160_full_factor.json (integer spectral factor; 1/d < 7.267398825422); witness_B40_energy.json.
- cp_obstruction.py/json: the Horn witness (Arb, 160 bits).
- independent_verify.py/json: degree 4/8/12 scalar certificates and the effective-constant comparisons (P60.7).
- packet_probe.py/json: the weighted escape probe.
- manifest.json: hashes and versions.
- Lead's independent re-check: E81 (src/e81_r9_verify.py; exact-rational Taylor models; all pass).
- NOT a certificate: E82's D ≈ 0.11667 (numerical lower bound on D; an upper bound needs a certificate, round 10).

## C-R10 (2026-10-19) Exact certificate for P62 (D <= 1333/10000; T-dense(7.5019)); archived in examples/r10_certificates/
- coupled_td.py → coupled_td_d10_K64_s0.2.json: Gurobi discovery of the 64 kernel values a_j and degree-10 potentials.
- certify_td.py → certificate_td.json:
  - a_j rounded up to 10⁻⁹, plus 1/2000;
  - β_j Bernstein coefficients at denominator 10¹⁰;
  - 128 half-cells of pointwise leaves in u = √(1 − x) (squared form u²(2 − u²)/4 − A² >= 0);
  - 64 exact Schur cubics; minimum Schur margin 18576429767/491520000000000.
- independent_verify.py → independent_verification.json: the agent's QQ/FLINT reconstruction (527 leaves, 127 CF caps,
  64 Schur cells).
- Lead's independent re-check: E84 (src/e84_r10_verify.py; Arb in x plus my own Schur integration). All pass.
- third_direct.py/json and third_probe.py/json: the sparse cubic-gadget probes, with Arb point certificates for the
  failed rounded candidates (R > 2.079, R > 2.081).
## C-R11 (2026-10-19) Exact certificate for P63 (D <= 259/2000; T-dense(7.7220)); archived in examples/r11_certificates/
- support_lines.py → support_lines.json: Gurobi LPs for k = 2..16. Each record stores rational nodes and weights; the
  line is re-derived exactly with the R-repair.
- discover.py → discovery_K192_d12_s0.2_t0_support.json: discovery of a_j and the degree-12 potentials. The K48/K64
  discovery files are also kept.
- certify.py → certificate_td.json:
  - a_j rounded, plus 1/2000;
  - 384 half-cells of leaves in u = √(1 − x);
  - 192 exact Schur cubics.
  - failed_certificate_slack_1e4.json is the failed 1/10000-slack attempt (fails near u = 0.32398 in half-cell 64),
    kept as a record.
- independent_verify.py → independent_verification.json: the agent's QQ/FLINT reconstruction.
- final_check.py → final_checks.json: hashes, binary algebra, Arb point dips of failed roundings, triangular
  repair-energy constants.
- Lead's independent re-check: E85 (src/e85_r11_verify.py → examples/e85/e85_verify.json). All pass.

## 2026-10-20 isolated lens-fiber certificates

The Boolean radial family has two separate rigorous LOWER bounds for M: exact-root Arb point evaluations and a nonnegative product-Fejer measure of exactly unit mean. Strong CRT kernel separation proves zero Fourier aliases, so the second certificate reduces to a finite weighted lens sum. All three finite certificates are rechecked with independent reverse-factor enumeration and 192-bit arithmetic. These do not certify global upper bounds. [Derivation and reproduction](notes/cstar_radial_boolean_2026-10-20.md).

## 2026-10-23: exact finite projection failure and full inverse comparison

[Current statements and proof](notes/P2_phase_projection_2026-10-23.md),
[independent internal review](notes/advisor_P2_coupling_2026-10-23.md).

The Boolean n76,L36 support has all-circle M<=17/2 by two disjoint
Sidon difference-square identities, with raw distinct differences
independently reconstructed. Its finite criterion Psi3>0.9990 is
certified by384-bit ball inverse recurrences; selected convolution
separately checks the inverse-square pairing. The complete inverse
uses a dyadic polynomial of band12672 and exact integer residual
norm, divided by the global inverse margin lambda-17/2. A sparse
Python-integer reconstruction independently checks the FLINT product.
The full H and original determinant are rigorously negative, despite
the false stronger finite-projection inequality.
Retaining ALL negative Fourier coefficients recovers the SAME finite
case with Psi_minus<-.7399 and2Gminus>y, entirely from finite
recurrences. The separate full inverse comparison still validates
the discarded positive-frequency energy. No universal extrapolation.
[All bounds/numerators](experiments/P2_projection_2026-10-23/results.json).

The weighted geometric finite model is certified without quadrature:
exact rational tail bounds enclose the ENTIRE inverse and both parity
matrices. Positive diagonal and determinant lower bounds establish PD.
Its coefficients are not Boolean, so it is a relaxation falsifier.
[Exact certificate](experiments/P2_geometric_2026-10-23/results.json).

These are paper/exact finite certificates, internally audited, not
new Lean/kernel checks or an unrestricted Chowla result.

## 2026-10-23: actual Boolean falsifiers and two full-norm methods

The negative-block strengthening is refuted by A={1,...,8}, with
paper all-circle M<=11/4 and an exact rational reverse gap. Exact
Q(sqrt32) field arithmetic separately corroborates the recurrence
and closed forms. Sturm gives an independent global upper proof.
Original P2 holds, by both an infinite residual certificate and
the independent exact finite reproducing-kernel norm formula.

On the degree87,n56 support,384-bit balls refute both negative-only
and COMPLETE cyclic-allpass sufficient closures. Independent finite
convolution and reversed polynomial products agree. Exact Sturm
rechecks lowM; the earlier full inverse certificate is matched to
the identical frequency set and proves original P2 negative.

[Certificate data](experiments/P2_aggregation_2026-10-23/prefix8.json),
[n56 data](experiments/P2_aggregation_2026-10-23/n56.json),
[complete statements and analytic proof](notes/P2_full_phase_2026-10-23.md),
[independent internal audit](notes/advisor_P2_aggregation_2026-10-23.md).
Neither a sampled minimum nor a finite inverse truncation is being
used as proof of the whole-circle or full inverse claims. No new
kernel check, universal Chowla result or novelty certification.
