# Independent audit: the axis-union counterfamily is valid

Date: 20 October 2026.

## Verdict and exact scope

The argument in the completed `../exterior/exterior_counterfamily.md` (the original upper-bound argument) is valid. It yields symmetric Boolean integer supports \(S_t\), with \(N_t=|S_t|\to\infty\), for which both

\[
K_{W_1}(S_t)=o(\sqrt{N_t}),\qquad K_{E}(S_t)=o(\sqrt{N_t}).
\]

Consequently a universal square-root dichotomy using only the two induced principal blocks \(W_1\) and \(E=W_2\setminus W_1\) is false. This is **not** a counterexample to a full-\(W_2\) claim. The matrix coupling \(W_1\) to \(E\) has not been controlled by this argument.

All five requested checks pass: exterior decomposition, cone estimate, scalar uniform Fourier estimate, probability intersection, and integer encoding. The base three-color noise argument was also independently checked against the stated matrix Bernstein theorem.

## 1. Definitions and the exact exterior decomposition

For a symmetric support \(S\) in an abelian group, put

\[
I(S)=\{0\}\cup S,\quad W_2(S)=I(S)+I(S),\quad E(S)=W_2(S)\setminus I(S).
\]

For a finite vertex set \(U\), its adjacency matrix is
\(B_U(u,v)=\mathbf 1_{u-v\in S}\), and \(K_U=-\lambda_{\min}(B_U)\).
Let \(T=-T\subset\mathbb Z\setminus\{0\}\) be finite and nonempty; write \(C=B_T\), \(n=|T|\), and \(E_T=E(T)\). For \(m\ge2\), set

\[
S=\bigcup_{j=1}^m T e_j\subset\mathbb Z^m.
\]

The union is disjoint and \(|S|=mn\). Every element of \(W_2(S)\) has at most two nonzero coordinates. Thus its exterior is the disjoint union

\[
E(S)=\bigsqcup_j E_Te_j\ \sqcup\ \bigsqcup_{i<j}\{ae_i+be_j:a,b\in T\}.
\]

There are no edges between distinct displayed pieces:

- Two distinct one-axis pieces differ in at least two nonzero coordinates.
- Two distinct two-axis pieces differ in at least two nonzero coordinates, even when they share one axis.
- A one-axis vertex can differ from a two-axis vertex in only one coordinate only if its sole coefficient equals the matching coefficient of that two-axis vertex. This would require an element of \(E_T\) to belong to \(T\), which is impossible.

Each one-axis piece induces \(B_{E_T}\). In a two-axis piece, an edge changes exactly one coefficient, so its matrix is
\(C\otimes I_n+I_n\otimes C\). The smallest eigenvalue of this Kronecker sum is \(2\lambda_{\min}(C)\). Hence exactly

\[
\boxed{K_E(S)=\max\{K_E(T),\,2K_C(T)\}.}
\]

## 2. The W1 cone estimate

There are no edges between distinct axis copies inside \(S\); the center is adjacent to every vertex of every copy. Assume

\[
C\succeq aJ-eI_n,\qquad a>0.
\]

For a center coordinate \(z\) and copy vectors \(v_j\), let \(h_j=\sum_xv_j(x)\). If \(k\ge e\), the quadratic form of \(B_{I(S)}+kI\) is at least

\[
k|z|^2+2\operatorname{Re}\!\left(\overline z\sum_jh_j\right)+a\sum_j|h_j|^2
 =a\sum_j|h_j+z/a|^2+(k-m/a)|z|^2.
\]

It is nonnegative for \(k\ge m/a\). Therefore

\[
\boxed{K_{W_1}(S)\le\max\{e,m/a\}.}
\]

The factor \(m\) is correct; no hidden factor of \(n\) appears.

## 3. Audit of the tapered base lower bound

Let \(X\ge2\) be an integer, \(0<\alpha\le1/2\), and let independent Bernoulli variables satisfy

\[
p_d=\mathbb E\eta_d=2\alpha(1-d/X),\quad 1\le d\le X.
\]

Write \(A=\{d:\eta_d=1\}\), \(T=A\cup(-A)\), and \(\mu=\mathbb E|A|=\alpha(X-1)\).
The restored proof establishes

\[
\mathbb E\|Z\|\le C_0\{\alpha\sqrt{X\log(4X)}+\log(4X)+1\}.
\]

The following dependence-sensitive points are correct:

