# Full run telescope, its limitation, and a root-ensemble pivot

2026-10-23. Sole internal AI advisor. Paper derivations and read-only
ledger review; no mathematical computation, VM action, GPU, extra agent
or outreach. Shared Dirichlet is untouched. No new universal exponent,
Chowla resolution, kernel verification or external-priority claim.

## 1. Exact multiplier and question

Let S=-S be a nonempty finite subset of Z\{0}, N=|S|,
D=sum_(s in S)exp(isx), K=-min_circle D, and t>0 belong to S.
Write

    A_t=S intersect(S+t),
    B=B_t={s in S:s-t in S,s+t not in S}, m=|B|,
    d(x)=1-exp(itx), q=d*F_B,
    Omega={x:K^2<D(x)<N-K}, w=D*1_Omega,
    J=integral w*|q|^2.

All integrals are normalized by dx/(2pi). If Omega is empty there
is nothing to estimate. Otherwise w is real, even and nonnegative.
The retained sufficient target is J<=C*K^2*m. It remains UNPROVED
in Z. The prior exact localization is H<=6K^2*m+J; the prior
centered determinant then gives a conditional exponent1/4.

The complete finite-run calculation below does NOT prove this target.
It gives an exact reflection cancellation and a lower energy bound.
No multiplier is dropped or replaced by1.

## 2. Finite runs and the full polynomial identity

Index the nontrivial t-runs by i. Their starts and tops are

    alpha_i, beta_i=alpha_i+L_i*t, L_i>=1.

The starts form L=-B because S is symmetric. Define the full prefix
polynomial, retaining every vertex before each top,

    P=sum_i sum_(r=0)^(L_i-1)exp(i*(alpha_i+r*t)*x)
     =F_(A_t-t).

Geometric telescoping along every run proves

    F_B=F_L-d*P,
    q=d*F_L-d^2*P.                                  (1)

This contains the run lengths without approximation. On the circle,
F_L=conj(F_B), so |d*F_L|=|d*F_B| POINTWISE. Consequently expansion
in the weighted L2(w) inner product gives exactly

    2Re<d*F_L,d^2*P>_w=||d^2*P||_w^2.               (2)

The endpoint energy J has canceled from both sides. Cauchy-Schwarz
in(2) yields only

    J>=||d^2*P||_w^2/4.                              (3)

This is the wrong direction for the desired upper bound. Keeping
all cross terms is essential: the cross term in(2) is exactly half
the purported positive correction, not a sign error or a small term.
The cancellation is pointwise before integrating, so the special
dependence w=D*1_Omega does not repair this step automatically.

## 3. Complete Fourier-kernel summation by parts

Let w_hat(k)=integral w*exp(-ikx), and set

    kappa(v)=2*w_hat(v)-w_hat(v+t)-w_hat(v-t).

The exact formula retaining the entire multiplier is

    J=sum_(b,c in B) kappa(b-c).                      (4)

Here w_hat and kappa are real and even. In particular kappa is the
Fourier coefficient sequence of w*|d|^2, a nonnegative function.
Its Toeplitz kernel is positive semidefinite, but individual
off-diagonal coefficients need not have either sign.

Write Delta_plus k(v)=k(v+t)-k(v) and
Delta_minus k(v)=k(v-t)-k(v). For EACH pair of runs, complete
telescoping gives

    kappa(beta_i-beta_j)-kappa(alpha_i-alpha_j)
      =sum_(r=0)^(L_i-1) Delta_plus kappa(alpha_i+r*t-beta_j)
       +sum_(s=0)^(L_j-1) Delta_minus kappa(alpha_i-alpha_j-s*t).
                                                               (5)

Summing i,j makes the left side zero: the starts are -B and
kappa is even, so their energy equals the top energy. Thus(5)
is the kernel form of the same cancellation in(2), not an upper
bound on J.

Taking absolute values replaces that exact cancellation by variation
along all run segments. Since integral w<=integral D_+<=K,

    |kappa(v)|<=4K,
    |Delta_plus/minus kappa(v)|<=8K.

