# Exponential continuation: fixed temperature is the old flatness gap

2026-10-23. Internal AI advisor, paper derivations only. Only this
assigned note is edited. No computation, VM operation, GPU, additional
agent or outreach. Shared Dirichlet remains on. No Lean/kernel-checked
proof or externally scrutinized result is claimed.

## 1. Exact quantitative equivalence at fixed scaled temperature

Let A be a finite nonempty set of distinct positive integers,
n=|A|, F=sum_A z^a, f=Re F, M=-min f. Assume ACTUAL M<=sqrt(n).
All averages are probability Haar averages. Define

    Y=f/sqrt(n), L=<|Y|>, mu=<Y_+>=<Y_->=L/2,
    Z_A(s)=||exp(-sF)||2²=<exp(-2sf)>,
    W_A(tau)=Z_A(tau/(2sqrt(n)))=<exp(-tau*Y)>.

Then Y>=-1 and <Y>=0. For EVERY tau>0,

    tau²*L²/8 <= W_A(tau)-1 <= (exp(tau)-1)*L/2.   (1)

Proof. Let psi(v)=exp(-v)-1+v. Mean zero gives
W-1=<psi(tau*Y)>. For u=Y_- in[0,1],

    psi(-tau*u)>=tau²*u²/2,
    psi(-tau*u)<=u*(exp(tau)-1-tau).

The second inequality is the convex secant bound between0 and1.
For Y>=0, psi(tau*Y)<=tau*Y. The upper bound in (1) follows by
adding the positive and negative contributions. For the lower bound,
<u²>>=<u>²=mu² suffices. No Booleanity was used in this equivalence.

In particular at the proposed temperature s=1/(2sqrt(n)), tau=1,

    L²/8 <= Z_A(1/(2sqrt(n)))-1 <= (e-1)*L/2.       (2)

Thus a uniform gap1+epsilon is EXACTLY qualitative low-M L1 flatness,
up to constants. A flatness bound ||f||1>=delta*sqrt(n) gives gap
epsilon=delta²/8. A gap epsilon gives
||f||1>=2epsilon*sqrt(n)/(e-1). This is the existing L25-type gap,
not a new consequence of allowing all Taylor coefficients.

The same conclusion holds if a gap is sought at ANY one of finitely
many bounded scaled temperatures, or at some tau<=T with T absolute:
the upper bound in (1) still forces a uniform L1 lower bound. A growing
temperature range is needed to permit a mechanism that does not
already require flatness. At growing tau, merely W>=1+epsilon is
insufficient for Chowla; the target must be log W>=c*tau.

No Boolean counterfamily to (2), and no new unit-coefficient flatness
inequality, was found. It would be incorrect to call the Boolean
fixed-temperature assertion false just because its weighted relaxation
fails.

## 2. Where a scalar moment attempt stops

Booleanity supplies <Y²>=1/2 and Y<=sqrt(n). These alone give only
the elementary normalization bound

    W_A(1)-1>=1/[4*(1+sqrt(n))].                    (3)

Indeed psi(y)>=y²/[2*(1+y_+)]. For y>=0 the difference after
multiplication by2(1+y) has derivative2y(1-exp(-y))>=0; for y<0
use psi(y)>=y²/2. Bound the denominator by2(1+sqrt(n)) and average.

This is not a new root-scale result or a genuinely coefficientwise
estimate: the argument retains only variance and an upper amplitude.
The normalized initial curvature W''(0)=1/2 (equivalently
Z_A''(0)=2n) does not produce a constant gap. The weighted examples
below preserve that curvature after energy calibration and still
have a vanishing fixed-temperature gap. The missing use of
1_A(a)²=1_A(a) cannot be replaced by its scalar norm identity alone.

## 3. Paper checks of the requested adversaries

### 3.1 Ordinary weighted Fejer: fixed-temperature relaxation is false

Use the conventions

    K_L=(1/L)*|sum_(j=0)^(L-1)z^j|²,
    G_L=sum_(j=1)^(L-1)(1-j/L)*z^j,
    2Re G_L=K_L-1.

