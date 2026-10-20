# Exact attainment and record-cardinality reduction for Chowla

Checkpoint: 2026-10-20T05:32:53.486301+00:00. Research remains ongoing; no universal Chowla/C* theorem is claimed. Reproduction: [experiment index](../experiments/cstar_structural_2026-10-20/README.md).

2026-10-20. This is a rigorous reduction, not a structural theorem or a Chowla bound. No novelty claim is made.

Write

  M(A) = -min_{t in R/Z} sum_{a in A} cos(2πat),
  kappa(n) = inf_{A subset positive integers, |A|=n} M(A).

The notation kappa avoids confusing this extremal function with the normalization K=2M used in CSTAR.

## 1. The fixed-cardinality infimum is attained

**Theorem.** For every positive integer n there is an n-element set A of distinct positive integers with M(A)=kappa(n).

**Proof.** For a vector a=(a_1,...,a_n) of distinct positive integers let

  H_a = {(a_1 t,...,a_n t) mod 1: t in R/Z} subset T^n,
  F(x) = sum_{j=1}^n cos(2πx_j),
  J(H) = -min_{x in H} F(x).

Then H_a is a compact connected subgroup and J(H_a)=M(A). Choose a minimizing sequence H_{a(r)}. The hyperspace of nonempty closed subsets of the compact metric space T^n is compact in Hausdorff distance, so after passing to a subsequence H_{a(r)} converges to a nonempty compact set H.

Three facts about this limit require checking.

1. H is a subgroup: 0 is in H, and if x,y are in H choose x_r,y_r in H_{a(r)} converging to them; x_r-y_r converges to x-y, which belongs to H by Hausdorff convergence.
2. H is connected. Otherwise H is the disjoint union of two nonempty relatively closed compact sets U,V at positive distance. Small disjoint open neighborhoods of U,V cover H and, eventually, H_{a(r)}. Hausdorff convergence forces H_{a(r)} to meet both neighborhoods, contrary to connectedness.
3. None of the characters e_j, e_i-e_j, e_i+e_j is trivial on H. Here integer vectors denote the corresponding characters T^n→T. Each is nontrivial on every H_{a(r)}, since a_j is nonzero and a_i±a_j is nonzero for i≠j. A nontrivial character on a compact connected subgroup has image all of T: its image is a nontrivial compact connected subgroup of T. If such a character were trivial on H, choose x_r in H_{a(r)} with character value 1/2. A convergent subsequence would give x in H with that same value, a contradiction.

The objective is continuous under Hausdorff convergence, since F is uniformly continuous: the two minima differ by at most the modulus of continuity of F at the Hausdorff distance. Thus J(H)=kappa(n).

A closed connected subgroup H of T^n is a torus. Its Lie algebra V is a rational subspace of R^n, and its integral cocharacter lattice Lambda=V∩Z^n spans V over R. Every character in the finite list in item 3 is a nonzero linear functional on V. Indeed, if its derivative vanished on V, it would vanish on the connected group H. Therefore none of the corresponding hyperplanes contains V. The lattice Lambda contains a point w outside their union: in an integral basis of Lambda this is avoidance of finitely many nonzero integer linear forms, which can be achieved, for example, by evaluating the integer vector (1,T,...,T^{d-1}) for an integer T outside finitely many polynomial roots.

Consequently w_j≠0 and w_i≠±w_j for i≠j. The circle H_w is contained in H. Hence

  J(H_w) ≤ J(H) = kappa(n).

But B={|w_1|,...,|w_n|} has n distinct positive elements, and evenness of cosine gives J(H_w)=M(B)≥kappa(n). Equality follows. ∎

The sign of the containment inequality matters: restricting the domain raises its minimum, so it *lowers* its negative minimum. This is why specialization to a circle proves attainment rather than the opposite inequality.

### Useful exact strengthening of the limit argument

