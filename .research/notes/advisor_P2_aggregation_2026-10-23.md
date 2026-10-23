# Boolean row aggregation and an explicit counterexample to the full-negative closure

2026-10-23. Sole internal AI advisor. Independent paper derivations,
read-only research-record review and this assigned note only. No
research computation, VM action, GPU, extra agent or outreach. Shared
Dirichlet remains on. No Lean/kernel verification or external priority
claim. The full Chowla goal and original odd P2 remain unresolved.

## 1. The exact candidate and the result

For a finite nonempty Boolean A, n=|A|, F=sum_A z^a, f=Re F,
assume ACTUAL M=-min_circle f<=sqrt(n). Put lambda=2sqrt(n),
p=(lambda+F)^(-1), T=<F,p^2>, y=-lambda*T, C2=<F^2,p>,
t=<F,F^2>, D=max(A), and

    K=(F^2+lambda*conjugate(F))*p^2,
    k_j=K_(-j)=lambda*sum_(a in A,a>=j)[z^(a-j)]p^2,
    Nminus=sum_(j=1)^D k_j^2.

The proposed full-negative sufficient criterion for t>0 was

    Nminus+(5lambda/(2t))*C2^2 >= y/2-y^2.       (FN)

It retains all negative Fourier coefficients, unlike the already
refuted constant-plus-conjugate(F) projection. It is STRONGER than
original P2, not an equivalent unrestricted certificate problem.

This attempt proves a conditioning-free multi-row lower bound,
but also gives a complete PAPER BOOLEAN COUNTEREXAMPLE to(FN):

    A={1,2,3,4,5,6,7,8}.

Its actual all-circle M is at most11/4<sqrt(8). Explicit finite
inverse formulas and rational bounds prove the reverse gap

    y/2-y^2-[Nminus+(5lambda/(2t))*C2^2]
                          >449/62500>0.         (1)

This kills(FN) as a universal sufficient step. It does NOT refute
P2 or S0: their full inverse norm includes the positive-frequency
phase energy discarded by(FN).

## 2. A genuine conditioning-free multi-row Boolean bound

Let n>=2,m=min(A)<D. For the terminal frequency packet

    E=A intersect(max(m,D-m),D],

define the integer local counts

    r_a=sum_(b in A,b>=a) 1_A(m+b-a), a in E.

Each r_a>=1, since b=a contributes the occupied frequency m.
The formal inverse-square coefficients satisfy

    [z^0]p^2=lambda^-2,
    [z^j]p^2=0 for0<j<m,
    [z^j]p^2=-2*1_A(j)/lambda^3 for m<=j<2m.

For a in E, D-a<m. Thus the exact row identities are

    k_a=1/lambda,
    k_(a-m)=1_A(a-m)/lambda-2r_a/lambda^2.       (2)

For the second formula every positive relevant coefficient degree
is below2m, so no higher convolution term was suppressed. The
upper coordinates lie in(D-m,D], and their shifted partners in
(D-2m,D-m]. They are positive and all row pairs are disjoint.

Let Rperp=||K-proj_(span{1,conjugate(F)})K||2^2.
For an absent partner a-m, its off-support squared coefficient
alone gives4r_a^2/lambda^4. For an occupied partner, the two
selected coefficients differ by2r_a/lambda^2, so their squared
distance from any common projection coefficient is at least
2r_a^2/lambda^4. Disjointness permits summation without any
condition-number or inverse-matrix estimate:

    Rperp >= (2/lambda^4)*sum_(a in E)r_a^2,     (3)

with factor4 instead of2 on absent partners. Also

    Nminus>=|E|/lambda^2.                        (4)

Equation(3) improves the old one-pair bound whenever several such
rows or larger local counts are present. It is genuinely Boolean:
both the leading and the minimum occupied amplitudes are exactly1.
It does not control all rows of an arbitrary support.

