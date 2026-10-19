# Round 18 report: correlated roundings and the boundary programme

Status: ROUND 18 COMPLETE as partial theorems and a certified obstruction to the proposed reverse implication. Chowla and the universal TAPER lemma remain OPEN.

- PROVED: a periodic triangular Bohr family at exactly density n^(-1/3) has an explicit full-W2 bound M>=7n/2720+1/2. This excludes that correlated family with a constant independent of density.
- PROVED: the independent-rounding argument extends to independent blocks with arbitrary internal correlations and bounded selected occupancy, uniformly at vanishing density.
- PROVED / finite, with two independent M certificates: at epsilon=3/7, an explicit 36-element set satisfies all four necessary conditions, even with complete triangular P28 and full W2, but M>3.9599>epsilon sqrt(36). Thus their literal same-epsilon converse is false.
- UNKNOWN: whether the four conditions are inconsistent for every sufficiently small epsilon, or admit a family defeating the cover as epsilon tends to zero. No asymptotic equivalence or Chowla counterexample is claimed.

## Scope and exact target

CONJECTURED target: there exists an absolute c > 0 such that every finite nonempty set A of distinct positive integers satisfies M(A) >= c sqrt(n), where n = |A| and M(A) = -min_x sum_{a in A} cos(ax), over the entire real circle.

All round 18 writes were restricted to this report and `tdense18_scratch/`. No root `.research/*.md` files were edited; no commits or subagents were used. All mathematical computation ran on dirichlet through `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4`, invoked from bash. No LaTeX. No LP/MILP/QP or SDP was needed.

## Starting frontier

PROVED / QUOTED from P70 and the round 17 report: small M implies energy-weighted P28 spikiness, the quantitative triple lower bound, the graph bulk constraints, and absence of the stated sharp boundary. Full P9 on W2 = {0} union ±A dominates its compressed star and the graph-A bulk bounds. Independent roundings are excluded with high probability when one window carries a fixed proportion of the Bernoulli variance. That theorem does not cover selected correlated outcomes.

PROVED / QUOTED circularity warning: optimizing unrestricted P29(b) gives exactly M already at h = 1, L = 2. Round 18 will measure the explicit sharp-boundary defect instead, and keep sampled P28 distinct from its all-window supremum.

UNKNOWN: whether the four explicit certificates together have a universal square-root lower bound; whether the proposed TAPER statement is true; whether their smallness implies small M in any uniform quantitative sense.

## Tasks carried out and limits

1. Tested 33 saved sets from sparse cumulative tapers, correlated Bohr tapers, dilation unions, forced-prefix thinning, tapered Singer–Bu sets, and antithetic/Thue–Morse selections. Every row includes sampled P28, full W2, compressed star, bulk, and exhaustive d,k boundary optimization.
2. Proved the two class theorems below, identified an invalid bounded-spike intermediate inference, and retained a precise unproved extraction lemma. The universal TAPER proof was not obtained.
3. Proved the literal same-epsilon reverse implication false by a finite certified example. The asymptotic small-epsilon alternatives remain undecided.

NUMERICAL outcome: cumulative and antithetic tapers retain sampled P28 around 0.27–0.29 sqrt(n). Nested Bohr tapers lower sampled P28 and strengthen W2. Tapered Singer–Bu gives the smallest sampled maximum, about 0.24535 sqrt(n), but its M estimate is about 0.76659 sqrt(n). No tested sequence supplies an o(sqrt(n)) family. Six representative candidates received all-circle Arb enclosures, and the 36-element reverse example also received an independent exact Sturm certificate. All numerical asymptotic interpretations are explicitly limited below.

## Exact finite reductions

PROVED (elementary; new packaging in this report). The complete positive sharp-boundary optimization is finite without a cutoff assumption on X. Put c0 = 2/(3 pi) - 1/8. Since D_d(k) >= k - |A_d|,

    c0 k - D_d(k) <= |A_d| - (1-c0)k.

Thus a positive value requires d to divide some a in A and k < |A_d|/(1-c0). The VM code enumerates all these d,k and computes D as an exact rational, using rational lower and upper bounds for c0. This is a complete boundary audit, unlike a scan of a few dilations or scales.

