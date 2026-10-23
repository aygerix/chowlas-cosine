# Optimal nonnegative endpoint: paper attack and a precise finite branch

2026-10-23. Sole internal AI advisor, paper work and read-only inspection
of existing records. Only this assigned note is edited in this task.
No research computation, VM operation, GPU, extra agent or outreach.
Shared Dirichlet is left on. Section5 records the completed exact
finite certificate and the independent paper/source audit. Earlier
numerical leads are preserved with their original status.

## 1. Exact question and quantifiers

For Boolean A, n=|A|, suppose

    M(A)+f_A=|Q|^2, Q=sum_(b in B)q_b*z^b, q_b>0 real.

Does EVERY such optimal nonnegative factor have qmax<=C for an
absolute C? The proposed first target C=1 is stronger. One factor
with qmax>1 refutes C=1 in this universal form. It does NOT refute
every larger C, and it does not show that another optimal branch
for the same A lacks a smaller endpoint. An existential bounded-
factor theorem is a separate, weaker assertion. General signed
or complex factors are outside the nonnegative endpoint question.

Throughout this note lambda=M(A) when optimality is asserted.
For other valid certificates lambda>=M(A), the distinction is explicit.

## 2. Exact restrictions and two attempted improvements

Translate/reflect the support to put qmax=a at exponent0 and the
other endpoint at L. From exact nonzero autocorrelations1/2,

    q_0*q_L=1/2, q_L=1/(2a),
    every other q_b<=1/(2a),
    S=sum q_b=sqrt(lambda+n).

At optimality Q has a unit-circle zero zeta. The triangle inequality
gives sum_(b>0)q_b>=a, and therefore

    a^2<=(k-1)/2, k=|B|.                         (1)

This is not uniform in k. It is the old endpoint restriction combined
with a zero; no support-size bound follows in this way.

First attempted strengthening: differentiate the off-zero correlation
constraints while minimizing sum q_b^2, or use their Lagrange equations.
At a unit zero zeta=e^(i*theta), the relevant stationarity identity is

    q_b+sum_(d>0)cos(d*theta)*(q_(b-d)+q_(b+d))
       =Re(e^(-i*b*theta)*Q(zeta))=0.              (2)

Every nonzero term has d in A. Thus the apparent optimality equation
is already the unit-zero equation in each phase; it supplies no new
coefficient control. At the largest endpoint, inserting q_b<=1/(2a)
into its real part recovers only (1). Treating (2) as an additional
inverse estimate would double-count the same information.

Second attempted strengthening: use the energy and total coefficient
mass to force balanced endpoints. Positivity actually gives

    lambda=sum q_b^2<=a*S,
    a>=lambda/sqrt(lambda+n).                     (3)

This is a LOWER bound on the largest endpoint. It says that if an
optimal positive factor exists with lambda much larger than sqrt(n),
its endpoint necessarily grows. More precisely the endpoint bounds give

    lambda<=a^2+(S-a)/(2a)=a^2-1/2+S/(2a).

Consequently a dense interval sequence with lambda proportional to n
would be an unbounded-endpoint counterfamily IF optimal nonnegative
factors existed along that sequence. Their coefficient positivity
has not been proved and is not assumed. Neither Jensen's formula
for an outer factor nor its large constant coefficient settles that
sign condition. No interval sweep was run.

These two attempts leave the actual uniform-C problem unresolved;
they identify a precise missing condition rather than prove it.

## 3. Existing finite data identify A={1,2,3,4,5}

Read-only inspection of the OLD artifact
experiments/cstar_structural_2026-10-20/positive_factor_search.json
found the full support[0,5] entry with nonzero correlations1,
energy K=3.45753648302061 and coefficient vector approximately

    (1.4762149761,.0184430780,.2927082370,
       .5347321868,.6689449202,.6774081121).

Divide this vector by sqrt(2) to obtain the current1/2-correlation
normalization. Its first coefficient is approximately1.04384>1,
with energy approximately1.72876824<2. Its OLD status is numerical
feasibility, not exact feasibility or proven optimality. It is a
specific branch lead, not already a certified counterexample.

The unit-zero condition can be imposed without separately solving
the global minimum of f_5. Write

    Q(z)=(z^2-2c*z+1)*(a+b*z+d*z^2+e*z^3).

Its six coefficients are exactly

    q0=a,
    q1=b-2c*a,
    q2=d-2c*b+a,
    q3=e-2c*d+b,
    q4=d-2c*e,
    q5=e.

In the five real variables(a,b,d,e,c), impose the FIVE polynomial
equations

    sum_(j=0)^(5-l) qj*q_(j+l)=1/2, l=1,...,5.   (4)

A validated real solution of (4) with |c|<1, all qj>0, q0>1 and
sum qj^2<2 would be a complete finite falsifier to C=1, even under
actual lowM. Indeed (4) gives the EXACT identity

    |Q(e^(ix))|^2=lambda+sum_(l=1)^5 cos(l*x)

for every real x. The quadratic factor has a unit-circle zero,
so lambda=M({1,...,5}) exactly. Its energy below2 implies
M<2<sqrt(5). This route avoids any assumption that a numerically
selected outer factor retains positive coefficients.