The limitation is concrete inside actual low M. Take no-carry
Sidon differences of B={1,q,...,q^(k-1)}, q=k+1,k>=3. They have
n=k(k-1)/2 and M<=k/2<=sqrt(n), while

    m=q-1, D=q^(k-1)-1,
    E={D}, r_D=1.

Indeed the next largest difference is D-m, exactly the excluded
lower endpoint; no other difference enters(D-m,D]. Thus this
terminal-packet argument can remain only the old one-pair bound
along an arbitrarily large actual-lowM Boolean family.

If |E| is a fixed positive fraction of n, (4) is useful, but that
short-window branch already has a P9 independent-star bound:
pairwise differences of E are below min(A). For example |E|>=n/4
implies Nminus>=1/16, which dominates y/2-y^2<=1/16 and proves
(FN) on that branch. This is a restricted reciprocal-certificate
consequence, not a new universal M bound. No universal large
terminal packet or extensive sum in(3) is assumed.

## 3. A rigorous all-circle premise for the eight-frequency counterexample

For A=[1,8], the Dirichlet identity gives

    1+2f_A(x)=sin(17u)/sin(u), u=x/2.

By evenness and2pi periodicity restrict x to[0,pi], hence
u in[0,pi/2]. At u=0 take the continuous value17.

For0<u<=pi/17, the ratio is nonnegative. For
pi/17<=u<=pi/14,

    sin(17u)>=-(17u-pi)>=-3u.

Also u<1/4, so sin(u)>=u-u^3/6>=95u/96. Consequently

    sin(17u)/sin(u)>=-288/95>-9/2.

For pi/14<=u<=pi/2, sin(u)>=sin(pi/14)>2/9, so the ratio
is again greater than-9/2. To check the strict sine bound using
only rational inequalities, 3.14<pi<22/7 gives

    pi/14>157/700, pi/14<11/49,
    (11/49)^3/6<1/500,
    sin(pi/14)>157/700-1/500=389/1750>2/9.

Therefore f_A>=-11/4 on the WHOLE circle, and

    M(A)<=11/4<sqrt(8), since121/16<8.            (5)

No sampled minimum or prior numerical interval example is needed.

## 4. Exact finite inverse formulas

Write

    lambda=4sqrt(2), u=1/lambda=sqrt(2)/8,
    r=1-u, R=r^8, t=28.

The formal comparison function for the infinite interval is

    p_infinity=(1-z)/[lambda*(1-r*z)].

For F_8=z+...+z^8,

    p_8=(1-z)/[lambda*(1-r*z)-z^9]
       =p_infinity+u^2*z^9*(1-z)/(1-r*z)^2+O(z^18).

Thus p_8^2 agrees with p_infinity^2 through degree8. Taking
partial sums of the latter coefficients gives, for s=0,...,7,

    k_(8-s)=u*r^(s-1)*[1-(s+1)u],               (6)

where s=0 simplifies to u. The selected inverse-square sum is

    y=u*[1-r^7*(1-9u)].                          (7)

For C2, the coefficients of F_8^2 form the triangle j-1 for
2<=j<=9 and17-j for10<=j<=16. The p_infinity part sums to
-r(1-R)^2. The displayed correction in p_8 sums by telescoping
to1-(1+8u)R. Hence exactly

    C2=u+[1-10u]*R-r*R^2.                        (8)

Equations(6)--(8) determine every quantity of(FN) in Q(sqrt(2)).
They use the actual cardinality calibration, not an oversized
lambda and not occupied-count normalization for weighted data.

## 5. A finite rational proof that(FN) fails

The elementary bounds

    .176<u<.177, .823<r<.824,
    .20<R<.22, .24<r^7<.27

are strict rational inequalities. The first follows by squaring
8*.176 and8*.177 around2. For R, use .67<r^2<.68 and
square twice; division by .823<r<.824 gives the r^7 bounds.
Equation(7) now gives

    .20<y<.206<1/4,
    y/2-y^2>.20/2-.20^2=.06.                    (9)

For example the unrounded y bounds are
.176*(1+.24*.584)=.20066816 and
.177*(1+.27*.593)=.20533947. Equation(8) gives

    -.04<C2<0.

