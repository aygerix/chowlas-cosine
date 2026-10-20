# Chowla / C*: research checkpoint

**20 October 2026, 06:01 UTC. Research remains active.**

This note separates proved reductions, exact counterexamples to particular shortcuts, a positive theorem for a specified random model, and numerical evidence on deterministic supports. None establishes the universal Chowla bound. The main unresolved issue is how the exact geometry of an arbitrary Boolean integer spectrum forces a sufficiently negative quadratic form, without an independence hypothesis or an unjustified relaxation of its coefficients.

## 1. Normalization and the precise target

For a finite nonempty set A of distinct positive integers, write

    f_A(x) = sum_{a in A} cos(2πax),    M(A) = -min_x f_A(x).

Chowla's square-root assertion asks for an absolute c>0 such that M(A)≥c√|A| for every A. Put S=A∪(-A), N=|S|=2|A|, and

    D(x) = sum_{s in S} exp(2πisx) = 2f_A(x),    K = -min D = 2M(A).

For a finite row set W, let B_W have entries 1_S(u-v), and put K_W=-λ_min(B_W). Every vector on W is a trigonometric test, so K≥K_W. The two-neighborhood target uses

    W1 = {0} ∪ S,    W2 = {0} ∪ S ∪ (S+S).

A universal K_W2≥c√N would therefore imply Chowla, but is a stronger assertion. An exact counterexample to one proposed constant is not a counterexample to the existence of some positive constant. In particular, the sharp local inequality K_W2≥√(N/2) has now been refuted, while the any-positive-constant assertion remains open.

## 2. Hypothetical counterexamples can be selected as exact record extremizers

Define κ(n)=inf_{|A|=n}M(A). **This infimum is attained for every n.** The proof uses compactness of closed subgroups of the torus rather than a bound on the largest frequency.

For an ordered frequency vector a, its circle H_a⊂T^n carries the function F(x)=Σ cos(2πx_j). A minimizing sequence of circles has a Hausdorff-convergent subsequence, with limit a compact connected subgroup H. The minimum of F varies continuously under that convergence. Each coordinate character, and each difference or sum of two coordinate characters, remains nontrivial on H: a nontrivial character of a connected subgroup has image all of T, which prevents its collapse to zero in the limit.

The integral cocharacter lattice of H consequently contains a vector w with nonzero coordinates, distinct up to sign. Its circle lies inside H. Restricting the minimizing domain can only decrease the negative minimum, so the n-element positive set {|w_j|} attains κ(n). This supplies no effective diameter bound.

Since every nonempty A has M(A)≥1/2, failure of Chowla would yield increasing strict running-record cardinalities n_j for κ(n)/√n, tending to ratio zero. At each such cardinality one may choose an exact global minimizer A_j. Every smaller positive-integer set B then satisfies

    M(B)/sqrt(|B|) > M(A_j)/sqrt(n_j).

Thus the hypothetical sequence may be globally cardinality-minimal and strictly hereditary ratio-minimal. This is a genuine reduction, not a structural classification. It does not itself give flatness, bounded additive rank, controlled relaxation error, or a Boolean rounding theorem.

Indeed hereditary minimality does not remove the integrality obstruction. The exact set {1,2,3,4,5,6,7,9} has M=2 and is strictly hereditary ratio-minimal, verified by Sturm positivity and rational witnesses for all 254 proper nonempty subsets. Yet a feasible fractional half-mass Fejér weighting has negative minimum 4/7, whereas every Boolean four-element subset has minimum magnitude greater than √2. The resulting gap exceeds 7√2/4. This is a finite gap, not a proof of an unbounded one.

Details: [attainment and record reduction](cstar_extremizer_compactness_2026-10-20.md), [exact hereditary/integrality example](cstar_subset_minimal_2026-10-20.md). The earlier universal L1/fixed-depth floor route remains closed in its stated scope; this reduction does not reopen it.

