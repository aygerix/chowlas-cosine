# Advisor attempt: Boolean square-root coupling and a direct-Rayleigh pivot

2026-10-21. Internal advisor paper derivation and independent audit.
Only this assigned note was edited. No research computation, VM job,
provisioning, spending, external message, or new agent was performed.
Statements below are paper proofs, not Lean/kernel-checked proofs or
external specialist review. Full unrestricted Chowla remains open.

Integrals are normalized dx/(2*pi). Let A be a finite nonempty set of
distinct positive integers, n=|A|, X=max(A), F=sum_(a in A) z^a,
D=2Re F, M=-min Re F, K=2M. Unless stated otherwise assume the ACTUAL
all-circle hypothesis M<=sqrt(n), set lambda=2sqrt(n), and use

    h=2lambda*(sqrt(1+F/lambda)-1)=sum_(j>=1) v_j z^j,
    F=h+h^2/(4lambda), q=Re h,
    a=sum_(a in A) v_a, Q=||q||_2^2,
    G=integral |lambda+F|-lambda, S=||h||_2^2.

The preceding audited note proves

    S=2Q=4lambda G,
    a>=c Q, c=1+sqrt(1-M/lambda)>=c0=1+1/sqrt(2).

The goal is a>=alpha*n for an absolute alpha>0. This attempt obtains a
quantitative but insufficient lower bound, exposes exactly which operator
estimate would strengthen it, and proves a local exchange stability
condition. None closes the missing n-scale inequality.

## 1. An actual aggregate lower bound, and why the small tests are automatic

Define the finite symmetric Hankel matrix on indices 1,...,X-1 by

    (H_A)_(u,v)=1_A(u+v).

For X=1 take this matrix to be empty with largest eigenvalue zero. Let
rho_A be its largest eigenvalue. Its entries are nonnegative and every
row has at most n ones; hence 0<=rho_A<=n. The coefficient recurrence
gives the EXACT selected cancellation identity

    n-a=(1/(4lambda))*v_<X^T H_A v_<X.

Consequently

    n-a<=rho_A*S/(4lambda)=rho_A*Q/(2lambda)
        <=rho_A*a/(2lambda*c),

and therefore

    a>=n/[1+rho_A/(2lambda*c)]
      >=n/[1+n/(2lambda*c0)].                       (1.1)

This is valid for every Boolean A in the actual low-M branch, with no
frequency bound. More generally it holds for any lambda>=2M with the
displayed c, whenever lambda>0.

At lambda=2sqrt(n),

    a/n>=4c0/[sqrt(n)+4c0].                          (1.2)

Thus the available estimate is order sqrt(n), not order n. The missing
factor is order sqrt(n); it has not been removed by using the recurrence.
The conditional operator branch rho_A<=C*lambda WOULD give macroscopic
coupling, with a>=n/[1+C/(2c0)].

This also recalibrates the previous four exact implementation tests. They
used lambda=2ceil(sqrt(n)), rather than the smaller original lambda.
Whenever n<2lambda*c0, (1.1) already forces a/n>1/2. This includes n=1,
16, 31, AND n=50 with lambda=16, since

    2lambda*c0=32+16sqrt(2)>50.

Their reported a/n>1/2 is an algebra/implementation check, not evidence
against asymptotically weak coupling. At original lambda=2sqrt(n), the
same automatic half-coupling branch includes every integer n<=46.

## 2. Falsifying the tempting uniform Hankel bridge; the exact factor gap

The operator branch rho_A=O(lambda) is false even on actual low-M Boolean
sets. For any A of n elements and X>1, the all-ones trial vector gives

    rho_A>=sum_(a in A)(a-1)/(X-1)
          >=n(n-1)/[2(X-1)].                        (2.1)

The canonical perfect-difference supports already recorded in the project
have X<=2n and M<=sqrt(n). Along that infinite sequence,

    rho_A>=(n-1)/4,

which is much larger than lambda=2sqrt(n). No specialized front asymptotic,
new family sweep, or computation is needed for this falsification.

The exact failed step is replacing the linked vector quadratic form
v^T H_A v by an O(sqrt(n))*||v||_2^2 bound on ALL vectors. The full
Hankel operator has a positive eigenvalue of order n in an admissible
Boolean control. A successful argument must exploit how this PARTICULAR
nonlinear v sits relative to the large positive eigenspace, rather than
impose a false global operator norm estimate. This is the adaptive linked
gap, not a new independent route around C*.