For its upper endpoint use
.177-.76*.20-.823*.20^2=-.00792<0;
for its lower endpoint use
.176-.77*.22-.824*.22^2=-.0332816>-.04.

For completeness the following rational upper bounds on the
individual squares in(6) give an elementary Nminus enclosure.
For s>=1, use u^2<.031329 and the upper bounds
1,.68,.47,.32,.22,.15,.10 for r^(2s-2), respectively
(the first is equality and the others are strict), and
|1-(s+1)u|<.648,.472,.296,.120,.062,.239,.416.

| s | Upper bound for k_(8-s)^2 |
|---|---:|
| 0 | .031330 |
| 1 | .013160 |
| 2 | .004750 |
| 3 | .001300 |
| 4 | .000150 |
| 5 | .000027 |
| 6 | .000270 |
| 7 | .000550 |

Their sum is .051537<.052. These decimal constants are exact
rationals, not floating-point outputs. Finally

    5lambda/(2t)=5/(56u)<.51,
    Nminus+(5lambda/(2t))*C2^2
         <.052+.51*.04^2=.052816<.06.            (10)

Subtracting(10) from(9) proves(1). Thus the stronger finite
closure is false on an explicit genuine Boolean support within
the ACTUAL low-M premise. No research computation is needed
for the conclusion. An independent exact quadratic-field check
by the parent is corroboration of this paper proof.

## 6. What is falsified, and the exact mathematical pivot

Define

    Gminus=[y^2+Nminus+2y]/5,
    Eplus=||P_(strictly positive frequencies)K||2^2.

The already proved phase identity gives

    g=Gminus+Eplus/5,
    2tH0-C2^2=Psi_minus-(2t/(5lambda))*Eplus,
    Psi_minus=(2t/(5lambda))
                 *(y/2-y^2-Nminus)-(C2)^2.       (11)

For A=[1,8], Psi_minus>0 by(1). Consequently a proof of original
P2 on even this small Boolean support cannot simply discard the
positive-frequency phase energy. Whether original P2 holds is a
different, full-norm question. No P2 or S0 falsification follows
from the finite counterexample above.

The positive phase coefficients that were omitted are explicitly

    K_j=[z^j](F^2*p^2)
             +lambda*sum_(a in A)[z^(a+j)]p^2, j>=1.

Their signed cross coupling is not controlled by retaining more
negative rows, applying a uniform Hankel norm, or repeating
successful finite examples. The first finite-projection closure
failed on n76; the entire negative closure now fails already on
n8. This is the required global review after two genuine closure
failures: stop promoting these projections to universal complete
witness arguments. Preserve the true norm identities and the
conditional branches already proved.

Any next derivation along P2 must keep this actual scalar positive
phase term and use new Boolean structure to control its interaction
with the selected coefficients. Equation(11) precisely records the
gap; merely restating its required lower bound is not a new route.
Unrestricted signed Rayleigh and the independent all-circle
construction programme remain alternatives; neither is blocked by
failure of this stronger two-plane criterion. No further projection
polishing or support sweep is authorized by this note.

Status: a proved multi-row auxiliary inequality and a rigorous
Boolean counterexample to a proposed unrestricted intermediate.
No universal exponent, full Chowla proof, counterfamily with
M/sqrt(n)->0, new computation or resource action by this advisor.

## 7. The local M-bound is already dominated by P9

The parent observed a sharper elementary spectral implication of
the SAME terminal packet E. I checked it independently. Both
E and E-m are independent in the A-difference graph, since each
has diameter<m=min(A), and the two vertex sets are disjoint.
The cross adjacency block, indexed by a,b in E, is

    B_(a,b)=1_A(m+b-a).

It is upper triangular: if b<a, its positive argument is below m.
Its row sums are r_a, because all b in A above a also belong to E.
The induced bipartite matrix has minimum eigenvalue-||B||, so P9
gives

    M>=||B||/2>=sqrt(sum_E r_a^2)/(2sqrt(|E|)).

