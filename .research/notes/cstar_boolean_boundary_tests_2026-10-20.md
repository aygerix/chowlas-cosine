# Boolean cross-frequency attempt: boundary Schur tests fail quantitatively

Status: a concrete attempted universal inequality is refuted, including in the high-ratio regime. No advance on universal C*. The exact obstruction below is stronger than the generic weight-agnostic Schur observation. It is a finite Boolean, torsion-free example, and specifies exactly which families of principal minors pass. No claim is made that all small arbitrary principal minors pass.

## Scope and existing-record check

Read CSTAR, STATE, P61–P63, P65's arithmetic/partial-convolution barriers, P77–P81, and the ROUTES entries for integral Gram lattices, P9/self-difference graphs and factor windowing. The proposed mechanism was: internal simultaneous Boolean Toeplitz constraints create an almost-full nullspace, then band-edge rows cannot remain in the internal range. If a single boundary row had squared nullspace leakage comparable to |S|, a Schur complement would force K comparable to sqrt(|S|). This is not asserted as a new route after the counterexample below. External priority has not been checked; the matrix calculation is elementary.

## 1. Attempted inequality and exact Schur derivation

For finite symmetric S in Z, write B_I=(1_S(i-j)) over a finite row set I. Suppose H=K I+B_I is positive semidefinite and P projects onto ker H. For an exterior row x, let b_x=(1_S(x-i))_{i in I}.

If the enlarged Toeplitz matrix is positive semidefinite at diagonal K+delta, its compression to ker H plus the new row is

    [[delta I, P b_x], [(P b_x)*, K+delta]].

Consequently

    delta(K+delta) >= ||P b_x||_2^2.                   (1)

The concrete prediction tested was:

    max_{x outside I} ||P b_x||_2^2 >= c |S|,         (BR)

when |S|/K^2 is large and dim ker H / |I| is close to one. This would force the desired square-root increment. (1) alone is weight-agnostic and does not advance C*. The task was to establish (BR) using exact Booleanity plus finite support.

## 2. Exact high-ratio Boolean counterexample to (BR), in Z

Choose integers d>=2, m>=2, and B=8m. Let

    S = { +/- t B^j : 1<=t<=m-1, 0<=j<d },
    I = { sum_{j=0}^{d-1} u_j B^j : 0<=u_j<=m-1 }.

Then |S|=2d(m-1), |I|=m^d. Base-B uniqueness (no carries in digit differences of magnitude <=3m) identifies the internal adjacency with the Cartesian product of complete graphs:

    H = d I + B_I
      = sum_{j=1}^d I_m tensor ... tensor J_m tensor ... tensor I_m.

Thus H is PSD at K=d and

    ker H = (1^perp) tensor ... tensor (1^perp),
    dim ker H = (m-1)^d.

Now take ANY integer x outside I. If x has a neighbor in I, write x=y+t B^j with y in I, 0<|t|<=m-1. This gives a digit vector for x in [-m+1,2m-2]^d. Any second such representation has the same digit vector, because their difference has all digits of magnitude <=3m and B=8m makes the encoding injective. If neighbors occurred in two different coordinate directions, each representation would force the other's altered coordinate to lie in [0,m-1]; all coordinates of x would then lie in that interval, so x would be in I, contradiction.

Therefore every exterior row meets I in at most ONE coordinate fibre, and

    ||b_x||_2^2 <= m,
    ||P b_x||_2^2 <= m,
    max_x ||P b_x||_2^2 / |S| <= m/[2d(m-1)].       (2)

Set m=d^2. Then

    |S|/K^2 = 2(d^2-1)/d -> infinity,
    dim ker H / |I| = (1-1/d^2)^d -> 1,
    max_x ||P b_x||^2 / |S| <= (1+o(1))/(2d) -> 0.

This disproves (BR) even with every proposed favorable premise: exact 0/1 coefficients, finite integer support, arbitrarily high local ratio, a PSD block with almost-full kernel, and arbitrary exterior integer rows (not only adjacent rows or a preselected direction).

This is NOT a Chowla counterexample: K=d is a local relaxation value, not the global minimum cost. In fact take x=6/(B-1). Then B^j x=x modulo 1 for every j, and the full polynomial equals d times [sin((2m-1)pi x)/sin(pi x)-1]. Thus its true global cost is at least (4/(3pi)+o(1))dm as m grows, and is Theta(dm). The example obstructs inferring this global cost from one boundary row. The geometry spreads the boundary loss across d independent coordinate directions.

