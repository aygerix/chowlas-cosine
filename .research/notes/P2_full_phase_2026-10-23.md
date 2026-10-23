# Stop the incomplete phase closures; preserve the full scalar constraint

2026-10-23. Previous checkpoint4bdf346 was progress. Full Chowla remains
unresolved. This is a research record, not a manuscript. The sole advisor
independently checked the derivations and exact source/artifact pairs in
[the aggregation audit](advisor_P2_aggregation_2026-10-23.md).
No new Lean/kernel verification or novelty claim.

## 1. Precise target and two failed sufficient strengthenings

Let A be a finite nonempty set of distinct positive integers, n=|A|,
D=maxA, F=sum_A z^a, f=Re F. Assume ACTUAL M=-min_circle f<=sqrt(n),
lambda=2sqrt(n), W=lambda+F, p=1/W. Integrals are probability Haar.
Set

    g=lambda²||p||²-1, T=<F,p²>, y=-lambda T,
    C2=<F²,p>, t=<F,F²>, H=<2f(Im p)²>,
    K=(F²+lambda*conjugate(F))*p².

The retained original P2 target is Phi=2tH-C2²<=0 for t>0; t=0 is
already settled by ImF. Universal P2 is sufficient for Chowla by the
earlier amplification theorem, but is NOT proved or refuted here.

Exactly, K0=-y, ||K||²=5g-2y, and

    k_j=K_(-j)=lambda*sum_(a∈A,a>=j)(p²)_(a-j), 1<=j<=D,
    Nminus=sum k_j², Eplus=||P_>0 K||²,
    Gminus=(y²+Nminus+2y)/5,
    g=Gminus+Eplus/5.

Thus

    Phi=Psi_minus-(2t/(5lambda))*Eplus,
    Psi_minus=(2t/(5lambda))*(y/2-y²-Nminus)-C2².       (1)

The candidate Nminus+(5lambda/(2t))*C2²>=y/2-y² discards Eplus.
It is FALSE even inside the exact Boolean/lowM domain.

## 2. A paper counterexample with eight frequencies

Take A={1,...,8}, lambda=4sqrt2, u=1/lambda, r=1-u, R=r^8, t=28.
The finite inverse coefficients give the exact closed forms

    y=u*[1-r^7*(1-9u)],
    C2=u+(1-10u)*R-r*R²,
    k_(8-s)=u*r^(s-1)*[1-(s+1)u], 0<=s<=7.

The s0 expression equalsu. To derive them, through degree16 use

    p=(1-z)/[lambda(1-rz)]
       +z^9*(1-z)/[lambda²(1-rz)²]+O(z^18).

Exact rational enclosures yield .20<y<.206, -.04<C2<0,
Nminus<.052 and5lambda/56<.51. Since y/2-y²>.06,

    y/2-y²-Nminus-(5lambda/56)*C2²
        >.06-.052-.51*.04²=449/62500>0.                 (2)

This is a paper sign proof, not a sampled minimum or an assumed
numerical optimization outcome.

For the ACTUAL all-circle premise write x=2s,0<=s<=pi/2 by evenness,
and 1+2f(x)=sin(17s)/sin(s). Up to s=pi/17 the numerator is
nonnegative. Between pi/17 and pi/14, sin(17s)>=-3s and
sin(s)>=95s/96, so the quotient>=-288/95>-9/2. Above pi/14,
sin(s)>=sin(pi/14)>389/1750>2/9, giving the same lower floor-9/2.
The elementary last inequality uses pi>3.14,pi<22/7 and
sin t>=t-t³/6. Therefore

    f>=-11/4, M<=11/4<sqrt8.                            (3)

The exact Q(sqrt32) implementation independently checks finite
recurrences against the closed forms, rational sign decisions against
(2), and all-circle (3) by exact Chebyshev/Sturm. A complete infinite
inverse residual separately proves ORIGINAL H<0 and Phi<0.
The exact kernel formula below provides a second full-norm method.
[Source](../../src/P2_prefix8_exact.py),
[all quantities/certificates](../experiments/P2_aggregation_2026-10-23/prefix8.json).

