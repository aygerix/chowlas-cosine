# An asymptotic counterexample to the fixed positive-half autocorrelation 3D certificate

Checkpoint: 2026-10-20T06:12:18.377072+00:00. Ongoing research; no universal Chowla/C* or W2 constant is established. [Reproduction index](../experiments/cstar_structural_2026-10-20/README.md).

2026-10-20.  This concerns ONLY the compressed span {1,D,|F_A|²/|A|−1}. It is not a counterexample to Chowla, nor to the full W2 certificate. The proof below establishes failure of a universal square-root bound for this particular universally supported profile family.

## Theorem

Let a parameter n tend to infinity, alpha=n^(−1/3), X=round(n/alpha), and independently include each integer 1≤a<X in A with probability

  p_a=2alpha(1−a/X).

Write m=|A|, F_A(x)=sum_{a∈A}e(ax), D=F_A+conjugate(F_A), and t=|F_A|²/m−1. On the event m>0, let K_3 be minus the smallest generalized eigenvalue of multiplication by D on span{1,D,t}, with its actual L2 Gram matrix. Then

  K_3 = (21630/241 + o_p(1)) X/n
      = (89.7510373444... + o_p(1)) n^(1/3).

In particular K_3/sqrt(m)→0 in probability. Therefore neither this full three-dimensional certificate nor its restricted scalar-positive-profile subfamilies can provide a universal c sqrt(m) bound.

The constant is large. Numerical samples through m≈100,000 still exhibit K_3/sqrt(2m)≈0.93. Those finite data do NOT show a collapsing ratio; the asymptotic proof, not a misread finite trend, establishes the counterexample.

## 1. Deterministic continuum shapes and exact Gram

Set phi(x)=2 integral_0^1 (1−u)e(ux)du, d=2Re phi=2sinc²(pi x), and v=|phi|². Their Fourier coefficient profiles, in the real-line transform convention, are

  d_hat(s)=2(1−|s|)_+,
  v_hat(s)=U(|s|) for |s|≤1, zero otherwise,
  U(s)=(2/3)(1−s)²(2+s)=4/3−2s+(2/3)s³.

The cubic shape Gram is

  J = integral_R d(x) [[d(x)²,d(x)v(x)],[d(x)v(x),v(x)²]] dx
    = [[22/5,736/315],[736/315,2369/1890]].

Its determinant is 5543/99225>0. Thus the two profiles are linearly independent in the d-weighted quadratic form. In particular a fixed multiple of v cannot cancel the deterministic d-spike.

Exact polynomial derivation: for 0≤s≤1,

  (d_hat*d_hat)(s)=8/3−4s²+2s³,
  (v_hat*v_hat)(s)=s^7/105−2s^5/5+4s^4/9+4s³/3−32s²/15+88/105.

The latter is obtained by integrating

  2 integral_s^1 U(y)U(y−s)dy + integral_0^s U(y)U(s−y)dy.

Therefore J_12=2 integral_0^1 U(s)(8/3−4s²+2s³)ds=736/315 and J_22=4 integral_0^1(1−s)(v_hat*v_hat)(s)ds=2369/1890. Similarly J_11=22/5. All are exact rational polynomial integrals, not numerical recognition. Also integral d v=22/15 and integral v²=88/105.

## 2. Deterministic periodic-to-continuum limit

Let mu=E F_A=sum p_a e(ax), Dbar=2Re mu, and tbar=|mu|²/n−1. Using n~alpha X is harmless at relative o(1) precision. The actual expected cardinality is alpha(X−1)=n(1+o(1)).

The nonconstant Fourier coefficients of Dbar are alpha d_hat(k/X). Its zero coefficient is zero, rather than 2alpha. The coefficients of |mu|²/n are

  alpha v_hat(k/X)+O(alpha/X)

uniformly on |k|≤X, by the Riemann sum for the autocorrelation of the one-sided triangular coefficient profile. They vanish outside that range. The zero coefficient of tbar additionally has −1.

