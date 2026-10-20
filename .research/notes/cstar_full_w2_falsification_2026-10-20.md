# Focused full-W2 falsification pass

**20 October 2026. Bounded test completed; the universal question remains open.**

## Target and outcome

For a finite positive-integer set A, put S=A∪(-A), N=|S|=2|A|, W2={0}∪S∪(S+S), and B_W2(u,v)=1_S(u-v). We tested the entire matrix, with K_W2=-λ_min(B_W2), seeking a growing family with K_W2/√N→0. For the original cosine sum, D=Σ_{s∈S}e(sx)=2Σ_{a∈A}cos(2πax) and K_global=2M(A), so K_global≥K_W2. These normalizations must not be interchanged.

**No vanishing-ratio family was found.** Four precisely defined enlargement classes have rigorous exclusions. Other outcomes are finite numerical observations, not asymptotic lower theorems. A small eigenvalue of a fixed trial space was never substituted for a small least eigenvalue of the full matrix.

## 1. Rigorous exclusions

### Tensor amplification

For T={0}∪S, W=T+T, B=B_W2(S), K=-λ_min(B), and ρ=λ_max(B), the unitized product S_d=T^d\{0} has the exact full-operator identity

    I+B_W2(S_d) = (I+B)^(tensor d),
    K_d = 1+(K-1)(1+ρ)^(d-1).

The full base matrix satisfies K≥√2 and ρ≥√N. Thus every fixed unitized base has normalized K_d tending to infinity, not zero. The heterogeneous version satisfies

    K_*/sqrt(N_*) ≥ ((sqrt(2)-1)/sqrt(3)) max_i K_i/sqrt(N_i).

A unitized product therefore cannot manufacture a vanishing ratio from constituent factors whose ratios stay bounded below.

For categorical powers S^d, let h=|S∩(S+S)|. The isolated leaves give

    K_W2(S^d)/sqrt(N^d) ≥ sqrt(1-(h/N)^d).

If h<N, this tends to one. If h=N, an exact tensor identity and a strict Perron bound give exponential growth. Consequently every fixed categorical base has liminf normalized K≥1. Changing near-contained bases remain a loophole; the result is not a universal tensor-free theorem.

### Unequal axis intervals

For S={t e_j:1≤|t|≤L_j}, even the first neighborhood already gives

    K_W2 ≥ K_W1 ≥ c sqrt(N),
    c = sqrt((sqrt(2)-1)/(sqrt(2)+5)) > 0.254.

The proof combines a three-block interval compression on the longest axis with the central-star compression. This is an axis-family exclusion, not a new general advantage of W2.

### Fixed geometric orbits

Fix b≥2 and finitely many primitive positive seeds R with b∤r. For any finite symmetric subset of ±R·b^j, set H=floor(log_b(2 max R)) and Δ=2|R|(2H+1). Order and divisibility bound the induced degree on S by Δ. Hence the central compression proves

    K_W2 ≥ (sqrt(Δ²+4N)-Δ)/2 ≥ sqrt(N)-Δ/2.

Arbitrary deletions within those fixed orbits are allowed. A growing primitive seed is not covered.

### Exact interval fibers

Suppose S⊂S+S and S′=qS+[-h,h], with q>5h. Unique digit coordinates give the exact full matrix B_W2(S′)=B_W2(S)⊗T_h, where T_h(r,t)=1_{|r-t|≤h} on [-2h,2h]. Therefore

    K_W2(S′) ≥ K_W2(S)[(2h+1)-h(h+1)/(4h+1)].

Its normalized certificate grows at least proportionally to √h times the seed's. This excludes these exact symmetric fibers, not adaptive unequal or correlated fibers.

Proofs: [tensor non-amplification](../experiments/full_w2_falsification_2026-10-20/analytic/tensor_nonamplification.md), [axis intervals](../experiments/full_w2_falsification_2026-10-20/analytic/axis_interval_full_w2.md), [geometric orbits and interval fibers](../experiments/full_w2_falsification_2026-10-20/multiscale/report.md).

## 2. Full-matrix numerical findings

The multiscale branch completed 84 runs. Examples below use actual realized N, not target cardinality. Values are floating-point estimates, not interval-certified spectral bounds.

