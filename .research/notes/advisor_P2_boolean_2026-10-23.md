# Boolean P2 attempt and the full fixed-degree phase-polynomial obstruction

2026-10-23. Internal AI advisor. Paper derivations and read-only inspection
of lead-produced artifacts; no computation, VM operation, GPU, additional
agent or external outreach. Only this assigned note is edited. Shared
Dirichlet must remain running. No Lean/kernel-checked proof is claimed.

## 1. Exact P2 target and result of this pass

A is a nonempty finite set of distinct positive integers, n=|A|,
F=sum_A z^a, f=Re F, b=Im F, M=-min_circle f. Assume ACTUAL
M<=sqrt(n), fix lambda=2sqrt(n), and put p=(lambda+F)^-1,
q=Im p. All averages below are probability Haar averages.

Write t=<F,F²>, C1=<F,p>, C2=<F²,p>, H=<2f*q²>. The precise
P2 energy matrix on span{b,q} is

    [[t/2,C2/2],[C2/2,H]].

For t>0, P2 is exactly 2tH<=C2²; for t=0, b itself already has
zero energy. The reduction P2=>Chowla is proved conditionally in
the preceding notes, but P2's Boolean determinant remains OPEN.

This pass gives an exact unit-coefficient recurrence identity whose
new residual has both signs inside actual low M. It does not prove
or falsify rational P2. It also proves a broader architecture
obstruction: ALL real polynomial witnesses of any fixed total degree
in f and b have bounded negative Rayleigh quotient along the dense
Singer sequence. Thus retaining phase while using finitely many
polynomial powers is insufficient. The proof below is elementary
once the cyclic difference sets exist; it avoids MZ sampling and
bounded-Riesz-projection dependencies.

## 2. A genuinely coefficientwise attempt: split backtracking exactly

Extend the real Taylor coefficients p_j by p_j=0 for j<0. The inverse
recurrence is

    lambda*p_j+sum_(c in A,c<=j)p_(j-c)=0 for j>=1.

Sum at j=a+b over ordered a,b in A. Define

    R_A(p)=sum_(a,b,c in A; c!=a,b; a+b>c) p_(a+b-c).

The zero-index terms a+b=c contribute t/lambda. Positive-index terms
with c=a or c=b contribute (2n-1)C1: each coincidence contributes
n*C1, and their intersection a=b=c was counted twice. Hence

    lambda*C2=-t/lambda-(2n-1)C1-R_A(p).             (1)

This is an actual unit-amplitude implication. For weighted coefficients,
the intersection instead involves sum_a w_a³*p_a, not simply C1;
the two other terms involve the coefficient square sum. It therefore
does not follow merely by replacing a weighted norm with support size.

However the new residual does not have a favorable universal sign.
Two exact examples are within the ACTUAL low-M fixed-lambda domain:

* A={1,2}. Its M=9/8<sqrt(2), lambda=2sqrt(2), and
  R_A=p_3=2/lambda³-1/lambda^4>0.
* A={1,2,3}. Here
  R_A=p_1+2p_2+p_3+3p_4+p_5
      =-4/lambda²+15/lambda³-16/lambda^4
                            +7/lambda^5-1/lambda^6.
  At lambda=2sqrt(3), the numerator after multiplication by lambda^6
  is 187lambda-769<0, since lambda<4.

For the second all-circle premise, with c=cos(x),
f=(2c²-1)(1+2c). If c<=0 its two factors have absolute value<=1,
so f>=-1. If c>=0, f+3/2=4c³+2(c-1/2)²>=0. Thus M<=3/2<sqrt(3).

Equation (1) keeps exact Boolean coincidences, but neither discarding
R_A nor assigning it a universal sign is valid. A proof of P2 would
still need a quantitative interaction between this finite selected
remainder and the FULL inverse norm entering H. No such estimate
was derived. These examples are not P2 counterexamples.