PROVED (elementary). For the Fejer triangular version of P28, all integer H and centers reduce to 1 <= H <= X and H <= m < X+H. For H >= X write m=H+r. Then

    V_(H,H+r)(x) = (1/H) sum_{a>r} (a-r) exp(iax).

Its centerwise supremum decreases as 1/H, so H=X dominates every H>=X. This permits an all-window, rather than sampled-window, upper certificate on a finite example. The reduction concerns triangular Fejer kernels; it does not optimize every other kernel allowed by general P28.

PROVED extension to noninteger widths, still with the integer modulation centers required by P28: if h<H<h+1, then psi_H=alpha psi_h+(1-alpha)psi_(h+1), where alpha=h(h+1-H)/H. Every permissible integer center for H is permissible for both integer widths. Triangle inequality and integration therefore bound its certificate by the maximum of the two neighboring integer-width certificates; integer endpoints were already checked. Widths below 1 give the same single-frequency bound as H=1. Thus the finite check also dominates all real triangular widths for which these windows are used.

## Structural review after the first two attacks

PROVED / logic: a one-sided certificate implication does not make the programme equivalent to Chowla. The current known implication is small M => all four small certificates. The reverse implication requires proof. Conversely, even a uniform cover of the four certificates could prove Chowla without providing an upper comparison M <= C times their maximum. These are different assertions.

Decision: continue the sparse deterministic constructions, but also test the reverse implication directly on the round 17 optimized finite set using all triangular windows, exact graph positivity, the exhaustive boundary audit, and certified M. Separately derive a theorem for correlated selectors with independent blocks; this addresses antithetic selection without silently reusing independence of individual frequencies.

## Correlated selectors with bounded block occupancy

PROVED on paper (round 18; exact finite moment audits recorded below). Let the potential positive frequencies be partitioned into disjoint finite blocks. The selector vectors on different blocks are independent; dependence within each block is arbitrary. In block j at most b_j frequencies are selected, put b = max_j b_j >= 1, let p_a be the marginal inclusion probabilities, and put mu=sum_a p_a=expectation|A|. For any one permissible triangular P28 window w_a, put

    v = sum_a p_a(1-p_a) w_a^2,
    B = (1/2) average_x |sum_a w_a X_a exp(iax)|.

Then, for v>0,

    M(A) >= B,
    expectation B >= v / (2 sqrt(6 b mu + 4 b^2)),
    variance B <= b/2,
    probability[B < v/(4 sqrt(6 b mu + 4 b^2))]
        <= 8 b (6 b mu + 4 b^2) / v^2.

Here M(empty)=0. If b is bounded and v >= c mu for a fixed c>0, this gives a square-root bound with probability tending to one, uniformly in the sizes of the frequency blocks and in the density. It covers independent antithetic pairs and one-point-per-cell sampling, and includes independent Bernoulli selectors as b=1. It does not cover a globally selected deterministic outcome or a single block containing all n selected points.

PROVED explicit corollary: if mu>=b and v>=c mu, then with probability at least 1-(80 b^2/c^2+b)/mu,

    M(A) >= c sqrt(|A|)/(4 sqrt(20b)).

Indeed 6bmu+4b^2<=10bmu, and independence of the blocks gives variance|A|<=bmu, hence probability[|A|>2mu]<=b/mu. If every block has a fixed selection count, so |A|=mu=n0 deterministically, the stronger bound c sqrt(n0)/(4 sqrt(10b)) holds with probability at least 1-80 b^2/(c^2 n0).

Proof. Symmetrize with an independent selector copy. For each block let Y_j(x) be its weighted Fourier difference and Q(x)=sum_j expectation|Y_j(x)|^2. Independence and symmetry give

    expectation|sum_j Y_j|^4 <= 3 Q(x)^2 + sum_j expectation|Y_j|^4.