## 3. Stronger family of passing simultaneous constraints

Let t>=1, and let J be ANY set of t exterior integers. Write C=(1_S(i-j))_{i in I,j in J}, and B_J for their adjacency. Each column of C has at most m ones, so

    ||C||op <= ||C||F <= sqrt(tm),
    ||B_J||op <= t-1.

Starting with diag(H, d I_t), which is PSD, the added block matrix [[0,C],[C*,B_J]] has lowest eigenvalue at least -sqrt(tm)-(t-1). Hence the entire Boolean principal block on I union J is PSD with diagonal

    K_t = d + sqrt(tm) + t - 1.                    (3)

This holds simultaneously for EVERY exterior J of cardinality t. Every principal submatrix of every such block also passes.

For m=d^2 and t=o(d),

    |S|/K_t^2 -> infinity.

For instance t=1 gives K_1=2d and |S|/K_1^2~d/2. The interior block has d^(2d) rows, and it remains consistent at an arbitrarily bad Chowla ratio after adding any one arbitrary exterior row. Even an unbounded number t=o(d) of arbitrary boundary rows can be absorbed without reaching square-root scale.

Precisely NOT established: arbitrary principal row sets of size <=|I|, or all contiguous Toeplitz sections, pass. The statement concerns subsets of this specified I together with at most t arbitrary exterior rows. Calling this a general finite-order Toeplitz blindness theorem would be incorrect.

## 4. Explicit finite-group test and a successful fixed-rank toy

The same internal block comes from a finite-group high-ratio example. For p=2m-1 prime, take in F_p^d the union of the d nonzero coordinate axes. Its Fourier transform has minimum -d and |S|=d(p-1), so |S|/d^2=(p-1)/d. The integer S above is its centered, base-B one-representative lift. Thus (2)-(3) are tested against an explicit exact Boolean finite-group high-ratio family, not merely P61's fractional packets.

For d=2 one can see the desired boundary leakage directly, and also its failure to scale with rank. Use the box {0,...,m-1}^2 before encoding. Take x=(m-1+q,y), with q between 1 and m-1 and 0<=y<m. Its nonzero entries lie on a fibre of length ell=m-q. With P0=I-J/m,

    P=P0 tensor P0,
    ||P b_x||^2 = (ell-ell^2/m)(1-1/m).

Choosing ell=floor(m/2) gives approximately m/4, comparable to |S|=4(m-1) at fixed rank. Equation (1) yields

    K_global >= 1+sqrt(1+||P b_x||^2),

a square-root bound for this toy. For general d the exact analogous formula is

    ||P b_x||^2 = (ell-ell^2/m)(1-1/m)^(d-1),

still only order m, whereas |S| is order dm. The missing factor d is real, not an estimate artifact. This fixed-rank success must not be sold as progress on the universal problem.

## 5. Simpler warning: singularity alone gives no leakage

For S={-1,1}, I={1,...,L}, take K_L=2cos(pi/(L+1)). The matrix K_L I+Adj(path_L) is PSD singular, with normalized kernel vector proportional to (-1)^j sin(j pi/(L+1)). Every exterior row is zero or an endpoint vector. Thus

    max_x ||P b_x||^2 = 2 sin^2(pi/(L+1))/(L+1) ~ 2 pi^2/L^3.

This already refutes a residual bound without the high-ratio premise. Section 2 is needed to refute the stronger, relevant version with high local ratio and almost-full kernel.

## Verdict

For a genuinely nonnegative, nonzero trigonometric polynomial, every finite Toeplitz principal Gram matrix is strictly positive definite: the integral of the polynomial times the squared modulus of a nonzero finite exponential sum is positive. Exact kernels above therefore occur at the boundary of a finite relaxation, not at a globally feasible density. A universal version would need quantitative approximate kernels; exact singularity alone cannot be assumed.

The attempted Boolean-specific step (BR) is false. Determinant nonvanishing or integrality cannot repair it: the high-rank example has exact zeros and exact Boolean constraints, and its residual is explicitly too small by a factor d. A bounded-boundary-row extension of a giant PSD test block is therefore insufficient. Aggregate constraints spanning a number of independent boundary directions that grows with rank are necessary for this strategy. No universal lower bound for those aggregate constraints was proved; replacing (BR) by such a bound would be another unproved C* ingredient, not a result.
