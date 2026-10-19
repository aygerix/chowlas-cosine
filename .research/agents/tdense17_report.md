# Round 17 research report

Status: continued after reading the lead's superseding correction. Revised T2 is complete as a refutation plus an explicit sufficient boundary theorem. Revised T1 remains OPEN: this continuation proves a broad-class probabilistic square-root theorem, derives the joint necessary conditions, and performs a simultaneous-certificate search, but proves neither an absolute four-way cover nor an infinite family defeating it. No proof of Chowla is claimed.

PROVED, retained from part 1: a precise obstruction to the unqualified bulk-versus-PSD dichotomy, uniform over all three permitted vertex-set choices, and a deterministic infinite family disproving CLIQUE-S for every proposed pair of absolute constants. These are obstructions to the original lemmas; neither refutes the corrected programme after conditioning on a hypothetical K=o(sqrt(n)).

## Continuation under the corrected brief

PROVED / scope: the correction at the end of `tdense17_brief.md` supersedes the original Tasks 1–2. The actual remaining T1 is to prove an absolute four-way cover under M=epsilon sqrt(n), or exhibit an explicit infinite family defeating all four certificates. A finite search cannot establish either conclusion. The old shifted-interval family has linear M and does not answer corrected T1. The CLIQUE-S proof below answers the refutation part of T2; the new boundary theorem supplies an explicit sufficient replacement hypothesis.

Current exact frontier: the joint necessary conditions and same-set tests are below. The unresolved step is a quantitative boundary-versus-spread statement for correlated roundings, especially at vanishing density; neither the finite tests nor the independent-rounding theorem resolves it. All new scripts and numerical outputs stay in `tdense17_scratch/`; all mathematical computation uses the VM wrapper with at most four cores. No subagents or commits.

### T1: exact joint necessary conditions

PROVED (elementary quantitative consequences of quoted P9, P28, P29). Let A be any finite nonempty set of distinct positive integers, n=|A|, X=max A, epsilon>0, and assume M(A)<=epsilon sqrt(n). Put K=2epsilon sqrt(n). All of the following hold simultaneously, with the SAME epsilon and A. These conditions are not proved inconsistent.

1. **Energy-weighted Fourier spikiness.** Use normalized circle average E. For an integer H>=1 put psi_H(b)=(1−|b|/H)+ and V_m(x)=sum_{a in A}psi_H(a−m)exp(iax). For ANY nonempty finite set J of integer centers m>=H, let q=|J|,

       Phi(x)=sum_{m in J}|V_m(x)|²,
       S=E Phi=sum_{a,m}psi_H(a−m)²,
       eta=(E sqrt(Phi))²/S  (when S>0).

   Then 0<eta<=1 and

       eta S <= 4q epsilon² n.

   Proof: P28 gives M>=(1/2)E sup_{m>=H}|V_m| >= (1/(2sqrt(q)))E sqrt(Phi). Parseval gives S. The factor S/q MUST be retained: small local energy can make a bare assertion eta=O(epsilon²) false or vacuous.

   In particular take 1<=H<=X, J={H,...,X+H−1}, q=X, and n_H=|A intersect [H,X]|. The right half of each triangular window contributes

       S >= n_H (H+1)(2H+1)/(6H) >= H n_H/3,
       eta <= 12epsilon² X n/(H n_H).

   Thus H>=delta X and n_H>=rho n imply eta<=12epsilon²/(delta rho). This is the precise spiky-spectrum conclusion in a scale with nonvanishing relative energy. Front-loaded examples require choosing a different scale, not dropping this hypothesis.

   A further necessary additive condition holds for each individual window: if s_m=sum_a psi_H(a−m)²>0, interpolation and P28 imply

       E|V_m|⁴ >= s_m³/(4epsilon² n).

   The left side is exactly sum_{a+b=c+d}w_a w_b w_c w_d, w_a=psi_H(a−m). This follows from (E|V|²)³ <= (E|V|)² E|V|⁴. It quantifies the high window energy needed to hide spread; it is not a new universal Chowla bound.

2. **Star/triple condition with constants.** Let e=T3=#{(a<b):a,b in A,b−a in A}. For S=±A,

       T_S=#{(s,s') in S²:s−s' in S}=6e.

   Indeed the same-sign ordered pairs contribute 4e and the opposite-sign ones 2e; e also equals the number of ordered positive solutions a+b=c in A. Compress Cay[{0} union S] to the center and the normalized all-ones vector on S. The resulting 2-by-2 matrix is

       [[0,sqrt(2n)],[sqrt(2n),3e/n]].

   Its negative eigenvalue and P9 give the explicit certificate

       M >= (sqrt((3e/n)²+8n)−3e/n)/4.

   Equivalently, the small-M hypothesis forces

       e >= (1/(3epsilon)−2epsilon/3)n^(3/2).

   The bound is useful for epsilon<1/sqrt(2); outside that range its right side may be nonpositive. Full P9 on W2={0} union ±A is stronger than this compression.

3. **Bulk and PSD constraints.** For H_A=Cay[A], every eigenvalue is >=−K. At a cutoff tau=gamma sqrt(n)>0 let the retained eigenvalues <=tau have mean −u and second raw moment q2. Their mean is nonpositive by trace zero, and 0<=u<=K. Bhatia–Davis gives

       q2 <= K tau+(K−tau)u <= K max(tau,K).

   Therefore, for EVERY gamma>0,

       sum_{|lambda|<=gamma sqrt(n)}lambda²/n²
           <= 2epsilon max(gamma,2epsilon),
       sum_{lambda<0}lambda²/n² <= 4epsilon²,
       tr P = tr N <= 2epsilon n^(3/2),
           where P,N are the positive and negative spectral parts of H_A.

   If alpha=2e/n²>4epsilon², the positive part has effective rank <=4epsilon² n/(alpha−4epsilon²), as in the earlier audit. This still need not be bounded independently of n. The exact trace split and star constraints alone do not furnish a contradiction in the tapered sparse regime.

4. **Quantitative Gibbs constraints and their sparse scope.** For every pair of integers L>h>=1 and every theta, put G_{L,h}(a)=sum_k(1−|a−kL|/h)+. P29(b) gives

       [h f_A(theta)−L Re sum_a G_{L,h}(a)exp(ia theta)]/(L−h)
           <= epsilon sqrt(n).

   In the nontrivial scale family L=X+h this reads

       sum_{a in A}[h/X−(1+h/X)(1−a/h)+]cos(a theta)
           <= epsilon sqrt(n).

   P48 additionally says every 1/X-normalized twisted limit has a continuous Hermitian PD representative. However, if n/X tends to zero, ALL such limits are zero, since their total variation is at most n/X. P53 explicitly assumes n>=X/C; its non-atomic-defect conclusion must not be imported uniformly into density n^(−1/3).

   A valid sparse replacement at this point is weaker: every weak limit mu of (1/n)sum_a exp(ia theta_j)delta_{a/X} satisfies Re integral exp(ity)dmu(t)>=0 whenever M/n tends to zero. Proof: test f_A(theta_j+y/X)/n at each fixed y. This statement concerns a finite measure, possibly singular; it does not imply that mu has a continuous density. The bounded-density input used by P48/P53 has disappeared.