For any fixed integer character k, in a Hausdorff-convergent sequence of connected closed subgroups H_r→H, the statement “k vanishes on H_r” eventually agrees with “k vanishes on H.” If k vanishes on H, infinitely many nontrivial restrictions would supply points with value 1/2 and give a contradiction as above. If k does not vanish on H, vanishing along a subsequence contradicts approximation of a point of H on which k is nonzero. Thus annihilator lattices converge by eventual membership for each fixed integer vector. In fact this eventual-membership assertion also holds for disconnected closed subgroups: every nontrivial subgroup of T contains a point whose distance to 0 is at least 1/3, which replaces the value 1/2 in the proof. Connectedness is needed later for the torus/cocharacter specialization, not for eventual character membership itself.

The proof supplies no effective upper bound for max B, and does not prove that a selected bounded-box optimizer is globally optimal. A primitive representative can always be chosen by dividing w by its coordinate gcd.

## 2. Record-cardinality counterexamples exist if Chowla fails

A basic uniform bound is M(A)≥1/2 for every nonempty A. To see this, p=M(A)+f_A is nonnegative, has integral M(A), and its Fourier coefficient at every a∈A is 1/2. Thus 1/2=|p-hat(a)|≤integral p=M(A).

Set r(n)=kappa(n)/sqrt(n). If the universal Chowla assertion fails, inf_n r(n)=0. Because every r(n)>0, there are increasing strict running-record cardinalities n_j tending to infinity such that

  r(n_j) < min_{1≤m<n_j} r(m),    r(n_j)→0.

At each n_j choose an attained minimizer A_j from Theorem 1. Then simultaneously:

- M(A_j)=kappa(n_j), exact global optimality among all integer sets of the same cardinality;
- M(B)/sqrt(|B|)>M(A_j)/sqrt(n_j) for every nonempty proper B⊂A_j;
- more strongly, the same strict inequality holds for *every* positive-integer set B with 1≤|B|<n_j, not only subsets;
- R(A_j)→0, so this is still a hypothetical Chowla-counterexample sequence.

This removes freedom to choose a merely padded example when selecting a hypothetical counterexample. It does not prove that an exact optimizer cannot itself have a padded decomposition or a rare-positive-excursion geometry. Any such exclusion is a new theorem requiring proof.

## 3. A precise optimality condition, and its limits

Let A be one of the strict record minimizers, n=|A|, M=M(A), H=f_A+M≥0. For D⊂A of size 0<d<n, strict record minimality gives

  sup_x [f_D(x)-H(x)] > -M(1-sqrt(1-d/n)).

Indeed the left side is M(A\D)-M. This is exact and gives a Boolean barrier-discrepancy condition, not a fractional KKT condition.

If n is even and |D|=n/2, write g_D=2f_D-f_A. Applying the displayed condition to D and A\D gives both

  sup_x [g_D(x)-H(x)] > (sqrt(2)-1)M,
  sup_x [-g_D(x)-H(x)] > (sqrt(2)-1)M.

Therefore a balanced Boolean signing with |g_D|≤H+(sqrt(2)-1)M everywhere would already contradict strict record minimality. No theorem constructing such a signing is supplied here. The existence of fractional signing g=0 says nothing about Boolean feasibility.

Global fixed-cardinality minimality also gives, for every disjoint replacement C⊂positive integers\A with |C|=|D|,

  sup_x [f_D(x)-f_C(x)-H(x)] ≥ 0.

The supremum equals M((A\D)∪C)-M. This is an exact exchange obstruction that hereditary minimality alone does not supply. Again it is not differentiable stationarity and does not imply a probability measure on the original minimum set with equal coefficient moments.

## 4. What remains open

The reduction proves that failure of Chowla can be tested on exact global cardinality minimizers at strict running records. It does not give quantitative floor flatness, uniform integrality-gap control, frequency compactness uniform in n, or a torsion-free exclusion of the finite-group quadric anatomy. The argument uses torus geometry to establish attainment, but at present yields no quantitative invariant distinguishing the surviving models at the many-spike step of C*.

## 5. Strict subadditivity and algebraicity

**Theorem.** For positive n,m, kappa(n+m)<kappa(n)+kappa(m).

