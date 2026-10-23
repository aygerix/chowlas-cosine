# Coupled cubic dual, one stopped pilot, and an explicit profile countermodel

2026-10-23, continuation after 92215dc. Full Chowla remains open.
This note closes the recorded two-scale task and makes a scope
limitation of the current dense-profile relaxation explicit.
The sole internal advisor checked the paper calculations independently;
see [its audit](advisor_cubic_two_scale_2026-10-23.md).
No publication priority, Lean/kernel verification, or unrestricted
exponent improvement is claimed.

## 1. Valid coupled dual and exact certificate algebra

Use the definitions and limiting hypotheses in
[the preceding proof](cubic_profile_cap_2026-10-23.md):

    phi(v)=(1-sqrt(1-v))/2, G(v)=v*sqrt(1-v)/4,
    v=4p(1-p), 0<=v<=2/3, c0=G(2/3)=sqrt(3)/18.

Positive definiteness of the ACTUAL cubic profile gives

    R(t)=G(v(2t))-2G(v(t))^2/c0+c0>=0.

For continuous 0<=gamma<=1/24, supported in [0,1], integration
and the change of variables s=2t give the upper-bound objective

    Lambda_t(v)=phi(v)+gamma(t/2)*G(v)/2-2gamma(t)*G(v)^2/c0,
    d<=c0*integral gamma+sup_(w in W) integral Lambda_t((2/3)|w|^2).

This is derived on the actual profile BEFORE Gabor-Jensen; individual
generators need not have positive-definite cubic profiles. The previous
note proves Lambda convex and increasing on [0,2/3]. Tangent
continuation at the actual support cap b(t) preserves the argument.

For ONE bounded discovery pilot take

    s(t)=(1-32|t-7/32|)_+, gamma=rho*s, 0<=rho<=1/24,
    integral s=1/32, cU=962250449/10^10>c0.

Replacing c0 by cU in the denominator and offset safely enlarges
the objective. Put a=rho*s(t/2)/2, dcoef=2rho*s(t)/cU and
v=(2/3)x^2. On a piece where s and s(t/2) are affine in t,
Lambda and its tangent continuation are affine in t. It suffices
to prove the UNSQUARED inequality at both t endpoints.

For a proposed rational upper bound B(x), on the low branch put

    L=1-a*v/2>0,
    A=B-1/2+dcoef*v^2*(1-v)/16.

Then L^2*(1-v)/4-A^2>=0 is sufficient for Lambda<=B.
On the tangent branch at a rational b, put

    Kb=b^2*(1-b)+b*(2-3b)*(v-b),
    N=4-2b-2v-a*(b^2+(2-3b)*v),
    A=B-1/2+dcoef*Kb/16.

Here N>=35/27>0, and N^2-64*(1-b)*A^2>=0 is sufficient.
Squaring the inequality at t endpoints does NOT justify interpolating
the squared polynomial in t. Affineness of the unsquared expression
is the reason endpoint verification is enough. No exact all-x
certificate for a positive-rho proposal was produced or needed.

## 2. Certified discriminator; the optimization did not use it

Let w(t)=(1-t)cos(pi*t)+sin(pi*t)/pi on [0,1], extended evenly
and by zero. This is the normalized autocorrelation of the
nonnegative half-sine function. Both w and
H(s)=s^2*sqrt(3-2s^2) have the monotonicities used in
[the probe source](../../src/cubic_two_scale_probe.py).

Using 192-bit Arb and monotone endpoint bounds on 64 intervals,
the probe certifies THROUGHOUT [3/16,1/4]

    [c0*H(w(2t))-2*c0^2*H(w(t))^2/cU+cU]/c0 < -1/100.

Thus the coupled information detects something the pointwise cap
alone misses. Child caps are inactive since w(3/8)<27/50 and
(2/3)(27/50)^2<1/5<b1. On the parent interval b>=b3>1/3;
the correction -2s*G(v)^2/cU is convex there, so its tangent
continuation only helps. This proves a strict objective decrease
for this particular generator, not a decrease of the supremum.

The ONE fixed K64, degree10 discovery LP returned

    rho=8.139804678365318e-10,
    kernel D=0.07238331307546421,
    offset=2.447665845790415e-12,
    total D=0.07238331307791188.