Even (1.1) uses less Boolean information than it first appears to. For a
nonnegative weighted F=sum p_j z^j, put E=sum p_j^2 and m=sum p_j. The
same row-sum proof gives

    a_weighted>=E/[1+m/(2lambda*c)].

Booleanity sets m=E=n, but this alone does not distinguish the weighted
escape. Indeed, for p_j=1-j/m0 on j=1,...,m0-1, rescale by

    t=(sum p_j)/(sum p_j^2)=3m0/(2m0-1).

The rescaled positive weights have sum equal to their squared sum, actual
M bounded, and G=O(log m0)=o(sqrt(E)). Some weights exceed one. Thus
nonnegativity plus equality of mass and energy is insufficient; the
individual coefficient cap at one is a genuine additional missing input.

## 3. A second attempt with coefficient idempotence: no hidden coercivity

Put b_j=[z^j] h^2/(4lambda)=1_A(j)-v_j. Boolean idempotence yields, for
example,

    a=sum_j v_j*(v_j+b_j)^2
     =sum_j v_j^3+2sum_j v_j^2 b_j+sum_j v_j b_j^2.

The norm identity is

    n=2a-S+sum_j b_j^2,
    a=(n+S-sum_j b_j^2)/2.                          (3.1)

Since |g|^2<=|F| for g=h/(2sqrt(lambda)), one gets sum b_j^2<=n.
This proves only a>=S/2=Q, weaker than the already known a>=cQ.
The cubic sums have no established sign because v and b are signed.

Coefficientwise Cauchy gives |b_j|<=S/(4lambda), which can force S to
have order lambda when the selected coefficients are near one. It cannot
force S to have order n. Equivalently, the available global row-sum
estimate in Section 1 has rho_A as large as order n. An unavailable
l1(h) bound cannot be inserted into Young's inequality; moreover h(1)
itself has order n^(3/4), so an O(lambda) l1(h) bound would already be
false for large n.

Thus the identity n-sum b_j^2=2a-S is an exact reformulation of a deficit,
not a new lower bound for it. Claiming that Boolean cubing makes this
deficit extensive would silently assume the missing result.

## 4. A quantitative deletion/exchange lemma: weak coupling is locally stable

Here G_lambda(P)=integral |lambda+P|-lambda is considered as a convex
functional of the real Fourier coefficients, with lambda FIXED. For the
initial low-M F put W=lambda+F, U=W/|W| and

    d_j=Re integral z^j*conjugate(U), j>=1.

These are its coefficient derivatives. Since |W|>=lambda-M>=lambda/2,

    sum_(j>=1) d_j^2
       <=||U-1||_2^2
        =2 integral (1-Re W/|W|)
       <=4G/lambda.                                (4.1)

The last step uses integral(|W|-Re W)=G.

For n>=9, every occupied a and unoccupied positive b satisfy

    G_lambda(F-z^a)-G_lambda(F)
       >=-d_a+1/(6912sqrt(n)),                      (4.2)

    G_lambda(F-z^a+z^b)-G_lambda(F)
       >=d_b-d_a+1/(6912sqrt(n)).                   (4.3)

These are uniform all-circle analytic inequalities, with no span bound.
The leading constants are deliberately coarse.

PROOF OF THE CURVATURE BOUND. Along either path F_t, t in[0,1], the
coefficients remain nonnegative and ||F_t||_2^2<=n. Also
Re(lambda+F_t)>=sqrt(n)-2>0, so the functional is twice differentiable.
For the path direction H,

    d^2/dt^2 G_lambda(F_t)
       =integral [Im(H*conjugate(lambda+F_t))]^2/|lambda+F_t|^3.

Let E_t={|F_t|>4sqrt(n)}. Its measure is at most 1/16, and on its
complement the denominator is at most (6sqrt(n))^3.

For deletion, H=-z^a, ||Im H||_2^2=1/2, and |Im H|<=1. Thus the
norm of lambda Im H on E_t's complement is at least sqrt(7n)/2.
The opposing term Im(H*conjugate(F_t)) has norm at most sqrt(n).
Their difference has norm greater than sqrt(n)/4.

For exchange, H=z^b-z^a, ||Im H||_2^2=1 and |Im H|<=2. The first
term on the complement has norm at least sqrt(3n). If p_j are the
nonnegative coefficients of F_t, then

    ||H F_t||_2^2
       =2sum_j p_j^2-2sum_j p_j*p_(j+b-a)<=2n.      (4.4)