The variation sum in(5) has2m*sum_i L_i=2m*|A_t| terms. The
resulting generic scale is16K*m*|A_t|, not K^2*m; it does not
even bound J until another comparison is supplied. Any improvement
must control these actual signed weighted differences. Run finiteness
alone does not license a constant bound independent of their lengths.

For completeness, trying continuous integration by parts merely
exposes the same multiplier dependence. Put a=K^2,b=N-K, a<b.
In distributions on the circle,

    dw=1_(a<D<b)*D' dx
       +a*sum_(D(r)=a) sigma_r*delta_r
       -b*sum_(D(r)=b) sigma_r*delta_r,              (6)

where sigma_r is the crossing orientation, zero at a noncrossing
tangency. This definition covers an odd higher-order crossing even
when D'(r)=0. For k!=0,

    w_hat(k)=(1/(2pi*i*k))
       *[integral_(a<D<b) D'(x)exp(-ikx)dx
          +a*sum_(D(r)=a)sigma_r exp(-ikr)
          -b*sum_(D(r)=b)sigma_r exp(-ikr)].          (7)

The level-crossing terms cannot be deleted. The elementary variation
bounds depend on max S through D' and the number of crossings;
no degree-free O(K^2*m) estimate follows. Replacing the sharp window
by a smooth cutoff changes these terms but does not provide the
missing quantitative control on D' or on the signed run sums.

## 4. A further exact real-part identity, still in the wrong direction

Let C_t consist of the t-isolated singleton vertices of S, and let
I=F_Ct. This is real because C_t=-C_t. For the union U of the
nontrivial runs, F_U=D-I. Telescoping full runs gives

    d*(D-I)=conj(F_B)-exp(itx)*F_B.

Multiply by conj(d) and take the real expression to obtain

    Re(q)=(1-cos(tx))*(D-I).                         (8)

Therefore the complete energy splits as

    J=integral w*(1-cos(tx))^2*(D-I)^2
           +integral w*(Im q)^2.                    (9)

This is an exact lower decomposition, not a way to discard the
imaginary part in an upper bound. It exposes another positive cost
that would need control rather than proving it small.

These geometric telescopes also hold on proper cyclic runs. A full
cycle contributes zero after multiplication by d. The periodic O4
model therefore satisfies their phase versions, even though its
middle energy violates the group O(K^2*m) target. Integer first
moments give one extra jet at the identity, already compatible with
the near-maximum cancellation; they do not determine the full
weighted kernel in(4).

## 5. Decision and actual mathematical pivot

Stop this finite-run compression as a claimed route to the missing
upper estimate. This does NOT refute the INTEGER middle estimate,
nor every possible use of order. It identifies its exact failed step:
the full telescope gives(2), while an upper bound would require an
independently proved variation estimate in(5) or(7). Naming that
unknown estimate is not progress.

A proposed return to an integer O4/Kerdock lift was checked against
the existing ledger. The parent located its earlier OR2/cohomological
and tapered-profile analysis in NOTEBOOK1399-1542 and P24/P27.
Do not restart that construction under a new name or run a control
without a changed mathematical mechanism.

The changed next calculation is instead inside the EXISTING
signed-centroid/factor-selection route: study the WHOLE ensemble of
real spectral factors under independent reciprocal-root choices,
retaining coefficient and centroid correlations. This is different
from projecting a single factor, a scalar endpoint bound or a fixed
allpass-kernel norm. The ultimate stable-factor gap remains open.

## 6. Exact real-branch ensemble

Let A be a nonempty Boolean positive-frequency set, n=|A|, X=max A,
lambda=M(A), and p=lambda+f_A. Choose a real factor Q with no
monomial padding and orient Q(1)=S=sqrt(lambda+n)>0. Separate its
unit-circle factor U and real off-circle reflection blocks D_j.
Every D_j is either a real linear block or an outside nonreal
conjugate-pair block; repeated roots can be labeled as separate copies.
Reversing a block preserves its circle modulus and its value at1.