This is effectively zero weight and no useful improvement over the
cap-only proposal. It is floating-point discovery, NOT an exact
optimality theorem about all multipliers. Stop this shape; do not
increase K, scan shapes/frequencies, or certify a zero-weight rerun.
The proved density endpoint remains C<400/29 from the prior commit.

Artifacts: [probe](../experiments/cubic_two_scale_2026-10-23/probe.json),
[discovery](../experiments/cubic_two_scale_2026-10-23/discovery_sigma0.6667_K64_d10_s0.1_t0.json).
Source: [discovery program](../../src/cubic_two_scale_discovery.py).
Both bounded Dirichlet jobs finished successfully. No GPU was used.

## 3. Explicit countermodel to the current continuum relaxation

This makes the older NOTEBOOK cont.18 small-PD-bump heuristic
rigorous for a specified class of conditions. Define on the real line

    W(t)=(1-|t|)_+, sigma=1/4, v(t)=sigma*W(t)^2,
    p(t)=phi(v(t)), e(t)=v(t)/4,
    h(t)=g(p(t))=G(v(t)).

These functions are continuous, even and supported in [-1,1].
They have ALL the following properties:

1. 0<=p<=p(0)=(2-sqrt(3))/4<(3-sqrt(3))/6.
2. e=p(1-p) and h=p(1-p)(1-2p) exactly.
3. p, e and h are positive definite on the real line.
4. e/e(0)=W^2 is exactly a single member of the Gabor square class.
5. Their density is

       d_*=integral_0^1 p(t)dt
          =1/2-sqrt(3)/8-pi/12 > 3/140.

Proof of (3) for p and e: W is the autocorrelation of the indicator
of [0,1], hence normalized positive definite. Products preserve
positive definiteness. The uniformly convergent series

    phi(v)=sum_(k>=1) Catalan_(k-1)*v^k/4^k

has nonnegative coefficients, proving the assertion for p; the
assertion for e is immediate.

For h, write u=1-t on 0<t<1 and v=sigma*u^2. Direct differentiation
gives

    h''(t)=sigma*(2-9v+6v^2)/(4*(1-v)^(3/2))>0.

The numerator is decreasing on [0,1/4] and has minimum 1/8.
Also h(1)=h'(1)=0. Consequently

    h(t)=integral_0^1 r*h''(r)*(1-|t|/r)_+ dr.

Each triangular kernel in this positive mixture is positive definite.
This proves the assertion for h on the entire real line, including
the corner at zero; differentiability across zero is not assumed.

For (5), an antiderivative of sqrt(1-u^2/4) is
u*sqrt(1-u^2/4)/2+arcsin(u/2). Evaluating the endpoints gives
the formula. Using sqrt(3)<26/15 and pi<22/7 gives the strict
lower bound 1/2-13/60-11/42=3/140.

An exact symbolic check of the derivative identity, endpoints,
antiderivative and rational bound ran on Dirichlet and passed:
[source](../../src/cubic_profile_countermodel.py),
[result](../experiments/cubic_two_scale_2026-10-23/profile_countermodel.json).
The positive-definiteness argument is the paper proof above, not
an inference from finitely sampled matrices.

The model also satisfies generic completely positive TRANSLATION
Gram conditions for p,e,h. A triangular kernel is an autocorrelation
of a nonnegative function, so its finite translation Gram matrices
are completely positive. Positive sums, limits and Schur products
preserve that cone. Apply the positive series for p, W^2 for e,
and the triangular mixture for h. This does not supply a completely
positive Boolean polynomial with small floor.

## 4. Scope and global research decision

All pointwise support caps, all positive-definite matrix constraints
on p,e,h, and all valid duals of THESE CONDITIONS accept this
profile. In particular, d_*>=1/C for every C>=140/3. These abstract
conditions therefore cannot by themselves contradict hypothetical
low-minimum sequences at every fixed density. Adding further sound
dual multipliers of the same conditions cannot remove an admissible
profile. The earlier numerical single-generator estimate near 15.6
is not promoted to a sharp all-mixture threshold by this observation.

This is a CONTINUUM RELAXATION COUNTERMODEL. It is not a set of
integers, a weighted finite-polynomial realization, a low-M sequence,
an Epoch construction, or an obstruction to every dense-set method.
Finite Boolean information discarded by the relaxation may eliminate
it. The exact n^(1/3) theorem for C<400/29 remains valid.

