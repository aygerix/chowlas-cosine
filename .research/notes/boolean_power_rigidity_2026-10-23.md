# Exact Boolean coefficients forbid nontrivial polynomial powers

2026-10-23. Research proof note, not a manuscript. Independently
checked on paper by the sole internal advisor; see
[the audit](advisor_boolean_norm_2026-10-23.md). No Lean/kernel
verification or external novelty claim. The preceding turn5678d00
was progress: it exposed the full coefficient equations and the
failure of phase-only relaxations. This cycle USES those exact
coefficients to prove a rigidity theorem.

## 1. Quantified theorem

Let A be any finite nonempty set of distinct positive integers,
D=maxA, n=|A|, and lambda>=M(A). Define the monic reciprocal
polynomial

    P_lambda(w)=2lambda*w^D
                  +sum_(a in A)(w^(D+a)+w^(D-a)).          (1)

Its constant and leading coefficients are1. Every coefficient
except the central one is exactly0 or1, and
P_lambda(1)=2(lambda+n)>0.

Suppose P_lambda=H^q for a REAL polynomial H and integer q>=2.
Then q=2, and exactly one of the following holds:

* A={D}, lambda=1, H=1+w^D up to the irrelevant overall sign;
* D is even, A={D/2,D}, lambda=9/8, and
  H=1+(1/2)w^(D/2)+w^D up to that sign.

In particular, no P_lambda of this form is a perfect polynomial
power of exponent>=3. No assumption of rational coefficients
of H, nonnegative coefficients of H, or optimality of lambda
is needed. The two surviving certificates automatically occur
at the actual all-circle optimum.

Scope: this excludes a single polynomial-power architecture.
It does NOT exclude general Fejer--Riesz factors |Q|^2, multiple
squares, a square with a nonconstant correction, or algebraic
mixed norm factors U^2-wV^2. It is not a proof of Chowla.

## 2. Reciprocity and local rationality are forced

Choose H monic (change its sign if q is even). Write d=degH,
so qd=2D. From H(0)^q=1 its real constant is+1 or-1.
The reciprocal identity for P_lambda gives Hrev=H or-H.
Evaluating at1 and using H(1)!=0 excludes the minus case.
Thus H(0)=1 and H is coefficient-reciprocal.

For every j<d, hence j<D unless q=2 and j<d=D, comparing
the coefficient of w^j in H^q gives

    q*H_j = (P_lambda)_j - a rational polynomial
                                  in H_1,...,H_(j-1).

All such H_j are rational, recursively. One may therefore use
finite p-adic valuations of them even when the starting H was
merely real. In the q=2 case they are dyadic rationals.

## 3. A strictly decreasing binomial valuation

Fix a prime p dividing q, and normalize v_p(p)=1. For r>=1,

    binom(1/q,r) = product_(i=0)^(r-1)(1-iq)/(q^r*r!),
    v_p(binom(1/q,r)) = -r*v_p(q)-v_p(r!).               (2)

Each numerator factor is a p-adic unit. The valuation decreases
STRICTLY when r increases: its next difference is
-v_p(q)-v_p(r+1)<0. The r=0 value is0 and fits the same ordering.

For q=2 this can also be written s_2(r)-2r, where s_2 counts
the1 bits of r. The factorial formula (2) suffices for the proof;
there is no reliance on floating root calculations.

## 4. First nonzero coefficient and the reversal contradiction

If H has no nonzero interior coefficient, H=1+w^d. Otherwise
let a be the least index1<=a<d with H_a!=0. Reciprocity gives
a<=d/2. The first nonconstant coefficient of P_lambda is
q*H_a. Since a<d<=D and it is a nonzero0/1 coefficient,

    H_a=1/q.                                             (3)

Let B(w) be P_lambda-1 truncated below degreeD. Its coefficients
are integers0or1, its first nonzero term is w^a, and its first
coefficient is1. For every j<d the formal binomial expansion

    H_j = [w^j] sum_(r>=0) binom(1/q,r)*B(w)^r            (4)

is exact. The noninteger central coefficient cannot enter these
degrees. Only r<=floor(j/a) contributes, and all coefficients
of B^r are integers.

For any k with ka<d, the r=k term at degree ka has coefficient1:
all k selected exponents must equal a. Every r<k contribution
in (4) has strictly larger valuation than (2) at k. The unique
least-valued term cannot cancel, so

    v_p(H_(ka))=v_p(binom(1/q,k)).                        (5)