## 3. Exact failure of the proposed five-count polynomial plane

For comparison the lead proposed the different plane span{Im F,Im F²}.
Its matrices are correctly normalized:

    Q=(1/2)*[[n,t],[t,E4]],
    E=(1/2)*[[t,E4],[E4,C5]],
    E4=||F²||2², B=<F³,F²>, C=<F,F^4>, C5=2B-C.

Thus the proposed inequality t*C5<=theta*E4², theta<1, would suffice
to make this plane useful. For t>0, the vector
Im F²-(E4/t)Im F would have energy at most
-(1-theta)E4²/(2t) and norm at most nE4²/(2t²), yielding a negative
Rayleigh quotient of magnitude at least (1-theta)t/n. The issue is
truth of the count inequality, not its conditional implication.

It is FALSE even with theta=1 on the existing certified n=56 support.
I read the saved integers and the independent signed-Laurent matrix
producer, without running either:

    t=1315, E4=89348, B=3610099, C=522296,
    C5=6697902,
    t*C5=8807741130,
    E4²=7983065104,
    4det(E)=824676026>0,
    4det(Q)=56*89348-1315²=3274263>0.

All energy diagonals are positive, so every nonzero vector in this
polynomial odd plane has POSITIVE energy. The saved all-circle bound
M<=7902460565/1644167168<5<sqrt(56) supplies the precise premise.
The support and certificates are in
`experiments/phase_five_count_2026-10-23/results.json`; its source is
`src/cstar_phase_five_count.py`. The second Laurent implementation
encodes 2i*Im F and 2i*Im F² and divides the selected products by-4;
the signs and factors check. The two other saved controls also
falsify the count inequality, but further finite cases are unnecessary.

This does NOT falsify rational P2: the same n=56 support has a
separately certified negative reciprocal direction. Higher nonlinear
content, rather than merely retaining phase in two polynomial powers,
matters in this exact example.

## 4. The broader architecture theorem

THEOREM. For every fixed integer d>=1 there exist constants C_d,
Q_d>0 with the following property. Let B be any cyclic
(Q,k,1) perfect difference set represented in {0,...,Q-1}, where
Q=k(k-1)+1>=Q_d. Let A be its positive INTEGER differences,
n=k(k-1)/2, F_A=sum_A z^a, f_A=Re F_A, b_A=Im F_A. For every
real polynomial P(u,v) of total degree at most d for which
q(x)=P(f_A(x),b_A(x)) is not identically zero,

    <2f_A*q²>/<q²> >= -C_d.                        (2)

The coefficients of P may depend arbitrarily on Q. If additionally
<q>=0, its energy is strictly positive, and in fact its Rayleigh
quotient is >=c_d*Q for one c_d>0 once Q is sufficiently large.

The difference-square identity always gives M(A)<=k/2<sqrt(n) for
k>2, so these are within the exact low-M domain. The established
dense-Singer L1 lower bound in the previous record also gives
M(A)>=c*sqrt(n) eventually; that separate family fact is not needed
for the proof of (2). This theorem is an exclusion of a UNIVERSAL
WITNESS ARCHITECTURE, not another Chowla lower-bound theorem for the
family. Singer existence supplies infinitely many such parameters;
it is an already-recorded dependency, not proved afresh here.

### 4.1 Elementary uniform interpolation from the perfect grid

Let omega=exp(2pi*i/Q), T_B=sum_(b in B)z^b, and define

    S=(k/Q)*sum_(j=0)^(Q-1)z^j, R=T_B-S,
    alpha=k²/Q ->1.

The cyclic difference property gives

    R(1)=0, |R(omega^r)|=sqrt(k-1) for 1<=r<Q.

Cardinal interpolation at these Q roots is exact for degree<Q:

    R(z)=sum_r R(omega^r)*L_r(z),
    L_r(z)=(1-z^Q)/[Q*(1-z*omega^-r)].