Include the common real scalar in U, and put

    A_j=(D_j+D_j^rev)/2, B_j=(D_j-D_j^rev)/2,
    Q_epsilon=U*product_j(A_j+epsilon_j*B_j),
    epsilon_j independent fair signs.

The unit factor U is palindromic. There is no root at1 because
p(1)>0. Unit roots at-1 and conjugate unit pairs have fixed half
multiplicities. Hence Q_epsilon^rev=Q_(-epsilon), all branches
have the same value S at1, and every real branch is included up to
overall sign and monomial translation. Repeated labeled choices
need not be uniform on DISTINCT factors; the product-sign law is
the law used in the following identities.

Independence gives the EXACT two-variable kernel

    E[Q_epsilon(z)Q_epsilon(w)]
      =U(z)U(w)*product_j[A_j(z)A_j(w)+B_j(z)B_j(w)]. (10)

The mean is U*product A_j and is palindromic. The complementary-
branch kernel changes PLUS to MINUS between the two products in
each factor. Thus coefficient covariance and expected reversal
antisymmetry can be evaluated without enumerating all branches.
At z=w on the circle the Hermitian version gives the deterministic
modulus p; this recovers the known factor norm, not a new bound.

More generally every integer r>=1 has the exact2r-variable moment
kernel

    E product_(ell=1)^(2r) Q_epsilon(z_ell)
      =product_ell U(z_ell)
        *product_j[(product_ell D_j(z_ell)
                         +product_ell D_j^rev(z_ell))/2]. (11)

The coefficient with every z_ell exponent a is E q_a^(2r).
No positivity or independence of the resulting coefficients is assumed.

## 7. Centroid correlations and a precise sufficient joint-budget test

Put d_j=deg D_j and

    theta_j=D_j'(1)/D_j(1)-d_j/2.

The signed coefficient centroid of the random branch is EXACTLY

    mu_epsilon=X/2+sum_j epsilon_j*theta_j,
    E(mu-X/2)^2=sum_j theta_j^2.                     (12)

This follows from (D_j^rev)'(1)/D_j^rev(1)=d_j-D_j'(1)/D_j(1).
Let c_a=q_a(epsilon), m_a=E c_a, sigma_a^2=E c_a^2. Define

    V=sum_(a in A)a^2/(2S)>0,
    R_a=E(a-mu)^2=(a-X/2)^2+sum_j theta_j^2,
    L_a=E[c_a^2*(a-mu)^2].

The signed variance sum_a c_a(a-mu)^2 equals V for EVERY branch.
Consequently weighted Cauchy-Schwarz proves the coupled bounds

    E Nminus <=B_N=(sum_a sigma_a-S)/2,
    E Vminus <=B_V=(sum_a sqrt(L_a*R_a)-V)/2.         (13)

The second inequality retains the actual coefficient/centroid
correlation in L_a; replacing mu by an independent mean or by X/2
would be wrong. Both right sides are nonnegative.

These mixed moments have an exact generating kernel. With v a real
auxiliary variable, define

    Phi(z,w;v)=E[Q_epsilon(z)Q_epsilon(w)
                              exp(v*(mu_epsilon-X/2))]
      =U(z)U(w)*product_j{
          cosh(v*theta_j)[A_j(z)A_j(w)+B_j(z)B_j(w)]
         +sinh(v*theta_j)[A_j(z)B_j(w)+B_j(z)A_j(w)]}.

Extract z^a w^a after applying
(a-X/2-d/dv)^2 and setting v=0 to obtain L_a. Thus (13) is
a finite root-dependent calculation, not a new moment independence
assumption or a claim of efficient high-degree evaluation.

For any fixed C>0 and integer r>=1, a sufficient selection certificate
is the strict inequality

    8B_N/S+6B_V/V+C^(-2r)*sum_a E c_a^(2r)<1.        (14)

Indeed Markov plus the union bound gives positive probability of

    Nminus<=S/8, Vminus<=V/6, qmax<=C.

