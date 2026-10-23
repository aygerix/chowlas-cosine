# Genuine integer sets force a quadratic modulation-convolution loss

2026-10-23. Research proof record, not a manuscript. Full Chowla and the
Epoch construction remain unresolved. The sole advisor independently
checked the complete paper argument and both finite implementations:
[audit and full derivations](advisor_modulated_convolution_2026-10-23.md).
Status: proved on paper using the stated classical discrepancy theorem;
separate exact finite certificates; no new Lean/kernel or novelty claim.

## 1. Exact theorem and scope

For a genuine finite A⊂Z_(>0), let S=±A,
D_A(x)=sum_(s∈S)exp(isx)=2sum_A cos(ax), and K_A=-min_circle D_A=2M(A).
For τ∈S put h_τ(x)=2(1+sin(τx))D_A(x) and G_τ=h_τ*h_τ, with
convolution normalized by dx/(2pi). This is SELF-convolution, not
autocorrelation; its Fourier coefficients are squares, not modulus squares.

THEOREM. For every Q divisible by8 with Q>=10^12, there exists a set
A_Q⊂{1,...,Q-1}, containing t=Q/4, with n_Q=|A_Q| and τ=-t such that

    n_Q=Q/2+O(sqrt(Q)), Q/3<=n_Q<=2Q/3,
    sqrt(Q)/20<=K_Q<=500sqrt(Q),
    G_τ(4pi/Q)<=-Q/25<=-K_Q²/6250000.                 (1)

All constants are absolute. The upper bound on K is over the ENTIRE
circle. Since K→infinity, no uniform replacement of the usual quadratic
floor by -o(K²) is possible, including any C*K^(2-delta),delta>0.

This is a sharpness obstruction to ONE ingredient of the P14/P19 boundary
programme. It is NOT a Chowla counterexample: M(A_Q)/sqrt(n_Q) stays
bounded below by an absolute positive constant. It does not rule out
improvements conditional on n/K²→infinity, and proves no universal
Chowla exponent gain. The proof threshold is not a proposed job size.

## 2. A Boolean identity and the negative expectation

Extend a_s=1_S(s), including a0=0. For positive t,

    (h_t)hat(s)=2a_s+i(a_(s+t)-a_(s-t)).

Using a_s²=a_s gives exactly

    G_t=(4-2cos(tx))*D_A+2F_Et+8 Im F_At,
    E_t=(S+t)∩(S-t), A_t=S∩(S+t),
    F_U=sum_(s∈U)exp(isx).                             (2)

The imaginary part of F_At equals that of F_Bt, B_t=A_t\(-A_t),
because the discarded intersection is symmetric. E_t can include0.

Start with independent Bernoulli X_a of mean1-a/Q for1<=a<Q,
and force X_t=1. The mean D is Fejer_Q-1+(1/2)cos(tx), hence is
everywhere at least-3/2 and equals-3/2 at x0=4pi/Q.

Let p(v)=(1-|v|)_+ and L_s(v)=p(v+s)p(v-s). For s<=1/2 its
even piecewise formula is (1-s)²-v² on0<=v<=s and
(1-v)²-s² on s<=v<=1-s. Integration by parts twice, retaining
the derivative jumps, gives at y=4pi

    Lhat_s(y)=[(4-12s)cos(ys)+12sin(ys)/y]/y²,
    Lhat_(1/4)(4pi)=-1/(16pi²),
    Lhat_(1/8)(4pi)=3/(16pi³).

The E_t product profile uses s1/4. The A_t product profile is shifted
by1/8, whose phase at y4pi is i. Evaluate G_(-t) at POSITIVE x0 so
the odd term of(2) is negative. Thus

    E G_(-t)(x0)=-c0 Q+O(1),
    c0=1/(8pi²)+3/(2pi³)>3/50.                       (3)

For completeness, the Riemann error per lens profile is below28:
TV(L_s exp(i4pi v))<=2+8pi<28. Symmetric duplicate/zero-index and
forcing exceptions cost at most5 for E_t and6 for A_t. Together with
the mean-D contribution the absolute error is at most
9+2(28+5)+8(28+6)=347<400. Therefore

    E G_(-t)(x0)<=-(3/50)Q+400.                       (4)

## 3. Conditional discrepancy rounds the nonlinear statistic

