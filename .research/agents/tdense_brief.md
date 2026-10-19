# Math brief (codex research agent): target T-dense — Chowla for dense sets A ⊂ [1, C·n], every C

You are a research mathematician working on Chowla's cosine problem in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine.
- Read CLAUDE.md first: conventions, honesty labels, and the rule that numerics are not proofs.
- Conventions: f_A(x) = Σ_{a∈A} cos(ax), M(A) = −min_x f_A, n = |A|.
- Rules:
  - Do NOT edit .research/*.md (the lead records results after verifying them). Do not commit. Do not launch
    subagents.
  - Write everything to `.research/agents/tdense_report.md` and keep it current: statements, full proofs or precise
    gaps, failed attempts with the exact reason, and code/data paths.
  - Computation: ONLY on the VM via `src/dirun.sh [-c cores] [-t secs] <cmd>` (see its header). Use at most -c 2
    (the VM is shared). Never compute on the laptop. Gurobi is the MILP/LP solver (gurobipy on the VM).
  - Scratch code goes in `.research/agents/tdense_scratch/`.
  - Label every claim PROVED / NUMERICAL / HEURISTIC / CONJECTURED. Keep all quantifiers exact.

## Target
T-dense: for every C >= 1 there is c(C) > 0 such that every finite A ⊂ [1, C·n] with |A| = n >= 1 has
M(A) >= c(C)·√n.
- Literature: Bu et al. arXiv:2610.17160 Prop. 9.7 proves only n^{1/4} for this class (via a run-top / boundary
  estimate, their Prop. 9.1). Their Remark 9.8(iii) leaves √n open.
- Ours (KERNEL-CHECKED): √n for C < 2.466 (|A| >= 0.41·max A ⇒ M >= √n/1000; P31 + P31-E).
- A proof for all C would be a new theorem. So would a proof for C up to some explicit C₀ > 2.466 by a genuinely
  new mechanism. A rigorous obstruction (a family where all available mechanisms provably fail), or a counterexample
  family, would also be valuable.

## What is known here (read these sections of .research/PROOFS.md and .research/NOTEBOOK.md)
- P31 (window–Nikolskii, PROOFS "P31"):
      W_w(M² + n/2) <= C_L(M² + S_A(w)/2),
  with S_A(w) = Σ_{a∈A}(1 − a/(w+1))₊², W_w = 1 + 2S_w, L = max A + w, and C_L = 0.811(L + 1) + 71/300
  (or (4/(3√3))(L + 1)(1 + o(1)) via Beckner, now kernel-checked).
  It gives √n unless A is FRONT-LOADED at every scale: S_A(θX) >= 0.822·θ/(1+θ)·n for all θ, roughly.
  So T-dense reduces to front-loaded dense sets.
- Escape-class structure (NOTEBOOK 2026-10-19 "frequency-localization no-go", "Why the P31 family stops"):
  - Localized windows are exactly critical on locally full sets.
  - EVERY second-moment window/PD-reweighting/dilated-window argument is linear in 1_A, i.e. a profile constraint,
    and front-loaded equidistributed sets satisfy all of them.
  - So the proof must use NONLINEAR (additive) information.
  - Front-loaded profiles evade because a convex decreasing density has a nonnegative cosine transform (Pólya);
    the √n must come from the rounding fluctuation.
- Tools (all kernel-checked):
  - P33: M >= n·min A/max A.
  - Dilation pinch: |A ∩ qZ| >= n/q − (1 − 1/q)M, and M(A ∩ qZ) <= M(A).
  - P36: truncation at gaps, M(A) >= M(A ∩ [1, D]) − (1 − cos(π/(D+2)))Σ_{a<=D} a².
  - P34: the complex-coefficient (phase-blind) window inequality.
- Third moment (classical): (∫(f+M)²)² <= ∫(f+M)·∫(f+M)³ gives M >= min(½√n, n²/(6T)), T = #{a + b = c}.
  A localized version with the multiplier (1 − K̂_H) (NOTEBOOK "B-test" section) needs a fine-scale triple EXCESS
  >= n^{3/2}/R to escape.
- Numerics (E52, E59, E63 in .research/EXPERIMENTS.md): searched front-loaded dense sets are bad (R ≈ 0.9–1.8).
  Every near-optimal dense set found is NOT front-loaded.

## Suggested lines (pick, combine, or replace with better ideas; say which you pursue and why)
1. Dichotomy by fine-scale additive structure. In the front-loaded dense case, combine P31 with a localized third
   moment (or a higher moment), so that front-loading plus few fine triples gives a contradiction.
   Then show that many fine triples in a dense set force structure (residue bias, long progressions) that the pinch,
   P33 or P36 can exploit.
2. Run/boundary structure (Bu et al. Prop. 9.1 gets n^{1/4} for all C). Sharpen their boundary estimate using
   front-loading. A front-loaded dense set has a dense initial segment at every scale: long runs.
3. Smooth part plus fluctuation. Write 1_A = ρ + β, with ρ the local density (convex decreasing, by Pólya and the
   kink argument of E52) and β the rounding error. Prove the fluctuation β must create a dip of size √n at some
   x >> 1/X, using P34 (phase-blind, complex coefficients) on a suitable positive-operator image of f_A.
4. Multi-scale / recursive. Front-loading cannot iterate more than O(log(1/δ)) density doublings in a dense set,
   since density <= 1. Find a mechanism that cashes this in. Note: truncation without gaps loses Θ(|core|), so a
   naive recursion fails; explain exactly why if you go this way.

## Falsification first
Before investing in a lemma, test it on:
- power-law profile sets ρ(t) ∝ t^{α−1} (α <= 0.79), randomly rounded and Beatty-rounded;
- two-level profiles;
- Bu/Singer sets (density ≈ 1/3, R -> ½, NOT front-loaded);
- the certified dense optima (examples/construct/N50_certified.json, examples/smallN_best.json).
The evaluator box_minlam.true_min (src/box_minlam.py) gives a grid + Newton minimum. That is evidence, not proof.

## Deliverable
A proof (complete, with explicit constants or explicit dependence on C), a precise reduction to one clearly stated
missing lemma with evidence, or a rigorous obstruction. State exactly what is new versus what is quoted.