Writing N_j for the selected count in block j, the occupancy bounds give expectation|Z_j(x)|^2<=expectation N_j^2<=b_j expectation N_j for the original block sum Z_j. Thus Q(x)<=2bmu and |Y_j(x)|<=2b. Parseval, which removes all cross-frequency covariance terms even within a block, gives average_x Q(x)=2v. Consequently the joint fourth moment is at most (6 b mu+4 b^2)2v. Holder interpolation gives the mean bound after the two symmetrization factors of 1/2. For the variance, B on real coefficient vectors is convex and 1/2-Lipschitz in Euclidean norm, by Parseval and Cauchy–Schwarz. Choose a subgradient g with squared norm at most 1/4. Resampling block j changes the coefficient vector by squared distance at most 2b_j, so convexity bounds the squared positive part of the change in B by 2b_j times the squared norm of that block of g. Block variance tensorization and exchangeability of a resampled pair give variance B <= sum_j expectation[(B-B_resampled_j)_+^2] <=2b expectation||g||^2<=b/2. Chebyshev gives the displayed probability. These arguments use independence of blocks only.

PROVED accompanying identity, for arbitrary correlated selectors: the circle average of the expected squared centered window sum is exactly v. Antithetic cancellation cannot remove this Parseval energy; it can move the energy into a thinner set of angles. Thus “hidden variance” must mean spectral concentration, rather than smaller coefficient variance.

## Forced prefixes after sparse thinning

PROVED corollary of quoted P70.2, rather than a new underlying boundary theorem. Suppose a random finite A contains [1,k] surely, expectation|A|<=N, and the expected number of selected frequencies in (k,4k) is at most delta k. No independence is assumed. For every fixed R>0,

    probability[M(A)<R sqrt(|A|)]
      <= 2delta/c0 + 4R^2 N/(c0^2 k^2).

Proof: D_1(k) is at most the number of selected tail frequencies, so Markov bounds the probability of D_1(k)>c0k/2 by 2delta/c0. On the complementary event P70.2 gives M>=c0k/2. A ratio below R then requires |A|>c0^2 k^2/(4R^2), whose probability is at most the second term, again by Markov. The same bound holds with the boundary certificate in place of M.

PROVED consequence: if delta tends to zero and N=o(k^2), this model has M/sqrt(|A|) tending to infinity in probability, already certified by the boundary. For the ideal selector model underlying the forced-thin experiments, L is of order t^(4/3), expected unforced count is t, and k is of order t^0.65. The maximum tail inclusion probability is O(t/L), so delta=O(t^(-1/3)) and N/k^2=O(t^(-0.3)). The corresponding random family therefore fails asymptotically. This does not assert that every selected rare outcome, or every fixed pseudorandom-seed sequence, satisfies the high-probability conclusion. It explains why sparse thinning destroys the smooth-tail protection of the old forced-prefix family.

## A deterministic theorem: periodic triangular Bohr tapers have a linear obstruction

PROVED on paper (round 18; ten exact finite witness checks passed). Let L be a positive multiple of 20, P>=100 an integer, q>=4L+1 an integer, and r_q(a) the centered residue modulo q. Define the genuine Boolean set

    A(L,q,P) = {1<=a<=Pq : |r_q(a)| <= L(1-a/(Pq))},
    n = |A(L,q,P)|.

Then the full W2 certificate, and hence M(A), satisfy

    -lambda_min(Cay[{0} union ±A])/2 >= 7n/6290 + 1/2.

The constant is independent of the density, the modulus, and the number of periods. In particular choose q=L^2 and P=L^2 and let L tend to infinity through multiples of 20. Then n=L^3 EXACTLY and density=1/L=n^(-1/3). In this sequence m=n/80 and the stronger bound is M>=7n/2720+1/2. This explicitly excludes that correlated nested-Bohr family; it does not exclude all moving Bohr windows.

Proof. Write h=L/20 and J=floor(P/8). Take three packets inside A:

    U = {jq+r : 1<=j<=J, -16h<=r<-14h},
    V = {jq+r : 1<=j<=J, -h<=r<h},
    W = {jq+r : 1<=j<=J, 14h<=r<16h}.