At EVERY smaller positive index j<ka, there are at most k-1
factors. Hence v_p(H_j)>v_p(H_(ka)), including v_p(0)=+infinity.

If a<d/2, choose k=floor(d/(2a))+1. Then

    d/2 < ka < d,
    0 < d-ka < ka.

Equation (5) and the smaller-index bound contradict reciprocity
H_(d-ka)=H_(ka). Therefore a=d/2. Every other interior index
vanishes by minimality and reciprocity, giving

    H=1+(1/q)w^(d/2)+w^d.                               (6)

This argument permits arbitrary signs in all intermediate H_j.
The exact integer0/1 spectrum, not coefficient nonnegativity of
H, drives the valuation comparison.

## 5. Finishing all exponents

For q>=3 we have d<D, so the coefficient of w^d in P_lambda
must be0or1. For H=1+w^d it is q. For (6) it is

    q+binom(q,2)/q^2 = q+(q-1)/(2q)>1.

Both are impossible. Thus q=2 and d=D. Squaring the two
remaining shapes gives exactly the sets and lambdas in Section1.
The singleton minimum is attained at Dx=pi. For the second case,
put u=cos(Dx/2): f=2u^2+u-1, whose minimum on[-1,1] is-9/8
at u=-1/4. Both are exact all-circle statements.

Consequences: a real coefficient-palindromic spectral factor
lambda+f_A=|Q|^2, after a monomial shift, also permits only these
two sets. Endpoints force q0=qD=1/sqrt2 up to a common sign,
so P_lambda=(sqrt2*Q)^2. Anti-palindromic factors are excluded
by Q(1)!=0. Also, if every root of P_lambda lies on the unit
circle, its nonnegative circle values force even multiplicities;
it is a real square and the same classification applies.
This does not classify all-real Chebyshev roots below-1.

## 6. A separate arithmetic gate for rational actual minima

Normalize gcdA=1 before this section; dilation preserves M.
Assume the ACTUAL c=2M(A)=a/b is rational in lowest terms,
b>1. Let alpha be a unit-circle zero of P_c at the global
minimum. It is a repeated root. Neither alpha=1 nor-1 occurs
when b>1. It also zeros the integer polynomial

    G(w)=w*P_c'(w)-D*P_c(w)
        =sum_(a in A) a*(w^(D+a)-w^(D-a)),                (7)

whose leading and constant coefficients are D and-D. Thus
D*alpha and D/alpha are algebraic integers. Multiplying
c=-sum_A(alpha^a+alpha^(-a)) by D^D makes an algebraic integer.
A rational algebraic integer is an integer, proving

    b divides D^D.                                      (8)

For every p|b set e_p=v_p(b)>0. Every root beta of P_c in a
p-adic splitting field has valuation+e_p/D or-e_p/D. Indeed,
valuation0 makes the central term uniquely least; for positive
valuation the constant term can cancel only against the central
term at D*v_p(beta)=e_p. Negative valuations follow by reciprocity.

Let h be the monic irreducible polynomial overQ of alpha. Since
conjugation sends alpha to1/alpha, h is reciprocal, has constant1
and even degree2m. Its square divides P_c, so m<=D/2. For each
p, exactly m roots of h have negative valuation and m positive.
In the coefficient of w^m of h, the elementary-symmetric term
choosing ALL negative-valuation roots is the UNIQUE least-valued
term, of valuation-m*e_p/D. This coefficient is rational, so

    D/gcd(D,e_p) divides m.

Using the SAME m for all denominator primes, set

    g=gcd(D,{e_p:p|b}).

Then D/g divides m, hence g>=2. In particular b is a perfect
g-th power for a divisor g of D. If g=2, h has degreeD and
P_c=h^2. The theorem above forces the primitive set A={1,2},
c=9/4,b=4. Consequently for n>=3, any nonintegral rational
c requires

    g>=3.                                              (9)

The same conclusion rules out ANY individual gcd(D,e_p)=2.
For prime primitive D=ell, (8) forces b1 or ell^ell; for n>=3
and D a power of2, a nontrivial denominator must be a perfect
fourth power. These are arithmetic constraints, not an
archimedean bound on M. Irrational actual minima remain outside
this section, as do arbitrary rational upper certificates.

