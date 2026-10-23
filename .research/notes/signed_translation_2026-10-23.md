# Bounded translations: a signed factor theorem and its precise selection obstruction

2026-10-23. Continuation after 1f2d803. The full Chowla goal remains
unresolved and is paused at the user's checkpoint request. The lead and sole internal advisor independently
derived the statements below. They are paper proofs, with exact
rational checks of the constants. No Lean/kernel or external novelty
claim. [Full independent audit](advisor_cp_translation_2026-10-23.md).

## 1. Quantified certificate theorem

Let A be ANY nonempty finite set of distinct positive integers,
n=|A|, and f(x)=sum_A cos(ax). Suppose a finite real Laurent
polynomial Q(z)=sum_b q_b z^b satisfies on the ENTIRE circle

    |Q(e^(ix))|^2=lambda+f(x).

Orient its overall sign so that

    S=Q(1)=sqrt(lambda+n)>0, N=sum_b(-q_b)_+.

Then the following assertions hold.

* If every q_b is nonnegative, lambda>sqrt(n/48).
* If N<=S/64, lambda>sqrt(31/4608)*sqrt(n).

These bounds concern the exact certificate floor lambda. When the
factor is taken at lambda=M(A), they bound actual M(A). Real
Fejer--Riesz supplies optimal real factors, but does NOT supply
either coefficient condition. No universal branch selection is
assumed or proved. General complex coefficient factors are outside
the signed positive/negative decomposition used here.

This removes qmax and negative centroid variance from the prior
sufficient signed-factor theorem, while imposing a stricter negative
mass threshold. The two sufficient hypotheses are not ordered.

## 2. Exact signed proof

Write R(d)=sum_b q_b q_(b+d). Boolean matching says R(0)=lambda,
R(d)=1/2 on +/-A, and R(d)=0 at every other nonzero lag.
Strict finite-support Cauchy at any present lag gives lambda>1/2.

For any theta put

    c=Q(e^(i theta))/S,
    X_b=(e^(ib theta)-c)q_b,
    U_d=sum_b X_b q_(b+d),
    E=integral_(probability circle) (lambda+f)|X|^2.

The coefficient sum of X is zero. Parseval and the reversed-lag
identity give

    E=sum_d |U_d|^2,
    U_(-d)=e^(id theta)U_d+c(e^(id theta)-1)R(d),
    E>=D_theta=|c|^2*(n-f(theta))/4.                  (1)

The factor1/4 follows by the parallelogram inequality summed over
ALL signed lags; using R(d)^2=R(d)/2 at the last step is essential.

Let MISSING denote ordered pairs b!=h with |b-h| not in A.
Expanding the Gram integral before discarding them gives

    E=(lambda-1/2)||X||_2^2-T_missing/2,
    T_missing=sum_MISSING X_b conj(X_h).

The terms e^(i(b-h)theta)q_bq_h vanish after summing each missing
lag. The |c|^2 term vanishes as well. Thus exactly

    T_missing=-2Re(conj(c)Z),
    Z=sum_MISSING q_bq_h e^(ib theta).

The total signed weight on missing pairs is zero, so a useful short
bound is

    sum_MISSING |q_bq_h|
      =sum_MISSING (|q_bq_h|-q_bq_h)
      <=sum_(all b,h)(|q_bq_h|-q_bq_h)
       =||q||_1^2-S^2=4N(S+N).

Consequently, for r=|c|,

    D_theta<=E<=(lambda-1/2)(1+r)^2*lambda
                                      +4r*N(S+N).    (2)

There is no bound on degree, span, qmax or signed variance here.

If lambda<=n/3, the normalized circle mean of |Q|^2/S^2 is
lambda/(lambda+n)<=1/4, while its value at zero is1. Continuity
therefore gives theta with r=1/2. At an optimal factor, a zero at
a global minimum gives the same crossing directly. At this theta,

    D_theta=3S^2/64,
    3S^2/64 <=(9/4)lambda(lambda-1/2)+2N(S+N).       (3)

For N=0 this gives S^2<=48lambda(lambda-1/2), so n<48lambda^2.
For N<=S/64, subtract 2*(65/4096)S^2 in (3):

    (31/2048)S^2 <=(9/4)lambda(lambda-1/2),
    lambda^2>(31/4608)n.

If lambda>n/3, both asserted certificate floors already follow from
lambda>sqrt(n)/3, for n>=1. This completes the all-certificate scope.

## 3. The universal small-mass branch assertion is false

The theorem is valid. The stronger assertion

    M(A)<=sqrt(n) implies SOME optimal real factor has N/S<=1/64

is REFUTED by a primitive infinite family. This is not a refutation
of a branch assertion restricted to hypothetical M/sqrt(n) tending
to zero or to a sufficiently small fixed ratio.

For even k, let

    B(k)={2*9^i+epsilon_i: 1<=i<=k},
    epsilon_i=0 for i<=k/2, and 1 thereafter.

