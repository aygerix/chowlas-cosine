# W2 adversarial continuation: exact perturbation obstruction and a failed projected shortcut

Checkpoint: 2026-10-20T05:46:32.196395+00:00. Ongoing research; no universal Chowla/C* or W2 constant is established. [Reproduction index](../experiments/cstar_structural_2026-10-20/README.md).

2026-10-20. Candidate under test, NOT proved: there exists an absolute c>0 such that every finite symmetric S⊂Z\{0} satisfies -lambda_min(B_W2)>=c sqrt(|S|), W2={0}∪S∪(S+S). This is stronger than universal C*. Bounded numerical tests cannot establish it.

## 1. Full optimized W2 tests (not global Fourier minima)

All listed K values come from the smallest eigenvalue of the full induced adjacency on W2. FFTs implement linear convolution matvecs, with padding strictly larger than coordinatewise max|difference between two rows minus a generator|; they do not substitute torus-grid minima for eigenvalues. Row sets are exact integer pair sums. ARPACK residuals are saved alongside results.

Ratios below are |S|/K_W2².

- Centered one-representative JL lifts, p=3,5,7 at depth2: .38699,.20628,.08244. Their small-base integer encodings (base p²) give .34674,.17279,.07653; sufficiently large base3p² agrees with the exact Z² graph.
- Taper-random one-representative JL lifts, p=3,5,7: .31455,.22783,.09911.
- Increasing depth: JL(p=3,a=3), JL(3,4), JL(5,3): .10155,.01521,.01129.
- Centered hyperbolic quadrics: (p,d)=(3,4),(5,4),(3,6),(5,6): .57399,.32495,.16203,.03370. The largest test has |S|=3224, |W2|=448681; no larger case was attempted.
- Balanced root shells, k plus-ones and k minus-ones: k=2,r=6,7,8 gives .27162,.48179,.34268; k=3,r=6,7,8 gives .21505,.11580,.04171.
- Product-Fejér independent Boolean rounding, p_s=∏_j(1-|s_j|/m)_+, symmetric pairs sampled together: m=3,d=2,3,4,5 gives .44662,.60464,.26176,.18062; m=4,d=2,3,4 gives .35911,.35050,.19788; m=5,d=2,3,4 gives .35083,.26378,.17144. This was chosen adversarially because m=3 has ambient doubled box9^d≈(E|S|)², so the one-dimensional interval-filling argument is unavailable. The numerical attack failed: certificates strengthened with dimension in the tested range.
- D-type roots ±e_i±e_j: r=4,6,8,10 gives .72328,1.16877,1.75,2.34757. This grows in the bounded range but is not evidence of divergence; the limiting scalar moment model already supplies an absolute bound.

Files: adversarial_w2_lifts.json, depth_w2.json, root_shell_w2.json, product_fejer_w2.json, d_root_w2.json, and corresponding scripts. These are numerical tests, not interval-arithmetic spectral certificates. Largest recorded residuals are below 10^-6. None refutes an any-constant W2 claim.

## 2. An exact obstruction to low-operator-norm finite-group near-realization

Let G be a finite abelian p-group, D⊂G\{0} symmetric and invariant under multiplication by every unit modulo the exponent of G. Let S={s_g:g∈D} be symmetric one-representative lifts in a torsion-free ordered abelian group, with a residue homomorphism taking s_g to g. Choose one distinct lift x_g of EVERY g∈G. Compare:

- B_G, the finite Cayley adjacency of D on these labels;
- B_R, actual adjacency between x_g using integer/torsion-free lags S.

Then B_R≤B_G entrywise. Set E=B_G−B_R: it is a symmetric nonnegative 0/1 deletion matrix.

### Ordered edge count

For M distinct ordered rows and q positive permitted lags, the number of undirected edges is at most

    qM-q(q+1)/2.

Proof: the i-th row has at most min(q,M-i) neighbors above it. Sum this bound. No arithmetic progression assumption is made.

Partition D into unit-scalar orbits T_j. Each orbit is exactly the set of generators of a cyclic subgroup H_j of order M_j=p^{b_j}; hence |T_j|=M_j(1-1/p)=2q_j. Different T_j are disjoint, so their edge sets are disjoint. On each H_j-coset the finite Cayley graph contributes M_j q_j edges. The lifted graph loses at least q_j(q_j+1)/2 by the ordered edge bound. Summing over cosets and over j gives

    1^T E 1 / |G| >= sum_j q_j(q_j+1)/M_j
                     >= (1-1/p)|D|/4.

Consequently

    ||E||op >= (1-1/p)|D|/4.                              (NR)

For a quadric cone, the orbits are nonzero field lines, M_j=p, and the sharper expression is |D|(p+1)/(4p). For JL D_{a,j}, scalar-unit invariance follows directly from the defining slope quotient: multiplying both coordinates by a unit leaves the valuation of y and x/(y/p^k) modulo p^{a-k} unchanged. Thus (NR) holds at EVERY depth, not merely a=2.

