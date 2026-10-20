# Deterministic positive-profile residual certificates: actual tests

Checkpoint: 2026-10-20T06:03:31.354729+00:00. Ongoing research; no universal Chowla/C* or W2 constant is established. [Reproduction index](../experiments/cstar_structural_2026-10-20/README.md).

2026-10-20.  These are floating numerical tests of valid Rayleigh-quotient certificates, not interval-certified values and not a universal theorem.

## 1. Identity and local support

Let D=sum_{s∈S}e(sx), S=±A, N=|S|=2n. Let P≥0 be a trigonometric polynomial, p0=integral P, t=P−p0, w=D−t, V=integral w²>0, and q=1−w/sqrt(V). Then integral q²=2 and direct expansion gives

  K≥p0+sqrt(V)−[integral Pq²]/2−[integral w³]/(2V).

This is EXACTLY the Rayleigh quotient −integral Dq²/2, not an independent probabilistic assumption. If support(w)⊂W2={0}∪S∪(S+S), the bound is a local W2 certificate.

The optimized two-dimensional span {1,w/sqrt(V)} gives the stronger bound

  K≥[sqrt(b²+4a²)−b]/2,
  a=integral Dw/sqrt(V), b=integral Dw²/V.

The implementation independently checked the fixed-q identity against direct integration on a small example. All following P and cubic diagnostic terms are evaluated at the best TWO-dimensional profile parameters, even though these terms describe the fixed-q decomposition.

## 2. Profiles and optimization actually performed

Single Fejér profile: P=alpha F_L, alpha≥0, F_L normalized with coefficients 1−|j|/L for |j|<L. Only L satisfying [−L+1,L−1]⊂W2 were admitted. Every admissible L was examined for the n20/n50, interval, and root controls. For the much larger E99c controls, L was sampled on a combined logarithmic/linear grid, approximately 180 candidates, including the ambient support endpoint. Alpha was optimized by a logarithmic search followed by bounded scalar minimizations; the unrestricted three-dimensional Ritz value on span{1,D,F_L−1} agreed with the attained constrained two-dimensional optimum for the reported cases. Thus there is no missed mixing-coefficient issue in those cases.

Order-specific profile: P0=|sum_{a∈A}e(ax)|²/n, with constant coefficient 1 and support in A−A⊂W2, then P=alpha P0. Both alpha≥0/two-dimensional optimization and the full span{1,D,P0−1} were computed. They agree to floating precision in these samples.

A useful exact structural check for this profile is

  integral D(P0−1) = (integral D³)/(3n).

Indeed if T counts ordered positive solutions a+b=c in A, the left side is 2T/n and integral D³=6T. The higher profile moments are not determined by D's scalar cubic alone.

## 3. Results

Conventions: n=|A|; K is for D=2sum_A cos, not the cosine minimum M=K/2. `P obstruction` means (integral Pq²/2)/sqrt(V); `cubic obstruction` means (integral w³/(2V))/sqrt(V). Negative cubic obstruction is helpful.

| Support | n | Full W2 K | Best single-Fejér 2D | L | alpha | P obstruction | cubic obstruction | Order-profile 2D / 3D |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| dense X30_s0 | 20 | 4.813847 | 3.380234 | 36 | 1.067869 | 0.078223 | 0.109009 | 2.313059 |
| N50_x72 | 50 | 7.111342 | 4.684989 | 86 | 1.121399 | 0.069892 | 0.142188 | 2.816416 |
| N50_x71, sharp-W2 counterexample | 50 | 7.056994 | 4.800326 | 87 | 1.105551 | 0.057358 | 0.146226 | 2.963297 |
| interval [1,20] | 20 | 8.100811 | 4.959851 | 31 | 1.310770 | 0.329244 | −0.772700 | 2.608186 |
| interval [1,50] | 50 | 18.462876 | 10.041189 | 77 | 1.320634 | 0.414619 | −1.388895 | 4.312445 |
| E99c target1000, exponent 1/2 | 1025 | 164.639407 | 44.323492 | 30257 | 0.066165 | 0.000232 | −0.000736 | 45.573948 |
| E99c target1000, exponent 1/3 | 1056 | 160.120864 | 43.481086 | 10381 | 0.199914 | 0.000481 | −0.014713 | 43.087793 |
| E99c target1000, exponent 1/4 | 1026 | 136.808908 | 40.339512 | 5554 | 0.361732 | 0.000558 | −0.018530 | 38.802795 |
| root differences, r=7, base5, gcd normalized | 21 | 4.543831 | 3.185891 | 3 | 0.173184 | 0.026539 | 0.770048 | 3.952688 |

