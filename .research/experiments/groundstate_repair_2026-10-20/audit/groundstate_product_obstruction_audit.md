# Independent audit: translated-ground-state and odd-sector obstruction

2026-10-20. Audited `schur/groundstate_product_no_amplification.md`, including its new Sections 6.1 and 7. This audit uses direct algebra and finite checks, not the E99c numerical scaling claim.

## Verdict

The unconditional construction is valid. It supplies genuine symmetric Boolean integer supports with a simple first-neighborhood bottom eigenvector for which the entire translated-bottom-vector space has negative certificate o(sqrt(|S|)). The stronger entire odd-W2-sector bound is also valid. No claim about failure of the full W2 certificate follows, and no claim of a Chowla counterexample follows.

All essential quantifiers, signs, coefficient normalizations, and integer embeddings check out. The proof does not need a random-model theorem. Small-matrix computations below are checks only, not premises.

## 1. Interval operator and multiplicity

Use cells of width h=2/(2L+1) centered symmetrically in [-1,1], identifying coefficient vectors with normalized cell indicators. The operator corresponding to h B_L has a bounded step kernel differing from 1[|x-y|<=1] only in an O(1/L) boundary strip and diagonal cells. Its Hilbert-Schmidt error is O(L^-1/2). Since 1/L divided by h tends to one and the operators are bounded, B_L/L has the same norm limit. Reflection is exactly respected. Extending the finite-rank operators by zero in the orthogonal complement is harmless because the limiting bottom is isolated below zero.

For the limiting operator F, an eigenfunction with lambda nonzero is absolutely continuous on each half, then satisfies the asserted second-order ODE. Writing y=1/lambda:

- Odd: f(x)=a sin(yx) for x>0. The differential identity lambda f'(x)=f(1-x) forces cos(y)=0 and sin(y)=1. Conversely these conditions give the differential identity, and the integral equation at x=1 holds because integral_0^1 f=lambda a=lambda f(1). Thus all and only nonzero odd eigenvalues are 1/(pi/2+2pi j). Each has one-dimensional eigenspace.
- Even: the integral equation at zero and one gives f(1)=f(0)/2, and the derivative identity gives f'(0)=-f(0)/(2lambda). Hence f(x)=a[cos(yx)-sin(yx)/2]. The remaining conditions give cos(y)=4/5, sin(y)=3/5. Conversely integral_0^1 f=lambda a[sin(y)+(cos(y)-1)/2]=lambda a/2=lambda f(1), so these are actual eigenvalues, not merely necessary boundary conditions. Again the eigenspaces are one-dimensional.

Thus the negative bottoms are respectively -2/(3pi) and -1/(2pi-arctan(3/4)), with a strictly positive gap. Compact self-adjoint norm convergence gives a one-dimensional spectral projection near the odd bottom, rules out other lower eigenvalues, and preserves parity. This proves the eventual simple odd bottom and linear even-sector gap.

The optional exact odd formula also checks numerically at L=2,5,10,30,100. It is not needed to establish the theorem.

## 2. Implant and Schur complement

Let A be the noncentral T block, b its all-ones column, and k=k(T). Positivity of [[k,b*],[b,A+kI]] implies A+kI>=0, b in its range, and b*(A+kI)^dagger b<=k. For k_L>k the inverse exists, and monotonicity on that range gives 0<=b*(A+k_L I)^(-1)b<=k. There are no cross-edges between nonzero T-axis and U-axis rows.

After eliminating A+k_L I, the remaining shifted interval block loses only that nonnegative center rank-one form. The odd sector is completely unchanged; the even sector remains strictly positive when delta L>k. The eliminated block is positive definite. Congruence therefore proves that the full shifted W1 matrix is PSD with exactly one zero eigenvector, namely the odd interval eigenvector, extended by zero onto T.

One can choose L=ceil(C0 k) universally: k>=sqrt(2) follows from the induced path on {-m,0,m}, m=max T. This absorbs both the asymptotic threshold and rounding. Also k_L<=2L=O(k), requiring no quantitative convergence rate.

## 3. Product bound and stronger odd-sector bound

For a product q_U(y)p(x,y), the x-frequency support at fixed y lies in {0} union T. The first-neighborhood Rayleigh inequality in x, followed by D_U>=-2L, gives energy at least -(k(T)+2L) times squared norm. This argument covers every complex p in the permitted space, not only real or profile-optimized vectors. A nonzero p cannot give an identically zero product with the nonzero trigonometric polynomial q_U.

For full W2, every row with x-coordinate outside {0} union T has y=0. Every odd coefficient vector in y vanishes at such a row. Consequently the same fixed-y argument applies to every odd W2 polynomial, proving K_W2,odd<=k(T)+2L. This is a stronger valid obstruction than just the product bound.

The ground-state coupling and any defined exterior resolvent preserve parity. Thus directions obtained by applying that resolvent to the old bottom mode remain in this weak odd sector. This statement must not be interpreted as controlling even exterior eigenvalues, or as using an exterior inverse at a pole. The report's explicit caveat correctly preserves this distinction.

