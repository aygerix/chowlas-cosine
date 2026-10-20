# Full-W2 tensor powering cannot amplify a finite deficit

Let S be a nonempty finite symmetric subset of Z^r\{0}, N=|S|, T={0} union S, W=T+T, and B=(1_S(u-v)) indexed by W. Write K=-lambda_min(B), rho=lambda_max(B).
For d>=1 put S_d=T^d\{0}. This is an exact Boolean symmetric support, N_d=(N+1)^d-1.

**Exact full-operator identity.** W2(S_d)=(T+T)^d=W^d, since W2(S_d)=({0} union S_d)+({0} union S_d). Moreover 1_{S_d}(u-v)+1_{u=v}=prod_i 1_T(u_i-v_i). Hence

    I+B_{W2(S_d)}=(I+B)^{tensor d}.

All eigenvalues, not just an invariant trial subspace, are products of d eigenvalues of I+B, minus 1.

**Uniform ingredients.** rho>=sqrt(N): use the nonnegative star vector with value sqrt(N) at 0 and value 1 on S. Its center-neighbor contributions alone give Rayleigh quotient sqrt(N); extra edges only increase it. Also K>=sqrt(2): choose s in S maximizing a generic linear functional, with its sign chosen positive. Then 2s not in S, and the principal submatrix on {0,s,2s} is the three-vertex path, of minimum eigenvalue -sqrt(2).

Choose one eigenvalue 1-K<0 and d-1 eigenvalues 1+rho>0 in the tensor product. Therefore

    K_d >= 1+(K-1)(1+rho)^(d-1).

Since 1+rho >= 1+sqrt(N) > sqrt(N+1), for every fixed base S,

    K_d/sqrt(N_d) -> infinity exponentially.

In fact the exact minimum product is -(K-1)(1+rho)^(d-1), because B is entrywise nonnegative symmetric, so every eigenvalue of I+B has absolute value at most 1+rho, and every negative eigenvalue has magnitude at most K-1. An odd number of negative factors is maximized in magnitude by exactly one most-negative factor, since K-1<=1+rho. Thus equality holds:

    K_d = 1+(K-1)(1+rho)^(d-1).

This rules out tensor-power amplification of a finite local sharp-constant deficit. It does not settle arbitrary hierarchical supports or any universal W2 bound.

**Transfer to integers.** The calculation is in a torsion-free lattice. A base expansion with base larger than the coordinate ranges of every relation u-v-s under consideration preserves W2 and its entire adjacency matrix. Thus the obstruction also applies to carry-free integer realizations.

## Categorical powers without adding zero

The following complementary calculation gives the categorical-product case. Put R_d=S^d (no zero coordinates), T=S+S, p=lambda_max(B_T), k=-lambda_min(B_T). Then W2(R_d)=S^d union T^d, since 0 belongs to T. The principal matrix on T^d is B_T^{tensor d}.

If S intersects T, choose a in the intersection. Both a and a+S lie in T. The star on these N neighbors yields p>=sqrt(N). Choosing an extreme s in S also gives the induced three-vertex path {a-s,a,a+s}, so k>=sqrt(2). Thus K_W2(R_d)>=k p^(d-1)>=k N^((d-1)/2).

If S and T are disjoint, B_S=0: an edge u-v in S with u,v in S would imply u=v+(u-v) in S+S. Let C be the rectangular matrix between S and T. Its column at 0 is all ones, so sigma=||C||>=sqrt(N). The full matrix is exactly

    [[0, C^{tensor d}], [(C^*)^{tensor d}, B_T^{tensor d}]].

If p>=sqrt(N), then p>0 and the zero-diagonal B_T has k>0, so the same principal lower bound applies. Otherwise p<sqrt(N), and compression onto left/right top singular vectors of C^{tensor d} yields

    K_W2(R_d) >= (sqrt(p^(2d)+4 sigma^(2d))-p^d)/2.

Here ||B_T||=p by Perron-Frobenius, so the lower-right scalar is at most p^d; monotonicity of the negative eigenvalue gives the inequality. It follows that liminf K_W2(R_d)/N^(d/2)>=1 in this case.

Hence categorical powers of any fixed nonempty finite symmetric torsion-free base cannot drive the normalized full-W2 certificate to zero either. The constants in the first cases can depend on the fixed base, so this does not address simultaneously changing bases.

