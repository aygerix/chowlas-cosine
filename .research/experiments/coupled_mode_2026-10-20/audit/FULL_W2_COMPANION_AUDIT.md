# Independent audit addendum: full W2, multiplicity, and center localization

20 October 2026. This audits the strengthened arguments in `order/direct_union_order_audit.md`, section 5, and `exterior/exterior_counterfamily.md`, section 5 and its enhanced simultaneous selection.

## Verdict

All stronger claims pass. With the strengthened, jointly selected tapered base, the same integer supports satisfy

\[
K_{W_1}=o(\sqrt N),\qquad K_E=o(\sqrt N),\qquad
K_{W_2\setminus\{0\}}=o(\sqrt N),\qquad
K_{W_2}=(1+o(1))\sqrt N.
\]

Moreover, for every fixed \(c\in(0,1)\), exactly one eigenvalue of the full \(W_2\) matrix lies below \(-c\sqrt N\) eventually. A normalized bottom eigenvector has squared mass tending to \(1/2\) at the original center, its noncentral component aligns with the opposite constant vector on \(S\), and its exterior squared mass tends to zero.

**Selection qualification:** The full lower bound requires adding interval filling, a centered supremum bound, and the cheap positive-energy condition to the original selection. The original three-condition lexicographic family alone does not establish that lower bound. The upper bound and weak noncentral-block statement already hold under the original conditions.

## 1. Noncentral square completion

Let \(H=B_{W_2(S)\setminus\{0\}}\), with \(S=\bigcup_{i=1}^mTe_i\). Assume

\[
C_T\succeq aJ-eI,\quad D_T\ge-G,\quad a>0.
\]

Decompose noncentral coordinates into singleton vectors \(v_i\in\mathbb C^T\), same-axis exterior vectors \(w_i\in\mathbb C^{E_T}\), and pair-coordinate arrays \(z_{ij}\in\mathbb C^{T\times T}\).

The joint single-axis block \((v_i,w_i)\) is indexed by \(W_2(T)\setminus\{0\}\), hence has energy at least
\(-G(\|v_i\|^2+\|w_i\|^2)\). Each pair block contributes at least

\[
a\|r_{ij}\|^2+a\|s_{ij}\|^2-2e\|z_{ij}\|^2,
\]

where \(r_{ij}\) and \(s_{ij}\) are its row and column sums, with complex conjugation handled in the usual Hermitian inner-product convention. The only cross terms involving that pair block are

\[
2\operatorname{Re}\langle v_i,r_{ij}\rangle+
2\operatorname{Re}\langle v_j,s_{ij}\rangle.
\]

For any vectors \(v,r\),
\(a\|r\|^2+2\operatorname{Re}\langle v,r\rangle
=a\|r+v/a\|^2-\|v\|^2/a\).
Thus every pair costs at most \(\|v_i\|^2/a+\|v_j\|^2/a\). Each singleton occurs in exactly \(m-1\) pairs, and there are no pair-to-axis-exterior or distinct-pair edges. Therefore

\[
H\succeq-hI,\qquad
\boxed{h=\max\{G+(m-1)/a,2e\}.}
\]

For \(X=t^8,\alpha=t^{-2},m=t\), the sharp probabilistic bounds give \(h=O(t^3\sqrt{\log t})\), and the explicitly rationalized bounds give \(h=O(t^3\log t)\). Either is \(o(\sqrt N)\), since \(N\asymp t^7\).

Writing the full matrix as

\[
B=\begin{pmatrix}0&b^*\\b&H\end{pmatrix},\qquad
b=\mathbf1_S\text{ on noncentral vertices},\quad\|b\|=\sqrt N,
\]

the star block has minimum eigenvalue \(-\sqrt N\). Weyl's inequality, or direct quadratic forms, gives

\[
\boxed{K_{W_2}\le\sqrt N+h.}
\]

## 2. Filling all centered frequencies in W2(T)

