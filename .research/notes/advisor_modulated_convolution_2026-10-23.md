# Modulated convolution: the quadratic floor is genuinely sharp

2026-10-23. Sole internal AI advisor. Independent paper derivation and
audit of the parent's triangular-profile and bounded-dependency rounding
arguments. Read-only repository review and primary-source verification;
no research computation, VM operation, GPU, extra agent or outreach.
Shared Dirichlet remains running. No Lean/kernel verification or external
novelty claim. Full Chowla remains open.

## 1. Exact target and the decisive result

For a finite nonempty set A of distinct positive integers, put S=+/-A,

    D(x)=sum_(s in S)exp(isx)=2f_A(x),
    K=-min_circle D=2M(A),
    h_t(x)=2(1+sin(tx))*D(x), t in S,
    G_t=h_t*h_t,

where convolution uses probability Haar measure dx/(2pi).
The candidate G_t>=-16K, or any universal subquadratic replacement
for the usual-16K^2, is FALSE.

**Paper theorem, using the classical Spencer discrepancy input below.**
For every integer Q divisible by8 and sufficiently large, there is a
genuine Boolean A_Q subset{1,...,Q-1}, containing t=Q/4, such that

    |A_Q|=Q/2+O(sqrt(Q)),
    sqrt(Q)/20 <= K_Q <=500sqrt(Q),
    G_t(-4pi/Q) <= -Q/25 <= -K_Q^2/6250000.     (1)

The conservative constants and Q>=10^12 suffice for the proof given
here, assuming the cited square-matrix discrepancy constant6. The
threshold is an existential proof threshold, not a proposed job size.
All constants are absolute and the K upper bound is over the ENTIRE
circle. Thus no universal floor-o(K^2) can hold, even on a bounded-ratio
Boolean integer family. In particular every power K^(2-delta), delta>0,
and every fixed linear constant are ruled out.

This is an obstruction to the proposed intermediate, not a counterexample
to Chowla: K is itself of square-root cardinality order. It supplies no
Epoch solution and no new unrestricted lower-bound exponent.
In particular n=Theta(K^2) along this family. It does not refute a
different floor whose hypotheses require a genuinely spiky regime
n/K^2 tending to infinity; such a conditional statement would need
its own proof and would retain a possible role in the universal problem.

## 2. Exact Boolean identity and normalizations

Write a_s=1_S(s), including a0=0. The Fourier coefficients of h_t are

    c_s=2a_s+i(a_(s+t)-a_(s-t)).

Since a_s^2=a_s,

    c_s^2=4a_s-a_(s+t)-a_(s-t)+2a_(s+t)*a_(s-t)
                          +4i*a_s*(a_(s+t)-a_(s-t)).

Define

    E_t=(S+t) intersect(S-t),
    A_t=S intersect(S+t),
    B_t={s in S:s-t in S,s+t not in S},
    F_U(x)=sum_(s in U)exp(isx).

The resulting exact identity is

    G_t=(4-2cos(tx))*D+2F_Et+8 Im F_Bt
       =(4-2cos(tx))*D+2F_Et+8 Im F_At.         (2)

The imaginary parts agree because A_t intersect(-A_t) is symmetric.
In particular E_t may contain0; its constant contribution is canceled
by that of-2cos(tx)D. The mean of h_t and of G_t is0.

As h_t>=-4K and has mean0,

    G_t+16K^2=(h_t+4K)*(h_t+4K)>=0.             (3)

This is the generic lower floor used later to obtain the lower bound
on the ACTUAL K of the constructed sets. Replacing Fourier squares
c_s^2 by absolute squares would destroy(2) and is not done.

## 3. A negative quadratic expectation from the triangular Boolean profile

Let Q be divisible by8, t=Q/4. Initially take independent Bernoulli
variables X_a, 1<=a<Q, with p_a=1-a/Q, and force X_t=1. Extend
symmetrically by a_(+/-a)=X_a and a0=0. For the unforced profile,

    E D=Fejer_Q-1>=-1.

Forcing X_t changes the mean by(1/2)cos(tx), hence its global
lower bound remains-3/2. At x0=-4pi/Q, the mean is exactly-3/2.
The unforced Fejer kernel vanishes there, and cos(tx0)=-1.

Put p(v)=(1-|v|)_+ and

    L_s(v)=p(v+s)*p(v-s), 0<=s<=1/2.

