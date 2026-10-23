# Full run cancellation and a joint root-ensemble test

2026-10-23. Continuation of781bfd9, classified as progress. Full
Chowla remains open. This checkpoint contains paper identities,
internally reviewed reductions, and two fixed interval-certified
ensembles. No universal exponent, stable-branch theorem, priority,
external scrutiny or kernel verification is claimed. Complete
[sole-advisor derivations](advisor_run_multiplier_2026-10-23.md).

## The promised finite-run calculation was carried out

Use S=±A,N=2|A|,D=2f_A,K=2M, t>0 in S. Let B=B_t be the
nontrivial t-run tops, L=-B their starts, d=1-exp(itx),
w=D*1_{K^2<D<N-K}, and P the polynomial containing every vertex
of a nontrivial run except its top. Full geometric telescoping gives

    F_B=F_L-dP, q=dF_B=dF_L-d^2P.

Reflection gives |dF_L|=|dF_B| pointwise, including under the ACTUAL
multiplier w. Therefore the full expansion is exactly

    2Re<dF_L,d^2P>_w=||d^2P||_w^2.

Cauchy yields J=||q||_w^2>=||d^2P||_w^2/4: a LOWER bound,
not the required upper estimate. The complete Fourier summation
by parts has the same cancellation. Its kernel is

    kappa(v)=2*w_hat(v)-w_hat(v+t)-w_hat(v-t),
    J=sum_(b,c in B)kappa(b-c).

Telescoping each top back to its start sums to zero by reflection;
absolute values introduce uncontrolled run lengths/kernel variation.
Continuous integration by parts also retains level-crossing atoms
at D=K^2 and D=N-K. They cannot be discarded. See advisorSections2-3
for the full formulas, including crossing orientation at tangencies.

If I is the Fourier polynomial of the t-isolated singleton vertices,
the other complete-run identity is

    Re q=(1-cos(tx))(D-I).

This too gives a LOWER bound for J and remains valid in cyclic models.
Decision: retire this run compression. The integer middle-band estimate
it was meant to prove is still open, not refuted. Do not repeatedly
rename its derivative/cross-term remainder as a new route.

## Mathematical pivot: real reciprocal-root choices

Return to the existing SIGNED-CENTROID route, not a new version of
the run-top target. Let

    lambda=M(A), p=lambda+f_A=|Q|^2,
    S0=Q(1)=sqrt(lambda+|A|)>0, X=max A,
    V=sum_(a in A)a^2/(2S0).

Here S0 is a scalar, unrelated to the symmetric frequency set above.
Every real factor can be described by a fixed palindromic unit-circle
factor U and independent choices D_j versus D_j^rev from nonunit
reciprocal real blocks. Repeated blocks may be labelled; the product
law is then on choices, not necessarily on distinct polynomials.
For the two examples here all blocks/branches are distinct.

Put A_j=(D_j+D_j^rev)/2, B_j=(D_j-D_j^rev)/2. Under independent
fair signs epsilon_j,

    Q_e=U*product_j(A_j+epsilon_j*B_j),
    E Q_e(z)Q_e(w)=U(z)U(w)*product_j[A_j(z)A_j(w)+B_j(z)B_j(w)].

This identity retains coefficient covariance exactly. More generally
the 2r-point kernel replaces the local factor by

    (product_(ell=1)^(2r) D_j(z_ell)
       +product_(ell=1)^(2r) D_j^rev(z_ell))/2.

Writing mu_e=Q_e'(1)/S0 gives

    mu_e=X/2+sum_j epsilon_j*theta_j,
    theta_j=D_j'(1)/D_j(1)-deg(D_j)/2.

Thus E mu=X/2 and Var(mu)=sum theta_j^2. Coefficient signs and
this centroid are correlated. Replacing mu by its mean in a negative
variance calculation is invalid.

For q_b the branch coefficients define Nminus=sum(-q_b)_+ and
Vminus=sum(-q_b)_+*(b-mu)^2. The existing signed-centroid theorem
proves root Chowla for a branch satisfying

    qmax<=C, Nminus<=S0/8, Vminus<=V/6.              (STABLE)

No universal selection of such a branch is known here. The new
root-dependent sufficient certificate uses

    sigma_b^2=E q_b^2,
    R_b=E(b-mu)^2,
    L_b=E[q_b^2*(b-mu)^2],
    B_N=(sum_b sigma_b-S0)/2,
    B_V=(sum_b sqrt(L_b*R_b)-V)/2.

