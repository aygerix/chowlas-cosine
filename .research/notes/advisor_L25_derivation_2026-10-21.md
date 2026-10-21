# Advisor derivation: a low-ratio Boolean obstruction to fixed-degree scalar witnesses

2026-10-21. The new GOAL.md is active. This note records an independent
mathematical derivation and review by the one internal advisor. I launched
no research computation or provisioned resource and edited only this file.
All integrals use normalized measure dx/(2*pi), with cos(a*x).

## Decision and exact scope

The following is a paper theorem, with a verified classical sampling
inequality as an external dependency. No Lean check or priority claim is
made. It addresses a proposed unrestricted witness principle inside
L25's actual domain, rather than extending a settled root-bound model.

**Theorem.** Fix an integer d>=1. There are finite constants C_d and k_d
such that the following holds. Let k>=k_d, Q=k(k-1)+1, and let
B subset {0,...,Q-1} be a cyclic (Q,k,1) perfect difference set: every
nonzero residue modulo Q has exactly one representation b-b' with
b,b' in B. Let A be the positive INTEGER differences of B and put

    n=|A|=k(k-1)/2, F(x)=sum_{b in B} exp(i*b*x),
    D(x)=2 sum_{a in A} cos(a*x)=|F(x)|^2-k.

For every real polynomial p of degree at most d for which
q(x)=p(D(x)) has mean zero, set a=<D,q>, Qq=||q||_2^2, H=<D,q^2>.
If q is not identically zero, then

    H>0, a^2/H<=C_d.

In particular, EVERY mixed determinant certificate made from such q
has positive K-root at most C_d. If a=n, then H>=n^2/C_d, regardless
of a norm constraint Qq<=beta*n. Nevertheless

    M(A)<=k/2<=sqrt(n)                               (exactly),

so these are genuine Boolean inputs satisfying L25's low-ratio
hypothesis. A fixed-degree q=P(D) cannot supply a uniform
O(n^(3/2)) constrained mixed cost even on this low-ratio class.

The degree d is fixed before k tends to infinity. The theorem does
not exclude degrees growing with k, rational functions of D, general
Fourier seeds, or finite-band projected iterations that leave the
scalar polynomial algebra.

Two supporting consequences are proved below:

1. On the same canonical perfect-difference class, ||D||_1>=c*k
   eventually for one absolute c>0. Thus vanishing normalized L1
   cannot arise in this particular control class. This does NOT
   prove the L25 constant 1/5.
2. Despite M<=sqrt(n), the normalized cubic cost diverges:

       <D^3>/n^(3/2) ~ (11/5)*sqrt(n).

   Therefore a uniform normalized-cubic bound cannot close the
   high-triple branch of the unrestricted inverse problem.

A companion arbitrary-support proposition in Section 7 shows that L1
flatness supplies an exact-coupling witness of degree less than 2*max(A),
using a de la Vallee Poussin multiplier. Thus general Fourier-band
optimization can escape the fixed-degree obstruction with a theoretically
adequate bandwidth; no such flatness conclusion has been proved for all A.

## 1. Booleanity and the exact all-circle upper bound

Cyclic difference uniqueness implies uniqueness of every positive
integer difference: two equal integer differences would be equal
modulo Q. There are exactly k(k-1)/2 of them, all positive and
distinct. The exact square identity gives

    D=|F|^2-k>=-k,
    M(A)<=k/2.

Since k^2<=2k(k-1)=4n for k>=2, this proves M(A)<=sqrt(n),
not merely an unquantified bounded-ratio condition.

Every assertion here is for canonical representatives in ONE interval
of Q consecutive integers; translating that interval changes F by
a unit-modulus monomial and does not change D. It includes arbitrary
cyclic cuts and multipliers followed by canonical reduction. It does
not automatically cover representatives spread over many periods.

## 2. Remove the exceptional root sample

Let z=exp(i*x), U_Q(z)=1+z+...+z^(Q-1), and write

    S=(k/Q)*U_Q, R=F-S.

For a Qth root zeta^j,

    R(1)=0,
    |R(zeta^j)|^2=k-1   (j!=0).

The second identity follows by expanding |F|^2 on the cyclic group:
its nonconstant Fourier coefficients are all 1. This identity is
used on the root grid only; no negative exponent is replaced by a
residue in a continuous-circle identity.

