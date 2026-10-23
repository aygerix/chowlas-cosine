# Translation completion: a single-factor root bound and the signed-mass extension

2026-10-23. Sole internal AI advisor. Paper derivations and read-only
record review. No computation, VM/GPU action, additional agent or
outreach. Shared Dirichlet is untouched. Full Chowla remains open.
The parent independently checked the consequential inequalities.
No Lean/kernel, external scrutiny or novelty-priority claim.

## 1. Fixed exact target and the CP quantity under examination

Let A be any nonempty finite set of DISTINCT POSITIVE INTEGERS,
n=|A|, f(x)=sum_A cos(ax), M=-min_(all real x)f(x). For a finite
nonnegative certificate write

    P(x)=lambda+f(x)=sum_i |Q_i(exp(ix))|^2,
    Q_i(z)=sum_b q_(i,b)z^b, q_(i,b)>=0,
    S_i=sum_b q_(i,b)>0, lambda_i=sum_b q_(i,b)^2.

All factors have finite integer support; individual monomial shifts
do not affect the certificate. Drop zero components. Then

    P0=lambda+n=sum_i S_i^2,
    sum_i lambda_i=lambda,
    sum_i R_ii(d)=(1/2)1_(+/-A)(d), d!=0,
    R_ji(d)=sum_b q_(j,b)q_(i,b+d).

Put

    c_i(theta)=Q_i(exp(i theta))/S_i,
    X_i(z)=Q_i(exp(i theta)z)-c_i Q_i(z),
    U_ij(d)=sum_b X_(i,b)q_(j,b+d),
    D_theta=(1/4)sum_(i,j,d in Z)
                    |exp(i d theta)c_j-c_i|^2 R_ji(d)^2.   (1)

The previous note proves the exact completion

    (lambda-1/2)sum_i||X_i||_2^2
       =D_theta+(1/4)sum_(i,j,d)
               |U_ij(-d)+exp(i d theta)U_ji(d)|^2.          (2)

Every missing lag vanishes in every component, because the q are
nonnegative. Thus every support is an A-difference clique. Since
|c_i|<=1, (2) gives D_theta<=4lambda(lambda-1/2).

Candidate under audit: does sup_theta D_theta>=c*n hold for an
absolute c>0 on EVERY such Boolean CP certificate with
lambda<=sqrt(n)? It would prove the existing CP-Chowla target.
It would not supply a cheap CP certificate for arbitrary A, so it
does not by itself resolve unrestricted Chowla.

## 2. Origins and component splitting do not change D

Shift component i by z^(h_i). Then

    c_i -> exp(i h_i theta)c_i,
    R_ji(d) -> R_ji(d+h_j-h_i).

After changing the summation lag, the phase factor in(1) acquires
only a unit scalar. Hence D is invariant under permissible individual
origins. Optimizing those origins cannot improve this candidate.

Replacing one Q by R copies Q/sqrt(R) also leaves the FULL sum(1)
unchanged. It does not leave a diagonal-only sum over i unchanged.
All cross components and signed lags in(1) are necessary.

## 3. Exact simplification for ONE nonnegative factor

For P=|Q|^2 with q_b>=0,

    S=Q(1)=sqrt(lambda+n),
    r(d)=(1/2)1_(+/-A)(d) for d!=0,
    |c(theta)|^2=P(theta)/S^2.

The d=0 term of(1) is0, and the two signed copies of A give

    D_theta=|c|^2*(n-f(theta))/4
            =(lambda+n)*x(theta)*(1-x(theta))/4,
    x(theta)=P(theta)/(lambda+n).                           (3)

If lambda<=n, then x(0)=1 and mean x=lambda/(lambda+n)<=1/2.
Continuity gives a point with x=1/2, so

    sup_theta D_theta=(lambda+n)/16.                       (4)

Thus the uncontracted quantity has a macroscopic exact value for
every SINGLE nonnegative factor. This does not need a Sidon
support, bounded multiplicity, bounded qmax, bounded span, or
optimality of the certificate.

For a clean stronger floor, take |c|=1/2. If lambda<=n/3,
the mean of x is<=1/4 and continuity again supplies this value.
At that point,

    D_theta=3(lambda+n)/64,
    ||Q(shift)-cQ||_2^2<=(1+|c|)^2lambda=9lambda/4.