Choose attained minimizers A,B. Their minimum sets Z_A,Z_B in T are finite and exclude 0. Finiteness follows because f_A+M(A) is a nonzero real-analytic trigonometric polynomial. Choose an integer Q divisible by all denominators of rational points of Z_A. For q a positive multiple of Q, every rational x∈Z_A satisfies qx=0∉Z_B. For an irrational x∈Z_A and a target y∈Z_B, the congruence qx=y mod 1 has at most one integer solution q, since two would imply x rational. Only finitely many q are therefore excluded. Choose a remaining q>max A; then A and qB are disjoint, and the two polynomials have no common minimum point. Their nonnegative excess functions have strictly positive sum on compact T. Consequently

  M(A∪qB)<M(A)+M(B)=kappa(n)+kappa(m),

which proves the assertion. This proof is exact, but supplies no lower bound for the strict improvement.

Also kappa(n) is a real algebraic number. For an attained A, write f_A(x)=P_A(cos(2πx)), where P_A is a sum of integer Chebyshev polynomials. Its minimum on [-1,1] is attained at an endpoint or a real root of P_A', so its value is algebraic. This is not an effective computation of kappa(n), nor a degree bound in terms of n.

## 6. Quantitative exclusion of sufficiently separated dilated blocks

The strict-subadditivity proof has a useful quantitative converse. For any finite positive-integer sets A,B with A∩qB empty,

  M(A∪qB) ≥ M(A)+M(B) - (π²/(2q²)) sum_{a∈A}a².                 (6.1)

To prove it, take a minimum point x of f_A, fix any minimum point y of f_B, and choose h with |h|≤1/(2q) and q(x+h)=y mod 1. Since f_A'(x)=0 and ||f_A''||∞≤4π² sum a², Taylor's theorem gives

  f_A(x+h)≤-M(A)+2π²(sum a²)h²,
  f_B(q(x+h))=-M(B).

Evaluation at x+h proves (6.1). Thus independent-phase behavior is quantitatively unavoidable at sufficiently large dilation, even without genericity assumptions on q.

For fixed block cardinalities a,b, define the strictly positive number

  delta_{a,b}=kappa(a)+kappa(b)-kappa(a+b).

If A∪qB is an exact global cardinality minimizer, (6.1) forces

  q² ≤ π²(sum_{u∈A}u²)/(2 delta_{a,b}).                         (6.2)

For a strict running-record optimizer C=A∪qB of size n=a+b, there is an explicit version that avoids unknown lower-cardinality optima. Put M=M(C) and

  gamma_{a,b}=(sqrt(a)+sqrt(b))/sqrt(a+b)-1>0.

Both blocks are proper subsets (and dilation preserves M), so strict record minimality gives M(A)+M(B)>M(1+gamma_{a,b}). Combining with (6.1) yields

  q² < π²(sum_{u∈A}u²)/(2 M gamma_{a,b}).                      (6.3)

In particular, if X=max A,

  q/X < π sqrt(a/(2 M gamma_{a,b})).                          (6.4)

These inequalities exclude a concrete class of artificial padding: record minimizers cannot consist of a slow block plus an arbitrarily remote common-dilation block. For balanced blocks gamma=sqrt(2)-1; the bound is quantitative even when M/sqrt(n) is small. It does not exclude blocks separated by merely a fixed factor, general high-frequency blocks without a common large divisor, or large frequency complexity inside B. No uniform-in-n conclusion is asserted.

## 7. A bounded-coefficient cross-relation constraint

Here is a second finite constraint, obtained by elementary moment technology. It is included as a precise consequence of exact optimality, not claimed as a new many-spike ingredient.

Let C=A∪B be a disjoint partition with |A|=a, |B|=b. Suppose there is **no** equality

  sum_{u∈A} r_u u = -sum_{v∈B} s_v v ≠ 0,
  r_u,s_v integers, sum |r_u|≤k+1, sum |s_v|≤k+1.             (7.1)

Then

  M(C)≥M(A)+M(B)-2(a²+b²)log(2k+1)/k.                       (7.2)

**Proof.** Put z_A=a-f_A≥0 and Z_A=∫z_A^k. The polynomial z_A^k has at most (2k+1)^a distinct Fourier frequencies. Since it is nonnegative, each Fourier coefficient has absolute value at most Z_A. Consequently

  (a+M(A))^k=||z_A^k||∞≤(2k+1)^a Z_A.

