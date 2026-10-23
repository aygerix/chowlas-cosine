# Exact Boolean coefficients: perfect-power rigidity and algebraic-minimum gates

2026-10-23. Sole internal AI advisor. The lead's new coefficient and
arithmetic arguments were independently checked on paper; the common-
denominator refinement below was also derived in this audit. Only this
assigned note is edited. No computation, VM action, GPU, extra agent or
outreach. Shared Dirichlet remains on. No external novelty or Lean claim.

## 1. Concrete result and exact scope

Let A be a nonempty finite set of DISTINCT positive integers, D=max(A),
n=|A| and lambda>=M(A). Define the monic reciprocal polynomial

    P_A(z)=2lambda*z^D+sum_(a in A)(z^(D+a)+z^(D-a)).

Its degree is2D, its endpoints are1, every off-center coefficient is
EXACTLY0 or1, and P_A(1)=2(lambda+n)>0.

THEOREM. If P_A=H^q for a real polynomial H and integer q>=2, then
q=2, and the only possibilities are

    H=1+z^D,
       A={D}, lambda=1;

    H=1+(1/2)*z^(D/2)+z^D, D even,
       A={D/2,D}, lambda=9/8.                    (1)

The sign of a square root can be changed; H in(1) is normalized monic.
There is NO real polynomial perfect power of exponent q>=3.
No rationality, coefficient nonnegativity or prior optimality of the
factor is assumed. The conclusion forces lambda=M(A) in both cases.

This is a genuine full-coefficient rigidity result. It is NOT a
universal lower bound on M(A): a general factorization uses Q*Qrev,
or the canonical K*Krev*(U^2-zV^2), rather than a perfect power.

## 2. Automatic normalization, reciprocity and rationality

Suppose P_A=H^q. Since P_A is monic, normalize H monic (change its sign
when q is even if necessary). If d=deg(H), then q*d=2D and d<=D.
The endpoint gives H(0)^q=1. Reversal of P_A gives

    (Hrev)^q=H^q.

Over real polynomials Hrev=H, or for even q possibly Hrev=-H.
The latter forces H(1)=0 and contradicts P_A(1)>0. Thus Hrev=H
and H(0)=1. In particular H is reciprocal and real, with endpoints1.

Writing h_j=[z^j]H, for1<=j<d the coefficient recursion is

    q*h_j=[z^j]P_A - a polynomial with integer coefficients
                            in h_1,...,h_(j-1).

All these [z^j]P_A are0 or1 because j<d<=D. Hence every h_j is
rational by induction. Rationality is therefore automatic; no
assumption on lambda or a chosen spectral branch was used here.
For q=2 these coefficients are dyadic rationals.

## 3. Strict valuation dominance proves the classification

If H has no nonzero interior coefficient it is1+z^d. Otherwise let
a be its FIRST nonzero interior index. Reciprocity gives a<=d/2.
The coefficient of P_A at a is q*h_a and is a nonzero bit, so

    h_a=1/q.

Put W=P_A-1. As a formal power series, with constant root+1,

    H=(1+W)^(1/q)
      =sum_(r>=0) binom(1/q,r)*W^r.              (2)

Only finitely many terms enter any given coefficient. No analytic
convergence or pointwise branch assertion is being made. Below degree
D, W has INTEGER bit coefficients, with first nonzero coefficient1
at a. Its possibly noninteger central coefficient cannot enter a
calculation at degree j<d<=D.

Choose a prime p dividing q. For r>=1, the numerator factors
1-i*q of binom(1/q,r) are all p-adic units. Therefore

    v_p binom(1/q,r)=-r*v_p(q)-v_p(r!),

and the difference at consecutive r is
-v_p(q)-v_p(r+1)<0. These valuations are STRICTLY decreasing.
For q=2 the equivalent formula is s_2(r)-2r; it follows from
v_2(r!)=r-s_2(r). Only strict decrease is needed.

At any index k*a<d, the largest possible r in(2) is k. The coefficient
of W^k at k*a is exactly1. All smaller-r contributions are INTEGER
multiples of binom(1/q,r), and have strictly higher valuation.
Thus the unique term of least valuation cannot cancel:

    v_p(h_(k*a))=v_p binom(1/q,k).                (3)