For v>=0 its two pieces are

    (1-s)^2-v^2,          0<=v<=s,
    (1-v)^2-s^2,          s<=v<=1-s.

An integration by parts, keeping the derivative jumps, gives at y=4pi

    integral_R L_s(v)*exp(iyv)dv
       =[(4-12s)cos(ys)+12sin(ys)/y]/y^2.       (4)

This formula is asserted at y=4pi, not at arbitrary y. At general y
there are additional endpoint terms involving y(1-s). In particular

    Lhat_(1/4)(4pi)=-1/(16pi^2),
    Lhat_(1/8)(4pi)=3/(16pi^3).                 (5)

The E_t product profile is L_(1/4). The A_t product profile is
L_(1/8) shifted by t/(2Q)=1/8, which at x0=-4pi/Q gives phase-i.
Therefore(2) has expectation

    E G_t(x0)=-c0*Q+O(1),
    c0=1/(8pi^2)+3/(2pi^3)>3/50.               (6)

Equivalently evaluate G_(-t) at+4pi/Q. Using G_t at the positive
angle instead would reverse the odd term and give the WRONG sign.

### Explicit bounded errors in(6)

Symmetry destroys Bernoulli independence only at s0 for E_t and
at s=t/2 for A_t; zero-frequency endpoints add at most two more
exceptions each. Before forcing, the error from each intersection's
independent product profile is at most2 in absolute value. Forcing X_t
can change at most three E_t products and four A_t products. The
respective expectation errors are therefore at most5 and6.

For f(v)=L_s(v)exp(i4pi*v), total variation is at most

    TV(L_s)+4pi*integral L_s<=2+8pi<28.

A grid Riemann sum with spacing1/Q, also on the shifted grid, differs
from Q times the integral by at most this variation. Thus the total
absolute error in(6) is bounded by

    9+2*(28+5)+8*(28+6)=347<400.

All these are uniform in Q. The bound c0>3/50 follows already from
pi<22/7: the two summands exceed2597/42592>3/50 in total. Hence

    E G_t(x0)<=-(3/50)*Q+400.                   (7)

## 4. Verified discrepancy dependency and arbitrary fractional rounding

The only discrepancy import is the square REAL-matrix bound

    |A_ij|<=1, A of size m by m
          ==> some signs epsilon have ||A epsilon||infinity<=6sqrt(m).

