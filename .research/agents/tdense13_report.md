# Round 13 research report

## Current checkpoint

PROVED round-13 results: R13-PK refutes every universal subquadratic PK bound; R13-C is an explicit relaxation retaining the exact convolution identity on the first J=o(q^(1/3)) frequencies along the peak orbit while staying at exponent 1/3; R13-M1 identifies cubic count integrality as the literal R12 fake's first failure; R13-M2 repairs every fixed order of scalar moment, integer-count and Newton congruence tests. No unconditional cyclic exponent above 1/3 and no new unconditional dense endpoint are claimed. Task 1 is delivered through the permitted precise-barrier alternative. Task 2's bounded implementations fail, with all 20 retained dips independently Arb-enclosed.

PROVED scope and conventions: this report follows `tdense13_brief.md`. Every computation ran through `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4`; no subagents, commits, LaTeX, or edits to top-level research Markdown files were made. Existing unrelated workspace changes were preserved. The report and `tdense13_scratch/` hold this round's work.

PROVED target: for every odd prime q admitting a symmetric set B excluding 0 with |B|=(q−1)/2, write λ(γ)=sum over c in B of exp(2πiγc/q), K=−min over γ≠0 of λ(γ), and Λ=max over γ≠0 of λ(γ). This convention is feasible only for q≡1 mod 4; q≡3 mod 4 requires toggling 0 or changing cardinality by one. Seek a proved quantitative uniformity statement QU(β), a conditional statement surviving the specified fakes, or an explicit partial-convolution relaxation barrier. No exponent improvement is claimed at this checkpoint.

PROVED quoted project state: P61–P64, NOTEBOOK continuations 15–17, E41, E82, and the round-12 report were audited as inputs. P63's unconditional dense endpoint is C<2000/259. P61's second-order reach and R12-S are quoted results, not discoveries of this round.

HEURISTIC initial research frontier (retained to show which targets were tested):

| Known | Exact gap | Candidate mechanism | Discriminating test |
|---|---|---|---|
| Exact binary convolution at every nonzero frequency | Quantitative gain from several frequencies | Positive mass must meet threshold negatives at many translates | Derive a weighted mixed-pair deficit identity and test saturation |
| PK is stronger than uniformity | Whether genuine half-sets refute PK | Symmetric random rounding of a positive Fourier profile | Prove concentration and certify finite cyclic spectra |
| R12-S matches selected scalar constraints | Higher additive-count integrality and positivity | Integral spectra with prescribed first two moments | Exact power-sum divisibility and all-order argument |
| Weighted P61 escapes attain the second-order reach | Binary realization | Near-interval, Paley-scale, and spectral-error-diffusion rounding | VM FFT/refinement, with Arb point values for every dip |

PROVED input audit completed: read CLAUDE.md, P61–P64, NOTEBOOK continuations 15–17, E41, E82's profile definition, and the round-12 report. The round brief overrides CLAUDE.md's generic commit and top-level-record instructions. No applicable AGENTS.md was found in the workspace or its ancestors. VM dependency check: Python 3.12.3, NumPy 2.5.4, SciPy 1.18.1, Gurobi 13.0.3, python-flint 0.9.0.

NUMERICAL completed work: `cyclic_probe.py` tested cosine-profile rounding and Gurobi trade-offs for q=17,37,61,89,101,109 on the prescribed VM. The input thresholds for q≤89 are independently evaluated E41 witnesses; q=101,109 K-min searches were time-limited and their actual bounds/status are recorded below. Arb certifies every spectrum of a reported trade-off incumbent. Gurobi optimality with floating cosine coefficients is not an exact algebraic optimality certificate. The complete curves at q=17,37 received separate exhaustive interval-enclosure proofs.

## PK is false: a genuine binary family

PROVED R13-PK. Fix any ε with 0<ε<1/2. For every sufficiently large prime q≡1 mod 4 there exists B=−B⊂Z_q, 0∉B, |B|=(q−1)/2, with

    λ(1)=εq/2+O(√(q log q)),
    λ(γ)≥−O(√(q log q)) for every γ≠0.

The constants may depend on ε. Consequently, for every fixed η>0 and C>0, the assertion Λ≤C K^(2−η) fails for some such B. This is an unconditional refutation of PK, rather than a relaxation example.

PROVED proof. For a=1,…,(q−1)/2 choose independent bits Y_a with means p_a=1/2+ε cos(2πa/q), and include both ±a when Y_a=1. Extend the mean profile to c=0 by the same formula. Discrete orthogonality gives, for γ≠0, expected λ(γ)=εq/2−(1/2+ε) at γ=±1 and −(1/2+ε) at every other γ. The expected number of selected pairs is (q−1)/4−ε/2.