PROVED scope/circularity check, new observation relative to the searched record: the unrestricted finite P29(b) certificate ALREADY EQUALS M(A). For h=1,L=2, G(a)=1_{2 divides a}, so

    f_A(theta)−2sum_{a even}cos(a theta)=−f_A(theta+pi).

Taking the supremum over theta yields M(A). Every P29 certificate is <=M, hence the supremum over all h,L,theta is exactly M. Thus an explicit infinite family defeating **fully optimized P29(b)** would itself disprove Chowla; this is not an easier adversarial test. The search below uses the specified restriction L=X+h and finitely many h/angles, and never promotes its values to the unrestricted certificate. Conversely the asymptotic PD constraints alone are too weak to supply a numerically defined fourth certificate without a scale and a quantitative defect. This distinction is essential to stating a noncircular four-way cover.

### T1 progress: independent roundings cannot hide the P28 window variance

PROVED on paper (new quantitative high-probability consequence in this continuation; no outside priority claim). Fix a finite set of potential positive frequencies, deterministic probabilities p_a in [0,1], and independent Bernoulli selectors X_a. Let A={a:X_a=1}; for this probabilistic statement only, set M(empty)=0. Fix a permissible P28 triangular window w_a=psi_H(a−m), m>=H, and put

    B(A)=(1/2)E_x |sum_a w_a X_a exp(iax)|,
    v=sum_a p_a(1−p_a)w_a².

The normalized circle average is E_x; expectations/variance below are over the independent selectors. Then M(A)>=B(A), and, for v>0,

    E B >= b(v):=v/(2sqrt(6v+1)),
    Var B <= 1/4,
    Pr(B < v/(4sqrt(6v+1))) <= 4(6v+1)/v².

For v>=1 this gives B>=sqrt(v)/(4sqrt(7)) except with probability at most 28/v. The variance estimate, not a claim of independent Fourier samples, is what makes the probability tend to one.

Proof of the mean bound. Take an independent copy X'_a and Y_a=X_a−X'_a. For every angle x, W=sum_a w_a Y_a exp(iax) has second moment Q=2v. Independence and symmetry give

    E|W|⁴ <=3Q²+sum_a E(Y_a⁴)w_a⁴ <=3Q²+Q,

since E Y_a⁴=E Y_a²=2p_a(1−p_a) and 0<=w_a<=1. Holder interpolation gives E|W|>=Q/sqrt(3Q+1). Also E|sum w_a X_a exp(iax)|>=(1/2)E|W| by the triangle inequality applied to the two copies. Average x and multiply by 1/2 to obtain E B>=Q/(4sqrt(3Q+1))=b(v).

Proof of the variance bound (included to avoid importing an unchecked concentration theorem). On real coefficient vectors z, F(z)=(1/2)E_x|sum_a w_a z_a exp(iax)| is convex and 1/2-Lipschitz in Euclidean norm: use the triangle inequality, Cauchy–Schwarz and Parseval. Choose a subgradient g(z) with norm<=1/2 (at z=0 one can choose zero). If z^(i) differs only at coordinate i, convexity gives

    (F(z)−F(z^(i)))+ <= (g_i(z)(z_i−z_i^(i)))+.

For selector vectors, |z_i−z_i^(i)|<=1. Product-measure variance tensorization (or its elementary conditional-variance induction) says

    Var F(X) <=(1/2)sum_i E(F(X)−F(X^(i)))²
              =sum_i E[(F(X)−F(X^(i)))+²]
              <=E sum_i g_i(X)² <=1/4,

where X^(i) resamples the ith coordinate independently, and the equality uses exchangeability of the pair. Chebyshev at half the mean lower bound proves the tail estimate. Independence is essential to the tensorization and symmetrized moment bounds; no assertion is made for correlated selectors.

PROVED corollary. Let mu=sum_a p_a tend to infinity and suppose one P28 window has v>=c mu for a fixed c>0. With probability at least 1−(28/c+1)/mu, for all sufficiently large mu,

    M(A)>=sqrt(c)/(4sqrt(14)) sqrt(|A|).

Indeed |A|<=2mu except with probability <=1/mu by its variance <=mu, and combine this with the preceding v>=1 estimate. This is a broad-class square-root theorem in probability, not a bound for every deterministic rounding and not a universal Chowla proof.

PROVED application to the corrected adversary. Let X be any even positive integer, 0<alpha<=1/4, and independently include a=1,...,X with p_a=2alpha(1−a/X). Set H=m=X/2. Then

    mu=alpha(X−1),
    sum_a p_a w_a²=alpha(2H²+1)/(3H)>=mu/3,
    v>=mu/6.

The middle identity follows by pairing a and 2H−a, whose probabilities sum to 2alpha and whose window weights agree. Consequently, as mu tends to infinity,

    Pr(M(A)>=sqrt(|A|)/(8sqrt(21))) >=1−169/mu.

This holds uniformly in alpha and includes alpha of order mu^(−1/3). Therefore the independent tapered random seed mechanism is rigorously covered by P28 with probability tending to one, even though its graph certificates can be only of order mu^(1/3). The constant is conservative. The theorem leaves exponentially or polynomially rare selected outcomes, and correlated or nearly binary structured roundings, available as possible adversaries; no exclusion of those is asserted.

PROVED sequence corollary: for any sequence of these tapered models with sum_j 1/mu_j finite (in particular, geometrically increasing expected sizes), with probability one the displayed square-root lower bound holds for all sufficiently large j. No independence between the different sizes is needed: the probability of a failure at some j>=J is bounded by 169sum_{j>=J}1/mu_j, which tends to zero. Thus an ordinary infinite sequence of independent-within-size tapered roundings almost surely cannot be a T1 adversary.

### T2: a correct sufficient boundary input

PROVED (explicit elementary corollary of positive Fejer smoothing and the interval dip; not claimed as a new underlying method). Let d,k be any positive integers and A_d={a/d:a in A,d divides a}. Define the ambient boundary defect

    D_d(k)=|[1,k] minus A_d|
           +sum_{b in A_d,k<b<4k}(1−b/(4k)),
    c0=2/(3pi)−1/8>0.

Then EVERY finite A satisfies

    M(A) >= c0 k−D_d(k) >= (23/264)k−D_d(k).

In particular, an AP clique of k+1 vertices with common difference d forces M>=c0 k/2 if its difference spectrum has D_d(k)<=c0 k/2. Such a cluster certifies M>=c sqrt(n) when k>=2c sqrt(n)/c0. This is a sufficient structured-branch input; no theorem extracts such a cluster from small negative spectrum here.

Proof. Averaging f_A((x+2pi j)/d) over j=0,...,d−1 gives f_{A_d}(x), so M(A_d)<=M(A). Convolve this polynomial with the mean-one Fejer kernel of degree 4k−1. The result

    g(x)=sum_{b in A_d,b<4k}(1−b/(4k))cos(bx)

