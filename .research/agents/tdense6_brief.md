# Math brief (codex research agent), round 6: adversarial — is there a "formal escape" from every proved constraint?

You are a research mathematician working on Chowla's cosine problem in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine.
- Read CLAUDE.md first: conventions, honesty labels, and the rule that numerics are not proofs.
- Conventions: f_A = Σ_{a∈A} cos(ax), M(A) = −min f_A, n = |A|, X = max A.
- Rules (unchanged):
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents. No LaTeX; markdown only.
  - Report: `.research/agents/tdense6_report.md` (keep it current). Scratch: `.research/agents/tdense6_scratch/`.
  - Computation ONLY on the VM via `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 ...` (at most 2 cores).
  - Gurobi (gurobipy) for any LP/MILP/QP.
  - Label every claim PROVED / NUMERICAL / HEURISTIC / CONJECTURED, with exact quantifiers.

## Target and state
T-dense: for every C >= 1 there is c(C) > 0 with M(A) >= c(C)√n for all A ⊂ [1, Cn], |A| = n.
Read first:
- PROOFS P40, P47, P52–P56. P56 is your round 5, with the lead's caveats.
- NOTEBOOK entries "2026-10-19 (night, cont. 7)" and "(night, cont. 8)". They contain:
  - the lead's uniform law-level TL1 (radial truncation);
  - the caveats on CY2 (the profile/central lobe is never graded; the central lag L(0) = R makes Z heavy-tailed);
  - the front Riesz test and the dimension barrier;
  - the HBSC negative-mass accounting: natural bound δ <~ M (or ~εM on radius-1/X windows), against the δ <= B·M/H
    that HBSC demands.

The lower-bound programme has reduced T-dense to one mesoscopic statement (HBCG / HBSC). Three rounds sharpened it
without closing it. This round TESTS it adversarially.

## Task 1 (main): construct a formal escape, or prove that none exists
Define precisely a class of "formal counterexample objects" that retains every constraint proved so far, and
nothing else. Suggested model: a sequence of local patterns, plus spike data, at mesoscopic heights:
- Blocks. A position variable t ∈ [0,1] and blocks of length ℓ (1 ≪ ℓ ≪ X). In each block a genuine BINARY word,
  or a [0,1] pattern realizable as a conditional expectation of a binary word, with local mean p(t). Global density
  ∫p = 1/C.
- Spikes. A spike set x_1..x_S with heights h_s ∈ [√(n/ε), o(X)], and twisted profiles w_s(t) equal to the local
  Fourier coefficients of the block patterns at x_s, so local Bessel and TL1 / FTL1-rad apply blockwise.
- Spike domination (P40): all but O(√ε)n of the energy lies in the spikes.
- Positivity:
  - each spike's Hermitian-extended profile has Fourier transform >= −M/X on its dominated region;
  - the sum of the contributions of all spikes and the bulk is >= −M pointwise in x.
  Make this exact for a finite family, e.g. on a fine x-grid with the true superposition, not spike by spike.
- SG: the Krein/Gram defect of any joint lift.
Then either:
- (a) EXHIBIT such an object with M <= ε√n for small ε (analytically, or numerically with Gurobi: LP/QP feasibility
  over profiles and spike data at moderate X, then increase X). Identify which mechanism lets it evade TL1/SG. Report
  its exact data. If it can be rounded to an actual set A, test the actual set (FFT minimum + refinement) and report
  R(A). A real set with small R would be the most important possible finding.
- or (b) PROVE that the constraints are inconsistent for ε < ε₀(C). That would be a proof of T-dense, or of a
  precisely stated conditional version.
- or (c) find the exact constraint that a formal escape violates only in the limit, and state it as the single
  missing lemma, replacing HBSC if it is weaker or more natural.
Be explicit about what "formal" leaves out, e.g. phase consistency between blocks (the same frequencies x_s in every
block), which ties the twisted profiles to one global sequence. The phase-consistency constraint may be exactly the
missing ingredient. Analyse it.

## Task 2: HBSC — prove, refute, or replace
- Decide whether HBSC (P56) can hold in the mesoscopic regime. The lead's accounting says the natural negative-mass
  bound is δ <~ M, while HBSC needs δ <= B·M/H.
- Either find the cancellation mechanism (why most spikes' profiles would be PD to relative accuracy M/H), or build a
  binary example (not necessarily a counterexample to Chowla) with M = o(X) whose tall-window lifts all have negative
  mass ≫ M/H. That would show HBSC is false as stated. In that case propose the correct replacement.
- Bu/Singer sets, E68/E72 optima and random dense sets are the available real data. Measure the actual negative
  spectral mass of natural lifts on them (block twisted profiles at their tall spikes, Hermitian-extended, FT
  negative part integrated).

## Task 3 (only if time remains): alternative mechanism
Bu et al. 2610.17160 Prop. 9.7: for A ⊂ [1, Cn], λ³‖f‖₁ >= (n − 1)/(32CC₁).
- Mechanism: the run-top bound |B_t| <= C₁K³μ summed over t, with Σ_t|B_t| >= N²/2 − N.
- Any bound Σ_{t <= 2Cn}|B_t| <= C'·n·K^{3−δ}μ (AVERAGED over t, using the order of Z) gives a dense exponent > 1/4.
- P22 shows group-agnostic per-t bounds cannot beat K⁴. Assess whether averaging over t plus Z-specific input (P31
  front structure, Fejér positivity) can beat K³μ. State the first missing inequality.

## Deliverable
For Task 1, a formal escape with exact data, a proof of inconsistency, or the precise missing constraint. For Task 2,
a verdict on HBSC. Say exactly what is new versus quoted.
