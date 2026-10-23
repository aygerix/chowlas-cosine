# P2 coupling: phase-defect SOS, a sharper sign branch, and a generic obstruction

2026-10-23. Sole internal AI advisor. Independent paper derivations,
read-only research-record inspection and this assigned note only. No
research computation, VM operation, GPU spending, extra agent or outreach.
Shared Dirichlet is left running. No new Lean/kernel-checked proof.

## 1. Exact domain and genuinely new conclusions

Let A be a nonempty finite set of distinct positive integers, n=|A|,
F=sum_A z^a, f=Re F, b=Im F, M=-min_circle f. Assume ACTUAL
M<=sqrt(n), fix lambda=2sqrt(n), and use probability Haar averages.
Write

    W=lambda+F, p=1/W, zeta=F/W=1-lambda*p,
    g=||zeta||2^2=lambda^2*||p||2^2-1>0,
    C1=<F,p>, C2=<F^2,p>, T=<F,p^2>,
    t=<F,F^2>, H0=<2f*(Im p)^2>, h=lambda*H0.

All coefficient pairings displayed here are real. The inverse is
analytic on a neighborhood of the closed disk because Re W>=lambda/2.
Schwarz's bound |zeta|<=1 follows from lambda^2+2lambda*f>=0.
The old exact identities are

    Q0=||Im p||2^2=g/(2lambda^2),
    H0=-g/lambda-T/2,
    C1=-2< b^2/|W|^2> <0,
    Eodd=[[t/2,C2/2],[C2/2,H0]].

For t>0 original odd P2 is C2^2>=2tH0; t=0 is already settled
by its first basis vector. No proof or Boolean falsifier of this
full odd determinant is obtained here.

There are NEW quantitative, fully proved intermediate results:

* An exact phase-retaining squared-norm identity and automatic bound
  H0/Q0<=lambda/2.
* Orthogonal constant/negative-frequency projections give a coupled
  constraint on g,C1,H0 and prove H0<0 whenever g>=4/25, improving
  the old generic sufficient branch g>9/16.
* Both parity planes can be tested by a joint inequality eliminating
  C2 and H0. Their simultaneous failure requires a quantified
  high-triple/weak-gap regime.
* A geometric positive-coefficient model makes BOTH planes positive
  at actual coefficient-L2 calibration. Thus these generic constraints
  do not imply the missing Boolean theorem.

The new inequalities are GENERIC analytic consequences at the stated
norm calibration. They do not yet exploit exact zero/one coefficients.

## 2. A phase-retaining SOS identity, not a modulus surrogate

Define the generally nonanalytic boundary function

    K=(F^2+lambda*conjugate(F))*p^2.

For every complex value F=f+ib and real lambda>0,

    |F^2+lambda*conjugate(F)|^2
       =(b^2-f(lambda+f))^2+b^2(lambda-2f)^2.

Also direct expansion gives

    |F|^2*|W|^2-|F^2+lambda*conjugate(F)|^2
                  =8lambda*f*b^2.

Divide by |W|^4 and integrate. The result is the exact identity

    ||K||2^2 = g-4lambda*H0 = g-4h.                (1)

This retains the Re(F^3) cross phase in the numerator. It neither
replaces F by |F| nor assumes a sign for a selected coefficient.
It immediately proves

    lambda*H0<=g/4,
    H0/Q0<=lambda/2.                              (2)

Thus the exceptional zero carrier has an automatic root-scale UPPER
cost at lambda=2sqrt(n), despite its potentially unbounded normalized
amplitude. Its lower Rayleigh bound is the usual -2M. Equation(2)
does not supply the missing negative sign.

For t>0 the odd P2 target can equivalently be written

    ||K||2^2+(2lambda/t)*C2^2 >= g.               (3)

Only the nonnegativity of the first term is automatic. Rewriting
P2 as(3) is not itself progress. The proved consequences(2) and
the projection estimate below are the extra information.
In particular a positive-determinant odd-plane falsifier necessarily
satisfies the stricter gate

    H0>0,  C2^2<t*g/(2lambda).                    (4)

## 3. Two orthogonal Fourier projections and the 4/25 sign branch

The constant Fourier coefficient of K is

    <K,1>=lambda*T=-2(g+h).                       (5)

Indeed F^2*p^2 is analytic with zero constant, leaving
lambda<conjugate(F)*p^2>=lambda*T. Bessel gives

    g-4h>=4(g+h)^2.