Dependencies beyond rational polynomial algebra: ordinary
algebraic-integer facts and an extension of v_p to a splitting
field. The root-valuation assertion was derived above directly;
no unchecked numerical Newton polygon is used.

## 7. Universal number-field version, without rational-M assumptions

The denominator argument also applies to arbitrary actual minima.
The critical root alpha zeros (7), so c=2M(A) is algebraic and
D^D*c is an algebraic integer, with no rationality assumption.
Let K=Q(c) in its chosen real embedding, and O_K its ring of
integers. Define the denominator ideal

    d(c)=product_(finite primes v) p_v^max(0,-v(c)),

where each v is normalized to have value groupZ. It divides
(D)^D. Suppose d(c)!=1 and set e_v=-v(c)>0 at its prime factors.
The minimal polynomial h of alpha over K is reciprocal of even
degree2m and h^2 divides P_c. This does NOT require K to be
totally real: complex conjugation fixes its chosen real embedding.

The same coefficient argument as Section6 gives D|m*e_v for
every denominator place. Consequently, with

    g=gcd(D,{e_v:v(c)<0}),

one has g>=2. If g=2 the real-power theorem forces the two-
frequency case. For every n>=3 with nontrivial denominator ideal,

    g>=3, g|D, and d(c) is a perfect g-th IDEAL power.     (10)

This is a constraint for EVERY Boolean A, including irrational
M. It neither controls the archimedean size of c nor treats the
case c algebraically integral. Perfect ideal power does NOT mean
a denominator element is a perfect power; no principal-ideal or
class-group assumption is being smuggled into (10).

Only prime ideals above rational primes dividing D can occur.
For prime D=ell, each nonzero e_v is a multiple ofell, bounded
by ell*v(D). Ramification prevents replacing this statement by
the single rational exponentell in the general number-field case.

## 8. Exact finite cross-check and decision

src/boolean_reciprocal_square.py completely enumerated first-half
coefficient bits for every even degree2..24, allowing signed
rational H and arbitrary central coefficients. All8190 bit vectors
were examined; exactly two shapes survived at each degree.
Direct polynomial squares and separate autocorrelations agree.
Exact Chebyshev/Sturm root counts certify unit-circle zeros and
the actual M for all24 survivors. Artifact:
experiments/boolean_square_2026-10-23/enumeration.json.
This finite check corroborates the argument; it does NOT prove
the unrestricted-degree theorem. Job terminal/PASS on Dirichlet,
2cores/4GB/180s cap; no GPU or VM lifecycle action.

Stop expanding this enumeration or optimizing a single perfect
power certificate. The full rigidity theorem already settles
that entire architecture. General real factors remain possible
and require phase asymmetry for n>=3.

First next derivation: carry the least-valuation argument into a
genuinely mixed expression2K*Krev*(U^2-wV^2). Determine precisely
how its second term can cancel the unique least-valued coefficient,
or use such cancellation to construct a new Boolean family. Do not
assume the square theorem excludes mixed norms, multiple factors,
or the full Chowla problem. Retain unrestricted signed Rayleigh
and all-scale susceptibility as distinct universal tracks.

An explicit warning against that overextension is already available.
For any real r, take U=1+((1+r^2)/2)w+w^2, V=r(1-w). Then

    U^2-wV^2=w^4+w^3
          +(9/4+(5/2)r^2+r^4/4)w^2+w+1.

This is the exact Boolean A={1,2} with a valid upper certificate
lambda=9/8+(5/4)r^2+r^4/8. The first outer coefficient stays1
because 2U_1-V_0^2=1: the second square cancels precisely where
the pure-power proof needed a unique least term. For r!=0 it is
nonoptimal, with constant canonical K=1/sqrt2 and
Q2=(U(z^2)+zV(z^2))/sqrt2. At r=0 the canonical common factor
changes, while the algebraic square limit remains valid.
At r=1/3, 2lambda=205/81 has a denominator prime3
despite D=2; this does not contradict Sections6--7, which concern
the ACTUAL minimum only. This fixed two-frequency family is a
mechanism check, not a growing construction or a new record.

Global decision: continue only if a quantitative use of the mixed
coefficient equations survives such cancellation, or a construction
actually increases cardinality with a certified smaller ratio.
Do not extrapolate exact nonvanishing of phase to a root-scale
energy gap. A quantitative stability statement would need its
own proof and adversarial tests, especially against the known Bu
near-square family. All current conclusions remain scoped above.