Since V=Vplus-Vminus, the variance condition is equivalent to
alpha<=1/8. The existing independently audited signed-centroid
theorem then gives S<=16C(lambda-1/2), hence
M(A)>=sqrt(n)/(16C). Therefore a UNIVERSAL proof of(14) with some
absolute C, under actual M<=sqrt(n), would prove full Chowla.

Crucial limits: (14) is a STRONGER sufficient condition for this
particular unbiased ensemble, not a necessary condition for a good
branch. A good branch can have exponentially small product-sign
probability. Nothing above proves (14), bounds a Boolean ensemble
mean, or authorizes a random factor search. At r=1 its final term
is exactly lambda/C^2, so a fixed-rank second-moment union bound
alone is useless when lambda grows. Higher/mixed coefficient
information is necessary even within this conditional certificate.

This is a concrete sufficient selection certificate tied to full Chowla,
not a repackaging of the endpoint middle integral. Its proposed
UNIVERSAL unbiased use is refuted by the explicit test below. The
formulas remain true; their upper bounds are not proved small.

## 8. Exact adversarial ensemble and invariant-moment scope

The parent proposed ONE discriminating test of the simpler mean
claim E Nminus<=S/8. I checked its paper setup, without computation.
For A0={1,2,3},

    f(x)=4*cos(x)^3+2*cos(x)^2-2*cos(x)-1,
    u=(sqrt(7)-1)/6,
    lambda=(17+7sqrt(7))/27<sqrt(3),
    c=1/2+2u, a=c+sqrt(c^2-1)>1,
    Q0=(z^2-2u*z+1)*(z+a)/sqrt(2a).

The critical point u is the global minimizer (the other critical
point is a maximum and the endpoints have values-1,3). Also
1<c<13/12 and1<a<3/2. All four Q0 coefficients are positive:
2ua<7/8, and qmax=q0=sqrt(a/2)<1. Thus Q0 itself and its
reverse meet all three stable-branch conditions.

For dilation L=8, the fixed unit factor is
U=(z^16-2u*z^8+1)/sqrt(2a). The off-circle polynomial z^8+a
splits into exactly four real conjugate-pair blocks

    D_j=z^2-2R*cos((2j+1)pi/8)*z+R^2,
    R=a^(1/8), j=0,1,2,3.

Independent reversal gives ALL16 oriented real branches. This is
not an additional successful n5 control or a root sweep. The completed
test REFUTES the unbiased mean-mass hypothesis; details and scope
are recorded in Section9. Stable existence and a claim restricted
to primitive gcd-normalized supports are not refuted.

For every real branch, q0*qX=1/2. Here the random log endpoint has
variance (log a)^2/(2L), tending to zero under even dilations even
though the interior signed costs are not controlled. Balanced
endpoints cannot replace the actual coefficient budgets.

Finally even LOG-cumulants are branch-invariant: reversal changes
log D_j(exp(v)) to d_j*v+log D_j(exp(-v)). In particular, with
A_r=sum_(a in A)a^r, the signed central fourth moment is fixed:

    sum_b q_b*(b-mu)^4=A_4/(2S)-3*A_2^2/(4S^3).

This does not extend to every even CENTRAL moment; the sixth
contains10*kappa_3^2 and can depend on the branch. These invariants
are exact constraints, not estimates of Vminus or Nminus.

## 9. Completed fixed-ensemble audit and the role of correlations

I read the complete `src/root_ensemble.py`, its independent
`src/root_ensemble_verify.py`, and both saved artifacts under
`.research/experiments/root_ensemble_2026-10-23/`. No rerun was
performed. The producer uses real quadratic factors and192-bit Arb;
the verifier uses conjugate complex linear factors and256-bit Arb.
They are different factorizations at different precisions, sharing
the Arb backend. The exact cubic identity is separately checked
in Q(sqrt(7)):

    f(v)+lambda=4*(v-u)^2*(v+c), c>1, -1<u<1.

