# Math brief (codex research agent), round 3: spike-dominated dense sets

You are a research mathematician working on Chowla's cosine problem in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine.
- Read CLAUDE.md first: conventions, honesty labels, and the rule that numerics are not proofs.
- Conventions: f_A = Σ_{a∈A} cos(ax), M(A) = −min f_A, n = |A|, S = A ∪ (−A).
- Rules (unchanged from rounds 1–2):
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents. No LaTeX; markdown only.
  - Report: `.research/agents/tdense3_report.md`. Scratch: `.research/agents/tdense3_scratch/`.
  - Computation ONLY on the VM via `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 ...` (at most 2 cores).
  - Gurobi (gurobipy) for any LP/MILP.
  - Label every claim PROVED / NUMERICAL / HEURISTIC / CONJECTURED; exact quantifiers.

## Target
T-dense: for every C >= 1 there is c(C) > 0 with M(A) >= c(C)√n for all A ⊂ [1, Cn], |A| = n.

## State after rounds 1–2 (read PROOFS P38–P46 and NOTEBOOK entries of 2026-10-19 late / late night)
- Proved:
  - P38: denominator filters for cumulative rounding.
  - P41: curved cumulative rounding via spike truncation, van der Corput and Vaaler.
  - P44: bounded discrepancy plus local overshoot.
  - P42: LM-dense is false.
  - P43: reciprocal masks on the random Fejér-mixture family.
  - P45: fixed-order moment certificates are blind behind spikes.
  - P46: MS ⇒ T-dense.
- The exact general reduction is P40 (spike truncation, Bhatia–Davis).
  - If M <= ε√n, then ∫_{f > √(n/ε)} f² >= (½ − √ε − 2ε²)n on a set U with |U| <= ε^{3/2}.
  - So a dense counterexample is SPIKE-DOMINATED: f ≈ −M + positive spikes carrying almost all L² energy, and
    1_A ≈ P_U 1_A in ℓ².
- Conjecture SB (NOTEBOOK): ∫_{f <= K√n} f² >= c·n for every A. It implies Chowla.
  - E67: no violator; SB is minimised by intervals (β ≈ 0.05–0.1, bulk = negative sidelobes).
  - Bu/Singer: β ≈ 0.45. Certified small optima: β ≈ 0.25–0.4.
- Recorded failures, do not repeat (NOTEBOOK late night):
  - Physical-space approximate-group arguments from f⊛f = ½f lose a factor ~ε√(δn): the errors are
    ‖φ‖₁·‖φ‖₂‖r‖₂ with ‖φ‖₁ ~ M.
  - Positive-definiteness of the spike part loses sup|r| ~ K√n.
  - P25 localization works at x-resolution 1/H ≫ 1/X, the spike width.
  Every route lost exactly the √n scale. The missing ingredient must be exact at that scale, as P41's exponential sums
  are for a specific rounding.

## Tasks, in priority order
T1. Spike-dominated dense sets. Assume A ⊂ [1, Cn], M <= ε√n, so P40's spike domination holds. Derive a contradiction
  for ε < ε₀(C), OR prove a precise structural consequence and isolate the single remaining lemma. Ideas, use or
  replace:
  - (a) Twisted profiles. At a spike x₀ the local shape of f is the transform of w(m) = 1_A(m)e^{imx₀} smoothed.
    Positivity forces each twisted profile to be "positive-definite / front-loaded"; a structure centred at nonzero
    phase gives anti-spikes (P24). Make this exact and quantitative.
  - (b) "Positive-bump uncertainty". A violator needs f̂(k) = hw·φ̂(kw)·Σ_j e^{−ikx_j}: positive bumps have decaying
    transforms, yet the coefficients are flat 0/1. So the spike point set must have exponential sums that vanish off
    S and grow toward the band edge on S. Formulate and prove a quantitative incompatibility, or find a point set
    that defeats it. The latter would be a construction lead: report it immediately.
  - (c) Multiscale. Split 1_A into band-limited layers (Fejér scales X, X/2, ...). Spike domination must hold for the
    filtered f at every layer, and the 0/1 constraint limits how much energy each layer can hide in spikes.
T2. Rigorous extensions of P41 (proof-writing; useful even if T1 stalls):
  - P41+: flat Sturmian pieces excluded from the bulk accounting. Needs the major/minor-arc Diophantine case analysis
    for the Vaaler truncation on flat pieces.
  - P41-B: cumulative rounding of Bohr-modulated curved profiles P(m/X, mα) (sketch in NOTEBOOK).
T3. Falsification. Test every candidate lemma on:
  - the E67 zoo (src/e67_zoo.py);
  - P42's family;
  - Bu/Singer sets;
  - the certified small optima;
  - the lead's constrained search E68 (examples/e68/), which looks for dense sets that are simultaneously
    spike-dominated (small β_K) and small in R.
  A dense set with small β_K AND small R would be the most important finding: report it with the exact set.

## Deliverable
A proof of T-dense or of a new explicit class, a precise single missing lemma with evidence, or a rigorous
obstruction. Say exactly what is new versus quoted.
