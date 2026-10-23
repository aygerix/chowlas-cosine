# S0 Boolean remainder audit: both components are indispensable

2026-10-23. Internal AI advisor, paper derivations only. No research
computation, VM operation, GPU deployment, additional agent or outreach.
Only this assigned note is edited. Shared Dirichlet must remain running;
only this project's own jobs may be ended. No Lean/kernel-checked proof.

## 1. Exact identity independently checked

Let A be a finite nonempty set of distinct positive integers, n=|A|,
F=sum_A z^a, f=Re F, D=2f, M=-min_circle f. All averages are normalized
Haar averages. Initially allow any real lambda>M, and define

    p=1/(lambda+F), h=F²/[lambda²*(lambda+F)],
    t=<F,F²>=#{ordered (a,b,c) in A³:a+b=c},
    r=||h||2², a=<F,h>, b=<F,Fh>, c=<F,h²>.

Inner products of the displayed real-coefficient analytic functions
are real. The lead's exact remainder identity is CORRECT:

    H0=<D*(Im p)²>
       =t/(2lambda^4)-lambda*r-c/2.                 (1)

For verification, p=1/lambda-F/lambda²+h and

    g=lambda²||p-1/lambda||2²
      =n/lambda²-2a+lambda²*r,
    T0=<F,p²>=-2n/lambda³+2a/lambda+t/lambda^4
                                  -2b/lambda²+c.

The coefficient equation (lambda+F)h=F²/lambda² gives
lambda*a+b=t/lambda². Substitution in H0=-g/lambda-T0/2 yields (1).
There is no lost real/imaginary-part factor. The proposed inequality
t/(2lambda^4)<=lambda*r+c/2 is exactly S0, not an additional theorem.

At the actual calibration lambda=2sqrt(n), M<=sqrt(n), the new task is
to control this COMBINED expression using unit coefficients. The
classical analytic identities themselves do not do so.

## 2. A negative selected Hankel term inside the exact domain

The lead and advisor independently reached the same small falsifier
to the stronger claim c>=0:

    A={1,5,6}, n=3, lambda=2sqrt(3).

These are the distinct positive differences of {0,1,6}, so the square
identity gives M<=3/2<sqrt(3) on the ENTIRE circle. No sampled premise
is being substituted for actual low M.

Since h²=F^4*p²/lambda^4, and below degree7 the only term of F^4 is
z^4, the selected coefficients are

    [z]h²=0,
    [z^5]h²=-2/lambda^7,
    [z^6]h²=3/lambda^8.

Consequently

    c=(3-2lambda)/lambda^8<0.                        (2)

Thus nonnegativity of the selected remainder-Hankel term is FALSE
for an actual-low-M Boolean support at the required lambda. This
does NOT refute S0: its norm term must also be retained, and t=2.

Even with t=0, c need not be nonnegative at arbitrary lambda>M.
For example A={1,5} has t=0 and M=2, and for every lambda>2 the same
degree calculation gives c=-2/lambda^7<0. This example is outside
the actual-low-M fixed-cardinality domain and does not refute the
weaker combined sum-free inequality requested in the task.

## 3. The norm term cannot pay all leading triangles either

The other tempting stronger bridge is

    t/(2lambda^4)<=lambda*||h||2².                  (3)

At actual low M, |F/(lambda+F)|<=1. Therefore

    ||h||2²<=n/lambda^4,
    lambda*||h||2²<=n/lambda³.

If (3) held universally it would force

    t<=2n*lambda=4n^(3/2).                          (4)

The already-recorded dense integer Sidon-difference controls refute
(4) inside the actual-low-M domain. No new family exploration or
numerical trend is needed. For an explicit paper bound, take an
existing cyclic (Q,k,1) Singer difference set in [0,Q-1],
Q=k(k-1)+1, and its positive integer differences A. Then

    n=k(k-1)/2, M<=k/2<sqrt(n) for k>2.

Let G=sum_(b in B)z^b. Its integer Sidon uniqueness gives
<|G|4>=2k²-k, and Cauchy on the fewer than3Q possible three-sums gives
<|G|6>>=k^6/(3Q)>=k^4/3. Since D=|G|²-k,

    6t=<D³>=<|G|6>-4k³+3k²>=k^4/6 for k>=24,
    t>=k^4/36.

For k>=64 this exceeds 4n^(3/2), because
4n^(3/2)<=sqrt(2)*k³ and k/36>sqrt(2). Available Singer parameters
above this threshold therefore falsify (3) rigorously. Existence and
the dense controls are prior dependencies, recorded in
`advisor_L25_derivation_2026-10-21.md`; the elementary three-sum
estimate is also in `advisor_boolean_boundary_2026-10-21.md` Section7.