A constant-coefficient cubic integral is a double sum over k,l with k+l+r=0. For these compactly supported piecewise-polynomial profiles, the Riemann sum gives

  integral Dbar³ / (n³/X) →J_11,
  integral Dbar² tbar / (n³/X) →J_12,
  integral Dbar tbar² / (n³/X) →J_22.

Here the main double sums have scale alpha³X²=n³/X. Uniform coefficient discretization errors are relatively O(1/X). Corrections from the exceptional constant coefficient of tbar involve only quadratic integrals of scale O(n²/X+1), which is o(n³/X). The missing zero coefficient of Dbar, a correction of −2alpha, contributes O(alpha³ X), again relatively O(1/X), plus smaller terms involving the constant correction in tbar. This coefficient-space argument avoids any unproved interchange of periodic tails with real-line integrals.

Useful bounds for the stochastic comparison are

  ||Dbar||_1+||tbar||_1=O(1),
  ||Dbar||_2²+||tbar||_2²=O(n²/X+1)=O(n^(2/3)).

For example Dbar=2alpha(F_X−1), so its L1 norm is at most 4alpha. Also integral |mu|²=O(n²/X), ||mu||_infinity=O(n), and hence integral |mu|⁴=O(n⁴/X), giving the tbar bounds.

## 3. Stochastic errors: uniform concentration suffices

Let Z=F_A−mu. Scalar Bernstein concentration on an O(X)-point trigonometric grid, followed by the Bernstein derivative inequality to control the gaps, gives

  ||Z||_infinity=O_p(sqrt(n log X)).

For completeness: each grid evaluation is a sum of independent centered bounded complex variables with total variance O(n). Apply Bernstein separately to real and imaginary parts, union-bound over C X grid points, and choose C large enough that the trigonometric derivative estimate bounds the continuum supremum by twice the grid supremum. Since X is polynomial in n, the resulting logarithm is O(log n). The same estimate at zero gives m=n+O_p(sqrt(n log n)), so m/n→1.

On m~n, expanding |mu+Z|²/m shows

  ||D−Dbar||_infinity+||t−tbar||_infinity
    =O_p(sqrt(n log n)).

The normalization change m versus n contributes at most O_p(sqrt(n log n)) because ||mu||_infinity=O(n). The quadratic noise term contributes O_p(log n), which is smaller.

Put E=O_p(sqrt(n log n)). Expand any of D³,D²t,Dt² around its barred counterpart. A term with one error is bounded in integral by E times the product of two deterministic L2 norms; a term with two errors by E² times a deterministic L1 norm; a term with three errors by E³. Hence every cubic-moment error is

  O_p(n^(7/6)sqrt(log n) + n log n + n^(3/2)(log n)^(3/2))
    = o_p(n^(5/3)) = o_p(n³/X).

Consequently the lower multiplication block satisfies

  H_lower/(n³/X) → J in probability.

This proves the needed stochastic moment limits without a high-degree collision-count variance lemma.

## 4. Center couplings and the L2 Gram

The basis elements D and t both have mean zero. The multiplication and Gram matrices are

  H = [[0,2m,integral Dt],
       [2m,integral D³,integral D²t],
       [integral Dt,integral D²t,integral Dt²]],
  G = diag(1,G_lower),
  G_lower=[[2m,integral Dt],[integral Dt,integral t²]].

The exact positive-integer counting identity

  integral Dt=(integral D³)/(3m)

therefore implies the center-coupling vector

  a=(2m,integral Dt)=(2n(1+o_p(1)),O_p(n²/X))=(2n(1+o_p(1)),o_p(n)).

To bound G_lower, Parseval gives ||Z||_2²=O_p(n), and the preceding supremum estimate yields integral |Z|⁴=O_p(n² log n). Thus

  integral |F_A|⁴ ≤8 integral |mu|⁴+8 integral |Z|⁴
                   =O_p(n⁴/X+n²log n),
  integral t²=O_p(n²/X+log n).

