# Independent audit: signed centroid and missing-lag cancellation

2026-10-23. Sole internal AI advisor. Paper proof only; no research
computation, VM operation, GPU, extra agent or outreach. Shared Dirichlet
is left on. This note records the root's signed extension independently
checked below, not a general inverse theorem or new universal exponent.

## 1. Exact hypotheses and quantities

Let A be a nonempty finite set of distinct positive integers, n=|A|.
Suppose a finite REAL-coefficient Laurent polynomial Q satisfies

    lambda+f_A=|Q|^2, Q=sum_(b in B)q_b*z^b,

with zero coefficients trimmed, but signs otherwise arbitrary.
Then lambda=sum q_b^2 and R(d)=sum_b q_b*q_(b+d) equals1/2 on
plus/minus A and0 at all other nonzero lags. Evaluation at1 gives
(sum q_b)^2=lambda+n. Orient Q by an overall sign so

    S=sum q_b=sqrt(lambda+n)>0,
    Nminus=sum_b max(-q_b,0),
    P=sum_b max(q_b,0)=S+Nminus.

Define the SIGNED centroid and its absolute second moments by

    mu=(sum b*q_b)/S,
    y_b=b-mu, x_b=y_b*q_b, sum_b x_b=0,
    Vplus=sum_(q_b>0)q_b*y_b^2,
    Vminus=sum_(q_b<0)|q_b|*y_b^2,
    Vabs=Vplus+Vminus>0, alpha=Vminus/Vabs,
    qmax=max_b |q_b|.

The signed centroid need not be inside the convex hull of B; no step
assumes it is. The following bound is valid:

    S*(1-4alpha)
       <=4*(lambda-1/2)*qmax+2*Nminus.             (1)

All quantities concern the chosen factor, which may depend on the
choice of spectral branch. Optimality is not required for (1).

## 2. Exact Gram identity and the lower estimate

Set U_d=sum_b q_b*q_(b+d)*y_b, for all integer d. Expanding gives
sum_d U_d^2=x^T G x with G_bc=R(b-c). The matrix is

    G=(lambda-1/2)*I+(1/2)*J-(1/2)*Mmissing,

where Mmissing_bc=1 precisely when b!=c and |b-c| is not in A.
Writing the missing term as the ORDERED sum

    Tmissing=sum_(b!=c,|b-c| notin A)x_b*x_c,

and using sum x_b=0 proves exactly

    sum_d U_d^2
      =(lambda-1/2)*sum_b q_b^2*y_b^2
          -(1/2)*Tmissing.                        (2)

The diagonal U_0 need not vanish; it is included in (2).
For d>0, U_-d=U_d+d*R(d). Pairing the squares and discarding
U_0^2>=0 gives

    sum_d U_d^2
      >=(1/2)*sum_(d>0)R(d)^2*d^2
      =(1/4)*sum_(d>0)R(d)*d^2
      =S*(Vplus-Vminus)/4.                        (3)

The middle equality uses EXACT Boolean off-zero correlations0,1/2.
The final identity is the signed weighted pair-variance identity:

    sum_(b<c)q_b*q_c*(b-c)^2
      =S*sum_b q_b*(b-mu)^2.

It also supplies an automatic but insufficient restriction:

    S*(Vplus-Vminus)=(1/2)*sum_(a in A)a^2>0,
    0<=alpha<1/2.                                 (4)

This is not a uniform margin alpha<=1/8. Positivity alone for a
weighted Fourier spectrum would not justify replacing R(d)^2
by R(d)/2 in (3).

## 3. Missing-lag cancellation: ordered factors check

For a positive missing lag d, put a_b=q_b*q_(b+d). Because R(d)=0,
sum_b a_b=0. Therefore

    sum_b a_b*y_b*y_(b+d)
      =sum_b a_b*(b+d/2-mu)^2.                    (5)

The discarded constant is -d^2*sum a_b/4=0. Grouping both orientations
of each lag in the ORDERED Tmissing gives a factor2 on the right of
(5). Its negative terms can only come from opposite coefficient signs.
For such an unordered pair b,c,

    2*((y_b+y_c)/2)^2<=y_b^2+y_c^2.

