# Independent audit: exterior dichotomy fails, while full W2 remains strong

20 October 2026. This independently audits the direct-union proposal and proves a full-W2 certificate on the same random tapered family. It is not a universal Chowla or full-W2 theorem. The only imported estimate is the previously proved tapered selected-adjacency bound, identified below. All other arguments are given here.

## 1. Definitions

For a finite symmetric nonempty support T in Z excluding 0, write

- n = |T|,
- I(T) = {0} union T,
- W2(T) = I(T) + I(T),
- E(T) = W2(T) minus I(T),
- C_T = (1_T(u-v)) indexed by u,v in T,
- B_V = (1_T(u-v)) indexed by u,v in V,
- K_V(T) = -lambda_min(B_V), and K_global(T) = -min D_T.

For m copies of the same T on independent axes, put

    S = union_{j=1}^m {t e_j : t in T} in Z^m.

Then |S| = mn. All statements below transfer to integer supports by a carry-free encoding; see section 6.

## 2. Exact exterior decomposition

The exterior rows are exactly:

1. axis rows x e_i with x in E(T);
2. pair rows t e_i + u e_j with i<j and t,u in T.

There are no edges between distinct blocks of these types. Two distinct axis blocks have a difference nonzero in two coordinates. An axis-exterior row x e_i could connect to a pair row t e_i+u e_j only if x=t, impossible because x is outside I(T) and t is in T. A difference of rows in different pair-index blocks has at least two nonzero coordinates. Each fixed pair-index block has matrix

    C_T tensor Id_n + Id_n tensor C_T.

Consequently, for m>=2,

    K_E(S) = max(K_E(T), 2 K_T(T)),                    (2.1)

where K_T(T) = -lambda_min(C_T). This is an exact spectrum identity, not a graph analogy or an asymptotic approximation.

Suppose

    C_T >= a J - delta Id,   a>0, delta>=0.            (2.2)

The W1 matrix consists of m diagonal C_T blocks and a center joined to each leaf. For center coordinate z and leaf vectors v_i, let b_i=sum_t (v_i)_t. Its quadratic form is bounded below by

    2 Re(conj(z) sum_i b_i) + a sum_i |b_i|^2
      - delta sum_i ||v_i||^2
    = a sum_i |b_i+z/a|^2 - (m/a)|z|^2
      - delta sum_i ||v_i||^2.

Thus

    K_W1(S) <= max(delta, m/a).                       (2.3)

## 3. A simultaneous tapered base

For X an integer tending to infinity, take alpha=X^(-1/4). Let eta_b, 1<=b<X, be independent Bernoulli variables with

    p_b = 2 alpha (1-b/X),

and let T = {+/-b : eta_b=1}. Put n0=2 sum_b p_b=2 alpha(X-1). Then n/n0 tends to 1 in probability.

The previously established selected-adjacency theorem gives

    C_T >= (2 alpha/3) J - delta Id,
    E delta = O(alpha sqrt(X log(4X)) + log(4X) + alpha).

The source is `../dependencies/weak_w1_taper_proof.md`, sections 1-2. The three-color decoupling and interval-feature proof were checked: signclass coincidences are isolated, the rectangular Bernstein variance includes off-diagonal products, and the feature bound is genuinely rank one rather than only PSD.

The mean Fourier polynomial is exactly

    mu(theta) = E D_T(theta) = 2 alpha(F_X(theta)-1),

where the Fejer kernel F_X has coefficients (1-|b|/X)_+ and is nonnegative. Let

    Z = D_T - mu.

A Bernstein tail bound on a sufficiently fine O(X)-point trigonometric grid, followed by the degree-X Bernstein derivative inequality, gives with probability tending to 1

    ||Z||_infinity = O(sqrt(n0 log X) + log X).

For example, each grid value is a sum of independent centered summands 2(eta_b-p_b)cos(b theta), bounded by 2 and with total variance at most 4 sum_b p_b=2n0. A grid of mesh at most 1/(4X), in radians, bounds the continuous supremum by twice the maximum grid value via ||Z'||_infinity<=X||Z||_infinity.

Since mu>=-2alpha,

    K_global(T) <= 2alpha + ||Z||_infinity
                = O(sqrt(n0 log X) + log X).         (3.1)

The matrix-noise estimate and the supremum estimate can hold on the same realization. Choose a sufficiently large absolute multiple in Markov's inequality for delta, then intersect with the high-probability cardinality and supremum events. Additional events needed in section 5 can also be included, as detailed there.

## 4. Failure of the proposed W1-or-exterior dichotomy

Take m=floor(X^(1/8)). Select a simultaneous good base from section 3. Then

    n comparable to X^(3/4),    mn comparable to X^(7/8),
    sqrt(mn) comparable to X^(7/16).