The sole imported discrepancy fact is the REAL square-matrix form:
an m×m matrix with entries of absolute value<=1 has a sign vector
with row discrepancy<=6sqrt(m). It is stated explicitly on PDF page2
of [Larsen2207.03268v2](https://arxiv.org/pdf/2207.03268v2), verified
directly this cycle. The older author-site URL returned404.

The fractional consequence is elementary. Pad any column restriction
of an m-row matrix by zero columns to m×m. For a dyadic p, at denominator
2^k round just odd coordinates by ±2^(-k) with that sign coloring.
Each level costs at most6sqrt(m)/2^k; the sum is at most6sqrt(m).
Integral/forced coordinates remain fixed. Dyadic approximation and a
subsequence of the finitely many final Boolean vectors proves the same
bound for arbitrary p∈[0,1]^N,N<=m. No rectangular or nonlinear
discrepancy theorem is assumed.

At x0, G is a quadratic Boolean observable. Every interacting pair of
positive indices has residues congruent up to sign modulo t. Its generic
components are

    {r+j*t,(t-r)+j*t:j=0,1,2,3}, 1<=r<t/2,

with size8; the exceptional components have size3 or4. Changing a bit
affects at most six squared Fourier coefficients, each of magnitude<=5,
so its effect on G is at most60.

In each of eight stages fix at most one bit per component. Conditional
expectations use original independent probabilities for all remaining
bits and the already-fixed past. The conditional expectation of G is
AFFINE in all current-stage bits, since none interact. Its slopes are
bounded by60. Fourier D-grid slopes are bounded by2.

Apply fractional discrepancy to the16Q grid rows and ONE G row,
normalizing by2 and60, respectively, and pad to m=16Q+1 rows/columns.
The conditional errors telescope over the eight stages:

    max_grid |D_final-E_initial D|<=96sqrt(16Q+1),
    |G_final(x0)-E_initial G(x0)|<=2880sqrt(16Q+1).       (5)

The final bits are dependent. No independence assumption is used after
rounding. This is a bounded-component nonlinear rounding lemma reduced
to ordinary linear discrepancy; the whole Fourier control and the
chosen quadratic observable are maintained simultaneously.

## 4. Entire-circle bounds and explicit constants

Let R=D_final-E_initial D, of degree<Q. Bernstein's derivative
inequality and nearest distance pi/(16Q) to the grid give

    ||R||infinity<=96sqrt(16Q+1)/(1-pi/16)<493sqrt(Q).

Hence actual K<=500sqrt(Q); the grid point0 gives n=Q/2+O(sqrtQ).
Using(4),(5), G_final<=-(3/50)Q+400+11880sqrtQ<=-Q/25 for
Q>=10^12. All frequencies are distinct positive integers belowQ,
and t remains occupied.

Finally h_τ>=-4K and has mean0, so positivity of its shifted convolution
gives

    G_τ+16K²=(h_τ+4K)*(h_τ+4K)>=0.

This forces K>=sqrtQ/20 and proves all assertions in(1).
The sets can be selected effectively by exhaustive finite search:
take the lexicographically first support containing t whose two
finite bounds in(5) hold with an added1 of slack. These predicates
are algebraic (roots of unity and rational initial probabilities),
so exact comparison decides them; the existence proof guarantees
termination. The added1 fits the strict margins in(1) at the stated
threshold. No practical Spencer implementation,
Epoch solution function, or vanishing-ratio algorithm is claimed.

## 5. One finite pilot and genuinely independent certificate arguments

The single fixed Bernoulli pilot Q65536,seed20261023, contains32787
frequencies and forces t16384. It does NOT implement the asymptotic
Spencer-selected family. Its own exact/ball certificates give

    G_-t(4pi/Q)=-4323.555399930924...,
    M(A)<421.404 by ball DFT plus minimizer Taylor remainder,
    M(A)<=75623/180<420.128 by a separate mean/noise Bernstein argument.

The point is independently checked using squared integer Fourier
coefficients, exact set-intersection identity(2), and a ball DFT with
an explicit sign-convention control. The two all-circle upper arguments
use the same Arb backend but different polynomials and remainder proofs.
Exact rational intervals, frequencies and seeds are authoritative.
The pilot certificates do not establish a refutation of the specific
16K constant; the asymptotic paper theorem refutes every fixed linear
constant. A false certification flag is not proof of the opposite bound.

[Producer](../../src/modulated_triangle.py),
[independent verifier](../../src/modulated_triangle_verify.py),
[pilot data](../experiments/modulated_triangle_2026-10-23/pilot.json),
[verification](../experiments/modulated_triangle_2026-10-23/verification.json).

## 6. What changed and the required next pivot

The immediately preceding covariance attempt produced no new Boolean
bound: its full matrix is exactly the finite Schur multiplier cap, and
its two proposed signed-vector tests have a growing Boolean prefix
relaxation counterexample. [Complete covariance audit](advisor_full_covariance_2026-10-23.md).
Stop polishing that representation without a new unit-amplitude idea.

P19's old PropositionC had finite interval-certified examples and a
HEURISTIC asymptotic explanation. Finite examples alone did not prove
the uniform no-o(K²) conclusion. The present theorem establishes that
conclusion by a different genuine integer family; it does not establish
an asymptotic constant for the original Singer examples. Membership of
their displayed t values is not used here; our t is explicitly forced.

Stop the global linear/subquadratic modulation-floor target. The theorem
does NOT close P14's separate Q2/truncation issue or refute improvements
restricted to genuinely spiky n/K²→infinity. Future progress through
that route must retain actual degree-one positivity and joint boundary
information, rather than optimize this already sharp loss.

First next derivation: return to P14's EXISTING joint non-saturation
question in the spiky regime. Keep the t-sum before estimating the
boundary functions; start with the exact five-linear expression for
sum_(t∈S)|F_(S∩(S+t))(x)|², then retain the B_t projection and pure-
positive remainders. A possible averaged gain must include the old K⁴
additive scale and must use the integer circle; P20 finite-group models
are adversaries. No such conditional gain is proved here, and naming
it is not a new route. Keep unrestricted signed Boolean coupling,
mixed/scalar-factor coefficient control and genuine growing construction
ideas as three distinct lines. All own jobs terminal/PASS, no GPU,
no VM lifecycle operations; shared Dirichlet remains on, conservative
RunPod total$0.10. No universal exponent improvement or full resolution.
