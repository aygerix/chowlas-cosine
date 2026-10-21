# Advisor: the averaged peak-one PD reference target is refuted

2026-10-21. Internal advisor, GPT-6.1 Sol/MAX. I read the current
ROUTES ledger before this attempt. This addresses the exact averaged
reference hypothesis proposed after IPD failed; it is not a new
construction-side root-bound exclusion. No jobs, provisioning, or
additional agents were launched. Only this note was edited.

All integrals use dx/(2*pi), with cos(a*x). Write D=2f_A,
n=|A|, K=-min_R D. The proposed target was: for every genuine Boolean
A with K<=2sqrt(n), some finite normalized PD coefficient profile
p:Z->[0,1], p_0=1, sum_{j>0}p_j=n, has

    H = integral D(D-D_p)^2 <= C n^(3/2),
    D_p = 2 sum_{j>0}p_j cos(jx),

with one absolute C. The following refutes this for EVERY C,
including unbounded/adaptive Fourier support and adaptive selected
coefficients. The lead proposed the two-front obstruction; I checked
it independently and give a quantitative elementary front derivation.

## 1. General positive-front budget lemma

Let D be any real measurable function with D>=-K. Let P>=0 have
mean b>=0, and write q=D+b-P. Suppose Q=integral q^2 is finite.
Let E be measurable, with D>0 on E, and put

    sigma = integral_E(D+b)-b,
    R_E   = integral_E 1/D.

If sigma>0 and 0<R_E<infinity, then

    integral Dq^2 >= sigma^2/R_E - KQ.                 (1)

Proof. Since integral_E P<=b, integral_E q>=sigma. Weighted
Cauchy--Schwarz gives integral_E Dq^2 >= sigma^2/R_E.
The contribution of the complement is at least -KQ. QED.

In particular, if D>=c k^2 on E, |E|<=C_E/k^2,
integral_E D>=b+delta, K=O(k), and Q=O(k^2), then

    integral Dq^2 >= (c delta^2/C_E)k^4-O(k^3).

This uses no PD assumption. It exposes the resource constraint:
a reference of total nonnegative mass b cannot match more than b
units of exceptional positive-front mass. An O(n) norm bound limits
how much negative mixed cost can compensate elsewhere.

## 2. Boolean counterfamily inside the exact low-K domain

Let k tend to infinity along Singer parameters, and put

    Q0 = k(k-1)+1.

Choose a cyclic (Q0,k,1) perfect difference set B, represented in
{0,...,Q0-1}. Sort it as b_1<...<b_k. Retain the indices i for which

    floor(3i/4)>floor(3(i-1)/4),

obtaining B' of size h=floor(3k/4). Thus every prefix of m sorted
points contains exactly floor(3m/4) retained points.

Let A_1 and A_2 be the positive INTEGER differences of B and B',
respectively. Their elements are distinct within each set, by cyclic
difference uniqueness. Set

    L=Q0^3,
    A=A_1 union L A_2,
    n=[k(k-1)+h(h-1)]/2.

The blocks are disjoint because max(A_1)<Q0<L. Hence A is a
genuine set of distinct positive integers, with no multiplicities.
The all-circle identities are

    D_1=|F_B|^2-k >=-k,
    D_2=|F_B'|^2-h >=-h,
    D(x)=D_1(x)+D_2(Lx) >=-(k+h).

Moreover,

    (k+h)^2<=4n
      iff (k-h)^2>=2(k+h).

Because h<=3k/4, this holds for k>=56. Thus K<=2sqrt(n),
or M(A)<=sqrt(n), exactly on the entire circle. Also

    n~25k^2/32,       n<=k^2,       K<=2k.

The construction is being used to refute an unrestricted reference
principle. It is not claimed to give M(A)/sqrt(n)->0.

## 3. Elementary quantitative front limit

Perfect difference uniqueness gives, for 1<=m<Q0,

    |F_B(2*pi*m/Q0)|=sqrt(k-1).

