# Chowla research handoff

## Experimental results and assessment for independent review

**Historical report dated 20 October 2026. Recovered from PDF on 20 October 2026 (UTC).**

Source: `chowla-research-handoff.pdf`, 10 pages, SHA-256 `3597a4312aae50c55e0ebf5d41c0816951353953a298e3253e24605489e0f3a7`.

This is a readable PDF-derived reconstruction, not recovered original Markdown. Prose is reflowed and mathematical notation normalized; source page boundaries are identified below. Charts are omitted rather than recreated without their data. See the [page-delimited extraction](research_handoff_2026-10-20.pdftotext.txt) and [provenance/status README](README.md). The later notes linked there supersede this report as overall project status; specific historical arguments retain only their stated scope. No original proof or experiment numbering has been updated.

## Source page 1: scope and normalizations

**Bottom line.** None of this work proves or advances the universal bound M_A ≥ c sqrt(|A|) for any absolute c > 0. The useful output is the elimination, by explicit calculations, of several stated shortcuts. These failures should not be relabeled as new gap conjectures. The missing ingredient remains a quantitative use of the exact simultaneous Boolean frequency arrangement.

### What is established and what is not

The report consolidates full negative-sublevel experiments, a conditional Boolean augmentation theorem with an advisor-attributed L1 strengthening, fractional Fejér padding, growing-order cyclotomic and determinant tests, and a high-rank Boolean boundary-Schur counterexample. The analytical arguments are paper proofs, not Lean or kernel-checked results; novelty and external priority have not been verified. The numerical evidence is floating point, not a rigorous certificate.

### Common normalization

    f_A(x) = sum_{a in A} cos(2πax),
    M_A = -min f_A,
    R_A = M_A/sqrt(|A|),
    H_A(t) = meas{x in R/Z : f_A(x) <= -t M_A},  0 <= t <= 1.

A is a nonempty finite set of positive integers; measure is normalized Haar measure. Boolean means each positive cosine coefficient is 0 or 1. For weighted f = sum c_k cos(2πkx), use E = sum c_k² and R = M/sqrt(E), so integral f² = E/2. The earlier E125 statistic is N(s) = H(1-s). At t = 1 the level set has measure zero for a nonconstant trigonometric polynomial.

### Relation to the symmetric formulation C star

For S = A union (-A), put

    D(z) = sum_{s in S} z^s,
    N = |S| = 2|A|.

On the circle D = 2f_A. Thus the true cost -min D = 2M_A. Nonnegativity of P = K+D, with integer K = ceil(2M_A), motivates the equivalent square-root-scale target N ≤ C K². Ceiling changes constants, not the asymptotic issue. No sharp constant is sought.

### Numerical design

Four original E125-type weighted packets use X = 1,024, 4,096, 16,384, 65,536; α = 0.9; J = round(X^α); seed X; independent uniform packet centers; and the E82 optimized autocorrelation profile. Controls include four full Singer-Bu sets and sixteen other Boolean examples. Frequencies and amplitudes were not rescaled to manufacture a match. Packet coefficients may be negative or exceed 1; they are not the bounded fractional objects of source page 6.

Explicit packet coefficients are

    c_k = φ(w(k/X)²) + 4c w(k/X) sum_j cos(kθ_j),
    φ(v) = (1-sqrt(1-v))/2,
    c = 1/sqrt(32J).

The profile w is the linearly interpolated normalized autocorrelation of the E82 N = 320 optimizer. Numerical curves use these signed coefficients, not coefficient mass as the energy denominator.

## Source page 2: full packet and Singer-Bu profiles

**Recovery note:** the source page contains plots, which are not reproduced in this text-only reconstruction. Their underlying full threshold arrays cannot be recovered from the text. The captions and interpretation follow.

All computed thresholds are retained and connected, including the whole interval rather than only near-floor points. Zero values at t = 1 are omitted from the log panel. Lines between thresholds are visual interpolation, not continuum bounds. Each profile uses its own polished estimate of the true minimum.

Near t = 0.99, the tested packets are hundreds of times above the four-Bu envelope; at moderate depths the profiles overlap or reverse. This is an observed family difference, not a necessary feature of arbitrary Boolean near-extremizers or hypothetical counterexamples.