Together with integral D²=2m, this gives ||G_lower||=O_p(n). Cauchy–Schwarz controls its off-diagonal entry as well. The matrices are positive definite on the stated span with probability tending to one; for example an eventual positive definite H_lower also rules out a linear dependence between D and t.

## 5. Schur-complement asymptotic

Since J>0, H_lower is positive definite with probability tending to one. The full H has precisely one negative eigenvalue by its Schur complement. The generalized negative eigenvalue −K_3 is the unique positive solution of

  K_3=a^T(H_lower+K_3 G_lower)^(−1)a.

Initially this gives K_3≤a^T H_lower^(−1)a=O_p(X/n)=O_p(n^(1/3)). Therefore

  ||K_3 G_lower||=O_p(n^(4/3))=o_p(n³/X),

so the added Gram term is negligible in the inverse. It follows that

  K_3=(4+o_p(1))(X/n)(J^(−1))_11.

Exact inversion gives 4(J^(−1))_11=21630/241. This proves the theorem.

The normalized smaller eigenvalue of J is small (about 0.01); consequently the positive deterministic residual becomes dominant only very late. A large finite crossover is an expected feature of this proof, not contradictory numerical evidence.

## 6. Actual finite tests through 100,000

The script samples two independent realizations at each target using seeds 650200+target+replicate. It computes the entire 3D Gram by one FFT and exact trigonometric quadrature on a grid longer than 3X, sufficient for all cubic products; no full W2 eigensolver is run. Floating generalized eigensolves are numerical, not interval-certified.

| target | realized m, replicate 0 / 1 | K_3, replicate 0 / 1 | K_3/sqrt(2m), replicate 0 / 1 | K_3/m^(1/3), replicate 0 / 1 |
|---:|---|---|---|---|
| 1000 | 972 / 991 | 40.6683 / 42.1116 | 0.92238 / 0.94591 | 4.10551 / 4.22387 |
| 4000 | 4091 / 3987 | 83.9325 / 84.1539 | 0.92790 / 0.94240 | 5.24792 / 5.30712 |
| 16000 | 16159 / 16223 | 168.6995 / 168.8489 | 0.93841 / 0.93738 | 6.67281 / 6.66993 |
| 64000 | 64203 / 64388 | 335.2471 / 336.2204 | 0.93556 / 0.93693 | 8.37234 / 8.38859 |
| 100000 | 100299 / 99696 | 418.2695 / 416.6739 | 0.93388 / 0.93313 | 9.00238 / 8.98608 |

These finite ratios remain healthy-looking and are far from the asymptotic coefficient 89.751. The normalized multiplication-block eigenvalues at target100000 are approximately (0.00931,5.6897) and (0.00939,5.5875), consistent with a small positive limiting eigenvalue. This is numerical corroboration of the shape geometry, NOT numerical evidence that the square-root ratio has already begun visibly collapsing.

## Files and scope

- order_profile_asymptotic.py
- order_profile_asymptotic_results.json
- order_profile_asymptotic.log

The theorem falsifies a fixed three-dimensional profile certificate despite its universal support admissibility and apparently favorable finite fits. It does not falsify adaptive Fejér profiling: the latter matches the deterministic two-sided triangular mean, whereas |F_A|²/m has the distinct one-sided-autocorrelation shape v. It does not falsify full W2 or any universal Chowla bound.

Independent audit: the written proof, rational shape integrals, coefficient Riemann limits, stochastic error estimates, Gram bound, and Schur step were independently checked on 2026-10-20. No mathematical correction was required; the negligible zero-coefficient correction of Dbar was made more explicit. The probability-one-in-the-limit statement also implies existence of a deterministic sequence of Boolean supports defeating the square-root bound for this fixed 3D span. It does not provide an explicit small finite instance already in the late asymptotic regime.