At ANY positive j<k*a, all possible r are at most k-1, so
v_p(h_j) is strictly greater than the right side of(3), or infinity
if h_j=0. The r=0 term contributes0 at these positive indices.

If a<d/2, choose k=floor(d/(2a))+1. Then

    d/2<k*a<d,
    0<d-k*a<k*a.

Reciprocity requires h_(d-k*a)=h_(k*a), contradicting the strict
valuation comparison. Therefore a=d/2. All later interior indices
reflect to indices below a and must vanish. Hence the ONLY two shapes
are

    H=1+z^d,
    H=1+(1/q)*z^(d/2)+z^d, d even.              (4)

If q>=3, d=2D/q<D. The OFF-CENTER coefficient [z^d]P_A is
q in the first case and

    q+binom(q,2)/q^2=q+(q-1)/(2q)

in the second case. Both exceed1, contradicting its bit value.
Thus q=2, d=D, and(4) yields exactly(1).

The first case has P_A=1+2z^D+z^(2D), and the second has off-center
exponents0,D/2,3D/2,2D with center9/4. Their cosine minima follow
exactly from cos(x)>=-1 and

    cos(x)+cos(2x)=2*(cos(x)+1/4)^2-9/8.

So the required all-circle optimal values really are1 and9/8,
including after frequency dilation. Signed interior H coefficients
were allowed throughout the proof; none was discarded by a
positivity assumption.

## 4. Spectral consequences and limits

A real spectral factor with reciprocal coefficients after trimming
a monomial phase makes P_A a real square after normalization by
sqrt(2). Anti-reciprocal coefficients are impossible because Q(1)!=0.
Thus only the two supports in(1) admit such a real linear-phase factor.
This term means coefficient reversal symmetry, not arbitrary real
Fejer--Riesz factorization.

If every root of P_A lies on the unit circle, circle nonnegativity
forces each root multiplicity to be even: its order along z=exp(ix)
is the same as its polynomial multiplicity, and a nonnegative real
analytic function has even zero order. The half-multiplicity root
multiset is closed under conjugation, giving a monic REAL square
root. Therefore again only the two cases in(1) occur. The presence
of circle roots already forces lambda=M(A).

This does NOT classify every real-rooted Chebyshev polynomial
lambda+sum T_a(T). Such a polynomial can have real roots below-1,
corresponding to negative real reciprocal roots off the unit circle.
The known three-harmonic control is not contradicted. No lengthy
classification of that broader specialized class was attempted.

## 5. Rational actual minima: the derivative polynomial

Now assume lambda=M(A), write c=2M(A)=u/b in lowest terms,
b>=1, and normalize gcd(A)=1 by dilation invariance. Keep D=max(A)
in this primitive normalization. Define

    P_c(z)=z^D*(c+sum_(a in A)(z^a+z^(-a))),
    G(z)=z*P_c'(z)-D*P_c(z)
        =sum_(a in A)a*(z^(D+a)-z^(D-a)).        (5)

At a global minimizer, alpha=exp(ix0) is a root of both P_c and G.
The derivative in x vanishes. Since alpha!=0, P_c'(alpha)=0,
so alpha is a REPEATED root of P_c. The integer polynomial G has
leading coefficient D and constant-D, independently of c.

It follows that D*alpha is an algebraic integer: substituting
y=D*alpha into G and multiplying by D^(2D-1) gives a monic
integer polynomial. The anti-reciprocity of G gives the same
assertion for D/alpha. For every a<=D,

    D^D*alpha^(plus/minus a)
       =D^(D-a)*(D*alpha^(plus/minus1))^a

is integral. Thus D^D*c is both rational and an algebraic integer,
and is an integer. Consequently

    b divides D^D.                               (6)

This is a constraint on RATIONAL actual minima. It says nothing
about a denominator for an irrational minimum and imposes no
uniform lower bound on M(A).

## 6. Reciprocal minimal factor and exact denominator exponents