Consequently

    Tmissing
      >=-sum_(opposite-sign UNORDERED missing pairs)
              |q_b*q_c|*(y_b^2+y_c^2)
      >=-sum_(ALL opposite-sign unordered pairs)
              |q_b*q_c|*(y_b^2+y_c^2)
      =-(Nminus*Vplus+P*Vminus).                   (6)

There is NO extra factor2 in (6): the ordered-pair factor was already
used in the midpoint inequality. The last equality counts each positive-
negative pair once, yielding the negative mass times the positive
variance and the positive mass times the negative variance.

For any a in A, finite-support Cauchy-Schwarz gives |R(a)|<lambda:
equality would require a nonzero finite sequence proportional to its
nonzero translate. Hence lambda>1/2. We may therefore use
sum q_b^2*y_b^2<=qmax*Vabs in the upper bound from (2),(6).
Combining with (3) and dividing by Vabs>0 gives

    S*(1-2alpha)/4
      <=(lambda-1/2)*qmax+(Nminus+S*alpha)/2.

This rearranges to precisely (1). The proof checks for nonoptimal
factors too; unit-circle zeros are not being used silently.

## 4. Quantitative stable branch and sharp base constant

If

    alpha<=1/8, Nminus<=S/8, qmax<=C,

then (1) yields

    S/2<=4C*(lambda-1/2)+S/4,
    S<=16C*(lambda-1/2),
    lambda>=sqrt(n)/(16C).                        (7)

The last step uses S^2=lambda+n. At lambda=M(A), (7) is an actual
square-root lower bound under the THREE stated factor conditions.
At a larger lambda it is only a certificate-energy floor. The
thresholds1/8 and the factor16 are convenient sufficient constants,
not claimed optimal.

The base coefficient4 in (1) is already sharp in the nonnegative
case. Take A={1,2}, Q=(1+z/2+z^2)/sqrt(2). Then

    lambda=9/8, qmax=1/sqrt(2),
    S=5/[2sqrt(2)], Nminus=alpha=0,
    S=4*(lambda-1/2)*qmax.

The central coefficient lies at mu=1, so it contributes no variance;
all weighted inequalities in that nonnegative centroid bound are
equalities. Improving4 universally requires some additional hypothesis.

## 5. Meaning, limitations, and exact next distinction

The lemma retains signs rather than requiring a single nonnegative
factor. Its nontrivial step is the use of zero missing correlations
to control the signed midpoint sum (5)--(6). It is invariant under
integer dilation or translation of factor support: the variances
scale together, while alpha,Nminus,S,qmax do not change.

It is not merely a new name for nonnegativity, but it also does not
establish any of the three stable-branch hypotheses for an arbitrary
optimal factor. In a hypothetical small-ratio sequence with bounded
qmax, (1) forces

    4alpha+2*Nminus/S >=1-o(1).

That is a necessary phase-cancellation alternative, not a contradiction.
General factors may have a macroscopic negative coefficient mass,
negative variance concentrated far from the signed centroid, or
growing endpoint amplitude. The one-variable factor theorem supplies
no quantitative control of those alternatives in this audit.

For a growing/vanishing-ratio proof, one must select an OPTIMAL real
factor and derive an independent restriction on at least those
bad alternatives. The estimate itself is valid but conditional;
assuming small alpha and small Nminus because cancellation is
unwanted would be circular. A finite failure of qmax<=1 for one
positive branch would not refute every bounded-C or signed-stability
version.

Status through this section: independently checked paper identities
and inequalities, including all signed/ordered factors. The later
Section7 records one exact finite interval result. No Lean/kernel-
checked proof, external novelty claim, universal exponent gain or
unrestricted representation estimate is asserted. No resource
action follows from this note.

## 6. One root reflection: exact coefficient and variance budget

This subsection audits a SINGLE reflection, not a proposed universal
descent theorem. Start with a real factor and a negative real root
-t, t>1, and write

    Q(z)=(z+t)*C(z), C(z)=sum_j c_j*z^j,
    Qr(z)=(1+t*z)*C(z).

Extend c_j by0 outside its finite range. On the unit circle
|z+t|=|1+t*z|, so Qr has exactly the SAME lambda and Boolean
cosine spectrum. Also Qr(1)=Q(1)=S>0, with no new orientation
choice. Its coefficient update is exactly

    q_j=t*c_j+c_(j-1),
    q'_j=c_j+t*c_(j-1),
    Delta q_j=(t-1)*(c_(j-1)-c_j).                 (8)