It proves the true all-circle optimum, not a grid minimum. The
intrinsic variance in the dilation is V=448/S. All16 selected
autocorrelations and all25-by25 covariance entries are checked
against the exact spectral target and product kernel.

The saved result rigorously encloses

    E_ind Nminus/S=0.22485... >1/8,
    B_N/S=0.29462...,

and the independent verifier confirms that all14 mixed branches
fail the mass budget. Exactly the all-outside and all-inside choices
are C1-stable. This refutes the simpler unbiased mean claim and,
since B_N>=E Nminus, defeats the sufficient criterion(14) for this
ensemble for EVERY choice of r,C. No local optimization or support
search is involved. The support has gcd8: normalization to the
primitive support avoids this particular counterexample completely.
No primitive-support mean claim is silently retired.

There is a stronger paper comparison. Impose the fully correlated
law epsilon_1=...=epsilon_4=eta, eta a fair sign. It has exactly the
SAME fair one-block marginals as the independent law, but is supported
only on the two explicit positive branches. Its covariance kernel is

    K_corr(z,w)=[Q_out(z)Q_out(w)+Q_in(z)Q_in(w)]/2,

whereas the independent covariance is the PRODUCT of blockwise
averages in(10). One-block marginals cannot determine these budgets.
In fact the correlated centroid variance is (sum theta_j)^2,
instead of sum theta_j^2. The better negative-mass/variance behavior
therefore does not follow from minimizing centroid spread.

Define the nonnegative joint cost for C=1,r=2 by

    Phi=8*Nminus/S+6*Vminus/V+sum_a q_a^4.

Phi<1 implies all three stable conditions directly; E Phi<1 also
guarantees such a branch. For the correlated law Nminus=Vminus=0.
The elementary bound sqrt(7)<8/3 gives lambda<4/3 and
c<19/18<37/35, hence a<7/5. Therefore

    sum q_a^4 <=qmax^2*sum q_a^2
                 =(a/2)*lambda<14/15<1.

Thus the same-marginal laws have rigorously different selection
outcomes, with no additional numerical estimate needed for the
correlated certificate. This does not show correlations are necessary
on primitive supports or that a favorable correlated law can be chosen
universally from Boolean coefficients.

## 10. Primitive discriminator and the unlicensed greedy inference

For a genuinely primitive test there is a smaller paper setup than
isolating the optimal minimum of an interval. Take

    A={1,7,8}=diff_+{0,1,8},
    Q=(1+z+z^8)/sqrt(2), lambda=3/2<sqrt(3).

The square identity gives lambda+f_A=|Q|^2, and Q vanishes at the
primitive cube roots, so this lambda is the ACTUAL minimum. The
support has gcd1 and the positive base and reverse are stable.
The only unit roots of F=1+z+z^8 are the primitive cube roots:
on the unit circle |1+z|=1 forces Re z=-1/2. For real z=-r,
F=1-r+r^8 has minimum1-7r_*/8>1/8, r_*=8^(-1/7)<1,
and F is positive on the positive axis. Thus it has no real roots.
It is squarefree: F'=0 would give z^7=-1/8 and F=0 would then
force z=-8/7, inconsistent with that equation. Moreover

    F-F^rev=z-z^7=z*(1-z^6),

so off-circle roots are not shared with their reciprocals. Removing
Phi3 leaves the degree6 residual

    R=1-z^2+z^3-z^5+z^6,

with exactly three distinct nonunit conjugate pairs and therefore
eight real reflection branches. The parent's ONE predeclared check
has now completed; its mean-mass and joint conclusions differ as
recorded in Section11. No larger trinomials or support campaign is
licensed. No such computation is performed by this advisor.

The proposed stronger assertion that every one-block local minimum
of Phi is below1 has no derived descent mechanism. For a single
block write the two coefficient vectors as a+b and a-b. Already
the fourth-power cost difference is

    sum[(a_j+b_j)^4-(a_j-b_j)^4]
           =8*sum a_j*b_j*(a_j^2+b_j^2),

