# Collective boundary certificate: exact optimization and a successful all-face calculation

Checkpoint: 2026-10-20T05:32:53.486301+00:00. Research remains ongoing; no universal Chowla/C* theorem is claimed. Reproduction: [experiment index](../experiments/cstar_structural_2026-10-20/README.md).

2026-10-20. CHAIN(c) / actual derivation. No universal Chowla bound is proved. The new calculation below repairs the high-rank axes test by using correlated exterior directions. It does not establish that arbitrary Boolean supports have those directions.

## 1. Exact optimization, including exterior cost

Let B be convolution by 1_S, S finite symmetric in Z, and let I,J be disjoint finite row sets. Write the principal matrix at diagonal K as

    [ H  C ]
    [ C* G ],     H=K I+B_I, G=K I+B_J.

Suppose H is PSD and P is its kernel projection. At a prospective global diagonal K+delta, compression to ran P plus all exterior coordinates is

    L_delta = [ delta I   PC        ]
              [ C*P      G+delta I ].

The exact necessary and sufficient condition for this COMPRESSED matrix to be PSD is

1. G+delta I is PSD;
2. ran(C*P) is contained in ran(G+delta I);
3. delta I >= PC (G+delta I)^dagger C*P.

For strict exterior positivity this is

    delta >= ||PC (G+delta I)^(-1/2)||op^2.                 (1)

Thus a raw singular value of PC is not the optimized certificate: it must be weighted by the full exterior resolvent. Equation (1), including the range condition at singular values, is the exact optimization over ALL exterior test vectors for each interior vector. It retains correlations and does not replace them by a maximum column or a Frobenius estimate.

A usable compression corollary is: if Q is any exterior subspace with QGQ <= gQ, and sigma=||PCQ||op, then

    delta >= (sqrt(g^2+4 sigma^2)-g)/2.                    (2)

The subspace need not be G-invariant. Choose singular vectors u,v for PCQ; their 2-by-2 compression has upper-left 0, cross entry sigma, and lower-right <=g. Monotonicity in the lower diagonal gives (2). In particular, cheap exterior modes with g=0 give delta>=sigma, not sigma^2/K.

For approximate kernels, assume PHP <= eta P instead. The same calculation gives

    delta >= [sqrt((eta-g)^2+4 sigma^2)-eta-g]/2.           (3)

These statements themselves are generic PSD algebra, not Boolean-specific progress.

## 2. All exterior faces repair the axes obstruction

Use exactly the support from the prior counterexample:

    S = { +/- t B^j: 1<=t<=m-1, 0<=j<d }, B=8m,
    I = { sum u_j B^j: 0<=u_j<m }.

It is safe to calculate in digit coordinates. On the union below, every coordinate difference has absolute value <3m; comparison to a member of S has coordinate magnitudes <4m, so base 8m introduces no false edges.

At K=d, H=sum_j J_m^(j), with kernel P=P0^tensor d, P0=I_m-J_m/m.

Take J to be the complete one-coordinate exterior shell: exactly one coordinate lies in

    E={-m+1,...,-1} union {m,...,2m-2},

and every other coordinate is in {0,...,m-1}. There are d disjoint faces J_j, each with 2(m-1)m^(d-1) rows. Different faces have NO edges between them, since their difference has at least two nonzero coordinates.

Within face j, the adjacency in its outside coordinate is

    E_j = (J_(m-1)-I) directsum (J_(m-1)-I).

There are no left-right outside edges: their minimum distance is m+1. In the untouched coordinates the adjacency is J_m-I.

Let Q0 be the projection onto vectors with zero sum separately on the left and right outside intervals. On face j set

    Q_j = Q0 in coordinate j, P0 in every other coordinate.

Then the FULL exterior compression satisfies

    QGQ=0, Q=directsum_j Q_j.                             (4)

Indeed the outside-coordinate adjacency is -I on Q0, each of the d-1 untouched adjacencies is -I, and the diagonal is d. This cancellation is why ignoring exterior cost misses the mechanism.

Let T be the m by 2(m-1) incidence matrix between an inside coordinate and E, with entries 1 when their difference lies in +/-[1,m-1]. Set L=P0 T Q0. The compressed coupling to face j is L in coordinate j and P0 in the others. Consequently

    (PCQ)(PCQ)* = sum_j (LL*)^(j) tensor P0^(others),
    ||PCQ||op = sqrt(d) ||L||op.                          (5)

The largest eigenvector is a tensor product of top eigenvectors of LL*. Thus the sqrt(d) is EXACT, not a trace estimate.

Equations (2),(4),(5) prove the finite Boolean principal-minor bound

    K_global >= d + sqrt(d) ||P0 T Q0||op.                (6)

### Explicit absolute constant

For m=4k+1, order the right columns by q=1,...,4k. They are R_iq=1[i>=q], i=0,...,4k. The left columns, after reversal, are 1-R. Choose the zero-sum input a with successive blocks

    +1 repeated k, -1 repeated 2k, +1 repeated k.

Its cumulative sum h=Ra is antisymmetric about i=2k, so P0 h=h. Also

    ||a||^2=4k, ||h||^2=(4k^3+2k)/3.