Already this forces H0<0 at g>=1/4: the upper root is

    h <=[sqrt(1+5g)-1-2g]/2.

For nonconstant F the constant projection is strict, since K cannot
be constant: multiplying a purported constant equality by W^2
would leave nonzero negative Fourier coefficients lambda*conjugate(F)
on one side and none on the other.

A second orthogonal test gives a stronger coupled bound. Since
1 and conjugate(F) are orthogonal and ||F||2^2=n,

    <K,conjugate(F)>
       =lambda<|F|^2*p^2>
       =lambda*(C1-lambda*T)
       =lambda*(C1+2g+2h).

Here the analytic F^3*p^2 term has zero mean, and
F*p^2=p-lambda*p^2 supplies the middle identity. Therefore

    g-4h >=4(g+h)^2
                +(lambda^2/n)*(C1+2g+2h)^2.

At the exact calibration lambda^2=4n this becomes

    g-4h >=4(g+h)^2+4(C1+2g+2h)^2.               (6)

This uses the FULL norm of K and hence the FULL inverse. It is not
a finite-band residual calculation. The same proof holds for real
weighted analytic F if n is replaced by ||F||2^2 and lambda is
calibrated accordingly; this scope matters in Section7.

Coefficient Cauchy gives

    |C1|<sqrt(g)/2.                              (7)

Strictness holds because equality would require p-1/lambda=cF.
Multiplication by lambda+F would then give
F*(lambda*c+1/lambda+cF)=0, impossible for nonconstant F.

Suppose h>=0 and g>=4/25. Then g>=1/16 and
C1+2g+2h>2g-sqrt(g)/2>=0. By(6), writing x=sqrt(g),

    x^2 > 4x^4+4(2x^2-x/2)^2
          =x^2+4x^3*(5x-2).

At x>=2/5 this is impossible. Consequently

    g>=4/25 ==> H0<0 ==> odd P2.                 (8)

Thus the unresolved odd-sign/P2 branch is now confined to
0<g<4/25. This is a proved restricted sign theorem, not a lower
bound on g and not an unrestricted Chowla bound.

## 4. An explicit coupled P2 sufficient test using g,C1,C2,t

Define

    A0=4+40g+16C1,
    B0=g-4g^2-4(C1+2g)^2.

Expanding(6) gives

    20h^2+A0*h<=B0.                              (9)

By(7), A0>=4+40g-8sqrt(g)>=18/5>0. Hence B0<=0
already forbids h>0. If B0>0, put

    U(g,C1)=[sqrt(A0^2+80B0)-A0]/40.

Then h<=U, and odd P2 follows whenever

    C2^2 >= (2t/lambda)*U(g,C1).                  (10)

Failure of odd P2 must therefore satisfy ALL of

    0<g<4/25, B0>0,
    0<h<=U(g,C1), C2^2<(2t/lambda)*U(g,C1).

These are independently proved constraints, rather than the original
determinant rewritten. They can narrow a prospective falsifier or
certify an additional branch without evaluating T separately. They
do not force a contradiction when g tends to zero. In particular
one cannot simply replace the selected C2 pairing by its norm bound:
the direction of Cauchy is insufficient for the required lower bound.

## 5. Both parity planes: a high-triple gate retaining all inverse terms

The parent proposed adding the centered even plane. Put

    u=Re(p-1/lambda), v=Im p.

Both the even basis{f,u} and odd basis{b,v} have the same norm Gram

    Q=(1/2)*[[n,C1],[C1,g/lambda^2]].

The even energy entries independently check as

    Eeven_ff=3t/2,
    Eeven_fu=C2/2-lambda*C1-n/lambda,
    Eeven_uu=-g/lambda+T/2-2C1/lambda.              (11)

For example the extra cross term is
<F(p-1/lambda),F>=-lambda*C1-n/lambda. No odd/even
cross term survives, since F,p have real coefficients. Thus the
full four-vector space is the orthogonal direct sum of these
energy blocks. It is a broader sufficient family, not an identity
asserting that original odd P2 always holds.

Write

    tau3=t/lambda^3, c=C2/lambda,
    he=lambda*Eeven_uu=-2(g+C1)-h.