| Family | N | Full W2 rows | K_W2/√N |
|---|---:|---:|---:|
| Balanced cumulative triangular rounding | 2,048 | 35,699 | 3.671881 |
| Centered quadratic triangular rounding | 8,420 | 234,073 | 3.578729 |
| Two centered rotations | 8,184 | 64,491 | 9.199987 |
| Dyadic seed replication, J=8 | 484 | 21,587 | 2.070613 |
| Dyadic seed replication, J=12 | 676 | 76,307 | 1.819338 |
| Singer difference lift, p=89 | 8,010 | 30,105 | 0.943956 |
| Sparse collapsed difference support | 3,874 | 111,595 | 1.500476 |

Dyadic replication declines over this finite range, but the fixed-geometric-orbit theorem excludes a zero limit for this fixed seed. Filled and tapered blocks instead grow strongly, reaching ratios approximately 44.83 and 40.69. Deterministic triangular roundings, including centered rotations through target cardinality 4,096, produce no vanishing-ratio lead. Their untested asymptotic behavior is not settled by these curves.

The correlated branch used three genuinely dependent constructions:

- Complete-residue triangular lifts preserve both the exact quotient and a prescribed height histogram. Histogram-preserving annealing gave best ratios 1.370, 1.627, 2.166 and 2.570 for N=30,60,126,250. These are bounded heuristic searches, not global optima.
- Singer perfect-difference lifts give D=|F_T|²-(p+1), exactly, with N=p(p+1). Thus K_global≤p+1 even though the finite quotient has K=1. Full-W2 ratios stayed approximately 0.88–1.03 through N=8,010. Exhaustive cyclic-cut choices through N=992 did not produce a decreasing trend. Neither an asymptotic limit nor a uniform positive lower constant is proved for these lifts.
- Collapsed random difference supports discard repeated differences to restore Booleanity. Tested ratios were approximately 1.39–1.93. There were only a few sizes and seeds; this is not a distributional theorem.

The final 18-case diagnostic compared B on T=S+S with B on full W2. These matrices need not agree: A={1,3,6} gives numerical K_T/K_W2≈0.96591. No promising near-contained growing-base gap appeared, but no uniform comparison theorem was established.

## 3. Independent validation and limits

All principal matrix-vector operations use nonwrapping zero-padded convolution on the full row set, not a sampled global Fourier minimum or a finite quotient matrix. The largest recorded full matrix has 234,073 rows.

Independent checks include:

- Exact Python-integer bitset verification of W2 for all 24 principal correlated supports.
- Separate entrywise construction and dense eigensolves on two small validation matrices.
- A directly assembled sparse matrix for dyadic J=8: 21,587 rows and 7,695,116 nonzeros. Its least eigenvalue agrees with the FFT result to about 1.4×10^-14; its residual is about 7×10^-12.
- Seven interval-fiber Kronecker comparisons against separately assembled full operators, agreeing within 2.1×10^-12.

Small residuals do not alone prove that an eigensolver found the absolute least eigenvalue. The large numerical outputs are not certified upper bounds for K_W2. Computed vectors provide Rayleigh lower tests up to numerical evaluation error. The rigorous exclusions above rely on proofs, not those residuals.

The [independent audit](../experiments/full_w2_falsification_2026-10-20/audit.md) records the separate checks and qualifications. Raw reports, support JSON, scripts and hashes are in the [reproduction index](../experiments/full_w2_falsification_2026-10-20/README.md). Large binary eigenvector caches are omitted; exact support inputs are retained so the full operators can be regenerated.

## 4. What remains unresolved

This focused pass does not refute universal full-W2 square-root control. It also does not prove it. The rigorous exclusions concern tensor amplification, axis intervals, fixed geometric seeds and exact interval fibers only. Finite Singer and deterministic-rounding curves do not close untested asymptotic regimes.

A possible escape would need features not neutralized here, such as growing primitive templates, genuinely adaptive fibers, or correlated lift geometry that suppresses the full negative spectrum. No such construction was established. This is the outcome of the approved bounded falsification test, not an assertion that all research directions are exhausted.
