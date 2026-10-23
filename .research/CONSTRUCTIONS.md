# Constructions (parametric families)

## 2026-10-23 — growing signed-mass obstructions, not Chowla counterexamples

Elementary explicit family: for even m>=2000 use balanced-parity
power9 Sidon sets of sizes2m and m; take their positive differences
A0,A1, D0=max A0 and A=A0 union(2D0+1)A1. Then
n=(5m^2-3m)/2, actual M=3m/2<=sqrt(n), R tends3/sqrt10,
gcd A=1, and EVERY optimal real factor has N/Q(1)>1/64.
The minimum and all-factor assertion are separate exact paper proofs.

Three-color upgrade: choose a known Bu half-constant base U of
sufficiently large size t with M(U)<=11sqrt(t)/20, t>=20000.
Set L=2max U+1 and A=U union LU union L^2U. Then n=3t,
M(A)<=33sqrt(t)/20<sqrt(3t), and the finite graph theorem forces
N/Q(1)>1/8 for EVERY optimal real factor. Gcd normalization makes
the family primitive if necessary. The cited Bu theorem is an
explicit dependency; its asymptotic threshold is not computed here.
Only a known limsup ratio<=sqrt3/2, not an exact or vanishing
asymptotic ratio, is inferred from this construction-side argument.

This refutes old universal stable-factor existence through its mass
budget; it does not disprove Chowla or provide an Epoch generator.
[Full formulas, graph proofs and scope](notes/signed_translation_2026-10-23.md),
[independent advisor audit](notes/advisor_cp_translation_2026-10-23.md).
Research paused at the user's checkpoint request.

## 2026-10-23 — continuum countermodel is not an integer construction

W=(1-|t|)_+, v=W^2/4, p=phi(v) gives an explicit admissible
model for the current cubic/Gabor profile relaxation, with density
1/2-sqrt(3)/8-pi/12>3/140. No finite Boolean realization with
small M is constructed. This is a scope result for the relaxation,
not an Epoch algorithm or a family with M/sqrt(n) tending to zero.
[Full proof and precise exclusions](notes/cubic_two_scale_and_profile_barrier_2026-10-23.md).

The CP-vector satellite example in the advisor note is also an
obstruction to a proposed estimate, not a new small-ratio family:
for even k>=8, take B_i=2*9^i+epsilon_i, 0<=i<k, with exactly
k/2 epsilon_i equal to 1. Let A0 be its distinct positive differences,
D=max A0, and append an odd L>2D. Then n=k(k-1)/2+1 and
M(A0 union {L})=k/2+1 EXACTLY, attained at pi. Equality of two
perturbed differences first reduces modulo16 to equality of the
power differences, then 9-adic valuations identify the pair.
F_B(pi)=0 proves the minimum via the exact difference square.
Thus the normalized ratio tends to 1/sqrt(2), rather than zero.

For EVERY optimal nonnegative square decomposition, each component
containing lag L has exactly two balanced endpoints; together these
contribute centroid numerator L^2/2 and denominator L^2/4. Low
components contribute at most n0*D^2/2 to either quantity. Hence
L/(kD) tending to infinity forces the proposed global variance ratio
to 2 uniformly over all optimal CP decompositions. This defeats a
universal square-root lower bound for that ratio, not CP-Chowla.
The all-k and all-circle statements are independently checked paper
proofs; no new numerical minimum or kernel certification is claimed.
Keep the genuine construction track separate. Previously
closed Paley DC deletion and nested residue schedules are not
reactivated by suggesting an unspecified recursive repair.
[Finite CP identities and scope](notes/advisor_cp_vector_2026-10-23.md).

## 2026-10-23 — integer obstruction to linear-K endpoint energy

An OBSTRUCTION family, not a vanishing-ratio construction. For every
integerQ>=2^21, independently selectingj<Q withprobability1-j/Q
and forcingQ yields a positive-probability genuineA⊂[1,Q] with
H_Q>=Q²/80 and actualK=2M<=4+sqrt(2Qlog(128Q²)). Thus
H_Q/(K|B_Q|)→infinity; no universal linear-K energy estimate exists.
The expectation constant43/1260 and explicit bounded-difference/
whole-circle derivative bounds prove existence. No sampler claiming
guaranteed output, Epoch solution, or effective asymptotic selection
is implemented. One modified saved pilot separately certifies ratio>15.

The admissibility repair S_O4 union{±t} keeps P22's group boundary
and actualK unchanged; its exact middle energy obstructs a generic
quadratic-K estimate. This is a consequence of an EXISTING finite-
group construction; it has no demonstrated all-circle integer lift.
[Full statements and limitations](notes/ordered_boundary_2026-10-23.md).

## 2026-10-23 — bounded-ratio integer family forcing quadratic convolution loss