1. Endpoint/difference sign-class collisions are exactly among \(v=-u,2u,u/2\). They contribute a matrix with at most three nonzero entries of magnitude at most one in any row or column, hence operator norm at most three.
2. For all remaining pairs, the three positive indices are distinct, and the probability of the ordered color pattern \((1,2,3)\) is precisely \(1/27\). Thus \(Z_{\rm good}=27\mathbb E_cZ^c\) entrywise, including the ordered rather than symmetric nature of \(Z^c\).
3. After conditioning on the coloring and color-1/color-2 endpoint variables, color-3 lag variables remain independent and centered. This is genuine conditional independence, not an independence assumption about the original graph entries.
4. Each lag matrix \(M_d\) has row and column degree at most two, so \(\|M_d\|\le2\).
5. The variance row-sum estimate includes off-diagonal products:
   \[
   \left\|\sum_d\operatorname{Var}(\xi_d)M_dM_d^*\right\|\le4\alpha n_2,
   \quad
   \left\|\sum_d\operatorname{Var}(\xi_d)M_d^*M_d\right\|\le4\alpha n_1.
   \]
   For a fixed endpoint pair its absolute lag is unique; this is what bounds the final sum by \(n_2\) or \(n_1\).
6. Rectangular Bernstein therefore gives conditional expectation
   \(O(\sqrt{\alpha(n_1+n_2)\log(4X)}+\log(4X))\). Taking expectation uses \(\mathbb E(n_1+n_2)\le2\mu\) and concavity of square root, producing the claimed scale \(\alpha\sqrt{X\log X}\).