This is an obstruction to an ARBITRARY-support component estimate,
not another lower-bound theorem about this settled family. Positive
Hankel contribution is essential in the high-triple regime, whereas
(2) shows that it is not always positive.

## 4. A valid component estimate, with its exact limited range

For every Boolean F and every analytic h in this calculation,

    |c|=|<F,h²>|<=||F||infinity*||h||2²=n*r.

Hence

    lambda*r+c/2 >= (lambda-n/2)*r.                  (5)

In particular the combined remainder cost is nonnegative whenever
lambda>=n/2. For t=0, this proves H0<=0 in that range, with strict
negativity when lambda>n/2. At lambda=2sqrt(n), it covers ALL
sum-free supports with n<=16, provided the inverse premise holds.
Small sum-free numerical successes in this range are therefore
automatic; they would not be discriminating evidence for S0.

For the requested sum-free alternative, the unresolved regime is
M<lambda<n/2; in the fixed actual-low-M problem it begins at n>16.
No sum-free Boolean counterexample to c>=-2lambda*r was obtained.
No assertion that this inequality is true in the remaining regime
is made. P9's existing square-root bound for t=0 is a different
certificate and does not establish the prescribed reciprocal sign.

## 5. A second attempted proof: pointwise/subharmonic payment fails

I tried to obtain the combined bound from a pointwise positive
remainder, or from subharmonicity plus the vanishing cubic moment
in the t=0 case. This attempt has a precise obstruction.

Normalize w=F/lambda and d(w)=w²/(1+w)=lambda*h. Analyticity allows
the averaged combined cost to be written as

    lambda*r+c/2=(1/lambda)*<Phi(w)>,
    Phi(w)=|d(w)|²+(Re w)*Re(d(w)²).                 (6)

The difference from the original integrand is a real part of the
analytic function w*d(w)², whose average is zero. At actual low M,
w lies in Re w>=-1/2. Nevertheless Phi is NOT nonnegative throughout
this half-plane. For example at w=2+4i,

    d(w)=(28+96i)/25,
    Phi(w)=3*(28/25)²-(96/25)²=-6864/625<0.

Thus a pointwise positive payment based only on that half-plane
cannot prove the combined bound.

There is also no repair by simply subtracting a multiple of the
known cubic moment to make this same potential subharmonic. Direct
differentiation gives

    Delta Phi(w)=4[Re w+|1+w|^-4-Re(1+w)^-3].

It is negative for Re w=-1/2 and sufficiently large |Im w|. In the
sum-free case <Re(w)*|w|²>=0, so one may try
Phi-alpha*Re(w)*|w|² without changing its average. Its Laplacian at
large |Im w| tends to 4*(1-2alpha)*Re w. Nonnegativity for both
positive and negative allowed real parts forces alpha=1/2. At
w=1 the resulting Laplacian is 4*(1/16-1/8)=-1/4<0.

This disproves that particular cubic-adjusted Jensen/subharmonic
argument. It is not a counterexample produced by a Boolean F,
nor an impossibility theorem for other Bellman functions or other
uses of the coefficient structure. The failure is relevant because
it locates exactly where the attempted proof discarded Booleanity.

## 6. A sign-retaining alternative derived from the same remainder

After both component-discarding attempts fail, retain the cross term
and allow the odd vector to move. Put

    u=Im F, v=Im h,
    e=<F²,h>, d0=<Fh,h>.

The exact two-dimensional norm and D-energy matrices are

    Q=(1/2)*[[n,a],[a,r]],
    E=(1/2)*[[t,e],[e,2*d0-c]],
    e=lambda²*(lambda*r+d0)>0.                     (7)

For the mixed energy, ImF*Imh is half the difference between
Re(F*conjugate(h)) and Re(Fh). Their two <F,Fh> contributions
cancel after multiplication by D, leaving <D*u*v>=e/2. Also
<D*v²>=d0-c/2. Finally (lambda+F)h=F²/lambda² gives the expression
for e, whose positivity follows from lambda+f>0.

The norm matrix is positive definite: proportionality of Im h and
Im F would force h proportional to F by analytic uniqueness and
their zero constants, incompatible with h=F²/[lambda²(lambda+F)]
for nonconstant F. S0 prescribes the coefficient vector
(-1/lambda²,1) in (7); optimizing the plane is a different condition.

When t=0, det E=-e²/4<0, so some odd combination has negative energy
for every lambda>M, without the unresolved claim about that one
prescribed vector. This provides no new square-root bound: the
sum-free branch is already handled quantitatively by P9. It does
demonstrate why failure of a prescribed reciprocal vector would not
mean failure of the full signed-Rayleigh problem.