with no prescribed sign. The negative-mass difference is a sum of
absolute-value differences, and the negative-variance difference
also changes the signed centroid. Neither covariance positivity nor
endpoint balancing controls their joint sign. A bad local minimum
in an already computed cube would refute that assertion cheaply;
absence of one is not a reason to adopt it or to start a greedy
research campaign. Root-ensemble formulas and a successful known
correlated law are retained, while general correlation selection
remains a precise OPEN gap.

## 11. Primitive result: mass passes, the full unbiased certificate fails

I read the complete `src/primitive_root_ensemble.py` and its updated
saved `.research/experiments/root_ensemble_2026-10-23/primitive.json`.
Numerical roots are only proposals. The script verifies an explicit
Rouche inequality on six rational-center disks of radius10^-40:

    |H(center)|+sum_(k>=2)|H^(k)(center)/k!|rho^k
                         <|H'(center)|rho.

The disks are disjoint, off the unit circle and off the real line,
and exhaust the degree6 residual. Real coefficients pair the three
upper roots with their conjugates. The exact polynomial gcd and
squarefree checks remove reciprocal coincidences. Thus the eight
branches are complete, not just eight root proposals. Both quadratic
and complex-linear products enclose their exact coefficients; all
autocorrelations match lambda=3/2 and the bits at1,7,8. The correct
intrinsic variance is114/(2S)=57/S. Negative mass and variance are
computed with each branch's OWN signed centroid.

The certified intervals give

    E Nminus/S in(0.1221,0.1223)<1/8,
    E Vminus/V in(0.0646,0.0647),
    8E Nminus/S+6E Vminus/V>27/20>1.

For example the first two lower bounds already give3411/2500>27/20.
Therefore the simple mean-mass claim SURVIVES this primitive case.
The JOINT sufficient certificate(14) under the unbiased law fails
for EVERY C,r, because B_N>=E Nminus and B_V>=E Vminus, before
adding its nonnegative moment term. Four branches satisfy all C1
stable conditions. The positive base/reverse have exact Phi=3/4.
Failure of the stronger averaged cost is not failure of stable-factor
existence or of Chowla.

I also read the final updated256-bit L8 verifier and artifact. Their
coherent joint cost is enclosed in(0.6594,0.6596), and the explicit
fourth-power multiplications agree with the producer. Near-zero
coefficient balls are handled by multiplication, not an unresolved
power evaluation. Both implementations share Arb; this is independent
factor multiplication rather than an independent arithmetic backend.

## 12. A bad single-flip local minimum already in the saved data

No new job is needed to rule out a universal single-flip descent
claim for Phi. Reading the existing L8 intervals, at choices0110,

    49710981568265215999/2^64 <=Phi
                  <=49710981568265347073/2^64.

The lower endpoint exceeds1. Its four one-flip neighbors have
certified LOWER numerators, in the same denominator2^64,

    66757129393733681151, 65279950696696037375,
    65247914232150024191, 66962980272272252927.

Each exceeds the vertex's UPPER numerator. Thus this is a strict
bad local minimum; reversal gives its complementary counterpart.
These inequalities are direct comparisons of saved rational
enclosures, not a new optimization experiment. The support is
imprimitive, so a primitive-only descent claim is not refuted by
this observation. It is nevertheless invalid to adopt a universal
one-block sign rule or infer one from the ensemble formulas.

## 13. Fair-law optimization is exactly branch-cost minimization

The parent identified a further important degeneracy. Reversal sends
epsilon to-epsilon, mu to X-mu, and preserves qmax, Nminus, Vminus
and every even coefficient moment. For any reversal-invariant cost
Phi on the finite branch set,

    inf_(joint laws with every sign marginal fair) E Phi
                                      =min_epsilon Phi(epsilon).