The P9 star on E also gives M>=sqrt(|E|)/2. Multiplication yields

    M^4>=sum_E r_a^2/16.                         (12)

For comparison, the phase argument(3) with lambda=2M gives
|zeta|<=1, g<=1, h>=-g/2 and Rperp<=||K||^2<=3. Thus it
would only give M^4>=sum_E r_a^2/24. This choice lambda=2M
is solely for comparing auxiliary M-bounds; it does not silently
alter the fixed calibration in(FN). Equation(12) is stronger.

Therefore the row identities are useful exact information about
this inverse input, but their restricted M-bound is not a new
root theorem. Do not turn their conditioning-free summation into
a claim of a universal advance already supplied by P9.

## 8. Mathematical pivot: a global allpass captures positive scalar phase

After(FN) fails, the parent proposed a genuinely different
positive-tail test. I checked the exterior expansions and then
derived the complete allpass-power projection as follows.

Let W=lambda+F, Wrev(z)=z^D*W(1/z), and

    B=Wrev/W, a=1/lambda.

The actual low-M margin makes W zero-free on the CLOSED disk.
Every zero of Wrev is strictly inside. Thus B is analytic and
inner on the circle, with B(0)=a, and lambda>=2 makes0<a<1.
This is a global scalar function using the full denominator, not
an additional positive Fourier coordinate.

Since |B|=1 on the circle,

    <K,B>=mean(K/B),
    K/B=W/Wrev-2lambda/Wrev+lambda*z^(-D)/W.

The first two functions have convergent EXTERIOR Laurent series
on the circle, with constants1/lambda and0 respectively; the
last term has mean lambda*p_D. Consequently

    <K,B>=1/lambda+lambda*p_D.

The negative part of K is orthogonal to B, while K0=-y. Hence

    <K_+,B-a>=(1+y)/lambda+lambda*p_D=:v,
    ||K_+||^2>=v^2/(1-lambda^-2).                (13)

The new stronger finite sufficient candidate is(FN) with the
additional term v^2/(1-lambda^-2) on its left. It retains genuine
positive scalar phase. Its universal extension, even strengthened
by the complete cyclic floor(14), is subsequently REFUTED by
the exact n56 certificate in Section10. The bound itself remains
valid and its n8 recovery is unaffected.

There is a complete calculation for ALL powers of this same B.
For every j>=2, all denominators in

    K/B^j=W^j/Wrev^j-2lambda*W^(j-1)/Wrev^j
                    +lambda*z^(-D)*W^(j-2)/Wrev^(j-1)

are exterior analytic. Their constant terms are a^j,0,0.
Thus <K,B^j>=a^j and <K_+,B^j>=(1+y)*a^j for j>=2.
The strictly positive-frequency functions

    e_j=B^(j-1)*(B-a)/sqrt(1-a^2), j>=1,

are orthonormal. Indeed B is inner and mean(B^k)=a^k, and
expanding |B-a|^2 makes all distinct-index pairings zero.
Their K_+ pairings are

    v/sqrt(1-a^2), -p_D/sqrt(1-a^2), 0,0,... .

Therefore the FULL projection onto this allpass cyclic subspace
gives the finite bound

    ||K_+||^2 >= (v^2+p_D^2)/(1-lambda^-2).       (14)

Merely adding more powers of the SAME allpass cannot keep gaining:
all their remaining orthogonalized correlations vanish exactly.
The subspace is not asserted to exhaust K_+ or the full Rayleigh
problem. No universal conclusion follows by naming it complete
within its own cyclic span.

### Paper recovery of the eight-frequency counterexample

For A=[1,8], p_D=-u^2*r^7 and v=u*(1+y-r^7).
The rational bounds above give v>.16, k_8>.176 and
k_7=u*(1-2u)>.113. Hence even the first allpass term suffices:

    Nminus+v^2/(1-u^2)
       >.176^2+.113^2+.16^2=.069345>1/16
       >=y/2-y^2.                               (15)