For each \(1\le h\le X\), take representations \(h=u+v\) with \(u,v\ne0\), \(|u|,|v|\le L_0=\lfloor3X/4\rfloor\), and distinct signclasses \(|u|\ne|v|\).

The interval intersection describing possible \(u\) has at least \(2L_0-h+1\ge X/2-1\) integers. Removing zero endpoints and the diagonal loses only a fixed number. Dividing by two for unordered representations leaves at least \(X/8\) edges for \(X\ge14\).

Regard these as edges on positive signclasses. A given signclass \(b\) occurs only through \(u=b\) or \(u=-b\), so degree is at most two. A greedy matching has at least one third of the edges, hence at least \(X/24\) disjoint edges. Both endpoint selection probabilities are at least \(\alpha/2\). Independence on disjoint signclasses gives

\[
\Pr\{h\notin T+T\}\le\exp(-\alpha^2X/96).
\]

Thus

\[
\Pr\{[-X,X]\nsubseteq W_2(T)\}\le X\exp(-\alpha^2X/96).
\]

For \(X=t^8,\alpha=t^{-2}\), this is \(t^8e^{-t^4/96}<1/8\) for every integer \(t\ge8\), and tends to zero. No independence between representations sharing a signclass is assumed.

## 3. Norms, correlation, and cheap positive energy

Use normalized Haar integration and set

\[
\mu(\theta)=2\alpha(F_X(\theta)-1),\quad Z=D_T-\mu,
\quad n_0=2\alpha(X-1),\quad n=|T|.
\]

Because \(Z\) is real, even, mean zero and has frequencies in \([-X,X]\), the interval-filling event makes it an admissible \(W_2(T)\) polynomial. Put

\[
V=\|Z\|_2^2=2\sum_d(\eta_d-p_d)^2,
\qquad c_0=\langle D_T,Z\rangle=2\sum_d\eta_d(1-p_d).
\]

On the size event \(n\asymp n_0\), using \(p_d\le2\alpha\) gives

\[
V=n-4\sum_d\eta_dp_d+2\sum_dp_d^2
  =n(1+O(\alpha)),\qquad c_0=n(1+O(\alpha)).
\]

Define

\[
P=\int2\alpha F_XZ^2\ge0.
\]

For \(v_d=\operatorname{Var}(\eta_d)\), independence implies

\[
\mathbb EZ^2=\sum_dv_d(e^{2id\theta}+2+e^{-2id\theta}).
\]

The Fejér coefficient at frequency \(2d\) is \((1-2d/X)_+\), so

\[
\mathbb EP=2\alpha\sum_dv_d[2+2(1-2d/X)_+]
 \le8\alpha\sum_dv_d\le4\alpha n_0.
\]

Consequently \(P\le32\alpha n_0\) with probability at least \(7/8\). Under that condition,

\[
d:=\frac{\int D_TZ^2}{V}
 =\frac PV-2\alpha+\frac{\int Z^3}{V}
 \le O(\alpha)+\|Z\|_\infty.
\]

This requires only an upper bound for the cubic term. It neither assumes zero cubic mean nor invokes an unjustified cancellation.

## 4. Simultaneous selection, including explicit failure budgets

The enhanced family can select the lexicographically first base satisfying:

1. \(n_0/2\le n\le3n_0/2\);
2. \(C_T\succeq aJ-eI\) with the established deterministic thresholds;
3. \(\|Z\|_\infty\le H_t\), where \(H_t=1+6t^3L+6L\) and \(L=2+8\lceil\log_2t\rceil\);
4. \([-X,X]\subseteq W_2(T)\);
5. \(P\le32\alpha n_0\).

For \(t\ge8\), their failure probabilities are respectively at most \(4/\mu<1/8\), \(1/4\), \(1/8\), \(1/8\), and \(1/8\), where \(\mu=n_0/2\). Their sum is strictly less than \(3/4\), so the intersection has positive probability (indeed greater than \(1/4\)). Independence of these five events is unnecessary.

