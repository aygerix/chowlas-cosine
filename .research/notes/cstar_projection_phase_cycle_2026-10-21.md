# Phase audit, Boolean construction projection, and the odd reciprocal

Status: paper identities and certified finite results; full Chowla OPEN.
All circle integrals below use normalized Haar measure. Let
F=sum_(a in A)z^a, f=Re F, D=2f, n=|A|, and lambda=2sqrt(n).
The proof track assumes ACTUAL M(A)<=sqrt(n); the construction track
certifies its own all-circle upper bounds. No GPU deployment or spend.

## 1. The phase-Hessian surrogate is exactly minimum modulus

For W=lambda+F, H an arbitrary real-coefficient analytic polynomial
with H(0)=0, and q=Im(H/W), the normalized quotient

    integral |W|q² / integral q²

has infimum min_circle|W|. Indeed H=W P permits every finite sine
polynomial q=Im P; odd paired localization reaches every minimum,
including endpoint minima by a limit. The external review and the
internal advisor independently found the same reduction. Retire its
interpretation as a new direct-Rayleigh mechanism. The exact identity

    integral Dq² = 2integral |W|q² - 2lambda integral q²
                   - 2integral (|W|-Re W)q²

remains correct. Keeping the last term allows the full odd Rayleigh
problem, whose infimum is -2M; it does not itself prove a Boolean bound.