All positive differences are distinct: equality of two perturbed
differences has a power-difference part divisible by16 and an
epsilon error of absolute value at most2. Both vanish; 9-adic
valuation then identifies the pair. Exactly half of B(k) is odd,
so F_B(pi)=0. The difference square proves its cosine minimum
is exactly -k/2 on the entire circle.

For ANY even m>=2000 take

    A0=diff_+(B(2m)), A1=diff_+(B(m)), D0=max A0,
    L=2D0+1, A=A0 union L*A1.

The two positive supports are disjoint; L is odd. The square lower
bounds and their common equality at pi give EXACTLY

    n0=2m^2-m, n1=(m^2-m)/2,
    n=(5m^2-3m)/2, M=3m/2<=sqrt(n),
    S^2=n+M=5m^2/2, M/sqrt(n) -> 3/sqrt(10).

The support is primitive: A0 contains144 and16*9^m+1, coprime
integers. Gcd normalization therefore does not remove this example.

Let Q be ANY real optimal factor and set u=q_+, v=q_-,
Pplus=sum u=S+N, mu_b=u_b/Pplus. Color pairs of integers LOW
when their absolute difference lies in A0, HIGH when it lies in
L*A1, and MISSING otherwise, including equal pairs. No triangle
has both colors: two low steps cannot reach a nonzero multiple of
L, while a difference of two high steps cannot be a low step.

For independent mu-distributed vertices let ell,h,epsilon be their
low, high and missing probabilities. Exact signed correlations imply

    ell>=(n0-N^2)/Pplus^2,
    h>=(n1-N^2)/Pplus^2,
    epsilon<=M/Pplus^2+2N/Pplus.                      (4)

The first two estimates subtract at most the entire off-diagonal
v-v mass N^2. For the last, sum u^2<=M, and at missing lags
R_u<=R_uv+R_vu; their total ordered cross mass is2Pplus*N.

Here is the full weighted graph argument. Write l(x),h(x),e(x)
for conditional degrees, and E for expectation under mu. The lack
of mixed triangles gives E[l h]<=epsilon. Symmetry, the binary
low kernel, and Jensen on differences of two rows give

    2(E l^2-ell^2)<=2ell-2E l^2,
    E l^2<=(ell+ell^2)/2.

Since h=1-l-e, it follows that

    E[l h]>=ell(1-ell)/2-epsilon,
    ell*h<=ell(1-ell)<=4epsilon.                     (5)

If N<=S/64, (4) yields

    epsilon<=3/(5m)+2/65,
    ell*h >= [(n0/S^2-1/4096)*(n1/S^2-1/4096)]
                                                     /(65/64)^4.

For m>=2000, the two numerator factors exceed3/4 and3/16,
respectively, and (65/64)^4<9/8. Thus ell*h>1/8, whereas
4epsilon<=12/(5m)+8/65<1/8, contradicting (5). EVERY optimal
real factor therefore has N/S>1/64. No finite root enumeration,
sampled minimum, or unproved asymptotic equidistribution is used.

## 4. Three colors refute even the older mass budget of one eighth

The following finite theorem is independent of any external
construction. Suppose A partitions into three blocks A_i of equal
cardinality t, no triangle in its colored Cayley graph uses more
than one color, and t>=85lambda for a real exact factor of
lambda+f_A. Then EVERY such factor has N/S>1/8.

Suppose instead N<=S/8 and use the positive-part probability mu
from Section3. Let ell_i be its three edge probabilities and
e=sum ell_i. The same ordered-correlation bounds give

    ell_i >= [t/S^2-1/64]/(81/64),
    1-e <= lambda/S^2+2/9.

Since S^2=3t+lambda, the premise gives t/S^2>=85/256 and
lambda/S^2<=1/256. Hence each ell_i>=1/4 and

    e>=7/9-1/256=1783/2304>3/4.                      (6)

For the union edge kernel let d(x) be the conditional degree.
Common neighbors of any edge xy have probability at least
d(x)+d(y)-1. The ordered triangle probability T therefore obeys

    T>=2E d^2-e>=e(2e-1).

For each color let M_i be its symmetric adjacency matrix weighted
on both sides by diag(sqrt(mu)). Then Tr(M_i^2)=ell_i and
its triangle probability is Tr(M_i^3)<=ell_i^(3/2), by the spectral
theorem and the l3/l2 inequality. This does not require positive
semidefinite adjacency. All triangles are monochromatic, so

    e(2e-1)<=T<=sum_i ell_i^(3/2)<=e*sqrt(max_i ell_i).

Divide by e>3/4 and square. The other two colors each have mass
at least1/4, so

    (2e-1)^2<=max_i ell_i<=e-1/2.

This contradicts (2e-1)^2-(e-1/2)=(4e-3)(e-1/2)>0.
The finite three-color theorem follows.

