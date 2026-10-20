# Explicit Jedwab–Li and Polhill positive Latin-square-type PDS

Checked 2026-10-19. Only this report is a deliverable; no commit was made.

**Answer:** the explicit examples below are not unions of subgroups, even allowing arbitrary subgroup orders and intersections. They are unions of subgroup differences. Their nonprincipal character sums have exactly the two positive-LS values, and their large-value sets, with the principal character adjoined, also fail to be subgroup unions.

## Sources, conventions, and scope

- **[JL]** J. Jedwab and S. Li, *Packings of partial difference sets*, Combinatorial Theory **1** (2021), #18, [DOI](https://doi.org/10.5070/C61055384), [arXiv:2012.00979v2](https://arxiv.org/abs/2012.00979v2), revised 21 September 2021, [PDF](https://arxiv.org/pdf/2012.00979v2). Locations below use the 41-page arXiv PDF's printed page numbers. Its placeholder running header is not the final journal citation.
- **[P]** J. Polhill, *Generalizations of partial difference sets from cyclotomy to nonelementary abelian p-groups*, Electron. J. Combin. **15** (2008), #R125, [journal record and DOI](https://doi.org/10.37236/849), [full paper](https://www.emis.de/ft/6964). Relevant pages: 3–5. Theorems 2.3–2.5 are restated there from reference [13], Polhill's 2002 paper; that earlier paper was not independently checked.

Use additive notation. A regular PDS satisfies \(0\notin D=-D\). Write \(\mathrm{LS}_r(n)\) for parameters

\[
(v,k,\lambda,\mu)=(n^2,r(n-1),n+r^2-3r,r^2-r).
\]

For \(H\le G\), \(H^\perp\) is the subgroup of characters trivial on \(H\), and \(\chi(D)=\sum_{d\in D}\chi(d)\), without normalization. A PCP of degree \(r\) uses \(r\) order-\(n\) subgroups intersecting pairwise in \(\{0\}\); being non-PCP does **not** itself rule out a union of overlapping subgroups of other orders.

Confidence labels distinguish **read in source**, **checked by computation**, and **derived here**. No substantive claim below relies only on recollection. PDF formulas in [JL, p. 23] and [P, pp. 4–5] were also inspected visually.

## 1. Jedwab–Li: the construction in coordinates

### What Theorem 5.3 actually specifies