Use(2) to obtain

    lambda+n<=48lambda(lambda-1/2),
    lambda>sqrt(n/48).                                     (5)

If lambda>n/3, then lambda>sqrt(n)/3>=sqrt(n/48), so (5)
holds in that case too. Therefore:

PROVED, paper: for EVERY finite Boolean A, any exact SINGLE
nonnegative real factor lambda+f_A=|Q|^2 has

    lambda>sqrt(|A|)/(4sqrt3).                              (6)

Only when lambda=M(A) does this become a lower bound on actual M.
It is a certificate-class floor otherwise. No assertion that every
optimal factor is nonnegative is made.

The preceding P8 weighted-multiplicity theorem was inspected. It
requires a multiplicity factor and does not dominate (6) when that
factor is unbounded. The earlier weighted centroid needed qmax;
(6) avoids that hypothesis. This is a project-level comparison, not
a primary-literature novelty claim.

## 4. Exact adversary checks: flat Sidon and separated Boolean unions

For a k-point Sidon difference support with Q=F_B/sqrt2,
lambda=k/2, n=k(k-1)/2, set x=|F_B(exp(i theta))|^2/k^2.
Formula(3) gives

    D_theta=k^2*x*(1-x)/8,
    sup D_theta=k^2/32.                                    (7)

The crossing follows from x(0)=1 and mean x=1/k. No assumption
of a zero of F_B is needed for this test.

A separated Boolean union does not furnish an immediate counter.
Suppose each component is flat Q_i=F_(B_i)/sqrt2 with k_i>=2,
each B_i is Sidon, the positive within-component difference supports
are disjoint, and each cross difference between B_i and B_j has a
unique representation. Sufficiently separated dilations provide
these precise hypotheses. Put

    x_i=|F_(B_i)(exp(i theta))|^2/k_i^2,
    K=sum_i k_i, T(theta)=sum_i k_i*x_i.

Each off-diagonal R_ji coefficient is then a single product1/2.
Direct summation of all ordered component pairs gives

    D_theta=T(theta)*(K-T(theta))/8.                        (8)

For example the i,j cross contribution is
(k_i*k_j/8)*(x_i+x_j-2x_i*x_j) for i<j; its phases cancel in
the pair sum, rather than being assumed independent. Since
T(0)=K, mean T=number of components<=K/2, and0<=T<=K,

    sup D_theta=K^2/32.                                    (9)

Cross terms can therefore remain large even if individual transition
windows do not overlap. Deleting them would miss exactly this effect.
This check is not a new root theorem for a settled family and not a
counterexample construction. An AP flat single factor is not Boolean;
ordinary large AP Boolean supports have M of linear order and fall
outside the proposed lambda<=sqrt(n) regime. No new finite controls
or scans were run.

## 5. Exact general reduction, and what ordinary Cauchy actually proves

Write x_i=|c_i|^2, and define

    A_c(x)=sum_i conj(c_i)Q_i(exp(i(x+theta)))
                                      *conj(Q_i(exp(ix))),
    V_c=sum_i lambda_i*x_i.

Parseval on the matrix entries in(1), with all signed lags, gives

    D_theta=(lambda-1/2)*V_c/2+P(theta)/4-||A_c||_2^2/2.     (10)

Indeed the two squared terms in the expansion have equal integrals,
while their cross inner product is ||A_c||^2. The clique identity
evaluates their remaining integrals exactly.

Pointwise Cauchy yields

    ||A_c||_2^2
       <=sum_i x_i*((lambda-1/2)lambda_i+S_i^2*x_i/2),

and therefore the valid lower bound

    D_theta>=(1/4)sum_i S_i^2*x_i*(1-x_i).                  (11)

It is useful if a macroscopic evaluation mass S_i^2 has a genuine
transition. It does NOT show that such mass is universal. The
stronger proposed rank-one bound

    D_theta>=P(theta)*(P0-P(theta))/(4P0)                   (12)

would replace sum S_i^2*x_i^2 in Cauchy by P(theta)^2/P0.
That is a different, stronger inequality; ordinary Cauchy gives the
opposite ordering of these two expressions. Equivalently, (12)
requires

    ||A_c||^2<=(lambda-1/2)*V_c+P(theta)^2/(2P0).            (13)

A wedge term/evaluation bound filling this variance gap is unproved.
No Boolean counterexample to (12) or to the original c*n candidate
has been derived here. No claim is based on absence of one.