For completeness, the bounded-variable exponential estimate used here follows by convexity of exp on each variable's range: a centred variable of range length d has exponential moment at most exp(t²d²/8). Multiply these estimates for independent variables, then optimize t. Each Fourier sum has range lengths at most 2 per pair, so the probability of an error exceeding u is at most 2 exp(−u²/(q−1)). The pair count has the same or better estimate. A union bound, with u=3√(q log q), supplies one outcome where every nonzero Fourier sum and the count have that error bound. Flip at most u+1 pairs to obtain exactly (q−1)/4 pairs; this changes every λ by at most 2u+2. Thus λ(1)=εq/2+O(√(q log q)) and K=O(√(q log q)), as claimed. Since K>0 (the nonzero Fourier trace is negative), Λ/K^(2−η) tends to infinity for 0<η≤2; η>2 is immediate from the same bounds and K≥1/2. Infinitely many primes q≡1 mod 4 follow from the elementary prime-divisor argument for (2p₁⋯p_r)²+1.

PROVED compatibility with QU: these examples cannot falsify a small-δ assertion. The quoted exact second-order peak inequality Λ²≤Λ+2K(K−1/2)(q−1), together with λ(1)∼εq/2, forces K≥(ε/(2√2)+o(1))√q. Their normalized negative threshold stays bounded away from zero.

PROVED bookkeeping correction/check. If QU(β) holds, combine Λ≥((q+1)/4−K²)/(K−1/2) with Λ≤Cq(K/√q)^β in the regime K≤δ₀√q, shrinking δ₀<1/4 if necessary. This yields K^(β+1)≥c q^(β/2) and hence K≥c' q^(β/(2β+2))=c' q^(1/2−1/(2(β+1))). Outside that regime the square-root lower bound already dominates. Thus β=1 gives 1/4 and β=2 gives 1/3. The notation β=∞ is a limiting aspiration, not a literal finite-constant theorem.

## Main result: an exact partial-convolution barrier

PROVED R13-C (paper proof; independent finite support checks passed). Let J(q) be any positive-integer function with J(q)=o(q^(1/3)). For every sufficiently large odd prime q there is a real even array λ on Z_q satisfying all the following:

- λ(0)=(q−1)/2, sum λ=0, and sum λ²=q(q−1)/2, exactly;
- −min over γ≠0 of λ(γ)=q^(1/3)/2;
- max over γ≠0 of λ(γ)=λ(1)=2q^(2/3)−q^(1/3)/2;
- sum over β≠0,γ of λ(β)λ(γ−β)=λ(γ), exactly, for every γ in ±{1,…,J(q)}.

PROVED consequence: this explicit relaxation, including the convolution identity along an increasing initial segment of the peak orbit, is consistent with exponent 1/3. In this relaxation δ=K/√q=(1/2)q^(−1/6) and Λ∼2q^(2/3), so QU(β) fails for every β>2. This is the requested barrier deliverable. The arrays need not be binary Fourier transforms. The assertion does not preserve the identity outside the specified segment, all additive-count integrality conditions, or every inequality that could be deduced using the missing equations.

PROVED construction and full proof. Write u=q^(1/3), H=4u², ℓ=ceil(u), and C=q u(u−2). We construct a nonnegative even h and then set z=h−u. Impose h(0)=u−1, h(±1)=H, and require

    sum h=q(u−1),     sum h²=q²+q u(u−2).

These imply sum z=−q, sum z²=q², z(0)=−1. Also z*z(γ)=h*h(γ)−C, where convolution is the unnormalized cyclic sum. Here h is even, so h*h(γ) equals its autocorrelation at displacement γ.

The already placed three sites contribute R₁=2(u−1)H at displacement 1, R₂=H² at displacement 2, and R_d=0 at every d≥3. Set R₂=0 if J=1 is irrelevant; for d=1,…,J the intended residual is C−R_d>0 for all sufficiently large q. For each d choose ℓ disjoint positive two-site clusters {t,t+d} and their reflected clusters {−t,−t−d}. Put the same amplitude

    a_d=sqrt((C−R_d)/(2ℓ))

on their four sites. Require that different clusters, the three original sites, and the eventual repair sites are at cyclic distances greater than J from one another. Within one pair, the two reflected edges contribute exactly 2a_d² to the autocorrelation at d; there are no other contributions at displacements 1,…,J. Thus h*h(d)=R_d+2ℓ a_d²=C for every d in the required segment.

The cluster sites use mass 4ℓ sum a_d=O(Jq) and energy 4ℓ sum a_d²=O(Jq^(5/3)). The original sites use mass O(q^(2/3)) and energy O(q^(4/3)). Since J=o(q^(1/3)), the remaining mass T and energy E obey

    T∼q^(4/3),     E∼q²,     T²/E∼q^(2/3).

They are positive. Choose m=4 ceil(3T²/(8E)), μ=T/m, and v=E/m−μ². For sufficiently large q,

    (3/2)T²/E≤m≤2T²/E,
    0≤v≤μ²,     μ+sqrt(v)≤2μ≤(4/3)E/T<4q^(2/3)=H.

Put μ+sqrt(v) on m/2 repair sites and μ−sqrt(v) on m/2 repair sites, each group itself a union of reflected pairs. They supply mass T and energy E exactly and stay nonnegative. The cluster amplitudes also satisfy a_d∼q^(2/3)/sqrt(2)<H, uniformly in d. Consequently H is the maximum h and occurs at ±1.