Each has m=2hJ=(L/10)J elements. Their frequencies are at most Jq+16h, hence at most 0.127Pq, and their centered residues have magnitude at most 0.8L. Thus all three packets lie in A. For any two packet elements, the magnitude of their difference is at most Jq+32h <= 0.129Pq, so the allowable residue radius for that difference is at least 0.871L. Residue differences between U and V, or V and W, have magnitude less than 0.85L. Differences inside a packet have magnitude less than 0.1L. All these distinct pairs are therefore edges. Residue differences between U and W exceed 1.4L and are less than q/2, so these pairs are never edges. There is no modular wrap in any of these tests because q>=4L+1.

Assign vector values 2 on U, -3 on V, and 2 on W. Its squared norm is 17m, and the exact adjacency quadratic form is -7m^2-17m. P9 gives M >= 7m/34+1/2. Since P>=100, J>=P/9. Thus m>=LP/90, while n<=(2L+1)P<=(41/20)LP; these imply n<=185m and give the stated bound. For the displayed sparse sequence, the same cardinality upper bound and a fixed fraction of the first P/2 periods with |r|<=L/4 give n of order LP=L^3. No limiting theorem is needed for the spectral bound.

PROVED exact cardinality in the sparse sequence. When P=q=L^2, for each 1<=r<L the two residues r and -r each contribute exactly P(1-r/L) elements, while residue 0 contributes P and residues ±L contribute none. Their sum is LP=L^3. Also L^2 is divisible by 8, so m=(L/10)(L^2/8)=n/80. This proves the stronger displayed bound and the exact density statement.

PROVED / mechanism: smooth tapering along the long coordinate does not smooth the transverse Boolean cutoff. The cutoff creates three large packets with the adjacency pattern just exhibited, which full W2 detects. An extraction of a sharp *one-dimensional* boundary in some A_d is unnecessary for this family.

Novelty scope: P9 and the negative eigenvalue of an induced three-vertex path were already in P70.7. The independent-block estimate and this explicit density-uniform packet construction were not found in the required grep of PROOFS. No outside priority claim, kernel check, or independent human review is asserted. This theorem is stronger than a numerical exclusion but is not a universal square-root theorem.

## Task 2: where the proposed structural implication still fails

PROVED obstruction to one suggested intermediate inference. A small L1/L2 ratio does not force concentration near a bounded number of frequencies at resolution 1/X, even after making gcd(A)=1. Take A=d{1,...,t} union {1}, with integers d>=2 and t>=1. Every triangular window restricts on the progression to a nonnegative unimodal sequence with maximum at most 1. Summation by parts gives, simultaneously for every H,m,

    |V_(H,m)(x)| <= 1 + min(t, 1/|sin(dx/2)|).

Since |sin(u/2)|>=|u|/pi for |u|<=pi, its circle average is at most 2+log(t). Thus the COMPLETE triangular P28 certificate is at most (2+log(t))/2, which is o(sqrt(|A|)). Yet the progression has d equal Fourier spikes and d may grow arbitrarily fast compared with t. A bounded number of arcs of width C/X captures only O(Cr/d) of its L2 energy if there are r arcs. The singleton does not change that conclusion. All this holds with gcd(A)=1.

PROVED scope: this is not a TAPER counterexample. The dilation d extracts A_d={1,...,t}, with D_d(t)=0, and full W2 sees a boundary. It demonstrates why the suggested “few frequencies, then a denominator” step requires an arithmetic description of an unbounded spike set, rather than a fixed-rank compactness assertion. The exact-mixing spike inequality quoted in NOTEBOOK applies to the positive measure built using M; no theorem here transfers arbitrary window L1 concentration to that measure with a uniform loss.

CONJECTURED surviving target TAPER-W2(c), with no M hypothesis: there is an absolute c>0 such that for every finite nonempty A, if its complete triangular P28 certificate and full W2 certificate are both less than c sqrt(n), then some d,k satisfy k>=sqrt(n)/c and D_d(k)<=c0 k/2. This is a weaker full-W2 version of the brief's TAPER target: full W2 can succeed even when its compressed star and graph-A bulk certificates fail. Both existential versions remain unproved. The finite example below excludes c=3/7; it does not exclude the existence of a smaller absolute c.