A limited consequence of(11) is worth separating from that open
target. If an available certificate has at most r nonzero components,
then

    lambda>sqrt(3/(512*r))*sqrt(n).                        (5C)

Indeed, if lambda<=n/6, the components with S_i^2>=4lambda_i
carry total S_i^2 mass at least n-3lambda>=n/2. One has
S_i^2>=n/(2r) and crosses x_i=1/4 by its mean lambda_i/S_i^2.
Equation(11) gives D>=3n/(128r), whereas D<4lambda^2.
If lambda>n/6 the stated weaker floor is automatic for n,r>=1.
This is a certificate-rank conditional bound, not a bound on the
number of components needed for arbitrary A. Artificial splitting
weakens it; use a minimal/merged decomposition when applying it.

## 6. Primary positive extension: small SIGNED coefficient mass suffices

The parent proposed this extension, independently derived and checked
here. Now Q is any REAL finite exact factor, with signs allowed:

    |Q|^2=lambda+f_A, Q(1)=S=sqrt(lambda+n)>0,
    N=sum_b(-q_b)_+, Pplus=sum_b(q_b)_+=S+N.

For any theta let c=Q(exp(i theta))/S and
X_b=(exp(i b theta)-c)q_b, so sum X_b=0. The pair completion
for ONE factor still has the Boolean term

    D_theta=|c|^2*(n-f_A(theta))/4.                         (14)

The Gram identity now retains the missing-pair term:

    E=integral (lambda+f_A)|X|^2
       =(lambda-1/2)||X||_2^2-T_missing/2,
    T_missing=sum_(ordered b!=h, |b-h| notin A)
                                  X_b*conj(X_h).          (15)

Every missing lag has signed correlation0. Expanding X in(15)
therefore kills BOTH the exp(i(b-h)theta) and |c|^2 terms. Thus

    T_missing=-2Re(conj(c)*Z),
    Z=sum_(ordered missing pairs)q_b*q_h*exp(i b theta).    (16)

The total signed weight over missing pairs is0. All negative ordered
pair weight, whether missing or not, has magnitude2Pplus*N. Hence
the missing negative weight is at most that amount; its positive
weight equals its negative weight. Consequently

    |Z|<=sum_missing |q_b*q_h|<=4Pplus*N.                   (17)

This ordered-pair factor4 is essential. Equations(15)-(17), the
triangle bound ||X||<=(1+|c|)sqrt(lambda), and D<=E give

    D_theta <=(lambda-1/2)(1+|c|)^2lambda
                                  +4|c|Pplus*N.          (18)

The coefficient lambda-1/2 is positive: a nonnegative continuous
polynomial with the nonzero Fourier coefficient1/2 has mean at
least1/2, and equality would force its positive mass onto a finite
phase level, impossible for a nonzero continuous polynomial.

At an OPTIMAL factor lambda=M(A), the all-circle minimum gives
|Q|=0 somewhere and |c(0)|=1, so continuity supplies |c|=1/2
without a density/cardinality assumption. Then(14),(18) become

    3S^2/64 <=(9/4)lambda(lambda-1/2)+2Pplus*N.             (19)

If N<=S/64, then Pplus*N<=(65/4096)S^2. Subtraction gives

    (31/2048)S^2 <=(9/4)lambda(lambda-1/2),
    lambda^2> (31/4608)*n.                                 (20)

Thus the primary result is:

PROVED, paper, parent plus independent advisor audit: for EVERY
nonempty finite Boolean A, IF an optimal real factor of M(A)+f_A
can be oriented so that N/Q(1)<=1/64, THEN

    M(A)>sqrt(31/4608)*sqrt(|A|).                           (21)

No bound on its maximum coefficient, negative centroid variance,
degree, frequency density or root-selection algorithm is required.
No existence of such a branch for every A is proved.

More generally, if N<=eta*S and
1/48-(8/9)eta(1+eta)>0, the same proof gives the certificate floor

    lambda^2>[1/48-(8/9)eta(1+eta)]*n.

This records the parameter dependence of the proof, not a search
for optimized constants.

## 7. Certificate-floor scope versus actual M

