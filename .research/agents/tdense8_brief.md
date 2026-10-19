# Math brief (codex research agent), round 8: from T-dense(4.44) to the macroscopic reach ≈ 6.05, then beyond

You are a research mathematician working on Chowla's cosine problem in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine.
- Read CLAUDE.md first: conventions, honesty labels, and the rule that numerics are not proofs.
- Conventions: f_A = Σ_{a∈A} cos(ax), M(A) = −min f_A, n = |A|, X = max A.
- Rules (unchanged):
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents. No LaTeX; markdown only.
  - Report: `.research/agents/tdense8_report.md` (keep it current). Scratch: `.research/agents/tdense8_scratch/`.
  - Computation ONLY on the VM via `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 ...` (at most 2 cores).
  - Gurobi (gurobipy) for any LP/MILP/QP/SDP-like optimisation (NonConvex=2 for bilinear terms).
  - Label every claim PROVED / NUMERICAL / HEURISTIC / CONJECTURED, with exact quantifiers.
  - Before claiming novelty, grep PROOFS.md. Round 7 re-derived our own P17(a) without noticing it.

## Where we are (read PROOFS P58, P17, P31, P32, P40, P47, P48, P53; NOTEBOOK cont. 9–10; E16, E78)
- Round 7 (your previous round; lead-verified) proved T-dense(C) for C < C_7 = (2/r)(1 + √(1 − ρ*))².
  - r is the asymptotic P31 Nikolskii constant: 4/(3√3) (Beckner) or 0.811 (elementary).
  - ρ* := sup ∫w²/(w(0)∫w) over even integrable doubly-positive w (w >= 0, ŵ >= 0).
  - With P17(a)'s ρ* <= 0.90565 this gives C < 4.4393, with an ineffective constant.
  - Mechanism: compactness gives a PD limit profile p. The exact high-pass diagonal gives the energy window
    p(0)(1 − p(0)) >= (2/r)∫p(1 − p); P31 gives the density window p(0) >= (2/r)∫p.