PROVED spacing and capacity detail. Place the positive clusters one after another, using a block of length 3J+3 per cluster, starting beyond 4J+10. A pair at {t,t+d} leaves a gap greater than J before the next cluster. Then place the positive repair sites with spacing 2J+2 and reflect all these sites across 0. The used half-line length is

    O(J²ℓ+Jm)=O(J²q^(1/3)+Jq^(2/3))=o(q).

Thus all positive sites lie below q/2−2J for sufficiently large q. This also separates every reflected pair of different clusters across the midpoint; the initial gap separates them across 0. The only near-0 sites are the three explicitly accounted for. Hence there are no wraparound correlations at the specified displacements. The total support is o(q), so some offzero sites have h=0 and min z=−u exactly.

Finally define λ(0)=(q−1)/2 and λ(γ)=z(γ)/2 for γ≠0. Equivalently z=2λ−qδ₀. The trace and energy above give the asserted trace and Parseval identities for λ. At every required nonzero γ, z*z(γ)=0 is equivalent to λ*λ(γ)=qλ(γ). Removing the β=0,γ contributions, whose sum is (q−1)λ(γ), proves exactly the asserted off-zero equation. Evenness supplies the negative γ equations. This completes the proof.

PROVED adversarial scope check. The construction has a genuine peak at 1 and preserves the γ=2 equation containing its square; it does not evade that equation by moving the peak outside the tested orbit. Every fixed number of equations is covered, and J can grow as any o(q^(1/3)) function. It also obeys the scalar second-order peak bound and the R12 scalar cubic peak bound for sufficiently large q. It is far from solving every equation: put s=2J+2, the spacing of the repair sites, and a=μ+sqrt(v), b=μ−sqrt(v). The repair sites alone contribute

    E−2(a²+b²−ab)=q²(1+o(1))

to h*h(s). This follows by counting the adjacent high-high and low-low pairs and the single high-low boundary on each reflected side. All other contributions are nonnegative. Cauchy–Schwarz gives h*h(s)≤sum h²=q²(1+o(1)), while C=o(q²). Hence z*z(s)=q²(1+o(1)), and the λ offzero identity has a defect q²(1+o(1))/4 at this untested frequency. The missing global equations therefore detect an explicit, maximal-scale defect; this is not an approximate solution of all q equations.

PROVED exact mixed-pair deficit identity (a diagnostic, not an exponent improvement). Extend P,N by zero at frequency 0 and write S=sum P, D_γ=sum over β of P(β)[K−N(γ−β)]. Every term in D_γ is nonnegative. At every γ where binary convolution holds,

    (P*P)(γ)+(N*N)(γ)+2D_γ=λ(γ)+2KS.

This follows by expanding λ=P−N on nonzero indices and substituting P*N=KS−D_γ. Thus the candidate pairing incompatibility must use the arrangement of deficits at additional frequencies. R13-C proves that the first o(q^(1/3)) peak-orbit equations alone cannot establish β>2 in the stated relaxation.

HEURISTIC strategic review after the PK obstruction and partial-convolution construction: discontinue universal PK and a fixed-J incompatibility argument. Continue the full-frequency incidence/additive-energy approach and additive-count arithmetic; both use information explicitly absent from R13-C. The construction side was tested separately below. No unconditional exponent improvement or new dense endpoint is claimed.

PROVED finite verification checkpoint: the sparse-support verification passed after repairing a python-flint/Fraction conversion. It counted every correlation monomial exactly at q=200³,400³,800³ with J=3,5,8, respectively, and checked mass, energy, level positivity and capacity with 180-bit Arb. These q are explicitly composite integer cubes, used for independently readable support checks; the paper argument above covers large primes and does not infer primality from these tests. The largest support has 947079 sites. The first exhaustive-curve audit also encountered a python-flint integer-conversion issue, repaired with exact integer extraction; both curve enumerations then passed.

PROVED audit-discovered implementation correction: the first Gurobi profile-rounding call made its seed counts with the default block length 256 and subsequently constrained 16-site blocks to those seed counts. Its two rows therefore did not follow the required 16-block E82 profile. The independent profile-discrepancy assertion caught this. They are retained in `binary_results_initial.jsonl` and `gurobi_round_initial_X128.npz`, `gurobi_round_initial_X256.npz`; their original R values were 1.072402 and 1.178721. The corrected solver constructs its seed with B=16 explicitly; the rerun passed the profile-count audit and produced R≈0.901275 and 1.180140. The other 18 rows passed the profile-count audit before this failure. No proof or successful construction depended on the incorrect rows.

## Moment test: the literal R12 fake fails, but every fixed order is repairable

PROVED R13-M1. The literal R12-S fake already fails the integer additive-count condition at k=3, before k=4. This does not contradict R12-S: that result imposed a cubic peak inequality, not cubic count integrality.

