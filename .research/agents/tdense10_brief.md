# Math brief (codex research agent), round 10: the second-order reach 1/D ≈ 8.571; certify it, then go past it (binarisation)

You are a research mathematician working on Chowla's cosine problem in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine.
- Read CLAUDE.md first: conventions, honesty labels, and the rule that numerics are not proofs.
- Conventions: f_A = Σ_{a∈A} cos(ax), M(A) = −min f_A, n = |A|, X = max A.
- Rules (unchanged):
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents. No LaTeX; markdown only.
  - Report: `.research/agents/tdense10_report.md` (keep it current). Scratch: `.research/agents/tdense10_scratch/`.
  - Computation ONLY on the VM via `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 ...` (at most 4 cores).
  - Gurobi (gurobipy) for every LP/MILP/QP (NonConvex=2 for bilinear terms).
  - Label every claim PROVED / NUMERICAL / HEURISTIC / CONJECTURED, with exact quantifiers.
  - Grep PROOFS.md before any novelty claim.

## State (read PROOFS P58–P61, NOTEBOOK cont. 11–12, EXPERIMENTS E80–E82, and your round-9 report)
- Your round 9 (lead-verified as P60) proved T-dense(C) for C < 6.9366: κ <= 0.749089, scalar reduction, redundancy
  of the density windows.
- You also found that residual covariance kernels are completely positive (CP), strictly beyond doubly nonnegative.
- The lead then made CP EXACT (P61, paper proof):
  - Gabor identity: for h = g + m >= 0 and a band-limited window ψ >= 0, avg_u |(h·ψ(· − u))^|² = |ĥ|² ⋆ |ψ̂|².
  - So the smoothed residual energy profile is an average of |w_u|², with each w_u a Hermitian PD function supported in
    [−1 − ε, 1 + ε].
  - Jensen with the convex φ(x) = (1 − √(1 − x))/2 gives, in every dense counterexample limit,
        ∫_0^1 φ(e/e(0)) <= D   and   d <= D,
        D := sup{ ∫_0^1 φ(|w|²) : w PD on R, supp w ⊂ [−1,1], w(0) = 1 }
           = sup{ ∫_0^1 φ((G⋆G̃)²) : G >= 0 on [0,1], ∫G² = 1 }.
  - Hence T-dense(C) for every C < 1/D. Windows, Beckner, ρ* and κ are not needed except to bound D.
  - SHARPNESS: your Task-3 weighted Fejér-packet escape, with packet transform w, realises every w. So 1/D is the exact
    reach of "positivity + two binary moment profiles".
- Numerics (E82, src/e82_cp_reach.py, examples/e82/):
  - D ≈ 0.1166747, 1/D ≈ 8.5708. All starts agree; the optimiser G* is a symmetric bump with G*(0)/G*(½) ≈ 0.38 and
    ∫_0^1 w² = 0.3400.
  - N₂ := sup ∫_0^1 w² ≈ 0.343488 (Beckner gives 0.38490).
  - κ_w := sup ∫φ(w²)/∫w² ≈ 0.3557 (still creeping up with N).
- Rigorous today: D <= rκ/4 (Beckner and your κ), i.e. T-dense(6.9366).

## Task 1 (first, bounded): adversarial check of P61
Try to break P61(a) and P61(b). Check every step:
- conventions and normalizations in the Gabor identity;
- uniform convergence in t;
- Hermitian PD and support of ŝ_u;
- Jensen over the continuous u-average;
- the dilation into the class;
- the X → ∞ and ε → 0 limits;
- a <= ½ and p = φ(4e);
- the Boas–Kac WLOG;
- for (b): positivity, the LLN for the profiles, and that P58's machinery applied to the escape returns exactly (p, e).
Report any gap with a fix, or state PROVED with the precise statement.