Thus the new global positive-phase bound recovers S0 on this
same Boolean input without C2 or a full numerical inverse norm.
This is a proved FINITE recovery, not an inferred universal rule.

For weighted leading coefficient c_D instead of1, the actual
formula has B0=c_D/lambda and
v=c_D*(1+y)/lambda+lambda*p_D; the second numerator in(14)
is c_D^2*p_D^2. The geometric truncations have c_D tending to0,
so this floor degenerates rather than contradicting their positive
plane countermodel. Unit TOP amplitude matters, but the full
Boolean pattern has not yet supplied a universal bound.

## 9. Full scalar norm as an exact Boolean matrix, with its necessary scope

The parent also derived a useful exact finite representation of
the FULL norm. I checked the elementary reproducing-kernel proof.
Write W=sum_(j=0)^D w_j*z^j, with w0=lambda,wD=1 and
wj=1_A(j) otherwise. For0<=i,j<D put

    C_(i,j)=sum_(k=0)^min(i,j)
       [w_(i-k)*w_(j-k)-w_(D-i+k)*w_(D-j+k)].

For phi_j(z)=z^j/W(z), direct polynomial division gives

    [1-B(z)*conjugate(B(w))]/[1-z*conjugate(w)]
                  =sum_(i,j) C_(i,j)*phi_i(z)*conjugate(phi_j(w)).

Each phi_j is orthogonal to B*H2: pairing with B*z^m is the
constant of z^(j-m)/Wrev, an exterior series with strictly
negative powers when j<D,m>=0. The displayed kernel belongs
to span(phi). Hardy's Cauchy identity and that orthogonality
show it reproduces this span. Since the phi_j are independent,
their Gram matrix is C^-1. In particular

    C>0,
    ||p||2^2=(C^-1)_(0,0),
    g=lambda^2*(C^-1)_(0,0)-1.                  (16)

No root selection or infinite Fourier truncation is hidden here.
This is classical kernel machinery, not an external novelty claim
or a new Boolean inequality simply from its finite dimension.

The explicit Boolean entries include

    C00=lambda^2-1,
    C0j=lambda*1_A(j)-1_A(D-j), j>=1,
    Cii=lambda^2-1+|A intersect[1,i]|
                         -|A intersect[D-i,D-1]|.

Partition C after its first coordinate, with remaining first
column v0 and tail Ctail. The Schur complement gives

    L=v0^T*Ctail^-1*v0,
    g=(1+L)/(lambda^2-1-L).                      (17)

This preserves actual scalar information lost by the projections.
An operator-norm bound on Ctail is not a substitute for the
needed linked Boolean estimate on this particular vector.

For the prefix A=[1,n], direct entry cancellation gives

    C=(lambda-1)*(lambda*I+J),
    g=n/[(lambda-1)*(lambda+n)].                 (18)

Here W is zero-free on the closed disk for EVERY lambda>1:
its numerator lambda-(lambda-1)z-z^(n+1) is nonzero for |z|<1
by strict triangle. On the circle equality can occur only at
z=1, where the common1-z cancels and W(1)=lambda+n>0.
No external zero-location theorem is needed.

At lambda=2sqrt(n), equation(18) tends to zero with growing n.
Thus zero-freeness and C>0 ALONE cannot prove the desired gap.
These prefixes violate actual low M for large n: at
x=3pi/(2n+1), the Dirichlet identity gives

    M>=1/2+(2n+1)/(3pi),

using sin(t)<=t. The necessary extra hypothesis is the actual
pointwise Re W>=lambda/2, or its full Toeplitz positivity
equivalent, not just spectral stability of W. Encoding that
joint hypothesis into(17) is an existing Boolean inverse problem,
not an independently solved route.

For n8, (18) itself gives g>1/8: the denominator in its u form
is r*(1+8u)<.824*2.416<2, while8u^2=1/4. Since y<.206,
h=y/2-g<.103-.125<0. This independently confirms original S0
and P2 on the counterexample to(FN). The failed criterion and
the actual full scalar norm have distinct, rigorously determined
outcomes.