Suppose b>1, fix a prime p dividing b and put e_p=v_p(b)>0.
In b*P_c the central coefficient u is a p-adic unit, and ALL
nonzero off-center coefficients equal b with valuation e_p.
Its endpoints are b. Thus its Newton polygon has the two slopes
plus/minus e_p/D, and every root has valuation plus/minus e_p/D.

An elementary verification avoids any ambiguity about the polygon:
if a root has positive valuation t, the smallest off-center term
valuation is the constant e_p, so cancellation requires Dt=e_p.
If t<0 the smallest off-center term is the leading one, giving
Dt=e_p+2Dt. If t=0 the central term alone has valuation0, which
is impossible. This proves the claimed two root valuations.

Let h be the MONIC minimal polynomial over Q of the complex unit
root alpha. Since alpha^(-1)=conj(alpha) is also a conjugate, h
is reciprocal up to a scalar. Its root multiset is closed under
inversion. At the prime p its roots all have valuation plus/minus
e_p/D, hence their counts are equal. Write deg(h)=2m. Repeatedness
of alpha and separability in characteristic0 imply h^2 divides P_c,
so m<=D/2.

The key integrality step MUST NOT claim that the product of just
one valuation group is rational. Instead inspect the coefficient
of z^m in the rational monic h. Its elementary-symmetric sum has
one UNIQUE term of least valuation: choose all m roots of negative
valuation. That term has valuation -m*e_p/D. Every other subset
replaces at least one such root by a positive-valuation root,
strictly increasing the valuation. No cancellation is possible.
The coefficient is rational, so its p-adic valuation is an integer.
It follows that

    D/gcd(D,e_p) divides m,
    gcd(D,e_p)>=2.                               (7)

The same h and m apply at EVERY denominator prime. Therefore

    lcm_(p|b)[D/gcd(D,e_p)]
       =D/gcd(D,{e_p:p divides b}) divides m.

In particular the COMMON gcd

    g=gcd(D,{e_p:p divides b}) >=2.               (8)

This strengthens separate per-prime tests. For example D=6 with
e_2=2,e_3=3 would pass both individual >=2 conditions but fails
the common one. Equivalently b must be a perfect g-th power for
some divisor g>=2 of D, with the support/exponent limits in(6).

For primitive D=ell prime, (6)--(7) give exactly the necessary
alternatives

    b=1 or b=ell^ell.                            (9)

This does not assert the second alternative is attained.

## 7. Combining the two genuine coefficient gates

If g=2 in(8), the divisibility forces m=D/2, hence deg(h)=D.
Since h^2 divides the monic degree2D polynomial P_c, one has
P_c=h^2. For completeness h is monic RECIPROCAL, not anti:
inversion gives hrev=h(0)*h, so h(0)^2=1; the minus case would
force h(1)=0, impossible since P_c(1)>0. The square theorem applies.

The singleton case has integer c=2. The other case is
A={D/2,D}, c=9/4. In primitive normalization it is exactly

    A={1,2}, D=2, c=9/4, b=4.                    (10)

Thus this is the ONLY primitive noninteger rational-minimum case
with common denominator gcd g=2. Any other primitive A with b>1
must have g>=3. In particular the weaker hypothesis that even ONE
prime has gcd(D,e_p)=2 already forces(10). Odd denominator primes
cannot realize that boundary case.

Example(10) verifies the endpoint of the argument: P_c equals
(z^2+z/2+1)^2, its unit-root minimal polynomial has degree2, and
the denominator4 attains b=D^D. This is an analytic boundary
check, not a finite search supporting an asymptotic assertion.

## 8. Verification status and decision

These are complete paper proofs and independent internal audits.
I read the full parent boolean_power_rigidity_2026-10-23.md note,
src/boolean_reciprocal_square.py and the saved
experiments/boolean_square_2026-10-23/enumeration.json. The source
enumerates every first-half bit vector for even H degrees2..24,
reconstructs signed rational H by the coefficient recursion, and
tests all remaining outer coefficients. The8190 bit vectors yield
exactly24 survivors, two per degree, with no other shapes.
Direct polynomial squares and a separately summed autocorrelation
match. Every saved unit-circle-root flag is true, with an exact
Chebyshev/Sturm check of the all-circle optimum. The enumeration
is complete in its stated finite scope; no numerical-minimum
inference or unannounced positivity restriction appears.

