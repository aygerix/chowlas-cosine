# Brief: a live construction line — new mechanisms for R(A) < 1/2 (lead, 2026-10-18 night)

## Context: what is dead and why (read before proposing anything)
Chowla: f_A(x) = Σ_{a∈A} cos(ax), M(A) = −min f_A, R = M/√|A|. Epoch needs R → 0. The best known value is
R → 1/2 (Bu et al.); the best certified finite value is 0.5537 at N = 161202 (Bu's identity on Singer sets).

Obstructions already proved or strongly evidenced (see `.research/STATE.md`, `.research/PROOFS.md`):
- **P8 (kernel-checked).** If f_A + M = |Q|² (Fejér–Riesz) with Q = Σ_{β∈B} q_β e^{iβx}, then R < 1/2 forces the
  |q|²-weighted mean difference multiplicity of the support B to exceed 2. Efficiency also needs the pair products
  q_β q̄_{β−g} to be nearly constant on each difference class.
  - Equivalent kurtosis form: ‖Q‖_4^4/‖Q‖_2^4 = 1 + 1/(2R²), so R < 1/2 ⟺ kurtosis > 3. Q must be "spiky", with an
    autocorrelation that is exactly two-valued off the origin.
- **P23 (just done).** Sparse supports with coherent multiplicity λ >= 3 ("λ-fold near-rulers") fail: W >= k exactly
  for k <= 12 and growing, best R 0.68. Reflection symmetry gives multiplicity at most 2 (Bu); signs, products, cyclic
  lifts and homometric triples all fail.
- **Square / quadratic class (Smith's theorem):** one positive eigenvalue, giving exactly Bu, R >= 1/2. A sum of several
  squares Σ P_j² behaves like a pseudo-random square, R ~ √log.
- **Quartic chaos (P²−c)²:** 0/1 coefficients force a pure He_4, R ≈ 0.87.
- **Lifts of finite cyclic examples** (cyclotomic classes beat 1/2 in Z_p, E10): off-grid sinc excursions, or
  fluctuation noise √n unless the window is H-invariant mod p (NOTEBOOK night entries, E10/E11).
- **Also dead:** dithered Fejér/Beatty, separated-block unions, Sidon lower-flatness, model sets with simple windows,
  Erdős–Turán quadratic Sidon sets.

What is NOT excluded: **dense FR supports.** P8 is vacuous when B is dense (multiplicities are large automatically),
and the issue is coherence plus Gibbs. STATE calls the dense regime "the one live candidate against C½".
- Heuristic identity: R = c_E·√((1 − ρ)/2), with ρ <= ρ* ≈ 0.724 (the doubly-positive profile constant, P17 bounds
  ρ* <= 0.9057).
- So R < 1/2 needs a residual with min/std ratio c_E < 1.35 together with a positive-definite macroscopic profile.
- Exhaustive box optima: N = 36: 0.5648; N = 41: 0.574; N = 42: 0.579. MILP: N = 45: 0.5718. LNS (search-limited):
  N = 50: 0.584, N = 60: 0.624, N = 80: 0.663.

## Your task
Keep a genuine construction line alive, with two parts.

1. **Dense regime at larger N, done properly.** Previous large-N searches (SA, LNS-MILP) are search-limited: random
   starts reach only 0.60 at N = 36, against an exact 0.5648. Design a search that respects the structure of good dense
   sets. Two possible starting points:
   - Exhaustive optima are near-intervals with a tail that cancels the core's Dirichlet lobe (EXPERIMENTS E16/E17,
     NOTEBOOK "anatomy").
   - The macroscopic profile must be nearly doubly positive.

   Ideas you might use: profile-constrained seeding, then exact-window MILP/LNS (src/lns_milp.py, src/box_ilp.py);
   multiscale moves; homotopy from Bu-type sets to dense ones; MILP with cutting planes at violating x for N ~ 50–150.

   Deliver the best R you can certify at N ≈ 50, 60, 80, 100, 150, 200, 300 (certification: src/chowla.py /
   EXPERIMENTS E2 tools, ball arithmetic). The discriminating question is whether the best dense R decreases toward or
   below 0.55 as N grows, or keeps rising. Bu-type sets give the comparison curve 1/2 + 0.42·√(log k/k).
2. **At least two genuinely new mechanisms**, each with a precise construction, a reason it might evade P8/Gibbs, a
   quick numerical test, and a verdict.
   - Do not resubmit anything on the dead list above unless you identify exactly which obstruction it avoids.
   - Candidate directions (you may choose others):
     - Fejér–Riesz factors with dense support and chirp-like or algebraic phases, whose autocorrelation is
       two-valued: search directly over Q, then round |Q|² to a set.
     - Hierarchical or multi-scale compositions in which each scale's defects fall on the next scale's large values.
     - Model sets with arithmetic or fractal windows (the NOTEBOOK says "weakened, not killed").
     - Sets from algebraic curves over finite fields lifted with tapered H-invariant windows.

## Rules
- **Compute:** everything runs on the GCP VM dirichlet via `src/dirun.sh -c 4 ...`. Never compute on the laptop, never
  touch the VM `fejer`. Write C for hot loops.
- **Certification:** a grid or FFT minimum is evidence only. Any claimed R must state uncertified/certified, and any
  record must be certified (ball arithmetic per E2, or the derivative bound min >= grid_min − (π/K)·Σ|a|).
- **Labels:** PROVED / NUMERICAL-EXACT / NUMERICAL / CERTIFIED / CONJECTURED / FAILED. Preserve failures with the
  smallest counterexample and the reason.
- Edit only `.research/agents/construct_report.md` and `.research/agents/construct_scratch/`. Do not edit other
  `.research` files and do not commit.

## Deliverable
`.research/agents/construct_report.md` containing:
- the dense-regime table (N, best certified R, set or generator, method, time);
- the mechanisms tried, with verdicts and why;
- the single most promising lead.

If anything certifies R < 0.5537 at any N, or shows a clear downward trend below 0.56, report it immediately with the
set, and keep going.