## Task 2 (main): a rigorous upper bound D₁ on D, hence T-dense(C₁₀) with C₁₀ = 1/D₁
Target C₁₀ >= 7.5; 8 or more would be excellent. Every exact improvement over 6.9366 counts. Ideas, unordered:
- (i) w-level Toeplitz potentials. For nonnegative PD w:
  - w(2t) >= 2w(t)² − 1 (stronger than the q-level branch, because (2x − 1)² − (2x² − 1) = 2(1 − x)²);
  - the 4-point branch;
  - Chebyshev supporting lines.
  Certify ∫φ(w²) <= κ_w'∫w² with κ_w' near 0.3557, then use Beckner N₂ <= r/2. That gives ≈ 7.3.
- (ii) A rigorous N₂ < 0.3849, i.e. sharp continuous additive energy ‖G⋆G̃‖₂² for unit-interval support, G >= 0.
  Numerical sup 0.686976 for ∫_{−1}^{1}; constant G gives 2/3. Any rigorous N₂ <= 0.36 is valuable. Check the literature
  briefly (continuous additive energy / L⁴ Nikolskii for Paley–Wiener / autoconvolution L² norms), but cap the search.
- (iii) Support-coupled certificates. These are needed to approach 8.57, because split bounds cap near 8.2.
  - t-dependent linear majorants φ(x²) <= a(t)x + [B(2t, y) − B(t, x)/2] with y >= L(x), using the dilation identity
    ∫B(2t, w(2t))dt = ½∫B(s, w(s))ds.
  - Then ∫_0^1 a w = ½⟨G, T_a G⟩ <= ½λ_max(T_a), where T_a has kernel a(|x − y|) on L²[0,1]. Bound λ_max rigorously,
    e.g. by a Schur test with a positive test function, or by a certified discretization bound.
  - The Egerváry–Szász / CF envelope w(t) <= cos(π/(⌊1/t⌋ + 2)) bounds the x-range.
- (iv) Anything else that is rigorous: Lasserre/SDP for the quartic structure, or branch-and-bound on a discretization
  with a proved continuum error.
Deliverable: an exact certificate (independently re-verifiable) and the theorem T-dense(C₁₀).

## Task 3 (main research): beyond 1/D — binarisation
Every positivity statement holds for the weighted escapes. So T-dense beyond 1/D, or a dense counterexample, depends
only on whether BINARY coefficient sequences can carry a residual made of positive packets.
1. Third order.
   - A binary sequence has coefficient skew Σ_k r_k³ψ(k/X)/X → ∫p(1 − p)(1 − 2p)ψ.
   - Random-centre packets give 0.
   - Resonant centres (θ_a ± θ_b ± θ_c ≈ 0 within 1/X) give skew. About J^{3/2} resonant triples are needed; an AP of
     centres gives ~J².
   - The required skew profile is e(1 − 2p) = (w²/4)√(1 − w²), which vanishes as w → 1. A single packet family's skew
     scales like w³, so several families with tuned cross-resonances are needed.
   Determine the reach of "positivity + THREE binary moment profiles". Either:
   - exhibit weighted escapes matching three moments (the reach is then <= the reach of your construction; is it still
     1/D?), or
   - prove a cubic inequality that forces a larger reach (for example, the CONJECTURED Σr³ <= B·M² + o(X) of your
     round 9, or something sharper).
2. Full binary law.
   - Lead's facts: (i) a {0,1}-valued PD function on a group is the indicator of a subgroup; (ii) Bohr /
     cut-and-project binarisations need PD window indicators, which is impossible; (iii) random rounding adds Θ(X) bulk
     error energy (P40).
   - Formulate the right "binary + positive packets" obstruction, or a construction that evades it.
   - A construction with R → 0 in the dense regime would disprove Chowla. Test any candidate numerically on the VM
     (FFT minimum, then a certificate for the best one).
   - An obstruction theorem pushing T-dense past 1/D is the Track-L goal.
   Either outcome is a result. Preserve every failed construction with its numbers.

## Deliverable
- Task 1: verdict on P61 with any fix.
- Task 2: rigorous D₁ with certificate, and T-dense(C₁₀).
- Task 3: the third-order reach (construction or inequality) and the clearest binarisation statement you can prove or
  refute.
Say exactly what is new versus quoted.