When t>0, the plane has a negative direction exactly when

    t*(2*d0-c)<e².                                  (8)

No universal estimate or root-scale margin for (8) is claimed. It is
a concrete sign-retaining pencil for a changed-witness attempt, not
a rebranding of (1) as a proof. The earlier weighted sign falsifier
and high-positive-front controls remain adversaries to any proposed
universal low-dimensional witness claim.

## 7. Decision and precise gap

PROVED/AUDITED: identity (1); calibrated Boolean negative-c example
(2); failure of the norm-only component bridge; the limited bound
(5); obstruction to the explicit pointwise/cubic-adjusted potential;
and the exact movable odd-plane pencil (7).

UNPROVED: the combined leading-triangle bridge, S0, R0, and the
sum-free prescribed-vector sign outside (5). No actual Boolean
positive-energy counterexample or new universal exponent was found.

Do not demand either component be separately favorable, and do not
spend on small sum-free calibration or further Singer family trends.
The next genuine step must control their signed interaction using
unit coefficients, or move to unrestricted signed Rayleigh directions.
Equation (7) is one exact intermediate for the latter; (8) must first
be derived or adversarially tested before receiving a universal label.
Maintain the independent construction track with all-circle upper
bounds. The failure of these component proofs does not block the
full goal or authorize a shutdown of shared Dirichlet.

## 8. Global plane-sign self-improvement: independent audit of P2

The lead subsequently derived a stronger amplification result for
the MOVABLE plane in (7). I independently checked its finite-lift,
moment and determinant bounds. No computation is needed. Define the
weaker local conjecture

    (P2) For EVERY Boolean A with ACTUAL M_A<=sqrt(n),
         SOME nonzero q in span{Im F_A, Im p_A} has
         <D_A*q²><=0, with lambda=2sqrt(n).

This is the same plane as span{Im F_A,Im h_A}. S0 implies P2 by its
prescribed vector; no converse to S0 is claimed. For t>0, P2 on one
support is exactly the non-strict determinant condition

    t*(2*d0-c)<=e².                                 (9)

For t=0 it already follows from (7). Crucially, universal P2 would
still imply full Chowla, despite imposing no prescribed direction
and no numerical energy margin.

### 8.1 Conditional amplified counterexample: the entire plane is positive

Suppose V is Boolean of cardinality N>=2^44, with

    M_V<=sqrt(N)/2,
    g_V(2sqrt(N))<=2^-104.                          (10)

Use EXACTLY the U,k,n',lambda,L construction from the padding theorem
in `advisor_R0_resume_2026-10-23.md` Section3. Thus

    k=floor(sqrt(N)/2^20), U=diff_+{1,9,...,9^(k-1)},
    m=k(k-1)/2, n'=N+m, lambda=2sqrt(n'),
    L=2^16*n'*9^k, A=support(U) union L*support(V).

The calibrated set A is Boolean and ACTUALLY low M on the full circle.
The hypothesis (10) is NOT known to be attained by a Boolean V.
Write b=Im F_A, q=Im p_A, and let E denote their two-dimensional
D_A-energy matrix. Its entries are Hbb,Hqq and J=<D_A*b*q>.

**Reciprocal diagonal.** The earlier torus bound is at least
Delta_H=k³/(96lambda^4). The finite-L error divided by Delta_H is
at most33792/(65536*k)<1/2, since k>=4. Therefore

    Hqq>=Delta_H/2>2^-77/sqrt(N).                   (11)

For the last inequality, k>=sqrt(N)/2^21 and lambda<3sqrt(N) give
Delta_H/2>1/[192*81*2^63*sqrt(N)]>2^-77/sqrt(N).
The stronger gap in (10) only improves the earlier negative-cost
estimate.

**Large positive polynomial diagonal.** Put L_V=||f_V||1 and fix
epsilon=2^-50. The exact factorization V=zeta_V*(lambda0+V),
lambda0=2sqrt(N), and Cauchy--Schwarz imply

    L_V<=||V||1<=sqrt(5*g_V*N)<epsilon*sqrt(N).

Booleanity gives <f_V²>=N/2. Since <(f_V)_+> = <(f_V)_-> = L_V/2,

    <(f_V)_-²><=M_V*L_V/2<=epsilon*N/4,
    <(f_V)_+²>>=N/4.

Cauchy in the form <X³><X>>=<X²>² for X>=0 now yields

    <(f_V)_+³>>=N²/(8*L_V),
    <(f_V)_-³><=M_V²*L_V/2<=epsilon*N^(3/2)/8,
    <f_V³>>=N^(3/2)/(16*epsilon).