The taper V_N=G_(N+1) has N occupied positive frequencies,
coefficients in(0,1), M<=1/2 and ||Re V_N||1<=1. Hence (1) gives

    0<W_N(1)-1<=(e-1)/(2sqrt(N)) ->0.

This is a WEIGHTED relaxation only. Its coefficient square sum is
N*(2N+1)/[6*(N+1)], not N.

Even exact variance/support-count calibration alone does not repair
it. Put a_N=sqrt(6*(N+1)/(2N+1)) and replace V_N by a_N*V_N.
It then has N occupied frequencies and analytic L2 square exactly N,
so <Y²>=1/2 just as in the Boolean problem. Yet M<=a_N/2<1 for
N>=2 and ||f||1<=a_N<2, so its fixed-temperature gap still tends
to zero. Some coefficients exceed1; it is not Boolean. Its maximum
real value is still <=N. Thus scalar variance, support count and
an O(N) positive-amplitude bound do not isolate unit coefficients.

### 3.2 A weighted ROOT-SCALE dip with no flatness

A sharper diagnostic separates fixed temperature from the actual
root-dip conclusion, rather than merely exhibiting small M. Let

    V_N=G_(N²)-G_N, n=N²-1, N>=2.

Every occupied coefficient is strictly between0 and1 and every
frequency1,...,N²-1 is occupied. Its real part is

    f_N=(K_(N²)-K_N)/2,
    ||f_N||1<=1, M_N<=N/2<sqrt(n).

At x=2pi/N², K_(N²)=0 and

    K_N=(1/N)*[sin(pi/N)/sin(pi/N²)]²>=4N/pi².

Therefore M_N>=2N/pi²>N/8. These weighted polynomials have a
genuine square-root negative dip, but ||f_N||1/sqrt(n)->0.
Consequently their fixed-temperature gap tends to zero by (2).
This proves in the relaxed setting that even the root-scale dip
does not imply fixed-temperature flatness. It is NOT a Boolean
counterexample or an implication about the truth of the Boolean
converse.

Later temperature detects the same dip. On x in[1/N,2/N],

    K_N>=4N/pi²>N/4,
    K_(N²)<=pi²<16.

For N>=128 this gives f_N<=-N/16, hence Y_N<=-1/16.
Including the reflected interval, this set has Haar measure at least
1/(pi*N). Thus

    log W_N(tau)>=tau/16-log(pi*N).

At tau=64log(pi*N),

    log W_N(tau)>=3tau/64.                         (4)

This is an explicit all-scale growth mechanism through a rare
negative packet, with no L1-flatness premise. It shows what a
growing-temperature argument is allowed to capture that the fixed
temperature excludes. No weighted-to-Boolean transfer is supplied.

### 3.3 Actual Boolean difference controls

For the already-recorded no-carry difference family, take
B={1,q,...,q^(k-1)}, q=k+1, and A=diff_+(B), k>=66. The previous
exact moment proof gives ||D_A||1>=k/5, D_A=2f_A, while
n=k(k-1)/2 and M<=k/2<sqrt(n). Hence

    ||f_A||1/sqrt(n)>=sqrt(2)/10,
    Z_A(1/(2sqrt(n)))>=1+1/400.

This uses the existing exact no-carry L1 estimate, not a new CLT or
new parameter sweep. The proof is recorded in the prior OP140 and
Boolean-boundary notes.

The dense Singer controls similarly have an already-proved
||f_A||1>=c_S*sqrt(n), c_S>0 eventually, so (2) supplies a fixed
gap c_S²/8. This is a consequence of their previous L1 theorem,
not independent evidence for the unrestricted assertion. Their
positive front alone does not establish the needed bulk flatness.

Both checks are compatible with the phase-polynomial obstruction:
the exponential uses unbounded degree, but at this particular
temperature its success is still equivalent to their flatness.

### 3.4 Arithmetic progressions: outside the premise eventually

For A={1,...,n}, uniformly on compact t intervals,
f_A(t/n)/n tends to sin(t)/t. On a subinterval of[4pi/3,5pi/3]
this is below-1/10. Consequently, for large n,

    M(A)>=n/10,
    W_A(1)>=c*n^-1*exp(sqrt(n)/10) ->infinity.