The exact theorem invoked is Theorem 1.6 in Joel Tropp, [User-Friendly Tail Bounds for Sums of Random Matrices](https://tropp.caltech.edu/papers/Tro11-User-Friendly-preprint.pdf), page 5. Its rectangular dimension factor, variance definition and bounded-summand hypotheses match this application. Integrating its tail gives the stated expectation estimate.

For completeness, the rank-one mean lower bound also checks out. With \(p_0=2\alpha\), the kernel \(p_{u-v}\) is the Gram kernel of the length-\(X\) interval indicators, scaled by \(2\alpha/X\). The intervals for \(u\in[-X,X]\) lie in \([-X,2X]\), so Cauchy–Schwarz gives

\[
P\succeq (2\alpha/3)J.
\]

Restricting to the selected support and accounting for the diagonal yields exactly

\[
C=P_T-2\alpha I+Z_T\succeq aJ-eI,
\quad a=2\alpha/3,\quad e=2\alpha+\|Z\|.
\]

Markov supplies an event of probability at least \(3/4\) on which

\[
e\le C_1\{\alpha\sqrt{X\log(4X)}+\log(4X)+1\}.
\]

## 4. Uniform scalar Fourier estimate, with explicit constants

Define

\[
D_T(\theta)=2\sum_{d=1}^X\eta_d\cos(d\theta),\qquad
R(\theta)=2\sum_{d=1}^X(\eta_d-p_d)\cos(d\theta).
\]

Use the explicit Fejér normalization

\[
F_X(\theta)=1+2\sum_{d=1}^X(1-d/X)\cos(d\theta)
 =\frac1X\left|\sum_{r=0}^{X-1}e^{ir\theta}\right|^2\ge0.
\]

(Some conventions call this \(F_{X-1}\); the formula removes that indexing ambiguity.) Then

\[
\mathbb E D_T(\theta)=2\alpha(F_X(\theta)-1)\ge-2\alpha.
\]

For fixed \(\theta\), the independent centered summands of \(R\) have magnitude at most two and total variance at most

\[
4\sum_dp_d=4\alpha(X-1)\le4\alpha X.
\]

Let

\[
L=\lceil8\pi X^2\rceil,\quad \ell=\log(16LX),\quad
u=\sqrt{8\alpha X\ell}+\frac43\ell.
\]

Scalar Bernstein, followed by a union bound over the \(L\) equally spaced points, gives

\[
\Pr\{\max_{\rm grid}|R|>u\}\le2Le^{-\ell}=\frac1{8X}.
\]

The deterministic derivative bound is

\[
|R'(\theta)|\le2\sum_{d=1}^Xd=X(X+1).
\]

Every point of the circle lies within \(\pi/L\) of a grid point, so the interpolation error is at most

\[
\frac{\pi X(X+1)}L\le\frac{1+1/X}{8}<1.
\]

Thus with probability at least \(1-1/(8X)\), uniformly in \(\theta\),

\[
D_T(\theta)\ge-G,\qquad
G=2\alpha+u+1
 =O\big(\sqrt{\alpha X\log X}+\log X+1\big).
\]

This also verifies the stronger assertion that the Fourier event can have probability tending to one.

For any finite integer vertex set \(U\), Fourier integration gives

\[
v^*B_Uv=\frac1{2\pi}\int_0^{2\pi}D_T(\theta)
 \left|\sum_{u\in U}v_ue^{iu\theta}\right|^2d\theta
 \ge-G\|v\|^2.
\]

Therefore \(K_E(T)\le G\). Also the rank-one lower bound gives \(K_C(T)\le e\). Consequently

\[
\boxed{K_E(S)\le\max\{G,2e\}.}
\]

## 5. The events intersect without any independence assumption

Since \(\operatorname{Var}|A|\le\mu\), Chebyshev gives

\[
\Pr\{\mu/2\le|A|\le3\mu/2\}\ge1-4/\mu.
\]

Intersect this event, the noise event of probability at least \(3/4\), and the uniform Fourier event. The union bound yields probability at least

\[
\frac34-\frac4\mu-\frac1{8X},
\]

which is positive, and at least \(1/2\) whenever \(\mu\ge32\). On the intersection,
\(n=|T|=2|A|\asymp\alpha X\). These three events are dependent; the proof does not need them to be independent.

## 6. Parameter substitution

For integer \(t\to\infty\), take

\[
X=t^8,\qquad\alpha=t^{-2},\qquad m=t.
\]

The probability intersection lets us choose one deterministic realization \(T_t\) for each sufficiently large \(t\). Its parameters satisfy

\[
n\asymp t^6,\quad N=mn\asymp t^7,\quad
 e=O(t^2\sqrt{\log t}+\log t),\quad m/a=\tfrac32t^3,
\]

and

\[
G=O(t^3\sqrt{\log t}).
\]

It follows that

\[
K_{W_1}(S_t)=O(t^3),\qquad K_E(S_t)=O(t^3\sqrt{\log t}),
\qquad \sqrt{N_t}\asymp t^{7/2}.
\]

The normalized upper bounds are \(O(t^{-1/2})\) and \(O(t^{-1/2}\sqrt{\log t})\), both tending to zero.

## 7. Carry-free embedding into the integers

Set

\[
\phi(x)=\sum_{j=1}^mx_jQ^{j-1},\qquad Q>5X.
\]

Every coordinate of a \(W_2\) vertex lies in \([-2X,2X]\). Thus coordinates in a vertex difference lie in \([-4X,4X]\); after subtracting a support element they lie in \([-5X,5X]\).

If integers \(c_j\) with \(|c_j|\le5X<Q\) satisfy \(\sum_jc_jQ^{j-1}=0\), reduction modulo \(Q\) forces \(c_1=0\). Dividing by \(Q\) and repeating forces all coefficients to vanish. Therefore:

- \(\phi\) is injective on \(W_2(S)\);
- \(\phi(W_2(S))=W_2(\phi(S))\), because \(\phi\) is a homomorphism;
- no distinct \(W_2\) vertex is identified with an interior vertex;
- \(\phi(u)-\phi(v)\in\phi(S)\) holds exactly when \(u-v\in S\).

So the entire full-\(W_2\) graph, not only its two principal blocks, is faithfully represented in the integers. The proposed \(Q=10X+1\) is safe, and even \(Q=5X+1\) suffices. The resulting support is a genuine symmetric set, with no zero and no multiplicities. Its adjacency remains Boolean.

## 8. Finite checks and reproducibility

The script `check_axis_union.py` and output `check_results.json` are in this audit directory. They verify:

- Exact exterior vertex and adjacency decomposition for every nonempty \(A\subseteq\{1,2,3,4\}\), with \(T=\pm A\), and \(m=2,3\): 30 cases.
- Full-\(W_2\) vertex injectivity and every full-\(W_2\) adjacency relation under \(Q=5\max(A)+1\), in all 30 cases.
- Exact three-color decoupling, by integer arithmetic, for all 16 endpoint patterns and all 81 colorings at \(X=4\).
- Floating-point spectral checks of the exact exterior eigenvalue formula, with maximum discrepancy \(6.22\times10^{-15}\).

These finite checks are corroborative only; the proofs above establish the infinite family.

## Final scope warning

An upper bound on the negative spectrum of each diagonal principal block is not an upper bound for the full block matrix. In particular,

\[
B_{W_2}=\begin{pmatrix}B_{W_1}&M^*\\M&B_E\end{pmatrix}
\]

can acquire additional negative spectrum through \(M\). The present audit neither estimates nor removes that possibility. The correct research conclusion is specifically that the **exterior-only square-root dichotomy fails**, even along a family with genuinely weak \(W_1\).
