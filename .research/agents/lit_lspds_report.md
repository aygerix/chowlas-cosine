# Literature check: small negative eigenvalues and Latin-square-type PDS

Web search and browsing were available and used; checked 2026-10-19. This is a statement check; no experiment or heavy computation was run. Parameter specializations and comparisons of published bounds are identified explicitly.

Conventions are those of the brief: all PDS below are regular, so \(0\notin D=-D\), and \(\mathrm{LS}_r(n)\) has character values \(n-r,-r\). “Nontrivial” excludes \(H\setminus\{0\}\) and \(G\setminus H\) for subgroups \(H\), including the empty/complete degeneracies. A PCP means subgroups of the **given group**, not merely a graph isomorphism to a net graph. For negative Latin square type the character values are \(r,r-n\); its parameter \(r\) is therefore not the magnitude of its negative eigenvalue. In the approximation results, write \(N=|G|\), to distinguish group order from the LS parameter \(n=\sqrt N\).

## 1. Exact results forcing a PCP

**A verified sufficient range for every finite abelian group is**

\[
2\le r<n,\qquad
n>\frac12(r-1)\(r^3-r^2+r+2\).
\tag{1}
\]

Every regular \(\mathrm{LS}_r(n)\) PDS in this range is a union of a degree-\(r\) PCP. No elementary abelian or prime-power assumption is required. This is a **specialization of the following two published results**, rather than a separately located theorem stated verbatim in PDS terminology.

**Graph recognition.** Bruck, Theorem 4.3 and equation (4.17), proves that a pseudo net-graph of order \(n\), degree \(r\), is the graph of a unique net when \(n>P(r-1)\), where

\[
P\(x\)=\tfrac12x^4+x^3+x^2+\tfrac32x.
\]

These are exactly the LS parameters. The uniqueness makes the net invariant under graph automorphisms, including the given Cayley translations. Bruck also gives the conditional improvement \(n>2(r-1)^3\) when the graph has no induced \((r+1)\)-claw (Theorem 4.2).