In normalized bases{b/lambda,lambda*v} and
{f/lambda,lambda*u}, with weight2f/lambda, the matrices are

    [[tau3/2,c/2],[c/2,h]],
    [[3tau3/2,c/2-C1-1/4],[c/2-C1-1/4,he]].       (12)

If BOTH are positive definite, h,he>0 and

    c^2<2tau3*h,
    (c-2C1-1/2)^2<6tau3*he.

Triangle and Cauchy imply the NEW necessary condition

    g+C1<0,
    (2C1+1/2)^2 < -16tau3*(g+C1).                (13)

Indeed |2C1+1/2| is at most the sum of the square roots on
the preceding two lines, which is at most
sqrt(8tau3*(h+he))=4sqrt(-tau3*(g+C1)). Therefore
the reverse weak inequality in(13) supplies a nonpositive energy
direction in at least one parity plane. C2 and H0 have been
eliminated, but no component was assigned a favorable sign.

The exact integral C1 identity gives -C1<=2g. If both planes
are positive definite and 0<g<=1/16, write v0=-C1. Then
g<v0<=2g<1/4. The function

    (1/2-2v0)^2/[16(v0-g)]

is decreasing on this interval. Equation(13) consequently forces

    t/lambda^3 > (1-8g)^2/(64g).                 (14)

This isolates a high-triple/weak-gap regime for simultaneous
failure. It does not eliminate that regime, and the relaxed
example in Section7 inhabits it. No universal Boolean estimate
on the right pairings or on t follows from(14).

## 6. A pointwise reverse-Cauchy premise is false even for actual Boolean A

The tempting ordering premise that negative f must have a smaller
|lambda+F| than positive f is FALSE inside the exact domain. Take

    A={1,6,7}, n=3, lambda=2sqrt(3).

These are the positive differences of{0,1,7}. The exact difference
square identity proves M<=3/2<sqrt(3) on the entire circle.

At x=2pi/5, z^6=z and z^7=z^2, hence F=2z+z^2 and

    f=(sqrt(5)-3)/4<0,
    |F|^2=4+sqrt(5),
    |lambda+F|^2=16+sqrt(5)
                          +(lambda/2)*(sqrt(5)-3)>16.9.

The last bound follows, for instance, from sqrt(5)>2.236,
sqrt(5)<2.237 and 3.464<lambda<3.465. At x=4pi/7 one has
z^6=conjugate(z), z^7=1, so F=1+2cos(4pi/7) is real and

    0<F<0.56,
    |lambda+F|^2<(3.465+0.56)^2<16.21.

For an elementary check, cos(4pi/7)=-sin(pi/14); using
3.14<pi<22/7 and y-y^3/6<=sin(y)<=y gives
0.55<F<0.56. Thus the denominator at the negative-f point is
strictly LARGER. The inequalities use paper rational bounds;
no numerical minimum or computation is a premise.

This refutes a plausible supportwise ordering needed by a simple
reverse-Cauchy proof. It does not refute P2 and does not justify
another successful-control search. The signed radial measure
view alone contains no missing Boolean bound.

## 7. Explicit norm-calibrated geometric obstruction to generic closure

The parent's proposed geometric countermodel has a complete paper
audit. For 0<r<1 and a>0 put

    F=a*z/(1-r*z), nE=||F||2^2=a^2/(1-r^2),
    lambda=2sqrt(nE), delta=a/lambda=sqrt(1-r^2)/2,
    s=r-delta.

This is initially an infinite analytic, NONBOOLEAN model. Its actual
weighted minimum is M=a/(1+r): its real part is an increasing
function of cos(x). Thus lambda>=2M and the same analytic margins
hold. Direct geometric summation gives

    p=1/lambda-a*z/[lambda^2*(1-s*z)],
    g=delta^2/(1-s^2), C1=-delta^2/(1-r*s),
    tau3=delta^3*r/(1-r^2)^2=r/(16delta),
    c=-delta^3*s/(1-r*s)^2,
    h=-g+delta^2/(1-r*s)
                        -delta^3*r/[2(1-r*s)^2].       (15)

The simplifications 1-s^2=delta(2r+3delta) and
1-r*s=delta(r+4delta) give, as delta tends to zero,

    g=delta/2-3delta^2/4+O(delta^3),
    C1=-delta+4delta^2+O(delta^3),
    h=3delta^2/4+O(delta^3), c=-delta+O(delta^2),
    he=delta+O(delta^2).

