# Independent audit: one nonnegative spectral factor

2026-10-23. Internal AI advisor, paper derivation and read-only ledger
comparison. Only this assigned note is edited. No research computation,
VM operation, GPU, extra agent or outreach. Shared Dirichlet remains on.

The proposed weighted-centroid lemma is CORRECT, with its single-factor
scope essential. The bounded-amplitude statement slightly sharpens as
below. No uniform coefficient bound at an optimal factor is established.

## 1. Statement and normalization

Let A be a nonempty finite set of distinct positive integers, n=|A|,
and f_A(x)=sum_(a in A)cos(a*x). Suppose there are a finite B subset Z
and strictly positive real q_b such that, for all real x,

    lambda+f_A(x)=|Q(e^(ix))|^2,
    Q(z)=sum_(b in B)q_b*z^b.

Zero coefficients are trimmed from B. Put k=|B|>=2 and

    r_Q(d)=sum_b q_b*q_(b+d),
    S=sum_b q_b, qmax=max_b q_b.

Constant and nonconstant Fourier coefficients give

    lambda=sum_b q_b^2,
    A=diff_+(B), r_Q(d)=1/2 for d in A,
    S^2=lambda+n.                                 (1)

The exact support identification uses positivity: no unwanted difference
coefficient can cancel. The endpoint product is1/2, so lambda>=1.

The proved coefficient-sensitive estimate is

    lambda-1/2 >= sqrt(lambda+n)/(4*qmax).          (2)

In particular,

    n<=16*lambda*(lambda-1/2)^2-lambda,
    lambda>=(n/16)^(1/3).                          (3)

If L=qmax/qmin, then

    k<=4L*(lambda-1/2),
    n<=(k-1)*lambda
       <=[4L*(lambda-1/2)-1]*lambda,
    lambda>=sqrt(n)/(2*sqrt(L)).                   (4)

The last bound is a convenient weakening of the preceding exact one.
All bounds concern the certificate energy lambda. They concern actual
M(A) only if the stated representation is available at lambda=M(A).

## 2. Exact weighted Gram proof

Set

    mu=(sum_b b*q_b)/S,
    x_b=(b-mu)*q_b,
    V1=sum_b q_b*(b-mu)^2,
    V2=sum_b q_b^2*(b-mu)^2.

Then sum_b x_b=0 and V1,V2>0. Define all signed-lag quantities

    U_d=sum_b q_b*q_(b+d)*(b-mu).

Important: U_0=sum_b q_b^2*(b-mu) is generally NOT zero. The
centering cancels sum x_b, not U_0. We retain U_0 in the upper
identity and discard its nonnegative square in the lower bound.

Expanding over all integer d gives exactly

    sum_d U_d^2=x^T G x,
    G_bc=r_Q(b-c).

By (1), G has diagonal lambda and ALL off-diagonal entries1/2:
every difference between distinct B-points belongs to A. Thus

    G=(lambda-1/2)*I+(1/2)*J,
    sum_d U_d^2=(lambda-1/2)*V2.                   (5)

For d>0, changing from lower to upper endpoint gives

    U_-d=U_d+d*r_Q(d).

Consequently

    sum_d U_d^2
      >=sum_(d>0)(U_d^2+U_-d^2)
      >=(1/2)*sum_(d>0)r_Q(d)^2*d^2
      =(1/4)*sum_(d>0)r_Q(d)*d^2.                 (6)

The last equality uses the EXACT value r_Q(d)=1/2 at every
nonzero lag; arbitrary positive autocorrelations do not suffice.
The weighted pair-variance identity is

    sum_(d>0)r_Q(d)*d^2
      =sum_(b<c)q_b*q_c*(b-c)^2=S*V1.             (7)

Combining (5)--(7) with V2<=qmax*V1 yields

    (lambda-1/2)*qmax*V1 >= S*V1/4.

Here lambda>=1 makes the multiplication by lambda-1/2 harmless.
Divide by V1>0 to obtain (2). Since qmax<=sqrt(lambda), squaring
gives the exact first inequality in (3). Dropping its negative
lower-order terms proves the displayed cubic certificate floor.

For (4), S>=k*qmin implies S/qmax>=k/L. Apply (2) before replacing
qmax by sqrt(lambda), and use S^2<=k*lambda together with (1).
This gives k<=4L*(lambda-1/2) and n<=k*lambda-lambda, as asserted.

## 3. Comparison with existing P8, P76, and the positive-factor note