Weighted Cauchy proves E Nminus<=B_N and E Vminus<=B_V. The
centroid-tilted two-point kernel in advisorSection7 computes L_b
WITHOUT assuming independence from mu. For C>0 and integer r>=1,

    8B_N/S0+6B_V/V+C^(-2r)*sum_b E q_b^(2r)<1       (ENS)

is sufficient for a stable branch by Markov/union, or simply by
averaging the nonnegative sum of the three normalized costs.
At r=1 the last term is lambda/C^2, so second moments alone do
not give a constant-C universal certificate as lambda grows.

## A complete dilation ensemble refutes the naive mean budget

For A0={1,2,3}, exact optimal

    u=(sqrt7-1)/6, lambda=(17+7sqrt7)/27<sqrt3,
    c=1/2+2u, a=c+sqrt(c^2-1),
    Q0=(z^2-2u*z+1)*(z+a)/sqrt(2a).

The identity f(v)+lambda=4(v-u)^2(v+c) on[-1,1] proves the actual
minimum. Q0 has positive coefficients and qmax=sqrt(a/2)<1.
Dilate by8. The fixed factor is
U=(z^16-2u*z^8+1)/sqrt(2a); the four nonunit real blocks are

    D_j=z^2-2R*cos((2j+1)pi/8)*z+R^2,
    R=a^(1/8), j=0,1,2,3.

All16 real branches were checked. Certified E Nminus/S0 lies in
(0.2248,0.2250), exceeding1/8. Exactly the base lift and its reverse
satisfy(STABLE) with C=1; all14 mixed branches fail its mass budget.
Real quadratic192-bit and independent complex linear256-bit Arb
calculations agree. The all-circle actual lambda has a separate
exact quadratic-field polynomial proof, not a sampled minimum.

The correlated law choosing ALL four signs together, fair±1, has the
SAME one-block marginals and only those two good branches. Its
actual joint cost with C=1,r=2 is in(0.6594,0.6596)<1. A paper
bound suffices: a<7/5,lambda<4/3 imply sum q_b^4<=qmax^2*lambda
<14/15, while Nminus=Vminus=0. Larger centroid variance can thus
coexist with ZERO negative cost; centroid balancing is not an objective.

Important qualification: gcd{8,16,24}=8. Normalizing gcd avoids
this example, so it does not refute a primitive-support hypothesis.

## Primitive support: mass alone passes, but the joint certificate fails

The advisor supplied a primitive discriminator A={1,7,8}, not a larger
search. Since

    f_A=(|1+z+z^8|^2-3)/2,

actual M=3/2<sqrt3, attained at primitive cube roots. Let

    1+z+z^8=(1+z+z^2)*(1-z^2+z^3-z^5+z^6).

The residual has three distinct nonunit conjugate pairs and no real
roots. Unit roots of the trinomial are only the two primitive cube
roots; squarefreeness and gcd with its reversal are checked exactly.
The positive base Q=(1+z+z^8)/sqrt2 and its reverse satisfy(STABLE).

All EIGHT real factors were evaluated at256 bits. Six disjoint root
disks of radius10^-40 were certified by the explicit Rouche bound

    |H(center)|+sum_(k>=2)|H^(k)(center)/k!|r^k
          < |H'(center)|r.

Root proposals alone carry no certification status. The six certified
disks cover the degree6 polynomial, and all budget operations enclose
the exact root-dependent values. Real quadratics and complex linear
factor multiplication independently give matching budgets, sharing Arb.

The resulting rigorous bounds are

    E Nminus/S0 in(0.1221,0.1223) <1/8,
    E Vminus/V  in(0.0646,0.0647),
    8E Nminus/S0+6E Vminus/V >27/20>1 (approximately1.3652).

Therefore the SIMPLE primitive mean-mass bound is NOT refuted by
this case. But(ENS) under the unbiased law is REFUTED for EVERY C,r:
its first two upper bounds already exceed1, and its remaining term
is nonnegative. Gcd preprocessing does not fix this JOINT failure.
Four branches meet allC1 budgets; the known base/reverse have exact
joint cost3/4. The failure belongs to the averaging certificate,
not to stable-branch existence or to Chowla.

Sources/data: src/root_ensemble.py, src/root_ensemble_verify.py,
src/primitive_root_ensemble.py and
experiments/root_ensemble_2026-10-23/{results,verification,primitive}.json.
All research computation used src/dirun.sh,2cores/4GB,120second caps;
individual jobs took<1second of compute. No GPU or VM lifecycle action.

## Arbitrary correlations are not an independent reduction