PROVED conditional implication: that single extraction lemma would imply Chowla with constant min(c,c0/(2c)), directly from P28, P9, and P70.2. This is a conditional implication, not a claimed reduction proving the extraction lemma easier than Chowla. No logarithmic-scale iteration or untracked density-dependent constant has been used.

Strategic review: discontinue the inference from small L1/L2 to finitely many absolute-scale spikes. Continue quantitative arithmetic packet extraction and the covariance/spread route. The new packet theorem uses an explicit Boolean configuration and has no loss per scale; extending its configuration extraction to arbitrary correlated tapers is the actual missing step. Repeating the same finite search at larger n would not prove that step.

## Task 3: precise implication diagram

PROVED / definitions. Let T(A) be the complete triangular Fejer P28 certificate; G(A) the full P9 certificate on W2; and Bdy(A)=max(0,max_(d,k)(c0 k-D_d(k))). Let

    C(A)=max(T(A),G(A),Bdy(A)),
    H_epsilon={A : M(A)<=epsilon sqrt(|A|)},
    C_epsilon={A : C(A)<=epsilon sqrt(|A|)}.

Then H_epsilon is contained in C_epsilon for every epsilon>0. Moreover C_epsilon implies all four quantitative necessary inequalities stated in P70.5: its T bound implies every energy-weighted window-spread bound; its G bound implies the compressed-star/triple and all graph-A bulk bounds; its boundary bound is exactly condition (iv). Thus C_epsilon is at least as restrictive as those four necessary conditions. These assertions use the same A and the same epsilon.

PROVED / logic. An absolute lower bound on C(A)/sqrt(n) would prove Chowla. An infinite family with C(A)/sqrt(n) tending to zero would refute this certificate cover, but would not by itself disprove Chowla: C<=M supplies no upper bound on M. An infinite family with certified M(A)/sqrt(n) tending to zero would disprove Chowla and would automatically defeat the cover. These two types of adversary must not be conflated.

UNKNOWN pending the inverse theorem: whether C_epsilon is empty for all sufficiently small epsilon; whether a density-independent comparison M<=constant*C is true; whether either the four original necessary conditions or the stronger C_epsilon admit an o(sqrt(n)) family. None of (a), the asymptotic version of (b), or a small-epsilon equivalence in (c) has been established by the existing programme. Calling the programme “equivalent” solely from its necessary conditions is unjustified. Calling it “inconsistent” solely from the tests is also unjustified.

### Certified finite separation: the literal reverse implication is false

PROVED / computer-assisted finite result, new certification of an already saved round 17 set. Take

    A = {1,...,11} union {13,...,27}
        union {29,30,31,34,35,37,44,45,48,50},
    n=36, X=50, epsilon=3/7, epsilon sqrt(n)=18/7.

Then

    T(A) < 1.424 < 18/7,
    G(A) < 18/7,
    Bdy(A) < 0.262 < 18/7,
    3.959921 < M(A) < 3.960017.

In particular A belongs to C_(3/7) and satisfies all four original necessary conditions with that SAME epsilon, but does not belong to H_(3/7). The same-epsilon biconditional, without a qualification about sufficiently small epsilon, is false. An absolute certificate cover with constant 3/7 also fails on this example. This does not refute a cover with a smaller constant or an asymptotic comparison with a constant loss.

PROVED / certificate details:

1. Complete P28: all 50 integer widths H=1,...,50 and all 50 potentially nonzero integer centers per width were checked with 100-bit Arb DFTs on 8192 points. At each point the supremum was enclosed from above by outward dyadic rationals. For each width let L_H=max_m sum_a a w_a. A nearest-cell quadrature bound gives

       T_H <= (1/(2G)) sum_j sup_m |V_(H,m)(2pi j/G)| + L_H pi/(4G).

   The resulting maximum upper bound is approximately 1.42320460949; the exact rational is saved. The finite reductions above cover all other widths and centers, including noninteger widths. This is an upper certificate for the COMPLETE triangular functional, not a sampled lower estimate.