For a paper seed only, f_5(t)=16t^5+8t^4-16t^3-6t^2+3t at
t=cos(x), and a minimizing stationary c satisfies
80c^4+32c^3-48c^2-12c+3=0 near.683. This approximate location is
not used as a proof. The root elected to validate ONLY system(4)
on Dirichlet with a rational interval-Newton/Krawczyk certificate,
not a family search. The advisor did not run that computation.

## 4. Strategic decision and remaining gap

The exact branch certificate in Section5 now refutes C=1. Its
classification of all real spectral branches also refutes the
existence of an optimal nonnegative branch with qmax<=1 for this
particular A. Retire both constant1 versions. Preserve the finite
support, implicit exact factor, unit-zero identity and coefficient
inequalities. Do not upgrade it to an unbounded endpoint family.

The endpoint conjecture concerns a restricted factor representation;
even a uniform bound here would still require a representation
bridge to arbitrary hypothetical small-ratio Boolean supports.
The weighted centroid lemma itself is valid, but the exact bound
(lambda-1/2)>=S/(4qmax) does not upper-bound qmax. Do not rename
this missing estimate as progress.

The structurally changed continuation is the signed-centroid identity
and its missing-lag cancellation term, with quantitative signed mass
and variance rather than an assumed nonnegative factor. Its general
inverse estimates are not established either; their exact hypotheses
must be audited independently. No extra endpoint sweep or resource
expansion is justified by the old artifact.

## 5. Completed exact n5 result and all-branch audit

The root's producer and separately differentiated verifier both
completed on Dirichlet with PASS. I read, but did NOT rerun,

    experiments/optimal_endpoint_2026-10-23/n5.json,
    experiments/optimal_endpoint_2026-10-23/n5_verification.json,
    src/optimal_endpoint_n5.py,
    src/optimal_endpoint_n5_verify.py,
    src/rational_box.py.

The producer uses floating algebra only for the proposed rational
center and inverse Jacobian. Exact rational interval operations
prove that x -> x-R*F(x) maps a closed five-dimensional rational
box strictly into itself, with derivative infinity norm<1. The
rational matrix R is nonsingular. Banach's theorem gives a genuine
real zero of (4) in the box. The verifier independently rebuilds
Q by convolution, differentiates with dual intervals, and checks
strict inclusion, contraction and rank again. Both share the
small exact-Fraction interval primitive, whose arithmetic I also
inspected; this is independent reconstruction/differentiation,
not an independent arithmetic backend or a Lean proof.

The box proves all six Q coefficients strictly positive, q0>1,
q0 larger than every other coefficient, |c|<1 and lambda=sum qj^2<2.
The saved display values are

    qmax approximately1.0437967021412156,
    M({1,...,5}) approximately1.7287682073931698.

The rigorous statements use the saved rational intervals, not
these displayed decimals. The global identity and unit-circle
quadratic in Section3 prove lambda=M exactly, for ALL real x.
In particular this falsifier satisfies actual M<2<sqrt(5).

It remains to justify the stronger ALL-BRANCH statement, rather
than silently replace it by one counterbranch. Let R(z)=a+bz+dz^2+ez^3
be the residual cubic in the certified Q+. The exact interval gates prove

    discriminant(R)<0,
    R(-t)=0 for one t>1,
    a/(e*t)>1.

The first condition gives one real root and one nonreal conjugate
pair, with no multiplicities. The last quantity is precisely the
squared modulus of that pair, by the product of the three roots.
Thus ALL three roots of R lie outside the unit disk. The bracket
for t is certified by opposite signs of R(-t) at its rational
endpoints, not by an unvalidated floating root.

After a monomial shift, EVERY real factor of the same Laurent
polynomial has degree5: its unique extreme product is the nonzero
frequency5 coefficient. Let U=z^2-2cz+1. In

    z^5*(lambda+f_5)=Q+(z)*Q+^*(z)

the two nonreal unit roots of U have multiplicity2. A real factor
must contain each once, since conjugate roots have equal multiplicity
and reversal contributes the same unit-root multiplicity. The other
root choices are independently (i) the real pair -t,-1/t, and
(ii) the outside conjugate pair versus its inside reciprocal pair.
Reality forces the conjugate pair to be selected together. There
are exactly FOUR real spectral branches up to sign and monomial
shift. Their modulus-normalization fixes the remaining scalar up
to sign.

The real-root-only reflection is explicit:

    Rr(z)=(t*z+1)*(e*z^2+(d-e*t)*z+a/t),
    Qr=U*Rr.

It preserves circle modulus because |z+t|=|t*z+1| there. Its
coefficient at z^2 is

    e+t*d-e*t^2-2c*(d-e*t+a)+a/t,

which the exact box certifies strictly NEGATIVE. The constant and
leading coefficients of Qr are a/t>0 and e*t>0; hence multiplying
by -1 cannot rescue nonnegativity. The complex-pair-only reflection
is the reversal of Qr, so it too has a negative coefficient and
positive endpoints. Reflecting all nonunit roots gives the reversal
of Q+, since U is palindromic. Therefore the ONLY nonnegative
real branches are Q+ and its reversal, modulo monomial translation.
Both have the same certified qmax>1.

Conclusion: A={1,...,5} is a genuine exact finite counterexample
to qmax<=1, even after choosing any optimal nonnegative real
factor. It is NOT a counterexample to every absolute C, not a
new construction with vanishing M/sqrt(n), and not a general
lower-bound proof. External novelty has not been checked. The
stable signed-centroid lemma is audited separately; no larger
endpoint sweep follows from this one result.