Equations (2.1)-(3.1), and K_E(T), K_T(T)<=K_global(T), give

    K_E(S) = O(X^(3/8) sqrt(log X)),
    K_W1(S) = O(X^(3/8) + X^(1/4) sqrt(log X) + log X).

Therefore

    K_E(S)/sqrt(|S|) = O(X^(-1/16) sqrt(log X)) -> 0,
    K_W1(S)/sqrt(|S|) = O(X^(-1/16)) -> 0.

This disproves the existence of a universal c>0 such that every symmetric integer support satisfies either K_W1>=c sqrt(N) or K_E>=c sqrt(N).

Crucial limitation: this does not upper-bound the full W2 matrix. The omitted cross block has edges from singleton rows to pair rows and from I(T)-rows to E(T)-rows. In fact section 5 proves full W2 is strong for a simultaneous choice of these same bases.

## 5. Full W2 reaches square-root scale on the same counterfamily

### 5.1 Every needed centered coefficient is supported in W2(T)

With probability tending to 1,

    [-X,X] subset W2(T).                              (5.1)

For each integer h with 1<=h<=X, consider representations h=u+v with nonzero signed integers |u|,|v|<=floor(3X/4), excluding |u|=|v|. There are at least cX unordered representations for an absolute c>0 when X is large: the interval intersection [-3X/4,3X/4] intersect [h-3X/4,h+3X/4] has length at least X/2, and exclusions remove only O(1) endpoints/diagonals.

View such representations as edges on the positive signclasses |u|,|v|. A fixed signclass b is used in at most two edges, from the choices u=b or u=-b. Thus this graph has a matching of at least c'X edges. Each matching edge succeeds independently with probability p_|u| p_|v|>=alpha^2/4. Hence

    P(h not in T+T) <= exp(-c'' alpha^2 X).

A union bound over 1<=h<=X, plus symmetry and 0 in I(T), proves (5.1), since alpha^2 X=X^(1/2). This proof uses independence only for disjoint signclasses. In particular Z, whose frequencies lie in [-X,X] and whose constant coefficient is zero, is an admissible W2(T) polynomial.

### 5.2 The centered polynomial has cheap positive energy

Let

    V = ||Z||_2^2 = 2 sum_b (eta_b-p_b)^2,
    c0 = <D_T,Z> = 2 sum_b eta_b(1-p_b).

Since p_b<=2alpha, n=2 sum eta_b, and sum p_b^2=O(alpha n0), the cardinality event gives, deterministically,

    V = (1+O(alpha)) n,   c0 = (1+O(alpha)) n.         (5.2)

For the first identity use V=n-4 sum eta_b p_b+2 sum p_b^2; the error has absolute value O(alpha n)+O(alpha n0). The second identity is immediate.

Define the nonnegative random quantity

    P = integral 2alpha F_X Z^2 >= 0.

Writing v_b=Var(eta_b), independence gives

    E Z^2 = sum_b v_b(e_(2b)+2+e_(-2b)).

Consequently

    E P = 2alpha sum_b v_b[2+2(1-2b/X)_+]
        <= 8alpha sum_b v_b
        <= 4alpha n0.                                (5.3)

By Markov, P<=C alpha n0 with probability as close to 1 as any desired fixed constant, by taking C large. Intersect this event with the selected-adjacency Markov event and the high-probability cardinality, supremum and support-filling events. The intersection still has probability bounded away from zero for every sufficiently large X. Thus one can choose a deterministic sequence satisfying all assertions at once.

The normalized diagonal energy obeys

    d = integral D_T Z^2 / V
      = P/V - 2alpha + integral Z^3/V
      <= O(alpha) + ||Z||_infinity
      = O(sqrt(n log X) + log X).                     (5.4)

This upper bound is all the negative-eigenvalue estimate needs. A large negative d would only strengthen the certificate. No unjustified cancellation of the cubic noise term is used.

### 5.3 Axis-symmetric two-dimensional compression

On the m-dimensional torus let Z_i(theta)=Z(theta_i). By (5.1),

    q(theta) = (1/sqrt(m V)) sum_i Z_i(theta)

is supported in W2(S). Because each Z_i has mean zero, q has norm 1 and is orthogonal to 1. Multiplication by D_S=sum_i D_T(theta_i) has the exact compression on span{1,q}

    [[0, b], [b, d]],
    b = sqrt(m) c0/sqrt(V) = (1+O(alpha)) sqrt(mn).

All mixed-coordinate terms in the lower diagonal vanish because they contain a mean-zero factor; the remaining diagonal is exactly the single-base d in (5.4).

Now m=X^(1/8) gives d_+/sqrt(mn)->0, where d_+=max(d,0). The negative eigenvalue magnitude of this matrix is

    (sqrt(d^2+4b^2)-d)/2 >= b-d_+/2.