is >=−M(A). Set x=3pi/(2k+1). The complete interval I=[1,k] has

    f_I(x)=−(1+csc(3pi/(4k+2)))/2
           <=−1/2−(2k+1)/(3pi).

Replacing f_I by its weighted version increases it by at most sum_{b<=k}b/(4k)=(k+1)/8. Missing prefix frequencies and present tail frequencies increase it by at most D_d(k). Hence

    g(x)<=−c0 k−[3/8+1/(3pi)]+D_d(k),

which proves the asserted weaker bound. High frequencies b>=4k are removed EXACTLY by the positive kernel; frequencies not divisible by d are removed EXACTLY by averaging. Thus no uncontrolled cancellation by the rest of A is assumed away.

PROVED interpretation: the boundary must be sharp in the **ambient difference spectrum**, after normalizing the AP step. A large exact clique merely gives [1,k] subset A_d. It does not bound the weighted mass between k and 4k. For the deterministic selected smooth family below, D_1(k)=(9/8+o(1))k: on k<b<4k, p_b=1−O((k/L)²), so its expected weighted tail is (9/8)k+O(1+k³/L²). Its actual weighted tail differs from this by at most norm(E)_infinity, by positive Fejer convolution. Both k³/L²=O(sqrt(L)) and norm(E)_infinity=O(sqrt(L log L)) are o(k). Thus the family fails the sharp-boundary hypothesis by a fixed factor, even for the lexicographically selected deterministic output, without an unproved typicality assumption. For a general non-AP near-clique, an analogous ambient witness, and an extraction theorem producing it, remain open.

### Joint-certificate search, verification, and handoff