For the probability density p_A=z_A^k/Z_A, Hölder gives

  ∫z_A p_A = (∫z_A^{k+1})/Z_A ≥ Z_A^{1/k}
             ≥(a+M(A))(2k+1)^{-a/k}.

Using M(A)≤a and 1-exp(-t)≤t,

  ∫f_A p_A≤-M(A)+2a²log(2k+1)/k.

Define p_B similarly. Every frequency of p_A (respectively f_Ap_A) is a sum of elements of A with integer coefficient l1-norm at most k (respectively k+1). Hypothesis (7.1) therefore implies, by taking Fourier constant terms,

  ∫p_Ap_B=1,
  ∫f_Ap_Ap_B=∫f_Ap_A,
  ∫f_Bp_Ap_B=∫f_Bp_B.

Internal zero-frequency relations cause no difficulty: they are already included in the separate constant coefficients. The nonnegative function p_Ap_B is thus a probability density whose expected f_C is at most -M(A)-M(B) plus the displayed error. Its expectation is at least min f_C=-M(C), proving (7.2). ∎

Consequences:

- For an exact global cardinality optimizer C, every partition A∪B has a nonzero cross relation (7.1) whenever 2(a²+b²)log(2k+1)/k < delta_{a,b}.
- For a strict running-record optimizer, it suffices that this error be at most M(C)gamma_{a,b}, using the strict lower bound M(A)+M(B)>M(C)(1+gamma_{a,b}).

Since log(2k+1)/k tends to zero, these are finite bounds. They rule out a partition that is independent up to the indicated additive-relation order. They do NOT yield n−1 linearly independent bounded relations: one relation with large support can cross every partition. Hence one cannot infer a bound on primitive max frequency from this argument. This explicitly identifies the missing rank/rigidity input rather than treating cross-relation connectivity as full frequency control.

## 8. Explicit Boolean counterexample to unconditional strict dimension drop

A tempting strengthening is: if a Boolean cosine sum has character rank at least two, some admissible integral one-parameter specialization avoids its minimum set and therefore strictly decreases M. This statement is false, even with six distinct characters.

In this subsection x,y are angles modulo 2π. Let

  F(x,y)=cos x+cos 3x+cos y+cos(y+x)+cos(y+3x)+cos(y+4x).

All six integer character vectors are nonzero and distinct up to sign, and they span Z². The exact identity

  F(x,y)+2 = (1/2)|1+e^{ix}+e^{iy}(e^{ix}+e^{4ix})|²

proves F≥-2. At x=π, both 1+e^{ix} and e^{ix}+e^{4ix} vanish. Thus the whole circle {x=π} consists of global minima, independently of y.

An admissible integral line (x,y)=(at,bt) must have a≠0 because the character x occurs. It therefore meets {x=π}. Every admissible line has exactly the same M=2 as the rank-two ambient torus. There is no line giving strict improvement. For example a=1,b=10 gives the six-element set {1,3,10,11,13,14}, with M=2 exactly. This is also a concrete unavoidable-floor factorization, rather than an abstract possibility of a positive-dimensional zero locus.

The example comes from four points {(0,0),(1,0),(1,1),(4,1)} whose six unordered differences are distinct up to sign. The four-point exponential sum has a common factor vanishing at x=π; its squared modulus produces exact Boolean difference coefficients. Thus a spectral-factor argument cannot dismiss these minimum hypersurfaces solely from Booleanity.

This example is not a global six-element optimizer: the consecutive set {1,...,6} has M<2. One exact verification is that

  2+sum_{j=1}^6 T_j(t)=32t^6+16t^5-40t^4-16t^3+12t²+3t+1

has no real roots on [-1,1] and is positive at t=0. Exact rational Sturm computation gives endpoint sign sequences (+,-,+,+,-,-,-) at -1 and (+,+,+,+,-,+,-) at 1, both with three variations. The lack of optimality is important: a theorem asserting strict dimension drop only for *global* cardinality optimizers remains unproved and is not contradicted here. Such a theorem must use global extremality in a substantive way; Booleanity, rank, and nonnegative factorization alone do not suffice.