The lower inequality is averaging. For the upper inequality, pair
a minimizing branch with its reverse, each with probability1/2.
Every sign marginal is fair and the cost is unchanged. This is exact,
including labeled repeated-block choices. Therefore unrestricted
correlations do not reduce the branch-selection problem at all.
The equality concerns the stronger COST, not an equivalence of
Phi<1 with all three individual stable inequalities.

I read the complete parent `run_and_root_ensemble_2026-10-23.md`
and found no consequential error in its statements, constants,
primitive root completeness or conditional implications. The record
correctly separates the primitive mean-mass pass from joint failure,
and does not claim a new exponent or general selection theorem.

## 14. First next operation, with an explicit kill rule

Do not replace independence by an arbitrary correlated-law wish or
by the refuted single-flip greedy rule. The parent's concrete next
operation retains TWO root blocks and ALL correlation lags. With
the remaining factor C fixed, write

    Q_(sigma,tau)=a+sigma*b+tau*c+sigma*tau*d,
    a=C*A_i*A_j, b=C*B_i*A_j,
    c=C*A_i*B_j, d=C*B_i*B_j.

There is the exact polynomial syzygy a*d=b*c. For
R_uv(h)=sum_k u_k*v_(k+h), the four Walsh coefficients of the
autocorrelation are

    C0=R_aa+R_bb+R_cc+R_dd
               =lambda*delta_(h0)+(1/2)*1_(+/-A)(h),
    Csigma=R_ab+R_ba+R_cd+R_dc=0,
    Ctau=R_ac+R_ca+R_bd+R_db=0,
    Csigmatau=R_ad+R_da+R_bc+R_cb=0.

The vanishing equations and syzygy hold for weighted spectra too.
The extra Boolean equation is LAGWISE

    C0(h)^2=C0(h)/2, h!=0.

Listing these equations is not a new bound. The actual next
derivation is to combine this idempotence with the signed coefficient
weights of a collective cost difference BEFORE summing lags, and
look for a sign-controlled remainder. An unsigned sum only recovers
the old fourth norm; polynomial lag weights recover the known
centroid/cumulant identities. Kill this attempted selection step
if it again reduces to those generic invariants or leaves an
uncontrolled signed cross term. No collective descent, pair-flip
algorithm or universal positive correlation is assumed.

The parent's explicit centered vectors for that next operation also
check. With mu=mu0+sigma*theta+tau*eta and y_k=k-mu0,

    x0=y*a-theta*b-eta*c,
    xsigma=y*b-theta*a-eta*d,
    xtau=y*c-theta*d-eta*a,
    xsigmatau=y*d-theta*c-eta*b.

Expanding (k-mu)q_k gives all four terms exactly. They can be inserted
into the existing full Boolean Gram/missing-lag identity on the fixed
index set0,...,X, allowing zero coefficients, without treating the
moving centroid as independent of the branch. No sign or upper bound
for their mixed Walsh interaction has been established. I inspected
the final parent record and saved rational local-minimum verification;
the four neighbor comparisons use the vertex UPPER endpoint and
neighbor LOWER endpoints, with the correct directions.

## 15. Essential finite-counterexample scope at checkpoint

BOTH ensemble examples have cardinality THREE. Their normalized
ratios M/sqrt(n) exceed3/4; dilation changes the span and branch count
but preserves cardinality and ratio. Thus the exact counterexamples
refute the proposed certificate for ALL actual-lowM supports under
M<=sqrt(n), including its primitive version. They do NOT refute a
growing-cardinality statement, a statement restricted to hypothetical
R tending to zero, or an independently justified finite-exception
preprocessing rule. The same limitation applies to the saved bad
single-flip local minimum. No such repaired asymptotic theorem or
small-ratio mechanism is proved here, so these qualifications are not
a license to enlarge the parameters or to call an untested repair
successful. Do not declare every independent-ensemble approach
impossible on the basis of these finite cases.

This is a concrete proposed calculation within the existing factor
route, not a new complete route or a promise of a theorem. The full
Chowla objective and the independent all-circle construction track
remain open. All computations discussed were the parent's bounded
Dirichlet jobs; this advisor performed only paper work and reads.