Consequently

    2tau3*h-c^2=3delta/32+O(delta^2)>0,
    6tau3*he-(c-2C1-1/2)^2=1/8+O(delta)>0.

Both matrices(12) are positive definite for sufficiently small
delta. The ACTUAL even matrix determinant divided by lambda^2
before the basis normalization is one quarter of the last line,
with limit1/32. This resolves the apparent factor4 convention.

Taking a=1 gives every coefficient in(0,1]. For any fixed rational
r sufficiently close to1, truncate to F_N=sum_(j=1)^N r^(j-1)z^j.
Then ||F-F_N||infinity<=r^N/(1-r), and exact norm calibration
lambda_N=2sqrt(sum_(j=0)^(N-1)r^(2j)) tends to lambda. The positive
inverse margin is uniform for large N, so inverse functions and
all energy entries converge uniformly. Both strict PD matrices,
the actual low-M inequality and the coefficient cap persist for
some finite N. Thus even finite positive coefficient caps plus
ACTUAL L2 calibration cannot prove the desired sign claim.

This is not a Boolean counterexample. It pinpoints the absent
unit-amplitude input in any attempt to close(6),(10),(13).

### Single finite certificate: source/artifact audited, not an advisor run

The parent chose r=99/101,a=1,N=1024, with infinite lambda=101/10.
Putting v=1/10, A1=1+4v-v^2, B1=(1+2v)(2-v), the simplified
formulas independently check as

    g=v/B1, C1=-v/A1,
    c=-v*(1-v-v^2)/A1^2,
    tau3=(1-v^2)/(16v),
    h=v^2*(1-3v)*(3+v)/(2A1^2*B1).

For a uniform tail E<=10^-6 and lambda error l<=10^-12, assume
lambda_N>=10, both real inverse margins>=9, first normalized
basis magnitudes<=6 and second magnitudes<=1. Then valid errors are

    e1=E/10+l/2,
    e2=l/9+(101/10)*(E+l)/81.

The l/2 uses the EXACT infinite ||F/lambda||infinity=5, not just
the loose magnitude6. The normalized weight changes by at most2e1.
For either normalized energy block, entry errors are

    err11=216e1,
    err12=24e1+72e2,
    err22=2e1+24e2.

These follow by bounding the weight by12, the first basis function
by6 and the second by1, at both endpoints. To certify finite PD
from infinite entries A,B,D, it is enough to verify

    A-err11>0, D-err22>0,
    (A-err11)*(D-err22)-(|B|+err12)^2>0.

This advisor checked the formulas, domains and propagation constants
on paper, then read the full producer
[P2_geometric_certificate.py](../../src/P2_geometric_certificate.py)
and the saved [results.json](../experiments/P2_geometric_2026-10-23/results.json).
The parent ran it on Dirichlet with exact Python Fraction arithmetic;
the artifact reports terminal PASS. I did not rerun it.

The source checks the exact rational geometric tail inequalities,
lambda_N>10, the all-circle margin and positive diagonal/determinant
lower bounds. Its direct closed forms independently agree with the
v-parametrization. The final finite polynomial is explicitly

    F_1024=sum_(j=1)^1024 (99/101)^(j-1)*z^j,
    nE=(10201/400)*(1-(99/101)^2048),
    lambda_N=(101/10)*sqrt(1-(99/101)^2048).

It has an ALL-CIRCLE weighted M upper bound505001/1000000,
and both complete reciprocal parity planes are strictly positive
definite. Coarsely rounded DOWN, the normalized determinant lower
bounds exceed0.00022995 for the odd plane and0.00939703 for the
even plane. Exact rational bounds, including both positive diagonal
bounds, are preserved in the linked artifact.

These are FULL inverse planes, not truncated carrier vectors or
sampled energies: the certified uniform transfer encloses all inverse
coefficients at once. The finite second-basis bound1 follows from
lambda_N>=2M_N, which the displayed strict margins imply. The e1
coefficient1/2 follows from the exact infinite magnitude5 noted
above. No interval minimum, floating-point solver or unverified
numerical quadrature is used in this certificate.

This is an exact finite RELAXATION falsifier with all coefficients
in(0,1], actual L2 calibration and a rigorous all-circle low-M
premise. It is not Boolean and refutes neither odd P2 nor Chowla.
The exact finite computation has an independent paper/source audit;
it has not acquired Lean/kernel verification or a separate arithmetic
backend by being read here.