The dense near-extremizers DO admit a Fejér profile with a controlled deterministic residual cubic: the cubic obstruction is approximately 0.11–0.15 times sqrt(V), not an uncontrolled skewness catastrophe. This provides a real square-root-scale certificate on these examples, though it leaves a substantial gap to W2. For N50_x71 the fixed-q bound at the optimized two-dimensional fit is 4.732594, compared with the two-dimensional 4.800326 and full W2 7.056994.

For E99c the two normalized obstruction terms are tiny, as the independent-noise picture predicts. These profile certificates capture about sqrt(N), while full W2 detects the substantially stronger extreme negative excursions present in those particular samples. These are the same seeded target1000 support realizations as the repository E99c control, generated with RNG seed 20261021 and exponents in the original order.

The order profile is uniformly admissible but is not competitive on the dense near-extremizers. It improves the base5 root-difference control, where a very short available Fejér profile leaves cubic obstruction 0.77. For intervals, the order profile is precisely F_n, whereas the better Fejér profile has L about 1.54n; its weakness there has a concrete profile-width explanation.

## 4. Two nonnegative Fejér packets

As a genuinely tested extension, searched all pairs of admissible lengths on the three dense near-extremizers. For each pair, solve the full four-dimensional generalized eigenproblem on {1,D,F_L1−1,F_L2−1}. Accept an eigenvector only when its profile representation has both nonnegative amplitudes, making it a valid P=alpha1 F_L1+alpha2 F_L2. Reported bounds are attained and valid; this procedure does not claim to exhaust every constrained boundary possibility.

| Support | two-packet bound | lengths | amplitudes | single-packet bound |
|---|---:|---|---|---:|
| dense n20 | 3.394903 | 2,36 | 0.480490,1.051688 | 3.380234 |
| N50_x72 | 4.750571 | 26,95 | 0.483757,0.892273 | 4.684989 |
| N50_x71 | 4.841885 | 9,91 | 0.492260,1.018696 | 4.800326 |

The small improvement suggests that adding a second centered Fejér scale does not explain the remaining W2 gap on these examples. This is finite evidence only, not a profile no-go theorem.

## 5. Reproducibility and numerical scope

Files in [the experiment directory](../experiments/cstar_structural_2026-10-20/README.md):
- profile_certificate.py: formulas, profile fitting, W2 eigensolver, main datasets.
- profile_certificate_results.json and profile_certificate.log: all main results, moments-derived diagnostics, optimization parameters, W2 solver residuals.
- profile_two_fejer.py, profile_two_fejer_results.json, profile_two_fejer.log: actual two-packet search.
- profile_root_difference_results.json and profile_root_difference.log: root control, A={(5^i−5^j)/4: 0≤j<i≤6}.

Repository input sources are examples/dense_runs/X30_s0.json, examples/construct/N50_certified.json, and the E99c generation specified above. The script's X is the actual maximum of the sampled A, not the nominal taper endpoint; the Fejér length is still freely optimized within W2's contained interval.

Small W2 matrices were diagonalized densely. Large E99c W2 matrices were represented by masked FFT convolution; numerical eigenpair residual norms were 5.4e−6, 2.9e−5, 1.6e−5 respectively. These are numerical least-eigenvalue computations, not rigorous interval certifications of optimal W2 K. Profile Rayleigh formulas have the correct support and give mathematical certificates when their numerical evaluations are replaced by rigorous arithmetic; that replacement has not been performed here.

## Conclusion

Actual selected Boolean near-extremizers can have controlled cubic residuals against a simple nonnegative profile; independence is not necessary for this finite phenomenon. The universally supported positive-half autocorrelation profile is useful on the root control but much weaker on dense examples. No tested profile yields a universal estimate, and no claim has been made that its obstruction terms remain controlled for arbitrary Boolean supports.

Additional root check: repeating the root experiment with A={(7^i−7^j)/6: 0≤j<i≤6} reproduces the displayed W2, single-Fejér, and order-profile values to the shown precision. This base7 version avoids short carry relations in the moment and W2 computations. Its separate files are profile_root_difference_base7_results.json and profile_root_difference_base7.log. The main table retains the original base5 labeling; the numerical conclusion does not depend on that choice.