## 3. Exact failure of the sharp W2 constant

An existing 50-frequency support, labelled N50_x71 in the data, has actual maximum 68. Explicitly it is

    {1,...,18} ∪ {20,...,37} ∪ {39,40,41,42,47,48,50,52,57,61,62,64,65,68}.

Its symmetric S has 100 elements, and W2 consists of all integers in [-136,136] except ±131, ±134 and ±135: 267 rows.

For its exact integer adjacency H=B_W2, every leading principal minor of

    50H + 353I

is positive. Fraction-free integer elimination checked every division exactly. A separate verification rebuilt W2 from the saved support, reversed the row order, checked all 267 positive pivots and matched the determinant. Sylvester's criterion therefore proves

    K_W2 < 353/50 = 7.06 < sqrt(50),
    N/K_W2² > 250000/124609 > 2.

The floating estimate is K_W2≈7.05699354. Only the rational upper bound is used in the exact refutation. This is not a global Chowla counterexample and does not refute K_W2≥c√N for an unspecified smaller c.

Exhaustive testing of all 65,535 nonempty subsets of [1,16], seeded annealing, variable-cardinality searches and structured lifted families gave finite diagnostics, not an asymptotic countermodel. Several restricted proof architectures also fail: odd-sector energy control, bounded-color induced subgraphs, a universal centered positive-spectrum cap, and a generic background-projection shortcut. Their failures specify what an argument cannot discard; they do not exhaust possible W2 methods.

Details and reproducibility: [W2 campaign](cstar_w2_universal_2026-10-20.md), [near-realization and cross-sector tests](cstar_w2_near_realization_2026-10-20.md), [experiment index](../experiments/cstar_structural_2026-10-20/README.md).

## 4. Positive result: an independently audited product-Fejér theorem

The most substantial positive result in this checkpoint excludes a concrete high-dimensional random family as an asymptotic W2 counterexample.

Let U=[-2,2]^d∩Z^d and p_s=∏_j(1-|s_j|/3) on U, zero outside. Independently select each nonzero sign class {s,-s} with probability p_s, retaining both signs. Write b_s for its indicator, S for the selected support, and

    v = sum_{s≠0} p_s(1-p_s) = 3^d - (19/9)^d.

Then

    P(K_W2 ≥ 1+sqrt(v)/6)
      ≥ 1 - 5^d exp(-((10/9)^d-3)/6) - 12/sqrt(v) - 728/v.

The failure bound tends to zero, although it can be useless at small d. Since |S|/3^d→1 in probability and v/3^d→1, this yields K_W2/√|S|≥1/6-o(1) with high probability. Here |S| counts both signs.

### Compact proof

**Filling.** The one-coordinate convolution p*p has values (19,16,10,4,1)/9 at absolute offsets 0 through 4. Thus R_t=(p*p)(t)≥(10/9)^d for t∈U. For t≠0, discard representations t=s+u involving zero or equal summands; their probability mass is at most 3. The remaining unordered representations form a simple graph on independent sign classes, of maximum degree two. Its edges split into at most three matchings, one with total probability weight at least (R_t-3)/6. Independence along that matching gives

    P(t∉S+S) ≤ exp(-(R_t-3)/6).

A union bound proves that U⊂W2 except with probability at most 5^d exp(-((10/9)^d-3)/6).

**Admissible centered vector.** Set X_s=b_s-p_s for nonzero s∈U, X_0=0, and w=(X_s)_{s∈U}. Define V=||w||² and the matrices P_uv=p_{u-v}, X_uv=X_{u-v}. Then B_U=P-I+X, and Xδ_0=w. The matrix P is positive semidefinite because its Fourier symbol is a product of nonnegative Fejér polynomials. The vector

    q = δ_0 - w/sqrt(v)

has norm squared 1+V/v. Crucially, the centered vector w has entries -p_s at unselected frequencies. Filling makes those rows available in W2; they are generally absent from W1.