Thus all coefficient changes can be checked from the existing
factor division; no new factor search or root solver is needed.
The signed centroid is Q'(1)/Q(1), where the prime here denotes
polynomial differentiation. Logarithmic differentiation gives

    mu_r=mu+delta, delta=(t-1)/(t+1).              (9)

For ANY real spectral branch of the same lambda+f_A, the exact
INTRINSIC signed variance is fixed:

    Vint=Vplus-Vminus=sum_(a in A)a^2/(2S)>0.      (10)

This follows already from (3)--(4); it also follows because
the second logarithmic derivative z*d/dz of the reflection
quotient (1+t*z)/(z+t) vanishes at z=1. Consequently

    alpha=Vminus/(Vint+2*Vminus),
    alpha<=1/8 iff Vminus<=Vint/6.                 (11)

The negative-variance budget has a branch-independent right side,
even though each branch has its OWN signed centroid. Translation
of factor support leaves centered variances unchanged; integer
dilation scales both sides of the budget by the same square.

For exact one-step accounting, let

    n_j=(-q_j)_+, n'_j=(-q'_j)_+,
    Bminus=sum_j n_j*(j-mu), Nminus=sum_j n_j.

Since S is fixed, the mass change is

    Nminus_r-Nminus=(||q'||_1-||q||_1)/2.          (12)

Expanding the NEW centered squares gives the exact variance change

    Vminus_r-Vminus
      =-2delta*Bminus+delta^2*Nminus
         +sum_j(n'_j-n_j)*(j-mu-delta)^2.          (13)

Equivalently, one may simply evaluate
Vminus_r=sum_j n'_j*(j-mu-delta)^2. There is no implicit
assumption that negative coefficients or their first moments
remain unchanged. For a nonnegative starting factor, (13)
reduces to the particularly transparent formula

    Vminus_r=sum_(q'_j<0)|q'_j|*(j-mu_r)^2.        (14)

Thus a small newly negative coefficient near the NEW centroid
can have a much smaller variance cost than a coefficient of the
same magnitude far from it. Small negative mass alone does not
guarantee the variance budget.

There is an exact endpoint trade as well. If the starting factor
is nonnegative with q0=a=qmax and last coefficient1/(2a),
the reflected endpoints are

    q0_r=a/t, qD_r=t/(2a).

Both are strictly below the old maximum a iff1<t<2a^2. Their
ideal balance is t=sqrt(2)*a, but t must be an EXISTING root;
it is not a free parameter. Signed interior coefficients may
become the maximum and must be checked separately.

There is a concrete obstruction to using endpoint balance as
a greedy global-amplitude principle. The exact analytic filter is

    L_t(z)=(1+t*z)/(t+z),
    l0=1/t, lj=(1-t^(-2))*(-1/t)^(j-1), j>=1.

For an initially nonnegative Q, convolution gives

    q1_r=q1/t+(1-t^(-2))*a >=(1-t^(-2))*a.

For large t, the large endpoint therefore moves almost intact
into the first interior coefficient. Even the formally balanced
choice t=sqrt(2)*a has this defect when a grows. The filter's
negative coefficient mass sums to1/t, giving Nminus_r<=S/t,
but small introduced negative mass does NOT imply a useful
decrease in the GLOBAL coefficient maximum. The infinite filter
expansion is absolutely summable for t>1; because Q has the
factor z+t its product is the finite polynomial Qr exactly.

A one-step admissible improvement can therefore be stated exactly:
evaluate (8)--(13), require qmax_r<qmax, Nminus_r<=S/8 and
Vminus_r<=Vint/6. If qmax_r<=C too, the already-proved stable
branch applies. No proof here guarantees that an admissible root
exists, that iteration cannot get stuck, or that successive
reflections keep either budget. Claiming such a selection theorem
from one example would be an unsupported universal step.

## 7. Interpretation of the SAME n5 signed branch

The real-root-reflected factor of the exact n5 certificate is
one of the already-classified spectral branches, not a changed A
or a changed minimum. The root evaluated its qmax, Nminus/S and
Vminus/Vabs from the EXISTING saved rational box, without rerunning
the root search. The saved phase_recovery.json is PASS. I read
that artifact and src/optimal_endpoint_phase.py without executing
them; I also checked their coefficient, centering and variance
formulas against the paper identities above.

The source reconstructs the reflected cubic and Q by interval
convolution. Exactly one coefficient, at z^2, is negative, and
all the others are positive. The strict rational interval gates
prove qmax<1, Nminus/S<1/8 and alpha<1/8. The saved upper-bound
displays are approximately

    qmax upper=.7861605954,
    Nminus/S upper=.06888684968,
    alpha upper=.00262295743.

The proof uses the exact rational intervals, not these rounded
displays. The signed centroid is computed from sum j*qj/S,
Vminus from the sole negative coefficient times(2-mu)^2, and
Vplus from the remaining coefficients. The code separately
checks Vminus<(55/(2S))/6, agreeing with the intrinsic budget
(10)--(11). The cubic root bracket is inherited from and checked
against the already independently verified n5 box. No new real
root or candidate support was searched.

This is a genuine finite selection recovery: ALL nonnegative
optimal branches fail the particular C=1 amplitude condition,
while this signed optimal branch meets ALL three stable-branch
conditions with C=1. The newly negative coefficient is close to
the reflected centroid, so its variance cost is small by (14).
The factor has the same lambda=M(A) and the same all-circle
identity, so the selection recovers sufficient-factor geometry
rather than improving the actual finite minimum.

It supplies no universal branch-selection estimate, unbounded
endpoint counterfamily or new minimum record. The exact five-
frequency example does not justify another support sweep or a
greedy root-reflection conjecture; the explicit first-coefficient
obstruction in Section6 must remain part of the handoff. All
three root-run jobs are recorded terminal/PASS; the advisor ran
none of them and performed no VM lifecycle operation or GPU work.

## 8. One nonreal conjugate-pair reflection

For an outside conjugate pair, write its real quadratic factor as

    D(z)=z^2-2u*z+v, v>1, u^2<v,
    Dr(z)=1-2u*z+v*z^2,
    Q=D*C, Qr=Dr*C, C=sum_j c_j*z^j.

The strict condition u^2<v means the pair is nonreal, and v is
its squared modulus. Extend c_j by0 outside its finite range.
The exact coefficient update is

    q_j=v*c_j-2u*c_(j-1)+c_(j-2),
    q'_j=c_j-2u*c_(j-1)+v*c_(j-2),
    Delta q_j=(v-1)*(c_(j-2)-c_j).                (15)

Because Dr is the real reversal of D, |Dr|=|D| on the unit circle.
Furthermore

    D(1)=Dr(1)=v+1-2u=(1-u)^2+(v-u^2)>0.

Thus S and lambda are exactly unchanged, and logarithmic
differentiation gives the centroid shift

    mu_r=mu+delta,
    delta=2*(v-1)/(v+1-2u)>0.                     (16)

The numerator is Dr'(1)-D'(1). This checks both the factor2 and
the sign. The branch-independent intrinsic variance (10) is
unchanged as well. With n_j=(-q_j)_+ and n'_j=(-q'_j)_+, the
SAME exact accounting applies:

    Nminus_r-Nminus=(||q'||_1-||q||_1)/2,
    Vminus_r-Vminus
       =-2delta*Bminus+delta^2*Nminus
          +sum_j(n'_j-n_j)*(j-mu-delta)^2.         (17)

Here Bminus is computed with the OLD centroid. The reverse
reflection is the inverse move and reverses the centroid shift.
No negative-mass, variance or maximum-coefficient monotonicity
is implied by (15)--(17).

Together with Section6, this gives the exact one-step bookkeeping
for negative-real and nonreal-pair root moves in a real spectral
branch. The remaining task must control these quantities JOINTLY
under a selection of flips, rather than merely balance endpoint
products or replace the falsified constant1 by another untested
constant. The n5 recovery proves that one signed move can work;
the filter identity proves why a large-endpoint balancing heuristic
can fail to reduce the GLOBAL maximum.

These stable-factor hypotheses are sufficient conditions, not
proved necessary conditions for Chowla and not a completeness
theorem for signed negative-Rayleigh witnesses. Neither general
existence of a branch meeting them nor an iterative descent
preserving both budgets has been established. All statements
in this subsection are paper algebra; no new computation or
resource action was performed.