## 8. Exact gap, pivot criterion and strategic decision

The new phase-SOS/projection argument shrinks the open odd sign
branch to0<g<4/25 and gives an explicit coupled upper bound U(g,C1).
Both parity planes add the high-triple gate(13)--(14). These are
actual new inequalities, not just the previous P2 identity again.
They use generic analyticity and coefficient energy, so they do
not fill the remaining Boolean gap. The geometric countermodel
shows why further generic positivity/Gram manipulation is insufficient.

For a claimed odd-P2 counterexample, the concrete discriminator is
ACTUAL M<=sqrt(n), 0<g<4/25, B0>0 and an exact positive determinant
2tH0-C2^2, with full inverse residual certification. Failure to
improve a score or additional examples with H0<0 is not evidence
for a universal theorem. If the broadened parity family is used,
its simultaneous PD candidate must also meet(13), and(14) when
g<=1/16. No new control sweep follows from these bounds.

A next proof attempt must exploit exact indicator coefficients
to force a quantitative relation between the selected nonlinear
pairing C2 and the phase-defect norm ||K||2, or falsify it in this
remaining narrow domain. The old recurrence residual R_A has both
signs and is not discarded. Equation(3) is an existing sufficient
target, not a new completeness theorem. If an actual Boolean PD
plane is certified, retire that plane as a universal bottleneck
and use unrestricted signed Rayleigh; do not infer failure of
Chowla from failure of this witness family. The independent
all-circle construction track also remains active.

Status: paper intermediate theorems and a decisive generic
countermodel; no odd-P2 proof, Boolean sign falsifier, improved
universal exponent, full Chowla resolution or counterfamily.

## 9. A finite-coefficient closure and the exact unprojected remainder

The parent proposed one sharper Boolean falsification test. Define

    y=-lambda*T>0,
    G3=[y^2+4(C1+y)^2+2y]/5.

Since h=y/2-g, the phase norm in(1) is5g-2y. Its projection
on the orthogonal span{1,conjugate(F)} has norm squared
y^2+4(C1+y)^2. Thus

    g>=G3,
    H0<=-G3/lambda-T/2.                          (16)

All quantities G3,C1,T,C2,t use finitely many formal inverse
coefficients at the exact fixed lambda. Consequently

    Psi3=2t*(-G3/lambda-T/2)-C2^2<=0             (17)

is a genuinely STRONGER sufficient criterion for odd P2. It
is not equivalent to P2, and no universal sign for Psi3 has
been derived. A single actual-lowM Boolean example with Psi3>0
would rigorously refute this particular finite-projection closure,
without refuting P2 or every possible richer finite projection.

The exact omitted energy can be named without discarding it:

    Rperp=||K-proj_(span{1,conjugate(F)})K||2^2
          =5*(g-G3)>=0.

It enters the original determinant with an explicit coefficient,

    2tH0-C2^2=Psi3-(2t/(5lambda))*Rperp.          (18)

If(17) is falsified, the remaining joint requirement is an
actual Boolean lower bound on THIS unprojected scalar phase
energy compared with the positive finite deficit, or a move to
unrestricted signed Rayleigh. Nonnegativity of Rperp alone does
not suffice when Psi3>0. Formula(18) is an exact gap statement,
not a new proof of the required lower bound.

The parent predeclared a single384-bit finite-recurrence test on
the already chosen separated-block L36 input (n76). Its actual
low-M premise is supplied by the exact union-of-difference-SOS
bound M<=17/2<sqrt(76). This advisor launched no job. Any old
grid sign for H0 is only a numerical observation; it is not
silently promoted to an exact odd-P2 success certificate here.

### The finite-projection closure is rigorously FALSE on a Boolean input

I subsequently read the full
[P2_projection_bound.py](../../src/P2_projection_bound.py), its
[saved result](../experiments/P2_projection_2026-10-23/results.json),
and the underlying
[alias producer](../../src/P2_alias_adversary.py) and fixed-family data.
The exact set is the disjoint union of the66 positive differences of
the saved12-point Singer set and36 times the10 positive differences
of{0,1,4,9,11}. It has n=76,D=396,t=1617. The producers check
distinctness of the integer differences and disjointness of the
two blocks. Each difference-square identity contributes at most
half the number of its underlying points, giving the rigorous
all-circle bound M<=6+5/2=17/2<sqrt(76).

