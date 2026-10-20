# Negative sublevels and the Chowla floor test

**Historical report dated 20 October 2026. Recovered from PDF on 20 October 2026 (UTC).**

Source: `chowla-negative-sublevels.pdf`, 5 pages, SHA-256 `b9668b72b5b0b72f0171f32a98b1630de61c986fde33f537f271731eb5927ecf`.

This is a readable PDF-derived reconstruction, not recovered original Markdown. Prose is reflowed and mathematical notation normalized; source page boundaries are identified below. Charts are omitted rather than recreated without their data. See the [page-delimited extraction](negative_sublevels_report_2026-10-20.pdftotext.txt) and [provenance/status README](README.md). The later notes linked there supersede this report as overall project status; its specific conditional obstructions retain only their stated scope.

## Source page 1: main conclusion, definitions and finite augmentation

**Main conclusion.** The observed packet-versus-Boolean near-floor separation is real in the tested examples, but it is not a universal obstruction to hypothetical Chowla counterexamples. An exact Boolean augmentation can preserve a counterexample sequence while forcing every fixed-depth negative sublevel to have vanishing measure.

### Definitions and the question

For a nonempty finite set A of positive integers, use normalized Lebesgue measure on R/Z and define

    f_A(x) = sum_{a in A} cos(2πax),
    M_A = -min f_A,
    R_A = M_A/sqrt(|A|),
    H_A(t) = meas{x : f_A(x) <= -t M_A},  0 < t <= 1.

A hypothetical counterexample sequence means |A| → ∞ and R_A → 0. The question is whether the shape of H, normalized by the true deepest minimum, distinguishes all such Boolean sequences from the P61(b) weighted packets. E125 uses N(s) = H(1-s), so its N(0.01) is H(0.99).

### Exact finite Boolean augmentation lemma

Let B be any nonempty finite set, let L ≥ 1 be an integer, and choose an integer q > max B. Put

    C = B union {q, 2q, ..., Lq},
    g_L(y) = sum_{k=1}^L cos(2πky),
    m_L = -min g_L.

Then C is Boolean, |C| = |B| + L, and

    2L/(3π) <= m_L <= M_C <= m_L + M_B <= L + M_B.

Whenever 2(t m_L - M_B) - 1 > 0,

    H_C(t) <= 1/[2(t m_L - M_B) - 1].

### Proof of the floor bounds

Disjointness is immediate. The pointwise lower bound f_C = f_B + g_L(qx) ≥ -M_B - m_L gives the upper bound on M_C. If y is a minimizer of g_L, root-of-unity averaging gives, for each a ∈ B,

    (1/q) sum_{j=0}^{q-1} exp(2πia(j+y)/q) = 0.

Thus one of the q points x = (j+y)/q has f_B(x) ≤ 0, while g_L(qx) = -m_L. Hence M_C ≥ m_L. No equidistribution limit or special choice of q is needed.

## Source page 2: why the universal fixed-depth test fails

### Completion of the finite proof

The Dirichlet identity and the point y = 3/(4L+2) give

    2g_L(y) + 1 = sin((2L+1)πy)/sin(πy),
    m_L >= (1/2)[1 + csc(3π/(4L+2))] >= 2L/(3π).

If f_C(x) ≤ -t M_C, then g_L(qx) ≤ -t m_L + M_B. Set a = t m_L - M_B. When 2a-1 > 0, g_L(y) ≤ -a implies |sin(πy)| ≤ 1/(2a-1). Writing d = dist(y,Z), the bound sin(πd) ≥ 2d puts this set in arcs of total measure at most 1/(2a-1). The map x ↦ qx preserves measure. This proves the sublevel bound.

### Conditional closure theorem

Suppose B_j is a hypothetical counterexample sequence, with n_j = |B_j| and M_j = o(sqrt(n_j)). Choose integers L_j satisfying max(M_j,1) = o(L_j) and L_j = o(sqrt(n_j)), and choose any q_j > max B_j. The augmentation above satisfies

    R_{C_j} <= (L_j + M_j)/sqrt(n_j + L_j) -> 0.