I did not execute that verification. It corroborates, and does
not prove, the arbitrary-degree theorem. The general q-power
theorem needs no new enumeration at q=3 or4. No substantive gap
was found in the parent's proof, prime-denominator statements or
power-of-two denominator corollary. No result here is called
kernel-checked or externally novel.

The proofs use the EXACT off-center0/1 coefficients and the central
exception explicitly. Positivity, a coefficient cap or generic
phase jets cannot substitute for their integral arithmetic. This
closes real perfect-power and reciprocal-factor construction
mechanisms, and gives a new rational critical-value obstruction.

It does not close the general K*Krev*(U^2-zV^2) coefficient problem,
prove a universal Chowla exponent or produce a vanishing family.
Integer actual minima are unaffected by the denominator gate.
Sections5--7 are its rational specialization; Section9 below
removes the rationality restriction using denominator ideals.
The next step must retain phase
and the mixed norm coefficient equations or use an independent
construction mechanism. Do not extend a specialized real-root
classification or another finite control sweep in place of that
remaining arbitrary-support task. Shared resources were untouched.

## 9. Universal algebraic denominator-ideal corollary

The parent's number-field extension is sound and removes the
rational-M hypothesis. Let A be ANY nonempty Boolean support,
D=max(A), c=2M(A) and K=Q(c), taken in its actual real embedding.
The critical polynomial G in(5) first proves alpha algebraic,
hence c algebraic and K a number field. The same scaled-integrality
argument, without any rationality step, proves

    D^D*c belongs to O_K.                         (11)

For every nonzero prime ideal p of O_K, normalize its valuation
v_p so v_p(K^*)=Z. Let e_p=max(0,-v_p(c)), and let

    den_K(c)=product_p p^(e_p)

be the integral denominator ideal. Only finitely many e_p are
nonzero. Equation(11) gives

    den_K(c) divides (D)^D,
    e_p<=D*v_p(D).                                (12)

In particular its prime ideals lie above rational primes dividing D.

If this ideal is nontrivial, define

    g=gcd(D,{e_p:e_p>0}).

Then g>=2, and

    den_K(c)=J^g, g divides D,                    (13)

for an integral ideal J. If g=2, necessarily

    A={d,2d} for some positive integer d,
    c=9/4, K=Q.                                  (14)

Consequently, for EVERY support with n>=3, its denominator ideal
is either trivial or a perfect g-th power with some divisor
g>=3 of D. Frequency dilation may first be removed to use the
strongest primitive value of D; c and its field K do not change.

### Proof and the embedding/valuation checks

K need not be totally real. What is required is the CHOSEN
embedding K subset R, which holds because c is the actual real
minimum value. Complex conjugation on C fixes every element of
this embedded K and sends the unit root alpha to alpha^(-1).
Thus the monic minimal polynomial h of alpha over K is reciprocal
up to a scalar, exactly as in the rational proof. If a denominator
place is negative, alpha cannot equal plus/minus1: those values
would give an integer c. Hence h has constant1 and even degree2m.
These are algebraic identities over K and remain valid in every
completion; no assumption is made that other embeddings of c are
real, positive or actual minima.

Repeatedness of the global unit root implies h^2 divides P_c
over K, so m<=D/2. Fix ANY negative place v with e=-v(c)>0,
normalized to have integer value group on K. The off-center
coefficients of P_c are0 or1, and its endpoints1 are units.
For a root beta in an algebraic closure of K_v, positive valuation
t requires cancellation of the constant and central terms,
so Dt=e. Negative valuation requires cancellation of the leading
and central terms, giving t=-e/D. Valuation0 leaves the central
term uniquely least and is impossible. Thus ALL h roots have
valuation plus/minus e/D. Reciprocity pairs them, m of each.

In the coefficient of z^m of h, the product of all m negative-
valuation roots is the UNIQUE least-valued elementary-symmetric
term. The coefficient therefore has valuation -m*e/D. It belongs
to K, whose chosen normalized valuation is integral, so

    D divides m*e.