The certificate floor in(20) also holds for NONOPTIMAL real exact
factors with N<=S/64. If lambda<=n/3, continuity and the mean
|Q|^2/S^2=lambda/(lambda+n)<=1/4 again give |c|=1/2. If
lambda>n/3, its asserted root floor is already weaker than
lambda>sqrt(n)/3. Only at lambda=M does that certificate floor
become the actual-M conclusion(21).

When N=0 the same argument gives the single-nonnegative result(6).
The earlier weighted-centroid argument needed qmax and the signed
centroid theorem additionally controlled negative variance. This
translation proof removes both conditions while requiring a smaller
negative-mass ratio. These are different sufficient hypotheses;
neither theorem establishes universal branch selection. Arbitrary
complex factors are not covered by the real positive/negative
coefficient decomposition.

## 8. Decision and remaining exact issue

The audit yielded an actual positive mathematical result, rather than
only a new reformulation: (6) for all single nonnegative factors and
(21) for optimal real factors with a small signed mass budget. The
proof keeps the exact Boolean missing-lag zero sums in(16); applying
Booleanity separately to nonflat CP components would be invalid.

The universal multi-component c*n estimate remains open. Formula(10)
is exact; (11) is proved; (12)-(13) are not. The next object must
control the full cross-component variance/coherence through exact
Boolean lag incidences, or establish a usable signed-mass branch.
A generic PSD/Cauchy contraction does neither. No successful-control
sweep, origin optimization, new GPU or numerical pilot follows from
the formula alone. The parent registered the signed translation
mechanism in ROUTES before any genuinely different work.

## 9. Growing Boolean falsifier of UNIVERSAL small-negative-mass selection

The parent then proposed the following exact adversary; I independently
checked its construction, weighted graph argument, ordered-pair
normalizations and rational margins. It preserves theorem(21) but
REFUTES the assertion that every actual-low-M A has a branch with
N/S<=1/64.

Take even m>=2000. Construct balanced-parity power9 Sidon sets B0
and B1 of sizes2m and m as in the preceding satellite proof. In each
set use first half epsilon=0, second half epsilon=1 in
b_i=2*9^i+epsilon_i. Let

    A0=diff_+(B0), A1=diff_+(B1), D0=max A0,
    L odd, L>2D0, A=A0 union L*A1.

The supports are disjoint, and both square minima occur at pi, since
both parity assignments are balanced and L is odd. Therefore

    n0=2m^2-m, n1=(m^2-m)/2,
    n=(5m^2-3m)/2,
    lambda=M(A)=3m/2<=sqrt(n),
    S^2=lambda+n=5m^2/2.                                 (22)

The actual ratio tends3/sqrt10, not0. The construction can be
primitive: A0 contains144 and16*9^m+1, which are coprime.
Thus gcd normalization does not remove the obstruction.

Color an edge on Z LOW if its absolute difference belongs to A0,
HIGH if it belongs to L*A1, and MISSING otherwise, including loops.
There is no mixed-color triangle. Two low edges have total magnitude
at most2D0<L and cannot close with a high edge; two high differences
are multiples of L and cannot close with a nonzero low edge.

Consider ANY real optimal factor q of lambda+f_A, oriented with sum
S>0. Put u=q_+, v=q_-, N=sum v, Pplus=sum u=S+N, and let
mu_b=u_b/Pplus be its coefficient probability law. Write

    ell=Pr_(X,Y~mu)(XY is LOW),
    h=Pr_(X,Y~mu)(XY is HIGH),
    epsilon=1-ell-h.

From R_q=R_u+R_v-R_uv-R_vu and the exact Boolean off-lag
coefficients,

    ell>=(n0-N^2)/Pplus^2,
    h>=(n1-N^2)/Pplus^2,
    epsilon<=lambda/Pplus^2+2N/Pplus.                      (23)

For the last estimate the diagonal contribution sum u_b^2 is at
most lambda. At each nonzero missing lag, R_u<=R_uv+R_vu;
the total ordered cross mass is2Pplus*N. There is no hidden
replacement of a signed correlation by its absolute value.

Here is the weighted graph inequality needed for(23). Let l(x),
h(x),e(x) be the conditional low/high/missing degrees. No mixed
triangle gives

    E[l(X)h(X)]<=epsilon.

For ANY symmetric0/1 low kernel, Jensen on row differences gives

    2(E l^2-ell^2)
      <=E_(X,Y,Z)(L(X,Z)-L(Y,Z))^2
       =2ell-2E l^2,
    E l^2<=(ell+ell^2)/2.                                 (24)