## 4. Signed-layer proof, exact error, and diagonal

For s,t with k plus and k minus signs, their difference belongs to the layer exactly when there is no opposite-sign overlap and exactly k same-sign overlaps. The signed-k-subset incidence Gram has entries binom(c(s,t),k), so G>=A entrywise. This includes the diagonal G_ss=binom(2k,k), A_ss=0.

For a fixed s, choose a matched positive and k-a matched negative coordinates in binom(k,a)^2 ways. Complete t on k positions outside support(s), choosing the signs in binom(k,a) ways. Hence the exact degree is

    d=F_k binom(r-2k,k),  F_k=sum_a binom(k,a)^3.

For the Gram row sum, choose the same signed k-subset of s, then complete its k missing positions outside that subset rather than outside support(s). This gives F_k binom(r-k,k). Therefore E=G-A is nonnegative, symmetric, regular, and has exact row sum

    e=F_k[binom(r-k,k)-binom(r-2k,k)].

Its operator norm equals e: the uniform vector attains e and every absolute row sum is e. Since G is PSD, lambda_min(A)>=-e. The cone decomposition is exact, giving

    kcentral <= k(T) <= max(kcentral,e),
    kcentral=2n/(sqrt(d*d+4n)+d).

One must not claim equality with kcentral for every finite r. For example r=8,k=2 gives kcentral approximately 6.3318 but k(T) approximately 11.4403. The report correctly uses an enclosure.

For the explicit diagonal, write A0=binom(r,k), B0=binom(r-k,k), C0=binom(r-2k,k), so sqrt(n)=sqrt(A0 B0). As A0>=B0,

    e/sqrt(n) <= F_k(1-C0/B0)
                 <= F_k k^2/(r-2k+1).

As sqrt(n)<=A0,

    d/sqrt(n) >= F_k C0/A0
                 >= F_k[1-2k^2/(r-k+1)].

These product bounds are valid for r>=3k. At r=ceil(4F_k^2 k^2), they give e/sqrt(n)<=1/F_k and d/sqrt(n)>=F_k/2. Since kcentral<=n/d, the final bound k(T)/sqrt(n)<=2/F_k follows. F_k>=k+1 tends to infinity, so this is an explicit diagonal with the asserted vanishing ratio.

## 5. Integer realization

A W2 adjacency relation involves at most five signed support vectors. For layer digits in {-1,0,1}, each coordinate in such a relation has absolute value at most five. Under base 7, the largest nonzero place cannot cancel: the sum of the absolute values of all lower terms is at most 5(7^m-1)/6<7^m. This also ensures injectivity of W2 rows and preserves product Gram relations (at most four support terms). No finite-group wraparound is being used.

For the second, interval implantation, a relation among at most five support vectors has first-coordinate magnitude at most 5M. Q>5M forces that coordinate to vanish in any relation t+Qu=0; the second coordinate then vanishes too. Hence W1 and W2 adjacency, inner products, and the product-space Rayleigh quotients survive the map into Z. The reflection is an inherited matrix involution after embedding; it need not be literal reflection of the scalar frequency.

## 6. Leakage and hostile cost

Normalize q_U in L2. With r_U=(D_U+k_L)q_U, orthogonality gives <q_U,r_U>=0 and ||r_U||^2=O(L^2). Expanding r=D_T q_U+r_U yields exactly

    R=n+R_U,
    <r,D_S r>=t3(T)-k_L n+<r_U,D_U r_U>.

The possible cross term involving integral D_T^2 is zero specifically because <q_U,r_U>=0, not merely because integral D_T=0. The remaining error is bounded by 2L R_U=O(L^3).

The W1 shifted quadratic form on delta_0-a 1_T is k-2na+a^2(kn+t3). Nonnegativity for every real a forces t3>=n^2/k-kn. With k=o(sqrt(n)) and L=O(k), both O(kn) and O(k^3) are o(n^2/k), while R=n+O(k^2) is asymptotic to n. Thus g>=(1-o(1))n/k, and g/sqrt(n) tends to infinity. The premise here is supplied by the deterministic layers, so “hypothetical” in Section 5 is now unnecessary wording, though not a mathematical defect.

## Checks and reproducibility

Run `OPENBLAS_NUM_THREADS=1 python check_groundstate_obstruction.py` from this directory. Output is stored in `check_groundstate_obstruction.json`.

The script exhaustively checks incidence and degree/error identities for (r,k)=(4,1),(5,1),(6,2),(7,2),(8,2); confirms the cone enclosure with full eigenvalue computations; checks interval odd formulas and gaps through L=100; and checks the exact leakage identity by direct coefficient convolution for T={-3,-1,1,3}, L=40. All assertions passed. The finite implant test has a simple bottom and zero T-axis/center groundstate coefficients, as predicted.

## Scope of the conclusion

This eliminates a universal repair principle based on the unique W1 bottom mode, even when its entire parity-preserving exterior resolvent is retained. It does not eliminate certificates carried by the opposite parity sector, general adapted W2 vectors, full W2, or universal Chowla. That boundary is essential and is correctly stated in the main report.