For a growing actual-low-M realization, use the cited
[Bu et al. v1 Theorem1.3](https://arxiv.org/html/2610.17160v1).
The versioned primary statement and infimum definition were reopened
and checked by lead and advisor. Its upper bound, with the strict
margin11/20>1/2, supplies sets U of every sufficiently large
cardinality t with M(U)<=11sqrt(t)/20. No attainment of the infimum
is required. The full external construction proof is a cited
dependency, not a new complete proof audit here.

Set D=max U, L=2D+1 and A=U union L*U union L^2*U. The
blocks are disjoint and no triangle has mixed colors: a unique
highest-scale edge is too large to be the sum of two lower ones;
the difference of two highest-scale edges is a multiple of that
scale and cannot be a nonzero lower edge. On the entire circle,

    n=3t, M(A)<=3M(U)<=33sqrt(t)/20<sqrt(3t).

For t>=20000 as well as sufficiently large for the cited bound,
t>=85M(A), since20000>(561/4)^2. The finite theorem proves
N/S>1/8 for EVERY optimal real factor. Gcd normalization preserves
all premises and the minimum, so primitive examples exist.

This refutes the OLD universal three-budget stable-factor existence
claim under M<=sqrt(n), already through its N/S<=1/8 requirement.
The new signed sufficient theorem remains true. There is no claim
of a vanishing normalized ratio or of a refutation of a branch
assertion restricted to hypothetical much smaller R. Only the known
upper limsup sqrt(3)/2 follows from this construction-side input;
no exact asymptotic ratio is proved here.

## 5. Multiple positive factors: retained quantitative object

The complete cross-component translation quantity D from the prior
checkpoint remains open as a universal CP route. The advisor derived
and the lead checked

    D_theta=(lambda-1/2)*sum_i lambda_i*x_i/2
                      +P(theta)/4-||A_c||_2^2/2,
    x_i=|Q_i(e^(i theta))/S_i|^2,
    A_c(x)=sum_i conj(c_i)Q_i(e^(i(x+theta)))conj(Q_i(e^(ix))),
    D_theta>=(1/4)sum_i S_i^2*x_i*(1-x_i).

For an AVAILABLE decomposition with at most r nonzero nonnegative
factors this proves lambda>sqrt(3/(512r))*sqrt(n). It does not
bound the required CP rank or supply a CP representation at a cheap
floor for arbitrary A. Artificial splitting weakens this corollary.

The stronger candidate

    D_theta>=P(theta)*(P(0)-P(theta))/(4P(0))

is unproved. It is equivalent to bounding ||A_c||^2 by
(lambda-1/2)sum lambda_i*x_i+P(theta)^2/(2P(0)). Ordinary Cauchy
has the larger term sum S_i^2*x_i^2/2, so it does not prove this.
Full component interactions do rescue the exact separated flat
Sidon calculation: D=T(K-T)/8, where K=sum k_i and
T=sum k_i*x_i, giving sup D=K^2/32. This is a paper mechanism
check on a settled class, not a new construction or a control scan.

## 6. Verification and global decision

[Exact constant checker](../../src/signed_translation_checks.py)
ran on Dirichlet with 2 cores / 4 GB / 45 seconds cap.
The first run stopped on a structural SymPy equality comparison;
expanding the difference repaired the check without changing any
mathematical formula. The terminal rerun passed in about0.159 seconds
compute. [Saved exact output](../experiments/signed_translation_2026-10-23/constants.json)
checks31/4608, all count formulas and the m=2000 rational margins;
the two-color contradiction gap is47/65000. Monotonicity of the
1/m terms extends those endpoint bounds to every m>=2000.
The all-circle minima and all-factor assertion have the separate
paper proofs above and the independent advisor audit. The checker
was extended and rerun for the already-derived three-color upgrade:
it passed in0.155 seconds, checking color probability1/4, edge
margin55/2304 above3/4, triangle gap34705/1327104, and the
finite construction-side threshold20000. It does not compute the
external theorem's asymptotic threshold.

GLOBAL REVIEW: the prior qmax/variance route was strengthened to
a one-budget sufficient theorem. A newly derived growing primitive
Boolean family then killed its unqualified low-M branch-selection
claim. Retain the theorem and the missing-lag error identity, but
do not promise universal N/S<=1/64 as the next lemma or enlarge
root/branch scans. The three-color upgrade also refutes the OLD
universal N/S<=1/8 three-budget existence target. A much smaller-R
conditional selection is neither
proved nor refuted here; the new example has R tending3/sqrt(10).

The changed remaining finite target is the full MULTI-component
coherence inequality above. The next derivation should keep its
exterior-square term and use the exact Boolean lag allocation;
contracting it to generic Cauchy is already audited as insufficient.
No numerical pilot is justified by the identities alone. Preserve
the distinct unrestricted signed Rayleigh and genuine growing
all-circle construction lines. No new GPU, VM lifecycle operation,
extra agent, manuscript or outreach occurred. Dirichlet remains
shared/running; cumulative RunPod cost is still $0.10.

At the user's request, this is the natural checkpoint. Research is
paused after organizing these results; no further experiment or
derivation is scheduled. The unresolved multi-component inequality
is a deferred next step requiring new user instructions to resume.
