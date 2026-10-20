# An interval implant defeats universal amplification by translated ground states

2026-10-20. Exact theorem and proof. This does not refute the full-W2 conjecture.

## Statement with no unproved random-model assumption

For S=-S subset Z\{0}, let I(S)={0} union S, k(S)=-lambda_min(B_I(S)). For a normalized bottom eigenvector q, define the translated-ground-state certificate

    Kprod(S,q) = -min_{0 != p, supp(p) subset I(S)}
                     integral D_S |q p|^2 / integral |q p|^2.

Its trial polynomials lie in W2. There is an absolute constant C such that for every nonempty T=-T subset Z\{0}, one can construct a Boolean integer support S with |S|>=|T| for which:

1. B_I(S) has a simple bottom eigenvalue, so q is unique up to scale;
2. k(S) <= C k(T);
3. Kprod(S,q) <= C k(T).

Consequently, a universal bound Kprod(S,q)>=c sqrt(|S|), even if required only when the bottom eigenvector is unique, implies a universal first-neighborhood bound k(T)>=c' sqrt(|T|). Conversely a universal first-neighborhood bound implies the product bound, since p=1 is allowed. Thus the two uniform square-root assertions are equivalent up to constants.

The signed-layer incidence construction in Section 6 supplies a rigorous sequence T_j with k(T_j)=o(sqrt(|T_j|)). Consequently this construction gives an actual Boolean integer sequence S_j with simple bottom eigenvectors and Kprod(S_j,q_j)=o(sqrt(|S_j|)). This refutes a universal square-root bound from the entire translated-bottom-vector space. The premise comes from the new deterministic incidence proof, NOT from the previously numerical E99c trend.

## 1. Interval ground state and a linear parity gap

Put U_L={-L,...,-1,1,...,L}, I_L=[-L,L]. B_L has entries 1 when 0<|a-b|<=L. Reflection a->-a commutes with B_L. Its lowest eigenvalue is simple and odd for all sufficiently large L. Write it -k_L. There is an absolute delta>0 such that, for all sufficiently large L,

    k_L = (2/(3*pi)+o(1)) L,
    lambda_min(B_L restricted to even vectors) + k_L >= delta L.

Here is a proof, rather than an empirical parity assertion. The scaled matrices converge in operator norm to the integral operator

    (F f)(x) = integral_{-1}^1 1[|x-y|<=1] f(y) dy

under the usual piecewise-constant mesh embedding. The discrepancy of the step kernels is supported in an O(1/L)-area neighborhood of |x-y|=1 (plus endpoints); hence its Hilbert-Schmidt norm is O(L^(-1/2)). Removing the diagonal changes the norm by O(1/L). Reflection is preserved.

For nonzero eigenvalue lambda, differentiate the integral equation on each half interval. It gives lambda^2 f''+f=0. On the positive half:

- Odd parity gives lambda f'(x)=f(1-x), and f(0)=0. With y=1/lambda, the boundary equations give cos y=0 and sin y=1. Thus nonzero odd eigenvalues are 1/(pi/2+2*pi*j), j integer. The least is -2/(3*pi), simple.
- Even parity gives lambda f'(x)=-f(1-x), f(1)=f(0)/2, and f'(0)=-f(0)/(2*lambda). Writing f(x)=a[cos(x/lambda)-sin(x/lambda)/2], the remaining endpoint equation gives cos y=4/5 and sin y=3/5. Thus nonzero even eigenvalues are 1/(theta+2*pi*j), where theta=arctan(3/4). The least is -1/(2*pi-theta), simple.

The gap between the even and odd bottom limits is

    Delta = 2/(3*pi) - 1/(2*pi-arctan(3/4)) > 0
          (approximately 0.0349).

Compact self-adjoint norm convergence preserves this isolated simple bottom eigenvalue and its parity, and gives any fixed delta<Delta for all large L. This proves the claimed gap. One may also use the exact odd-sector formula

    k_L = 1 + 1/[2 sin(3*pi/(4L+2))],  L>=2,

which follows by diagonalizing the anti-triangular matrix H_ab=1[a+b>L]. The continuum argument is needed only for the even-sector comparison.