The [advisor's complete proof](advisor_phase_modulus_2026-10-21.md)
also derives a useful quantitative comparison. With m=min|W|,

    ||f||1 <= 2(lambda-m²/lambda)
              +(m/lambda)*sqrt((lambda²-m²)/2).

To prove this, P=W-m²/W has nonnegative real part and constant
b=lambda-m²/lambda. Decompose
f=Re(P-b)+m²Re(1/W-1/lambda), bound the first L1 norm by2b,
and use the mean-zero analytic L2 identity on the second. Thus
qualitative root-scale L1 flatness implies a root-scale modulus dip,
which implies a root-scale negative cosine minimum. No converse from
Chowla alone, or Boolean counterexample to a modulus bound, is claimed.

For p_y=1/(lambda+F-iy), averaging (Re p_y)² or (Im p_y)² over y
returns pi/[2(lambda+f)] pointwise. The associated averaged Rayleigh
quotient is -2(lambda-1/I), I=integral1/(lambda+f), the known real
resolvent leverage. The real constant in Re p_y must be retained.
The phase average supplies no new Boolean estimate.

## 2. A changed independent construction mechanism, tested and stopped

The CPU pilot allows arbitrary final supports in [1,X]. It alternates
two exact Euclidean projections on an even sample grid G>2X:

* P_pos(v)=max(v,-9sqrt(n)/20), pointwise.
* P_bool(v): select the n largest REAL Fourier scores at1..X,
  set those positive half-spectrum entries to1/2, and set all others
  including DC to zero.

The distance formula
||v-f_A||²=||v||²+n/2-2sum_(a in A)Re(vhat_a)
proves the second projection is nearest among all cardinality-n sets.
The Douglas--Rachford step is
v <- v+P_bool(2P_pos(v)-v)-P_pos(v). The latent vector may be signed;
it is not a bounded-mean nonnegative-reference residual. No nonconvex
convergence, discrete feasibility, or all-circle feasibility is assumed.

Two Singer/Bu seeds (p=7,17) initialize n=56,306; three other replicas
use a fractional Fejer profile with two deterministic perturbations.
Four replicas, at most2000 iterations, seeds20261028 and20261107.
The initial Fejer profile has mass nX/(X+1), not n; every Boolean
projection has EXACT cardinality n. Final supports can leave the seed
architecture and did exchange29 and167 frequencies respectively.

| n | Ambient X | Actual final max A | Certified M/sqrt(n) interval |
|---:|---:|---:|---|
|56|165|87|[0.6413534850845988,0.6422769733733848]|
|306|915|743|[0.6503943481370947,0.6506951223043251]|

Displayed decimals summarize the saved rational/Arb bounds. Both outputs
strictly improve their PARTICULAR unoptimized seeds, and both are
provably above1/2. They miss the9/20 target. These are not records,
an asymptotic family, or evidence that the half constant can be beaten.
The stated GPU go/no-go condition fails; discontinue this pilot rather
than expand its replica count or buy GPU throughput.

All-circle upper certification uses an Arb DFT of every grid value,
plus the rational remainder242sum a²/(49G²). At a true minimizer,
f'=0 and |f''|<=sum a², so the nearest grid Taylor bound gives error
pi²sum a²/(2G²), smaller than the saved rational remainder. A separate
high-precision cosine point gives a lower bound on M. The verifier
independently checks point bounds, exact cardinality and seed gains;
for n56 it additionally proves the upper bound by exact Chebyshev/Sturm
positivity (chain length88). The n306 upper remains the producer's
Arb all-grid/Taylor certificate, not an independent Sturm result.

## 3. The exceptional zero-carrier odd reciprocal: exact test

Put p=1/W and S=integral|p|². For a POSITIVE carrier z^b p,
q=Re(z^b p) or Im(z^b p) has Q=S/2 and normalized amplitude<=2sqrt2.
Any root-scale negative quotient from such an individual seed forces
qualitative L1 flatness. For a sufficiently high carrier its norm gap
g=lambda²S-1 is equivalent to flatness up to constants; do not rename
this existing gap. The advisor also gives an admissible low-M Boolean
control with a negative low-carrier correction coefficient, but adaptive
real/imaginary selection takes its absolute value and is not refuted.

At ZERO carrier q=Im p, the denominator changes:

    Q0=(S-lambda^(-2))/2,
    H0=integral Dq²=1/lambda-lambda*S-T0/2,
    T0=sum_(a in A)[z^a]p².

The normalized amplitude bound is now only2sqrt2/sqrt(g), which may
diverge. Thus the positive-carrier retirement argument does not cover
this seed. Its correction is negative, T0<0: if
B(lambda)=sum_(a in A)[z^a]p, Fourier orthogonality gives

    B(lambda)=-2integral (Im F)²/|W|²,
    B'(lambda)=4integral (lambda+f)(Im F)²/|W|⁴>0,
    T0=-B'(lambda)<0.

Consequently the correction -T0/2 is POSITIVE. Its size relative to
-2lambda Q0 cannot be discarded in a proposed negative witness.

Test only the two already certified projection outputs, at the original
lambda=2sqrt(n). FFT proposes a dyadic analytic polynomial P_B, B=8max A.
This proposal is certified by its exact polynomial residual r=W P_B-1:

    ||p-P_B||2 <= ||r||2/(lambda-M_upper) = epsilon.

The residual coefficients are (U_j+lambda V_j)/T for exact integers
U,V and T=2^64; hence its squared norm is evaluated from exact sums
sum U²+4n sum V²+2lambda sum UV. With S_P=||P_B||²,

    |S-S_P| <= 2sqrt(S_P)epsilon+epsilon²,
    |T0-sum_A[z^a]P_B²|
      <=sqrt(n)epsilon*(1/(lambda-M_upper)+sum_j|P_B,j|).

These are full reciprocal-function enclosures, not sampled quadrature.
Exact finite sine vectors Im P_B are also saved and their energies
checked by independent selected correlation sums. A second verifier
rebuilds the residual by sparse integer shifts and computes T0 directly
using the analytic inverse recurrence at768-bit Arb precision.

The resulting H0/(Q0 sqrt(n)) intervals are near
-0.360 for n56 and -0.302 for n306;
the rational endpoints in results.json are authoritative. Both are
negative finite witnesses, and neither proves a universal sign or
square-root rate. The [completed advisor sign audit](advisor_zero_carrier_2026-10-21.md)
is recorded below; success on these inputs is not permission for a sweep.

One subsequent adversarial test was approved by the advisor because it
changes the stress mechanism rather than enlarging that family: the
SAVED n337 support with fully occupied prefix1..243, actual max587 and
an existing all-circle M upper below sqrt337. This is the same support
that falsifies pointwise analytic-root coupling; its large coherent
prefix specifically tests whether the positive reciprocal correction
overturns the negative term. At band4696 its full normalized quotient
is certified between

    -10036793251590557697/18446744073709551616
    and -10021080754422099967/18446744073709551616,

approximately-.544. It remains negative and supplies no sign falsifier.
The separate sparse-residual/formal-inverse verifier PASSes this case
as well. Stop this adversarial test; no size or parameter enlargement.
Data: zero_reciprocal_2026-10-21/{prefix,prefix_verification}.json.

The advisor's sign audit isolates the exact missing orientation. Put
g=lambda²S-1 and tau=-lambda*T0/(2g). Then

    H0/Q0=2lambda*(tau-1).

The actual lowM premise yields tau>=1-M/lambda>=1/2. A negative
quotient requires an UPPER bound tau<1, which is not proved. In
particular, T0<0 alone has the wrong implication to certify negativity.
For the fixed prefix {1,2}, a hand calculation gives

    H0=(lambda²-11lambda+6)/(2lambda⁴(lambda+2)(lambda-1)),

positive at sufficiently large lambda. This does not refute the proposed
lambda=2sqrt(n) bound: arbitrary enlargement of lambda changes the
statement. Separated Sidon padding also does not transfer this prefix
energy, because S and unshifted T0 retain pure high-block contributions.
No admissible Boolean sign falsifier or universal sign bound was found.

There is an elementary sufficient LARGE-gap branch. Under lowM,
zeta=F/W is Schur and ||zeta||²=g. Since
T0=lambda^-2 sum_A[z^a](zeta²-2zeta), Cauchy and
||zeta²||2<=||zeta||2 give |T0|<=3sqrt(g)/(2lambda), hence

    H0/Q0<=-2lambda*(1-3/(4sqrt(g))).

This is negative for g>9/16 and has root scale if g stays above that
threshold by an absolute margin. It is a high-gap sufficient subcase,
not a new universal estimate; high-gap information already implies
qualitative flatness. The unresolved case is small g.

For a falsifiable next statement, record PROVISIONAL R0: for EVERY
nonempty finite Boolean A with M<=sqrt(n), at the FIXED lambda=2sqrt(n),

    tau<=1-1/400, equivalently H0/Q0<=-sqrt(n)/100.

If proved, this would imply M>=sqrt(n)/200, and M>sqrt(n) already
satisfies that conclusion. The constant is a candidate target only;
three successful tests provide no universal evidence or license to
assume it. A small-g Boolean upper estimate on tau, or an admissible
counterexample to R0 followed by a pivot, is the next discriminating
task. Arbitrarily increasing lambda or weighted coefficient escapes
do not test this exact Boolean statement.

## 4. Artifacts, review and decision

Reproduce on Dirichlet:

    src/dirun.sh -c 2 -m 6 -t 180 python src/cstar_boolean_projection.py
    src/dirun.sh -c 2 -m 6 -t 180 python src/cstar_boolean_projection_verify.py
    src/dirun.sh -c 2 -m 6 -t 150 python src/cstar_zero_reciprocal.py
    src/dirun.sh -c 2 -m 6 -t 150 python src/cstar_zero_reciprocal_verify.py
    src/dirun.sh -c 2 -m 6 -t 150 python src/cstar_zero_reciprocal.py --prefix
    src/dirun.sh -c 2 -m 6 -t 150 python src/cstar_zero_reciprocal_verify.py --prefix

Data: experiments/boolean_projection_2026-10-21/{results,verification}.json
and experiments/zero_reciprocal_2026-10-21/{results,verification}.json.
All final jobs terminal/PASS. The first reciprocal producer run stopped
at an outward-rounding assertion: one denominator step did not cover
float ulp error. It was corrected to an explicitly checked8-ulp rational
padding before the successful run. The failed run established no bound.

GLOBAL REVIEW: unrestricted phase optimization and phase averaging reduce
to existing gaps; stop treating their extra parameters as progress.
The independent construction projection changed the mechanism and was
tested with all-circle certificates, but supplied no half-constant
improvement; no GPU follow-up. Zero-carrier reciprocity remains a specific
unresolved Boolean seed after two construction tests and one distinct
coherent-prefix stress test, with no universal conclusion. Next work
must produce an actual Boolean sign/cost
estimate or a counterexample/pivot, rather than add successful controls.
Full Chowla, L25, OP140 and a vanishing-ratio construction remain OPEN.
The user subsequently PAUSED the campaign; all jobs and advisor tasks
are complete. This checkpoint preserves the next derivation for a later
explicit resume.