Since h=1-l-e and l<=1,

    E[l h]>=ell(1-ell)/2-epsilon.

Combining gives ell(1-ell)<=4epsilon, and h<=1-ell yields

    ell*h<=4epsilon.                                     (25)

Suppose N<=S/64. Equations(22)-(23) imply

    epsilon<=3/(5m)+2/65,
    ell*h >= [(n0/S^2-1/4096)*(n1/S^2-1/4096)]
                                                   /(65/64)^4.

For m>=2000 the first numerator factor is>3/4, the second
is>3/16, and (65/64)^4<9/8. Consequently ell*h>1/8.
But

    4epsilon<=12/(5m)+8/65<1/8,

because 1/8-8/65=1/520 and m>=2000>1248. This contradicts(25).

Thus EVERY real optimal factor of this explicit growing primitive
actual-low-M Boolean family has N/S>1/64. No branch enumeration,
root approximation or sampled minimum is involved. The universal
mass-only selection claim is retired. This is not a falsifier of a
selection assertion restricted to hypothetical much smaller R, nor
of theorem(21), CP-Chowla, or unrestricted Chowla.

## 10. Scope review before the three-color strengthening

The positive results are (6), (21), and the finite-rank corollary(5C).
They are conditional certificate-class statements with no frequency
bound. Universal low-M signed-mass selection is now refuted by(22),
so it must not be the handoff's promised missing lemma.

The full multi-component D target, exact formulas(10)-(11), and its
unproved coherence improvement(12)-(13) remain separate. A new
argument must use quantitative Boolean lag allocation rather than
asserting that every scalar branch has small negative mass. The
growing graph obstruction itself is useful finite Boolean information;
it does not prove that all phase-selection methods fail.

Read-only computational audit: I inspected src/signed_translation_checks.py
and experiments/signed_translation_2026-10-23/constants.json after the
parent's Dirichlet run. The script uses exact Fraction/SymPy arithmetic
for the n,M,S identities and rational endpoint inequalities above.
It reports EXACT_CONSTANTS_PASS, including margin31/2048, coefficient
31/4608, and contradiction gap47/65000 at m=2000. It does not
enumerate the large supports, isolate spectral roots, or certify a
sampled minimum; the all-circle statements and weighted graph lemma
are the paper arguments. I did not rerun the script or claim an
independent arithmetic backend. No mathematical assertion depends
on the earlier structural-SymPy-comparison code correction.

## 11. Three colors refute the OLD universal1/8 mass budget

The following strengthening was proposed by this advisor and checked
independently by the parent. It supersedes the remaining universal
mass-selection suggestion above, not the proved sufficient theorem.

FINITE THEOREM. Suppose a Boolean A has a partition into three classes
A1,A2,A3 of the SAME cardinality t, and no triangle of its Cayley
graph has edges from more than one class. Let

    lambda+f_A=|Q|^2

be any real finite exact factor and suppose t>=85lambda. Orient
S=Q(1)=sqrt(lambda+3t)>0. Then

    sum_b(-q_b)_+ > S/8.                                  (26)

This is a certificate-floor obstruction at arbitrary lambda, not
only at actual optimality.

Proof. Suppose N<=S/8. Use the positive-part probability mu as
in Section9, and let ell_i be the three color probabilities. Put
e=sum_i ell_i=1-epsilon. With alpha=t/S^2 the same ordered
correlation calculation gives

    ell_i >=(alpha-1/64)/(81/64),
    epsilon<=lambda/S^2+2/9.                              (27)

The finite premise t>=85lambda gives alpha>=85/256 and
lambda/S^2<=1/256. Hence

    ell_i>=1/4 for i=1,2,3,
    e>=7/9-1/256>3/4.                                    (28)

All loops remain missing; no diagonal probability is dropped.

We need two elementary weighted-graph triangle estimates, proved
here rather than assumed from a named theorem. For the union edge
kernel W, let d(x)=E_y W(x,y), with mean e. For an edge xy,
its common-neighbor probability is at least d(x)+d(y)-1. Thus
the ordered triangle probability tau satisfies

    tau>=2E d(X)^2-e>=e(2e-1).                            (29)

For color i form the finite real symmetric matrix

    M_i=diag(sqrt(mu))*W_i*diag(sqrt(mu)).