PROVED calculation. Use R12-S's sign normalization z=h−u with u³=q, m its multiple-of-four support count, and a=q−1. The nonzero h mass is T=a(u−1) and its squared mass is E=a(u²−2u+q+1). The offzero third power sum of z is

    −2T³/m²+3TE/m−3uE+3Tu²−a u³.

Reduce modulo u³=q. The coefficient of u² is exactly

    3a(m−a)(m−2a)/m².

It is nonzero because 0<m<a for sufficiently large q. The coefficient of u is −3a(m−a)((q+1)m−2a)/m². Since q is prime, 1,u,u² are linearly independent over Q. The third power sum is therefore irrational. For an actual half-set, the integer quantity qT₃(B)−((q−1)/2)³ must equal one eighth of that sum. The literal fake fails this constraint.

PROVED R13-M2 (fixed-order scalar arithmetic barrier). Fix any integer r≥3. For every sufficiently large prime q≡1 mod 4, there is a real even scalar spectral array λ on Z_q with λ(0)=(q−1)/2, exact trace and Parseval as above, K=q^(1/3)/2 and Λ asymptotic to a positive constant times q^(2/3), such that:

- for every k≥0, the shifted moments sum over γ≠0 of (λ(γ)+K)^k are nonnegative and every associated moment/Hankel positivity inequality holds;
- for every 1≤k≤r, T_k=[((q−1)/2)^k+sum over γ≠0 of λ(γ)^k]/q is an integer;
- for 2≤k≤r, 0≤T_k≤((q−1)/2)^(k−1), with T₂=(q−1)/2;
- the first r power sums satisfy all Newton integrality congruences of an algebraic-integer characteristic polynomial. One can also preserve the residue of each T_k modulo any prescribed fixed integer.

The theorem does not assert that the counts are simultaneously realizable by a set, that the full q−1 degree characteristic polynomial is integral, or that the array is a Galois orbit. It establishes that no bounded order of these scalar moment, integrality and fixed-divisibility tests can improve the exponent in this relaxation.

PROVED proof. Start with the same nonnegative-h mass-and-energy construction used in R13-C, omitting all dedicated convolution clusters. Put h(0)=u−1 and put h=c_j q^(2/3) on r reflected pairs, where c_j=2+j/(r+1), 1≤j≤r, are distinct fixed numbers in (2,3). The remaining positive mass T∼q^(4/3) and energy E∼q² are filled on m=4 ceil(3T²/(8E)) other sites with μ±sqrt(v) as above. These values are nonnegative and less than 2q^(2/3) for large q. Set z=h−u and λ as before. There are unused sites at λ=−u/2; the first two moments are exact.

Let H=q^(2/3)/2 and x_j=λ_j/H=c_j−q^(−1/3) for the r distinguished pairs. Hold every other spectral entry fixed. The map from x=(x₁,…,x_r) to their normalized power sums has components F_k(x)=2 sum_j x_j^k, 1≤k≤r. Its Jacobian has entries 2k x_j^(k−1) and determinant

    2^r r! product over i<j of (x_j−x_i),

which is nonzero and bounded away from zero for fixed r. These x approach a fixed interior vector of distinct positive values. The inverse-function theorem therefore gives a neighborhood and inverse Lipschitz constant depending only on r, uniformly for large q.

Choose a genuine reference half-set B₀ at the same q, for example the first (q−1)/4 reflected nonzero pairs, and let T_k⁰ be its integer additive counts. Set L=r!, or a multiple of r! and any additional desired fixed modulus. For k=3,…,r choose the nearest number T_k⁰+L t_k, t_k an integer, to the provisional real count T_k. Keep k=1,2 unchanged. The required unnormalized power-sum changes have absolute value at most qL/2. After normalization by H^k, all changes are O_r(q/H³)=O_r(q^(−1)); the first two changes are zero. The uniform inverse-function theorem supplies a change x_j by O_r(q^(−1)), equivalently λ_j by O_r(q^(−1/3)), realizing all the target moments exactly. The entries remain positive, separated, of the stated scale, and above the unchanged floor −K. Symmetric pairs preserve evenness.

For every k≤r the resulting power sums are congruent modulo r! to the reference half-set's power sums. Newton's expression for the k-th elementary symmetric coefficient is an integer-coefficient polynomial in the first k power sums divided by k!. Consequently those coefficients are integers too. This proves the claimed finite integrality congruences, rather than merely the separate integrality of the power sums.

Finally put b=(q−1)/2 and L_max=max over γ≠0 of |λ(γ)|=O_r(q^(2/3)). The offzero squared sum is (q²−1)/4. For every k≥3,

    |sum λ(γ)^k|≤L_max^(k−2)(q²−1)/4.

Since L_max/b tends to zero and ((q²−1)/4)/b² tends to 1, the right side is at most b^k/2, uniformly over all k≥3, for sufficiently large q. Thus 0<T_k< b^(k−1) whenever its integrality was imposed. Shifted moment positivity and all Hankel inequalities hold automatically because λ+K≥0 is an actual finite atomic measure. This completes the proof.