All tests are exact finite/rational or real-algebraic tests. In particular, the supremum test for the even real polynomial \(Z\) is the pair of polynomial inequalities \(H_t\pm Z\ge0\) on \([-1,1]\) after substituting \(x=\cos\theta\), and \(P\) is a finite rational Fourier coefficient sum. Hence the enhanced lexicographic definition is mathematically well-defined.

## 5. Exact two-dimensional compression and full-W2 asymptotic

On the product torus let

\[
q(\theta_1,\ldots,\theta_m)=\frac{\sum_{i=1}^m Z(\theta_i)}{\sqrt{mV}}.
\]

It is admissible on \(W_2(S)\), has norm one, and is orthogonal to the constant polynomial. For \(D_S=\sum_iD_T(\theta_i)\), the exact compression to \(\operatorname{span}\{1,q\}\) is

\[
\begin{pmatrix}0&\beta\\\beta&d\end{pmatrix},\qquad
\beta=\frac{\sqrt m\,c_0}{\sqrt V}
      =(1+O(\alpha))\sqrt{mn}.
\]

For the lower diagonal, expand \(D_S(\sum_iZ_i)^2\). The sole nonvanishing terms have all three factors on the same coordinate; every other term contains a mean-zero factor. Thus the lower diagonal is precisely the single-base \(d\), with no hidden factor of \(m\).

Since \(d_+\le O(\alpha)+H_t=O(t^3\log t)=o(\sqrt N)\), the negative eigenvalue magnitude is at least

\[
\frac{\sqrt{d^2+4\beta^2}-d}{2}\ge\beta-d_+/2
 =(1-o(1))\sqrt N.
\]

Together with section 1,

\[
\boxed{K_{W_2}/\sqrt N\longrightarrow1.}
\]

Carry-free integer encoding preserves this whole finite graph, so no product-torus approximation is needed after transfer to ordinary integer supports.

## 6. Exactly one square-root negative eigenvalue

Let the eigenvalues of \(B=B_{W_2}\) be ordered increasingly. Since deleting the center produces \(H\), Cauchy interlacing gives

\[
\lambda_2(B)\ge\lambda_1(H)\ge-h=-o(\sqrt N).
\]

The smallest eigenvalue is \(-(1+o(1))\sqrt N\). Therefore for each fixed \(c\in(0,1)\), exactly one eigenvalue is below \(-c\sqrt N\) for all sufficiently large members of this family. This disproves any universal route requiring two or more square-root negative eigenvalues in full W2 for every Boolean support. It does not disprove a claim requiring only one such eigenvalue.

## 7. Bottom eigenvector center and exterior mass

Let \((z,v)\) be a normalized eigenvector for the smallest eigenvalue \(-k\), where \(k/\sqrt N\to1\). Write \(r=|z|\), \(s=\|v\|\), so \(r^2+s^2=1\). Since \(H\succeq-hI\),

\[
-k=2\operatorname{Re}(\overline z\,b^*v)+v^*Hv
 \ge-2\sqrt N\,rs-hs^2.
\]

Dividing by \(\sqrt N\), using \(h/\sqrt N\to0\), and \(2rs\le1\), forces \(2rs\to1\). Equivalently, \((r-s)^2\to0\), so

\[
\boxed{|z|^2\to1/2,\qquad\|v\|^2\to1/2.}
\]

Set \(u=b/\sqrt N\), the unit constant vector on the original support \(S\). The center row of the eigenvector equation says exactly

\[
\langle u,v\rangle=-\frac{k}{\sqrt N}z.
\]

Hence

\[
\left\|v+\frac{k}{\sqrt N}zu\right\|^2
 =\|v\|^2-\frac{k^2}{N}|z|^2\longrightarrow0.
\]

