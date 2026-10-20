# Exact idempotent mixing: quantitative deductions and countermodels

Checkpoint: 2026-10-20T05:46:32.196395+00:00. Ongoing research; no universal Chowla/C* or W2 constant is established. [Reproduction index](../experiments/cstar_structural_2026-10-20/README.md).

2026-10-20. Let S=−S⊂Z\{0}, N=|S|, f=sum_{s∈S} e(sx), K=−min f, h=K+f≥0, p=h/K. Haar measure has mass one. Then

  h*h=h+K²−K,
  p*p=1−1/K+p/K,
  integral h=K, integral h²=K²+N.

These are the exact Boolean coefficient identities, not an additional assumption. No C* bound is proved below.

## 1. Concentrated spike mass must have nearly full sumset

For a measurable E let tau=integral_E p and F=E+E (use an outer-measurable hull if needed). Independence and the exact identity give

  tau² ≤ integral_F p*p = (1−1/K)|F| + (1/K) integral_F p
         ≤ (1−1/K)|F|+1/K.

For K>1, consequently

  |E+E| ≥ (tau²−1/K)/(1−1/K).

If tau≥1−delta, the weaker convenient form is |E+E|≥1−2delta−1/K. Thus if |E+E|≤L|E|, then

  tau² ≤ (1−1/K)L|E|+1/K.

This is a useful conditional exclusion of concentrated *mass* on a small-doubling spike set. It does not control concentrated *energy* whose p-mass is tiny. The finite quadric models satisfy it because their cone sumsets fill the group. This is an elementary mixing consequence, not claimed as new.

## 2. Exact threshold-overlap inequality

For E_T={h≥T}, positivity gives, for every x,

  T² |E_T ∩ (x−E_T)| ≤ h(x)+K²−K.

More generally, writing g_T=h 1_{h>T}, the discarded convolution contributions are nonnegative and at most 2KT, so

  h(x)+K²−K−2KT ≤ (g_T*g_T)(x) ≤ h(x)+K²−K.

At scales h≫K²+KT, high peaks behave approximately like a self-convolution of high peaks. The critical problem is that such peaks need not carry a positive fraction of the energy.

## 3. Explicit quadric model defeats the K²-tail strategy

Work on the finite group F_p^r with normalized Haar measure, r≥6 even, and a nondegenerate split quadratic form with positive Gauss sign. Let S be its nonzero zero cone and f its Fourier sum. Put a=p^{r/2−1}. The exact values are

  N=|S|=p^{r−1}+(p−1)a−1,
  K=a+1,
  h(0)=N+K=p^{r−1}+p^{r/2},
  h(x)=p^{r/2} on nonzero points of the dual cone,
  h(x)=0 elsewhere.

The ordinary spike height divided by K² is asymptotic to p^{2−r/2}, tending to zero. The origin's contribution to integral h² is

  h(0)²/p^r,

whose ratio to K²+N is asymptotic to 1/p. Therefore, for any fixed c>0,

  integral_{h≥cK²} h² / integral h² →0.

Meanwhile N/K²≈p→infinity. Thus almost all counterexample energy can lie below the scale at which the additive K² term in h*h becomes negligible. A high-spike iteration that only exploits h≫K² necessarily misses the main energy in this explicit model. Torsion-freeness must enter before or inside such a strategy; positivity and exact idempotence alone cannot repair it.

## 4. Sharp warning about approximate mixing in absolute L1

Let F_L be the normalized Fejér kernel of order L, and choose any K≥2. The strictly positive probability density

  q=1+(F_L−1)/K

has

  integral q²=1+[ (2L/3)+(1/(3L))−1 ]/K²,

which is arbitrarily large as L/K² grows. Its exact mixing defect is

  r=q*q−(1−1/K)−q/K=(F_L*F_L−F_L)/K².

Since both kernels in the numerator are probability densities,

  ||r||_1≤2/K².

For even L, the coefficient at L/2 gives ||r||_1≥1/(4K²). Thus the defect is genuinely of order K^{-2}, while the L2 energy can be unbounded independently. Any proposed mixing-to-energy stability statement tolerating a universal O(K^{-2}) L1 defect is false, already for positive trigonometric polynomials on the circle.

The density q has positive floor, so K is a negativity allowance rather than the actual contact scale of K(q−1). This can be repaired without changing the conclusion, as follows.

## 5. The approximate countermodel can have an actual zero

Let Q=max q, choose an integer m arbitrarily large, and put

  b(x)=F_m(x−x0)/m,  0≤b≤1,  b(x0)=1,
  epsilon=integral q b≤Q/m,
  p=q(1−b)/(1−epsilon).

Then p is a nonnegative trigonometric polynomial of mean one, p(x0)=0, and

  ||p−q||_1≤2epsilon/(1−epsilon).