## Source page 3: all twenty Boolean control profiles

**Recovery note:** the source page contains plots, which are not reproduced. The original text describes the controls as follows.

Each panel shows full-range curves for its stated family; the same dotted packet X = 65,536 is repeated as a visual reference. Counts: 4 full Bu, 5 thinned Bu, 5 small simulated-annealing (SA), 2 dense SA, 3 Bernoulli-packet, 1 random half-density. These are selected finite examples, not an exhaustive search or an optimality claim.

## Source page 4: numerical values and uncertainty

| Family and parameter | E | M/sqrt(E) | H(0.5) | H(0.9) | H(0.99) |
|---|---:|---:|---:|---:|---:|
| Packet X=1,024 | 115.1 | 0.7647 | 0.3101 | 0.1580 | 0.0216 |
| Packet X=4,096 | 484.2 | 0.6873 | 0.3593 | 0.2107 | 0.0239 |
| Packet X=16,384 | 1,922.8 | 0.6388 | 0.3949 | 0.2549 | 0.0363 |
| Packet X=65,536 | 7,638.3 | 0.5965 | 0.4251 | 0.2930 | 0.0433 |
| Bu q=61 | 3,782 | 0.6040 | 0.3621 | 0.0240 | 8.41e-05 |
| Bu q=101 | 10,302 | 0.5885 | 0.3704 | 0.0262 | 3.44e-05 |
| Bu q=151 | 22,952 | 0.5777 | 0.3801 | 0.0292 | 9.41e-06 |
| Bu q=199 | 39,800 | 0.5658 | 0.3825 | 0.0402 | 1.43e-05 |
| Small SA n=20 | 20 | 0.6011 | 0.3930 | 0.0729 | 0.0082 |
| Small SA n=36 | 36 | 0.5648 | 0.3735 | 0.0579 | 0.0061 |
| Small SA n=100 | 100 | 0.6650 | 0.2722 | 0.0288 | 0.0019 |

Against the envelope of the four full Bu curves, the first sampled threshold where each packet exceeds it is respectively 0.75, 0.61, 0.44, 0.30. The first sampled ratios ≥ 3 are 0.89, 0.87, 0.86, 0.85 and persist on the sampled grid through 0.9999. At t = 0.99 the ratios are approximately 256, 284, 432, 516. These are grid statements only. Small-SA controls show why that envelope is not a universal Boolean bound.

### Method and error interpretation

FFT grids locate extrema; numerical polishing estimates M. Cubic Hermite crossing integration is supplemented by direct root refinement near the floor and at all thresholds for small-SA controls. For Bu, polished-extremum checks correct hidden valleys and holes. Doubling the grids changes the packet curves by at most 4.6 × 10^(-6) and the four principal Bu curves by at most 1.6 × 10^(-7) in absolute H.

These are observed refinement differences, not rigorous error bars. Floating-point agreement neither certifies the global minimum nor proves every narrow sublevel component was found. Relative errors can be larger when H is tiny. H(1) = 0 is imposed from the mathematical level-set fact, not a grid count. The exact arguments below do not depend on these numerical minima.

## Source page 5: exact Boolean augmentation proof

### Finite statement

Given nonempty B ⊂ N, integer L ≥ 1 and integer q > max B, set

    C = B union q{1,...,L},
    g_L(y) = sum_{k=1}^L cos(2πky),
    m_L = -min g_L.

Then C is Boolean, |C| = |B|+L, and

    2L/(3π) <= m_L <= M_C <= m_L + M_B <= L + M_B.

Disjointness and the upper bound are immediate. Choose a minimizer y of g_L. For every a ∈ B, q does not divide a, so the average of exp(2πia(j+y)/q) over j = 0,...,q-1 is zero. At least one grid point x = (j+y)/q has f_B(x) ≤ 0 while g_L(qx) = -m_L. Hence M_C ≥ m_L, with no limiting equidistribution assumption.

    2g_L(y)+1 = sin((2L+1)πy)/sin(πy).

