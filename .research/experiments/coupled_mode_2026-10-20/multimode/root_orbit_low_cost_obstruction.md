# Root-difference obstruction to a low-cost spectral-mass shortcut

20 October 2026. Exact finite Boolean calculation plus a proved limit. This is a counterexample to the restricted estimate below, not to full W2 or Chowla. It does not satisfy K_W1/sqrt(N) -> 0.

## Result

Let S_r = {e_i-e_j : i != j} in Z^r, N=r(r-1), W=({0} union S_r)+({0} union S_r), J=W\{0}, A=B_J, and b=1_{S_r} in l2(J). For every real sequence tau_r=o(r),

    ||1_{(-infinity,tau_r]}(A)b||^2 / N -> 0.                 (1)

In particular, taking all nonpositive modes of the punctured full-W2 matrix does not necessarily capture a fixed fraction of the central Boolean coupling. Nevertheless, exactly and for every r>=4,

    K_W2(S_r) >= 4r/9 >= (4/9)sqrt(N).                       (2)

Thus an all-mode argument restricted to nonpositive, or o(sqrt(N))-cost, punctured modes fails even though full W2 has square-root negativity. Modes of positive cost comparable to sqrt(N) suffice and cannot in general be discarded.

Base-7 encoding v -> sum_i v_i 7^i gives finite symmetric Boolean integer supports with exactly the same W2 graph: the coordinates of u-v-s have absolute value at most 5, and the largest nonzero digit dominates the sum of all smaller digits. Thus this is not a torsion-group countermodel.

## Exact orbit compression

The permutations of coordinates and global negation preserve S and W. The five orbits in W, their representative patterns, and sizes are

    0: (),                  1
    R: (1,-1),              n=r(r-1)
    D: (2,-2),              n
    V: +/-(2,-1,-1),        n(r-2)
    Q: (1,1,-1,-1),         n(r-2)(r-3)/4.

These exhaust sums of at most two roots. Let psi_O be the normalized indicator of orbit O. For a row in orbit O, the counts of its S-neighbors in the five orbits are exactly

    C_r =
    [0, r(r-1), 0, 0, 0;
     1, 2r-4, 1, 2r-4, (r-2)(r-3);
     0, 1, 0, 2r-4, 0;
     0, 2, 2, 2r-6, r-3;
     0, 4, 0, 4, 4r-16].

These entries follow by adding an ordered root e_i-e_j to the representative and inspecting the resulting pattern. The script root_orbit_response.py independently enumerates every ordered root and verifies detailed balance |O|C_OO'=|O'|C_O'O. Each count is a polynomial in r of degree at most two: the two ordered indices belong either to the at most four distinguished coordinates of the representative or its zero coordinates. Thus exact enumeration at three or more distinct r>=5 verifies the displayed polynomial formulas; r=4 is checked separately.

The symmetric normalized compression is M=diag(sqrt(|O|)) C diag(1/sqrt(|O|)), i.e.

    M =
    [0, sqrt(n), 0, 0, 0;
     sqrt(n), 2r-4, 1, 2sqrt(r-2), 2sqrt((r-2)(r-3));
     0, 1, 0, 2sqrt(r-2), 0;
     0, 2sqrt(r-2), 2sqrt(r-2), 2r-6, 2sqrt(r-3);
     0, 2sqrt((r-2)(r-3)), 0, 2sqrt(r-3), 4r-16].

For J delete the first row/column, obtaining M_J. Since b=sqrt(n) psi_R is invariant, its spectral measure under A is exactly its spectral measure in this four-dimensional invariant subspace. Non-invariant modes have zero coupling to b. This is an exact reduction, not an approximation to the full spectrum.

## Proof of (1)

In the order (R,D,V,Q), the norm limit is

    M_J/r -> L =
    [2,0,0,2;
     0,0,0,0;
     0,0,2,0;
     2,0,0,4].

The error is O(r^(-1/2)). The spectrum of L is {0, 2, 3-sqrt(5), 3+sqrt(5)}. Its nullspace is exactly span(psi_D), orthogonal to psi_R.

Here is an elementary projection argument, avoiding an appeal to an unspecified eigensolver. Let P_r be the spectral projection of M_J/r on (-infinity,tau_r/r], and let v be a unit vector in its range. Then

    <v,Lv> <= ||L-M_J/r|| + tau_r/r.

Since L >= (3-sqrt(5)) P_{D-perp}, the right side tending to zero implies

    ||P_{D-perp}v||^2 -> 0,

uniformly over such unit vectors (if the displayed right side is negative the subspace is empty). Since psi_R lies in D-perp, ||P_r psi_R|| -> 0. Multiplication by n gives (1). This proof applies to any tau_r=o(r), including a fixed negative cutoff, zero, or a growing sub-square-root positive cutoff.

## Proof of (2)

Use f=psi_0-psi_R+(1/2)psi_Q. Its norm squared is 9/4 and its energy is

    <f,B_W f> = 3r-8 - 2sqrt(r(r-1))
                         - 2sqrt((r-2)(r-3)).

For r>=4, sqrt(r(r-1))>=r-1 and sqrt((r-2)(r-3))>=r-3, so this is at most -r. The Rayleigh quotient gives (2).

## Interpretation and limits

The quantitative problem is not merely to find negative exterior modes or to count them. Here the central response is carried, to leading order, by a strictly positive 2-by-2 block [[2,2],[2,4]] after scaling by sqrt(N). Coupling this block to the center still gives a square-root negative eigenvalue.

This example does not refute the stronger proposed weak-W1 extension statement: there is r supported on W2\I with ||D+r||^2 <= C N and integral D|D+r|^2 <= C N^(3/2). Indeed here D alone has norm squared N and its normalized energy is 2r-4, already O(sqrt(N)). Nor does it establish such a statement in general.

A further scope distinction: (1) concerns the spectral projection of b onto low eigenmodes. It does not rule out a non-invariant subspace whose compressed quadratic form is nonpositive, or a vector formed by mixing a costly b-coupled mode with an independent negative mode. Such independent negative modes can have zero direct coupling to b. The proof must not be described as excluding every low-Rayleigh-cost trial vector.