One predeclared existing n56,degree87 support also refutes the negative-
only condition, with certified Psi_minus>.0995. Its global upper bound
7902460565/1644167168<sqrt56 is rechecked by Sturm. Its ORIGINAL P2
is negative by a support-matched earlier complete inverse certificate.
[Source](../../src/P2_aggregation_test.py),
[data](../experiments/P2_aggregation_2026-10-23/n56.json).
There was no new support search or expansion of the old alias family.

## 3. A valid many-row identity, with an already stronger P9 bound

Let m=minA, E=A∩(max(m,D-m),D], and
r_a=sum_(b∈A,b>=a)1_A(m+b-a). Since inverse-square degrees below2m
have only the constant and linear-F terms,

    k_a=1/lambda,
    k_(a-m)=1_A(a-m)/lambda-2r_a/lambda², a∈E.

These row pairs are disjoint. Their residual energy over the scalar
conjugate-F projection is at least2sum_E r_a²/lambda⁴, and
Nminus>=|E|/lambda². This is an exact inverse-coefficient identity.
It does not give a new M-bound: P9 on E and E-m, both independent
packets, plus the star on E gives

    M>=||r||/(2sqrt|E|), M>=sqrt|E|/2,
    M⁴>=sum_E r_a²/16.

The corresponding phase-only bound has denominator24 and is weaker.
No-carry Sidon difference sets can have E={D},r_D1 with n→infinity
and exact lowM; terminal-window aggregation cannot be universal.
Do not enlarge a search to compensate for this mathematical limitation.

## 4. A changed global positive-phase bound, and its complete limitation

Unlike (1)'s discarded tail, keep scalar positive phase via the WHOLE
polynomial. W is monic and zero-free on the closed disk. Put

    Wrev(z)=z^D W(1/z), B=Wrev/W, a=1/lambda.

B is an analytic inner function, B0=a. Exterior Laurent expansions
give

    K/B=W/Wrev-2lambda/Wrev+lambda*z^(-D)/W,
    <K,B>=a+lambda*p_D,
    <Kplus,B-a>=(1+y)/lambda+lambda*p_D=:v.

The first two exterior constants are1/lambda and0, respectively.
Negative frequencies are orthogonal to B, so no scalar phase term
is replaced by its modulus. For j>=2, K/B^j has only interior poles
and exterior constant a^j; hence <Kplus,B^j>=(1+y)a^j.

The functions e_j=B^(j-1)(B-a)/sqrt(1-a²),j>=1, are orthonormal
and have strictly positive Fourier frequencies. Their Kplus pairings
are v/sqrt(1-a²), -p_D/sqrt(1-a²), then ZERO for all j>=3. Therefore

    Eplus >= Ecyclic=[v²+p_D²]/(1-lambda^(-2)).           (4)

This is the COMPLETE contribution from all powers of this B.
More powers cannot improve it. The unit leading coefficient enters
through B0=1/lambda; for a tiny weighted top coefficient c it becomes
c/lambda and the bound degenerates accordingly.

Bound(4) recovers n8, even without C2. Paper lower bounds
v>.16,k8>.176,k7>.113 give
Nminus+v²/(1-u²)>.069345>1/16>=y/2-y². The exact field check
gives the stronger two-correlation S0 margin>.0198.

However it does NOT close P2 universally. On the SAME n56 falsifier,

    Psi_cyclic=Psi_minus-(2t/(5lambda))*Ecyclic
                 >.0810162273>0.                       (5)

All balls and cross-checks are in the linked n56 artifact. Thus the
universal sufficient criterion using the ENTIRE cyclic allpass space
is also FALSE. Stop this closure. Retain (4) as a valid finite bound,
not a universal witness-completeness principle. Original P2 survives.

## 5. Full inverse information as an exact finite kernel matrix

An exact representation avoids discarding the scalar tail. Write
w0=lambda,wD1,wj=1_A(j) for0<j<D. For0<=i,j<D define

    Cij=sum_(k=0)^min(i,j)
         [w_(i-k)w_(j-k)-w_(D-i+k)w_(D-j+k)].

Then C is positive definite and

    ||p||²=(C^-1)00,
    g=lambda²(C^-1)00-1.                                (6)