If D+D covers G and the original S is a one-representative lift, one may choose x_g from W2, one per residue class. The same bound applies for every such choice. Thus an o(sqrt(|D|)) operator-norm approximation to the original finite Cayley adjacency is impossible in this literal deletion-only, one-representative model. This excludes a specific proposed countermodel mechanism, not all possible near-realizations with added edges, multiple representatives, changed comparison operator, or approximate labels.

**Important:** (NR) does not imply a negative eigenvalue of size sqrt(|D|). Deletion can act in a positive spectral sector. Weyl cannot be reversed.

## 3. Background projection: actual lifts succeed, but the universal shortcut is FALSE

For each actual centered JL/quadric lift, choose a least-Euclidean-norm W2 representative of every group residue, and form E as above. Let P_bg be the Fourier projection onto the finite graph's eigenvalue -K_G. Then

    P_bg B_R P_bg = -K_G P_bg - P_bg E P_bg.

Therefore K_W2 >= K_G+lambda_max(P_bg E P_bg), provided a positive maximum is found. This is a valid projected certificate, not the full optimized one.

Numerical examples:

- JL p=3,a=2: lambda_max=2.58045=.52673 sqrt(|D|).
- JL p=5,a=2: lambda_max=10.44644=.95362 sqrt(|D|).
- JL p=7,a=2: lambda_max=29.86112=1.62906 sqrt(|D|).
- JL p=3,a=3: lambda_max=20.44165=1.33631 sqrt(|D|).

Further completed cases are in project_deleted_edges.json. A large positive eigenvalue is numerically present in these particular representatives. It is NOT forced by the raw norm bound, as the following exact counterexample shows.

### Counterexample: complete-group model lifted to odd representatives

Let G=Z_V with V odd, D=G\{0}, N=V-1. Its Cayley graph is complete, B_G=J-I, K_G=1, and P_bg projects to 1^perp. For each residue pair {g,-g}, choose one positive ODD integer representative a_g≡g mod V, and use ±a_g. Such representatives exist since V is odd. They can be chosen distinct. This gives a symmetric one-representative S, all of whose elements are odd.

On R={0}∪S the actual graph is exactly a star: every center-leaf edge is present, and every leaf-leaf difference is even, hence not in S. Thus K_R=sqrt(N).

Nevertheless, for E=(J-I)-B_star, the compressed operator P_bg E P_bg has spectrum

    (N-1)/(N+1) once;  -1 with multiplicity N-1.

Proof: on 1^perp, P_bg B_star P_bg has eigenvalue -2N/(N+1) along P_bg delta_0, and zero on the leaf-difference subspace. Subtract it from -I.

Hence

    lambda_max(P_bg E P_bg)<1=o(sqrt(N)),

despite exact Booleanity, torsion-free integer lifts, preserved center/S rows, finite-group ratio N/K_G²→∞, and ||E||op of order N. The full star has the desired sqrt(N) negative eigenvalue, but it comes from coupling between the spike and background sectors, not from the background block alone. Therefore a universal projected-positivity lemma of that form is refuted. A viable argument must retain the cross-sector Schur term (or another adaptive choice of directions).

## 4. Exact cross-Gram attempt and a concrete two-vector repair on E99c

For I={0}∪S, J=W2\I, let B_I be the interior adjacency, C the cross block, and

    R_ij=(1_S*1_S)(i-j), i,j∈I.

Because I+S⊂W2, exact full convolution gives

    R=B_I²+CC*.

If B_I u=-K1 u, ||u||=1, set g=C*u. Its squared leakage is

    a=u*Ru-K1².

Its exterior cost at diagonal K1 is

    c=<g,(K1 I+B_J)g>/a.

The two-vector compression alone gives

    K_W2 >= K1 + (sqrt(c²+4a)-c)/2.                        (CG)

This is generic matrix algebra. The prospective Boolean step would have to ensure enough leakage with controlled cost for an appropriate low interior direction. An unweighted uniform bound on every kernel direction is false for the previous giant axes block: its lowest leakage directions have R=O(d²+d), while |S|≈dm can be much larger. The successful all-face argument selects special directions instead.

For the exact E99c samples, applying (CG) to a numerical MINIMUM eigenvector of the full first-neighborhood graph gives:

- n=1056: a/|S|=1.19825, c=-8.25662, K1=33.64218, two-vector K>=88.24573.
- n=3962: a/|S|=1.05946, c=-2.34018, K1=48.82910, two-vector K>=141.63193.
- n=15881: a/|S|=1.05681, c=-10.65723, K1=77.73026, two-vector K>=266.34771.

Thus even one adaptive exterior combination, rather than a filled-interval vector, restores square-root scale in these controls. It is weaker than the full W2/interval tests, but directly exposes the missing covariance: leakage is approximately |S| and exterior cost is nonpositive. These measurements do not prove those inequalities for arbitrary Boolean S. Scripts/results: taper_two_step_krylov.py/json.
