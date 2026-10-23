# Exponential continuation: exact identities, two reductions, and the decision

2026-10-23. Previous goal turn classified as progress: checkpoint
f5801d2 contains reviewed amplification and phase-polynomial results
with exact finite artifacts. This continuation attempts the recorded
all-order coefficient problem. Full Chowla remains unresolved.
The following paper derivations were independently checked in
[the exponential audit](advisor_exponential_boolean_2026-10-23.md)
and [the depth/global review](advisor_exponential_depth_2026-10-23.md).
No new kernel verification, universal exponent or novelty claim.

## 1. Exact coefficient evolution retains the collision terms

Let F=sum_A z^a, f=ReF, n=|A|, E_s=exp(-sF)=sum_j c_j(s)z^j,
Z(s)=<exp(-2sf)>=sum_j c_j(s)². All averages use probability Haar
measure. Extend c_j by zero for j<0. Exactly,

    c_0=1, c_j(0)=0 for j>0,
    c_j'=-sum_(a in A)c_(j-a),
    j*c_j=-s*sum_(a in A,a<=j)a*c_(j-a).

The second recurrence computes any finite coefficient prefix exactly
when s is rational. Define R_d(s)=sum_(j>=0)c_j*c_(j+d), R_0=Z.
Then

    Z'=-2sum_A R_a,
    R_d'=-sum_A(R_(d+a)+R_(|d-a|)).

Writing r_+(d)=#{ordered a+b=d} and
r_-(d)=#{ordered (a,b):a-b=d}, d>0, gives

    Z''=2n*Z+2sum_(d>0)(r_+(d)+2r_-(d))*R_d.       (1)

The diagonal2n uses unit coefficients. The off-diagonal correlations
can be negative and cannot be discarded. At zero, Z'(0)=0 and
Z''(0)=2n. No lower bound controlling their later cancellation was
proved. Initial curvature is not a norm-growth theorem.

## 2. Fixed scaled temperature is exactly the old flatness gap

Assume actual M<=sqrt(n), put Y=f/sqrt(n), L=<|Y|>, and
W(tau)=<exp(-tau*Y)>. For every fixed tau>0,

    tau²*L²/8 <= W(tau)-1 <= (exp(tau)-1)*L/2.       (2)

Proof: subtract the mean-zero linear term. On Y=-u,0<=u<=1,
the exponential remainder is at least tau²u²/2 and at most
u*(exp(tau)-1-tau). On Y>=0 it is between zero and tau*Y.
Both first-part masses equal L/2; Cauchy gives <Y_-²>>=L²/4.

Thus a uniform positive gap at a bounded scaled temperature is
equivalent, up to constants, to lowM L1 flatness. Do not rebrand it
as a new Boolean estimate or launch another successful-control sweep.

The advisor supplies a useful relaxation discriminator:
F_N=G_(N²)-G_N, G_L=sum_(j<L)(1-j/L)z^j. Its coefficients lie in(0,1),
occupied cardinality is N²-1, and
f=(Fejer_(N²)-Fejer_N)/2. It has ||f||1<=1 and M between N/8
and N/2 eventually, so its actual dip is root scale while (2)'s
fixed-temperature gap vanishes. Later tau=64log(pi*N) gives
logW>=3tau/64. The complete interval estimates are in the audit.
This is a weighted model, not a Boolean example or a Chowla result.

## 3. Generic selected-exponential sign; exact phase bookkeeping

Define C(u)=<F,exp(-uF)>=sum_(a in A)c_a(u), real. For any
real-coefficient analytic F with f>=-M, not just Boolean ones,

    C(u)<0 when 0<uM<=1,
    -C(u)>=u*<f_-²>>=u*||f||1²/4,
    |C(u)|<=2exp(uM)*||f||1.                       (3)

To prove the sign, use mu=1+f/M>=0 and analyticity:
1+C(u)/(2M)=<mu*Re exp(-uF)>. Bound Re exp(-uF) by exp(-uf),
then apply (1+y)exp(-ty)<=1+(1-t)y for y>=-1,0<t<=1.
The latter follows by differentiating the logarithmic difference;
its minimum is zero at y=0. For the first quantitative estimate,
the scalar deficit at y=-v has second derivative
t*exp(tv)*(2-t+tv)>=t, so it is at least tv²/2.

With E_s=exp(-sF), the complete even/odd moments are

    Q_even=(Z+1)/2, Q_odd=(Z-1)/2,
    H_even=(-Z'+C(2s))/2,
    H_odd =(-Z'-C(2s))/2.                          (4)

The even part includes the constant. For2sM<=1 its sign is negative.
The sign is generic and does not solve the Boolean quantitative gap;
at a fixed scaled temperature a root-sized C amplitude is again
equivalent to flatness by (3). No phase term was discarded.

## 4. A depth bound checks, but an existing certificate is stronger

Let h(A)=max{r>=1:A intersects rA}, with repetitions allowed.
Then C(u) is a degree-h polynomial with C'(0)=-n. The norm bound
|C(u)|²<=n*(exp(2uM)-1), followed by the odd-polynomial change
P(v)=C(v²/M)/v and the Chebyshev alternation derivative bound,
gives M>=sqrt(n)/[(2h-1)*sqrt(e²-1)]. The algebra is valid.

It is dominated by P9: set ell(a)=max{r:a in rA}, L_j={ell=j}.
Each W_j=L_j union(-L_(h+1-j)) has no A-differences. Internal
differences would strictly increase ell, and a cross sum would have
length at least h+1. The total size over j is2n, so P9 gives

    M(A)>=sqrt(n/(2h)).                            (5)

This is a useful derived corollary of the existing star certificate,
not a new universal lower-bound advance. Depth<=2 forbids EVERY
positive sum length>=3; merely A intersect3A empty is insufficient,
as A={1,4} shows. Do not restart the weaker exponential-depth proof.

Trying to make (5) universal by deleting O(M) frequencies also fails:
the [sharp core theorem](cstar_depth_core_2026-10-23.md) shows that
even actual-lowM Sidon-difference sets can require Theta(n) deletions
to leave bounded recomputed depth. The distinction between deleting
vertices with a fixed connection set and deleting/recomputing
frequencies is essential.

## 5. All-scale gap and strategic decision

For L(tau)=logW(tau), define tilted probability proportional to
exp(-tauY), m=L' and V=L''=Var_tilt(Y). Exactly,

    m(T)=int_0^T V(tau)dt,  m(T)<=M/sqrt(n),
    L(2T)>=T*m(T).

A uniform positive lower bound on the susceptibility integral up to
C*n*log(2n) is equivalent up to constants to Chowla; the converse
uses the already-checked phase-Bohr localization. The lower bound
itself is unproved. This is the existing C* problem with no additional
finite-plane restriction, not a new theorem about Boolean growth.

Global review after two reductions: stop bounded-temperature and
bounded-depth restatements. Keep the all-scale signed correlations
in (1), but require an actual new unit-coefficient inequality before
more numerical tests. Maintain reciprocal/full signed witnesses as
auxiliary routes. The independent construction track instead tested
a mathematically changed growing-multiplicity l1 loss, with its
derivation and failed single pilot preserved in
[the construction note](multiplicity_l1_2026-10-23.md).

All own CPU jobs are terminal; no new GPU use or spend. Shared
Dirichlet remains on. No external input is blocking further research.