Probability convolution is L1-Lipschitz, hence the mixing defect of p is at most

  2/K²+(2+1/K)||p−q||_1.

Choosing m≫QK² makes this (2+o(1))/K². Also

  integral q²(1−b)² ≥ integral q²−2Q epsilon.

Choosing m still larger makes the energy loss arbitrarily small. Therefore p can simultaneously have actual minimum zero, unbounded L2 energy, and mixing defect O(K^{-2}). The associated f=K(p−1) has actual negative minimum −K. It is not Boolean: the argument isolates the indispensable exact spectral constraint rather than supplying a counterexample.

## 6. What stronger defect control actually yields

For any even real probability density p and r=p*p−(1−1/K)−p/K, write a_j=K p_hat(j) for j≠0. Then

  |a_j(a_j−1)|≤K²||r||_1.

Thus o(K^{-2}) L1 mixing error does force every scaled Fourier coefficient uniformly close to {0,1}. For eta=K²||r||_1<1/8, the real-root estimate gives dist(a_j,{0,1})≤2eta. This is coefficientwise rounding only: the number of coefficients and preservation of nonnegativity after rounding remain uncontrolled. The Fejér countermodel sits exactly at the scale where this conclusion need not hold.

## Current conclusion

The useful complementary facts are a precise mass-versus-sumset inequality, the exact truncated-convolution error scale, an explicit permitted model with virtually all energy below K², and a circle countermodel showing that O(K^{-2}) absolute mixing error is too weak even with contact at zero. None excludes exact torsion-free Boolean counterexamples. A successful spike-mixing estimate must either operate below K² using integer-frequency geometry, or preserve coefficientwise Boolean information far more strongly than an absolute L1 mixing approximation.

## 7. Stronger extension: arbitrarily small absolute mixing defect is insufficient

The O(K^{-2}) example can be strengthened. Fix K≥2 and eta>0, take alpha=eta/K (with alpha≤1), and set

  q=1+alpha(F_L−1).

Then

  r=q*q−(1−1/K)−q/K
   =alpha²(F_L*F_L−1)−(alpha/K)(F_L−1),
  ||r||_1≤2(eta²+eta)/K²,
  integral q²=1+alpha²[(2L/3)+(1/(3L))−1].

For any prescribed positive defect tolerance and any prescribed energy, choose eta sufficiently small and then L sufficiently large. The density has smaller defect and larger energy than prescribed. The notch construction in §5 again enforces an actual zero with arbitrarily little additional defect or energy loss.

Thus there is NO nonzero absolute L1 stability tolerance that implies an energy bound, even for nonnegative finite-degree trigonometric polynomials with actual contact at zero. In this strengthened example all scaled nonzero coefficients K q_hat(j) lie in [0,eta]: they are individually close to the Boolean value zero, but arbitrarily many tiny coefficients collectively carry huge energy. This is compatible with the coefficientwise conclusion of §6.

The precise missing stability hypothesis is control of the accumulated Fourier mass in the near-zero branch (or a bound on spectral size/degree), not merely that each coefficient is close to one of the two roots. Exact Booleanity annihilates that entire branch; any approximation-based spike proof must retain this distinction.

## 8. What L2 defect controls, unlike L1 defect

For an even real p, define a_j=K p_hat(j), j≠0, and round each a_j to its nearest element of {0,1}. Let B be the indices rounded to 1, D_B=sum_{j∈B}e(jx). For every real a,

  dist(a,{0,1})≤2|a(a−1)|.

Parseval therefore gives the exact robust rounding estimate

  ||K(p−1)−D_B||_2 ≤ 2K² ||r||_2.

Furthermore the Fourier energy in the small branch |a_j|≤1/2 satisfies

  sum_{|a_j|≤1/2} |p_hat(j)|² ≤4K² ||r||_2².

Consequently a relative L2 defect o(||p−1||_2/K) does exclude the tiny-coefficient escape in §7. It guarantees an energy-close Boolean spectrum. It still does not preserve p≥0 after Boolean rounding: controlling the induced negative excursions is a separate issue. This estimate is elementary coefficient algebra and is not a new Chowla bound.

## 9. Stronger contact construction with evenness and nonnegative Fourier coefficients

This replaces the signed-spectrum notch in §§5,7 when preserving the sign of every Fourier coefficient matters. Fix K≥2, 0<eta<1/2, alpha=eta/K, and q=1+alpha(F_L−1). Let

  g_m(x)=sum_{j=1}^m cos(2πjx),  m_m=−min g_m,

and choose an integer Q>L−1. Define

  delta_* = min_{g_m(Qx)<0} q(x)/(−g_m(Qx)),
  p(x)=q(x)+delta_*g_m(Qx).