Here epsilon²<1/2 supplies the conservative final factor. Also
t_V=(4/3)<f_V³>. The finite integer lift adds triples EXACTLY:

    t_A=t_U+t_V.

Indeed L>2*max(support U): two U frequencies cannot sum to a positive
L-multiple, and a mixed U/LV relation would require a nonzero U
frequency to be divisible by L. The other mixed size cases are
impossible as well. Thus

    Hbb=t_A/2>=N^(3/2)/(24*epsilon)>2^45*N^(3/2).    (12)

This is an exact relation-count statement, not an approximate torus
transfer of a high-degree cubic moment.

**Off-diagonal.** On the actual circle,

    J=-2*<f_A*(Im F_A)²/|lambda+F_A|²>.

Actual low M gives |F_A/(lambda+F_A)|<=1. Hence

    |J|<=2*||f_A||1<=2*(||f_U||1+L_V)
                       <=2*(k+L_V)<2^-18*sqrt(N),
    J²<2^-36*N.                                    (13)

The bound ||f_U||1<=k follows from its difference-square upper
M_U<=k/2 and mean zero, or directly from that square identity.
Combining (11)--(13),

    Hbb*Hqq>2^-32*N>J².

Both diagonals are positive and the determinant is positive. Thus
the full energy form on this explicit plane is POSITIVE DEFINITE,
not merely positive on q. This A contradicts P2 if a Boolean V
satisfying (10) exists. No such V was found or assumed to exist.

### 8.2 Consequence: P2 alone would imply Chowla

If P2 were universal, (10) would be impossible. For N<2^44 the
elementary g_V>=1/(sqrt(N)+2)² already exceeds2^-104. Therefore
P2 would imply a uniform norm gap on the whole strict-margin class
M_V<=sqrt(N)/2. The previously checked identity then gives

    ||f_V||1>=(lambda0-M_V)²*g_V/lambda0,
    M_V>=||f_V||1/2.

These bounds, together with the complementary M_V>sqrt(N)/2
branch, prove conservatively

    P2 universal  ==>  M(A)>=2^-107*sqrt(|A|)
                      for EVERY Boolean A.          (14)

Thus (9) is a weaker LOCAL sufficient target than the prescribed
S0 sign or R0 margin, with the same ultimate implication after
global amplification. This is not a proof of P2, a pointwise
equivalence with Chowla, or a quantitative quotient bound on the
plane for each individual support.

### 8.3 Explicit weighted plane-sign falsifier, with variance corrected

The previous Fejer pad V_N=sum_(j=1)^N(1-j/(N+1))*z^j has
g_V(2sqrt(N))<=3*N^-1/4. Consequently every N>=2^424 satisfies
(10)'s gap bound. The Boolean variance N/2 CANNOT be reused for this
weighted pad. Instead its exact coefficient square sum gives

    ||V_N||2²=N*(2N+1)/[6*(N+1)]>=N/4,
    <f_V²>>=N/8.

All coefficients are still in(0,1), its M_V<=1/2, and
L_V<epsilon*sqrt(N), epsilon=2^-50, as before. The adjusted bounds
are

    <(f_V)_+²>>=N/16,
    <f_V³>>=N^(3/2)/(256*epsilon),
    t_V>=N^(3/2)/(192*epsilon),
    Hbb>=N^(3/2)/(384*epsilon)>2^41*N^(3/2).

For the third moment use positive third at least N²/(128*L_V)
and negative third at most epsilon*N^(3/2)/8; epsilon²<1/32
suffices. Triple addition remains exact with the natural weighted
pairing. The inverse/mixed-cost and derivative estimates from the
padding proof do not need Booleanity of V, so (11) and (13) remain
valid. Now Hbb*Hqq>2^-36*N while J²<2^-36*N: strict positivity
still holds, even with the corrected smaller variance.

This gives a fully explicit occupied-count-calibrated WEIGHTED
counterexample to P2 for every N>=2^424, using the same integer U
and L. It is outside the Boolean domain, so it refutes neither P2
nor Chowla. It does rigorously prevent replacing exact unit
coefficients by mere nonnegativity and an upper cap in an attempted
proof of (9). No weighted-to-Boolean transfer is claimed.

### 8.4 Updated next proof target

The independently audited new reduction is (14). Retaining the
entire two-dimensional energy matrix has a definite mathematical
purpose; it is not justified merely by finite solver successes.
The missing step is a Boolean proof or counterexample to the
nonpositive-determinant assertion (9), under the exact low-M and
fixed-lambda hypotheses. The weighted amplified plane is already
a paper adversary to any proof that loses unit coefficients.
No new experiment, theorem proof, resource action or universal
positivity claim has been undertaken in this audit subsection.