Thus the opposing term has norm at most sqrt(2n), and
sqrt(3)-sqrt(2)>1/4 again leaves a norm greater than sqrt(n)/4.
This autocorrelation inequality is the key improvement over the naive
bound |H|<=2. Consequently both second derivatives are at least

    (n/16)/(216n^(3/2))=1/(3456sqrt(n)).

Integrating with weight 1-t proves (4.2)--(4.3).

These lemmas do NOT prove flatness. In fact they identify a pitfall in a
one-deletion or one-exchange minimal-counterexample argument. Set

    J_bad={j>=1: |d_j|>1/(27648sqrt(n))}.

By (4.1),

    |J_bad|<=2*27648^2*(G/sqrt(n))*n.                (4.5)

If a hypothetical weak-coupling sequence has a/n->0, then
G/sqrt(n)<=a/(4c0*n)->0. Hence |J_bad|=o(n). Every deletion at an
ordinary occupied index, and EVERY swap whose two endpoints avoid
J_bad, INCREASES G_lambda by at least 1/(13824sqrt(n)). Only o(n)
positive indices are exceptional, including outside A. Thus weak
coupling would be compatible with strong local deletion and exchange
stability; minimality alone supplies no contradiction.

Endpoint swaps need not retain M<=sqrt(n). The inequality holds in the
larger neighborhood where the displayed positive real-part bound applies;
it therefore also holds for any swaps that do retain the low-M condition.
Weighted positive profiles have analogous differential curvature bounds.
The Boolean feature here is that a FULL unit deletion/swap is available
and preserves nonnegative coefficients and the squared-norm bound.