I directly inspected [Larsen, arXiv2207.03268v2, PDF page2,
Introduction](https://arxiv.org/pdf/2207.03268v2), which states this
form of Spencer's classical result. The former author-site URL in
the forced-plateau note returned404 during this audit; the versioned
arXiv primary text was accessible. No algorithmic guarantee from
Larsen's later theorems is used. This is the SAME dependency as the
previous forced-plateau rounding argument.

Here is a complete derivation of the needed fractional consequence.
For an m-row real matrix with entries at most1 and at most m columns,
every column restriction can be padded by zero columns to m by m.
Thus its hereditary sign discrepancy is at most d=6sqrt(m).

For a dyadic vector p in[0,1]^n, at denominator2^k change only odd
coordinates by +/-2^(-k), choosing the signs with row error at most
d/2^k. This halves the denominator, never changes an integral
coordinate, and stays inside[0,1]. Summing levels costs less than d.
For arbitrary p, approximate by dyadic vectors and take a subsequence
of the finitely many resulting Boolean vectors. Continuity gives

    exists X in{0,1}^n with ||A(X-p)||infinity<=6sqrt(m). (8)

There is no denominator penalty, extra logarithm or assumption that
p=1/2. Forced coordinates remain fixed. No rectangular theorem or
unproved multi-choice discrepancy assertion is required.

## 5. Why eight stages control the nonlinear observable

At the fixed angle x0, G_t is a real quadratic function of the X_a.
Every monomial comes from indices s,s+t,s-t after identifying a with-a.
Its interactions remain within the components under a->|a+/-t|.

For Q=4t with t even, the generic component, indexed by
1<=r<t/2, is

    {r+j*t,(t-r)+j*t:j=0,1,2,3},

of size8. The exceptional components are the multiples{t,2t,3t}
and the four indices congruent t/2 modulo t. Thus each component
has at most8 bits. Removing the forced bit cannot enlarge it.

Order each component and fix one bit per component in each of at
most eight stages. Given all previous fixed bits, define conditional
expectations using the ORIGINAL independent probabilities on the
unfixed bits. With only one current-stage variable in any component,
conditional E G_t is affine in all current-stage bits. There are no
cross-component monomials. The conditional slope at a bit is bounded
by its maximum pointwise bit-flip difference.

Changing X_a affects c_s^2 at at most six frequencies s in
{+/-a,+/-a+t,+/-a-t}. Each squared coefficient has magnitude at
most5, so the total bit-flip difference of G_t(x0) is at most60.
Conditional slopes are therefore bounded by60 uniformly, regardless
of the earlier deterministic choices.

Use m_rows=16Q+1 rows at each stage: the Fourier grid
x_j=2pi*j/(16Q), j0,...,16Q-1, and ONE conditional-observable row.
Normalize Fourier slopes2cos(a*x_j) by2 and the G slope by60.
All entries are at most1, so(8) applies by zero padding. One stage
changes the conditional D-grid means by at most12sqrt(m_rows)
and the conditional G expectation by at most360sqrt(m_rows).

Summing all eight stages gives

    max_grid |D_final-E_initial D|<=96sqrt(m_rows),
    |G_final(x0)-E_initial G(x0)|<=2880sqrt(m_rows). (9)

The conditional drifts telescope to the actual final observable.
This does NOT condition on any sampled future bits: future product
laws are only used to define the conditional expectations. The
rounding choices use these fixed probabilities and past choices.
Consequently no independence assumption has been silently carried
over to the final dependent Boolean set.

This argument is a general bounded-component rounding lemma: linear
statistics and a bounded-difference sum of component observables can
be controlled simultaneously in O(sqrt(number of rows)), with a
constant depending on the maximum component size. It is a proved
reduction to linear discrepancy, not a conjectured nonlinear
discrepancy theorem.

## 6. All-circle certification and quadratic sharpness

Let R=D_final-E_initial D. It has degree at most Q-1. Bernstein's
inequality at the16Q-point grid gives

    ||R||infinity <=96sqrt(16Q+1)
                         +(pi/16)*||R||infinity.

Since sqrt(17)<33/8 and pi<22/7,

    ||R||infinity<493sqrt(Q).

The initial mean is everywhere at least-3/2. Thus the ACTUAL
all-circle negative minimum satisfies

    K_Q<=500sqrt(Q).                             (10)

The grid point0 in(9) also gives |A_Q|=Q/2+O(sqrt(Q)). All final
coefficients are exactly0/1, X_t remains1, and every frequency is
a distinct positive integer below Q.

Combining(7),(9), with sqrt(16Q+1)<(33/8)sqrt(Q), yields

    G_t(x0)<=-(3/50)*Q+400+11880sqrt(Q).

For Q>=10^12 this is below-Q/25. Finally the generic bound(3)
forces K_Q>=sqrt(Q)/20. Equations(1) follow. In particular

    -G_t(x0)/K_Q^2>=1/6250000.

Because K_Q tends to infinity, EVERY proposed universal error term
o(K^2) fails along this family, including all positive power savings.
The argument proves existence for each sufficiently large multiple
of8. Exhaustive finite selection with slack in the algebraic grid
rows can make the intermediate counterfamily effective, although
no practical generator or Epoch interface is claimed or needed.
The discrepancy-selected sets are not Monte Carlo outputs.

## 7. Independent finite-group check on positivity/projection algebra

There is also a simple exact algebraic adversary to any group-agnostic
PSD/Markov proof of the proposed linear floor. This is a MODEL check;
the integer proof above does not need a group-to-integer transfer.

For an odd prime p, let d be a nonsquare and

    Q(x)=x1*x2+x3^2-d*x4^2, S={x in F_p^4:Q(x)!=0}, t=e3.

Crucially Q(t)=1, so t is INSIDE S. The quadratic-character
calculation recorded in P20 gives ACTUAL K=p, with nontrivial
spectrum-p or p(p-1). At the character exp(2pi*i*2nu*x3/p),
D=-p. The two zero-quadric intersections needed in(2) lie at
x3=0 and x3=1/2, respectively. Both have N=p(p-1) points:
the equations x1*x2=d*x4^2-1 and d*x4^2-1/4 never have zero
right side, since d is nonsquare.

For phi=2pi*nu/p, inclusion-exclusion in(2) gives EXACTLY

    G_t=(2+8sin(phi))*N
                 -p*[4+2cos(2phi)+8sin(2phi)].

Choose nu nearest3p/4. Then sin(phi)=-cos(pi/(2p))<-3/4.
The leading coefficient is below-4 and the remaining bracket has
absolute value at most14. For p>=11, G_t<=-2p^2. Thus positivity
and exact Boolean convolution idempotence alone cannot prove the
linear floor, even with an admissible modulation frequency.

## 8. Relation to the old record and the required strategic pivot

The earlier bedert_avg note Section6 recorded small linear-looking
values on a limited Singer selection. The later P19 report already
recorded finite quadratic-sized negative values and a heuristic
macroscopic-overlap explanation. I inspected those records. I have
not independently reconstructed admissible-t membership for every
old point, and do not upgrade the old heuristic limit into a proof.
The present triangular construction forces the frequency t and
proves the entire asymptotic order with its all-circle K bound.

The Spencer mechanism is shared with the existing forced-plateau
route, but the new step is controlling a NONLINEAR local observable
at the same time as the entire Fourier discrepancy. This validates
the modulation-floor counterfamily; it is not another proposed
improvement to a settled Sidon M-bound.

Discontinue the universal linear/subquadratic h_t*h_t floor. No
constant optimization or larger successful-control sweep can rescue
it. Improving this one source would not by itself have improved the
universal exponent, because the pure-positive truncation/Q2 sources
in P14 remain separate; they have not been proved small here.

Keep exact identities(2),(3), the bounded-component rounding tool,
and the independent all-circle construction track. A continuation
through P14 would need its actual joint non-saturation or intermediate-
height structure, with all t and all remainder terms retained, rather
than a better pointwise convolution floor. Those are existing open
targets, not established by naming them. No full Chowla conclusion,
new unrestricted exponent or kernel verification is claimed. The
separate finite experiment below was run by the parent, not the advisor.

## 9. Read-only audit of the single finite pilot and independent verifier

After completing the paper argument, I read the full producer
`src/modulated_triangle.py`, independent verifier
`src/modulated_triangle_verify.py`, and the saved pilot/verification
artifacts in `.research/experiments/modulated_triangle_2026-10-23/`.
I did not execute either source or perform a duplicate computation.

The producer uses Q=65536, seed20261023, independent probabilities
1-a/Q, and forces t=16384. Its saved support has n=32787 distinct
positive frequencies, maxA=65046, and the required t in A. It evaluates
G_(-t)(4pi/Q), which is equivalent to the sign convention in(1).
The exact integer coefficients are c_s^2, not |c_s|^2. Its separately
constructed shifted-set coefficient identity has the correct imaginary
sign for the negative modulation. A 192-bit ball Horner evaluation and
an independently folded ball DFT agree on the point enclosure.

The verifier reconstructs the actual sets

    E=(S+t) intersect(S-t), At=S intersect(S+t),
    G_(-t)(4pi/Q)=6D+2Re(F_E)-8Im(F_At).

It compares its 192-bit enclosure with the producer's saved rational
endpoints. The recorded interval encloses approximately

    G=-4323.555399930924.

The producer's all-circle certificate evaluates f on a 16Q-point
96-bit Arb DFT grid and checks every ball above -316. At a true global
minimum the derivative is zero, so the nearest grid point gives a
Taylor error at most pi^2*sum(a^2)/(2*(16Q)^2). Its rational replacement
242*sum(a^2)/(49*(16Q)^2) is valid from pi<22/7. The resulting saved
upper bound is

    M <=11351778564305199/26938034880512
      =421.4033657116358... .

The second method centers the cosine polynomial by its exact forced
triangular expectation. This expectation is at least -3/4. The
verifier's 96-bit Arb DFT bounds the absolute grid discrepancy by337;
Bernstein's derivative inequality then gives an all-circle multiplier
less than56/45. It therefore independently obtains

    M <=3/4+(56/45)*337=75623/180
      =420.1277777777778... .

These are two different mathematical all-circle remainder arguments,
using the same Arb DFT backend; they are not independent arithmetic
implementations. The shifted-set point reconstruction is also distinct
from the producer's local Fourier-coefficient construction. Both saved
jobs report PASS. The rational proof-constant checks are corroborations
of the paper inequalities, not an implementation of Spencer rounding.

The finite example is a Bernoulli mechanism check. It is NOT one of
the discrepancy-selected asymptotic sets, does not establish a finite
counterexample to the particular -16K floor from these bounds, and
does not lower the certified normalized cosine minimum toward zero.
The theorem in Sections1-6 proves the universal subquadratic-floor
failure independently of this finite experiment. No further pilot,
support sweep or GPU computation is required for that conclusion.