Strategic decision: stop the unused two-scale shape and stop treating
successive constant refinements in this relaxation as a demonstrated
route to unrestricted Chowla. Retain the completed dense theorem.
The unrestricted line must derive a new finite Boolean consequence;
the separate completely positive vector-centroid attempt is being
audited rather than assumed to provide that consequence. Keep a
genuine growing all-circle construction line distinct from both.
No manuscript or outreach work is authorized. Shared Dirichlet was
left running; no lifecycle action occurred; cumulative RunPod cost
remains $0.10.

## 5. Changed finite Boolean attempt: preserve all component interactions

This is a refinement of the existing P76 completely positive (CP)
certificate problem, not a representation theorem for arbitrary A.
Suppose a FINITE decomposition is available:

    P(x)=lambda+f_A(x)=sum_i |Q_i(e^(ix))|^2,
    Q_i(z)=sum_b q_(i,b) z^b, q_(i,b)>=0.

Every component support is an A-clique: a missing positive lag
has total correlation zero, and all component correlations are
nonnegative, so each vanishes separately. For any X_i supported
on that clique and whose coefficients sum to zero,

    integral P*|X_i|^2=(lambda-1/2)*||X_i||_2^2.       (9)

The vector-centroid choice X_(i,b)=q_(i,b)(b-mu_i) is valid, but
its hoped-for global variance ratio is false even for every optimal
CP decomposition in the growing satellite example in the advisor
note. Its actual M<=sqrt(n) and normalized limit is 1/sqrt(2),
not zero. This is an obstruction to that proposed bridge only.

For bounded translations fix a real theta, set S_i=Q_i(1)>0 and

    c_i=Q_i(e^(i theta))/S_i,
    X_(i,b)=(e^(ib theta)-c_i)q_(i,b),
    U_ij(d)=sum_b X_(i,b)q_(j,b+d),
    R_ji(d)=sum_b q_(j,b)q_(i,b+d).

The exact relation, including complex phases, is

    U_ij(-d)-e^(id theta)U_ji(d)
        =(e^(id theta)c_j-c_i)R_ji(d).                (10)

Sum (9), expand P=sum_j|Q_j|^2, and use Parseval. Applying the
parallelogram identity to the involution (i,j,d)->(j,i,-d) gives

    (lambda-1/2)sum_i ||X_i||_2^2
      =1/4 sum_(i,j,d) |e^(id theta)c_j-c_i|^2 R_ji(d)^2
       +1/4 sum_(i,j,d) |U_ij(-d)+e^(id theta)U_ji(d)|^2. (11)

ALL signed lags, including zero, are retained. This identity is
unchanged by replacing any Q_i by R identical copies Q_i/sqrt(R).
A diagonal-only attempt instead produces sum_i |c_i|^2 R_ii(d)^2,
which shrinks under that harmless duplication. Thus diagonal-only
componentwise squares cannot be substituted for the Boolean total

    sum_i R_ii(d)=1_A(d)/2, d>0.                     (12)

There is no claim that (11) alone forces a square-root floor.
Using (12) to bound (11) without losing the cross-component
interactions is the precise unproved finite task.

A common-center contraction is already audited and must not be
restarted as a new route. Define

    a_theta=sum_(i,b) q_(i,b)^2 e^(ib theta),
    T_theta=sum_i S_i Q_i(e^(i theta)),
    B_theta=(lambda-1/2)a_theta+T_theta/2.

With a COMMON complex c in X_i=Q_i(e^(i theta)z)-cQ_i(z),
the exact total energy equals

    E(c)=lambda^2+f_A(theta)/2
          +|c|^2*(lambda^2+n/2)-2Re(conj(c)*B_theta). (13)

Its minimum is at c=B_theta/(lambda^2+n/2), giving just the
generic Schur/Cauchy inequality

    |B_theta|^2<=(lambda^2+f_A(theta)/2)*(lambda^2+n/2).

This gives no new Boolean size bound. The separate MEAN penalty
is minimized at c=T_theta/(lambda+n), with value
(P(theta)-|T_theta|^2/(lambda+n))/2. That c need not minimize
the full energy (13). Dropping this penalty is invalid. Retain the
uncontracted finite object (11) only as a precise open target;
do not launch a pilot absent a quantitative conjecture about it.
[Independent advisor derivations and satellite proof](advisor_cp_vector_2026-10-23.md).