Since \(k/\sqrt N\to1\), also \(\|v+zu\|\to0\). After multiplying by a global phase, the complete eigenvector converges in norm to

\[
\frac1{\sqrt2}\left(e_0-\frac{\mathbf1_S}{\sqrt N}\right).
\]

The exterior component of \(u\) is zero, so

\[
\boxed{\|v|_E\|_2^2\longrightarrow0.}
\]

This does **not** make the exterior removable. The operator norms need not be uniformly bounded after square-root normalization. A vanishing-norm exterior correction may still cancel a much larger positive energy. Thus closeness of eigenvectors in \(\ell^2\) does not transfer their Rayleigh values to the W1 restriction. In fact the independently established \(K_{W_1}=o(\sqrt N)\) proves that the exterior correction is essential here.

## 8. Optional exact-interior extension on this same family

The jointly selected family admits a stronger, explicit variant of its centered trial: the coefficients on the original support can be kept **exactly equal to one**, with a small exterior correction.

For the base, write

\[
W(\theta)=\sum_{s\in T}p_{|s|}e^{is\theta},\qquad Q=Z+W.
\]

Then \(Q\) has coefficient one on every selected frequency and coefficient \(-p_d\) at each unselected signed frequency \(\pm d\), with no constant coefficient. Interval filling ensures all unselected frequencies concerned belong to \(E(T)\). Thus \(Q=D_T+r\), with \(r\) supported entirely in \(E(T)\), and exactly

\[
\|Q\|_2^2=n+2\sum_{d:\eta_d=0}p_d^2=n+O(\alpha n),
\qquad \|r\|_2^2=O(\alpha n).
\]

Here \(\sum_dp_d^2\le2\alpha\sum_dp_d=\alpha n_0\) and \(n\asymp n_0\). Also \(\|W\|_2^2\le4\alpha^2 n\).

Because \(D_T+G\ge0\), the pointwise inequality \(|Z+W|^2\le2|Z|^2+2|W|^2\) gives

\[
\begin{aligned}
\int D_T|Q|^2
&\le\int(D_T+G)|Q|^2\\
&\le2\int(D_T+G)|Z|^2+2\int(D_T+G)|W|^2\\
&\le O(Gn)+2(n+G)\|W\|_2^2\\
&=O(Gn+\alpha^2n^2).
\end{aligned}
\]

The third line uses the already proved centered energy bound \(\int D_TZ^2\le O(Gn)\), \(\|Z\|_2^2\asymp n\), and \(D_T\le n\). The final line uses \(G=o(n)\) along this family. This is an upper bound; no lower bound or cancellation for the energy is assumed.

Now set \(Q_{\rm tot}=\sum_{i=1}^mQ(\theta_i)\). Its coefficients on \(S\) are exactly one, and \(Q_{\rm tot}-D_S\) is supported in the axis-exterior part of \(E(S)\). Zero means make all cross-coordinate norm and energy terms vanish, so

\[
\|Q_{\rm tot}\|_2^2=N+O(\alpha N),\qquad
\|Q_{\rm tot}-D_S\|_2^2=O(\alpha N),
\]

and

\[
\frac{\int D_S|Q_{\rm tot}|^2}{N^{3/2}}
\le O\!\left(\frac G{\sqrt{mn}}+\alpha^2\sqrt{\frac nm}\right)
=O(t^{-1/2}\log t+t^{-3/2})\longrightarrow0.
\]

The base lower bound \(D_T\ge-G\) also gives \(\int D_T|Q|^2\ge-G\|Q\|_2^2\); after multiplying by \(m\), its magnitude divided by \(N^{3/2}\) tends to zero. Hence the total normalized energy actually tends to zero, not merely its positive part.

Consequently this particular family satisfies the exact fixed-interior extension target with a vanishing relative exterior correction and even sub-square-root normalized energy. This is a family-specific result, **not** a proof of that extension target for arbitrary weak-W1 Boolean supports.