At y = 3/(4L+2), the numerator is -1. Using sin u ≤ u gives

    m_L >= [1+csc(3π/(4L+2))]/2 >= 2L/(3π).

Also m_L ≤ L.

If f_C(x) ≤ -t M_C, then g_L(qx) ≤ -t m_L + M_B. Set a = t m_L - M_B and assume 2a-1 > 0. The identity forces |sin(πqx)| ≤ 1/(2a-1). For d = dist(qx,Z), sin(πd) ≥ 2d. The allowed arcs have measure at most 1/(2a-1); integer dilation preserves Haar measure. Therefore

    H_C(t) <= 1/[2(t m_L - M_B)-1].

When the bound exceeds 1 it is merely trivial. This is an exact finite statement, not an estimate inferred from the plots.

### Conditional closure for every hypothetical counterexample sequence

Suppose n_j = |B_j| → ∞ and M_j = o(sqrt(n_j)). Choose integers L_j with max(M_j,1) = o(L_j) and L_j = o(sqrt(n_j)); rounding sqrt(max(M_j,1) sqrt(n_j)) suffices. Choose any q_j > max B_j. Then

    R_{C_j} <= (L_j+M_j)/sqrt(n_j+L_j) -> 0,
    sup_{δ <= t <= 1} H_{C_j}(t)
        <= [2δ L_j/(3π)-1]^(-1) -> 0 for every δ > 0.

The second estimate holds eventually because M_j ≤ δ L_j/(3π). The added o(sqrt(n)) frequencies have negligible coefficient energy yet control the normalization. This does not construct an actual counterexample. It proves that, if any exist, some have vanishing negative mass at every fixed positive depth.

## Source page 6: vanishing bulk and fractional profile instability

### Advisor-attributed L1 strengthening

**Attribution retained from the source:** the advisor proposed this strengthening in material shared by the user. This recovery verifies that the attribution and argument are present in the PDF; it does not independently identify the advisor or establish priority.

Put u_j = f_{C_j}/M_{C_j}. Mean zero and f_B ≥ -M_B imply

    ||f_B||_1 = 2 integral (f_B)_- <= 2M_B.

For D_L = 2g_L+1, N = 2L+1 and d = dist(y,Z),

    |D_L(y)| <= min(N, 1/(2d)),
    ||D_L||_1 <= 2 integral_0^{1/2} min(N,1/(2d)) dd
              = 1 + log N.

The integral splits at d = 1/(2N). Thus

    ||g_L||_1 <= 1 + (1/2)log(2L+1).

Measure preservation and source page 5 give

    ||u_j||_1 <= (3π/(2L_j))[2M_j+1+(1/2)log(2L_j+1)] -> 0,
    ||u_j||_2² = (n_j+L_j)/(2M_{C_j}²) -> infinity.

Since 0 ≤ (u_j)_- ≤ 1, its squared L2 norm tends to zero. For fixed η > 0, E_j = {u_j > η} has measure ≤ ||u_j||_1/η → 0, while

    integral_{(R/Z) minus E_j} (u_j)_+² <= η ||u_j||_1 -> 0.

The divergent positive energy lies in rare excursions. Equivalently 1+u_j → 1 in L1 but its squared L2 norm diverges.

### Every fixed Boolean H profile has a bounded fractional approximation

Fix A, f, M > 0 and q > max A. Set

    K_N(x) = (1/N) |sum_{k=0}^{N-1} exp(2πikx)|²,
    F = f + ε(K_N(qx)-1),  0 < ε <= 1/2.

The disjoint added coefficients 2ε(1-k/N) lie in [0,1], and

    E(F) = |A| + 4ε² (N-1)(2N-1)/(6N).

K_N ≥ 0 and integral K_N = 1 give F ≥ f-ε and ||F-f||_1 ≤ 2ε. For U = {f < -M+δ} of measure v > 0, some x ∈ U has K_N(qx) ≤ 1/v. Hence

    M-δ-ε/v <= M_F <= M+ε,

so M_F → M uniformly in N. Choose ε → 0 and Nε² → ∞. Then M_F/sqrt(E(F)) → 0 and F/M_F → f/M in L1.