This is an OBSTRUCTION family, not a candidate vanishing-ratio family.
For every integer Qdiv8,Q>=10^12, eight conditional Spencer stages
give distinct positive A_Q⊂[1,Q-1], n=Q/2+O(sqrtQ), containingQ/4.
ActualK=2M lies in[sqrtQ/20,500sqrtQ], while for τ=-Q/4,
h_τ=2(1+sin τx)D_A has(h_τ*h_τ)(4pi/Q)<=-K²/6250000.
Convolution is probability Haar. Thus M/sqrt n has a positive
lower bound; this family does not meet Epoch's quantified target.

Selection rule: start with p_a=1-a/Q, forcep_(Q/4)=1. At each of
eight component stages choose a Boolean rounding satisfying the
finite16Q Fourier-grid and conditional-observable row bounds from
the proof. Existence follows from square padding/dyadic Spencer.
Equivalently choose the lexicographically first full support meeting
the two bounds(5) of the proof with an added1 of slack. Exhaustive
search with exact algebraic comparison is an
effective finite selection rule; no practical implementation of this
astronomical-threshold asymptotic algorithm is claimed.

[Full parameter map and proof](notes/modulated_triangle_2026-10-23.md).
The saved Q65536 Bernoulli pilot in src/modulated_triangle.py is a
SEPARATE finite mechanism check and has its own two all-circle bounds.
Do not label it a Spencer-selected output or infer the theorem from it.

2026-10-23 full-coefficient gate: a SINGLE exact real polynomial
power P_lambda=H^q is completely classified. Onlyq2 survives,
with A={d},lambda1 or A={d,2d},lambda9/8. No coefficient-sign
or rationality assumption on H is needed; the all-degree proof
uses p-adic dominance of the exact outer bits. Thus no growing
construction exists in this architecture. General complex squares,
multiple squares and nonconstant corrections remain outside.
[Proof and certified finite corroboration](notes/boolean_power_rigidity_2026-10-23.md).

Mixed correction remains materially different: U=1+((1+r²)/2)w+w²,
V=r(1-w) gives exact A12 outer bits and lambda9/8+5r²/4+r4/8.
This fixed-size nonoptimal family is only a cancellation check,
not a promising asymptotic construction. A useful next result
must increase cardinality with a certified smaller ratio or prove
a quantitative arbitrary-support mixed-coefficient constraint.

2026-10-23: all-class l1 rounding of a high-multiplicity complex
square is now excluded by a general paper theorem. For every k-point
real B, E_r=sum_nonzero|r_d-r|>=((r-2)k+2r)/6. Thus the proposed
growing-r error o(k sqrt r) is impossible, and the displayed
square/l1 upper certificate is strictly above1/2 in every finite
case r>=2. [Proof and scope](notes/multiplicity_centroid_2026-10-23.md).
The one changed count pilot failed before this proof explained it;
no enlargement or GPU. This does not bound actual M from below or
close the earlier P23 route which discards weak classes, signed
correction near factor zeros, or general weighted/signed factors.

Weighted continuation: one positive-real factor lambda+f_A=|Q|²
satisfies lambda-1/2>=sqrt(lambda+n)/(4qmax). It gives certificate
energy restrictions but no general representation theorem. The
precise next weight/phase gap is in
[the weighted note](notes/weighted_centroid_2026-10-23.md).

2026-10-20 deterministic upgrade: the full p-point cyclic-Sidon fiber architecture at primitive ||u||<=sqrt(X) has M>=sqrt(n)/16 eventually for EVERY deterministic assignment under kernel gap>3X. No actual marginal/independence law remains. Dense windowed intersections with Fourier norm<=Bp^delta, any fixed delta<1/2, also have a positive square-root lower bound after adaptive window/cardinality matching. Stop treating sharp conditional Cp^3 or correlations alone as an escape in these classes. The spectral endpoint and arbitrary supports remain open. [Proof and concrete partial/windowed certificates](notes/cstar_sidon_deterministic_2026-10-20.md).

2026-10-20 Sidon-fiber update: primitive ||u||<=U, lifted affine-parabola differences give a genuine Boolean family n=Theta(X^2 log U), each left fiber M<=p_u/2, and a uniform ensemble with M(mean)=O(U^2). At U=X^(1/4), a nonlinear mixed-certificate paper theorem forces Pr[M>=sqrt(n)/5]>=1/6 for ANY coupling with these whole-fiber marginals. Thus a small mean does not give a guaranteed counteralgorithm. Arbitrary deterministic parameter choices remain outside that probability theorem; a precise conditional reference-cubic bound would exclude them within this architecture. [Construction, exact mean, theorem and checks](notes/cstar_sidon_mixed_2026-10-20.md).

2026-10-20 update: the truncated integer cone under the stated phase-rich CRT encoding is now excluded for **arbitrary** selections, including nonuniform/correlated/non-lens ones: ||u||>=sqrt(X), n/X^2->infinity implies M>=n/(32X) and R->infinity. Nonuniform center laws do repair the previous uniform-marginal parity obstruction, but not this deterministic residue average. Discontinue its logarithmic-gain counterexample strategy. No arbitrary-encoding or unrestricted Chowla statement follows. [Proof, finite witnesses and exact scope](notes/cstar_wide_parity_2026-10-20.md).

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