Use exterior input (a,-a). It has squared norm 8k and maps to 2h. Therefore

    ||L||op^2 >= (2k^2+1)/3,
    K_global >= d + sqrt(d(2k^2+1)/3).                   (7)

This is Omega(m sqrt(d)), while |S|=2d(m-1). In particular the previously problematic m approximately d^2 regime is detected with room to spare. This is a certificate on I union its first exterior shell, with explicitly specified vectors, not an evaluation of the global polynomial at a specially aligned phase.

For other m, the exact statement (6) remains valid. Direct SVD gives ||L||/m=0.24060,0.22972,0.22637,0.22542 for m=5,9,17,33. These numerical values are only checks; (7) is the proof used.

Interpretation: the one-row bound saw only O(m) squared leakage. Correlated zero-sum combinations along a face give O(m^2); combining all d independent faces gives O(dm^2). The exterior cost vanishes on precisely those combinations. Both improvements matter.

## 3. Coordinate-free extension attempted: what survives and what fails

A potential sufficient condition is an exterior projection Q with

    ||PCQ||op^2 >= c|S|,    QGQ <= C sqrt(|S|) Q,

and an interior approximate-kernel error eta=O(sqrt(|S|)) small enough in (3). This would give a square-root increment. I tried to replace the explicit tensor zero-sum subspaces by total leakage or by the first neighborhood of the origin.

### Total leakage loses the needed information

For a unit interior kernel vector u, extend u by zero to Z and put q=K+D_S. The vector g=(K+B)u vanishes on I, so it is supported on the full finite exterior boundary J=(I+S) minus I. Exactly,

    a=||C*u||^2=integral q^2 |U|^2,
    b=<C*u,G C*u>=integral q^3 |U|^2,
    integral q |U|^2=0.

Testing only the exterior vector C*u gives the matrix

    [0, sqrt(a); sqrt(a), b/a].

This reduces the proposed collective gain to weighted second/third moments. Booleanity and integer order have disappeared from the estimate; large positive exterior cost can absorb the leakage. It is not a replacement for (4). Further Krylov vectors similarly produce moment matrices, not a new Boolean inequality. This is an exact diagnostic, not a counterexample to every possible aggregate method.

### A coordinate-free first-neighborhood alternative is already obstructed

For I={0}, using J=S gives the known self-difference graph. Writing A=S intersect Z_positive, its odd sector is D-E and its even sector (including the center) is

    [0, sqrt(2) 1*; sqrt(2) 1, D+E],
    D_ab=1_A(|a-b|), E_ab=1_A(a+b).

Initial exhaustive A subsets [1,13] gave |S|/K_local^2<=3, but this is NOT evidence for a universal bound. A subsequent finite search already gave 3.51555, and more importantly the repo's E99c tests exactly this graph, up to translation. It finds the tapered sparse controls with certificates on the n^(1/3) scale rather than sqrt(n). P70.3 proves their actual global sqrt(n) negativity by independent-rounding methods, not this graph. Therefore this alternative is dropped rather than advertised as a new conjecture supported by small exhaustive searches.

The exact model S={e_i-e_j:i!=j} also explains why constants inferred from tiny supports are misleading. The exterior graph is regular of degree 2(r-2), with least eigenvalue >=-2 (it is a line graph of the bipartite graph with the perfect matching removed). Its central two-dimensional sector has negative eigenvalue

    r-2-sqrt((r-2)^2+r(r-1)),

so its local |S|/K_local^2 tends to 3+2sqrt(2). This is the familiar B3-difference/moment mechanism (P10), not a new route.

I additionally tested balanced root shells with k positive and k negative coordinates. At k=2, r=6,8,10 their first-neighborhood ratios were 2.7471,3.2090,3.8266. The exterior degree is 10*C(r-4,2); its nonconstant negative spectrum cannot be discarded. This experiment was stopped once the already-recorded E99c obstruction was checked. It is not evidence of a universal result or a proved asymptotic countermodel.

## 4. Scope of the result and remaining precise issue

Proved here: exact full-exterior variational optimization; a genuinely collective all-face certificate restoring the missing rank factor in the existing Boolean axes counterexample, in fact giving K>=d+c m sqrt(d).

Not proved: existence, for arbitrary finite Boolean integer support, of enough correlated low-cost exterior modes. The successful axes proof uses two facts absent from generic moments: its exact 0/1 fibre incidence supplies cumulative-sum amplification, and its separate integer left/right intervals provide zero-sum modes with exactly canceled exterior diagonal cost. Replacing these facts by a uniform statement for arbitrary supports is the unresolved step. No claim that these calculations advance the universal bound, exclude every admissible finite-group lift, or exhaust further approaches is made.

Source checks: .research/CSTAR.md; prior boundary note; PROOFS P9, P10, P19, P70; src/e99c_tapered.py and src/e99_selfgraph.py. Reproduction scripts and recorded data are in [the experiment directory](../experiments/cstar_structural_2026-10-20/README.md).

Independent assembled-matrix check: for (d,m)=(2,5),(3,5), explicitly constructing I,J,C,G,P,Q gives ||QGQ||_F<4e-15. The measured coupling norms are 1.7013016167040804 and 2.0836604297485426, agreeing with sqrt(d)||L|| to 3e-15. This verifies the full face ordering and cross-face zero pattern, not just the one-dimensional calculation.