On the unit circle the sum of |L_r| is O(1+log Q), uniformly in z.
To see this, bound the nearest term by a constant using
|1-z^Q|<=Q*distance(z,nearest root), and bound the remaining terms
by C/j in order of their angular distances. Therefore

    ||R||infinity=O(sqrt(k)*log(2Q)).                (3)

This elementary bound is sufficient; no endpoint MZ theorem is being
assumed. The usual finite-geometric bound also gives, for fixed p>1,

    ||S||p=O_p(k*Q^(-1/p)).

### 4.2 Transfer the real and analytic profiles

Let Fejer_Q=Q^-1*|sum_(j=0)^(Q-1)z^j|². Then

    D_A=2f_A=|T_B|²-k,
    D0=alpha*(Fejer_Q-1),
    D_A-D0=2Re(S*conjugate R)+|R|²-(k-alpha).

Using (3), for every FIXED p>2,

    ||D_A-D0||p
       =O_p(Q^(3/4-1/p)*log(2Q)+Q^1/2*log²(2Q)).

Both terms are o(Q^(1-1/p)). Projecting onto positive frequencies
costs only an additional O(log(2Q)): the finite projection kernel
sum_(j=1)^(Q-1)z^j has L1 norm O(log(2Q)), by the same geometric
bound, and Young's inequality applies. Consequently, with

    F0=alpha*sum_(j=1)^(Q-1)(1-j/Q)*z^j,

we have

    ||F_A-F0||p
      =O_p(Q^(3/4-1/p)*log²(2Q)+Q^1/2*log³(2Q))
      =o(Q^(1-1/p))  for every fixed p>2.           (4)

The estimates are uniform in the particular perfect difference set.
No sampling or Hilbert-transform theorem beyond these elementary
finite-kernel estimates is required. The p>2 qualification is
essential; it cannot be silently applied to the second moment.

### 4.3 All nonconstant energy entries have the required degree

For multi-indices I=(r,s), 1<=m=r+s<=d, define

    v_I=(f_A^r*b_A^s)/Q^m, mu_I=<v_I>, w_I=v_I-mu_I.

Every uncentered energy entry <D_A*v_I*v_J> has homogeneous degree
ell=m_I+m_J+1>=3 in F_A and its conjugate. At p=ell, (4) and
Holder imply that replacing F_A by F0 changes this entry by o(1).
Indeed a homogeneous difference of degree ell is bounded by a
constant times |F_A-F0|*(|F_A|+|F0|)^(ell-1), whose integral is
o(Q^(ell-1)); the normalization is exactly Q^(ell-1).

Define the entire profile

    H(t)=integral_0^1 (1-s)*exp(i*s*t) ds,
    Re H(t)=(1-cos t)/t²,
    Im H(t)=(t-sin t)/t²,

with the removable values at t=0. On x=t/Q,
F0(e^(ix))/Q tends to H(t). The finite geometric formula supplies
the uniform bound |F0(e^(it/Q))/Q|<=C/(1+|t|) for |t|<=pi*Q.
Dominated convergence gives the limiting energy Gram

    G_IJ=(1/pi)*integral_R Re H(t)
           *(Re H(t))^(r_I+r_J)*(Im H(t))^(s_I+s_J) dt.  (5)

The ENERGY ENTRIES THEMSELVES converge to (5). They are not to be
multiplied by Q: D_A supplies a factor Q and dx supplies Q^-1.
The tail is integrable since total degree is at least3.

### 4.4 Strict positive definiteness, including phase polynomials

Re H is positive almost everywhere. Suppose a real polynomial
P_0(u,v), with nonconstant monomials of degree<=d, had zero quadratic
form in (5). Continuity would force

    P_0(Re H(t),Im H(t))=0 for all real t.

The invertible complex linear change of variables u=(z+w)/2,
v=(z-w)/(2i) yields a nonzero complex polynomial R_0(z,w) satisfying

    R_0(H(t),H(-t))=0 for real t.