Source: R. H. Bruck, *Finite nets. II. Uniqueness and imbedding*, Pacific J. Math. **13** (1963), 421–457, [DOI 10.2140/pjm.1963.13.421](https://doi.org/10.2140/pjm.1963.13.421), [original PDF](https://msp.org/pjm/1963/13-2/pjm-v13-n2-p05-s.pdf). **Confidence: read in source**, including visual inspection of the polynomial, whose fractions are garbled in extracted text.

**Passage from an abelian regular action to subgroup lines.** Leung–Ma–Schmidt, Corollaries 7–8 and Notation 9, apply to a partial geometry \(\operatorname{pg}(s+1,t+1,\alpha)\) with an abelian Singer group. Their notation counts \(s+1\) points per line and \(t+1\) lines per point. A line stabilizer has order either (1) or \(s+1\). Their group-ring decomposition is

\[
D=-\(t+1\)\{0\}+\sum_{U\in\mathcal U}U+
\sum_{L\in\mathcal L}LL^{(-1)},
\]

where \(|U|=|L|=s+1\), and an orbit-line term supplies \(s+1\) distinct lines through (0). Specializing to a degree-\(r\) net gives \(s+1=n,t+1=r,\alpha=r-1\). Since \(r<n\), there are no orbit-line terms; the \(r\) lines through (0) are subgroups meeting pairwise only at (0). This checks the subgroup conclusion in (1), not just the graph conclusion.

Source: K. H. Leung, S. L. Ma, B. Schmidt, *Proper partial geometries with Singer groups and pseudogeometric partial difference sets*, J. Combin. Theory Ser. A **115** (2008), 147–177, [DOI 10.1016/j.jcta.2007.05.001](https://doi.org/10.1016/j.jcta.2007.05.001), [author manuscript, §2](https://personal.ntu.edu.sg/bernhard/Publications/pub/SingerPG.pdf). **Confidence: read in source; the displayed application is a parameter specialization.** Corollaries 7–8 are not restricted to proper partial geometries, despite the paper's title.

For \(G=\mathbb F_p^2\), all nontrivial regular PDS are PCPs without a small-\(r\) restriction; see question 3. I have not certified (1) as the best available universal bound.

## 2. Positive Latin-square-type examples which are not PCPs

### A small exception: the Shrikhande graph

In \(G=\mathbb Z_4^2\),

\[
D=\{\pm(0,1),\ \pm(1,0),\ \pm(1,-1)\}
\]

is the connection set of the Shrikhande graph, with parameters \((16,6,2,2)=\mathrm{LS}_2(4)\). It is not the lattice graph \(L_2(4)\), whereas a degree-2 PCP gives that lattice graph. Thus it is not a PCP. Here \(r=2=n/2\); small absolute \(r\) alone is insufficient without an order restriction.

Source: A. Abdollahi, E. R. van Dam, M. Jazaeri, *Distance-regular Cayley graphs with least eigenvalue −2*, Des. Codes Cryptogr. **84** (2017), 73–85, [DOI 10.1007/s10623-016-0209-4](https://doi.org/10.1007/s10623-016-0209-4), [arXiv:1512.06019v2, §4.1 and Theorem 4.7](https://arxiv.org/html/1512.06019v2). **Confidence: read in source; non-PCP conclusion checks the degree-2 construction.** The original graph is due to S. S. Shrikhande, *The uniqueness of the \(L_2\) association scheme*, Ann. Math. Statist. **30** (1959), 781–798, [DOI 10.1214/aoms/1177706207](https://doi.org/10.1214/aoms/1177706207); that original full text was not accessed.

### The PCP bound used to certify the infinite examples

For

\[
G=\prod_{i=1}^v\mathbb Z_{p^i}^{\,2s_i},\qquad
m=\min\{s_i:s_i>0\},
\]

with prime \(p\) and nonnegative \(s_i\), not all zero, the maximum PCP degree is \(p^m+1\). This is Bailey–Jungnickel, Theorem 2.7, reproduced as Result 2.7 in Jedwab–Li below.

Original source: R. A. Bailey, D. Jungnickel, *Translation nets and fixed-point-free group automorphisms*, J. Combin. Theory Ser. A **55** (1990), 1–13, [DOI 10.1016/0097-3165(90)90043-V](https://doi.org/10.1016/0097-3165(90)90043-V). **Confidence: read in Jedwab–Li's restatement; original theorem text not accessed.**

### Galois-ring examples in powers of \(\mathbb Z_4\)

Davis–Xiang, Theorem 2.1, constructs positive LS PDS in \(\mathbb Z_4^{2k}\times\mathbb Z_2^{4\ell-4k}\) when \(1\le k\le j\le\ell\) and \(j\) is even, with

\[
n=4^\ell,\qquad r=4^{\ell-1}+1.
\]

Take \(j=k=\ell\) with even \(\ell\ge4\). Then \(G=\mathbb Z_4^{2\ell}\), whose maximum PCP degree is \(2^\ell+1<r\). These examples cannot be PCPs. In particular \(G=\mathbb Z_4^8,n=256,r=65\) works. Their ratio is \(r/n=1/4+1/n\). The paper also constructs negative LS PDS, but those are a different parameter family.

Source: J. A. Davis, Q. Xiang, *Negative Latin square type partial difference sets in nonelementary abelian 2-groups*, J. London Math. Soc. **70** (2004), 125–141, [DOI 10.1112/S002461070400540X](https://doi.org/10.1112/S002461070400540X), [arXiv:math/0407423, Theorem 2.1](https://arxiv.org/pdf/math/0407423). **Confidence: construction read in source; non-PCP status is the comparison with the published maximum degree above.**

### Lifting and product constructions: counterexamples even with \(r=o(n)\)

Jedwab–Li, Theorem 5.3, gives regular \(\mathrm{LS}_{p^{(a-1)s}}(p^{as})\) PDS in \(\mathbb Z_{p^a}^{2s}\) for every prime \(p\) and positive \(a,s\). For \(a\ge3\), their \(r=p^{(a-1)s}\) exceeds the PCP maximum \(p^s+1\). Taking \(a=3\) gives \(r=n^{2/3}\) and \(r/n=p^{-s}\to0\). Consequently, **\(r=o(n)\) is not sufficient in general abelian groups**. This does not contradict (1).

Their Theorem 3.15 also gives a product construction for LP-packings, producing further Latin-square-type PDS in direct products.

Source: J. Jedwab, S. Li, *Packings of partial difference sets*, Combinatorial Theory **1** (2021), #18, [DOI 10.5070/C61055384](https://doi.org/10.5070/C61055384), [arXiv:2012.00979](https://arxiv.org/abs/2012.00979), [published author PDF](https://www.sfu.ca/~jed/Papers/Jedwab%20Li.%20PDS%20packings.%202021.pdf). **Confidence: Results 2.7, Theorems 3.15 and 5.3 read in source; stated examples specialize these results.**

### Cyclotomy: a distinction needed when using this literature

Polhill's cyclotomy/product paper explicitly uses positive \(\mathrm{LS}_{(p-1)(p^2+1)}(p^4)\) PDS in \(\mathbb Z_{p^2}^4\) (Theorem 2.5 and the construction at the start of §3). For primes \(p\ge3\), \(r=(p-1)(p^2+1)>p^2+1\), the PCP maximum in that group, so these positive ingredients are non-PCP. Here \(r/n\sim1/p\). The final cyclotomic/product families emphasized in the paper are **negative** LS PDS; they must not be counted as positive LS counterexamples. I did not certify a positive non-PCP example defined solely as a union of finite-field cyclotomic classes.

Source: J. Polhill, *Generalizations of partial difference sets from cyclotomy to nonelementary abelian \(p\)-groups*, Electron. J. Combin. **15** (2008), #R125, [DOI 10.37236/849](https://doi.org/10.37236/849), [original PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v15i1r125/pdf/). **Confidence: read in source; non-PCP status checks the same published degree bound.**

## 3. What is classified in \(\mathbb Z_p^2\) and \(\mathbb Z_p^3\)?

**Order \(p^2\), elementary abelian.** Every nontrivial regular PDS in \(\mathbb F_p^2\) is a union of punctured one-dimensional \(\mathbb F_p\)-subspaces. Its parameters are \(\mathrm{LS}_r(p)\), \(2\le r\le p-1\). Up to complement one can restrict to \(2\le r\le(p+1)/2\) for odd \(p\). The subgroup and complementary-subgroup cases correspond to \(r=1,p\). This describes the sets; classification up to group automorphism further identifies selections under \(\operatorname{PGL}(2,p)\). It does not say that all choices of a given size are equivalent.

Source read: Aiso Heinze, *Applications of Schur rings in algebraic combinatorics: graphs, partial difference sets and cyclotomic schemes*, PhD thesis, Universität Oldenburg (2001), §3.2.3, Proposition 3.2.19 and Lemma 3.2.20, [repository record](https://oops.uni-oldenburg.de/321/), [full text, pp. 54–56](https://oops.uni-oldenburg.de/321/1/351.pdf), URN urn:nbn:de:gbv:715-oops-3519. **Confidence: read in source**, including its explicit convention of identifying complementary cases. This result predates 2016.

**The De Winter–Kamischke–Wang attribution.** The located paper is S. De Winter, E. Kamischke, Z. Wang, *Automorphisms of strongly regular graphs with applications to partial difference sets*, Des. Codes Cryptogr. **79** (2016), 471–485, [DOI 10.1007/s10623-015-0109-z](https://doi.org/10.1007/s10623-015-0109-z); preprint title *Automorphisms of strongly regular graphs*, [arXiv:1411.3429](https://arxiv.org/html/1411.3429).

Its main result restricts fixed vertices and vertices sent to neighbors under an automorphism. Corollary 4.2 recovers the multiplier theorem: for a regular PDS in an abelian group of order \(v\), if \(\Delta=(\lambda-\mu)^2+4(k-\mu)\) is a square, then \(D^{(u)}=D\) whenever \(\gcd(u,v)=1\). Section 5 excludes abelian PDS with parameters \((100,33,8,12)\) and \((100,36,14,12)\). **Confidence: read in source. I found no theorem in this paper claiming a new classification of PDS in \(\mathbb Z_p^2\) or \(\mathbb Z_p^3\).** The multiplier theorem is useful structural input, not a higher-dimensional PCP classification.

**Order \(p^3\), elementary abelian, odd \(p\): a precise partial classification.** Tantipongpipat's thesis proves: if \(p\equiv3\pmod4\), all regular PDS in \(\mathbb F_p^3\) are trivial (Theorem 41); if \(p\equiv1\pmod4\), every nontrivial one has Paley parameters

\[
\left\(p^3,\frac{p^3-1}{2},\frac{p^3-5}{4},\frac{p^3-1}{4}\right\)
\]

(Lemma 44). Theorem 45 says it selects a square or nonsquare half of each punctured one-dimensional subspace. Theorem 46 reduces the remaining selection problem to a signed matrix equation; §3.4 explicitly does not obtain a general classification of its solutions. Thus “Paley type” here classifies parameters, **not** equivalence to the classical Paley set.

Source: Uthaipon Tantipongpipat, *Cameron-Liebler line classes and partial difference sets*, University of Richmond honors thesis (2016), §3, [institutional record](https://scholarship.richmond.edu/honors-theses/929/), [author PDF, pp. 26–32](https://www.uthaipon.com/files/U-Tantipongpipat-undergraduate-thesis.pdf). **Confidence: read in source; this is an honors thesis, not a verified journal classification.** The congruence statements quoted here concern odd primes. Also, \(p^3\) is not a square, so these nontrivial PDS are outside \(\mathrm{LS}_r(n)\) with integer \(n\).

## 4. Robust and approximate results

**There is a directly relevant union-of-subgroups theorem.** With the unnormalized transform \(\widehat{1_A}(\chi)=\sum_{a\in A}\chi(a)\), put \(M_G(A)=\sup_\chi(-\widehat{1_A}(\chi))\). Sanders, Theorem 1.4, says that for a nonempty finite symmetric subset of a discrete abelian group there is a family \(\mathcal H\) of \(O(M_G(A))\) subgroups with

\[
M_G\(A\)\ge \bigl\(\log|A\triangle\textstyle\bigcup\mathcal H|\bigr\)^{\Omega(1)}.
\]

This uses the source's asymptotic notation; the exact-subgroup case \(M=0\) is treated separately, and logarithms describe the regime of large error. Equivalently, allowing \(1+M\) handles bounded/zero edge cases: at most \(O(1+M)\) subgroups and error at most \(\exp(O((1+M)^C))\) for an absolute \(C\). Theorem 1.3 implies: for each density bound \(\alpha_0>0\), there is \(C_{\alpha_0}\) such that, in finite abelian \(G\), \(|A|\ge\alpha_0|G|\) guarantees a subgroup \(H\) with \(|A\triangle H|\le C_{\alpha_0}(1+M)^{C_{\alpha_0}}\). Neither theorem fixes subgroup orders or intersections.

Source: T. Sanders, *Chowla's cosine problem*, Israel J. Math. **179** (2010), 1–28, [DOI 10.1007/s11856-010-0071-4](https://doi.org/10.1007/s11856-010-0071-4), [arXiv:0807.5104v2, Theorems 1.3–1.4](https://arxiv.org/pdf/0807.5104v2). **Confidence: read in source; the exponential formulation is a reformulation of its asymptotic bound.**

**A stronger recent approximation on the scale of the whole group.** Jin–Milojević–Tomon–Zhang, Theorem A.1: for every \(\delta>0\) and fixed \(0<\gamma<1/4\), every sufficiently large finite group \(G\) and inverse-closed \(A\subseteq G\) with \(M_G(A)\le N^\gamma\) admit a subgroup \(H\le G\) such that \(|A\triangle H|\le\delta N\). For \(0<\gamma<1/6\), \(M_G(A)<N^\gamma\) gives \(|A\triangle H|\le N^{1-\alpha}\), with some sufficiently small \(\alpha>0\) depending on \(\gamma\). In nonabelian groups \(M_G\) is defined using the least Cayley adjacency eigenvalue. For abelian groups it is the Fourier quantity above.

Source: Z. Jin, A. Milojević, I. Tomon, S. Zhang, *From small eigenvalues to large cuts, and Chowla's cosine problem*, [arXiv:2509.03490v2](https://arxiv.org/html/2509.03490v2#A1), revised 27 October 2025. **Confidence: read in the current arXiv version**, not just the older author PDF, where this was Theorem 14.1. These are errors relative to \(N\), not \(|A|\). For sparse LS PDS, an (o(N)) statement can be uninformative relative to the support; it does not give a degree-\(r\) PCP.

**Nearly two-valued spectra: nearby work, without a PCP conclusion.** Ihringer, Proposition 1.4: let a \(k\)-regular graph have order \(v\), real \(k>u\ge0>w\) and \(\varepsilon>0\), at least \(f_1\) and at most \(f_2\) restricted eigenvalues in ([u,k]), all eigenvalues at least \(w-\varepsilon\), and at least \(v-f_2\) eigenvalues in \([w-\varepsilon,w]\). If \(w^2+w>\varepsilon\), then \(v\le f_2(f_2+1)-f_1\). This is an approximate absolute bound, not an edit-distance or subgroup theorem. The paper also defines approximately strongly regular graphs by common-neighbor counts with means \(\lambda,\mu\) and both variances at most \(\sigma^2\), and develops approximate Krein/inertia bounds.

Source: F. Ihringer, *Approximately strongly regular graphs*, Discrete Math. **346** (2023), 113299, [DOI 10.1016/j.disc.2022.113299](https://doi.org/10.1016/j.disc.2022.113299), [arXiv:2205.05792v3](https://arxiv.org/pdf/2205.05792v3). **Confidence: read in source, Proposition 1.4 and introduction.** I did not verify a theorem upgrading nearly LS character values to closeness to exactly \(r\) equal-order, pairwise-trivially-intersecting subgroups. This is a limit of this check, not a nonexistence claim about the literature.

## 5. Cyclic groups and cyclic Sylow subgroups

**Ma's cyclic classification, with regularity essential.** A regular PDS \(D\subseteq\mathbb Z_v\setminus\{0\}\) has one of the following forms: \(D\cup\{0\}\) is a subgroup; \(\mathbb Z_v\setminus D\) is a subgroup; or \(v\) is a prime congruent to \(1\pmod4\) and \(D\) is the set of nonzero quadratic residues or nonresidues modulo \(v\). In particular the nontrivial cyclic examples are precisely these prime-order Paley examples. Since \(v=n^2>1\) is composite, cyclic groups have **no nontrivial regular LS PDS**. This does not exclude the subgroup and complementary-subgroup cases.

Original sources: S. L. Ma, *Partial difference sets*, Discrete Math. **52** (1984), 75–89, [DOI 10.1016/0012-365X(84)90105-5](https://doi.org/10.1016/0012-365X(84)90105-5); S. L. Ma, *A survey of partial difference sets*, Des. Codes Cryptogr. **4** (1994), 221–261, [DOI 10.1007/BF01388454](https://doi.org/10.1007/BF01388454).

Verification source: S. Huczynska, L. Johnson, *New constructions for disjoint partial difference families and external partial difference families*, J. Combin. Des. (2024), [DOI 10.1002/jcd.21930](https://doi.org/10.1002/jcd.21930), [arXiv:2305.06846, proof of Theorem 2.7](https://arxiv.org/pdf/2305.06846). **Confidence: read the explicit cyclic PDS classification in that proof, which cites both Ma papers; Ma's original full texts were not accessed.** This is a statement about regular PDS, not arbitrary difference sets or skew PDS.

**One cyclic Sylow subgroup already obstructs nontrivial PDS in an abelian group.** If finite abelian \(G\) has a cyclic Sylow-\(p\) subgroup and \(|G|\ne p\), it has no nontrivial regular PDS. If **all** Sylow subgroups of a finite abelian group are cyclic, the group is cyclic, so the preceding classification applies. These assertions do not automatically extend to nonabelian groups.

Sources read: Heinze's 2001 thesis above, Theorem 3.2.16, gives the Schur–Wielandt theorem that an abelian group with a cyclic Sylow subgroup has no nontrivial primitive Schur ring unless its order is prime; its PDS connection is explained in §3.1.3. Z. Wang, *Partial Difference Sets in Abelian Groups*, [Irsee 2017 slides](https://cage.ugent.be/~ml/irsee5/slides/Wang.pdf), states the PDS consequence explicitly under “Restrictions on the group,” attributed to Ma 1994. **Confidence: read in these sources; original Ma/Schur–Wielandt proofs not accessed.**

## Five-line summary

KNOWN — For finite abelian regular LS PDS, (1) forces a PCP; in \(\mathbb F_p^2\), every nontrivial regular PDS is already a PCP.  
KNOWN — Shrikhande gives \(\mathrm{LS}_2(4)\) without a PCP, and lifting gives non-PCP families with \(r=n^{2/3}=o(n)\) in nonelementary abelian groups.  
KNOWN — Small negative Fourier coefficients do force approximation by subgroups (Sanders; Jin–Milojević–Tomon–Zhang), with the distance scales and subgroup restrictions stated above.  
OPEN / NOT SETTLED BY THIS CHECK — The optimal universal exact threshold beyond (1), and sharper thresholds under additional group hypotheses, were not certified; no global priority or openness claim is made.  
OPEN / NOT SETTLED BY THIS CHECK — No quantitative near-LS-to-PCP stability theorem fixing exactly \(r\) order-\(n\) subgroups with trivial pairwise intersections was verified.