For |t|<=pi, expand the values exp(it*j/Q0), 0<=j<Q0, by their
exact Q0-point discrete Fourier transform. Write its coefficients
as a_m(t). For m!=0, with d_m=min(m,Q0-m), the geometric-series
formula and |sin u|>=2|u|/pi on |u|<=pi/2 give

    |a_m(t)|<=1/d_m,
    sum_{m=1}^{Q0-1}|a_m(t)|<=2(1+log Q0).

The zero coefficient is a Riemann sum for
J(t)=integral_0^1 exp(its)ds, with error at most pi/Q0.
Using the root-value identity therefore proves the uniform bound

    sup_{|t|<=pi}|F_B(t/Q0)/k-J(t)|
       <= pi/Q0+2(1+log Q0)/sqrt(k) ->0.               (2)

This is a finite DFT identity, not a sampling approximation to the
continuous-circle theorem. No MZ inequality or CLT is needed.

For the retained subset, the prefix sums of
1_{i retained}-3/4 have magnitude less than1. Summation by parts
and total variation <=|t| give

    |F_B'(t/Q0)/k-(3/4)F_B(t/Q0)/k|
       <=(1+pi)/k                                   (|t|<=pi).

Consequently, uniformly on this compact interval,

    D_1(t/Q0)/k^2 -> G(t),
    D_2(t/Q0)/k^2 -> (9/16)G(t),
    G(t)=(sin(t/2)/(t/2))^2,  G(0)=1.                (3)

The minimum of G on [-pi,pi] is 4/pi^2>2/5.
Writing m0=(1/(2*pi))integral_{-pi}^pi G(t)dt, the elementary
bound sin(u)/u>=1-u^2/6 gives G(t)>=1-t^2/12, hence

    m0>=1-pi^2/36>13/18,
    (1+9/16)m0 >325/288>1.                         (4)

All errors in (3) can be bounded from (2) and the displayed
summation-by-parts estimate. Thus the eventual assertions below
have effective thresholds, even though no threshold was optimized.

## 4. Two fronts exceed the reference's entire mass

On the circle define

    I={x: dist(x,2*pi*Z)<=pi/Q0},
    E_1=I,
    E_2={x:Lx modulo 2*pi belongs to I},
    E=E_1 union E_2.

Both E_i have normalized measure 1/Q0. Since L/Q0 is an integer,
I spans exactly L/Q0 periods of the periodic indicator 1_I(Lx).
Thus the overlap has the EXACT measure

    |E_1 intersect E_2|=1/Q0^2.                      (5)

An O(1/L) boundary error would also suffice, but is unnecessary.

Equations (3) and the global bounds D_1>=-k, D_2>=-h show that,
for all sufficiently large k,

    D>=k^2/10 on E,
    |E|<=2/Q0<=4/k^2.

The two front integrals satisfy

    integral_{E_1}D >= integral_I D_1-h/Q0,
    integral_{E_2}D >= integral_I D_2-k/Q0.

By (3), their respective principal terms tend to m0 and
(9/16)m0. Since D<=2n everywhere, (5) bounds double counting
by 2n/Q0^2=o(1). Consequently

    liminf integral_E D >=(25/16)m0>325/288.

In particular, for all sufficiently large k,

    integral_E D>=17/16,
    integral_E 1/D<=40/k^4.                         (6)

These statements use the actual all-circle functions. A sampled
minimum, a grid convergence assertion, and statistical independence
between the blocks do not enter the proof.

## 5. Uniform lower bound for EVERY admissible averaged reference

Let p be ANY finite symmetric PD profile in [0,1], p_0=1, with
sum_{j>0}p_j=n. Its polynomial

    P=1+D_p

is nonnegative and has mean1. Orthogonality and the coefficient
conditions give, for q=D-D_p=D+1-P,

    Q=2[n+sum p_j^2-2 sum_{a in A}p_a]<=4n.

Apply (1) with b=1 and (6). Here sigma>=1/16, so

    H=integral Dq^2
      >=k^4/10240-4Kn
      >=k^4/10240-8k^3.                             (7)