Its squared Hilbert-Schmidt norm is ell_i, while its cubic trace
is the color triangle probability tau_i. By the spectral theorem,

    tau_i=Tr(M_i^3)<=sum_j |eig_j(M_i)|^3
                         <=(sum_j eig_j(M_i)^2)^(3/2)
                         =ell_i^(3/2).                    (30)

This does not assume the adjacency matrix is positive semidefinite.
No mixed triangles implies tau=sum_i tau_i. Therefore

    e(2e-1)<=tau<=sum_i ell_i^(3/2)
                         <=e*sqrt(max_i ell_i).

Since e>3/4, division and squaring are legitimate. Each of the two
other colors has probability at least1/4, so

    (2e-1)^2<=max_i ell_i<=e-1/2.

But

    (2e-1)^2-(e-1/2)=(4e-3)*(e-1/2)>0,

contradicting(28). This proves(26).

## 12. Growing primitive actual-low-M realization of the three-color premise

Use the existing construction-side theorem of
[Bu et al., arXiv2610.17160v1, Theorem1.3](https://arxiv.org/html/2610.17160v1).
It gives the half-constant asymptotic upper bound for the infimum at
each cardinality. Since11/20>1/2, for every sufficiently large t
one may choose a genuine Boolean set U of size t with

    M(U)<=11sqrt(t)/20.                                   (31)

The strict margin also justifies choosing a set from the infimum;
no unproved attainment of that infimum is needed. This source was
reopened during this audit: its definition of the infimum and the
statement of Theorem1.3 were inspected. The full construction proof
is a cited dependency previously examined by the project, not a new
complete proof audit in this turn. The finite graph theorem(26)
does not depend on that external existence theorem.

Let D=max U, L=2D+1, and set

    A=U union L*U union L^2*U.                            (32)

These are disjoint positive-frequency classes. There is no mixed
triangle. In a purported triangle, a unique edge of largest scale
exceeds the sum of the other two since L>2D; if exactly two edges
have the largest scale, their signed difference is a multiple of
that scale, whereas a nonzero lower-scale edge is smaller than it.
Both alternatives are impossible. No common minimizing angle is
needed for the all-circle bound

    n=3t, lambda=M(A)<=3M(U)<=33sqrt(t)/20<sqrt(3t).        (33)

Choose t>=20000 as well as sufficiently large for(31). Since
20000>(561/4)^2, one has

    t>=85*(33sqrt(t)/20)>=85lambda.

The finite theorem applies to EVERY real optimal factor of this A:

    N/Q(1)>1/8.                                          (34)

Dividing all frequencies by their common gcd preserves cardinality,
M, the color partition and the absence of mixed triangles. Thus
the infinite family may be made primitive. There are no zero,
negative, repeated or weighted output frequencies, and(33) is a
global-in-angle statement inherited from(31), not a grid test.

Taking successively smaller fixed margins above the source's1/2
constant shows that the construction can have
limsup M(A)/sqrt(|A|)<=sqrt3/2. No EXACT asymptotic ratio or
vanishing ratio is proved here. It is a counterfamily to a universal
intermediate, not to Chowla and not a better construction-side record.

## 13. Final global decision after the growing three-color obstruction

The OLD proposed universal stable branch simultaneously required
bounded qmax, N/S<=1/8, and negative centroid variance<=1/8.
Equation(34) refutes that existential three-budget assertion on
growing primitive actual-low-M Boolean inputs: its MASS requirement
already fails for every real optimal branch. This is stronger than
the two-Sidon1/64 obstruction, and is not an inference from a finite
branch scan or a small-cardinality exception.

It does not refute a branch-selection statement restricted to a
hypothetical much smaller or vanishing normalized M, and it does
not invalidate the signed sufficient theorem(21). Do not silently
replace the old unconditional target by such a restriction without
stating new quantifiers and a new mechanism.

Preserve the positive single-factor root theorem(6), signed-mass
certificate floor(20), and finite-rank CP corollary(5C). Universal
multi-component CP translation lower bounds remain unproved. A
future argument must use full finite Boolean allocation or an actual
changed construction; it cannot promise universal low negative mass,
discard cross components, optimize their origins, or revive the
completed continuum-profile relaxation as an unrestricted proof.
No further computation was required for this strengthening.
