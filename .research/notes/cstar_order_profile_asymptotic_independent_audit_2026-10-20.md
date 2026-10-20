# Independent audit of the order-profile asymptotic obstruction

Checkpoint: 2026-10-20T06:12:18.377072+00:00. Ongoing research; no universal Chowla/C* or W2 constant is established. [Reproduction index](../experiments/cstar_structural_2026-10-20/README.md).

Audited [the order-profile asymptotic proof](cstar_order_profile_asymptotic_2026-10-20.md). Verdict: the stated restricted three-dimensional theorem is correct. No substantive gap was found. This does NOT refute full W2, adaptive profiling, or Chowla.

## Independently reproduced exact constants

Using compact Fourier profiles d_hat(s)=2(1-|s|) and v_hat(s)=(2/3)(1-|s|)^2(2+|s|), independently evaluated the convolution integrals by splitting the (s,t) plane into its six sign/order triangles. Exact symbolic arithmetic gives

J=[[22/5,736/315],[736/315,2369/1890]],
det J=5543/99225,
4(J^{-1})_11=21630/241.

The degree-seven polynomial for v_hat*v_hat, integral d v=22/15, and integral v²=88/105 also agree exactly. The audit script uses a different triangular-domain decomposition for J rather than simply entering the claimed answers into numerical integration.

## Periodic-to-continuum audit

The deterministic Dbar coefficients agree with alpha d_hat(k/X) away from k=0. The autocorrelation coefficients of |mu|²/n agree uniformly with alpha v_hat(k/X) up to O(alpha/X), because the coefficient sequences are bounded piecewise polynomials and alpha X/n=1+O(1/X). Compact coefficient support means each cubic integral is a two-dimensional Riemann sum, with scale alpha³X²~n³/X. No uncontrolled physical-space tail interchange is involved.

The exceptional constant term of tbar contributes lower-degree integrals O(n²/X+1), negligible against n³/X. The missing Dbar zero coefficient is -2alpha; its correction is O(alpha³X), relative O(1/X), also negligible. I suggested explicitly naming this latter correction in the proof; it does not change the result.

An independent alternative check uses Abel summation to bound |mu(y/X)|/n by C/(1+|y|) on |y|<=X/2, followed by dominated convergence for the cubic profiles after removing the constant terms. This gives the same limit, but is not needed for the author's compact-coefficient proof.

## Stochastic bounds audit

- The uniform bound uses variance-sensitive Bernstein with total variance O(n), not Hoeffding with X summands. An O(X) grid and the trigonometric Bernstein derivative inequality give ||Z||infinity=O_p(sqrt(n log X)). This grid step is valid for the complex polynomial, and no independent grid values are assumed.
- The same bound at0 yields m=n+O_p(sqrt(n log n)); deterministic E m-n is only O(alpha). Therefore m~n and normalization of |F_A|²/m causes an error of the claimed order.
- Both D-Dbar and t-tbar have sup norm O_p(sqrt(n log n)). The |Z|²/m term is only O_p(log n).
- Deterministic L1 norms are O(1), squared L2 norms O(n²/X+1). Expanding cubic products consequently gives errors O_p(n^(7/6)sqrt(log n)+n log n+n^(3/2)(log n)^(3/2)), all o_p(n^(5/3)). This establishes the entire lower multiplication-block convergence, not just its diagonal.
- Parseval gives ||Z||2²=O_p(n), hence integral |Z|⁴=O_p(n² log n). Thus integral t²=O_p(n²/X+log n), and the full lower L2 Gram has norm O_p(n). This is stronger than the coarse O_p(n log n) estimate and is justified.

## Center and Schur audit

Both lower basis functions have exact mean0. The exact identity integral Dt=(integral D³)/(3m) gives the coupling vector (2n(1+o_p(1)),O_p(n²/X))=(2n(1+o_p(1)),o_p(n)). It correctly uses realized m, not target n, before taking the limit.

Since J is positive definite, the lower multiplication block is positive definite with probability tending to1. This also establishes linear independence of D,t in L2 on that event. The full multiplication matrix has precisely one negative eigenvalue by inertia, and the generalized negative eigenvalue satisfies

K=a^T(H_lower+K G_lower)^{-1}a.

Monotonicity first bounds K by O_p(X/n), after which K G_lower=O_p(n^(4/3))=o_p(n^(5/3)). Substitution into the inverse yields exactly

K=(21630/241+o_p(1))n^(1/3).

No circular use of the desired asymptotic occurs.

## Numerical scope

The FFT length exceeding3X is sufficient for every cubic product of D and t. The displayed finite samples through target100000 do NOT show a collapsing square-root ratio, and the note explicitly says so. The constant about89.75 and small minimum eigenvalue of J explain a potentially enormous crossover. The analytic asymptotic, rather than an extrapolation from those samples, is what refutes the restricted universal certificate.

Reproduction: [exact symbolic audit](../experiments/cstar_structural_2026-10-20/audit_order_profile_asymptotic.py).