Put C=w*Xw=Σ_{s,t}X_sX_tX_{s-t}. Direct expansion gives

    q*B_Uq = q*Pq - ||q||² - 2V/sqrt(v) + C/v.

**Moments.** Symmetric sign-class independence yields EV=v and Var(V)≤2v. Both covariance cases t=s and t=-s must be included; doing so gives E(w*Pw)≤2v and E(q*Pq)≤3.

Choose lexicographically positive representatives and write their centered variables as Y_a. Exactly,

    C = 12 sum_{a<b, a+b=c} Y_aY_bY_c
          + 6 sum_a Y_a²Y_{2a}.

All terms are centered. Distinct terms are orthogonal unless identical: unmatched variables force zero expectation, while a possible doubling cycle is excluded by torsion-free arithmetic. With L=Σ_a EY_a²=v/2 and |Y_a|≤1, the resulting variance is at most 144L²+36L²=45v².

**Rayleigh bound.** Chebyshev and Markov give simultaneous events

    v/2 ≤ V ≤ 2v,
    q*Pq ≤ sqrt(v)/4,
    |C| ≤ v^(3/2)/4,

with total failure probability at most 8/v+12/√v+720/v. On these events q*B_Uq≤-||q||²-√v/2 and ||q||²≤3. Therefore its Rayleigh quotient is at most -1-√v/6. Combining with filling proves the stated probability bound.

### Generalization, transfer and scope

The spectral calculation works for any finite symmetric positive-definite mean profile p with p_0=1 and 0≤p_s≤1. It requires only six-wise independence of the sign-class Bernoulli variables. Its W2 conclusion separately requires that the candidate support U fill inside W2. The exponential matching estimate for filling uses full independence, not merely six-wise independence.

For the product model, φ(s)=Σ_j s_j11^j gives an exact integer encoding. Differences u-v-s of W2 rows and a generator have coordinates in [-10,10]; successive reduction modulo 11 excludes false adjacencies. Thus the graph and its certificate transfer exactly to positive integer frequencies, not approximately.

The theorem and constants were independently audited. Exact combinatorial checks in dimensions one through three verified the cubic coefficients and every filling graph. These checks support, but do not replace, the general proof. See [full theorem](cstar_product_fejer_asymptotic_2026-10-20.md) and [independent audit](cstar_product_fejer_independent_audit_2026-10-20.md).

## 5. Why approximate idempotence is not enough

Exact Boolean coefficients imply the mixing identity p*p=1-1/K+p/K for p=(K+D)/K≥0. Absolute L1 approximation to that identity, however accurate, does not control energy, even under much stronger positivity and contact conditions than a simple weighted taper supplies.

Fix K≥2, a small η>0, α=η/K, and the normalized Fejér kernel F_L. Set q=1+α(F_L-1). It is even, positive, of mean one, and has nonnegative Fourier coefficients. Its mixing defect has L1 norm at most 2(η+η²)/K², while ||q||²_2 grows without bound as L grows.

To enforce an actual zero without negative Fourier coefficients, let g_m(x)=Σ_{j=1}^m cos(2πjx), m_m=-min g_m, choose Q>L-1 and set

    δ = min_{g_m(Qx)<0} q(x)/(-g_m(Qx)),
    p = q + δ g_m(Qx).

Then p≥0, min p=0 and its mean remains one. The spectra are disjoint. Averaging q over the Q preimages of a minimizing point of g_m gives

    (1-α)/m_m ≤ δ ≤ 1/m_m.

Since m_m≥2m/(3π) and ||g_m||_1≤1+(1/2)log(2m+1), the L1 perturbation tends to zero with m, while disjoint spectra ensure energy does not decrease. Choosing η small, L large and then m large produces arbitrarily small absolute mixing defect, arbitrarily large energy, an actual zero, and every scaled nonconstant coefficient K p̂(j) in [0,η].