PROVED distinction: R13-M2 repairs each fixed order with a threshold depending on r. It does not handle r growing with q or impose all arithmetic moments simultaneously. In particular it does not establish a barrier to the full Galois-orbit condition. This is the exact remaining scalar-arithmetic gap. A moment LP retaining only real positivity cannot remove these examples; no LP/SDP computation is needed for that redundant relaxation.

## Other attempted gains, and their exact failure points

PROVED cubic positive-convolution calculation. Let F=max(λ,0) on the full dual group, including F(0)=(q−1)/2, and let N=max(−λ,0). Since b(0)=0, sum F=sum N≤qK and sum |λ|≤2qK. Three-fold telescoping and the elementary convolution inequality max|a*c|≤max|a| sum|c| give

    max |F*F*F−λ*λ*λ|≤7q²K³.

For a peak λ(1)=Λ>0, the nonnegative array G=F−Λδ₁ satisfies

    0≤G*G*G(1)=F*F*F(1)−3Λ(F*F)(0)+3Λ³.

The final single-delta cubic term vanishes for odd q, because 3≠1 mod q. Also λ*λ*λ=q²λ and (F*F)(0)≥q(q−1)/2−qK². Hence

    Λ[q²/2−3q/2−3qK²−3Λ²]≤7q²K³.

In the hypothetical K=o(√q) regime, R12-H gives Λ=o(q), so Λ=O(K³). Combined with the peak lower bound this recovers only K≥c q^(1/4). This failed attempt is retained: the cubic truncation error loses K³. It does not provide a new proof of QU(2). The source check of Sanders v2 confirms its 1/3 statement and full-convolution/Boolean-spectrum mechanism, but I did not derive a self-contained new proof of that strength.

PROVED large-positive-spectrum incidence bound. For S={γ≠0:λ(γ)≥t}, the exact offzero identity gives t² r_(S+S)(γ)≤Λ+2K sum P for γ≠0. At t=q/(4K), K≥1, Λ≤q/2 and sum P≤qK imply r_(S+S)(γ)≤40K⁴/q (an explicit safe constant; the asymptotic leading constant is 32). A set of size of order K² has average representation count of order K⁴/q. Thus this bound alone does not contradict the q^(1/3) scale. No Chang/Bohr structural conclusion beyond this incidence estimate was established.

PROVED spike audit of the kurtosis route. With normalized inverse transforms P̌(c)=q^(−1)sum P(γ)exp(2πiγc/q), P̌(0)≤K. The c=0 term in its Haar fourth moment can be as large as K⁴/q. At K=q^(1/3) this grows, instead of vanishing. Removing that term invalidates the universal 3/2 kurtosis inequality: P63.5 supplies the explicit Paley counterexample. Also Parseval gives average |Ň|²≤K²/q while the available sup bound remains max |Ň|≤K. Small L² correction permits the exceptional point and does not justify an offzero sup bound. Neither subtracting the spike nor replacing the sup estimate by an unproved random-cancellation claim supplies a gain here.