## 2. Boolean direct-sum support and exact ground-state retention

Initially work in Z^2. Set

    S = (T x {0}) union ({0} x U_L).

In W1, the nonzero T and U coordinates have no edges between them. Write b for the all-ones vector indexed by T, and B_T^0 for the principal matrix on T without the center. At diagonal k_L, eliminating this T block subtracts only

    a = b^* (B_T^0+k_L I)^(-1) b

from the center diagonal of B_L+k_L I.

Take L so that k_L>k(T). Since the full first-neighborhood matrix for T at diagonal k(T) is positive semidefinite, its Schur complement (with the standard range condition if singular) implies

    0 <= a <= k(T).

Equivalently, this follows directly by minimizing the quadratic form and noting that increasing the T-block diagonal decreases the Schur correction.

The odd interval ground state has zero center coordinate. It therefore remains a zero eigenvector after the center correction. The entire odd sector is unaffected. On the even sector, B_L+k_L I is at least delta L I. If k(T)<delta L, subtracting a center rank-one form of norm at most k(T) leaves this sector strictly positive. Hence the full W1 matrix at diagonal k_L is PSD with a one-dimensional kernel consisting of the odd interval ground state. Thus

    k(S)=k_L,
    q(x,y)=q_L(y).

This is an exact ground-state statement, not merely a Rayleigh upper bound.

Choose L=ceil(C0 k(T)) with C0 an absolute sufficiently large constant. This ensures all preceding conditions, including the finite-size threshold. There is no issue when k(T) is small: every nonempty symmetric integer support contains the induced path {-m,0,m}, with m=max T and 2m not in T, so k(T)>=sqrt(2). Thus increasing C0 absorbs the fixed threshold. We have L=O(k(T)).

## 3. The entire translated space stays weak

Every p with frequencies in I(S) has the form

    p(x,y)=a(x)+b(y),

where a has frequencies in T and b has frequencies in {0} union U_L. For each fixed y, the x-polynomial q_L(y)p(x,y) has frequencies in {0} union T. By the definition of k(T),

    integral_x D_T(x) |q_L(y)p(x,y)|^2
        >= -k(T) integral_x |q_L(y)p(x,y)|^2.

Integrate in y. Also D_U(y)>=-2L pointwise. Therefore

    integral (D_T(x)+D_U(y)) |q_L(y)p(x,y)|^2
        >= -(k(T)+2L) integral |q_L(y)p(x,y)|^2.

This applies to EVERY p in the translated trial space, with no assumptions about signs, profiles, or independence. It proves

    Kprod(S,q_L) <= k(T)+2L = O(k(T)).

The obstruction is structural: multiplication by a ground state confined to the auxiliary coordinate does not create any T+T Fourier rows. The full W2 matrix does contain those rows. Therefore this theorem does not transfer to full W2.

## 4. Transfer back to integer frequencies

Let M=max |T| and choose Q>5M. Embed (t,u) as t+Q*u. On W2, differences relevant to deciding adjacency have first-coordinate magnitude at most 5M, so no carry can produce a false relation to S. Thus this map preserves all W1 and W2 adjacency relations, and in particular the product-space Gram and energy integrals (their nonzero Fourier relations have the same bound). It also preserves cardinality and Booleanity.

Consequently the construction is an actual finite symmetric integer support, not a finite-group or multivariate substitute.

## Interpretation

This is a precise obstruction to the proposal that translating the unique weakest first-neighborhood eigenvector universally supplies the missing square-root certificate. It is stronger than failure of a selected pair or of the raw-leakage aggregate. With the deterministic base supplied in Section 6, it is an unconditional bad sequence for this certificate. It is NOT a proof that full W2 fails and NOT a proof of Chowla.

## 5. Exact leakage and why the exterior cost is genuinely hostile

The same construction isolates the limitation of a raw ground-state leakage estimate. Let r_U=(D_U+k_L)q_L and R_U=||r_U||^2. In the direct sum,

    r=(D_S+k_L)q_L = D_T q_L+r_U,
    R=||r||^2 = |T|+R_U.