Since n~25k^2/32, the right side divided by n^(3/2) tends to
infinity. This lower bound holds for ALL admissible profiles,
uniformly over their degrees and over their selected coefficients.
It refutes the exact averaged peak-one mass-n PD reference target
for every proposed absolute C.

In fact, the same argument excludes any nonnegative mean-one
measurable P with ||D+1-P||_2^2<=beta*n, for each fixed beta:
replace -4Kn by -beta*Kn. PD and coefficient conditions were
used only to obtain the automatic beta=4 norm bound.

Convex averaging or randomizing admissible references cannot repair
the obstruction. Their average is still a nonnegative mean-one
reference, and remains an admissible profile if each input was
admissible. The lower bound applies to the average itself. Also,
H+KQ=integral(D+K)q^2 is convex, so averaging does not evade the
positive-front resource deficit through the signed objective.

## 6. Existence input and interpretation

The classical existence input was also checked in the primary research
paper [Meszaros, Ronyai and Szabo, Section1.2, p3](https://arxiv.org/pdf/1908.05591),
which states the cyclic parameters and the trace-zero construction.
The original AMS-hosted Singer PDF returned403; it was not treated as
read. The elementary argument below supplies the needed construction.

There are infinitely many needed perfect difference sets: take
finite fields F_(s^3) over F_s with s=2^r, quotient their cyclic
multiplicative groups by F_s^*, and let B consist of the classes
whose representatives have trace zero. The quotient order is
s^2+s+1, and the trace-zero plane contains s+1 projective points.
For any nontrivial quotient element, the original plane and its
multiple are distinct two-dimensional subspaces of a three-
dimensional vector space, with a one-dimensional intersection.
This gives exactly one ordered representation of each nonzero
difference. Distinctness of the planes follows from nondegeneracy
of the trace pairing: in degree3 and characteristic2, Tr(1)=1,
so for u!=0 one can test against u^(-1). This recovers precisely
the cyclic (s^2+s+1,s+1,1) parameters used above.

The weighted Fejer escape is not being smuggled into this proof.
It admits P=1+D_w with mean1 and zero residual, and has no
contradictory excess front mass of the displayed kind. The present
supports are genuinely Boolean; they deliberately combine two
exceptional fronts whose total mass exceeds the reference budget.
Likewise, the earlier lacunary-difference IPD obstruction is not
being enlarged here: the new failure is an averaged mixed-cost
lower bound, not an L-infinity tail argument.

**Discriminating finite certificate.** On one chosen support, certify
D>=eta>0 on E, integral_E D>1+delta, the overlap or |E|, and the
global K upper bound. Then (1), or the weaker bound
delta^2*eta/|E|-4Kn, certifies a lower bound simultaneously for
EVERY admissible reference. Positivity of a finite lower bound is
not required for the asymptotic theorem (7); it is only a diagnostic
of the finite size. No such finite run was performed by the advisor.

**Decision.** Stop the peak-one PD averaged-reference target as a
universal sufficient architecture. Both uniform discrepancy and the
exact averaged surrogate are now refuted, by different Boolean
mechanisms. The P73 variance/coupling corollary remains true, but
does not establish usefulness of the restricted residual class.
Return the primary effort to arbitrary signed witnesses / OP140,
which do not impose a nonnegative reference of fixed total mass;
retain direct negative-Rayleigh alternatives and the independent
all-circle construction track. Full Chowla and L25 remain OPEN.

Status: paper counterexample theorem, checked independently against
the lead's two-front derivation. No Lean/kernel-checked proof,
external scrutiny, new computation, or GPU expenditure is claimed.

## 7. Corollary: every absolute bounded reference mean also fails

Subsequent advisor audit, 2026-10-21. The lead proposed the following
extension; the dilation, overlap, budget, and uniform quantifiers
check out. One normalization correction: the ratio limit below is
for the certified budget Kbar, not necessarily the actual minimum K.

**Corollary.** Fix B>=0 and beta>0. There is a family of genuine
Boolean supports A_m, with n_m->infinity and K_m<=2sqrt(n_m),
such that the following holds uniformly for EVERY measurable
P_m>=0 with mean b_m in [0,B] and

    q_m=D_m+b_m-P_m,    integral q_m^2<=beta*n_m:

    integral D_m q_m^2 / n_m^(3/2) -> infinity.

More precisely, the proof gives a lower bound independent of P_m
that tends to infinity. This excludes each absolute bounded-mean,
bounded-norm nonnegative-reference repair, without Fourier or
coefficient restrictions.

Choose a fixed integer r such that r*m0>B+2delta for some delta>0,
where m0>13/18 is the central front mass above. For integer
m>4(r-1), take r full Singer blocks with

    k_i=2^(m-4i)+1,   Q_i=k_i(k_i-1)+1,   0<=i<r.

Let A_i be their canonical positive integer difference sets. Define

    L_0=1,    L_j=product_{i<j}(L_i Q_i),
    A_m=union_{i=0}^{r-1} L_i A_i,
    n_m=(1/2)sum_i k_i(k_i-1),
    Kbar_m=sum_i k_i.

The new block's minimum frequency is at least L_j, which exceeds
the maximum frequency in every earlier block. Thus the union is
Boolean and its cardinality is the displayed sum. The square
identities give K_m<=Kbar_m. With k_0 as the scale,

    Kbar_m/(2sqrt(n_m))
      -> (sum_{i<r}16^(-i))/sqrt(2sum_{i<r}256^(-i))
      < (16/15)/sqrt(2) <1.

Therefore the actual low-K hypothesis holds eventually.

Set E_i={x:L_i x modulo 2*pi is in [-pi/Q_i,pi/Q_i]}.
For i<j, L_j/L_i is an integer divisible by Q_i, directly from
the product defining L_j. Each E_i component spans an integer
number L_j/(L_i Q_i) of periods of 1_{E_j}. Consequently

    |E_i intersect E_j|=1/(Q_i Q_j)                 (exactly).

The full-block front limit proved above applies to each of the
finitely many blocks. Since k_i/k_0->16^(-i), the union E has

    D_m>=c_B*k_0^2 on E,
    |E|<=C_B/k_0^2,
    integral_E D_m>=r*m0-o(1)>B+delta.

For the last bound, each block contributes m0-o(1) on its own
front; all other blocks cost at most Kbar_m/Q_i=O_B(1/k_0)
there. Double counting costs at most
2n_m*sum_{i<j}1/(Q_i Q_j)=O_B(k_0^(-2)). All constants are
allowed to depend on the fixed B, through r.

For every b_m in [0,B], the budget lemma has

    sigma=integral_E(D_m+b_m)-b_m>=delta,
    integral_E1/D_m<=C'_B/k_0^4.

It follows uniformly over the stated P_m that

    integral D_m q_m^2
      >=c'_B*k_0^4-beta*Kbar_m*n_m
      >=c'_B*k_0^4-O_{B,beta}(k_0^3).

Since n_m is asymptotic to a positive constant times k_0^2,
the corollary follows. A bounded mean may depend on m and on the
support; it is still covered. Allowing the mean to grow without
bound is a different architecture and is not excluded here.

The lead additionally reports one Arb-certified p127 packet check:
the full k=128 block and its h=96 subset give n=12688,
M<=112<sqrt(n), front mass lower 1.165974519, and front height
lower 3167.694262769. Independent midpoint-ball checks reportedly
confirmed its front integrals. I did not rerun those jobs. This is
finite evidence for the packet premises; no positive finite mixed-
cost bound or universal Chowla conclusion is inferred from it.

Status: the bounded-mean extension is a paper corollary checked by
the advisor, with no new computation, external scrutiny, or Lean
formalization. Retain arbitrary signed q / OP140 rather than
replacing reference mean1 by another absolute bounded mean.