The classical Marcinkiewicz-Zygmund sampling inequality states that
for each fixed 1<p<infinity there is a constant M_p independent of
Q and the analytic polynomial P of degree at most Q-1 such that

    integral |P|^p <= (M_p/Q)*sum_{j=0}^{Q-1}|P(zeta^j)|^p.

The exact needed version is recalled in equation (1), introduction,
of [Ortega-Cerda and Saludes, arXiv:math/0507533v1](https://arxiv.org/pdf/math/0507533),
published in Journal of Approximation Theory 145 (2007), 237-252.
I checked this primary source. Conventions for normalizing the
integral only modify M_p. In particular,

    integral |R|^p <= M_p*k^(p/2),
    ||R||_p=O_p(sqrt(k)).                            (2.1)

Exact L2 orthogonality also gives

    ||S||_2^2=k^2/Q=O(1),
    ||R||_2^2=k-k^2/Q.

The elementary Dirichlet-kernel estimate, for fixed p>1, gives

    integral |S|^p=O_p(k^p/Q),
    ||S||_p=O_p(k^(1-2/p)).                         (2.2)

All constants are independent of the choice of B.

## 3. Every fixed high moment is dominated by the positive front

Put

    G(t)=(sin(t/2)/(t/2))^2, G(0)=1,
    mu_r=(1/(2*pi))*integral_R G(t)^r dt.

Rescale x=t/Q. Since k^2/Q tends to 1,

    |S(t/Q)|^2/Q -> G(t).

For |t|<=pi*Q, the left side is bounded by
C*min(1,|t|^(-2)). Dominated convergence gives, for every fixed r>=1,

    integral |S|^(2r)/Q^(r-1) -> mu_r.

For fixed integer r>=3, expand |F|^(2r)=|S+R|^(2r). Every mixed term
is bounded by a fixed multiple of integral |R|^j*|S|^(2r-j), for
1<=j<=2r. By Holder, (2.1), and (2.2), it is at most

    O_r(k^[2r-2-j*(1/2-1/r)]).

Because 1/2-1/r>0, every one is o(k^(2r-2)). Therefore

    integral |F|^(2r)/Q^(r-1) -> mu_r.

Expanding (|F|^2-k)^r changes only lower-order terms. For powers
of |F| of order at least four, the preceding norm bounds give
integral |F|^(2m)=O_m(k^(2m-2)); the remaining cases use integral
|F|^2=k. Consequently

    integral D^r/Q^(r-1) -> mu_r, r>=3.             (3.1)

These convergences are uniform over all B with the stated parameters.

**Important exception.** Formula (3.1) does not extend to r=2:

    integral D^2/Q=2n/Q -> 1, whereas mu_2=2/3.

Rounding/noise or the remainder R contributes at the same order in
the second moment. This is precisely the exception that must be
retained in the coupling vector and norm matrix.

The mu_r are rational and explicitly computable:

    mu_r = sum_{j=0}^{r-1} (-1)^j binom(2r,j)*(r-j)^(2r-1)
           / (2r-1)!.

This follows from Fourier inversion for the sum of 2r independent
uniform [0,1] variables at r. In particular

    mu_1=1, mu_2=2/3, mu_3=11/20.

## 4. The complete fixed-degree mean-zero scalar space

Use the basis

    psi_j = D^j/Q^(j-1) - integral D^j/Q^(j-1), j=1,...,d.

The means being subtracted are O(1); the first is zero. Let
H^(Q)_ij=<D,psi_i*psi_j> and a^(Q)_j=<D,psi_j>. From (3.1),

    H^(Q)/Q^2 -> H_d, (H_d)_ij=mu_(i+j+1),
    a^(Q)/Q -> v_d,
    (v_d)_1=1, (v_d)_j=mu_(j+1) for j>=2.

The centering correction in H is only O(Q): each mean is O(1) and
<D,D^j/Q^(j-1)>=O(Q). The first component of v is 1 by the exact
second moment, not mu_2.

For a nonzero real vector c,

    c^T H_d c
      =(1/(2*pi))*integral_R G(t)*(sum_{j=1}^d c_j*G(t)^j)^2 dt >0.

Indeed, G is continuous, nonconstant, and takes an interval of
positive values. A nonzero polynomial cannot vanish on that
interval. Thus H_d is positive definite.

For all sufficiently large k, uniformly in B, H^(Q) is positive
definite and a^(Q)^T*(H^(Q))^(-1)*a^(Q) is bounded. This proves
H>0 and a^2/H<=C_d for every nonzero q in the entire span, including
arbitrary coefficient vectors depending on k.

There is an exact computable limiting cap:

    C_d^* = v_d^T*(H_d)^(-1)*v_d,
    sup_{q!=0} a^2/H -> C_d^*.

All entries of v_d and H_d are rational. For every epsilon>0,
eventually C_d can be taken as C_d^*+epsilon. The norm matrices are
O(Q), so the best positive determinant root also tends to C_d^*.
For the upper-bound implication alone, use simply

    Qq*K^2+H*K-a^2=0  ==>  K<=a^2/H.

This is an upper bound on what these witnesses can CERTIFY. It is
not an upper bound on the actual K=-min D.

## 5. A positive L1 constant for this control class

The theorem above does not require an L1 asymptotic. A separate
argument shows that vanishing normalized L1 is impossible here.

Integer Sidon uniqueness gives the exact fourth moment

    integral |F|^4=2k^2-k.

Also

    integral |S|^4
      =(k^4/Q^4)*(2Q^3+Q)/3 ~ (2/3)k^2.

At this fourth-moment order the earlier common-exponent Holder
bound is not enough. Instead use ||R||_6=O(sqrt(k)) and

    integral |S|*|R|^3 =O(k^(3/2)),
    integral |S|^2*|R|^2=O(k^(5/3)),
    integral |S|^3*|R|=O(k^(11/6)).

The exponents follow respectively from Holder with S in L2, L3,
and L^(18/5). All are o(k^2). Expanding |S+R|^4 therefore gives

    integral |R|^4 ~ (4/3)k^2.

For Y=|R|^2-k,

    integral Y^2 ~ k^2/3,
    integral |Y|^3 <=4*(M_6+1)*k^3.

Cauchy-Schwarz, in the form
(integral Y^2)^2 <= (integral |Y|)*(integral |Y|^3), now gives
||Y||_1>=c_1*k for one absolute c_1>0 eventually. Finally,

    ||D-Y||_1
      <=2*||R||_2*||S||_2+||S||_2^2=O(sqrt(k)),

so ||D||_1>=c*k for some absolute c>0, uniformly in B.
The inequality ||D||_1<=2K also yields M(A)>=c*k/4, if desired.
This does not supply the specific constant k/(5*sqrt(2)) required
asymptotically by L25. No assertion that this control proves L25
or settles arbitrary Newman-polynomial flatness is made.

This result audits the literal canonical-Singer flatness lead:
one cannot infer continuous-circle L1 flatness from the root grid.
It is not a general adjudication of every construction or main
claim in the previously screened preprint.

## 6. High triples: a natural inverse statement is false

By (3.1) and mu_3=11/20,

    integral D^3 ~ (11/20)Q^2,
    integral D^3/n^(3/2) ~ (11/5)*sqrt(n) -> infinity,

while M(A)<=sqrt(n) holds exactly. Thus

    M(A)<=sqrt(n)  ==>  integral D^3=O(n^(3/2))

is FALSE even for canonical Singer integer-difference inputs.
The high-triple branch cannot be discharged by assuming a bounded
normalized cubic moment on bounded-ratio Boolean supports.

The lead's elementary calibration remains valid: for mu=||D||_1/2,
P=D_+, N=D_-, one has integral P^2>=2n-K*mu and

    integral D^3 >= (2n-K*mu)^2/mu-K^2*mu
                  =8n^2/||D||_1-4nK

when 2n-K*mu>=0. For genuine Boolean D the cubic moment is
nonnegative; when 2n-K*mu<0 the displayed final right side is
negative, so that final lower bound remains valid by this separate
argument. Hence K/sqrt(n)<=2 and integral D^3/n^(3/2)<=32 imply
||D||_1/sqrt(n)>=1/5. The Singer examples show why the complementary
branch is real rather than an algebraic nuisance.

## 7. Positive finite-band theorem for ARBITRARY supports

This proposition was derived by the lead and independently checked here.
It improves my preliminary Jackson-smoothing argument: it preserves the
coupling exactly with no Bernstein approximation error.

Let A be ANY nonempty finite set of distinct positive integers, X=max(A),
n=|A|, D=2*f_A, and L=||D||_1. Define the Fejer kernel

    F_N(x)=|1+exp(i*x)+...+exp(i*(N-1)*x)|^2/N,

which has degree N-1, mean 1, is nonnegative, and has multiplier
1-|j|/N on |j|<N. Set

    V=2*F_(2X)-F_X.

Then

    Vhat(j)=1 for |j|<=X,
    Vhat(j)=2-|j|/X for X<|j|<2X,
    Vhat(j)=0 for |j|>=2X,
    integral V=1, ||V||_1<=3.

V is not pointwise nonnegative. What matters for L2 contraction is
the distinct fact that its multipliers lie in [0,1]. Let s=sign(D),
m0=integral s, and define

    q=(n/L)*(V*s-m0),

where * is normalized circle convolution. This is a real mean-zero
trigonometric polynomial of degree at most 2X-1, and V*D=D, so

    <D,q>=(n/L)*<V*D,s>=n.

Parseval gives

    Qq=(n^2/L^2)*sum_{j!=0} Vhat(j)^2*|shat(j)|^2
       <=n^2*(1-m0^2)/L^2 <=n^2/L^2.

Also ||V*s-m0||_infinity<=3+1=4. Since integral D_+=integral D_-=L/2,

    |H|=|integral D*q^2|<=8*n^2/L.

The factor 8 uses the separate positive and negative masses; the rougher
bound ||D||_1*||q||_infinity^2 would give 16.

**Unrestricted conditional conclusion.** For every delta>0 and every
genuine A with L>=delta*sqrt(n), there is a real q with

    degree(q)<2X, mean(q)=0, a=n,
    Qq<=n/delta^2, |H|<=8*n^(3/2)/delta.             (7.1)

No density, maximal-frequency restriction, ratio bound, or construction
hypothesis is used. X only specifies the witness bandwidth; it is not
bounded in an asserted universal conclusion.

For L25's delta=1/5, (7.1) gives a=n, Qq<=25n, H<=40*n^(3/2) in the
FULL positive-frequency band {1,...,2X-1}. Consequently a rigorous
lower bound on that band's constrained minimum exceeding 40*n^(3/2)
would force failure of L25's L1 conclusion. To make it an L25
counterexample, also certify K<=2*sqrt(n). A numerically poor proposed
witness supplies no such lower bound.

There is pointwise norm slack for rational approximation: sign(D)
cannot be a finite trigonometric polynomial because D has open arcs of
both signs. It therefore has a nonzero Fourier tail beyond 2X, and the
multiplier contraction above is strict before the final weak bound.
Rational approximation plus repair along D can preserve a=n and the
norm budget for each fixed input, with small cost slack. No uniform
size of that slack or approximation precision is asserted.

This is not a proof of L25. It is a finite-band realization of its
sufficient witness, and it justifies using general Fourier seeds in
bandwidth2X when testing the conditional inverse principle. It does
not claim that this bandwidth approximates the full-space optimizer
to arbitrary accuracy, or that a restricted Krylov subspace has
already found the band optimum.

## 8. Independent review of the |D| quadrature certificate

The lead proposed an N^(-2) quadrature remainder for ||D||_1.
I independently checked it. For g=|D|, distributionally,

    g''=sgn(D)*D'' dx + 2 sum_{simple zeros r}|D'(r)| delta_r.

Zeros of higher multiplicity have D'(r)=0 and give no atom.
Periodicity gives

    2 sum |D'(r)|=-integral sgn(D)*D'' <=integral |D''|,
    TV(g'')<=2 integral |D''|.

For nonzero integer m,
|g_hat(m)|<=TV(g'')/(2*pi*m^2). The coefficients are absolutely
summable, so summing the nonzero N-multiples proves

    |grid_mean_N |D| - ||D||_1|
      <=(2*pi^2/(3*N^2))*||D''||_1
      <=7*ceil(sqrt(2 sum_{a in A} a^4))/N^2.

The last expression is a rational rigorous remainder if the ceiling
is computed with exact integer arithmetic. Arb must separately
enclose the finite grid evaluations. No root isolation is needed.
The proposed check A={1,2} has ||D||_1=3*sqrt(3)/pi, as stated.
I did not run the implementation or its tests.

## 9. ONE next arbitrary-support operator target

The finite-band proposition removes bandwidth uncertainty for a
sufficient certificate under flatness. It does not supply the missing
Boolean estimate: its proof works for general finite-band real D as
well. The following is a precise CONJECTURAL target using linked
zero/one Toeplitz-plus-Hankel entries, not a proved consequence of
positivity or an assumption for further theorems.

For ANY nonempty Boolean A, let X=max(A), n=|A|, c=1_A as a vector
indexed by1,...,2X, and

    C_jk=(1/2)*(1_A(|j-k|)+1_A(j+k)),
    Z=C+2*sqrt(n)*I.

**OP140 (CONJECTURED):** for EVERY genuine Boolean A,

    K=-min D<=2*sqrt(n)
      ==> J=c^T*Z^(-1)*c >= sqrt(n)/140.             (9.1)

The actual global low-K hypothesis implies C>=-sqrt(n)*I and
Z>=sqrt(n)*I, so the inverse exists. The value1/140 is calibrated
below, not proved. This is a computationally useful finite-band
inverse target, not an independent proof of L25.

A STRONGER optional spectral-leverage variant replaces the global
low-K hypothesis by the finite-matrix condition

    C >= -sqrt(n)*I
      ==> c^T*Z^(-1)*c >= alpha*sqrt(n),             (9.2)

for an absolute alpha>0, provisionally1/140. This variant is not
assumed and may fail even if OP140 or L25 is true. The linked
Booleanity matters: c_j and the entries
of C come from the SAME frequency indicator, with no weights,
duplicates, bounded-span hypothesis, or prescribed construction.

Why OP140 advances the full theorem: on its low-K branch, for every
band witness positivity gives

    a^2<=K*(H+K*Qq)<=K*(H+4*sqrt(n)*Qq).

The variational supremum of a^2/(H+4*sqrt(n)*Qq) is J, so

    J<=K.

Thus OP140 would prove K>=sqrt(n)/140, hence M>=sqrt(n)/280;
the complementary branch K>2*sqrt(n) already has M>sqrt(n).
No separate norm/cost conversion is needed for this implication.
For comparison, the full mean-zero L2 variational leverage at
lambda=4*sqrt(n) is lambda-1/I, I=integral1/(lambda+D), consistent
with the earlier resolvent formula. J here is the finite-band value.

The stronger variant (9.2) would also prove full Chowla: when C has
an eigenvalue below -sqrt(n), its eigenvector directly gives
H/Qq<-2*sqrt(n), hence M>sqrt(n); in its other branch use the
following controlled-coupling witness. Set

    v=n*Z^(-1)*c/J, q=sum_j v_j*cos(j*x).

Then

    a=c^T*v=n,
    Qq=||v||^2/2 <= n^(3/2)/(2J) <= n/(2alpha),
    H<=v^T*Z*v=n^2/J <= n^(3/2)/alpha.

The usual positivity determinant yields an absolute square-root
lower bound. This conversion is also available for OP140, but its
direct J<=K implication above is simpler. Preserve the distinction
between the global hypothesis in (9.1) and the stronger proposed
finite-matrix branch in (9.2).

The numerical constant1/140 is calibrated, not established. If L25
holds on a given input and K<=2*sqrt(n), then the branch condition
holds, and Section7's sign witness gives

    J=sup_v (c^T*v)^2/(v^T*Z*v)
      >= L^2/(8L+4*sqrt(n)) >= sqrt(n)/140.

Tests of OP140 must use the certified global bound K<=2*sqrt(n),
rather than inferring it from finite C. A counterexample only to
the stronger finite-matrix version need
not refute L25. Constants other than1/140 remain possible even
if that provisional value fails.

**Weighted escape, checked analytically.** For every integer m>=2,
take the non-Boolean weights w_a=1-a/m, 1<=a<m. Put

    D_w=2 sum_a w_a*cos(a*x)=F_m-1>=-1,
    n_w=sum_a w_a^2=(m-1)*(2m-1)/(6m) -> infinity.

Here ||D_w||_1<=2. Form the SAME weighted Toeplitz-plus-Hankel C_w,
the coefficient vector c_w, and Z_w=C_w+2*sqrt(n_w)*I. Its finite
matrix branch holds because C_w>=-I/2. Nevertheless, enlarging
the variational space to all real L2 functions gives

    J_w=c_w^T*Z_w^(-1)*c_w
      <= integral D_w^2/(D_w+4*sqrt(n_w))
      <= [4*sqrt(n_w)/(4*sqrt(n_w)-1)]*||D_w||_1/2
      =O(1).

The final bound follows separately on D_w>=0 and D_w<0. Thus
J_w/sqrt(n_w) tends to zero. Even a linked [0,1]-weighted version
of (9.1) is false. A proof must use exact indicator structure,
not merely bounded coefficients, mean/variance normalization,
positive definiteness, or small negative minimum. The existing
period-five two-profile escape is a further adversary.

For an adversarial finite test, an upper certificate on J below
sqrt(n)/140, together with a certified global low-K bound, refutes
OP140. A finite branch PSD certificate alone instead tests only
the stronger variant. A feasible v only gives a LOWER
bound on J. An approximate inverse solve without a residual/error
certificate supplies neither global conclusion. No extra job was
requested or launched for this proposed next test.

There is an inexpensive rigorous residual route for BOTH bounds.
For any proposed vector w, let r=c-Z*w and

    E=2*c^T*w-w^T*Z*w.

Completing the square gives the exact identity

    J=E+r^T*Z^(-1)*r.

Under the certified low-K hypothesis Z>=sqrt(n)*I, hence

    E<=J<=E+||r||^2/sqrt(n).                        (9.3)

Rational w, exact or rigorously enclosed C*w, and a rigorous
square-root enclosure give a certified J interval without
inverting a large matrix exactly. The entries involving sqrt(n)
can be handled in its quadratic field or by outward intervals.
This is the first concrete finite test of OP140 to use when
authorized; a small residual certifies an upper bound as well as
a witness lower bound.

## 10. Strategic decision and remaining exact gap

The first attempted countermechanism was that the canonical Singer
controls might become L1-flat while keeping their exact square-root
upper budget. The MZ decomposition gives a uniform positive L1
constant in that class, although it does not settle the proposed
1/5 threshold. The important extracted mechanism is the exceptional
origin sample plus a uniformly Lp-bounded remainder.

The second attempt was to capture the high-triple branch with a
fixed-degree scalar witness. The complete moment-matrix argument
refutes that universal witness principle INSIDE the low-ratio domain.
This is a concrete obstruction to a solver architecture, not a
resolution of Chowla or a reason to stop.

Decision: do not treat a fixed count of D-only moment/Krylov steps
as a universal inverse theorem, and do not enlarge Singer trend
sweeps merely to fit a limiting constant. Retain growing-degree
rational resolvents and general/adaptive Fourier seeds. Under the
uncompressed multiplication operator, a fixed-depth Krylov space
starting from 1 or D lies in the scalar polynomial algebra and is
covered by the obstruction. Finite-band truncation or a general
seed can leave that algebra and is not automatically covered.

I read src/cstar_gpu_projected.py. Its cosine-coordinate center1_A
has a=n and Q=n/2; the Euclidean tangent radius sqrt(47n) therefore
targets Q<=24n. The reduced matrix W*(C*W^T) and forcing W*C*1_A
have the correct factors. The general/random seeds plus sampled
resolvents are outside the scalar fixed-degree restriction. The
sampled Kgrid is not a certified global K, so the rational starts
are grid proposals even if lambda may lie below the true K. Exact
final polynomial verification is what makes an accepted result
global. I also flagged a defensive empty-block guard before taking
the maximum of a Gram spectrum after Krylov exhaustion.

For finite scalar caps, degree4 needs moments through order9.
An independent packed moment recount through7 fully covers
degrees1..3, not every input to degree4; the lead was notified
to keep that verification scope precise. The lead subsequently
reports a PASS after extending the recount to9 and adding rational
Schur/linear-system checks. I did not rerun those jobs.

The Spencer rounded-profile argument sent by the lead has the same
positive limiting H matrix and is sound with its r=2 caveat. Its
published checkpoint only proves M<=70*sqrt(n), so by itself it
does not place that family inside L25's M<=sqrt(n) domain. The
Singer argument above closes that scope gap without improving a
discrepancy constant.

The exact unrestricted gap remains: derive a Boolean/torsion-free
mechanism controlling L1 or producing a useful direct certificate
for arbitrary low-ratio A, including the high-triple branch.
Weighted positivity and scalar moments alone do not supply it.
No universal exponent, Epoch generator, or arbitrary-A flatness
bound was proved here. Independent all-circle construction work
must continue separately from lower-bound certificates.

First concrete next check coordinated with the lead: use an exact
finite scalar-space cap and a broader certified witness on one
saved genuine low-ratio input to validate this separation, then
test whether the projected general-seed/full-resolvent method
escapes it. The lead owns those Dirichlet jobs and resource records;
none was launched by this advisor.