Both sides are entire in t, so this identity extends to complex t.
Write R_0(z,w)=sum_(j=0)^J A_j(z)*w^j with A_J nonzero. At t=iy,
y->+infinity,

    H(iy)~1/y ->0,
    H(-iy)~exp(y)/y² ->+infinity.

If A_J has its first nonzero coefficient at degree m, then
A_J(H(iy))~a*y^-m, a!=0. The highest w-power thus dominates
exponentially every lower power. It cannot sum to zero. If J=0,
the same first nonzero coefficient argument applies directly.
This contradiction proves strict positive definiteness of G.

In particular the odd analytic power family Im H^j is independent:
a polynomial P(H(t)) real on the real t-axis would give
P(H(t))=P(H(-t)); the same imaginary-axis comparison rules this out.
The bivariate argument proves more than that special case.

### 4.5 Centering, constants and the Rayleigh lower cap

For degree1, mu_I=0 exactly. For degree2, the exact second moment
gives mu_I=O(1/Q); for degrees>=3 this follows from (4). Thus all
mu_I=O_d(1/Q). Also

    c_I=<D_A*v_I>=O_d(1).

For degree1 these are exactly n/Q for f_A/Q and0 for b_A/Q.
For higher degrees, use the fixed moment of degree m+1>=3.
Centering therefore changes each energy entry only by O_d(1/Q).
The centered energy matrix G_Q still converges to the strictly
positive G and is uniformly positive definite eventually.

Each ||w_I||2² is O_d(1/Q). For degree1 use the exact moment, and
for higher degrees use the moment of degree2m>2 in (4). NO false
second-moment profile limit is needed. In particular the second
moment's known noise contribution does not create a gap here.

Write any allowed polynomial witness as

    q=a0+sum_I a_I*w_I, a0=<q>.

The coefficients may depend on Q. Then

    <D_A*q²>=a^T*G_Q*a+2a0*c^T*a
                >=-a0²*c^T*G_Q^-1*c>=-C_d*a0²,
    <q²>=a0²+||sum_I a_I*w_I||2²>=a0².

This proves (2). If a0=0 and q!=0, positive definiteness gives
strictly positive energy. Moreover the norm matrix is O_d(1/Q)
while the energy matrix is bounded below, giving Rayleigh>=c_d*Q.
All assertions are uniform over coefficients, including arbitrarily
Q-dependent and ill-scaled polynomial combinations.

Odd phase polynomials have zero mean automatically. Thus for every
fixed d the ENTIRE odd analytic power plane
span{Im F_A^j:1<=j<=d}, and indeed the larger odd bivariate polynomial
space, has positive energy eventually. Constant, cosine/even and
sine/odd components were all included in the bounded-cap theorem.

## 5. What this says about P2 and affine phase trials

The theorem does not cover p=(lambda+F)^-1, unbounded-degree
polynomial sequences, or arbitrary Fourier coefficients. Hence it
does not falsify P2. It does show that a fixed count of polynomial
powers cannot replace that nonlinearity, even after complex phase
and optimized coefficients are retained. This extends the earlier
scalar-D positive-front obstruction rather than creating a new
family-root-bound route.

P2 remains a potentially artificial bottleneck: its truth would
force qualitative L1 flatness on strict-margin inputs, while no
converse from Chowla to this particular plane is proved. The new
Boolean identity (1) has not supplied its missing interaction bound.
It should remain a falsifiable auxiliary target, not a required
definition of success for the full goal.

The lead also proposed integer translation as a changed phase test.
There is a sharp paper warning against an uncontrolled trial. If
A0 is ANY certified low-M set with n>1, A=2A0 preserves all current
statistics and the low-M premise. But A+1 consists entirely of odd
frequencies, so

    f_(A+1)(pi)=-n, M(A+1)=n.