2. Full W2: H is the 73-by-73 integer adjacency matrix on {0} union ±A. Every coefficient of det(xI+7H+36I) is strictly positive, checked exactly. Since the matrix is symmetric, any nonpositive eigenvalue of 7H+36I would give a nonnegative root of that polynomial, impossible. Hence H+(36/7)I is positive definite and G(A)<18/7. The 74 exact coefficients are saved in `graph_exact.json`.
3. Boundary: all relevant 37 divisors and 144 (d,k) pairs were scanned with exact rational defects and enclosing rational c0 bounds. A maximizing witness is d=15,k=3,D=0. The exhaustive upper bound is approximately 0.261619772368. The largest k which could satisfy D_d(k)<=c0k/2 is exactly 3, using both lower and upper rational c0 comparisons. Thus TAPER-W2(3/7), and the original TAPER(3/7), fail: their boundary alternative requires k>=14.
4. M, two independent methods: an Arb DFT on 32768 points plus the global second derivative bound at a global minimizer gives the displayed enclosure. Independently, the exact degree-50 Chebyshev polynomial plus 3961/1000 has Sturm variation 25 at both -1 and 1, hence no interval root, and is positive there. At t=286011/319808 its value is less than -39599/10000. This proves independently 3.9599<M<3.961. No sampled numerical minimum is used to establish the reverse counterexample.

PROVED / limits of the Task 3 verdict: option (c), read as a literal same-epsilon equivalence for every epsilon, is disproved. The choice between inconsistency below some sufficiently small absolute epsilon and an asymptotic certificate-evading family remains UNKNOWN. There is no proved reduction from small certificates to small M, and no proof that the programme is merely a circular restatement. Unrestricted P29(b) would be circular in that sense; the explicit certificates used here are demonstrably different from M.

## Adversarial tables

NUMERICAL display below. Every certificate column is divided by sqrt(n). P28 uses H=1 and floor(X/d) for d=1,2,4,8,16,32, centers spaced by max(1,floor(H/4)), and a power-of-two circle grid of size at least max(2048,16X). W2 is the FULL induced graph, not a compressed star; star and BD are also reported separately. BD uses graph A with cutoff sqrt(n). Boundary optimization is exhaustive over all d,k; raw bounds are exact rational enclosures in JSON, while normalized displayed decimals are rounded. R is an uncertified FFT/Newton estimate in this table. The complete 33-row table and individual grid records are in [adversarial_table.md](tdense18_scratch/adversarial_table.md) and [adversaries.json](tdense18_scratch/adversaries.json).

| family | n | X/n | P28 | full W2 | star | BD | boundary | R estimate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| cumulative linear | 96 | 7.167 | 0.284876 | 0.526912 | 0.305182 | 0.080563 | 0.017801 | 2.028498 |
| cumulative linear | 768 | 14.928 | 0.286877 | 0.431299 | 0.225725 | 0.044668 | 0.009440 | 2.580128 |
| antithetic | 768 | 14.988 | 0.285217 | 0.409405 | 0.227022 | 0.044386 | 0.012587 | 2.471909 |
| Thue–Morse | 768 | 14.988 | 0.279040 | 0.403196 | 0.226012 | 0.044578 | 0.009440 | 2.465290 |
| random antithetic pairs | 768 | 14.865 | 0.275563 | 0.407023 | 0.225738 | 0.044648 | 0.006433 | 3.111121 |
| nested Bohr, rank 1 | 769 | 14.956 | 0.079401 | 2.306003 | 0.032060 | 0.045956 | 0.066040 | 6.048725 |
| nested Bohr, rank 2 | 764 | 14.937 | 0.127769 | 1.445513 | 0.040565 | 0.056465 | 0.018930 | 4.065029 |
| dilation union | 735 | 22.782 | 0.244167 | 0.539462 | 0.127374 | 0.065129 | 0.012867 | 2.423123 |
| tapered Singer–Bu, q=127 | 756 | 54.254 | 0.245348 | 0.215125 | 0.193679 | 0.042482 | 0.009515 | 0.766594 |
| forced prefix, sparse thinning | 840 | 13.251 | 0.268865 | 0.480792 | 0.156345 | 0.059348 | 0.009879 | 2.559600 |
| prior finite optimizer, complete P28 quadrature | 36 | 1.389 | 0.230299 | 0.428184 | 0.125422 | 0.114192 | 0.043603 | 0.659987 |