Final continuation status: the stronger full-negative closure is
REFUTED; the local multi-row M-bound is dominated by P9; a new
global allpass bound retains positive phase and recovers n8;
the exact finite matrix representation preserves the full norm.
None establishes a new unrestricted Boolean lower bound. No
resource operation, computation or additional agent by this advisor.

## 10. Exact corroboration and the complete cyclic closure is false

I read both full sources
[P2_prefix8_exact.py](../../src/P2_prefix8_exact.py) and
[P2_aggregation_test.py](../../src/P2_aggregation_test.py), and their
saved [prefix8](../experiments/P2_aggregation_2026-10-23/prefix8.json)
and [n56](../experiments/P2_aggregation_2026-10-23/n56.json) artifacts.
All computations were the parent's Dirichlet jobs; none was run
by this advisor. No additional test is proposed.

The n8 source implements exact Q(sqrt(32)) arithmetic and exact
sign decisions by rational squaring with the appropriate sign
branches. Its direct finite recurrence and independent geometric
closed forms agree. It confirms the paper reverse gap, the new
allpass recovery, and the exact kernel norm. An independent exact
Sturm chain verifies the whole-circle bound M<=11/4. Its full
inverse residual independently encloses the exact norm and original
negative P2 determinant. These are corroborations of the proofs
above, not premises substituted for an all-circle argument.

The n56 source uses an existing Boolean support of degree87 and
actual M upper7902460565/1644167168<sqrt(56), rechecked by exact
Sturm (chain length88). All finite inverse pairings use384-bit
Arb enclosures. Its inverse-square recurrence also agrees with
direct coefficient convolution, and every negative row agrees
with a separate reversed-polynomial/product implementation.

On that actual-lowM input, the full-negative criterion Psi_minus
is positive near0.0995053255. Subtracting the COMPLETE cyclic
allpass contribution still leaves

    Psi_cyclic >=1494485611361596415/18446744073709551616>0,

approximately0.0810162273. Thus the stronger finite closure using
ALL powers of this same global B is rigorously FALSE. Equation(14)
remains a true bound, but its universal sufficiency is refuted.
The original P2 determinant is a different quantity and is not
refuted by this certificate. Stop optimizing this cyclic closure;
all its additional power correlations already vanish exactly.

No arithmetic/enclosure error was found in these sources. Their
proof statuses are exact finite certificates plus independent
paper/source review, not Lean/kernel-checked mathematics.

## 11. The proposed centroid bound is valid but dominated by old P29

The parent proposed a trace consequence of C and the half-plane.
Every phi_j has norm squared S=||p||2^2, so

    Tr(C^-1)=D*S,
    Tr(C)=D*(lambda^2+n)-2*sum_A a.

Both identities check directly, including the endpoint a=D.
The generic trace inequality Tr(C^-1)>=D^2/Tr(C) and
Re p=(lambda+f)|p|^2>=(lambda-M)|p|^2 give

    S<=1/[lambda*(lambda-M)],
    lambda*M>=2*sum_A a/D-n.

Letting lambda decrease to M proves the valid inequality

    M^2>=2*sum_A a/D-n.                          (19)

However the actual half-plane combination is unnecessary for
this conclusion: Tr(C)>0 ALREADY implies lambda^2>the right
side for every lambda>M. Its limit is exactly(19). This is an
automatic stability-kernel consequence, not an extra half-plane
constraint newly extracted from the full matrix.

More decisively, the Boolean conclusion is already dominated
by [P29(b)](../PROOFS.md). Set h=D,L=2D in its Fejer-grid
inequality. Since sum_A(1-a/D)=n-sum_A a/D, it gives the
STRONGER linear estimate

    M>=2*sum_A a/D-n.                            (20)