Thus APs fail the actual-low-M premise eventually. Their large
fixed-temperature response is a useful sign/normalization check,
not evidence about the conjectured bound on admissible low-M sets.

## 4. A full-scale mechanism: integrated tilted variance

Write

    L_A(tau)=log W_A(tau),
    dmu_tau=exp(-tau*Y)*dx/(2pi*W_A(tau)),
    m_A(tau)=L_A'(tau)=-E_mu_tau Y,
    V_A(tau)=L_A''(tau)=Var_mu_tau(Y).

These exact identities hold at every finite tau. Mean zero gives
m_A(0)=0; convexity gives m_A>=0 and increasing. If
a=M/sqrt(n), then

    m_A(T)=integral_0^T V_A(tau)dt <=a,
    L_A(2T)>=T*m_A(T).                             (5)

This section's identities do not need the earlier low-M premise;
the proposed all-scale criterion applies to every Boolean A.

The second inequality integrates m_A over[T,2T] and uses its
monotonicity. A lower bound on the TOTAL susceptibility in (5)
would yield pressure growing linearly with temperature, without
requiring a gap at tau=1. It does not lose a factor by locating
one favorable interval among logarithmically many scales.

The precise proposed Boolean all-scale estimate is

    There exist absolute c,C>0 such that for EVERY Boolean A,
    integral_0^(C*n*log(2n)) Var_mu_tau(f_A/sqrt(n)) dtau >=c. (6)

This estimate is UNPROVED. It is a derivative formulation of the
existing all-order/Gibbs C* target, not a new universal theorem.
It is equivalent to Chowla up to constants, as follows.

The forward implication is immediate from m_A(T)<=M/sqrt(n).
For the converse, a phase Bohr ball around a minimizing point has
measure at least (a/(32sqrt(n)))^n and satisfies Y<=-3a/4.
The elementary proof is in `advisor_P2_boolean_2026-10-23.md`
Section6 and uses only a partition of the phase torus and uniform
differences. It gives

    L_A(tau)>=(3a/4)*tau-n*log(32sqrt(n)/a).

At

    tau0=(4n/a)*log(32sqrt(n)/a),

we have L_A(tau0)>=a*tau0/2, hence m_A(tau0)>=a/2.
If Chowla holds with a>=c0>0, tau0<=C(c0)*n*log(2n), proving
(6) for absolute constants. No max-frequency assumption enters.

This completeness check is important: (6) permits rare negative
wells and is not known to force fixed-temperature flatness. The
weighted root-dip example in Section3.2 explicitly has its pressure
growth at a later temperature while its fixed-temperature gap
vanishes.

## 5. What the Boolean argument still has to accomplish

The normalized Boolean curvature V_A(0)=1/2 is not enough to prove
(6). Variance can, in a relaxation, collapse in a very thin initial
temperature layer and have arbitrarily small TOTAL integral. The
energy-calibrated Fejer example in Section3.1 has exactly that
initial curvature but

    integral_0^infinity V_A(tau)dt=M/sqrt(N)->0.

Here m_A(infinity)=M/sqrt(N) follows from the elementary Laplace
principle for a continuous function on the circle. The root-dip
example behaves differently: its early response tends to zero but
later susceptibility recovers a positive total area.

A genuinely useful unit-amplitude estimate must exclude ALL-SCALE
collapse, or force such a late recovery, using the individual
identities 1_A(a)²=1_A(a). Replacing these by initial curvature,
support count, nonnegative weights or scalar norm calibration
would admit the explicit failures above. No inequality performing
that Boolean step was derived here. The lead's signed coefficient
and cluster analysis should be aimed at this integrated quantity,
not at forcing a constant response at a predetermined temperature.

Decision: do not promote the proposed fixed-temperature gap to a
new primary mechanism or launch more controls for it. Keep it as
the existing qualitative L1 target. Pursue all-order coefficient
growth across temperature with the exact pressure/susceptibility
criterion (6), while preserving unrestricted signed Rayleigh and
the independent all-circle construction track. No Boolean
fixed-temperature counterfamily, universal gap, new exponent or
resolution of Chowla is claimed by this note.