I inspected PROOFS P8 and P76, and the actual prior note
cstar_positive_factor_energy_2026-10-20.md. Their normalizations
differ: the prior positive-factor note has nonzero correlations1
and energy K=2lambda after multiplying the current Q by sqrt(2).

P76 already supplies the cancellation-free support identification
and clique/CP perspective. For a single factor its Cauchy step
is exactly n<=(k-1)*lambda. It does not supply the new weighted
centroid comparison (2), and CP sums do not let one apply (2)
to each summand: individual correlations need not equal1/2.

P8 proves n<=2*mu_bar*lambda^2 and its maximum-multiplicity
variant for much more general, even signed/complex factors. It
does give an OLD bounded-L consequence when combined with the
endpoint product. Namely qmax>=1/sqrt(2), so
qmin>=1/(sqrt(2)*L). Every summand in a lag correlation is at
least qmin^2; hence its integer multiplicity is at most L^2.
Applying P8 gives

    lambda>=sqrt(n)/(sqrt(2)*L).                   (8)

Thus (8) is stronger than the convenient last bound in (4) for
1<=L<2; they agree at L=2. The centroid bound improves the
dependence on L for L>2. Do not label bounded-amplitude square-root
behavior itself new merely because it is rederived here. No
uniform bound on mu_bar is supplied by the factor hypothesis.

The old positive-factor note proves endpoint restrictions near
the minimal energy, low-support facts, and a countercontrol to
using only outer-lag equalities. It explicitly leaves the large-
energy positive-factor question open. Its inspected statements do
not contain (2) or (3). This is a project-ledger comparison, not
an external novelty search or a priority claim.

## 4. Optimality and the missing qmax estimate

If a single positive factor exists at lambda=M(A), then a global
minimum forces Q to have a zero on the unit circle. Conversely a
zero in a valid factorization forces lambda=M(A). This observation
does not make the factor coefficients uniformly bounded.

The root's explicit nonoptimal countercontrol checks. For A={1,2},
take any t>0 and

    Q=(t, 1/[2*(t+1/(2t))], 1/(2t)).

Its lag2 product and lag1 correlation are both1/2, for all t.
Its coefficient maximum tends to infinity as t tends to infinity.
To see exactly why this is not an optimal counterexample, write
u=t+1/(2t)>=sqrt(2). Then

    lambda(t)=u^2-1+1/(4u^2)>=9/8.

Equality holds only at t=1/sqrt(2). Also
f_{1,2}=2*cos(x)^2+cos(x)-1 has actual M=9/8. Thus the unbounded
coefficients are solely nonoptimal certificates. At optimality
this example has Q=(1,1/2,1)/sqrt(2), with bounded coefficients.

A unit-circle zero yields the triangle restriction qmax<=S/2,
but that is not a uniform coefficient bound. The old endpoint
restriction sharpens the location of a possible concentration:
if a,d are the two endpoint coefficients, ad=1/2 and every
interior coefficient is at most min(a,d). Thus qmax=max(a,d),
and every other coefficient is at most1/(2*qmax). At a unit-circle
zero their sum must be at least qmax, forcing k-1>=2*qmax^2.
This permits growing k and does not give qmax=O(1). It is an
application of the OLD endpoint restriction, not a new inverse
theorem. The elementary audit here provides neither a proof of
the uniform optimal-factor bound nor a Boolean counterfamily.
Intervals are a potential adversary only if the needed positivity
of their optimal spectral-factor coefficients is proved; it was
not proved or assumed in this audit. No numerical interval trend
or positive-factor search was run.

If one established qmax<=C in a factor at lambda=M(A), (2) would
give M(A)>=sqrt(n)/(4C). Both existence of such an optimal
nonnegative factor and the coefficient bound are additional
requirements, not consequences of ordinary Fejer--Riesz
factorization. General factors can have signed or complex
coefficients and cancel unwanted differences; then the exact
constant-off-diagonal Gram and support identification fail.

## 5. Status and next distinction

Equations (1)--(8) and the nonoptimal countercontrol are checked
paper statements. They are not kernel-checked or externally
scrutinized, and no novelty claim is made. No numerical input was
used in their proof. The genuine ingredient beyond positivity of
lambda+f is one cancellation-free factor with every nonzero
autocorrelation EXACTLY1/2. This is a useful weighted certificate
constraint, not yet an unrestricted Boolean inverse theorem.

The remaining distinction is coefficient concentration at an
OPTIMAL nonnegative factor, or a different argument handling
signed phase cancellation. Neither is settled by this note.
No representation theorem, general Chowla exponent improvement,
construction family or resource action follows.