NUMERICAL / mechanism distinctions: cumulative and antithetic variants retain a visible spread contribution in these tests; no density-uniform deterministic theorem for all such roundings is claimed. Nested Bohr variants trade smaller spread for larger W2; the packet theorem proves this mechanism for the explicitly stated periodic class, not for every tested shrinking rational window. Dilation unions do not perfectly isolate components under divisibility filters, and retain substantial W2 here. Tapered Singer–Bu is the best finite certificate adversary but still has a spread contribution around 0.245sqrt(n); these three rows do not prove a positive limiting constant. Sparse forced prefixes eventually create the sharp boundary under the marginal hypotheses proved above.

PROVED / six representative all-circle enclosures, displayed with conservative outward bounds. These support finite statements only; exact rationals and finer outward decimal tables are in [representative_minima.json](tdense18_scratch/representative_minima.json) and [certified_minima_table.md](tdense18_scratch/certified_minima_table.md).

| family | n | X | certified M interval |
|---|---:|---:|---:|
| cumulative linear | 96 | 688 | [19.875,19.882] |
| antithetic | 96 | 696 | [24.411,24.421] |
| nested Bohr, rank 1 | 96 | 699 | [22.450,22.461] |
| dilation union | 95 | 1938 | [20.792,20.805] |
| tapered Singer–Bu | 72 | 2016 | [7.427,7.444] |
| forced prefix, sparse thinning | 107 | 641 | [19.516,19.522] |

## Verification, novelty, and strategic handoff

PROVED / exact finite checks: all 255 nonempty subsets of [1,8] cross-check the boundary pruning against a direct independent d,k enumeration; 283 coefficient checks verify the H>=X reduction; 3648 rational coefficient checks verify the noninteger-width interpolation; two correlated block models each enumerate 27 selector states and all 729 symmetrized pairs for exact second/fourth moments; ten packet cases verify every possible packet difference, including n=512000 and density=1/80. The checks corroborate the written proofs and are not substitutes for their universal arguments. The final audit verifies all 33 saved sets, hashes, graph coefficients, finite M certificates, and exact threshold comparisons.

Quoted versus new: P9, P28, P70.2, and the round 17 independent-selector argument are quoted inputs. The bounded-occupancy block extension, the explicit sparse Bohr packet family and its linear W2 bound, the complete finite reductions and complete certificate audit, and the certified same-epsilon reverse counterexample are new work in this round. The set used for the last result itself was found in round 17. The forced-prefix statement is an elementary new corollary of the quoted boundary theorem. The project PROOFS grep preceded novelty statements. No external priority or kernel verification is claimed.

HEURISTIC strategic recommendation: continue only with a joint inverse theorem that uses low window spread AND low full-W2 spectrum. The concrete target is to extract either a large three-packet configuration or a sharp arithmetic boundary, with constants independent of rank, density, and the number of scales. Low L1 alone cannot bound the number of spikes. A selected high-rank taper whose clocks change before any modulus repeats for sqrt(n) steps is a more discriminating next construction test than a larger version of the periodic examples excluded here.

UNKNOWN / exact remaining gap: no theorem yet produces either packet structure or a sharp boundary for every Boolean set with small complete P28 and small W2. The block theorem leaves globally selected correlated outcomes untouched. The finite separation does not settle epsilon tending to zero. No proof of Chowla, no asymptotic certificate-evading family, and no equivalence reduction is claimed.

Reproducibility: [manifest.json](tdense18_scratch/manifest.json) gives VM-only commands, source/data hashes, and the recorded retries; [verification.json](tdense18_scratch/verification.json), [reverse_separation.json](tdense18_scratch/reverse_separation.json), [sturm_independent.json](tdense18_scratch/sturm_independent.json), and [final_audit.json](tdense18_scratch/final_audit.json) contain the exact evidence. Environment: Python 3.12.3, NumPy 2.5.4, SciPy 1.18.1, python-flint 0.9.0. No unattended process is left running.