Every level set of nonconstant f is finite; its CDF is continuous. Convergence in probability therefore gives uniform CDF convergence, hence

    sup_{0 <= t <= 1} |H_F(t)-H_A(t)| -> 0.

Quantitatively, with

    D = ||F/M_F - f/M||_1,
    ω(h) = sup_s meas{|f/M-s| <= h},

threshold sandwiching gives

    sup |H_F-H_A| <= D/η + ω(η).

This is a stable-profile obstruction, not a Boolean counterexample or a match to P61's two coefficient profiles.

## Source page 7: packet asymptotics and growing cyclotomic norms

### Why the P61 flat-background limit is real but model-specific

For a fixed continuous compactly supported positive-definite kernel w with w(0) = 1, its inverse Fourier transform W is nonnegative and integrable with integral W = 1. Periodization gives

    S_X(x) = X sum_{m in Z} W(X(x+m)).

Let T(r) = integral_{|u|>r} W(u) du → 0. For 2J translated or reflected packets, remove the radius-r/X arcs about their centers. Their union has measure ≤ 4Jr/X and the average packet mass outside has integral ≤ T(r). Thus

    meas{(sum packets)/(2J) > η} <= 4Jr/X + T(r)/η.

If J → ∞ and J/X → 0, take r → ∞ with Jr/X → 0. Write

    B = sqrt(J/8),
    c = 1/sqrt(32J),
    E_X = P_X + c sum packets - B.

The smooth part has mean zero and P_X ≥ -1/4. Markov gives (P_X+1/4)/B → 0 in probability. Hence E_X/B → -1. Together with E_X ≥ -B-1/4 this gives M_X/B → 1 and H_X(t) → 1 for every fixed 0 < t < 1. For the triangular kernel T(r) = O(1/r); no such rate is assumed for general w.

### Prime norms with exact Boolean mean and variance

Let S = -S, 0 ∉ S, N = |S|, X = max S and

    P(z) = K + sum_{s in S} z^s >= 0 on the circle,

K an integer ceiling of the true cost. For prime q > 2X+1, set d = q-1. P(ζ_q) cannot vanish because z^X P has degree 2X < deg Φ_q. Its conjugates are positive, and its norm is a positive integer R_q ≥ 1.

    μ_q = K-N/d,
    V_q = qN(d-N)/d².

Indeed sum_{j=1}^{q-1} ζ_q^{js} = -1 for nonzero s; the zero sums in S+S are exactly N, so

    sum_{j=1}^{q-1} D(ζ_q^j)² = qN-N².

AM-GM yields only K ≥ 1+N/(q-1), a density bound at q comparable to X.

The sharp global quadratic majorant for 0 < t ≤ B and 0 < μ < B is

    log t <= log μ + (t-μ)/μ - c(μ,B)(t-μ)²,
    c(μ,B) = [B/μ - 1 - log(B/μ)]/(B-μ)².

It follows by monotonicity of (u-1-log u)/(u-1)², represented as

    integral_0^1 (1-s)/(1+s(u-1))² ds.

With B = K+N, the norm gives c(μ_q,B)V_q ≤ log μ_q. As q → ∞ this becomes

    N/K - log(1+N/K) <= N log K.

For every integer K ≥ 2 this is automatic for all N: its left side is ≤ N/K and log K ≥ 1/K. This specific norm-plus-variance inequality is vacuous for the target; it does not exclude optimizations using more conjugate data.

## Source page 8: integral controls and redundant determinant bounds

### One globally positive control at all coprime orders

    U_L(z) = 1+z+...+z^(L-1),
    P_L(z) = U_L(z)U_L(z^(-1))
           = L + sum_{0<|k|<L} (L-|k|)z^k.

This has nonnegative integer coefficients, constant K = L and extreme coefficients 1. Its off-zero Fourier energy is

    E_L = 2 sum_{r=1}^{L-1} r² = L(L-1)(2L-1)/3,
    E_L/K² ~ 2L/3 -> infinity.

The off-zero coefficient mass is instead L(L-1) asymptotic to K². Energy equals support size only in the Boolean case.