Here is a complete kernel argument. The independent functions
phi_j=z^j/W,j<D, are orthogonal to every B*z^s,s>=0: their
pairing is the constant of z^(j-s)/Wrev, whose exterior series
has no constant term. The Hardy kernel minus its B multiple,
(1-B(z)conjugate(B(w)))/(1-z*conjugate(w)), therefore reproduces
each phi_j. Expanding its numerator gives phi(z)^T C conjugate(phi(w)).
The quotient is polynomial of degree<D in each variable because its
numerator vanishes at z*conjugate(w)=1. Linear independence then
identifies the Gram matrix of phi with C^-1. This also proves C>0.
This representation is not claimed novel or a new universal bound.

Let v0=(lambda*1_A(j)-1_A(D-j))_(j=1)^(D-1), and let Ctail remove
the first row and column. The exact scalar Schur complement is

    L=v0^T*Ctail^-1*v0,
    g=(1+L)/(lambda²-1-L),
    L=max_x[2v0·x-x^T*Ctail*x].                          (7)

An absolute order-n lower bound on 1+L in the actual lowM domain would
give the EXISTING norm-gap route to Chowla. Equation(7) is a coordinate
representation of that open gap, not a proof or an independent route.
No uniform operator bound may replace this linked signed input.
The exact calibration is1+L=4n*g/(1+g). Use1+L>=eta*n uniformly;
L>=eta*n alone fails for singletons, whereL0. Small cases must not
silently be dropped from a claimed universal theorem.

Scope guard: for A={1,...,n}, W is zero-free for everylambda>1,
C=(lambda-1)(lambda I+J), and

    g=n/[(lambda-1)(lambda+n)]→0 atlambda2sqrt(n).         (8)

Zero-freeness follows directly from
(1-z)W=lambda-(lambda-1)z-z^(n+1), strict triangle inside and
the removable z1 boundary case. These prefixes violate actual lowM
for large n: x=3pi/(2n+1) gives M>=1/2+(2n+1)/(3pi).
Thus C>0 by itself cannot replace the actual half-plane assumption.
For n8, (8) is an exact quadratic-field full-norm value that agrees
with the independent polynomial-residual enclosure.

The trace consequence M²>=2sum_A a/D-n is valid but OLD P29(b)
already gives the stronger linearM bound in its useful range; P13(a)
supplies M>=1 for the remaining range. Do not count this as a new
centroid or unrestricted lower-bound improvement.

## 6. Global review and the first next coupled calculation

Stop the full-negative and complete cyclic-allpass sufficient closures.
Both have genuine Boolean counterexamples. Stop terminal-packet M
bounds and trace-centroid upgrades, which the existing ledger dominates.
The true global allpass bound and exact kernel formula are retained.

The actual half-plane has an unprojected necessary constraint that must
be kept alongside C. For the D×D lower triangular coefficient Toeplitz
matrices T=T_D(W), P=T^-1=T_D(p), integration against every polynomial
h of degree<D gives

    Re(P)>=(lambda-M)*C^-1,
    Re(P)>=(lambda/2)*C^-1 in the actual-lowM branch.     (9)

This follows from Re p=(lambda+f)|p|²; C^-1 is the FULL covariance,
not a truncated inverse norm. Equation(9) is necessary, not claimed
equivalent to the entire-circle condition at this one finite dimension.
Bare Re(T)>=lambda I/2 is too weak: it holds for all large prefixes
although they violate lowM. The full constraint(9) can see that loss.
For prefix256,lambda32,h=(1-z128)(1+...+z127), the left quadratic
form is3-4(31/32)^128+(31/32)^256<=3, while the right is128/31>3.
This is a paper scope test, not a new computation or family theorem.

First next calculation: use the adaptive signed x=Ctail^-1 v0 from(7)
and the Schur vector(1,-x) in(9), retaining ALL covariance terms.
Derive a genuinely Boolean inequality for those forms, or exhibit a
Boolean obstruction satisfying the necessary joint constraints. An
order-n leverage estimate remains the same open C* norm-gap problem;
do not rename it as a solved or novel route. Do not restart a trace,
generic operator-norm, fixed-power, or successful-control argument.

Three live lines remain arbitrary-support signed Boolean coupling,
actual scalar/mixed-factor coefficient control, and independent growing
Boolean constructions with all-circle upper bounds. This cycle has no
universal exponent improvement or vanishing-ratio family. Every own job
is terminal/PASS; no GPU use, no VM lifecycle action, shared Dirichlet
left running, cumulative conservative RunPod spend still$0.10.