If the right side is at least1, (20) dominates(19). Below1,
the old P13(a) averaging identity already supplies M>=1: average
f_A(x+2pi*j/D) over j=0,...,D-1. Since D=max(A), exactly
the frequency D survives, giving cos(Dx)>=-M. Set x=pi/D.
The same bound also follows from monic stability and the product
of root moduli, but is not a new project calibration. Thus the
suggested centroid root corollary is fully dominated by old P29(b)
and P13(a), with the high-centroid case already an old LINEAR-M
branch. No external priority claim is made for these elementary
calibrations or the classical stability-kernel machinery.

## 12. A necessary full matrix constraint that really retains the half-plane

A precise unprojected constraint remains available. Let
T=T_D(W) be the lower triangular coefficient Toeplitz matrix,
and P=T^-1=T_D(p). For every analytic polynomial h of degree<D,
the actual half-plane gives

    integral Re(p)*|h|^2
            >=(lambda-M)*integral |p|^2*|h|^2.

The second Gram matrix is the FULL covariance C^-1, not a
finite inverse truncation. Consequently

    Re(P)>=(lambda-M)*C^-1,
    Re(P)>=(lambda/2)*C^-1 in the low-M branch.  (21)

Here Re(P)=(P+P^*)/2. This is a derived necessary operator
constraint, not an already proved Boolean lower bound on its
Schur complement. A scalar trace or a generic operator-norm
replacement would discard the linked information again.

Bare Re(T)>=lambda*I/2 is too weak even as a scope condition:
for prefixes Re(T)=(lambda-1/2)I+J/2, positive at the desired
margin for all lambda>=1. Nevertheless actual low M fails for
large prefixes. Constraint(21) retains the full inverse covariance
and can distinguish that loss.

For an explicit paper check of strictness, take an even prefix
n=2m and h=(1-z^m)*(1+z+...+z^(m-1)). Its coefficient sum
is zero and squared norm n. The exact prefix kernel gives

    h^*C^-1*h=n/[lambda*(lambda-1)].

The coefficients of p through degree n-1 agree with
p_infinity=u*(1-z)/(1-rz), u=1/lambda,r=1-u. Direct Poisson
integration or geometric coefficient summation gives

    h^*Re(P)*h=3-4r^m+r^(2m)<=3.

For n256,lambda32 the low-M right side of(21) equals128/31>3,
so(21) fails although C>0 and the bare Re(T) margin hold.
This is only a logical scope check on the NEW matrix constraint;
the prefix's large M is already proved more strongly by old P29.
It is not a new family-exclusion theorem or an experiment.

The next finite-matrix proof task, if retained, must use the
joint Boolean structure of C,T and(21), rather than stability,
a trace, or a universal cyclic-projection completeness claim.
For D>=2 one concrete first adaptive signed vector is
x=Ctail^-1*v0, testing the polynomials with coefficient vectors
(0,x) and(1,-x) in(21). Its exact variational identity is

    ell=v0^T*Ctail^-1*v0
        =max_z[2v0^T*z-z^T*Ctail*z].

The correctly quantified uniform target is1+ell>=eta*n,
since the exact calibration identity is

    1+ell=4n*g/(1+g).

It is the EXISTING scalar norm-gap route through(17), not a
new target with an independent completeness theorem. An unqualified
ell>=eta*n is FALSE: every singleton A={D} has ell=0 and
g=1/3. One may use that version only after an explicit large-n
restriction. A successful derivation must produce a new Boolean
bound on these actual coupled quadratic forms; choosing the
optimizer or substituting an operator norm proves no such bound.
For D=1 take the empty tail and ell=0.
No estimate converting that joint condition into a universal
root-scale lower bound has been derived. This identifies a
concrete unprojected object without announcing another renamed
gap as research progress. Full signed Rayleigh and the independent
construction track remain live alternatives.

Final audit status: all proposed centroid formulas are correct,
but the resulting M-bound is already dominated by the ledger.
Complete cyclic allpass sufficiency is refuted on n56. The exact
norm representation and the half-plane operator constraint remain
valid tools, with no new unrestricted exponent or Chowla resolution.
