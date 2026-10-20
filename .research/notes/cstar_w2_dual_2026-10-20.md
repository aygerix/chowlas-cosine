# W2 dual: exact doubled-maximum certificate and the uncanceled exterior cost

Checkpoint: 2026-10-20T05:46:32.196395+00:00. Ongoing research; no universal Chowla/C* or W2 constant is established. [Reproduction index](../experiments/cstar_structural_2026-10-20/README.md).

2026-10-20. CHAIN(c). No universal square-root bound is proved.

Let S=-S be a finite subset of Z\{0}, d=|S|, m=max S, D(x)=sum_{s∈S}e(sx), and W2={0}∪S∪(S+S). Write r_j(u)=1_S^{*j}(u). Positivity of K I+B_W2 is equivalent to

  integral (K+D)|q|²≥0

for every q with Fourier support in W2. The target is a universal K≥c sqrt(d).

## 1. A genuinely order-sensitive exact compression

Take

  q=e_m-e_{-m},   u=Dq.

Both q and u have support in W2. The following identities use the maximum m, not merely generic moment positivity:

  ||q||²=2,
  integral D|q|²=0,                     since 2m∉S,
  <q,u>=0,
  ||u||²=integral D²|q|²=2(d-1),        since r_2(2m)=1,
  integral D q conjugate(u)=2(d-1),
  integral D|u|²=2[r_3(0)-r_3(2m)].

Here r_2(2m)=1 is exactly the torsion-free extremal fact that s+t=2m with s,t∈S forces s=t=m.

Therefore, on the orthonormal pair q/sqrt(2), u/sqrt(2(d-1)), the adjacency quadratic form is exactly

  [ 0                 sqrt(d-1) ]
  [ sqrt(d-1)         t         ],

where t=[r_3(0)-r_3(2m)]/(d-1). Consequently W2 positivity implies

  K²+tK≥d-1,
  K≥(sqrt(t²+4(d-1))-t)/2.                         (1)

This gives the desired square-root bound whenever t≤C sqrt(d), with an explicit constant depending on C. The condition is concrete and falsifiable; no sign or size bound for t is assumed.

## 2. Exact interval falsification of the naive closure

For S={±1,...,±n}, d=2n, direct ordered-triple counting gives

  r_3(0)=3n(n-1),
  r_3(2n)=(n²+3n-4)/2,
  t=(5n²-9n+4)/(2(2n-1)) ∼ 5n/4.

The first identity counts ordered signed triples with one magnitude equal to the sum of the other two. For the second, all three summands must be positive; bounded positive compositions of 2n give binomial(2n-1,2)-3 binomial(n-1,2).

Thus the bound in (1) tends to 8/5 as n tends to infinity. It does not even grow like sqrt(d) for intervals, although intervals themselves are easy examples for stronger W2 tests. This is an exact counterexample to the claim that the doubled-maximum identity plus one multiplication by D closes W2 universally.

The surviving obstacle is specific: the new direction has a large positive diagonal of order d. A large coupling of size sqrt(d) to a zero-Rayleigh vector is insufficient unless exterior cost is also controlled. This matches the full-resolvent issue in the separate collective-boundary calculation.

## 3. Exact translation/Gram structure available beyond generic PSD

If K I+B_W2 is PSD, choose Gram vectors v_w, w∈W2, with

  <v_u,v_v>=K if u=v, 1 if u-v∈S, and 0 otherwise.

For every s∈S, the assignment v_t↦v_{s+t}, t∈{0}∪S, extends to an isometry from the central span V0=span{v_t:t∈{0}∪S} into the full Gram space. It is well-defined because the translated Gram matrix agrees exactly with the original one. These partial translations satisfy

  T_s v_0=v_s,
  T_s v_t=T_t v_s=v_{s+t},  s,t∈S.

Also v_0 is orthogonal to every v_u with u∈(S+S)\(S∪{0}). These are simultaneous exact constraints, not independent arbitrary block PSD conditions.

They do not automatically give commuting operators on a common invariant space: T_s maps V0 into the larger Gram space, and T_s T_t is generally undefined there. Therefore invoking a commuting-unitary dilation or an ordinary full Toeplitz extension at this point would require an additional theorem. No such extension has been established here.

## 4. Current scope

Actual output: an exact two-dimensional W2 certificate using the unique doubled maximum, a complete interval countercalculation showing why its hoped-for closure fails, and the precise partial-translation compatibility that a stronger Gram argument must exploit. This does not refute the W2 square-root conjecture. It rules out the specific shortcut of treating the large boundary coupling as a square-root certificate without paying its positive exterior diagonal.

## 5. Strict boundary leakage and a weak effective gap

For every nonempty S, one does have the strict inequality

  K_W2 > K_W1,   W1={0}∪S.                                (2)

Indeed suppose equality held at K. Let q be a nonzero kernel vector of K I+B_W1, extended by zero to W2. Its quadratic form in K I+B_W2 is zero. Positivity of that matrix forces the full matrix-vector product to vanish. Since Dq is supported in W2, this says the Laurent polynomial (K+D)q is identically zero. The Laurent polynomial ring over C is an integral domain, and neither factor is zero, a contradiction.

More generally, every nonempty finite row set I has strictly decreasing minimum adjacency eigenvalue upon the enlargement I'=I∪(I+S). The same proof works without central symmetry of I. This is a finite-support, torsion-free boundary argument. It does not assume a favorable sign for an exterior compression.

There is even a frequency-independent but extremely weak effective lower bound on the gap. Let N=|W2|≤d²+d+1. All eigenvalues of B_W1 and B_W2 are real algebraic integers in [-d,d], because their matrices are symmetric integer matrices with maximum degree at most d. Their algebraic conjugates obey the same bound. Let lambda<mu be their respective minimum eigenvalues (W2 first). If their monic irreducible minimal polynomials are different, their resultant is a nonzero integer. Its product formula, isolating the factor lambda-mu and bounding every other root difference by 2d, gives

  mu-lambda ≥ (2d)^{-(N(d+1)-1)}.

If their minimal polynomial is the same, its degree is at most d+1; its nonzero integer discriminant gives an even stronger bound by the same root-difference argument. In particular a safe uniform conclusion is

  K_W2-K_W1 ≥ (2d)^{-N(d+1)}.                            (3)

No explicit frequency bound or root-separation theorem is imported here: the resultant/discriminant products themselves establish (3). This gap is exponentially tiny in a polynomial of d and is nowhere near the required sqrt(d) scale. It establishes strict quantified leakage, not a solution of C*. The meaningful missing ingredient is a much stronger collective lower bound on leakage after accounting for the exterior resolvent.