NUMERICAL finite search, not a cover proof: `fourway.py` evaluates the MAXIMUM of sampled P28, full P9 on W2={0} union ±A, truncated BD on A, P9 on A, compressed star, and P29(b) restricted to L=X+h. Full W2 already dominates graph A and BD, but they are retained separately to show the mechanism. Coarse h are floor(X/d), d=1,2,4,8; window centers are spaced by max(1,h//2); the circle grid is a power of two >=2(2X+1). Fine checks add d=16,32, halve the center spacing, and use grid >=8(2X+1). These are numerical quadratures and floating eigenvalues, not rigorous lower enclosures.

NUMERICAL: 58 seeded/adversarial sets, including tapered rank-2/3/4 Bohr windows and smooth Bohr roundings, quadric lifts, forced-prefix profiles, tapered and flat random sets, APs, shifted intervals, sum-free intervals, many AP/Bohr pieces, small-N sets and Singer–Bu sets. Ten starts then receive 400 fixed-cardinality swap proposals each (4,000 total), minimizing the simultaneous certificate maximum, with seed 171702. Individual probabilities, parameters, sets, cardinalities, M estimates and hashes are saved. Every winner is rechecked with the fine grid. The 36-element winner has fine objective 0.4281838033 and R_est=0.659987; it is a finite illustration that optimizing the certificates need not optimize M, not an asymptotic adversary. No family defeating all four was found.

Selected joint rows below are COARSE NUMERICAL values, all divided by sqrt(n). The complete 58-row table is [fourway_all_tables.md](tdense17_scratch/fourway_all_tables.md), the fine checks and ten search histories are [fourway_tables.md](tdense17_scratch/fourway_tables.md). Gibbs always means the explicitly restricted finite P29 family above.

| family | n | P28 | W2 | BD | Gibbs | maximum |
|---|---:|---:|---:|---:|---:|---:|
| tapered random, target 640, factor 0.6 | 610 | 0.27697 | 0.43913 | 0.04791 | 1.41851 | 1.41851 |
| hard tapered Bohr rank 2, target 640 | 642 | 0.12425 | 1.30626 | 0.05857 | 2.89438 | 2.89438 |
| hard tapered Bohr rank 3, target 640 | 639 | 0.15982 | 1.20010 | 0.06360 | 2.43669 | 2.43669 |
| hard tapered Bohr rank 4, target 640 | 616 | 0.17578 | 1.05281 | 0.06475 | 2.05134 | 2.05134 |
| smooth Bohr rounding rank 4, target 640 | 629 | 0.25286 | 0.51538 | 0.06365 | 1.33138 | 1.33138 |
| forced prefix, L=1024, exponent 5/6 | 789 | 0.18273 | 0.59554 | 0.06451 | 0.50061 | 0.59554 |
| hard rank-4 quadric lift, p=5 | 260 | 0.20170 | 1.03109 | 0.08355 | 2.87066 | 2.87066 |
| tapered rank-4 quadric lift, p=5 | 33 | 0.30356 | 0.54936 | 0.05418 | 1.70359 | 1.70359 |
| flat random, density 0.05 | 89 | 0.30904 | 0.58705 | 0.02272 | 1.38251 | 1.38251 |
| flat random, density 0.25 | 505 | 0.28113 | 0.84490 | 0.09426 | 3.62539 | 3.62539 |
| flat random, density 0.5 | 1040 | 0.22819 | 1.55104 | 0.13042 | 3.83568 | 3.83568 |
| 32 AP pieces, spacing 1000 | 512 | 0.08494 | 4.45184 | 0.08863 | 5.32393 | 5.32393 |
| 32 Bohr pieces, spacing 1000 | 320 | 0.13408 | 2.32659 | 0.06671 | 4.53878 | 4.53878 |
| Singer–Bu, q=31 | 992 | 0.22117 | 0.37736 | 0.09550 | 0.50496 | 0.50496 |

NUMERICAL energy audit: [fourway_energy_tables.md](tdense17_scratch/fourway_energy_tables.md) contains eta, S/(q n), the resulting RMS spread certificate, weighted fourth moment, e/n^(3/2), and sqrt(n)-bulk for all 58 sets plus all ten winners. It keeps the energy factor in the exact necessary condition. For the hard rank-2 Bohr seed at target 640, eta=0.198332 and S/(q n)=0.110320; for tapered random at the same target and factor 0.6, eta=0.804549 and S/(q n)=0.111525. This separates true spectral concentration from a disappearing energy budget. All values are numerical; the theorem above, not this table, excludes typical independent tapering.

PROVED / interval-certified finite CLIQUE-S instance, re-run on the VM at 120-bit Arb precision: the saved L=4096, seed=17, k=1024 set has n=3086, X=7587,

    M <=76.88736479952657,
    clique_global=1025, clique_global/K >=6.665594552970759,
    clique_in_S=1024, clique_in_S/K >=6.65909153389469.

The global clique includes 0; the clique contained in S does not. The independent conservative certificate M<=80 in the earlier verification remains available. Finite ambient boundary defects D_1(k)/k are EXACTLY 3325003/4194304=0.79274249... at L=4096, and 1100542663/1073741824=1.024960226... at L=262144. Both comfortably fail the sharp-boundary threshold c0/2, as required; their asymptotic limit is 9/8.

PROVED / additional independent pure-Arb certificate: [fourway_independent_cert.py](tdense17_scratch/fourway_independent_cert.py) establishes the exact rational bound

    M <=384437/5000=76.8874,
    clique_global/K >=2562500/384437=6.665591501338321...,
    clique_in_S/K >=2560000/384437=6.659088485239454....

This certificate uses only directed ball arithmetic for the numerical inequalities. Let G=2^21, h=pi/G, and S3=sum_a a³=62806119343873. If x* is a global minimum and x_j its nearest grid point, Taylor at x*, f'(x*)=0, and the bound |f'''|<=S3 give

    f(x*)>=f(x_j)−(|f''(x_j)|+S3 h)h²/2.

Two 120-bit Arb DFTs enclose f(x_j) and f''(x_j) at every j. For every one of the 2,097,152 points, the right side plus 384437/5000 is strictly positive; the smallest lower margin exceeds 0.00248. There is no floating critical-point calculation in this independent proof. Its complete result is [fourway_independent_certificate.json](tdense17_scratch/fourway_independent_certificate.json).

Verification artifact: [fourway_verification.json](tdense17_scratch/fourway_verification.json). EXACT integer audits check T_S=6e and the positive ordered-sum interpretation for all 511 nonempty subsets of [1,9]. NUMERICAL audits check the bulk upper bound on those sets at four cutoffs (2,044 checks); no violation occurred. EXACT rational arithmetic checks the sparse-triangle/window identity for H=1,...,64. Arb independently encloses ten smoothed boundary witnesses. A finite enumeration of seven selector coordinates checks the convex-variance estimate numerically (variance 0.01271078 versus the proved upper bound 1/4). Three 128-sample tapered ensembles have observed B variances 0.01326, 0.01907, 0.02155; these experiments are sanity checks, not the proof of concentration.

Reproducibility: [continuation_manifest.json](tdense17_scratch/continuation_manifest.json) records the seven successful VM commands, Python 3.12.3, NumPy 2.5.4, SciPy 1.18.1, source/output hashes and counts. All mathematical execution was through the required VM wrapper, in bash, with at most four cores. The first verification attempt was stopped after noticing an unnecessarily repeated set conversion; its corrected rerun completed. No mathematical result depends on the stopped run. No edits were made to `.research/*.md`, no commits and no subagents were used.

Strategic review / decision. The two corrected targets moved differently. T2 now has a complete asymptotic refutation, a re-certified instance with both clique conventions, and an ambient boundary hypothesis that genuinely forces Gibbs without assuming away the other frequencies. T1 gained precise joint constraints, the sparse-scope and unrestricted-P29 corrections, and a square-root theorem for independent roundings with nonvanishing window variance. It remains open for deliberately selected rare outcomes, correlated low-variance roundings, and multiscale structures. Discontinue searches for universal clique rigidity and additional ordinary independent tapered seeds. The next discriminating task is a quantitative boundary-versus-spread lemma for CORRELATED roundings with small window L1 norm, stated at a specified scale and with an explicit ambient defect. A future search should specify that restricted fourth certificate in advance; fully optimizing P29(b) silently restores the original M minimization problem.

## Scope and controls

- Read CLAUDE.md, NOTEBOOK continuation 19 in full, E99, P9, P27–P29, P48, P53, P63, P66 and P69.
- No edits to `.research/*.md`, no commits, no subagents. This report and `tdense17_scratch/` are the only intended write destinations.
- All mathematical computations run on the VM using `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 ...`, launched from bash. The existing wrapper itself has a zsh shebang and is left unchanged.
- Numerical minima and floating eigenvalues are NUMERICAL, never global certificates.

## Research frontier at entry (resolved status below)

| Status | Exact statement or gap | Discriminating test |
|---|---|---|
| PROVED, quoted | P9: every finite induced graph has bottom eigenvalue at least −2M(A). | Check every computed graph against numerical M, without treating this as certification. |
| PROVED, quoted; being rechecked | Continuation 19.7 truncated Bhatia–Davis and trace split. | Derive constants and the actual rank consequence. |
| CONJECTURED in brief | A universal square-root spectral bulk or low-rank PSD approximation on one of the permitted vertex sets. | Shifted intervals with macroscopic negative spectrum. |
| CONJECTURED in brief | CLIQUE-S: absolute constants c1,c2 bound every clique by c1K+c2. | Force a long initial interval in a random rounding of a smooth positive-definite profile. |
| UNKNOWN | A quantitative integer-specific replacement for clique rigidity strong enough for Chowla. | Test rank-2/3 Bohr pieces, many small pieces, and rank-4 quadric lifts. |

## Initial derivations (historical checkpoint, superseded by proofs below)

HEURISTIC at entry, now PROVED below: for A = {m+1,...,3m}, the self-difference adjacency is bipartite with cross block B(i,j)=1[j>i]. Its macroscopic negative spectrum defeats the proposed bulk-versus-PSD dichotomy as written. This example has large M and is handled by an additional direct spectral alternative; it does not refute Chowla.

HEURISTIC at entry, now PROVED below and strengthened to prefix length L^(5/6): let g(j)=(L−|j|)+, Q=sum g(j)^2, and p(a)=sum g(j)g(j+a)/Q. The mean cosine polynomial is at least −1/2. Forcing all a<=floor(L^(2/3)) costs bounded total expectation error, while the uniform random error is O(sqrt(L log L)). This yields cliques larger than every fixed multiple of K.

Novelty discipline: searched PROOFS.md for clique, initial interval/segment, prefix, B-spline, smooth/Gaussian rounding, shifted interval, Bhatia–Davis, quasirandomness and trace-fourth terms. The generic profile-rounding mechanism is already in the project; the proposed clique consequence and the shifted-interval obstruction were not found in that search. External priority is not asserted.

## First VM results and strategic review

NUMERICAL, `tdense17_scratch/probe.json`: for shifted intervals with n = 32,128,512,2048, the gamma=1 bulk divided by n² is 0.04404,0.02442,0.01255,0.007218; negative spectral energy divided by n² is 0.11719,0.12305,0.12451,0.12488. The proposed singular-value formula agrees with independent dense eigendecomposition for m=16,64.

NUMERICAL: forced smooth-profile roundings at L=512,4096,32768,262144 give clique/K ratios up to 1.296,1.676,2.027,2.642. The last value is an uncertified estimate, not a certified lower bound for the ratio.

PROVED, interval-certified finite case using the existing Arb-DFT/Taylor certifier: L=4096, seed=17, n=3057, max A=7587, clique size=257, M<=76.67014789178872, hence clique/K>=1.6760108534205944. This finite instance alone does not refute unspecified absolute constants in CLIQUE-S; the independent asymptotic proof appears below.

Strategic review after the two distinct tests: discontinue attempts to prove the unqualified dichotomy or CLIQUE-S unchanged. Continue with exact obstruction proofs, adversarial tables, and a replacement lemma that controls all finite induced graphs rather than just Cay[A]. The direct large-negative-eigenvalue alternative repairs the shifted-interval example. Smooth profile rounding attacks clique rigidity itself, so a repair must change its hypotheses or conclusion.

Further NUMERICAL refinement: forcing a prefix of length L^(5/6), rather than L^(2/3), costs only O(sqrt L) in the mean profile. At L=4096, seed=17, the resulting set has n=3086, a clique of size 1025, and the existing Arb/Taylor certificate gives M<=76.88736479952657, hence clique/K>=6.665594552970759. At L=262144, seed=17, the numerical ratio is 21.149634587081778 (clique size 32769, n=197122); the large example is not interval-certified.

## Exact obstruction to BULK versus PSD

PROVED (new application in this report; no external priority claim). Let A_m={m+1,...,3m}, n=2m, m>=2. Fix any beta>0, gamma>0 and epsilon<1/sqrt(32). For all sufficiently large m, EVERY one of W=A_m, W=A_m union {0}, and W=A_m union (A_m+t), for EVERY integer t, simultaneously satisfies:

- sum of lambda² over |lambda|<=gamma sqrt(n) is o(n²), uniformly in t;
- distance in Frobenius norm from H_W to the PSD cone is at least (1/sqrt(32)−o(1)) times |W|.

Thus no choice among the three permitted vertex-set rules can make the unqualified dichotomy with a small-error PSD alternative true. The obstruction is to the stated alternative, not to arbitrary definitions of “structured.” A definition including all finite-complexity indefinite graphons would classify these intervals as structured.

Proof on W=A_m. In the lower-half/upper-half ordering, H=[0 B; B-transpose 0], B(i,j)=1[j>i], i,j=1,...,m. Its nonzero singular values are

    s_j = 1 / (2 sin((2j−1)pi/(4m−2))),   j=1,...,m−1.

Deleting a zero row and column reduces B to an invertible triangular all-ones matrix. Its inverse is the first-difference bidiagonal matrix; diagonalizing its squared singular-value matrix gives the displayed formula. Consequently the spectrum of H is the pairs +s_j,−s_j and two zeros, and

    sum_negative lambda² = sum_j s_j² = m(m−1)/2.

The last equality also follows directly from the number of ones in B. Projection onto the PSD cone deletes exactly the negative eigenvalues, so the normalized squared distance on A_m tends to 1/8.

Uniform bulk proof, including all translates. Partition Z into consecutive cells of length h=ceil(n/q). W occupies at most 2q+3 nonempty cells. Replace each coordinate by its cell representative in the indicator m<|u−v|<=3m to obtain a block-constant matrix T of rank at most 2q+3. For fixed u, an entry can change only when v is within 2h of one of u±m,u±3m, so at most 16h+4 entries in that row change. Since |W|<=2n,

    norm(H_W−T)_F² <= 32n²/q + 40n.

For any matrix with a rank-r approximation T, its spectral energy at singular values <=a is at most r a² + norm(H_W−T)_F²: keep at most r such singular values and apply the rank-r tail bound to the rest. Set a=gamma sqrt(n), q=ceil(sqrt(n)); this is O_gamma(n^(3/2))=o(n²), with constants independent of t.

Every allowed W contains A_m. The restriction of a PSD matrix to A_m is PSD, hence its squared error on W is at least m(m−1)/2. Since |W|<=4m, the squared error normalized by |W|² is at least (m−1)/(32m). This proves the assertion even without a rank restriction.

PROVED scope check: at x=pi/(2m), f_A(x)=−cot(pi/(4m)), so M(A_m)>=cot(pi/(4m)) is linear in n. Adding the alternative “a negative eigenvalue already has magnitude >=c sqrt(n)” removes this obstruction immediately. The example does not challenge the low-K-conditioned programme.

## CLIQUE-S verdict: false for every pair of absolute constants

PROVED (paper proof below; new clique consequence relative to the searched project record). For every pair of real constants c1,c2 there is a finite set A of distinct positive integers and an integer clique C with C−C contained in ±A union {0} such that

    |C| > c1 (2M(A)) + c2.

The conclusion remains true for cliques contained in S=±A. In fact there is a deterministic, terminating family with n between L/2 and L, max A<2L, containing the complete interval {1,...,L^(5/6)}, and M(A)=O(sqrt(L log L)). No randomness is needed in the definition of the final family; randomness proves its finite selection rule succeeds.

Construction and proof. Let t>=4 be an integer, L=t^6, k=t^5, and g(j)=(L−|j|)+ on Z. Put

    Q = sum_j g(j)^2 = L(2L²+1)/3,
    p_a = sum_j g(j)g(j+a)/Q,  1<=a<=2L−2.

Every p_a is rational in [0,1]. Also

    1 + 2 sum_a p_a cos(ax) = |sum_j g(j) exp(ijx)|²/Q >= 0

for every real x. This is an exact positive-definite mean profile, with constant term 1.

Force all a<=k to be present; for a>k choose independent Bernoulli(p_a) variables X_a. Let Y_a=X_a−p_a for a>k, and E(x)=sum_{a>k}Y_a cos(ax). The forcing error D=sum_{a<=k}(1−p_a) obeys

    1−p_a = sum_j (g(j+a)−g(j))²/(2Q)
           <= a² sum_j(g(j+1)−g(j))²/(2Q)
           = La²/Q <= 3a²/(2L²),
    D <= 3k³/(2L²) = (3/2)sqrt(L).

The inequality is Cauchy–Schwarz on the a telescoping increments; sum of squared first increments is 2L. Therefore every realization satisfies f_A(x)>=−1/2−D−|E(x)| for every x.

Set G=16L², r=ceil(log_2(128L²)), and u=ceil(sqrt(Lr)), all integers. For a fixed angle, Hoeffding's inequality (proved here by the usual bounded-variable exponential-moment argument) gives

    Pr(|E(x)|>u) <= 2 exp(−u²/L).

There are fewer than 2L independent terms, each with range length at most 1. On the G equally spaced angles, the union-bound failure probability is at most

    2G exp(−u²/L) <= 2G 2^(−r) <= 1/4.

For completeness, the bounded-variable argument used is: if Z has mean zero and lies in an interval of length b, convexity of exp and a second-derivative bound on the log moment-generating function give E exp(sZ)<=exp(s²b²/8); multiply over terms and minimize exp(−su+s² sum b²/8) over s. This yields 2 exp(−2u²/sum b²), hence the displayed bound.

Since |E'|<=sum_{a<2L}a<2L², every point of the circle is within pi/G of a grid point, and grid success implies norm(E)_infinity<=u+pi/8<u+1/2. Thus

    M(A) <= u + (3/2)sqrt(L) + 1 <= B_L := u + 2sqrt(L) + 1.

The cardinality mean is

    E|A| = (L^4/Q−1)/2 + D.

It lies between 3L/4−1 and 3L/4+(3/2)sqrt(L). With L>=4096, the event ||A|−E|A||<=L/8 implies L/2<=|A|<=L. Its failure probability is at most 2 exp(−L/64). Intersecting it with grid success has positive probability, at least 3/4−2 exp(−L/64).

To make the family explicit, enumerate the subsets of {1,...,2L−2} containing {1,...,k} in lexicographic order and select the first satisfying L/2<=|A|<=L and |E(2pi j/G)|<=u for every 0<=j<G. These are finitely many comparisons of real algebraic numbers, because p_a is rational and the phases are roots of unity. They are decidable, including equality. The probability argument proves the search terminates. This is an explicit but computationally impractical generator, not a claim that our seeded samples equal its selected output.

Finally C={0,...,k} is a clique, and C'={1,...,k} is a clique contained in S. Since

    (k+1)/(2B_L) grows on the order of L^(1/3)/sqrt(log L),

the ratio |C|/K tends to infinity, and |C|−c1K tends to infinity for each fixed c1. This disproves CLIQUE-S including its additive constant c2.

PROVED relevance to the structured branch: these are exact cliques of size much larger than sqrt(n), yet M=o(|C|). Thus a linear Gibbs dip cannot be inferred from a clique or an initial AP alone, even when the rest of A is disjoint from its differences. Contributions from the other frequencies cancel it. A lower bound of order sqrt(n) on this family is not refuted: the quoted P63 theorem already applies, since max A/n<4.

## Noise calculations and audit of the quoted tools

PROVED, exact identities for every finite nonempty A. Write h(u,v)=1_A(|u−v|) for u,v in A and d(u)=sum_v h(u,v). Define

    T = #{(u,v): u<v, u,v in A, v−u in A},
    U = #{(x,a,b): x,a,b,a+b,x+a,x+a+b in A, a,b>0},
    c(u,v) = #{w in A: |w−u| and |w−v| are in A}.

Then

    tr H = 0,
    tr H² = 2T,
    tr H³ = 6U,
    tr H⁴ = sum_{u,v in A} c(u,v)²
           = 2T + 4 sum_u binom(d(u),2) + 8 C4(H),

where C4(H) counts unoriented simple four-cycles, each counted once. The cubic formula uses the unique increasing order x<x+a<x+a+b of each triangle. The fourth-power formula counts all closed length-four walks, including backtracking, so “four-cycle count” without these degeneracies must not be substituted directly.

More generally, for every finite W in Z and integer j>=2,

    tr H_W^j = sum over s1,...,sj in ±A with sum s_i=0
               of |W intersect (W−s1) intersect ... intersect (W−s1−...−s_(j−1))|.

This is an exact additive-count formula for each required moment. The self-referential condition is used precisely by taking W=A, so each base point and all its partial sums must themselves be frequencies of A. None of the spectral inequalities below uses that condition; they apply to arbitrary symmetric trace-zero matrices.

PROVED, rechecked quoted Bhatia–Davis. Let H be any real symmetric h-by-h trace-zero matrix, tau>0, and let mu,v be the mean and variance of its eigenvalues <=tau. Their sum is nonpositive because all omitted eigenvalues are positive, so mu<=0. If kappa=−lambda_min(H), averaging (lambda+kappa)(tau−lambda)>=0 gives

    v <= (tau+|mu|)(kappa−|mu|),
    kappa >= v/(tau+|mu|)+|mu|.

This proves continuation 19.7(a) exactly, including the cutoff-mean term. There is no assumption that the bottom eigenvector is orthogonal to the constants.

PROVED, quantitative bulk consequence. If h<=cn and sum_{|lambda|<=gamma sqrt(n)}lambda²>=beta n², take tau=gamma sqrt(n). The second raw moment of the retained distribution is at least beta n²/h. With q2=v+mu², the preceding expression is

    (q2+tau|mu|)/(tau+|mu|) >= min(q2/tau,tau).

Therefore P9 gives

    M(A) >= (1/2) min(gamma,beta/(c gamma)) sqrt(n).

For W=A, c=1; for either larger permitted W one may use c=2 (also for n=1). This proof tracks the mean loss exactly instead of assuming it is negligible.

PROVED, what a C4 estimate actually needs to say. Order eigenvalues so lambda1 is the Perron eigenvalue of an adjacency matrix. If

    sum_{i>=2}lambda_i² >= delta n²,
    sum_{i>=2}lambda_i⁴ <= C n³,

then at most (C/gamma²)n² of that second moment lies above gamma sqrt(n) in absolute value. Hence beta>=delta−C/gamma², and choosing gamma²=2C/delta gives the preceding square-root bound. The same argument works after removing any specified collection of positive outliers, provided these two bounds hold for the remaining eigenvalues. Removing a macroscopic negative outlier is unnecessary, since P9 already succeeds.

PROVED correction to the proposed quasirandomness step: ordinary asymptotic C4 accuracy at o(n⁴) only implies residual eigenvalues o(n), not a bound at sqrt(n). An additive Cn³ residual-fourth-moment bound is sufficient for a constant-fraction sqrt(n)-scale bulk; a bare o(n⁴) statement is not. More explicitly, for a fixed alpha in (0,1), divide n vertices into r~n^(1/3) equal groups of size s~n^(2/3), take a symmetric independent-edge density-alpha graph B on the r groups, and replace each group by s twins (no internal edges). With positive probability tr B²~alpha r² and lambda1(B)~alpha r, so the residual square mass is ~alpha(1−alpha)r². The C4 law is alpha⁴r⁴+o(r⁴), hence after blowing up it is alpha⁴n⁴+o(n⁴), but every nonzero blown-up eigenvalue has form s lambda(B). Since s/sqrt(n)->infinity, the energy inside gamma sqrt(n) is at most r gamma² n=o(n²), while a constant fraction of n² remains outside the top. This is a generic-graph logical counterexample to the proposed inference, not an assertion that these graphs have the self-difference form.

PROVED justification of the probabilistic base just used: center B by alpha(J−I). In the fourth trace of this centered matrix, independence and mean zero kill every closed walk using an edge only once, leaving O(r³) walks with bounded expectation. Thus its expected fourth trace is O(r³). Markov gives centered operator norm o(r) with probability tending to one. The edge count is alpha r²+o(r²) by its variance O(r²). It follows that lambda1(B)=alpha r+o(r), every other eigenvalue is o(r), and tr B⁴=alpha⁴r⁴+o(r⁴). This supplies the required qualitative law without importing a quantitative random-matrix theorem.

Literature note (CITED-VERIFIED bibliographic source only): the original [Chung–Graham–Wilson paper, 1988](https://authors.library.caltech.edu/records/b1b1j-x5y91) concerns equivalent qualitative quasirandomness properties. The source abstract and bibliographic record were accessible; its PDF fetch was unavailable here. No quantitative theorem is imported from that inaccessible PDF. The sufficient n³ estimate and the blow-up obstruction are derived above.

PROVED, rechecked quoted trace split, with its rank limitation. If lambda_min(H)>=−K, take the positive and negative spectral parts P,N. Then

    H=P−N,  P,N PSD,  norm N<=K,
    tr P=tr N<=hK,
    norm(H−P)_F²=tr N²<=hK².

For h=n, alpha=tr(H²)/n² and K=epsilon sqrt(n), this gives

    tr(P²)>=(alpha−epsilon²)n²,
    effective_rank(P)=(tr P)²/tr(P²)
                     <= epsilon² n/(alpha−epsilon²),

when alpha>epsilon². This is not a rank bound R(epsilon) independent of n. The paper argument in continuation 19.7(b) is correct up to the stated order epsilon²n/alpha, but it does not itself give the bounded effective rank requested in the proposed dichotomy. The zero-diagonal, Boolean, self-induced hypotheses would have to provide that additional step.

PROVED limitation of the Gram-to-clique inference: an induced three-vertex path has bottom eigenvalue −sqrt(2), so K I+H can be PSD on this non-clique as soon as K>=sqrt(2). In the proposed small-K regime K=epsilon sqrt(n), K can still diverge. Thus exact Gram positivity by itself is not a transitivity or clique statement. This example does not refute a quantitative global extraction theorem; it identifies a missing implication.

## Structured branch and boundary tests

PROVED, quoted: P27 supplies square-root bounds for its explicitly stated bounded unions of translated dilates; P29(b), P48 and P53 constrain full twisted profiles. None states that an arbitrary large clique forces a linear dip. The smooth-profile family above shows why the full profile, including all frequencies outside the cluster, must remain in any such application.

PROVED, quantitative loss accounting: if a particular cluster polynomial has a negative value at most −b times its size ell, and the rest contributes at most E at that same angle, then M>=b ell−E. This beats c sqrt(n) only if ell>=(c sqrt(n)+E)/b. For E=O(sqrt(n)) the threshold is of order sqrt(n). Without control of E, even ell~n^(5/6) need not force M of order ell. There is no valid extraction-to-Gibbs theorem proved here.

NUMERICAL boundary tests: the rank-4 GAP lift uses balanced coordinates v in [−h,h]^4, integer encoding v1+Bv2+B²v3+B³v4, B=4h+3, and the condition v1v2+v3²−d v4²!=0 modulo p, d a quadratic nonresidue. The base prevents carries for differences of lifted vertices. Positive encoded points give A. Hard cutoffs use all such points; tapered cutoffs independently round the product triangular probabilities, using seed 17 and then reflect by the ±A convention. These are finite examples, not a proof uniform in p, dimension, boundary size, or taper.

NUMERICAL: at p=3, going from one residue box to a three-repeat hard box changes (n,R_est) from (30,2.0634) to (2430,11.6387). Product triangular thinning of the larger box gives (235,2.5764). At p=5, hard and tapered one-box examples give (260,4.1134) and (33,2.2825). No small-R lift appears in these tests. The much smaller tapered cardinality means the reduction in R must not be interpreted as a matched-size boundary asymptotic.

NUMERICAL Sidon cancellation search, using Gurobi 13.0.3 only: plant the Singer clique of sizes 4,6,8 (q=3,5,7), fix every positive difference to be present, and allow all additional frequencies up to three times the largest planted difference. Minimize the sampled negative minimum with cutting planes; at most four solves, 25 seconds per solve, four threads. The incumbents were the original difference sets (no extra frequencies selected), with certified clique/K lower bounds 1.0101181,1.0335728,0.99999764. The q=3 final finite-grid model was solved to its floating tolerance; q=5,7 reached the time limit. These are neither exact continuous optimality certificates nor a global exclusion of Sidon cancellation. Full candidates and bounds are in sidon_completion.json.
## Adversarial tables

NUMERICAL unless a separate exact or interval certificate is explicitly stated. Density alpha is tr(H²)/n² (including the diagonal normalization). B1 and B2 are the spectral energies inside sqrt(n) and 2sqrt(n), divided by n². Dpsd is the Frobenius distance to the PSD cone divided by n. BD is the truncated Bhatia–Davis bound at tau=sqrt(n), divided by sqrt(n).

| family | n | R est | alpha | B1 | B2 | Dpsd | −min eig / sqrt n | star | BD |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| smallN_36 | 36 | 0.56479 | 0.85185 | 0.11701 | 0.11701 | 0.31021 | 0.68305 | 0.68308 | 0.23306 |
| smallN_50 | 50 | 0.61199 | 0.88 | 0.092483 | 0.092483 | 0.26446 | 0.58219 | 0.59158 | 0.19718 |
| smallN_80 | 80 | 0.66339 | 0.8425 | 0.10669 | 0.12306 | 0.28066 | 0.62869 | 0.6287 | 0.19908 |
| smallN_100 | 100 | 0.66502 | 0.7852 | 0.14331 | 0.16103 | 0.30444 | 0.72128 | 0.72128 | 0.21974 |
| singer_bu_61 | 3782 | 0.60402 | 0.56154 | 0.1702 | 0.18808 | 0.28896 | 0.73859 | 0.73859 | 0.19781 |
| AP_128 | 128 | 2.5116 | 0.99219 | 0.0077515 | 0.0077515 | 0.088042 | 0.088388 | 0.088388 | 0.088388 |
| shifted_interval_128 | 128 | 7.5489 | 0.24609 | 0.02442 | 0.046595 | 0.35078 | 3.5732 | 3.5732 | 0.16883 |
| sumfree_odd_128 | 128 | 11.314 | 0 | 0 | 0 | 0 | -0 | 1 | 0 |
| AP_512 | 512 | 4.9423 | 0.99805 | 0.0019493 | 0.0019493 | 0.044151 | 0.044194 | 0.044194 | 0.044194 |
| shifted_interval_512 | 512 | 15.062 | 0.24902 | 0.012548 | 0.024743 | 0.35286 | 7.1885 | 7.1885 | 0.15193 |
| sumfree_odd_512 | 512 | 22.627 | 0 | 0 | 0 | 0 | -0 | 1 | 0 |
| bohr_rank2 | 1283 | 7.7587 | 0.56262 | 0.021489 | 0.042857 | 0.21121 | 2.995 | 2.995 | 0.091783 |
| bohr_rank3 | 715 | 5.829 | 0.4201 | 0.041983 | 0.074324 | 0.22609 | 1.8101 | 1.8101 | 0.11656 |
| many_AP_8 | 128 | 6.0215 | 0.41016 | 0.070186 | 0.13226 | 0.37117 | 2.6687 | 2.6687 | 0.20779 |
| many_Bohr_8 | 80 | 5.1464 | 0.18375 | 0.073035 | 0.12643 | 0.28725 | 1.4126 | 1.414 | 0.15087 |
| many_AP_32 | 512 | 11.371 | 0.4541 | 0.036488 | 0.07815 | 0.35837 | 4.9881 | 4.9881 | 0.17726 |
| many_Bohr_32 | 320 | 9.857 | 0.20344 | 0.029078 | 0.068602 | 0.29585 | 2.8095 | 2.81 | 0.13342 |
| quadric_3_1_False | 30 | 2.0634 | 0.34667 | 0.19706 | 0.19706 | 0.3292 | 0.89047 | 0.90724 | 0.25806 |
| quadric_3_3_False | 2430 | 11.639 | 0.32274 | 0.039189 | 0.083247 | 0.26142 | 2.7426 | 2.7426 | 0.12058 |
| quadric_3_3_True | 235 | 2.5764 | 0.088909 | 0.07577 | 0.088909 | 0.19453 | 0.60849 | 0.64581 | 0.08298 |
| quadric_5_1_False | 260 | 4.1134 | 0.38308 | 0.088299 | 0.11824 | 0.26114 | 1.3711 | 1.3713 | 0.16711 |
| quadric_5_1_True | 33 | 2.2825 | 0.10836 | 0.10836 | 0.10836 | 0.22401 | 0.62129 | 0.79194 | 0.10836 |
| random_0.05 | 103 | 2.3913 | 0.057498 | 0.057498 | 0.057498 | 0.1662 | 0.45279 | 0.77873 | 0.057498 |
| random_0.25 | 563 | 5.6411 | 0.26663 | 0.19096 | 0.19467 | 0.32139 | 1.0429 | 1.043 | 0.20404 |
| random_0.5 | 1002 | 5.825 | 0.49547 | 0.21589 | 0.24953 | 0.36015 | 1.2214 | 1.2214 | 0.25938 |
| forced_spline_512 | 381 | 1.3827 | 0.80482 | 0.098069 | 0.098069 | 0.24794 | 0.71607 | 0.7161 | 0.14228 |

NUMERICAL moment and rank audit. T3=tr(H³)/n³, T4=tr(H⁴)/n⁴, C4res=(tr(H⁴)−lambda_max^4)/n³. The effective rank is (tr P)²/tr(P²); traceP is tr(P)/n^(3/2). Qneg is sum_negative lambda² divided by n K_est². Raw integer counts and cutoff mean/variance for every row are in zoo.json.

| family | T3 | T4 | C4res | eff rank | traceP | Qneg |
|---|---:|---:|---:|---:|---:|---:|
| smallN_36 | 0.6232 | 0.54095 | 0.034319 | 1.8036 | 0.19457 | 0.075418 |
| smallN_50 | 0.69662 | 0.62071 | 0.026177 | 1.8723 | 0.17416 | 0.046684 |
| smallN_80 | 0.60949 | 0.51815 | 0.044956 | 3.7814 | 0.19 | 0.044747 |
| smallN_100 | 0.49336 | 0.39032 | 0.073105 | 6.1296 | 0.20603 | 0.052392 |
| singer_bu_61 | 0.19533 | 0.10941 | 2.7058 | 279.43 | 0.18794 | 0.057215 |
| AP_128 | 0.97668 | 0.96911 | 6.0558e-05 | 1 | 0.087698 | 0.00030719 |
| shifted_interval_128 | 0 | 0.020192 | 1.311 | 8.1555 | 0.088543 | 0.00053982 |
| sumfree_odd_128 | 0 | 0 | 0 | 0 | 0 | 0 |
| AP_512 | 0.99415 | 0.99221 | 3.8072e-06 | 1 | 0.044108 | 1.9951e-05 |
| shifted_interval_512 | 0 | 0.020671 | 5.3684 | 12.156 | 0.054371 | 0.00013721 |
| sumfree_odd_512 | 0 | 0 | 0 | 0 | 0 | 0 |
| bohr_rank2 | 0.24943 | 0.1404 | 9.9193 | 13.005 | 0.072462 | 0.00018526 |
| bohr_rank3 | 0.12287 | 0.051746 | 3.034 | 21.481 | 0.10529 | 0.0003761 |
| many_AP_8 | 0.089722 | 0.054274 | 0.62439 | 7.6201 | 0.12734 | 0.00094991 |
| many_Bohr_8 | 0.0085313 | 0.0047182 | 0.11458 | 12.112 | 0.1238 | 0.00077884 |
| many_AP_32 | 0.12417 | 0.072475 | 2.232 | 12.192 | 0.088063 | 0.00024832 |
| many_Bohr_32 | 0.011807 | 0.0059566 | 0.51357 | 20.393 | 0.085945 | 0.00022522 |
| quadric_3_1_False | 0.057556 | 0.025427 | 0.091367 | 6.0419 | 0.21907 | 0.0063632 |
| quadric_3_3_False | 0.055935 | 0.018142 | 3.7842 | 65.344 | 0.082711 | 0.00012613 |
| quadric_3_3_True | 0.0016357 | 0.00023755 | 0.015254 | 60.448 | 0.11461 | 0.0014253 |
| quadric_5_1_False | 0.090211 | 0.035023 | 0.69381 | 21.133 | 0.15998 | 0.0010076 |
| quadric_5_1_True | 0.0018365 | 0.0010237 | 0.017617 | 9.4703 | 0.12921 | 0.002408 |
| random_0.05 | 0.00023611 | 8.2683e-05 | 0.0061408 | 32.922 | 0.097718 | 0.0012077 |
| random_0.25 | 0.018806 | 0.0053258 | 0.083861 | 123.83 | 0.18954 | 0.00081149 |
| random_0.5 | 0.12176 | 0.06063 | 0.14508 | 126.28 | 0.2147 | 0.0009557 |
| forced_spline_512 | 0.56403 | 0.46266 | 0.30303 | 12.096 | 0.15362 | 0.0080382 |

NUMERICAL clique lower bounds. Clique membership and all pair differences are checked exactly. These are heuristic lower bounds for the clique number, not maximum-clique certificates. The column +0 extends the clique by the common neighbor 0; K_est is an uncertified minimum estimate.

| family | clique in S | with 0 | K est | (with 0)/K est |
|---|---:|---:|---:|---:|
| smallN_36 | 12 | 13 | 6.777539 | 1.9181 |
| smallN_50 | 19 | 20 | 8.65491 | 2.310827 |
| smallN_80 | 28 | 29 | 11.86707 | 2.443737 |
| smallN_100 | 21 | 22 | 13.30049 | 1.654074 |
| singer_bu_61 | 76 | 77 | 74.29203 | 1.03645 |
| singer_bu_101 | 101 | 102 | 119.4616 | 0.8538306 |
| singer_bu_151 | 151 | 152 | 175.0295 | 0.868425 |
| singer_bu_199 | 199 | 200 | 225.7681 | 0.8858647 |

NUMERICAL and separately certified profile examples. All listed ratios use a known clique; global clique maxima were not computed.

| L | forced prefix | seed | n | clique | M est | clique/K est | certified ratio lower |
|---|---:|---:|---:|---:|---:|---:|---:|
| 512 | 64 | 17 | 381 | 65 | 26.989404 | 1.2041763 | — |
| 512 | 64 | 117 | 388 | 65 | 25.084862 | 1.2956021 | — |
| 4096 | 256 | 17 | 3057 | 257 | 76.666533 | 1.6760899 | 1.6760108534205944 |
| 4096 | 256 | 117 | 3080 | 257 | 81.991146 | 1.5672424 | — |
| 32768 | 1024 | 17 | 24631 | 1025 | 263.83401 | 1.9425093 | — |
| 32768 | 1024 | 117 | 24556 | 1025 | 252.88758 | 2.0265922 | — |
| 262144 | 4096 | 17 | 196893 | 4097 | 775.27619 | 2.6422842 | — |
| 262144 | 4096 | 117 | 196612 | 4097 | 799.34218 | 2.5627323 | — |
| 4096 | 1024 | 17 | 3086 | 1025 | 76.883729 | 6.6659098 | 6.665594552970759 |
| 4096 | 1024 | 117 | 3108 | 1025 | 77.291206 | 6.6307673 | — |
| 262144 | 32768 | 17 | 197122 | 32769 | 774.69424 | 21.149635 | — |
| 262144 | 32768 | 117 | 196876 | 32769 | 791.61635 | 20.697526 | — |