The cross term vanishes because D_T has mean zero. In particular R>=|T|: leakage is plentiful, not absent. Also R_U=O(L^2).

Write n=|T| and t3(T)=integral D_T^3. Orthogonality, together with <q_L,r_U>=0, gives the exact exterior numerator

    <r,D_S r> = t3(T)-k_L n + <r_U,D_U r_U>.

The first-neighborhood PSD condition itself implies

    t3(T) >= n^2/k(T)-k(T)n.

Indeed, apply its quadratic form to the coefficient vector delta_0-a 1_T and demand a nonpositive discriminant. The last residual term has absolute value at most 2L R_U=O(L^3).

For the proved weak-W1 sequence with k(T)=o(sqrt(n)), take L=O(k(T)) as above. Then

    R=(1+o(1))n,
    g=<r,D_S r>/R >= (1-o(1)) n/k(T) >> sqrt(n).

Thus even an optimal universal lower estimate R>=c n would not make the q,r test work here. The exterior Rayleigh cost is forced to be large and positive by the same weak-W1 hypothesis. The full translated-space upper bound already proves its failure to amplify, and this calculation identifies the precise cost mechanism. A new full-W2 argument must use exterior directions outside the translated ground-state space.

## 6. A proved weak-W1 base: balanced signed layers

This deterministic construction was checked algebraically during this proof attempt. It replaces, rather than assumes, the earlier numerical E99c premise.

Fix k>=1. In Z^r, let T_{r,k} consist of vectors with exactly k coordinates +1, k coordinates -1, and all remaining coordinates zero. Then

    n=|T_{r,k}|=binom(r,k) binom(r-k,k)
      =(1+o(1)) r^(2k)/(k!)^2

as r->infinity with k fixed.

Let A be the adjacency matrix on T_{r,k} without the center. For s,t in T, write c(s,t) for the number of coordinate positions where they share the same nonzero sign, and o(s,t) for positions where they have opposite nonzero signs. The difference s-t belongs to T exactly when

    o(s,t)=0 and c(s,t)=k.

Indeed opposite overlap creates a forbidden digit +/-2; with no opposite overlap, support(s-t) has size 4k-2c, so it has size 2k precisely at c=k. Its coordinate sum is zero, guaranteeing k of each sign.

Index rows R of an incidence matrix Z by all signed coordinate sets of size k, and columns by s in T. Put Z_R,s=1 if R is a signed subset of s. Then

    (Z^* Z)_st=binom(c(s,t),k).

This agrees with A_st unless s,t have at least k+1 common coordinate positions: either c>k, or c=k and o>=1. For each fixed s the number of such exceptional t is O_k(r^(k-1)), because at least k+1 of t's 2k nonzero positions have already been chosen from the fixed 2k positions of s. Every error entry is bounded by binom(2k,k). Therefore

    ||A-Z^*Z||op <= max_row sum_absolute_errors
                  = O_k(r^(k-1)),
    lambda_min(A) >= -O_k(r^(k-1)).

The diagonal is included among the exceptional pairs; no diagonal correction is omitted.

Coordinate permutations act transitively on T, so A is regular. Its exact degree is

    d = sum_(a=0)^k binom(k,a)^2
            binom(r-2k,k-a) binom(r-3k+a,a).

Here a matching positive positions and k-a matching negative positions are chosen from s; the remaining signed positions of t must lie outside support(s). Thus

    d = (r^k/k!) F_k + O_k(r^(k-1)),
    F_k=sum_(a=0)^k binom(k,a)^3.

The full W1 matrix is the cone over A. On the center and uniform vector its matrix is [[0,sqrt(n)],[sqrt(n),d]]. On the orthogonal complement it equals A. Hence

    k(T_{r,k})/sqrt(n) -> c_k,
    c_k=(sqrt(F_k^2+4)-F_k)/2.

The negative eigenvalues from the orthogonal complement contribute only O_k(1/r) after normalization. Since F_k->infinity, c_k->0. Choosing k->infinity and then r sufficiently large for each k produces a diagonal sequence with k(T)=o(sqrt(|T|)). All quantifiers are explicit: the proof first fixes k, takes r->infinity, and only then chooses the diagonal. No uniform-in-k error estimate is being asserted.