This does not assume that the individual group product belongs
to K. It only uses its unique least valuation in a coefficient
that DOES belong to K. The same h and m work simultaneously at
all negative places. Therefore D/g divides m<=D/2, proving g>=2.
The ideal factorization in(13) is obtained by dividing every
negative exponent by g.

If g=2, degree(h)=D and the monic degree2D P_c must equal h^2.
Although its coefficients initially lie in K, their actual real
embedding makes it a REAL square. The real-power theorem applies
without a rational coefficient assumption. It leaves only the
singleton or two-harmonic case; the singleton has integral c=2
and is excluded by the nontrivial denominator hypothesis. This
proves(14) and the n>=3 conclusion.

### Scope that must be retained

A perfect power IDEAL need not be principal, and(13) does not
assert a denominator generated by a g-th-power ELEMENT. There
is no total-reality or Galois hypothesis on K. For prime primitive
D=ell, every nonzero e_p is a positive multiple of ell, bounded
by ell*v_p(ell). Ramification can make v_p(ell)>1; one must NOT
copy the rational conclusion that the only nonzero exponent is
ell. The old b=ell^ell alternative is its K=Q specialization.

This is a universal arithmetic constraint on actual minima, not
an archimedean lower bound. Algebraic-integer c is unaddressed,
and the condition gives no size bound on a nonintegral c. It
constrains exact algebraic constructions and factorizations while
leaving the unrestricted mixed phase problem open. The corollary
was independently audited on paper; no computational examples,
new searches, VM operations or formal verification were used.

## 10. Explicit mixed cancellation prevents an automatic extension

The parent's short mixed-norm countercontrol is correct. For real r set

    U=1+[(1+r^2)/2]*w+w^2,
    V=r*(1-w).

Then exactly

    U^2-w*V^2
      =w^4+w^3+[9/4+(5/2)r^2+r^4/4]*w^2+w+1.   (15)

Writing u1=(1+r^2)/2, the FIRST outer coefficient is
2*u1-r^2=1: the two terms cancel at the coefficient level.
The square proof's unique-least-term argument cannot be copied
while discarding the second norm term.

To match the canonical normalization P_A=2K*Krev*(U^2-wV^2),
take the constant K=1/sqrt(2). Thus

    Q_2=[U(z^2)+z*V(z^2)]/sqrt(2)

is an exact factor for the DOUBLED set2*{1,2}, with the same
all-circle minimum convention, and certifies for A={1,2}

    lambda=9/8+(5/4)r^2+r^4/8.

The displayed values lambda=5/2 at r=1 and lambda=205/162
at r=1/3 check. For r!=0, U and V are coprime because V's
only root is1 and U(1)>0. Their mixed norm is strictly positive
on the whole circle. More explicitly, with T=(w+w^(-1))/2,

    w^(-2)*(U^2-wV^2)
       =4*(T+1/4)^2+(5/2)r^2+r^4/4>0.

Consequently lambda is STRICTLY larger than actual M({1,2})=9/8.
There is no extra boundary zero, no improved construction and
no infinite-cardinality assertion. At r=0 the family limits to
the classified square; the canonical gcd then becomes nonconstant,
so it should not be described as a nontrivial constant-K mixed
decomposition at that endpoint.

This also sharply checks the arithmetic hypotheses: at r=1/3
the NONOPTIMAL upper certificate has c=2lambda=205/81 and
D=2. Its denominator is supported at3 rather than at2. That is
not a counterexample to the actual-minimum gate; it demonstrates
why that gate cannot be applied to arbitrary rational upper
certificates. Adding a unit-circle-zero common factor can restore
boundary optimality for a new symbol, but does NOT automatically
preserve any off-center Boolean coefficients.

I reread the parent's final rational and number-field Sections6--7.
No major objection remains: the normalized valuation, chosen real
embedding, common-degree, perfect-ideal-power and ramification
qualifications are all correct. This mixed example is a concise
handoff barrier to overextending the power theorem, not a new
calibration or an instruction to launch another experiment.
Only this advisor note was edited; no computation or VM action.
