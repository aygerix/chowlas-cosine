# Addendum: a fixed profile can look successful before failing asymptotically

**20 October 2026. Supplement to the unchanged research checkpoint, version 0.**

A further targeted calculation resolves one specific question left open by the deterministic profile table. The universally admissible positive-half autocorrelation profile does **not** give a universal square-root certificate, even when the full three-dimensional trial space is optimized. This is a restricted failure, not a counterexample to Chowla or to full W2.

## Exact result

Independently retain each positive integer a<X with probability 2α(1-a/X), where α=n^(-1/3) and X=round(n/α). Write m=|A|, F_A=Σ_{a∈A}e(ax), D=F_A+conjugate(F_A), and t=|F_A|²/m-1. Let K_3 be minus the smallest generalized eigenvalue of multiplication by D on span{1,D,t}, using its actual L2 Gram matrix.

The proved asymptotic is

    K_3 = (21630/241 + o_p(1)) n^(1/3),
    K_3/sqrt(m) → 0 in probability.

It also rules out a square-root guarantee for the smaller scalar-positive-profile subfamilies inside that span. The profile is supported in A-A, hence available in W2; lack of admissible rows is not its problem.

The obstruction is a mismatch between two deterministic spike shapes. The triangular mean of D and the one-sided autocorrelation shape of t are linearly independent in the relevant weighted quadratic form. Their exact limiting multiplication matrix is

    J = [[22/5, 736/315], [736/315, 2369/1890]],
    det J = 5543/99225 > 0.

Uniform Bernstein concentration makes the random cubic errors lower order. A Schur-complement calculation then gives K_3~4(J^(-1))_11 X/n, producing the displayed constant. Thus optimizing coefficients within this fixed space cannot cancel the residual positive spike sufficiently well.

## Why the finite table was not misleadingly reinterpreted

At sample sizes through m≈100,000, the measured K_3/sqrt(2m) remains about 0.93. Those data do **not** visibly show collapse. The asymptotic coefficient 21630/241≈89.751 is large and the smallest eigenvalue of J is small, so the crossover can be very late. The theorem comes from the asymptotic proof, not an extrapolation of the finite ratios.

Adaptive Fejér profiling is not refuted: it can match the two-sided triangular mean rather than being forced to use this autocorrelation shape. Nor is the independently audited product-Fejér/full-W2 theorem affected.

## Two other archived refinements

The positive-definite rounding lemma now permits central mass p_0=h. Its spectral conclusion is K_U≥h+sqrt(v)/6 with failure probability at most 12h/sqrt(v)+728/v; a W2 conclusion additionally requires candidate-support filling. Six-wise independence suffices for the spectral moments, while the stated exponential filling estimate still requires full independence.

For a single nonnegative spectral factor with Boolean autocorrelations, an exact endpoint-energy inequality gives finite bounds when interior energy E<1. A central-binomial construction shows why arbitrarily many outer-lag equations alone cannot extend this to a general support-energy theorem: it satisfies those outer equations with only logarithmic energy, but other correlations are fractional. It is therefore a countercontrol to an endpoint-only argument, not a valid Boolean counterexample.

The universal coefficient-geometry gap remains open. The delivered main checkpoint is preserved as version 0; this addendum records subsequent findings separately.

References: [full order-profile theorem](cstar_order_profile_asymptotic_2026-10-20.md), [independent audit](cstar_order_profile_asymptotic_independent_audit_2026-10-20.md), [variable-central-mass lemma, §7.1](cstar_product_fejer_asymptotic_2026-10-20.md), [positive-factor endpoint results](cstar_positive_factor_energy_2026-10-20.md). The order-profile proof and exact constants passed independent audit; the symbolic integral check was also rerun during archiving.