- Numerically ρ* ≈ 0.7239 (E16; E78: all autocorrelation starts converge to 0.723871, slightly above the half-sine
  autocorrelation's π²/24 + 5/16 = 0.723734). The sharp ρ* would give C ≈ 6.046.
- Your exact witness (witness_B48.json; archived in examples/r7_certificates/) is PD and fails both windows at every
  θ at 1/d = 6.0539. So the macroscopic PD + window method stops at ≈ 6.05.
- Lead's analysis (NOTEBOOK cont. 10):
  - Realisations of the witness are Chowla-safe for other reasons: random rounding is bulk-dominated (P40);
    cumulative rounding is P41-type.
  - A counterexample beyond 6.05 must carry essentially all of its residual energy (≈ 0.525d, about half the total) in
    spikes of height >= √(n/ε) (P40 applied to H_h f). Whatever is not carried by macroscopic twisted atoms must be
    MESOSCOPIC spikes, which the macroscopic limit cannot see.
  - Band-pass windows: for every mesoscopic filter H ∈ [0,1], H·f >= −M, so the windows apply to every spectral
    portion. In the limit σ_{0+} >= (2/r)∫σ_t dt as measures. This adds nothing against the witness family
    σ_t = e(t)ν.

## Task 1 (bounded): sharpen ρ* rigorously
Prove ρ* <= ρ₁ with ρ₁ as small as you can. Each improvement converts directly into T-dense(C) via
C < (2/r)(1 + √(1 − ρ₁))²; for example ρ₁ = 0.80 → 5.44, 0.75 → 5.85, 0.7245 → 6.04.
- Ideas, unordered:
  - Multi-point Gram constraints. For each t, the sequence (w(kt))_{k∈Z} is PD with w(0) = 1 (Toeplitz PSD). P17(a)
    used only {0, t, 2t}.
  - The separable trick: for any functions α, β, ∫_0^∞ β(w(2t))dt = ½∫_0^∞ β(w(t))dt. Search for pointwise inequalities
    α(w(t)) >= β(w(2t)) (or with more lattice points) valid for all PD sequences that integrate to ∫(ρw − w²) >= 0.
    Gurobi can optimise the certificate within a parametrised family.
  - Non-separable cross terms ∫w(t)w(2t) are where P17(a) loses (Cauchy–Schwarz). Try to bound them sharply.
  - Fourier symmetry: J(w) = J(ŵ) (Plancherel). Use constraints on w and ŵ simultaneously.
  - Literature: doubly-positive / Turán-type extremal problems (Gorbachev, Ivanov, Tikhonov, Kolountzakis, Révész).
    Is sup ∫w²/(w(0)∫w) known? Cap this search at a short look.
- Also decide numerically whether general doubly-positive w beat the autocorrelation class (E78 suggests not; E16
  reported 0.7245 for signed h with a penalty). Report the best numerical ρ* with method and resolution.
- Deliverable: a theorem ρ* <= ρ₁ with exact-arithmetic certificate if computer-assisted, hence T-dense(C₁') with
  explicit C₁'.

## Task 2 (main research): beyond the macroscopic barrier
Goal: prove T-dense(C) for some C > 6.054, or produce a precise two-scale formal escape that explains why not.
1. Two-scale limit object. Describe a counterexample sequence with C slightly above 6.05 by:
   - the macroscopic profile p (PD, both windows);
   - the macroscopic twisted atoms (P48/P53: PD Hermitian profiles, local Bessel);
   - a MEASURE-valued description of the mesoscopic spikes (heights h ∈ [√(n/ε), o(X)], frequencies, twisted
     amplitude profiles w_s(t) along position t).
   Use P40 on f and on every filtered H·f (all residual energy in spikes).
2. √n-scale constraints that survive in this two-scale limit. Derive each precisely, with error terms:
   - (a) P32's LOCAL window, pointwise in x₀ before averaging. Spike energy near x₀ <= (3ρ/2θ)(M + g_w(x₀))², where
     g_w is the front-weighted cosine sum. In the limit, a mesoscopic spike's twisted amplitude must be FRONT-LOADED IN
     AMPLITUDE: g_w(x_s) ∝ X∫_0^θ(1 − t/θ)w_s(t)dt must be large compared with the spike's energy. Quantify this.
   - (b) Band-pass windows (H ∈ [0,1] around groups of spikes): aggregated spike energy profiles are front-loaded.
   - (c) Mesoscopic PD of twisted profiles (the HBSC question). The round-6 verdict: natural lifts fail. Which
     aggregated/windowed form survives?
   - (d) Higher-order windows: L⁶ Nikolskii windows (third moments) and product windows (f + M)(f(· + θ) + M) >= 0.
     Do they give NEW macroscopic constraints on p, or on (p, spikes), beyond the two windows?
3. Feasibility. With the witness profile (or the optimal ρ* profile) as the macroscopic part, decide whether some
   spike configuration satisfies all of (a)–(d) plus local Bessel and the binary energy identity e = p(1 − p).
   - If infeasible: compute the new reach C₂ > 6.05 and prove T-dense(C₂) (ineffective is fine).
   - If feasible: exhibit the formal escape exactly. Try to realise it as actual sets (VM) and measure R. Name the
     extra constraint a real set would violate (arithmetic coherence of spike frequencies? the TL1 81% cap? SG?).
   Either outcome is a result. A real set with small R would be the most important finding.

## Task 3 (only if time remains): effective constant
Replace the compactness/diagonal by a finite-scale argument (energy-increment choice of the smoothing width h,
quantitative PD of the smoothed profile with error O(M/X), robust P17(a)). Prove an explicit c(3) > 0 (tiny is fine).
This is the Lean candidate: say which steps are finite inequalities.

## Deliverable
For Task 1, a rigorous ρ₁ and the resulting C. For Task 2, either T-dense(C₂) with C₂ > 6.054 and a proof, or the
precise two-scale formal escape and the single missing mesoscopic inequality. Optionally Task 3. Say exactly what is
new versus quoted.