For every fixed δ > 0, eventually M_j ≤ δ L_j/(3π), and monotonicity gives

    sup_{δ <= t <= 1} H_{C_j}(t)
        <= [2δ L_j/(3π) - 1]^(-1) -> 0.

The added L_j = o(sqrt(n_j)) frequencies are negligible in coefficient energy but dominate the minimum. A narrow negative trough therefore controls the normalization. If any counterexamples exist, there are counterexamples with vanishing fixed-depth H.

### Exact scope

This is not an actual counterexample, a proof of Chowla, or a novelty claim. It blocks the assertion that every arbitrary hypothetical counterexample must have H(t_0) ≥ c > 0 at some fixed depth t_0. The original background can move into the boundary layer t asymptotic to M_j/L_j → 0. Scale-dependent depths and joint Boolean coefficient-energy inequalities are not excluded. No such new inequality is established here.

### The packet limit is nevertheless genuine

For a fixed continuous compactly supported positive-definite kernel w with w(0) = 1, the P61(b) construction with J → ∞ and J/X → 0 obeys

    M_X/sqrt(J/8) -> 1,
    H_X(t) -> 1 for each fixed 0 < t < 1.

This is a model-specific asymptotic, not a characterization of every obstruction. At t = 1, H = 0 for each nonconstant trigonometric polynomial.

## Source page 3: full numerical curves across increasing sizes

**NUMERICAL.** The plots retain the whole negative-sublevel range, not only the near-floor samples. Each polynomial is normalized by its numerically polished minimum. No amplitude or frequency rescaling is applied.

**Recovery note:** the source page contains a two-panel figure. Its chart image and plotted threshold samples are not available in this text reconstruction. The following explanatory text is retained; no chart values are inferred from pixels.

Top: full curves on linear axes. Bottom: the same profiles on logarithmic vertical axes, revealing the near-floor gap. Values at t = 1 are exactly zero in the mathematical definition and are omitted from the log plot. Curves connect computed thresholds and do not represent a continuum error certificate.

The finite data establish a family separation, not a universal Boolean law. The packet sizes use E125's optimized kernel and original seeds, extended to the largest size shown; Singer-Bu data retain their original frequencies. The two families are ordered by their own natural size parameters rather than artificially matched degrees.

## Source page 4: numerical comparison and reliability

| Family and size | E | M/sqrt(E) | H(0.5) | H(0.9) | H(0.99) |
|---|---:|---:|---:|---:|---:|
| Packet X=1,024 | 115.1 | 0.7647 | 0.3101 | 0.1580 | 0.0216 |
| Packet X=4,096 | 484.2 | 0.6873 | 0.3593 | 0.2107 | 0.0239 |
| Packet X=16,384 | 1,922.8 | 0.6388 | 0.3949 | 0.2549 | 0.0363 |
| Packet X=65,536 | 7,638.3 | 0.5965 | 0.4251 | 0.2930 | 0.0433 |
| Bu q=61 (n=3,782) | 3,782 | 0.6040 | 0.3621 | 0.0240 | 8.41e-05 |
| Bu q=101 (n=10,302) | 10,302 | 0.5885 | 0.3704 | 0.0262 | 3.44e-05 |
| Bu q=151 (n=22,952) | 22,952 | 0.5777 | 0.3801 | 0.0292 | 9.41e-06 |
| Bu q=199 (n=39,800) | 39,800 | 0.5658 | 0.3825 | 0.0402 | 1.43e-05 |

The table uses coefficient-square energy E = sum c² for weighted packets and E = |A| for Boolean sets. Packet coefficients are not assumed to lie in [0,1]; this is distinct from the bounded fractional construction below.

