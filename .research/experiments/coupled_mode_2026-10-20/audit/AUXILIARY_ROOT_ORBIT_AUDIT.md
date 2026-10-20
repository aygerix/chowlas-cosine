# Auxiliary audit: root-difference response and bouquet identity

20 October 2026. Audited `multimode/root_orbit_low_cost_obstruction.md` and `multimode/bouquet_response_and_scope.md`.

## Verdict and scope

The root-difference low-cost spectral-mass obstruction is correct. The bouquet Schur-complement and fixed-interior-extension implications are also correct, subject to two notation clarifications below. None of this establishes an additional weak-W1 obstruction or a universal full-W2 theorem. The Laguerre numerical diagnostics were not promoted to proved statements.

For the root support S_r={e_i−e_j:i≠j}, N=r(r−1), let A be the punctured W2 matrix and b=1_{S_r}. Then, for every real τ_r=o(r),

    ||1_{(-∞,τ_r]}(A)b||² / N → 0,

while K_W2≥4r/9≥(4/9)√N. This is a genuine Boolean torsion-free example, preserved by the stated base-7 embedding.

## Checks

- The five orbit types exhaust sums of at most two roots. Their cardinalities are correct, including the combined positive/negative V orbit of size r(r−1)(r−2).
- Each neighbor-count row follows by adding an ordered root. Independently enumerating r=4,…,12 verified all 45 representative rows exactly. For example, a V vertex has 2 root neighbors, 2 D neighbors, 2(r−3) V neighbors, and r−3 Q neighbors; a Q vertex has 4 root neighbors, 4 V neighbors, and 4(r−4) Q neighbors.
- The normalized orbit matrix is symmetric by detailed balance. Since b is invariant under the coordinate-permutation/global-negation group, its spectral measure is exactly that of the four-dimensional punctured invariant compression. No statement about the remaining spectrum is needed.
- The limit matrix has eigenvalues 0, 2, 3−√5, 3+√5 and nullspace exactly the D coordinate, orthogonal to b's R coordinate. The projection proof is valid even when τ_r is negative. The bound is uniform on unit vectors in the projected subspace, so it controls the norm of the projection of the R vector, not merely individual eigenvectors.
- The stated trial vector has norm squared 9/4 and energy 3r−8−2√(r(r−1))−2√((r−2)(r−3))≤−r for r≥4. This proves the advertised full-W2 bound.
- The carry-free integer embedding is valid because every tested adjacency relation has coordinate coefficients bounded by 5, while base 7 dominates lower places.

## Quantitative reminder that this is not weak W1

The root-induced graph is regular of degree 2r−4. Compressing W1 to its center and normalized root indicator gives

    [[0, √(r(r−1))], [√(r(r−1)), 2r−4]].

Its negative eigenvalue magnitude divided by √N tends to √2−1. In particular,

    liminf K_W1(S_r)/√N ≥ √2−1 > 0.

Thus this auxiliary example does not refute a low-cost-response claim restricted to genuinely weak W1. It does refute the corresponding unconditional claim.

## Bouquet notation clarifications

For the bouquet matrix B_m, the Schur-complement statement must read

    K I + B_m is positive semidefinite
    iff K ≥ m <b,(A+K I)^{-1}b>,

under K>−λ_min(A). The unshifted bouquet itself is not positive semidefinite when b≠0. At a pole the range/pseudoinverse qualification in the source is correct.

For complex a=<b,g>, the two off-diagonal entries of the 2×2 compression are conjugates. Equivalently rotate the phase of g to make a≥0. The eigenvalue expression involving |a|² is already correct.

The fixed-interior extension criterion is sound: disjoint Fourier supports give <D,q>=n and ||q||²≥n. Together with ||q||²≤Cn and <q,Dq>≤Cn^(3/2), this yields |a|≥√(n/C) and h≤C√n. The 2×2 formula consequently gives a positive constant times √n already at m=1, with constant depending only on C, and the stated amplification for independent copies.