At lambda=2sqrt(76), the parent ran384-bit Arb recurrences for
p through degree2D and for p^2 through the same degree. The
second recurrence uses(lambda+F)*p^2=p. Its selected T value
also agrees, in rigorous balls, with the independent convolution
sum of the p coefficients; the displayed difference ball has
radius2.94e-111. C2 is formed from exact ordered pair counts,
and t is an exact integer count.

The resulting OUTWARD rational enclosure has

    Psi3 >=18429338424493848575/18446744073709551616>0,

approximately0.9990564. The bracket helper uses floating numbers
only to propose coarse endpoints, then verifies strict outward
containment with Arb comparisons; those comparisons, not floating
rounding assumptions, justify the saved interval. The artifact
reports terminal PASS and explicitly labels the stronger criterion
refuted. I audited its formula and enclosure construction without
rerunning the job.

This is an actual Boolean falsifier of the UNIVERSAL SIGN claim
Psi3<=0. It refutes the constant-plus-conjugate(F) projection
closure, not P2. This initial finite-recurrence portion did not
compute g or the true determinant; the subsequent full comparison
below does. Equation(18) shows exactly where the unprojected scalar
phase energy is still required. No larger finite-projection search
is justified by this failure.

### Same-support full inverse comparison now certified

The parent subsequently added ONE full inverse certificate on this
SAME support, and I read the updated producer and the artifact's
full_norm_comparison. The approximation has degree12672. Its exact
polynomial residual includes every exterior coefficient through
degree12672+396; the rigorous inverse margin is supplied by the
same all-circle bound M<=17/2. The residual encloses the ENTIRE
inverse, not only its finite band. I also re-read the invoked
cstar_zero_reciprocal.one implementation and its norm/energy error
propagation. Its exact finite sine energy agrees with a separate
signed-correlation formula. No second arithmetic backend or new
formalization is implied by that independent identity check.

The updated certificate proves H0<0 and

    2tH0-C2^2
       <=-61023999017144500223/18446744073709551616<0,

approximately-3.3081176154. In contrast the stronger Psi3 is
strictly positive near0.9990564. The missing orthogonal phase
energy is rigorously positive, with

    Rperp in
      [2141800053402265087/18446744073709551616,
       2141800053402365185/18446744073709551616],

approximately0.116. Thus the omitted part really repairs the
failed finite closure on this exact Boolean input. Original S0
and P2 both HOLD on the example; their finite-projection shortcut
FAILS. The earlier grid sign has now been replaced by this full
inverse residual certificate for this one support only.

No support enlargement, new sweep, GPU or VM lifecycle action is
authorized or warranted by the comparison.

## 10. Full negative Fourier block: a derived candidate with a known generic limit

The parent proposed retaining every negative coefficient of K
instead of its rank-one projection on conjugate(F). This is a
valid exact algebraic refinement. For j=1,...,D,

    K_(-j)=lambda*sum_(a in A,a>=j) [z^(a-j)]p^2.

The F^2*p^2 term is analytic, so these are ALL negative Fourier
coefficients. They are finite functions of formal inverse-square
coefficients, with no frequency sampling or tail assumption.
Together with K0=-y, Parseval gives

    Gminus=[y^2+sum_(j=1)^D K_(-j)^2+2y]/5<=g,
    Gminus>=G3,
    5*(g-Gminus)=||P_(strictly positive frequencies)K||2^2.

The last equality is exact. Substitution of Gminus for g gives
another STRONGER sufficient finite-coefficient P2 criterion, not
an established universal inequality. Its discarded term is now
the entire positive-frequency scalar phase tail. The only checked
finite case is recorded below; this advisor ran no computation.

It must be compared with the recorded Hankel barrier precisely:
K_- is the selected-coefficient Hankel action on the SPECIAL
input p^2. A false uniform Hankel operator-norm estimate cannot
be imported, but failure of that operator shortcut does not settle
the special-input question. The exact Boolean indicator rows are
retained in this formula; a new estimate must use their interaction
with this inverse, rather than merely the number of rows.

There is a decisive generic limitation already visible without a
new experiment. For the infinite geometric model in Section7,

    K_(-j)=lambda*a*r^(j-1)*p(r)^2, j>=1.