FFT grids locate candidate extrema; numerical polishing estimates M, and threshold crossings are integrated using cubic Hermite interpolation, with direct root refinement in the near-floor tails. Doubling the grids changes the displayed packet curves by at most 4.6 × 10^(-6) and the four main Singer-Bu curves by at most 1.6 × 10^(-7) in absolute H. These are observed refinement differences, not rigorous error bars. Floating-point agreement does not certify the global minimum or prove that every narrow sublevel component has been found. Relative errors can be much larger when H is tiny; the endpoint t = 1 is imposed mathematically, not inferred from a grid count.

### How to read the evidence

At half depth, the E125 packet and Singer-Bu profiles are comparable; close to the floor, the gap is large. Neither a finite-size gap nor a fitted near-floor power law supplies the missing universal implication. In particular, the exact augmentation theorem does not depend on the numerical examples.

### Reproducibility and source scope

Source-reported repository baseline: commit `dfd51a19d0b094850f451d1cc82c88880be77b17`. Definitions and model comparison: `src/e125_floor.py` and `.research/EXPERIMENTS.md`, E125. Packet construction: `src/e83_escape_binarise.py` and `.research/PROOFS.md`, P61(b). The source states that numerical data, scripts and all threshold samples accompany it separately. This reconstruction does not assert that those separate early assets or baseline commits were recovered.

The exact arguments in this report are mathematical deductions; the curves and polished minima are floating-point evidence, not certified theorems.

## Source page 5: packet limit and profile caveat

### Packet concentration for every fixed kernel

Let W be the inverse Fourier transform of w. Positive definiteness gives W ≥ 0 and integral W = 1. The periodized packet is

    S_X(x) = X sum_{m in Z} W(X(x+m)).

Define T(r) = integral_{|u|>r} W(u) du → 0. Outside the union of radius-r/X arcs around the 2J translated or reflected packet centers, the average packet mass has integral at most T(r). Thus for η > 0,

    meas{(sum packets)/(2J) > η} <= 4Jr/X + T(r)/η.

Choose r → ∞ with Jr/X → 0. This proves that the average packet tends to zero in probability, independently of the centers. Write

    B = sqrt(J/8),
    c = 1/sqrt(32J),
    E_X = P_X + c sum packets - B.

The smooth part satisfies P_X ≥ -1/4 and integral P_X = 0, so (P_X+1/4)/B → 0 in probability by Markov's inequality. Consequently E_X/B → -1 in probability.

The global bound E_X ≥ -B-1/4 and convergence in probability imply M_X/B → 1. Therefore E_X/M_X → -1 in probability, proving H_X(t) → 1 for each fixed t < 1 in the stated depth range. For the triangular kernel T(r) = O(1/r); a general fixed kernel need not have that rate.

### A separate obstruction to a stable profile-only discriminator

Fix any nonempty Boolean A and its f,M. Choose q > max A and let

    K_N(x) = (1/N) |sum_{k=0}^{N-1} exp(2πikx)|²

be the Fejér kernel. For 0 < ε ≤ 1/2, define

    F = f + ε(K_N(qx)-1).

The supports are disjoint and all coefficients lie in [0,1]. Its coefficient-square energy is

    E(F) = |A| + 4ε² (N-1)(2N-1)/(6N).

Since K_N ≥ 0 and integral K_N = 1,

    F >= f-ε,
    ||F-f||_1 <= 2ε.

For U = {f < -M+δ}, with measure u > 0, some x ∈ U has K_N(qx) ≤ 1/u. Thus

    M-δ-ε/u <= M_F <= M+ε,

proving M_F → M uniformly in N as ε → 0.

Choose ε → 0 and Nε² → ∞. Then M_F/sqrt(E(F)) → 0 but F/M_F → f/M in probability. Every level set of the nonconstant trigonometric polynomial f is finite, so its distribution is atomless. The distribution functions, and hence H_F on [0,1], converge uniformly to H_A.

**What this adds.** Every fixed Boolean H-shape can be approximated uniformly by bounded fractional polynomials with diverging normalized energy. This does not match P61's two coefficient profiles, nor rule out a genuinely Boolean energy theorem. It rules out treating stable H-shape separation alone as the required energy mechanism.