### Stronger isolated-leaf bound for categorical powers

Let H=S intersect (S+S), h=|H|. Every vertex in S\H is isolated in B_S: if s-t is in S for s,t in S, then s=t+(s-t) belongs to S+S (and symmetry gives the same for t).

For S^d the corresponding active subset is exactly H^d. Therefore the induced W1 star with center 0 and leaves S^d\H^d is an actual star, with N^d-h^d leaves. It follows that

    K_W2(S^d)/N^(d/2) >= sqrt(1-(h/N)^d).

If h<N for a fixed base, this tends to 1. Sum-free bases (h=0) give the bound 1 immediately at every power. If S is contained in S+S, then W2=S+S and the exact categorical identity B_d=B_W2^{tensor d} holds; its most-negative eigenvalue is -(K_1)(rho_1)^(d-1), so K_d/sqrt(N^d)>=K_1/sqrt(N) because rho_1>=sqrt(N).

For changing bases S_d, a necessary condition for a normalized categorical certificate to vanish is

    d |S_d\(S_d+S_d)|/|S_d| -> 0.

This follows because 1-(1-r_d)^d ->0 requires d r_d ->0. It is a necessary condition, not a sufficiency statement or a universal Chowla proof.

## Heterogeneous unitized products: every factor must already fail

The fixed-base restriction can be removed for unitized products. Take arbitrary nonempty finite symmetric torsion-free supports S_i, with N_i=|S_i|, W_i=({0} union S_i)+({0} union S_i), K_i=-lambda_min(B_i), rho_i=lambda_max(B_i). For

    S_* = product_i ({0} union S_i) \ {0},
    N_* = product_i (N_i+1)-1,

one has exactly

    I+B_* = tensor_i (I+B_i),
    K_* = 1+max_i [(K_i-1) product_{j!=i}(1+rho_j)].

The minimum product uses one negative factor: any odd number of negative factors can be replaced, except one, by positive Perron factors without decreasing its magnitude. Each K_i>=sqrt(2), rho_i>=sqrt(N_i), N_i>=2. Therefore

    K_*/sqrt(N_*) >= max_i (K_i-1)/sqrt(N_i+1)
      >= ((sqrt(2)-1)/sqrt(3)) max_i K_i/sqrt(N_i).

The first inequality also includes all remaining factors (1+rho_j)/sqrt(N_j+1)>1. The second uses

    (1-1/K_i)sqrt(N_i/(N_i+1))
      >= (1-1/sqrt(2))sqrt(2/3)=(sqrt(2)-1)/sqrt(3).

Thus a vanishing normalized certificate for heterogeneous unitized products would require every constituent factor's normalized full-W2 certificate to vanish already. This is a rigorous non-amplification theorem, not merely a fixed-base asymptotic observation.

For heterogeneous categorical products with S_i contained in S_i+S_i for every i, the analogous exact identity B_*=tensor_i B_i gives the still stronger bound

    K_*/sqrt(product_i N_i) >= max_i K_i/sqrt(N_i).

For general heterogeneous categorical products, the isolated-leaf argument gives

    K_*/sqrt(product_i N_i) >= sqrt(1-product_i |S_i intersect(S_i+S_i)|/N_i).

Hence a possible escape requires the sum of the missing overlap fractions to tend to zero. This last necessary condition alone does not settle the remaining near-contained heterogeneous case.

### Fixed categorical powers: stronger final dichotomy

If S is contained in T=S+S, every s in S has at least one neighbor in B_S: write s=a+b with a,b in S; then a is a distinct vertex and s-a=b is in S. The uniform-on-S compression with the central vertex 0 therefore has lower-right entry at least 1. Since W1 is contained in T,

    rho_T >= (1+sqrt(1+4N))/2 > sqrt(N).

Thus in the contained case the exact tensor formula gives K_d/sqrt(N^d) tending to infinity exponentially. In the non-contained case the isolated-leaf lower bound tends to 1. Therefore every fixed nonempty finite symmetric torsion-free base satisfies the stronger conclusion

    liminf_{d->infinity} K_W2(S^d)/sqrt(N^d) >= 1.

This does not eliminate the changing-base near-contained loophole described above.
