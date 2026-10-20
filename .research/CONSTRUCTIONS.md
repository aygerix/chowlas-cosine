# Constructions (parametric families)

| family | N | M bound | R limit | status |
|---|---|---|---|---|
| Sidon differences (B Sidon, k) | k(k-1)/2 | k/2 (exact identity) | 1/sqrt2 | proved |
| Bu et al. two-sided Sidon | k(k-1) | k/2 + O(sqrt(k log k)) | 1/2 | cited (asymptotic) |
| A_{k-1} root square, A4={s_i+s_j-s_k-s_l} | ~k^4/8 | ~k^2/4 (completing square) | 1/sqrt2 | derived here, heuristic |
| Wick degree-4, A4={±a_i±a_j±a_k±a_l}=8 e_4(cos a x) | 8C(k,4) | Gaussian heuristic | 0.866 | heuristic |
| Cube framework P7 | sum 2^{|S|-1} | -(1/2) min_eps g_J | R_cube(J) | rigorous template; search EXP-1 |

## Dense near-interval family (2026-10-18; numerical mechanism, no parametric theorem)
A = [1, L] \ H ∪ T: interval with a few holes H and a sparse tail T near t ≈ 2π/x1 (x1 ≈ 4.49/L, first Dirichlet lobe).
Best certified: N=20 (R <= 0.6011), N=34 (R <= 0.6043). R increases with N under SA (0.64 at N=54, 0.69 at N=122);
heuristic explanation (NOTEBOOK 2026-10-18): the positive-definiteness tolerance of the macroscopic profile is ~c/√L,
loose at small L. No infinite family; not a candidate for R -> 0.

## Status of the Bu family after P16 (2026-10-18)
Bu et al. (2610.17160): A(S) = {3|s−t|} ∪ {|3(s+t)+1|}, S Sidon, N = k(k−1), R -> 1/2 from above (excess ≈ 1.0–1.4√k in
our reproductions). P15: f_{A(S)} = P^2 − k/2 − C/2 with P(x) = C(x/2), C = Σcos((6s+1)x). P16: R(A(S)) >= 1/2 − O((L/k^3)^{1/6})
for every Sidon S ⊂ [−L,L], and for all dilate/shift variants A_{q,r}. So the family is EXHAUSTED at constant 1/2: no
choice of Sidon set, dilation or shift helps. Beating 1/2 needs a different algebraic template (not a single real square
minus a concentrated diagonal); unions of several squares need 2-D (or r-D) visits to fail, i.e. lower-flat vectors of
Sidon-type cosine sums — the same missing lemma as SNZ (STATE line 1).
## Dense family status (E14, E16–E18)
Best certified finite R = 0.56481 (N=36). Theory (E16): ρ <= ρ* ≈ 0.7239 for doubly-positive profiles; unless rounding
errors are positively skewed the dense limit is >~ 0.5255. LNS/SA data rise with N past 36.

## Bu step as a map; the bi-flat target (2026-10-19; NOTEBOOK "Construction track")
- Dilation pinch (PROVED): |A ∩ qZ| >= n/q − (1 − 1/q)M. One dilation level gains at most √q in R. Bu: √2 at q = 3.
- Map. If D admits a BI-FLAT factor V (autocorrelation 0/1 off 0, autoconvolution 0/2, up to junk), then
  A = 3D ∪ (3Σ + 1) has R(A)² = R(D)²/(1.5 + R(D)²) + (junk). Iterating gives R -> 0.
  - Only known bi-flat family: unimodular Sidon (Bu, R -> ½).
  - Any bi-flat V with R(D) < 1/√2 beats ½. Multiplicity >= 2 is necessary; exact versions are impossible in Z, so it
    must be approximate.
- Status: OPEN target. No candidate yet.

## One-Bu-step class A = 3D ∪ E with D fixed (2026-10-19 night; NOTEBOOK T1–T10; E64, E65)
- Geometry. Z(x) = e^{ix}W(3x) must lie in the equilateral triangle of inradius P(x) = f_D(3x) + M.
- Ceilings:
  - pinch λ <= 2 + 2M/|D|;
  - phase-blind λ <= R(D)² + ½, attained iff W = V² with V bi-flat; for Sidon D this is Bu;
  - for general q: pinch λ <= q − 1, phase-blind λ <= (1 + 2R²)/(q − 1);
  - q = 2 is pinned at λ <= 1 + M/|D|, attained by "Bu-q2" 2D ∪ {2(s + s') + 1}.
- Beating ½ from Sidon D needs a gain f > 8ε in λ at slack εk. Generic extras give f <= 2ε² (T10, heuristic).
- Exact optima (E64):
  - dense optimal D admit no E at slack <= 5% (rigid: W must vanish at every near-minimiser);
  - Sidon D at small k beat Bu at equal k by central-spike vertex locking (R(A)/R_Bu = 0.80–0.94 for k = 6–8);
  - the larger-k trend (k = 9–24) is pending.
- Status: OPEN, under test. If R_opt/R_Bu -> 1, the class is exhausted at ½, as predicted.

## Boolean radial lens-shell family (2026-10-20)

Exact rational Halton centers on dyadic primitive-u shells realize the disk-autocorrelation fractional profile with genuine zero/one rank-one matrices, n~(3pi/32)X^2 log X and a nonnegative limit at EVERY fixed matrix phase. FAILED as a counterexample under the stated h=6X^3+(1,3,5,7) CRT encoding: positive Fejer isolation proves M>=X^(3/2)/2^36 for L>=64. Three finite sets are independently reconstructed and certified, with point R lower bounds>6.4201,10.6327,18.6951. The construction is retained as a countercontrol to inferring global sign from a good macroscopic profile. Within-shell center correlations and other encodings are not excluded. [Generator, exact membership, proofs and checks](notes/cstar_radial_boolean_2026-10-20.md).

## Small-fiber independent centers and correlated repairs (2026-10-20)

Removing all large fibers gives a new independent-center model with n~(3/32)X^2 log X, variance~cX^3 at a mean-transform zero and a paper CLT; a stronger theorem shows its prescribed mean has sharp negative budget m/2. Same-marginal dependence, thinning and bounded radius staggering retain a growing-phase mean hole in the stated scale gap. Finite center optimizations repair listed phases but have separate certified negative points. A mod5 full/empty assignment repairs the entire limiting zero circle at the same cardinality, changes the marginals and fails linearly at t=5. No all-angle upper bound or counterexample found. [Exact hypotheses, sampler tradeoff, proofs and saved choices](notes/cstar_fiber_centers_2026-10-20.md).