These are non-Boolean countercontrols. They isolate the danger of arbitrarily many tiny coefficients near the Boolean value zero. Relative L2 defect behaves differently: in this construction it is comparable to ||p-1||_2/K. A sufficiently strong accumulated spectral error also preserves the floor. Thus the result is not a claim that every approximation approach fails; it shows why coefficientwise proximity or absolute L1 error alone cannot replace exact Booleanity. Details: [mixing and contact constructions](cstar_idempotent_mixing_2026-10-20.md).

## 6. Deterministic positive-profile fitting: what the actual tests show

For a deterministic D and a nonnegative trigonometric profile P with mean p_0, put w=D-(P-p_0), V=∫w² and q=1-w/√V. The exact identity is

    -∫Dq²/2 = p_0+sqrt(V) - ∫Pq²/2 - ∫w³/(2V).

If supp(w)⊂W2, this is a local certificate. Optimizing the two-dimensional span {1,w/√V} gives a stronger Rayleigh bound. Profiles tested were nonnegative multiples of admissibly supported Fejér kernels, pairs of such kernels, and the always-admissible positive-half autocorrelation |Σ_{a∈A}e(ax)|²/|A|.

The following are **floating numerical values, not interval-certified bounds**. All K values use D=2f_A, not M. The profile parameters were genuinely optimized, but the table is finite evidence, not a theorem for arbitrary supports.

| Support | n | Full W2 K | Single Fejér, 2D | Two Fejér packets | Autocorrelation profile |
|---|---:|---:|---:|---:|---:|
| Dense X30_s0 | 20 | 4.813847 | 3.380234 | 3.394903 | 2.313059 |
| N50_x72 | 50 | 7.111342 | 4.684989 | 4.750571 | 2.816416 |
| N50_x71 | 50 | 7.056994 | 4.800326 | 4.841885 | 2.963297 |
| Interval [1,50] | 50 | 18.462876 | 10.041189 | Not tested | 4.312445 |
| E99c target 1000, exponent 1/3 | 1056 | 160.120864 | 43.481086 | Not tested | 43.087793 |
| Root differences, rank parameter 7 | 21 | 4.543831 | 3.185891 | Not tested | 3.952688 |

For N50_x71, the normalized positive-profile and residual-cubic costs are approximately 0.05736 and 0.14623 times √V. Thus selected deterministic near-extremizers can have controlled residual cubic terms; independence is not necessary for this finite phenomenon. Two packets improve only modestly. The autocorrelation profile performs better on the root control but worse on the dense examples.

For E99c, both normalized obstruction terms are tiny, consistent with independent noise. Full W2 sees stronger excursions than these low-dimensional fits. Large W2 eigensolver residuals are documented, and no interval-arithmetic certification has been substituted for numerical output. See [complete profile table and methodology](cstar_profile_certificate_2026-10-20.md).

## 7. The exact universal gap

The random theorem succeeds because three facts align: a positive-definite mean profile, controlled centered cubic/positive cost, and enough actual W2 rows to include the negative centering coefficients. No argument yet forces that alignment for arbitrary deterministic or correlated Boolean integer supports, even after exact record-extremizer selection.

The deterministic profile experiments make a concrete next question credible: can one construct a suitable nonnegative profile, with admissible residual support and controlled Rayleigh costs, for every relevant extremizer? They do not answer it. Exact idempotence cannot be weakened indiscriminately, generic Gram or partial-matching algebra admits countermodels, and a large boundary coupling is insufficient without its exterior cost.

Restricted factorization theorems and rank estimates remain useful, but no universal representation theorem bridges them to all Boolean spectra. Work on positive factors and alternative profiles continues. The checkpoint therefore records a proved random-model exclusion, sharper obstructions to invalid shortcuts, and a precise coefficient-geometry problem still to be solved, not an exhausted search or a universal solution.