For every q > 1 coprime to L,

    U_L(ζ_q) = (1-ζ_q^L)/(1-ζ_q).

The automorphism ζ_q ↦ ζ_q^L permutes primitive conjugates, so Norm U_L = Norm P_L = 1. This saturates the integer-product bound at all coprime orders simultaneously, including every prime q > 2L. All evaluations come from one polynomial on Z: there is exact no-wrap compatibility, not separately chosen finite-group models. At noncoprime orders evaluations may vanish; any nonzero norm is still a positive integer.

**Scope.** This is not Boolean: interior coefficients exceed 1. It refutes integrality-only Fourier-energy bounds, not C star. A successful arithmetic argument must exploit the coefficient cap or an exact Boolean relation that rejects this control. Frobenius congruences alone hold for every integer polynomial and do not reject it.

### Every principal Toeplitz determinant is already at least one

More generally take any nonnegative real Laurent polynomial P with extreme coefficient 1, without integrality. Since z^X P is monic, Jensen's root formula gives integral log P ≥ 0. Circle zeros give integrable logarithmic singularities. For arbitrary distinct integer indices I = {i_1,...,i_m}, define

    G_I = (P-hat(i_a-i_b)).

Then

    det G_I >= exp(m integral log P) >= 1.

Proof: choose an outer Fejér-Riesz factor Q with P = |Q|² and |Q(0)|² = exp(integral log P). Shift and sort I so its indices are nonnegative. The coefficient vectors z^(i_a)Q have a triangular minor at rows i_1,...,i_m, with diagonal Q(0). Cauchy-Binet bounds the Gram determinant below by |Q(0)|^(2m). This holds for all principal index sets at growing order, not just contiguous sections.

Thus "the positive determinant is an integer, hence ≥ 1" adds nothing to positivity and the extreme coefficient 1. P_L satisfies all these lower bounds while its energy/K² diverges. Relations between actual determinant values, other arithmetic data and full coefficient recovery are not ruled out. Full conjugate values at q > 2X+1 encode the coefficients and can simply restate the original problem.

## Source page 9: a high-rank Boolean boundary-Schur test fails

For finite symmetric S ⊂ Z and an index set I, put

    B_I = (1_S(i-j)).

Suppose H = K I + B_I is PSD and P projects onto ker H. An exterior row x has

    b_x = (1_S(x-i))_{i in I}.

If the extended block is PSD at diagonal K+δ, compression to ker H and that row gives

    [[δI,       P b_x],
     [(P b_x)*, K+δ ]] >= 0,
    δ(K+δ) >= ||P b_x||_2².

The attempted Boolean step was

    max_{x not in I} ||P b_x||² >= c|S|

when |S|/K² is large and the kernel occupies almost all of I. This would force a square-root increment. The following exact torsion-free example refutes that step.

    d,m >= 2,  B = 8m,
    S = {±t B^j : 1 <= t <= m-1, 0 <= j < d},
    I = {sum_{j=0}^{d-1} u_j B^j : 0 <= u_j <= m-1}.

Then |S| = 2d(m-1), |I| = m^d. Base-B uniqueness identifies B_I with the adjacency of the Cartesian product of d complete graphs on m vertices. Hence H = d I + B_I is the sum of d tensor terms with J_m in one coordinate and identities elsewhere. H is PSD at K = d, with

    ker H = (1-perp)^(tensor d),
    dim ker H = (m-1)^d,
    P = (I_m-J_m/m)^(tensor d).

For any x outside I with a neighbor, write x = y+t B^j. Its digit vector lies in [-m+1,2m-2]^d. Two such representations must agree: their difference has digits of magnitude ≤ 3m and B = 8m makes this encoding injective. If neighbors occurred in two different coordinate directions, each representation would force the other altered coordinate into [0,m-1]. All coordinates would then be in that interval and x ∈ I, a contradiction. Thus every exterior row meets at most one coordinate fibre.

    ||P b_x||² <= ||b_x||² <= m,
    max_{x not in I} ||P b_x||²/|S| <= m/[2d(m-1)].

Take m = d². Then

    |S|/K² = 2(d²-1)/d -> infinity,
    dim ker H/|I| = (1-1/d²)^d -> 1,