PROVED source-verified quoted statement: [Sanders, Chowla's cosine problem, v2, 14 October 2010](https://arxiv.org/pdf/0807.5104v2), Theorem 1.2 and the following sentence, gives the exponent 1/3 for symmetric half-sets with the (q+1)/2 convention. Sections 3–4 use Boolean convolution identities, positive spectral truncation, and a subgroup-or-intermediate-spectrum alternative. This is quoted context; R13-PK, R13-C and R13-M2 above are independent derivations. No literature-priority claim is made.

## Binary probes: results checkpoint

NUMERICAL completed scope: X=4096,65536,1048576 for Paley local rankings at q near X^(1/2), X^(2/3), X; dilated interval rankings at q near X^(1/2), X; and 64-mode sequential spectral error diffusion. Gurobi rounding was run at X=128,256. Every construction has exact rounded E82 counts on fixed blocks, with cumulative count discrepancy at block boundaries at most 1/2. The block profile uses the largest-D N=320 E82 row, its normalized autocorrelation w, and p=(1−sqrt(1−w²))/2. Its front limit is p(0)=1/2. The actual sets are stored as compressed integer arrays; actual maximum frequencies are also recorded, since X is an allowed cap, not necessarily max A.

PROVED certificate scope: every row has a 180-bit Arb enclosure at an exact rational phase, independently re-evaluated at 220 bits, proving a lower bound on M and hence excluding a good construction. The audit also enclosed R itself with Arb square roots and proved R>3/5 for every retained set. The reported M estimates use FFT oversampling of at least 16(X+1) points and bounded local refinement around the 16 lowest grid samples. They are not all-x upper bounds. No row reached R<0.56, so the all-x certification trigger did not arise.

NUMERICAL summary table (M and R estimates; each dip separately Arb-certified):

| Family | X | n | M estimate | R estimate | M/√X | Certificate |
|---|---:|---:|---:|---:|---:|---|
| Paley, θ=1/2 | 4096 | 478 | 212.373704 | 9.713747 | 3.318339 | Arb point |
| Paley, θ=1/2 | 65536 | 7646 | 1917.975305 | 21.934405 | 7.492091 | Arb point |
| Paley, θ=1/2 | 1048576 | 122342 | 18044.040137 | 51.587680 | 17.621133 | Arb point |
| Paley, θ=2/3 | 4096 | 478 | 118.522056 | 5.421073 | 1.851907 | Arb point |
| Paley, θ=2/3 | 65536 | 7646 | 934.648532 | 10.688855 | 3.650971 | Arb point |
| Paley, θ=2/3 | 1048576 | 122342 | 6509.103508 | 18.609444 | 6.356546 | Arb point |
| Paley, θ=1 | 4096 | 478 | 44.906131 | 2.053959 | 0.701658 | Arb point |
| Paley, θ=1 | 65536 | 7646 | 221.669182 | 2.535060 | 0.865895 | Arb point |
| Paley, θ=1 | 1048576 | 122342 | 1024.699627 | 2.929603 | 1.000683 | Arb point |
| Dilated near-interval, θ=1/2 | 4096 | 478 | 102.787438 | 4.701388 | 1.606054 | Arb point |
| Dilated near-interval, θ=1/2 | 65536 | 7646 | 1585.431078 | 18.131353 | 6.193090 | Arb point |
| Dilated near-interval, θ=1/2 | 1048576 | 122342 | 15060.239939 | 43.057033 | 14.707266 | Arb point |
| Dilated near-interval, θ=1 | 4096 | 478 | 160.431879 | 7.337983 | 2.506748 | Arb point |
| Dilated near-interval, θ=1 | 65536 | 7646 | 3061.322043 | 35.009981 | 11.958289 | Arb point |
| Dilated near-interval, θ=1 | 1048576 | 122342 | 49528.643630 | 141.601759 | 48.367816 | Arb point |
| Spectral error diffusion | 4096 | 478 | 223.632252 | 10.228701 | 3.494254 | Arb point |
| Spectral error diffusion | 65536 | 7646 | 3717.623151 | 42.515591 | 14.521965 | Arb point |
| Spectral error diffusion | 1048576 | 122342 | 61617.486234 | 176.163605 | 60.173326 | Arb point |
| Gurobi profile rounding, corrected B=16 | 128 | 15 | 3.490621 | 0.901275 | 0.308530 | Arb point; MILP time limit |
| Gurobi profile rounding, corrected B=16 | 256 | 30 | 6.463891 | 1.180140 | 0.403993 | Arb point; MILP time limit |

HEURISTIC kill decision, limited to these implementations: all sampled size sequences have R>0.6 and increasing estimated R. Stop these fixed-block laws rather than scaling them further. The q=o(X) texture dips occur close to cyclic roots and reflect the amplified local negative spectrum. The θ=1 interval and diffusion families instead show a fixed-block comb artifact: minimizing a finite collection of running spectral errors does not control untracked modes. The completed audit measured the rational modes and separated the smooth profile from the residual at each dip. These observations do not exclude optimized near-interval tails or all forms of spectral error diffusion.

## Cyclic trade-off data and exact finite curves

PROVED exact finite curves: an independent exhaustive search enumerated all 70 symmetric half-sets at q=17 and all 48620 at q=37, reduced to 10 and 2704 dilation orbits. Each 2cos(2πa/q) was enclosed with Arb and then enclosed between integers divided by 2^100. All subsequent spectral sums and interval comparisons used exact integers. Threshold intervals for different orbits were disjoint; domination comparisons were strict. The pairs stored in `audit_results.json` define the exact algebraic threshold and peak, and the following decimal values are approximations to them. The maximal peak is constant between consecutive thresholds, right-continuous at each threshold, and infeasible below the first one.

| q | κ threshold, approximate | Λ_max, approximate | Peak-aligned pair representatives |
|---:|---:|---:|---|
| 17 | 2.561552812809 | 1.561552812809 | 1,2,4,8 |
| 17 | 2.827064740717 | 4.418975723730 | 1,2,3,4 |
| 37 | 3.367213311135 | 10.105610182931 | 1,2,3,4,5,6,7,9,10 |
| 37 | 3.936706943203 | 10.442086316530 | 1,2,3,4,5,6,7,8,10 |
| 37 | 4.936455538258 | 10.781004362416 | 1,2,3,4,5,6,7,8,9 |

NUMERICAL Gurobi scan: κ=factor×K_base+2e−8, with factors 1,1.025,1.075,1.15,1.35,1.7. Every objective below is the peak at frequency 1 of the stored binary incumbent; every incumbent has an Arb-certified feasible spectrum. Except for the two explicitly bounded q=89 entries, Gurobi returned OPTIMAL for the floating-coefficient model. This is a numerical solver conclusion at q≥61, not an interval-certified exhaustive optimality proof.

| q | K_base | f=1 | f=1.025 | f=1.075 | f=1.15 | f=1.35 | f=1.7 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 2.561552813 | 1.561553 | 1.561553 | 1.561553 | 4.418976 | 4.418976 | 4.418976 |
| 37 | 3.367213311 | 10.105610 | 10.105610 | 10.105610 | 10.105610 | 10.442086 | 10.781004 |
| 61 | 4.081699308 | 7.084233 | 14.353842 | 14.353842 | 17.397434 | 17.614098 | 18.213202 |
| 89 | 4.630072322 | [13.394879,21.006159] | [13.394879,21.358383] | 24.118553 | 25.237879 | 25.795467 | 26.356518 |
| 101 | 5.182140773 | 26.887157 | 28.263135 | 28.571549 | 28.947109 | 29.428008 | 30.046927 |
| 109 | 5.488450340 | 30.403629 | 30.521421 | 31.188632 | 31.416191 | 31.866473 | 32.552111 |

NUMERICAL interpretation and limitations. The curve is a finite staircase, rather than a smooth power law. At q=17 the first substantial increase in the negative allowance changes the optimal set from Paley to an interval. At q=61 an allowance of only 2.5% doubles the attainable peak. These finite-size jumps do not test δ→0. For q=101,109, K_base is a time-limited incumbent threshold, not a proved minimum: the K-min solver lower bounds were respectively 2.324406 and 2.190548. Their scans start at those incumbent thresholds. At q=89 the two low-threshold scans timed out after eight seconds; the displayed brackets are incumbent and solver upper bound. These points are not reported as solved optima.

PROVED input audit detail: the q=89 E41 pair list has K in an Arb interval around 4.630072322354611, whereas its text line says 4.630071582. This discrepancy exceeds mere rounding to the printed digits. I use the independently evaluated threshold of the actual pair list throughout this round and do not certify the printed E41 scalar. Also the q=61 pair list has maximal eigenvalue about 7.08423; the broad quoted description Λ≈0.27q at K_min is not uniform across all the supplied small-q witnesses. The original E41 files were not edited.

NUMERICAL PK illustration (the theorem R13-PK, rather than this finite table, is the refutation). Symmetric cosine-profile rounding with ε=0.2 and the seeds in `cyclic_profiles.json` gave:

| q | K, approximate | Λ, approximate | Certificate status |
|---:|---:|---:|---|
| 257 | 20.138957 | 28.804507 | Every nonzero eigenvalue Arb-enclosed |
| 1021 | 56.284884 | 77.803959 | Every nonzero eigenvalue Arb-enclosed |
| 4093 | 138.689391 | 372.890636 | FFT numerical |
| 16381 | 252.359787 | 1626.223389 | FFT numerical |
| 65537 | 521.275882 | 6489.005048 | FFT numerical |

PROVED feasibility: each stored set has exactly (q−1)/2 elements, excludes 0, and is invariant under negation. The proof controls all sufficiently large q≡1 mod 4 and every fixed η>0; no finite-ratio extrapolation is used.

## Binary failure mechanism in P61–P64 language

NUMERICAL discriminating evidence at X=1048576: the smooth profile's value at the certified dip lies between −0.250 and −0.197 for all six large-X laws. The residual contributes essentially the entire dip: about −18043.7905 (Paley θ=1/2), −6508.8537 (Paley θ=2/3), −1024.4498 (Paley θ=1), −15059.9956 (near-interval θ=1/2), −49528.4461 (near-interval θ=1), and −61617.2548 (diffusion). The Paley θ=1/2 and θ=2/3 minimizers are within respectively 1.1e−7 and 8.91e−6 in the scaled coordinate qx/(2π) of a cyclic root. The θ=1 near-interval and diffusion dips lie respectively 2.94057/X and −1.00877/X from the fixed block harmonics 1/256 and 2/256 in the normalized variable x/(2π).

PROVED finite rational-mode certificates: at x=2π/256, the X=1048576 near-interval θ=1 and diffusion sets have values enclosed around 66737.5269304 and 69123.9082100, respectively. Divided by X these are about 0.063646 and 0.065922. The point dips in the table occur beside these macroscopic positive spikes. Thus the block rule has introduced a coherent rational component; the nearby negative sidelobes are directly certified, not inferred from its positive height. These center and dip evaluations are in `audit_results.json` and `final_summary.json`.

PROVED interpretation of the coefficient constraints: the returned sets are binary, so no binary coefficient identity is violated by them. They enforce b²=b and every raw binary moment exactly. What fails is the positivity required to inherit P61's weighted escape: the rounding residual creates certified negative excursions. The weighted escape's first two moments do not control that residual. P63's repair-energy and four-moment observations explain why coefficient repair is not an infinitesimal modification of a Gaussian/positive-packet escape. In these data the residual second and third profiles approach the actual Bernoulli targets, while the low negative floor is lost.

HEURISTIC mechanism and scope: q=o(X) repeats the cyclic negative spectrum across about X/q periods; tapering does not provide the positive capacity to cancel all those modes (P63.5 and P64's periodic-schedule obstruction). At q≈X the Paley probe removes that amplification and is the least bad large-X family, but still has ordinary large negative fluctuations. Fixed-block near-interval ordering and one-pass diffusion create rational spikes and envelopes with negative sidelobes; this conflicts with P48/P63's necessary positivity and torsion-budget conditions for a hypothetical M=o(√X) family. The present laws are not exactly the nested model of R12-N, so that theorem is not invoked as an all-parameter proof for them. The failure is certified for the listed instances and explained structurally, rather than extrapolated to every texture or every optimized taper.

## Final verification, novelty and handoff

PROVED finite audit outcome: `finalize.py` completed successfully on the specified VM with four cores. It verified 36 cyclic incumbent spectra; all 20 retained integer sets, their count profiles and their point dips; the full q=17,37 trade-off curves (70 and 48620 candidates); R12-S's nonzero cubic irrationality coefficient at three independently chosen primes; and the exact nonzero Vandermonde determinants for every order r=3,…,10. The R13-C support/mass/energy tests passed again. At the explicitly omitted frequency s=2J+2 their normalized sign-convolution defects were enclosed around 0.970244, 0.975111 and 0.980046 times q², confirming the paper's identified obstruction. Final Arb precision was 220 bits. `manifest.json` records SHA256 hashes of the sources, data and saved sets; `final_audit_vm.log` records the detailed final audit.

PROVED audit limitations and retained corrections: the finite R13-C samples are composite cubes, not prime instances; the infinite-prime theorem rests on the paper proof. The Vandermonde checks verify the local algebra behind R13-M2, not an all-orders Galois realization. The Gurobi optima at q≥61 use floating coefficients; only the separate exhaustive q=17,37 curves have exact-enclosure optimality certificates. Routine verifier repairs included Arb integer/Fraction conversions, replacing structural SymPy equality by algebraic simplification, restoring 220-bit precision after imported modules set their defaults, and correcting a strict inequality to equality for the isolated repair-site correlation. All final checks passed after those repairs. None of the paper results is Lean-kernel-checked or externally scrutinized.

PROVED novelty scope: searches of PROOFS.md for PK, QU, peak, scalar moment, power sum, partial convolution, threshold deficit, profile modulation, Newton and algebraic integer were made before claiming novelty. The record already contained the second-order peak calculation, R12-S, the Paley kurtosis counterexample, the root filter and the cyclic homogenization reduction. Those are quoted inputs. The new assemblies in this report are R13-PK's refutation for genuine half-sets; R13-C's growing-segment exact-convolution relaxation and its explicit omitted-frequency defect; R13-M1's first integrality failure; R13-M2's arbitrary-fixed-order arithmetic repair; the exact small trade-off staircases; and the specific binary laws, data and failure diagnostics. External priority is unchecked; no claim of an exhaustive literature search is made.

PROVED reproducibility commands, all run from the repository root:

```bash
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 420 python .research/agents/tdense13_scratch/cyclic_probe.py
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 480 python .research/agents/tdense13_scratch/binary_probe.py
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 240 python .research/agents/tdense13_scratch/finalize.py
```

NUMERICAL reproducibility detail: Gurobi uses seed 1913 and at most four threads. Each finite trade-off model uses five or eight seconds, with eight-second K-min seed searches for q=101,109; binary models use ten seconds per cutting iteration, three iterations. Time-limited incumbents can vary across reruns; the stored pair lists and integer arrays make every reported certificate reproducible independently of the optimizer. The saved tables include status, solver bound, runtime, set, phase, FFT length and certificate status. Python 3.12.3, NumPy 2.5.4, SciPy 1.18.1, Gurobi 13.0.3 and python-flint 0.9.0 were used.

HEURISTIC final strategic decision: kill universal PK; kill fixed-segment incompatibility as a sufficient relaxation; kill fixed-order scalar moment/integrality improvements; and stop scaling the tested fixed-block binary laws. Keep three distinct directions active for a subsequent round:

1. Full-frequency incidence constraints. The exact R13-C defect at 2J+2 shows what the missing equations detect. First derivation: seek a bound forcing an adaptive sum/difference of the large positive spectrum to detect such concentration, rather than prescribing γ=2,…,J in advance. Any claimed gain must enforce the incidence inequalities at every frequency and survive genuine cosine-profile textures in the small-δ regime.
2. Arithmetic of growing moment degree or the complete Galois orbit. First derivation: quantify the inverse-function constants in R13-M2 as r grows, and identify the first degree where integer characteristic-polynomial constraints can no longer be repaired at q^(1/3). Every fixed r is excluded as a route by this round's theorem; simultaneous all-order arithmetic remains open.
3. Block-free, coordinated q≈X binary tapers. First experiment: remove the fixed 256-site clock, use adaptive worst-frequency cuts or staggered count windows, and compare the negative minimum and fixed rational correlations at X=4096. The first pass must remove the observed rational comb before increasing X. The current data justify dropping these implementations, not dropping all q≈X construction ideas.

PROVED remaining exact gap: neither QU(β) for β>2 nor a binary escape with R<0.56 has been established. R13-C and R13-M2 concern separate explicitly stated relaxations; no array is claimed to satisfy their two enlarged constraint sets simultaneously. No unattended continuation is implied.