**Read in source:** [JL, Theorem 5.3, p. 23](https://arxiv.org/pdf/2012.00979v2#page=23) gives, for every prime \(p\), positive \(a,s\), and subgroup \(U\le\mathbb Z_{p^a}^{2s}\) of order \(p^{as}\), a \((p^{(a-1)s},p^s)\) LP-packing relative to \(U\). Definition 3.1 means that its \(p^s\) blocks are disjoint regular \(\mathrm{LS}_{p^{(a-1)s}}(p^{as})\) PDS and partition \(G\setminus U\).

There is no uniquely specified “the set \(D\)” in this theorem. Subgroups, quotient identifications, and block labels are choices. Here is a fully specified realization for \(s=1\), choosing

\[
G_a=(\mathbb Z/p^a\mathbb Z)^2,\qquad U_a=\{(x,0):x\in\mathbb Z/p^a\mathbb Z\}.
\]

### The paper's two lifting operations

For precision, a \((c,p)\) LP-partition in \(G\setminus V\) relative to \(H\le V\) has \(|G|=p^2c^2\), \(|V|=pc^2\), and \(p\) disjoint blocks \(R_j\) of size \((p-1)c^2\) partitioning \(G\setminus V\). For nonprincipal \(\chi\), the multiset \(\{\chi(R_j):0\le j<p\}\) is

\[
\begin{cases}
\{-c^2,\ldots,-c^2\},&\chi\in V^\perp,\\
\{0,\ldots,0\},&\chi\in H^\perp\setminus V^\perp,\\
\{(p-1)c,-c,\ldots,-c\},&\chi\notin H^\perp.
\end{cases}
\]

This is [JL, Definition 4.1, p. 16](https://arxiv.org/pdf/2012.00979v2#page=16), **read in source**, specialized to \(t=p\).

**Read in source:** [JL, Theorems 4.4 and 4.6, pp. 16–18; Theorems 5.2–5.3, pp. 22–23](https://arxiv.org/pdf/2012.00979v2#page=16) use these set operations:

\[
R_j=\bigsqcup_{i=1}^{p}\{g\in V_i:g+H_i\in S_{ij}\},
\qquad
D_j=R_j\sqcup\{g\in V_0:g+H_0\in P_j\}.
\tag{1}
\]

Here \(S_{ij}\) are blocks of LP-partitions in \(V_i/H_i\setminus G'/H_i\); \(P_j\) are blocks of an LP-packing in \(V_0/H_0\) relative to \(U/H_0\). These are inverse images under quotient maps, followed by ordinary disjoint union. The group-ring plus signs in the proofs do not mean Minkowski sum of sets. The base case is the punctured spread in Examples 3.7 and 4.3.

### Explicit quotient maps and recursion

**Derived here by choosing coordinates in (1).** Let labels \(j,t\) range over the integer representatives \(0,\ldots,p-1\). For \(a\ge2\), take

\[
\begin{aligned}
G'&=pG_a,& Q&=p^{a-1}G_a,\\
H_0&=\langle(p^{a-1},0)\rangle,&V_0&=\{(x,y):p\mid y\},\\
H_t^{\rm fin}&=\langle(p^{a-1}t,p^{a-1})\rangle,
&V_t^{\rm fin}&=\{(x,y):x\equiv ty\pmod p\}.
\end{aligned}
\]

The horizontal index \(0\) on \(H_0,V_0\) is the paper's distinguished index; the superscript “fin” avoids confusing it with finite slope \(t=0\). The corresponding quotient maps to \(G_{a-1}\) are

\[
q_{\rm hor}(x,y)=(x\bmod p^{a-1},\ y/p),\qquad
q_t^{\rm fin}(x,y)=((x-ty)/p,\ y\bmod p^{a-1}).
\tag{2}
\]

In \(q_t^{\rm fin}\), first form \(x-ty\) modulo \(p^a\), then divide by \(p\), giving a well-defined residue modulo \(p^{a-1}\). The kernels are \(H_0,H_t^{\rm fin}\), respectively. Also \(q_t^{\rm fin}(G')=\{(u,v):p\mid v\}\), and \(q_t^{\rm fin}(Q)\) is the horizontal order-\(p\) subgroup. Thus these are exactly the quotient configurations needed in Theorem 5.2.

Define the auxiliary shell blocks \(R_{a,j}\) and packing blocks \(D_{a,j}\) by

\[
R_{1,j}=D_{1,j}=\{(jz,z):z\in\mathbb F_p^\times\},
\tag{3}
\]

\[
R_{a,j}=\bigsqcup_{t=0}^{p-1}(q_t^{\rm fin})^{-1}(R_{a-1,j}),
\qquad
D_{a,j}=R_{a,j}\sqcup q_{\rm hor}^{-1}(D_{a-1,j}).
\tag{4}
\]

Each inverse image is restricted to the map's domain in (2). Equations (3)–(4) implement Theorems 4.6/5.2 and 4.4/5.3, respectively, with \(U=U_a\). They give \(p\) disjoint sets partitioning \(G_a\setminus U_a\).

For another subgroup \(U\) permitted by Theorem 5.3, the paper chooses \(H_0\le U\le V_0\), recursively constructs a packing relative to \(U/H_0\), and uses the second operation in (1). One must retain those choices; (3)–(4) fix the horizontal-\(U\) realization rather than claiming all permitted choices give the same set.

### Closed membership formula

**Derived here.** Write \([w]_M\) for the representative in \(\{0,\ldots,M-1\}\). The first recursion gives

\[
R_{a,j}=\{(x,y):p\nmid y,\quad
[xy^{-1}]_{p^a}\in[jp^{a-1},(j+1)p^{a-1})\}.
\tag{5}
\]

For the whole block, exclude \(y=0\). If \(k=v_p(y)<a\), put \(b=a-k\), \(z=y/p^k\in(\mathbb Z/p^b\mathbb Z)^\times\). Then

\[
\boxed{(x,y)\in D_{a,j}\iff y\ne0\ \text{and}\quad
[(x\bmod p^b)z^{-1}]_{p^b}\in[jp^{b-1},(j+1)p^{b-1}).}
\tag{6}
\]

To verify (5), a lift replaces a lower slope \(\ell\) by \(t+p\ell\); iterating enumerates precisely the slopes with highest base-\(p\) digit \(j\). Iterating \(q_{\rm hor}\) until \(y\) becomes a unit gives (6).

## 2. Subgroup differences and the exact \(\mathbb Z_{27}^2\) test

### A uniform description by \(H\setminus K\)

For \(0\le k<a\), set \(b=a-k\), and, for \(0\le t<p^{b-1}\), put \(\ell=t+jp^{b-1}\). Define

\[
\begin{aligned}
H_{k,\ell}&=\{(x,y):p^k\mid y,\quad x\equiv\ell(y/p^k)\pmod {p^b}\}\\
&=\langle(\ell,p^k),(p^b,0)\rangle,\\
K_{k,\ell}&=H_{k,\ell}\cap\{(x,y):p^{k+1}\mid y\}.
\end{aligned}
\tag{7}
\]

These are subgroups, with \(|H_{k,\ell}|=p^a\), \(|K_{k,\ell}|=p^{a-1}\). Formula (6) becomes the disjoint union

\[
\boxed{D_{a,j}=\bigsqcup_{k=0}^{a-1}\quad
\bigsqcup_{t=0}^{p^{a-k-1}-1}
\bigl(H_{k,t+jp^{a-k-1}}\setminus K_{k,t+jp^{a-k-1}}\bigr).}
\tag{8}
\]

There are \((p^a-1)/(p-1)\) differences, each of size \((p-1)p^{a-1}\), yielding \(|D_{a,j}|=p^{a-1}(p^a-1)\). Each difference is also a union of \(p-1\) nonzero cosets of its \(K\), so (8) gives \(p^a-1\) disjoint cosets, all of order \(p^{a-1}\), with different underlying subgroups allowed.

This answers “smallest description” in terms of operations: **one subgroup subtraction per piece suffices; zero subtractions, i.e. positive unions of subgroups, do not suffice for the examples below.** No minimum number of pieces over all possible \(H,K\) or coset orders is asserted.

### Explicit example requested in the brief

Take \(p=3,a=3,j=0\), and write \(D=D_{3,0}\subset\mathbb Z_{27}^2\). Formula (6) says:

| Condition on \(y\) | Membership condition on \(x\) |
|---|---|
| \(3\nmid y\) | \([xy^{-1}]_{27}\in\{0,1,\ldots,8\}\) |
| \(y=3z,\ 3\nmid z\) | \([(x\bmod9)z^{-1}]_9\in\{0,1,2\}\) |
| \(y=9z,\ z=1,2\) | \(x\equiv0\pmod3\) |
| \(y=0\) | never in \(D\) |

Already \((1,1)\in D\) but \(3(1,1)=(3,3)\notin D\cup\{0\}\). Every union of subgroups is closed under multiplying any of its elements by 3. Therefore **\(D\cup\{0\}\) is not a union of subgroups of any orders**, regardless of overlaps.

**Checked by computation, exhaustively on the specified VM:** there are exactly **76** subgroups of \(\mathbb Z_{27}^2\); exactly 10 lie in \(D\cup\{0\}\). The complete list of maximal contained subgroups is

\[
\boxed{\langle(0,1)\rangle,\quad\langle(3,1)\rangle,\quad
\langle(6,1)\rangle,\quad\langle(9,9)\rangle,\quad\langle(18,9)\rangle.}
\tag{9}
\]

Their orders are \(27,27,27,3,3\). Their union has **79** elements including 0, so it covers **78 of the 234** elements of \(D\), leaving **156 uncovered**. Equation (8) has 13 subgroup differences here, equivalently 26 disjoint order-9 cosets.

For completeness, the same checked realization with \(j=1\) or \(j=2\) contains **no nontrivial subgroup at all** after adjoining 0. Indeed it contains no order-3 element: an order-3 element has both coordinates divisible by 9, whereas (6) in its last nonempty layer requires \(x\equiv jz\not\equiv0\pmod3\). Every nontrivial subgroup of this 3-group contains an order-3 element.

**Derived here, beyond the checked case:** all the blocks in this fixed realization fail to be subgroup unions when \(a\ge3\). For \(j=0\), use
\((p^{a-3},1)\in D_{a,0}\) but \((p^{a-2},p)\notin D_{a,0}\). For \(j\ne0\) and \(a\ge2\), the same absence of order-\(p\) elements proves the claim. This is not a classification of every choice in Theorem 5.3. For example, at \(a=1\) the blocks are punctured lines; the present \(D_{2,0}\) is also a union of \(p\) punctured order-\(p^2\) cyclic subgroups.

## 3. Character values and the dual large-value set

**Read in source:** [JL, Lemmas 2.5 and 3.3, equation (3.1)](https://arxiv.org/pdf/2012.00979v2#page=6) give, with \(n=p^a,r=p^{a-1}\),

\[
\chi(D_{a,j})\in\{n-r,-r\}\quad(\chi\ne1).
\]

Every nonprincipal \(\chi\in U_a^\perp\) sees \(-r\) on every block; every \(\chi\notin U_a^\perp\) sees \(n-r\) on exactly one block. The dual blocks themselves form an LP-packing relative to \(U_a^\perp\) [JL, Remark 3.10(ii), p. 11]. That fact alone does not imply subgroup unions.

Here are the exact characters selecting a given block. Identify the dual with \(G_a\) by

\[
\chi_{u,v}(x,y)=\exp(2\pi i(ux+vy)/p^a).
\]

**Derived here:** if \(u=0\) and \(v\ne0\), the value is \(-r\). Otherwise write \(u=p^hU\), where \(h=v_p(u)<a\) and \(U\) is a unit modulo \(p^{a-h}\), and put \(b=a-h\). Then

\[
\boxed{\chi_{u,v}(D_{a,j})=n-r\iff
[-vU^{-1}]_{p^b}\in[jp^{b-1},(j+1)p^{b-1}).}
\tag{10}
\]

All other nonprincipal characters have value \(-r\). Equivalently, with \(J(x,y)=(-y,x)\),

\[
\boxed{E_{a,j}:=\{(u,v)\ne(0,0):\chi_{u,v}(D_{a,j})=n-r\}=J(D_{a,j}).}
\tag{11}
\]

**Proof of the character rule.** Orthogonality applied to (8) gives the exact integer formula

\[
\chi_{u,v}(D_{a,j})=
\sum_{k,\ell}\left[p^a\mathbf1_{H_{k,\ell}^\perp}(u,v)
-p^{a-1}\mathbf1_{K_{k,\ell}^\perp}(u,v)\right],
\tag{12}
\]

where, with \(b=a-k\),

\[
\begin{aligned}
(u,v)\in H_{k,\ell}^\perp&\iff p^k\mid u\ \text{and}\ u\ell+vp^k\equiv0\pmod{p^a},\\
(u,v)\in K_{k,\ell}^\perp&\iff p^k\mid u\ \text{and}\ u\ell+vp^k\equiv0\pmod{p^{a-1}}.
\end{aligned}
\]

For \(u\ne0\), levels \(k>h\) contribute zero. At each \(k<h\), the number of solutions to the second congruence is \(p\) times the number for the first, so those levels cancel. At \(k=h\), the second congruence has exactly one \(\ell\) in the prescribed block of \(p^{b-1}\) slopes; the first has one exactly in case (10). This gives \(p^{a-1}(p\mathbf1-1)\). For \(u=0,v\ne0\), if \(l=v_p(v)\), the nonzero contributions telescope to \(p^{a-1}[-p^l+(p^l-1)]=-r\). Finally, applying (6) to \((v,-u)\) proves (11).

Thus **\(E_{a,j}\cup\{(0,0)\}\) has exactly the same subgroup-union status as \(D_{a,j}\cup\{0\}\)**. The literal set \(E_{a,j}\) excludes the identity character, so the substantive question is the version with that character adjoined.

For \(p=3,a=3,j=0\), an explicit dual witness is

\[
(1,19)\in E_{3,0},\qquad3(1,19)=(3,3)\notin E_{3,0}\cup\{0\}.
\]

The maximal contained dual subgroups are exactly the \(J\)-images of (9), again covering 79 elements including 0. **Checked by computation:** all 729 character sums, by two independent exact methods, have multiplicities

| Character value | Number of characters |
|---|---:|
| \(234\) (principal) | 1 |
| \(18=n-r\) | 234 |
| \(-9=-r\) | 494 |

The direct difference counts also give \((v,k,\lambda,\mu)=(729,234,81,72)\). The character methods were subgroup orthogonality in (12), and direct exponent counting reduced modulo \(\Phi_{27}(z)=1+z^9+z^{18}\); no floating-point Fourier calculation was used.

## 4. Polhill's positive \(\mathrm{LS}_{(p-1)(p^2+1)}(p^4)\) ingredients

### Explicit set and subgroup-union obstruction

**Read in source:** [P, Theorems 2.3–2.5, p. 4, and the opening construction of §3, p. 5](https://www.emis.de/ft/6964) use \(R=\operatorname{GR}(p^2,2)\), its Teichmüller set \(T\), and \(G=R^2\cong\mathbb Z_{p^2}^4\). Put \(q=p^2\). For a row \(b\in T\) and a column \(t\in T\cup\{\infty\}\), their 2-array consists of

\[
S_{b,t}=\{(z,(t+pb)z):z\in R\},\quad
S_{b,\infty}=\{(pbz,z):z\in R\}.
\tag{13}
\]

Choose \(B\subset T\setminus\{0\}\), \(|B|=p-1\), and \(A\subset T\cup\{\infty\}\), \(|A|=p-1\). A regular positive ingredient is

\[
\boxed{D=\left(\bigsqcup_{b\in B}\bigsqcup_{t\in T\cup\{\infty\}}
(S_{b,t}\setminus pS_{b,t})\right)
\sqcup\left(\bigsqcup_{t\in A}(S_{0,t}\setminus\{0\})\right).}
\tag{14}
\]

Indeed, \(S_{b,t}\cap pG=pS_{b,t}=pS_{0,t}\). Thus (14) is precisely the order-\(p^2\) part of \(p-1\) selected nonzero rows, plus \(p-1\) punctured subgroups of the first row. Theorem 2.5 specializes to \(e=f=p-1\), its ring exponent 2 and extension degree 2; hence

\[
n=p^4=q^2,\qquad r=eq+f=(p-1)(p^2+1),\qquad |D|=r(p^4-1).
\]

In §3, the regular ingredients are \(D_i\) for \(1\le i\le p-1\). The exceptional \(D_0,D_p\) there have an extra entire subgroup, include 0, and should not be identified with the regular set (14). The final product sets in Theorems 3.1–3.2 are negative LS; (14) is their positive ingredient.

**Derived here:** choose a column \(t\notin A\) and a row \(b\in B\). There is a primitive \(g\in S_{b,t}\), and \(g\in D\). But \(pg\in pS_{0,t}\setminus\{0\}\) is absent from \(D\), since the only order-\(p\) elements in (14) have directions in \(A\). The subgroups \(pS_{0,t}\), indexed by distinct columns, are one-dimensional \(\mathbb F_q\)-subspaces of \(pG\) intersecting only at 0; each has order \(p^2\). Hence **\(D\cup\{0\}\) is not a union of subgroups**, with arbitrary orders and overlaps allowed. This proof works for every selection \(A,B\) above and every prime \(p\).

The natural pieces are exactly subgroup differences in (14): the shells have subgroup orders \(p^4\) and \(p^2\), and the first-row pieces have the form \(S\setminus\{0\}\). Each shell is also a disjoint union of \(q-1\) nonzero cosets of \(pS_{b,t}\). For \(p\ge3\), non-PCP status additionally follows from \(r>p^2+1\), the maximum PCP degree from [JL, Result 2.7, p. 7](https://arxiv.org/pdf/2012.00979v2#page=7); the multiplication argument establishes the stronger conclusion.

### Which characters take the large value?

Use the perfect trace pairing

\[
\chi_{u,v}(x,y)=\exp\left(\frac{2\pi i}{p^2}\operatorname{Tr}_{R/\mathbb Z_{p^2}}(ux+vy)\right).
\]

For finite \(t\), let \(L_{b,t}(u,v)=u+(t+pb)v\); for \(t=\infty\), let \(L_{b,\infty}(u,v)=pbu+v\). Orthogonality applied to (14) gives

\[
\chi_{u,v}(D)=
\sum_{b\in B,t}\left(q^2\mathbf1_{L_{b,t}=0}-q\mathbf1_{pL_{b,t}=0}\right)
+\sum_{t\in A}\left(q^2\mathbf1_{L_{0,t}=0}-1\right).
\tag{15}
\]

**Derived here:** if \((u,v)\notin pG\), its reduction determines a unique column \(t_0\) for which \(pL_{b,t_0}=0\). It is independent of \(b\). At most one of the selected full annihilators \(L_{b,t}=0\), \(b\in B\), or \(L_{0,t}=0\), \(t\in A\), contains this primitive character. If \(N\in\{0,1\}\) records that event, (15) is

\[
q^2N-|B|q-|A|=nN-r.
\]

If \((u,v)=p(u_1,v_1)\ne0\), there is again a unique annihilated column \(t_0\), now determined by \((\bar u_1,\bar v_1)\). Every selected row contributes \(-q\), and the first row contributes \(q^2\mathbf1_{t_0\in A}-|A|\). Thus the value is \(n-r\) exactly if \(t_0\in A\), and otherwise \(-r\). This confirms the values supplied by [P, Theorem 1.1, p. 3 and §3, p. 5](https://www.emis.de/ft/6964) while explicitly identifying their characters.

Since \(S_{b,t}^\perp=J(S_{b,t})\) for \(J(x,y)=(-y,x)\), these two cases prove

\[
\boxed{\{(u,v)\ne0:\chi_{u,v}(D)=n-r\}=J(D).}
\tag{16}
\]

Consequently the large-value set with 0 adjoined is not a union of subgroups either.

**Checked by computation:** for \(p=3\), take \(R=\mathbb Z_9[w]/(w^2+1)\), \(B=\{1,-1\}\), \(A=\{0,\infty\}\). All 6561 characters evaluated by (15) give

\[
|D|=1600,\qquad \chi(D):\quad1600\ (1\text{ time}),\quad61\ (1600),\quad-20\ (4960).
\]

The computed high-value support equals \(J(D)\) exactly. The explicit subgroup obstruction is \(g=(1,4)\in D\), \(3g=(3,3)\notin D\cup\{0\}\), where these coordinates are scalar elements of \(R\). The general assertions (14)–(16) rest on the argument above; this finite check is supporting verification.

## 5. Reproducibility and computational scope

Both small checks ran from the repository root through

```text
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 1 -t 600 python -c '<Python source below>'
```

The inline source avoids creating another repository file. Both jobs exited 0 on the designated Dirichlet VM; the first recorded Python 3.12.3, Linux x86_64. Only the standard library was used. No heavy computation or floating-point calculation was performed. The scripts are preserved below so that the group constructions, scope of enumeration, and assertions can be reproduced without an additional artifact.

For the subgroup enumeration, every subgroup has unique triangular generators \((d,0),(t,e)\), where \(d,e\mid27\), \(0\le t<d\), and \(d\mid(27/e)t\). Intersecting with the horizontal axis determines \(d\), projecting on the second coordinate determines \(e\), and reducing a lift of \(e\) modulo \(d\) determines \(t\). Thus the enumeration is complete, including subgroups of all orders, not just cyclic subgroups or PCP candidates.

### Exact Jedwab–Li check

```python
import itertools,json,sys,platform
from collections import Counter
from functools import lru_cache
p,a=3,3
m=p**a
Z=(0,0)
G=list(itertools.product(range(m),repeat=2))
@lru_cache(None)
def R(b,j):
    n=p**b
    if b==1:
        return frozenset(((j*y)%p,y) for y in range(1,p))
    n0=n//p
    lower=R(b-1,j)
    return frozenset((x,y) for x in range(n) for y in range(n) if y%p and (((x-(x*pow(y,-1,p)%p)*y)%n)//p,y%n0) in lower)
@lru_cache(None)
def P(b,j):
    if b==1:return R(b,j)
    n=p**b;n0=n//p
    return R(b,j)|frozenset((x,y) for x in range(n) for y in range(0,n,p) if (x%n0,y//p) in P(b-1,j))
def shells(j):
    out=[]
    for k in range(a):
        b=a-k;n=p**b
        for t in range(p**(b-1)):
            lam=t+p**(b-1)*j
            H=frozenset((x,y) for x,y in G if y%p**k==0 and (x-lam*(y//p**k))%n==0)
            K=frozenset((x,y) for x,y in H if y%p**(k+1)==0)
            assert len(H)==m and len(K)==m//p
            out.append((k,lam,H,K))
    return out
subs={}
divs=[p**i for i in range(a+1)]
for d in divs:
 for e in divs:
  for t in range(d):
   if ((m//e)*t)%d:continue
   H=frozenset(((i*d+j*t)%m,j*e) for i in range(m//d) for j in range(m//e))
   subs[H]=[(d,0),(t,e)]
def subgroup_report(A):
    eligible=[H for H in subs if H<=A]
    maximal=[H for H in eligible if not any(H<K for K in eligible)]
    cover=frozenset().union(*maximal)
    return {"contained_subgroups":len(eligible),"maximal":[{"generators":subs[H],"order":len(H)} for H in sorted(maximal,key=lambda H:(-len(H),subs[H]))],"covered_with_zero":len(cover),"uncovered_nonzero":len(A-cover),"uncovered_sample":sorted(A-cover)[:8]}
results={"python":sys.version.split()[0],"platform":platform.platform(),"group_order":len(G),"total_subgroups_enumerated":len(subs),"sets":{}}
for j in range(p):
 D=P(a,j);S=shells(j)
 assert D==frozenset().union(*(H-K for k,l,H,K in S))
 assert len(D)==p**(a-1)*(m-1)
 assert Z not in D and all(((-x)%m,(-y)%m) in D for x,y in D)
 assert not any(P(a,j)&P(a,k) for k in range(p) if k!=j)
 def annih(w,A):return all((w[0]*x+w[1]*y)%m==0 for x,y in A)
 vals={w:sum(len(H)*annih(w,H)-len(K)*annih(w,K) for k,l,H,K in S) for w in G}
 # Independent exact cyclotomic reduction: Phi_27(z)=1+z^9+z^18.
 for (u,v),value in vals.items():
  c=Counter((u*x+v*y)%m for x,y in D)
  reduced=[c[t]-c[t+18] for t in range(9)]+[c[t+9]-c[t+18] for t in range(9)]
  assert reduced==[value]+[0]*17
 large=frozenset(w for w in G if w!=Z and vals[w]==m-p**(a-1))
 assert set(vals[w] for w in G if w!=Z)=={-9,18}
 difference=Counter(((x-u)%m,(y-v)%m) for x,y in D for u,v in D if (x,y)!=(u,v))
 assert set(difference[g] for g in D)=={81}
 assert set(difference[g] for g in G if g!=Z and g not in D)=={72}
 multbad=next(((x,y),((p*x)%m,(p*y)%m)) for x,y in sorted(D) if ((p*x)%m,(p*y)%m) not in D|{Z})
 dualbad=next(((x,y),((p*x)%m,(p*y)%m)) for x,y in sorted(large) if ((p*x)%m,(p*y)%m) not in large|{Z})
 results["sets"][j]={"D_size":len(D),"shell_count":len(S),"subgroup_report":subgroup_report(D|{Z}),"p_closure_witness":multbad,"character_counts":dict(Counter(vals.values())),"dual_subgroup_report":subgroup_report(large|{Z}),"dual_p_closure_witness":dualbad,"PDS_lambda_mu":[81,72],"dual_equals_rotation_D":large==frozenset(((-y)%m,x) for x,y in D)}
print(json.dumps(results,indent=2))
```

### Exact Polhill check

```python
import itertools,json,sys
from collections import Counter
p=3;m=9
R=list(itertools.product(range(m),repeat=2));zero=(0,0)
def add(x,y):return ((x[0]+y[0])%m,(x[1]+y[1])%m)
def neg(x):return ((-x[0])%m,(-x[1])%m)
def mul(x,y):return ((x[0]*y[0]-x[1]*y[1])%m,(x[0]*y[1]+x[1]*y[0])%m)
def scale(c,x):return ((c*x[0])%m,(c*x[1])%m)
def power(x,k):
 y=(1,0)
 for _ in range(k):y=mul(y,x)
 return y
T=[x for x in R if power(x,9)==x]
assert len(T)==9
cols=T+[None];B=[(1,0),(8,0)];A=[zero,None]
def C(b,t):return scale(p,b) if t is None else add(t,scale(p,b))
def line(b,t):
 c=C(b,t)
 return frozenset((mul(c,z),z) if t is None else (z,mul(c,z)) for z in R)
def inpG(g):return all(v%p==0 for x in g for v in x)
D=frozenset().union(*(line(b,t)-frozenset(g for g in line(b,t) if inpG(g)) for b in B for t in cols),*(line(zero,t)-{(zero,zero)} for t in A))
def expr(u,v,b,t):
 c=C(b,t)
 return add(mul(c,u),v) if t is None else add(u,mul(c,v))
vals={}
for u in R:
 for v in R:
  val=sum(81*(expr(u,v,b,t)==zero)-9*(scale(p,expr(u,v,b,t))==zero) for b in B for t in cols)
  val+=sum(81*(expr(u,v,zero,t)==zero)-1 for t in A)
  vals[u,v]=val
large=frozenset(w for w,val in vals.items() if w!=(zero,zero) and val==61)
assert len(D)==1600 and Counter(vals.values())==Counter({1600:1,61:1600,-20:4960})
assert large==frozenset((neg(y),x) for x,y in D)
# Omitted finite column t=1 and selected nonzero row b=1.
g=((1,0),(4,0));pg=tuple(scale(p,x) for x in g)
assert g in D and pg not in D|{(zero,zero)}
print(json.dumps({"ring":"Z_9[w]/(w^2+1)","Teichmuller_set":T,"B":B,"A":["0","infinity"],"D_size":len(D),"character_counts":dict(Counter(vals.values())),"large_equals_J_D":True,"p_closure_witness":[g,pg]},indent=2))
```

## Three-line summary

Jedwab–Li: the specified \(\mathbb Z_{27}^2\) block and, more generally, the fixed realization above for \(a\ge3\), are not subgroup unions even after adjoining 0; 13 subgroup differences suffice in the checked case.<br>
Polhill: the regular positive ingredients are unions of full punctured subgroups and subgroup shells, and fail subgroup-union closure under multiplication by \(p\).<br>
Dual: both explicit constructions have exactly \(n-r,-r\) off the principal character, with high-value support \(J(D)\); adjoining the principal character does not make that support a subgroup union.