More generally a common period d gives translated grid values
n*cos(2pi*s*j/d). An even order d/gcd(d,s) gives the same exact
failure; an odd order>=3 gives M>=n*cos(pi/order). Tiny integer
shifts relative to max frequency therefore have no uniform low-M
guarantee. A valid Boolean translation test needs an independently
proved boundary/phase bound, not a parameter sweep. None was derived
here. The weighted smooth-taper translation heuristic is not such
a Boolean bound.

## 6. A structurally different next lemma, with completeness checked

After the fixed-degree obstruction, allow genuinely unbounded degree
rather than another fixed plane. One precise alternative is the
all-order exponential norm

    Z_A(s)=||exp(-s*F_A)||2²=<exp(-2s*f_A)>, s>0.

The potential next Boolean estimate is

    There exist absolute c,C>0 such that for EVERY A,
    some 0<s<=C*sqrt(n)*log(2n) satisfies
                 log Z_A(s)>=c*s*sqrt(n).           (6)

This is an equivalent-up-to-constants formulation of Chowla, not a
new proved estimate or a claim of a new route. It belongs to the
existing analytic/Gibbs C* programme. Its advantage over insisting
on P2 is that its completeness has an elementary quantitative check;
there is no unproved restriction to two vectors or a fixed degree.

Indeed let min f=-M at x0 and eta=M/(4n)<=1/4. The phase Bohr set

    B_eta={h: every a*h mod2pi lies within eta of0}

has Haar measure at least (eta/8)^n. Partition the phase torus into
ceil(2pi/eta)^n cubes. For independent uniform x,y, Cauchy gives
probability at least the reciprocal of that cube count that their
phase vectors share a cube. Their difference x-y is uniform and
then lies in B_eta. Since ceil(2pi/eta)<=8/eta, the bound follows.
It has no max-frequency dependence.

On x0+B_eta, f<=-3M/4, so

    log Z_A(s)>=(3/2)*s*M-n*log(32n/M).

At s=(2n/M)*log(32n/M), this gives log Z_A(s)>=s*M. Thus a
Chowla bound M>=c0*sqrt(n) implies (6) for absolute constants
depending only on c0. Conversely log Z_A(s)<=2sM makes (6) imply
M>=c*sqrt(n)/2. This proves the stated equivalence and locates the
still-unproved Boolean growth estimate precisely.

There is also an actual full-Rayleigh witness interpretation. For
E_s=exp(-sF_A), the sum of the real and imaginary energies is

    <D_A*(Re E_s)²>+<D_A*(Im E_s)²>=-Z_A'(s).

The log partition function is convex with derivative0 at s=0.
Its derivative at the displayed s is therefore at least M, and
some real or imaginary component has quotient<=-M. The real
component includes its constant; that is permitted in the full
Rayleigh problem. For arbitrary mean-zero nonconstant f, some
component already has negative energy at every s>0, so qualitative
sign alone here proves nothing. The genuine target is the growth
in (6), with unbounded-degree concentration allowed.

This is a proposed next derivation, not an instruction to compute
or an assertion that exponential coefficient cancellations are
controlled. It prevents another artificial finite-dimensional
bottleneck while keeping an exact, falsifiable Boolean target.
The independent construction track and unrestricted signed Fourier
certificates remain active alternatives. No P2 proof, Boolean P2
counterexample, new universal exponent or Chowla resolution was
obtained in this pass.

Checkpoint review: I also read the lead's complete
`cstar_phase_polynomial_obstruction_2026-10-23.md` and
`cstar_phase_five_count_2026-10-23.md` after saving this derivation.
No substantive gap was found. The corrected energy scaling, p>2
qualification, degree-two norm caveat, uniformity over perfect
difference sets, parameter-dependent polynomial coefficients, and
constant/centering completion are all retained correctly. The broader
architecture theorem is paper-proved and internally audited; novelty
and external scrutiny remain unverified. No further derivation or
computation is requested by this checkpoint review.