but the leakage ratio tends to 0. More exactly, a fibre of length ℓ gives

    ||P b_x||² = (ℓ-ℓ²/m)(1-1/m)^(d-1).

At fixed d = 2, ℓ approximately m/2 succeeds at square-root scale; at growing rank it misses the factor d. Fixed-rank success is not universal progress.

## Source page 10: scope of the boundary failure and review agenda

### What passes and what does not

For any integer t ≥ 1 and any set J of t exterior integers, let C be the cross block. Every column has at most m ones, so ||C||_op ≤ sqrt(tm), and the exterior adjacency has norm ≤ t-1. Perturbing diag(H,d I_t) therefore shows that the Boolean block on I union J is PSD at

    K_t = d + sqrt(tm) + t-1.

This holds for every such J simultaneously. For m = d² and t = o(d), |S|/K_t² → ∞. Only subsets of this specified I plus at most t exterior rows are covered. Arbitrary row sets of comparable size and all contiguous Toeplitz sections are not claimed to pass.

This is not a Chowla counterexample: K = d is local. At x = 6/(B-1), B^j x ≡ x mod 1 and the full sum equals

    d[sin((2m-1)πx)/sin(πx)-1].

Its true cost is at least (4/(3π)+o(1))dm and is Θ(dm). For p = 2m-1 prime, the corresponding union of nonzero coordinate axes in F_p^d has Fourier minimum -d and size d(p-1); the integer support is its centered one-representative lift. The arbitrary-m integer calculation does not require p prime.

Even singularity alone gives no leakage: for S = {-1,1}, I = {1,...,L}, the PSD boundary K = 2cos(π/(L+1)) has maximum leakage

    2sin²(π/(L+1))/(L+1) ~ 2π²/L³.

For genuinely globally nonnegative nonzero P, every finite Gram block is strictly positive definite, since

    integral P |sum c_i z^i|² > 0

for nonzero coefficients. Exact kernels therefore describe local relaxations, not globally feasible densities.

### Assessment and questions for skeptical review

The universal fixed-depth floor-flatness route is closed in its stated necessary-condition form. Bounded distribution tests continuous at zero also collapse under the augmentation; unbounded moments, moving thresholds, positive-tail statistics and separately proved structural reductions remain outside that obstruction. Norm integrality, determinant lower bounds and a bounded-boundary-row test are insufficient in the exact senses proved here. None of this rules out all distributional, arithmetic or Toeplitz methods.

Check:

1. Every factor of two between cosine and symmetric Fourier energy.
2. The conditional quantifiers and minimum bounds in augmentation.
3. Uniform CDF convergence versus energy-sensitive statistics.
4. Jensen and arbitrary-index triangular-minor scope.
5. The base-8m uniqueness and the restricted family in K_t.

Any proposed replacement must reject the explicit controls and prove, not assume, the missing simultaneous Boolean constraint. No new universal aggregate inequality has been obtained.

### Provenance and reruns

The source reports local snapshot `446367d948fedba07c5e70e3fdf9d9fcd106b08b`, not pushed, and public base `dfd51a19d0b094850f451d1cc82c88880be77b17`. These are historical source locators. The public baseline was separately restored in the repository history; the local snapshot has not been recovered. Neither Git object is reconstructed from this PDF.

Source-note locators printed in the report:

- `negative_sublevels_2026-10-20.md` and its `_appendix.md`.
- `cstar_cyclotomic_determinants_2026-10-20.md`.
- `cstar_boolean_boundary_tests_2026-10-20.md`.

Data locators printed in the report:

- `packets/e125_final.jsonl`.
- `boolean/definitive_boolean_curves.json`.
- `comparison_summary.json` in the experiment bundle.

Repository cross-references printed in the report: P61(b), P65.3, E125, `src/e125_floor.py`, and `src/e83_escape_binarise.py`. The source explicitly calls these locators, not claims that local notes exist on the remote. It states that the PDF contains the arguments needed for proof review and that a reproducibility ZIP is optional for rerunning numerical work. **This recovery does not assert that every named early source, dataset, or commit was recovered.**