Since q≥1−alpha>0, the infimum is attained away from the zero set of g_m(Qx), and p≥0 with equality somewhere. Both summands are even and their nonconstant spectra are disjoint. All their nonzero Fourier coefficients are nonnegative. The constant coefficient stays one.

The contact coefficient has exact bounds

  (1−alpha)/m_m ≤ delta_* ≤1/m_m.

The lower bound is immediate. For the upper bound, take a point y where g_m(y)=−m_m, and its Q preimages x_k=(y+k)/Q. Since Q>deg q, the average of q(x_k) is exactly its constant coefficient 1. At least one preimage has q(x_k)≤1, proving the bound. This is an exact roots-of-unity averaging argument.

Useful explicit estimates are

  m_m≥2m/(3π),
  ||g_m||_1≤1+(1/2)log(2m+1).

For the first, evaluate the Dirichlet kernel D_m=1+2g_m at x=3/[2(2m+1)], where its numerator is −1, and use sin u≤u. For the second, integrate |D_m(x)|≤min(2m+1,1/[2 dist(x,Z)]).

Consequently

  ||p−q||_1 ≤ [3π/(2m)] [1+(1/2)log(2m+1)] =: epsilon_m →0,
  ||p||_2²=||q||_2²+(delta_*²m)/2 ≥||q||_2².

The old scaled coefficients are K q_hat(j)=eta(1−|j|/L) in [0,eta]. The new ones equal K delta_*/2≤3πK/(4m). Therefore m≥3πK/(4eta) ensures EVERY nonzero scaled coefficient belongs to [0,eta].

Because p,q are probability densities, their mixing defects differ in L1 by at most (2+1/K)epsilon_m. Thus

  ||p*p−(1−1/K)−p/K||_1
  ≤2(eta+eta²)/K²+(2+1/K)epsilon_m.

Given any K≥2, any positive desired defect tolerance, any desired L2 energy, and any positive scaled-coefficient cap, first choose eta below the cap and sufficiently small; then choose L sufficiently large; finally choose m sufficiently large. This produces an even, nonnegative, finite-degree trigonometric polynomial p with mean one, actual minimum zero, all scaled Fourier coefficients in [0,eta], arbitrarily small absolute L1 mixing defect, and arbitrarily large L2 energy. No negative Fourier coefficients or loss of energy is involved.

## 10. Sharp L2 distinction for the strengthened construction

For any such p with all a_j=K p_hat(j) in [0,eta], the defect has coefficients −a_j(1−a_j)/K². Parseval gives the two-sided estimate

  [(1−eta)/K] ||p−1||_2 ≤ ||r||_2 ≤ [1/K] ||p−1||_2.

Thus this construction does NOT defeat a hypothesis of relative L2 mixing error o(||p−1||_2/K). Its tiny L1 defect lives in a high-energy, narrow-spike error. More generally, for any real p, the energy of the branch |a_j|≤eta<1 is bounded by

  sum_{|a_j|≤eta} |p_hat(j)|² ≤ [K²/(1−eta)²] ||r||_2².

This precisely separates the insufficient absolute L1 hypothesis from a meaningful energy-sensitive approximation hypothesis.

## 11. Direct Boolean projection: two different failure modes and a sufficient floor bound

For the strengthened example with eta<1/2, nearest-Boolean Fourier rounding sends every nonconstant coefficient to zero. The projected density is 1. It remains positive but loses the actual zero AND all nonconstant energy. This explains why coefficientwise proximity to {0,1} alone is not an energy-preserving approximation.

Projection need not even preserve positivity in general. Take K=2 and q=1+(F_7−1)/2, and impose actual contact using the same positive-coefficient Dirichlet padding with m sufficiently large that the new scaled coefficients are below 1/2. Nearest-Boolean rounding keeps exactly frequencies ±1,±2,±3, since 1−j/7 exceeds 1/2 exactly for j=1,2,3. Its density is

  p_B=1+cos(2πx)+cos(4πx)+cos(6πx).

At cos(2πx)=1/4, p_B=−5/16. The input is nonnegative, even, has nonnegative Fourier coefficients, and attains zero; the nearest Boolean projection is not nonnegative.

There is, however, an elementary valid sufficient condition. Let b_j be the rounded coefficients and E_1=sum_{j≠0}|a_j−b_j|. Then

  ||D_B−K(p−1)||_infinity≤E_1.

If min p=0, this implies |M(D_B)−K|≤E_1. Therefore E_1=o(K) DOES preserve the actual negative threshold relatively. With d nonzero input frequencies, the L2 rounding estimate supplies E_1≤2K² sqrt(d)||r||_2, so the sufficient condition is ||r||_2=o(1/[K sqrt(d)]). This condition depends on spectral size; there is no claim that every approximation method fails. Exact Booleanity, or a sufficiently strong energy-and-floor-preserving substitute, is the distinction.