Global reversal maps every branch epsilon to-epsilon, preserves its
qmax,Nminus,Vminus and any corresponding joint cost. Pair ANY one
branch with its reverse. Every block marginal is then fair±1.
Consequently, for any reversal-invariant branch cost Phi,

    inf_(joint laws with all fair marginals) E Phi
         =min_(real branches) Phi.

One inequality is averaging; the other is the branch/reverse law.
Thus optimizing unrestricted correlations is exactly the old branch-
selection problem. Do not announce a new universal route merely by
allowing correlations after independence fails. A useful next rule
needs an actual quantitative Boolean sign or descent inequality.

All even LOG-cumulants of Q(exp(v))/S0 are branch-invariant. In
particular the signed central fourth moment is

    sum_b q_b*(b-mu)^4
       =sum_A a^4/(2S0)-3(sum_A a^2)^2/(4S0^3).

The sixth CENTRAL moment need not be invariant: it contains the
branch-dependent10*kappa3^2. These identities do not bound the
negative budgets.

Global decision: retire the full-run compression and universal
independent(ENS), including its primitive version. Keep the exact
kernels as finite verification tools. Do not enlarge either ensemble
or assume a greedy root-flip descent without deriving its sign.
Indeed the advisor identified a strict BAD one-block local minimum
of Phi=8Nminus/S0+6Vminus/V+sum q_b^4 in the SAVED L8 cube.
At epsilon choices(0,1,1,0) the certified cost interval is
[49710981568265215999,49710981568265347073]/2^64, entirely above1.
The four neighbor LOWER numerators, over the same denominator, are
66757129393733681151,65279950696696037375,65247914232150024191,
66962980272272252927. Each exceeds the vertex's upper numerator.
Its complement is another such trap. The verifier checks all these
rational inequalities after independently recomputing the costs.
Thus universal one-block descent for THIS joint cost is refuted,
despite an explicit good global branch. This example has gcd8;
no primitive-only local-descent theorem is claimed either way.
The goal remains full Chowla; no result here improves the universal
exponent or supplies an effective vanishing-ratio family.

Scope of these falsifications: BOTH sets have cardinality3 and
R(A)>3/4. Dilation increases the degree, not cardinality. They do
NOT refute a proposed estimate restricted to sufficiently large n,
to a substantially smaller fixed ratio, or to a hypothetical R→0
sequence. Such a conditional/asymptotic repair is unproved, not
excluded. The strategic decision retires the UNQUALIFIED rules
tested here, not every use of independent choices in a different
regime. Do not turn finite counterexamples into a blanket method
impossibility or expand the same controls to simulate such evidence.

## First next derivation: a coupled square with exact lagwise Booleanity

Advisor-directed pivot within the signed-factor line; do not introduce
a general two-flip descent conjecture. Keep two root blocks variable:

    Q_(sigma,tau)=a+sigma*b+tau*c+sigma*tau*d,
    a=C*A_i*A_j, b=C*B_i*A_j,
    c=C*A_i*B_j, d=C*B_i*B_j, ad=bc.

With R_uv(h)=sum_k u_k*v_(k+h), constancy of autocorrelation for
all four choices gives the exact Walsh equations

    C0=R_aa+R_bb+R_cc+R_dd=lambda*1_(h=0)+(1/2)1_(h in ±A),
    C_sigma=R_ab+R_ba+R_cd+R_dc=0,
    C_tau=R_ac+R_ca+R_bd+R_db=0,
    C_sigmat=R_ad+R_da+R_bc+R_cb=0.

The nonconstant equations and ad=bc hold for weighted positive
polynomials too. The specifically Boolean input is LAGWISE
C0(h)^2=C0(h)/2 for h!=0. Summing this immediately only recovers
the old fourth-norm identity, not a new inequality.

Let mu=mu0+sigma*theta+tau*eta and y_k=k-mu0. The centered
derivative vector x_k=(k-mu)q_k has four exact Walsh components:

    x0=y*a-theta*b-eta*c,
    x_sigma=y*b-theta*a-eta*d,
    x_tau=y*c-theta*d-eta*a,
    x_sigmat=y*d-theta*c-eta*b.

These retain the moving centroid. First next operation is to insert
the FOUR vectors into the existing exact Boolean Gram/missing-lag
identity, retaining its mixed Walsh coefficient, and try to bound
that signed interaction using the lagwise0-or1/2 equations BEFORE
aggregation. A useful inequality must control an actual collective
term; listing these identities is not progress on selection itself.
Kill this refinement if it gives only norm/centroid invariants or
continues to hold unchanged in the certified weighted geometric
countermodel. No new ensemble, root-flip blocksize sweep or greedy
claim is authorized by this calculation.