Thus the WHOLE negative block is proportional to conjugate(F);
its rank-one projection is exact and Gminus=G3. Including all
negative coefficients does not repair the generic countermodel.
Any prospective gain must be Boolean and specific to the coupled
inverse input. This is a derived next candidate, not a new route,
a theorem about its missing sign, or authorization for a sweep.

### One same-support finite recovery, now source/artifact audited

The parent extended the SAME L36 producer/artifact once more to
compute all D negative coefficients from the existing384-bit
inverse-square recurrence. I read the complete updated source
and the relevant saved intervals. The summation includes j=D,
uses the exact formula above, and encloses every real squared
coefficient with Arb arithmetic. The accompanying full inverse
certificate is now also cross-checked by sparse Python-integer
shifts, independently of the producer's FLINT polynomial product.
This checks its residual norm bound and hence its full-norm
enclosure; it remains an exact computation, not Lean verification.

The full-negative sufficient criterion is rigorously negative:

    Psi_minus=2t*(-Gminus/lambda-T/2)-C2^2
       <=-13650084382353821695/18446744073709551616<0,

approximately-0.7399725571. The saved quantities are approximately
G3=0.1099250294, Gminus=0.1193007272 and g=0.1331464721.
Thus the individual Boolean positions recover a valid finite
certificate where the rank-one negative projection failed.

In fact these finite data already suffice for S0 on this input:

    2*Gminus_lower > y_upper,

because their common-denominator numerators satisfy
4401419964686003198>4255597977635272705. Hence
H0<=(-Gminus+y/2)/lambda<0, even before using C2 or the
separate full-inverse comparison. This is ONE finite recovery;
it is not evidence sufficient for a universal claim.

Writing Nminus=sum_(j=1)^D K_(-j)^2, the exact remaining
finite candidate for t>0 is

    Nminus+(5lambda/(2t))*C2^2 >= y/2-y^2.        (19)

This is equivalent to Psi_minus<=0 and is stronger than P2.
It is a specific inverse-input Hankel quadratic-form inequality
with every Boolean row retained. It is not implied by generic
norms or coefficient caps, and no universal proof or Boolean
falsifier of(19) is claimed. No additional support search follows.

## 11. A genuinely Boolean two-row boundary gap, with its factor size

The parent identified a useful exact distinction from weighted
models. I independently checked the full coefficient argument.
Let n>=2, m=min(A)<D=max(A), and initially allow any lambda>M.
The inverse-square formal series satisfies

    [z^0]p^2=1/lambda^2,
    [z^j]p^2=0 for0<j<m,
    [z^m]p^2=-2/lambda^3.

The extreme two negative coefficients of K are therefore

    K_(-D)=1/lambda,
    K_(-(D-m))=1_A(D-m)/lambda-2/lambda^2.       (20)

Intervening occupied frequencies contribute zero by the middle
line of the preceding display, so(20) requires no extra gap
assumption on A. It uses the unit amplitudes at BOTH m and D.

For any projection coefficient c, the squared distance of the
negative block from c*conjugate(F) has the following lower bound.
If D-m is absent, that off-support coordinate contributes
4/lambda^4. If D-m is present, the two selected coordinates
D and D-m differ by2/lambda^2. Their squared errors about
the same c sum to at least half this squared difference,
namely2/lambda^4. Positive frequencies only add energy. Thus

    Rperp>=2/lambda^4.

At the fixed calibration lambda^2=4n, equation(18) gives

    g-G3>=2/(5lambda^4)=1/(40n^2).               (21)

This is an actual quantitative zero/one coefficient consequence,
not merely generic strictness of a Gram inequality. It is tiny:
no macroscopic n-scale gain or Chowla bound follows. Weighted
endpoint amplitudes enter multiplicatively in(20), so its fixed
constant cannot be imported into the coefficient-cap relaxation.

The precise next proof attempt is to aggregate Boolean row identities
of this kind toward(19), while retaining their correlations with
the special inverse-square input. An operator-norm replacement,
independent-sign assumption or repeated successful finite controls
would lose the needed information. The old uniform Hankel shortcut
and the geometric model must remain explicit adversaries. Neither
original P2 nor the stronger candidate(19) is a required completeness
assumption for the unrestricted signed-Rayleigh/full Chowla goal.

Final status for this follow-up: one finite recovery, an exact tiny
Boolean boundary gap, and a precise stronger candidate. No universal
sign theorem, new exponent, new resource action or additional agent.