Therefore the same counterfamily satisfies

    K_W2(S) >= (1-o(1)) sqrt(|S|).                    (5.5)

This is a rigorous separation: both diagonal blocks I and E are sub-square-root, but their full matrix has a square-root negative direction. The trial uses centered Boolean noise; its coefficients on unselected lags live in E. It is not a direction confined to E and not a repair of one prescribed W1 eigenvector.

### 5.4 The entire noncentral block is weak, giving an exact limiting constant

The following stronger upper bound is independently checked here. Let U=W2(S) minus {0}, G=K_global(T), and retain C_T>=aJ-delta Id. Then

    K_U(S) <= max(G+(m-1)/a, 2delta).                 (5.6)

Indeed, the full-axis block on W2(T) minus {0} is bounded below by -G Id. Write a pair-block vector as an n-by-n matrix Y_ij, and write x_i for the singleton T coordinates on axis i. The pair-block positive mean energy and cross energy are

    a||Y_ij 1||^2 + a||Y_ij^T 1||^2
       +2 Re<x_i,Y_ij 1>+2 Re<x_j,Y_ij^T 1>.

Completing these two squares costs at most

    -(||x_i||^2+||x_j||^2)/a.

The remainder of the pair-block energy is at least -2delta||Y_ij||_F^2. Summing over pairs charges each singleton (m-1)/a, proving (5.6). Thus K_U=o(sqrt(N)) for our parameters.

The full W2 matrix is the sum of diag(0,B_U) and the center-star matrix. That star has norm sqrt(N), since its cross vector has exactly N unit entries. Therefore

    K_W2(S) <= sqrt(N)+K_U(S) = (1+o(1))sqrt(N).

Combined with (5.5), the same jointly chosen family has

    K_W2(S)/sqrt(N) -> 1,
    K_W1(S)/sqrt(N) -> 0,
    K_U(S)/sqrt(N) -> 0.                             (5.7)

So even allowing every noncentral row does not force a strong negative direction by itself. The asymptotically sharp direction necessarily couples the center to a well-chosen noncentral profile.

## 6. Transfer from independent axes to ordinary integers

All coordinates of S lie in [-X,X], and W2 coordinates lie in [-2X,2X]. Any relation tested for W2 adjacency has coordinate form u-v-s, with each coordinate of absolute value at most 5X. Choose an integer base Q>5X+1 and encode

    (x_1,...,x_m) -> sum_{j=1}^m x_j Q^(j-1).

A nonzero bounded coefficient vector c with |c_j|<=5X cannot encode to zero: its highest nonzero term has magnitude at least Q^h, while all lower terms total at most 5X(Q^h-1)/(Q-1)<Q^h. Thus W1/W2 row identities, membership and adjacency are preserved exactly. This transfers all spectral assertions to Boolean finite integer supports. The numerical exponents concern cardinality, not the potentially enormous largest encoded frequency.

## 7. Implication for the ongoing universal question

The exterior-only alternative is false even in the weak-W1 regime, for genuine torsion-free Boolean supports. A universal full-W2 proof cannot insist that all missing negativity be present in the exterior principal block; it must allow cross-block negative directions. The two-dimensional centered trial and matching upper bound prove that the full-W2 question survives this particular obstruction with exact limiting ratio 1. Neither direction establishes a universal full-W2 or Chowla theorem.

## 8. Joint deterministic selection and exact assembly check

If an explicit deterministic selection rule is desired, for each sufficiently large X choose the lexicographically first support among the finitely many candidates satisfying all of the following, with fixed sufficiently large absolute constants:

1. |n/n0-1|<=n0^(-1/4) (which holds with probability tending to 1 by Chebyshev; mere comparability also suffices for the deterministic coefficient normalization).
2. C_T>=(2alpha/3)J-delta0 Id, with delta0 an eightfold upper bound for the expected matrix-noise error plus 2alpha.
3. ||D_T-mu||_infinity<=C(sqrt(n0 log X)+log X).
4. [-X,X] is contained in W2(T).
5. integral 2alpha F_X(D_T-mu)^2<=32alpha n0.

Condition 2 fails with probability at most 1/8 after taking a sufficiently large certified constant; condition 5 fails with probability at most 1/8 by (5.3). Conditions 1, 3 and 4 hold with probability tending to 1. Their intersection has probability at least 1/2 for all sufficiently large X. Consequently such a choice exists, and the same selection satisfies every conclusion above. A lexicographic rule imposing only earlier, weaker conditions is not asserted to satisfy the new ones automatically.

The script `verify_direct_union.py` checks a small instance using integer arithmetic for the exterior block decomposition, carry-free encoded adjacency, centered-polynomial Gram, center coupling and diagonal energy. Its eigenvalues are floating diagnostics only; it is not used as proof of an asymptotic statement. Results are stored in `verify_direct_union_results.json`.
