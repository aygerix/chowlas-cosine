# Unequal axis intervals survive already at W1

Let S={t e_j: 1<=j<=J, 1<=|t|<=L_j} in Z^J, N=2 sum_j L_j, and L=max_j L_j. Define W1={0} union S, W2=W1+W1, and K_i=-lambda_min(B_Wi). Then

    K_2 >= K_1 >= c sqrt(N),
    c=sqrt((sqrt(2)-1)/(sqrt(2)+5)) > 0.254.

This rules out both equal and unequal axis-interval families as full-W2 asymptotic counterexamples. The proof is entirely at W1 and should not be presented as a new benefit of W2.

## One-axis certificate
Set k=ceil(L/3), d=L-k+1, and choose three intervals of k consecutive integers starting at -d, 0, d on an axis of length L. All three blocks lie in [-L,L]. Within each block every pair is adjacent. Between consecutive blocks every pair is adjacent since d+k-1=L. Between the first and last blocks no pair is adjacent since 2d-k+1=2L-3k+3>L.

The constant-on-block compression is k(I+A(P3))-I. Its minimum eigenvalue is k(1-sqrt(2))-1. Thus

    K_1 >= 1+(sqrt(2)-1)ceil(L/3) >= c0 L,
    c0=(sqrt(2)-1)/3.

## Central-star certificate
Compress onto delta_0 and the unit vector uniform on S. Different axes give no edges between their nonzero points. The induced degree at a point on axis j is at most 2L_j, so the exact compression is

    [[0, sqrt(N)], [sqrt(N), a]],  0<=a<=2L.

Therefore

    K_1 >= (sqrt(a^2+4N)-a)/2 >= sqrt(L^2+N)-L.

## Optimize the two bounds
Put ell=L/sqrt(N). The first bound is increasing in ell and the second decreasing. Their crossing solves

    c0 ell=sqrt(ell^2+1)-ell,
    ell=1/sqrt(c0^2+2c0).

Consequently their maximum is always at least sqrt(c0/(c0+2)), which is the claimed c.

All eigenvalue comparisons are rigorous principal-subspace lower bounds on K, sufficient to eliminate this proposed counterfamily. A sufficiently large carry-free integer encoding preserves the complete W1 and W2 graphs.