Finally embed Z^r in Z by s -> sum_(j=0)^(r-1) s_j 7^j. Every relation used in the full W2 adjacency test has coordinate coefficients bounded by 5. For base 7 a highest nonzero coefficient cannot be cancelled by all lower coefficients, since their maximum magnitude is 5(7^m-1)/6<7^m. Thus the embedding is injective and preserves all relevant adjacency relations. This yields genuine Boolean integer supports with the stated weak-W1 property.

Applying Sections 1-4 to this sequence proves the unconditional failure of the translated-unique-ground-state square-root certificate. Full W2 remains untouched by this no-amplification theorem.

### 6.1 Exact row counts and an explicit diagonal sequence

The preceding error estimate can be sharpened to an exact regular row count. The degree formula simplifies to

    d=F_k binom(r-2k,k).

For the Gram G=Z^*Z, its row sum is

    F_k binom(r-k,k).

To verify the latter, choose a signed k-subset R of a fixed column s: if R has a positive signs, there are binom(k,a)^2 choices. Complete R to a member of T by choosing k positions outside R and choosing their remaining signs, in binom(r-k,k) binom(k,a) ways. Sum over a.

Since A<=G entrywise, E=G-A is symmetric, nonnegative and regular, with exact row sum

    e=F_k [binom(r-k,k)-binom(r-2k,k)].

Therefore ||E||op=e and lambda_min(A)>=-e, without unspecified constants. Writing

    kcentral=(sqrt(d^2+4n)-d)/2,

we have the finite rigorous enclosure

    kcentral <= k(T_{r,k}) <= max(kcentral,e).

For r>=4 F_k^2 k^2, elementary products of binomial ratios give

    e/sqrt(n) <= F_k k^2/(r-2k+1) <= 1/F_k,
    d/sqrt(n) >= F_k [1-2k^2/(r-k+1)] >= F_k/2.

(The inequality product(1-x_i)>=1-sum x_i is used with nonnegative x_i.) Since kcentral<=n/d,

    k(T_{r,k})/sqrt(n) <= 2/F_k.

Thus taking the explicit integer r_k=ceil(4F_k^2 k^2), with k->infinity, gives a proved weak-W1 sequence. No unspecified diagonal selection, concentration assertion, or numerical extrapolation is necessary.

## 7. Stronger obstruction: even the full odd-sector exterior resolvent cannot repair this mode

Reflection y->-y commutes with the full W2 matrix. Its full odd sector is a complementary trial space, not a superset of the translated-ground-state space, and it too has a small negative minimum.

Indeed, the W2 row set of the direct sum is

    (({0} union T union (T+T)) x {0})
    union ({0} x ({0} union U union (U+U)))
    union (T x U).

Every row with x-coordinate outside {0} union T has y=0. An odd-in-y coefficient vector vanishes at every such row. Consequently an arbitrary polynomial F in the entire odd W2 sector, for each fixed y, has x-Fourier support in {0} union T. The same fixed-y positivity argument gives

    integral D_S |F|^2 >= -(k(T)+2L) ||F||^2.

Thus

    K_W2,odd <= k(T)+2L = O(k(T)).

The unique W1 ground state is odd. Its exterior coupling C^*q is odd, and the full exterior matrix and its resolvent preserve parity. Therefore optimizing over ALL exterior directions coupled to this ground state cannot leave this weak odd sector. This is not merely failure of a chosen exterior profile or of a two-vector estimate: the complete cost-weighted resolvent seen by the bottom mode has no square-root repair on the constructed sequence.

There is an important limitation. The even exterior sector may already have a large negative eigenvalue. If so, the full-W2 square-root certificate comes from that sector without coupling to the old ground state. The theorem does not rule this out and does not refute the full-W2 conjecture. It rules out a proof that universally attributes the missing square-root negativity to amplification of the first-neighborhood bottom mode, even with its complete exterior resolvent retained.
