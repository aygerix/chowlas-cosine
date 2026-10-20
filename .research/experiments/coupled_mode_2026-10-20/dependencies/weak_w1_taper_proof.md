# A weak-W1 tapered family by three-color decoupling

20 October 2026. New derivation, independently checked in this research pass. This is a W1 obstruction, NOT a Chowla counterexample.

## Statement

There are finite symmetric integer supports S_j with N_j→∞ and K_W1(S_j)=o(√N_j).

More quantitatively, let 0<α≤1/2 and X≥2. Independently select a∈{1,...,X} with probability p_a=2α(1−a/X), and reflect. Put μ=α(X−1)=E|A|. There is a universal C such that, with positive probability bounded away from zero when μ→∞,

    |A|≍αX,
    K_W1 ≤ C[α√(X log(4X))+log(4X)+α^−1].

Take X=t^4, α=1/t. With positive probability N≍t^3 and K_W1=O(t√log t)=o(t^(3/2)). Moreover K_W1/√N→0 in probability: divide the expectation bound by √μ, use Markov at any fixed positive threshold, and use |A|/μ→1.

## 1. The masked centered noise

Let η_a be the independent Bernoulli variables, ξ_a=η_a−p_a, extended by zero outside 1≤a≤X. On the fixed ambient vertex set V={−X,...,−1,1,...,X}, let

    Z_uv = η_|u| η_|v| ξ_|u−v|   (u≠v),    Z_uu=0.

We claim

    E||Z|| ≤ C[α√(X log(4X))+log(4X)+1].               (1)

The dependence between endpoints and differences is NOT discarded. Separate pairs for which the three positive indices |u|,|v|,|u−v| fail to be distinct. For u,v≠0 and u≠v these are precisely among

    v=−u, v=2u, v=u/2.

There are at most three per row/column. Their matrix has operator norm at most 3 by row/column absolute sums.

For all remaining pairs, independently color the positive indices 1,...,X uniformly with colors 1,2,3. Define Z^c by keeping only entries with

    color(|u|)=1, color(|v|)=2, color(|u−v|)=3.

For each fixed Bernoulli realization, the exact entrywise identity is

    Z_good = 27 E_color Z^c.

Thus E||Z_good||≤27 E_color E_η||Z^c||. The matrix Z^c is rectangular in effect, despite retaining an ambient square indexing; symmetry is not needed.

Condition on the coloring and all Bernoulli endpoint variables of colors 1 and 2. For each lag d of color3, define M_d to have entries η_|u|η_|v| when u is color1, v color2 and |u−v|=d, zero otherwise. Then

    Z^c = Σ_(d:color3) ξ_d M_d.

The remaining ξ_d are independent and centered conditional on all the endpoint data. Every M_d is a 0/1 matrix with at most two ones in each row and column, so ||M_d||≤2.

Let n_1,n_2 denote the numbers of selected signed endpoints of colors1,2, and n_*=n_1+n_2. Since Var ξ_d≤p_d≤2α, the two rectangular variance sums satisfy

    ||Σ Var(ξ_d) M_d M_d*|| ≤ 4α n_2,
    ||Σ Var(ξ_d) M_d* M_d|| ≤ 4α n_1.                 (2)

For example, the row sum of the first sum at u is at most

    2α Σ_d Σ_v (M_d)_(u,v) Σ_u' (M_d)_(u',v)
      ≤ 4α Σ_d Σ_v (M_d)_(u,v) ≤ 4α n_2.

The last inequality holds because for a fixed pair u,v its absolute lag d is unique. These variance matrices are symmetric entrywise nonnegative, so maximum row sum bounds their operator norms. This verifies (2), including possible nonzero off-diagonal entries of M_dM_d*.

Rectangular matrix Bernstein, integrated in t, now gives conditionally

    E_lags ||Z^c|| ≤ C[√(α n_* log(4X))+log(4X)].

Taking expectations and using concavity of square root and E n_*≤2μ≤2αX proves (1). No claim of independence between original graph entries has been made.

The only imported result is rectangular matrix Bernstein. One source is Tropp, User-Friendly Tail Bounds for Sums of Random Matrices, Theorem1.6, https://tropp.caltech.edu/papers/Tro11-User-Friendly-preprint.pdf. It bounds the norm tail by (d1+d2) exp(−t²/[2(σ²+Rt/3)]); here d1+d2≤4X, R≤2, σ²≤4αn_*. Integrating that stated tail yields the displayed expectation estimate with an absolute constant.

## 2. A rank-one lower bound for the mean kernel

Set p_0=2α and p_d=2α(1−|d|/X)_+ for all integer d. The deterministic kernel P_uv=p_(u−v) on V obeys

    P ≽ (2α/3) J.                                    (3)

Indeed, p_(u−v) is the Gram matrix of the interval features sqrt(2α/X)·1_[u,u+X]. All such intervals lie in [−X,2X]. For any complex vector c, Cauchy–Schwarz gives

    c*Pc = (2α/X)∫|Σ_u c_u 1_[u,u+X](t)|² dt
          ≥ (2α/X) |X Σ_u c_u|²/(3X)
          = (2α/3)|Σ_u c_u|².

This bound remains true on any selected principal submatrix.

## 3. Adding the center

On the selected S, the exact adjacency is

    B_S = P_S −2α I + Z_S.

Hence B_S≽aJ−eI, where a=2α/3 and e=2α+||Z||. The W1 adjacency adds a center with all-one cross vector:

    B_W1 = [[0,1*],[1,B_S]].

For k≥max(e,1/a),

    kI+B_W1 ≽ [[k,1*],[1,aJ]],

and the right-hand block matrix is PSD because ka≥1 (it acts only on center and the constant vector; all other directions are zero). Therefore

    K_W1 ≤ max(2α+||Z||,3/(2α)).                     (4)

By Markov, ||Z||≤4E||Z|| with probability at least3/4. Standard Bernoulli variance bounds give |A|/μ→1 in probability as μ→∞. Their intersection therefore has positive probability for all sufficiently large parameters. Equations(1),(4) prove the statement.

## Audit checks / scope

- Symmetric signs share one Bernoulli variable; coloring was done on positive signclasses, not signed vertices.
- Antipodal and doubling collisions were separated rather than incorrectly decoupled.
- Lag matrices are partial degree-two incidence matrices, not assumed matchings; the variance bound accounts for their off-diagonal products.
- The positive mean uses a rank-one lower bound, not mere positive semidefiniteness, which would not control the center.
- This proves existence of weak W1 supports, while their full W2/global minima may remain of square-root size or larger. It does not approach a Chowla counterexample.