There is also a global necessary size for a correlated move. If A' has n
elements, replaces m frequencies, and G_lambda(F_A')<=(1-theta)G_lambda(F_A)
with theta in(0,1), convexity and (4.1) give

    G_lambda(F_A')-G_lambda(F_A)>=-sqrt(8mG/lambda),
    m>=theta^2*lambda*G/8=theta^2*G*sqrt(n)/4.       (4.6)

This is a concrete constraint on a finite adversary: a prescribed
fractional G improvement cannot come from exchanges below that scale.
It is not an existence theorem for an improving move, or an n-scale
Boolean coupling estimate.

### A conditional collective-move branch with exact additive hypotheses

The root proposed this extension and the advisor independently checked
each constant. It is a useful next structural hypothesis, not a flatness
proof. Suppose A and A' both have n elements and ACTUAL M<=sqrt(n).
Let H=F_A'-F_A, m=|A\A'|=|A'\A|, and s=||H||_2^2=2m>0. Suppose an
absolute L>=1 satisfies

    ||H||_4^4<=L*s^2,
    ||H F_A||_2^2<=n*s, ||H F_A'||_2^2<=n*s.        (4.7)

For lambda=2sqrt(n), define

    c_L=1/[16*(2+16sqrt(L))^3].

Then

    G_lambda(F_A')-G_lambda(F_A)
       >=c_L*m/sqrt(n)-sqrt(8mG/lambda).            (4.8)

PROOF. Along F_t=(1-t)F_A+tF_A', the coefficients are nonnegative,
||F_t||_2^2<=n, Re(lambda+F_t)>=sqrt(n), and by convexity of the product
norm ||H F_t||_2^2<=n*s. Trim E_t={|F_t|>R sqrt(n)} with R=16sqrt(L).
Its measure is at most R^(-2). Holder and (4.7) give

    integral_(E_t) (Im H)^2
       <=integral_(E_t)|H|^2<=sqrt(L)*s/R=s/16.

Since H is analytic with zero constant, ||Im H||_2^2=s/2. On the
complement the lambda Im H term has norm at least sqrt(7ns)/2. The
opposing Im(H*conjugate(F_t)) term has norm at most sqrt(ns). The
difference is greater than sqrt(ns)/4, while the denominator in the
second derivative is at most (2+R)^3 n^(3/2). Thus the Hessian is at
least c_L*s/sqrt(n). Taylor's integral supplies half this curvature,
namely c_L*m/sqrt(n). Bound the initial directional derivative below
using (4.1) to obtain (4.8).

Consequently any nonincreasing move satisfying (4.7) must have

    m<=4G*sqrt(n)/c_L^2.                            (4.9)

Together with (4.6), a theta-fractional improvement in this class requires

    theta^2*G*sqrt(n)/4<=m<=4G*sqrt(n)/c_L^2.

If G=o(sqrt(n)), a MACROSCOPIC nonincreasing move must therefore either
have unbounded signed fourth moment ||H||_4^4/s^2 or violate one of the
mixed energy bounds in (4.7). For finite sets these are exact integer
additive quantities: for example ||H||_4^4 is the sum of squares of the
signed convolution coefficients of H^2, and the other two norms are sums
of squares of coefficients of H F_A and H F_A'. No continuous-circle
sampling is needed to test these hypotheses.

The unresolved next derivation is whether high-energy correlated moves
can actually reduce G while retaining low M, or whether their additional
Boolean structure supplies a direct negative-Rayleigh certificate. The
lemma asserts neither alternative. It identifies a concrete correlation
condition that ordinary single-frequency search does not test.

## 5. Pointwise lower bounds really fail inside the actual low-M branch

The root's pointwise-prefix derivation was independently audited. If A
contains [1,b], the coefficients through b equal those of

    h_inf=2lambda*(sqrt((1-rz)/(1-z))-1), r=1-1/lambda.

For lambda>=1,

    h_inf'=(1-z)^(-3/2)*(1-rz)^(-1/2),
    0<v_j<=min(1,2sqrt(lambda/j)),
    sum_(j<=b) v_j<=4sqrt(lambda*b).                (5.1)

Indeed both derivative factors have positive coefficients. Replacing r
by one bounds the derivative coefficient by j, giving v_j<=1. The bound
[z^m](1-z)^(-3/2)<=2sqrt(m+1), and the total sum of the second factor's
coefficients at r, equal to sqrt(lambda), give the other inequality.

The recorded forced-plateau family has n_old~5L/12, b=L^(5/6), and
M_old<=70sqrt(n_old). These are existing Spencer-rounding dependencies,
not newly proved here. To put the countercontrol into ACTUAL low M,
choose the least k with N=k(k-1)/2>=10^6*n_old and form distinct positive
differences of

    B={1,(k+1),...,(k+1)^(k-1)}.

Difference uniqueness is the previously recorded elementary no-carry
fact. The square identity gives M_pad<=k/2<=(4/5)sqrt(N) for k>=5.
Moreover N is between 10^6*n_old and (10^6+3000)*n_old. A sufficiently
high dilation makes all padding frequencies exceed the old support,
preserving the prefix recurrence and ensuring disjoint supports.

For t=N/n_old>=10^6,

    70+(4/5)sqrt(t)<=sqrt(1+t),

because sqrt(1+t)-(4/5)sqrt(t) is increasing for t>=16/9 and already
exceeds 70 at 10^6. The union therefore has M<=sqrt(n_old+N) globally.
Its total n is Theta(L), lambda=Theta(sqrt(L)), and (5.1) gives

    v_b=O(L^(-1/6)), prefix coupling=O(L^(2/3))=o(n).

Thus an absolute per-occupied-frequency lower bound is false even on the
actual low-M Boolean class. This does not falsify aggregate coupling:
the large padding block can supply it. No further canonical sweep is
needed. The root separately reported a certified finite prefix example;
this advisor did not rerun that computation.

## 6. Changed mechanism: full Rayleigh bands approximate the global minimum

The root proposed the following enabling lemma, independently audited
here. It does not use low M or L1 flatness. A targeted text search in the
proof/notebook/route/code records found no existing EXACT version; no
literature-priority claim is made. Earlier full-space inverse-residual
lemmas concern a different leverage variational problem.

Let V_B be ALL real trigonometric polynomials of degree at most B,
including the constant and both cosine and sine sectors. Define

    K_B=-inf_(0!=q in V_B) integral Dq^2/integral q^2.

For every integer N>=1, B=N-1,

    0<=K-K_B<=6sum_(a in A) a^2/(2N^2+1)
              <=3nX^2/N^2.                        (6.1)

PROOF. Let c_j=(1-|j|/N)_+, so Fejer_N=sum_j c_j exp(ijx), and

    A0=sum_j c_j^2=(2N^2+1)/(3N),
    kappa_a=sum_j c_j*c_(j-a)/A0.

Translation telescoping gives

    ||c-shift_a(c)||_2^2<=a^2||c-shift_1(c)||_2^2=2a^2/N,
    0<=1-kappa_a<=a^2/(N*A0)=3a^2/(2N^2+1).

At a true global minimizer x0 choose q(x)=Fejer_N(x-x0). Its quotient is

    R=2sum_(a in A) kappa_a*cos(a*x0),
    R-D(x0)<=2sum_(a in A)(1-kappa_a)
             <=6sum a^2/(2N^2+1).

Every quotient is at least min D=-K, while the finite infimum is at
most this trial quotient. These two inequalities prove (6.1).

To capture a true K>=c*sqrt(n) to error at most (c/2)*sqrt(n), it suffices
to take N>=sqrt(6/c)*X*n^(1/4). This is a frequency-dependent approximation
theorem, NOT an unrestricted Boolean lower bound or a claim that such a
dip has been proved to exist.

For implementation the ORTHONORMAL real bases are

    even: 1, sqrt(2)cos(x),...,sqrt(2)cos(Bx),
    odd: sqrt(2)sin(x),...,sqrt(2)sin(Bx).

Write d_j=1_A(j) for j>0 and d_0=0. Multiplication by D compresses to

    T_even(0,0)=0, T_even(0,j)=sqrt(2)*d_j,
    T_even(j,k)=d_|j-k|+d_(j+k), j,k>=1,
    T_odd(j,k)=d_|j-k|-d_(j+k), j,k>=1.

The even and odd sectors decouple because D is even. Both blocks and the
constant are essential for the FULL-space K_B claim. The existing
mean-zero cosine GPU action alone is not that full compression. One may
also use the exact integer Toeplitz matrix on complex Fourier indices
[-B,B]; its least quotient equals the full real one by splitting real and
imaginary parts.

A found negative-Rayleigh vector gives a LOWER bound on K_B, hence K.
A certified finite PSD cap T_B+k_cap*I>=0 gives K_B<=k_cap; combining it
with (6.1) gives the global upper K<=k_cap+error. An unproved numerical
smallest eigenvalue is not such a PSD cap. This distinction matters for
the independent all-circle construction track.

### Saved finite evidence inspected at this checkpoint

The advisor read the saved JSON results; no producer or verifier was
rerun here. The root's Dirichlet artifact
experiments/sqrt_boolean_2026-10-21/prefix.json records 256-bit ball
agreement between the positive derivative convolution and the formal
recurrence on the saved n337,X587,prefix243 support. It gives

    v_243 in (0,1/2), approximately 0.42106801219918,
    a/n approximately 0.63456896519751.

Thus the finite pointwise half-coupling claim fails while aggregate
half-coupling survives on ONE input beyond the automatic branch. Its
actual low-M status is inherited from the prior certified global upper
28339210049/1879048192; the artifact explicitly says that upper bound
was not recomputed in this producer. This finite observation is separate
from the asymptotic pointwise falsification in Section 5.

The saved rayleigh_numpy.json records PASS for ten even/odd Fourier
actions against independent matrix/Laurent controls, four Fejer kernel
translation controls, and twelve rational finite PSD-cap/global-error
checks on analytic inputs. The operator comparisons are floating-point
checks; the PSD caps are marked exact rational checks. These validate
implementation and normalization on those controls, not a new universal
bound. In particular a tiny finite band can have K_B=0 for A={101}; its
large rigorous error in (6.1) then prevents an inaccurate global claim.
No GPU deployment or performance result is involved.

## 7. Decision and exact next gap

Two aggregate derivations were attempted: the selected Hankel quadratic
form gives (1.1), with an explicit sqrt(n) factor gap and a falsified
uniform operator shortcut; coefficient cubing gives no additional sign
or coercivity. The minimal-counterexample attempt yields a positive local
curvature theorem, but its consequence is deletion/exchange stability of
a hypothetical weak input, not a contradiction.

Keep the square-root seed as an explicit diagnostic, not an assumed
universal solver. Its four small successes lie inside the automatic
half-coupling branch. Any next finite test intended to distinguish a
universal coupling claim must lie outside that branch, use a certified
actual low-M Boolean support, and compare with the full-space certificate
instead of silently treating a weak seed as weak Chowla behavior.

For an aggregate adversary, classify correlated exchange directions via
the exact signed fourth/mixed-energy conditions (4.7), with the necessary
change scale (4.6), instead of ordinary one-swap descent. No existence of
a successful exchange is asserted. Weighted profiles and Boolean intervals
must remain distinct controls: weighted Fejer has G=O(log n_eff) under low
M, whereas the Boolean interval has linear M and violates the hypothesis.

The substantive changed proof/certification pivot is (6.1): actual full
negative-Rayleigh bands, with all parity sectors, can be compared directly
to the global minimum without the stronger L1 surrogate. The CPU action
and exact finite-PSD/global-error controls reported in Section 6 are now
complete. A new mathematical question, rather than another successful
control sweep, is required before GPU deployment. Preserve the
independent all-circle construction track. No new universal exponent,
absolute Chowla constant, or vanishing-ratio family was obtained here.
