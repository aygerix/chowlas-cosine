# Math brief (codex research agent), round 9: the full macroscopic reach of T-dense, effective constants, then mesoscopic

You are a research mathematician working on Chowla's cosine problem in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine.
- Read CLAUDE.md first: conventions, honesty labels, and the rule that numerics are not proofs.
- Conventions: f_A = Σ_{a∈A} cos(ax), M(A) = −min f_A, n = |A|, X = max A.
- Rules (unchanged):
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents. No LaTeX; markdown only.
  - Report: `.research/agents/tdense9_report.md` (keep it current). Scratch: `.research/agents/tdense9_scratch/`.
  - Computation ONLY on the VM via `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 ...` (at most 2 cores; another
    lead job, E80, is using 1 core).
  - Gurobi (gurobipy) for every LP/MILP/QP (NonConvex=2 for bilinear terms).
  - Label every claim PROVED / NUMERICAL / HEURISTIC / CONJECTURED, with exact quantifiers.
  - Grep PROOFS.md before any novelty claim.

## State (read PROOFS P17, P31, P40, P48, P53, P58, P59; NOTEBOOK cont. 10–11; E78–E79)
- Your rounds 7–8 (lead-verified) proved T-dense(C) for every C < 4(2 − ρ)/r = 6.156, with an ineffective constant.
- Ingredients:
  - the PD limit profile p;
  - the exact high-pass diagonal (residual energy profile e = p(1 − p));
  - P31 density and energy windows;
  - ENERGY-PD (autocorrelation of g + m >= 0 ⇒ e PD ⇒ a = p(0) <= ½);
  - ρ* <= 0.815276.
- You also proved an explicit c(3) = 10^{−6000005} by a finite Gaussian-scale pigeonhole.
- Lead's findings since (E79):
  - The ρ*-extremal shape p = a·q (half-sine autocorrelation) VIOLATES energy-PD: the FT of e has min −0.0094 at
    y ≈ 7.8 for a = ½. So the enlarged class {p PD, e PD, windows} has reach strictly above 4(2 − ρ*)/r ≈ 6.63.
  - E80 (lead, running) estimates that class's reach by SLSQP over autocorrelation profiles; results land in
    examples/e80/. Do not wait for it.
- Lead's synthesis of the macroscopic limit (NOTEBOOK cont. 11 §2):
  - For every continuous 0 <= H <= 1 on T, the marginal t ↦ H(0)²p(t)² + ∫H²dσ_t (σ_t = the residual's local
    spectral measure, total mass e(t)) is PD and front-loaded.
  - For the shape-independent family σ_t = e(t)ν, this reduces to "p PD, e PD, windows on p and e".

## Task 1 (main): the exact reach of the macroscopic limit, and the theorem that goes with it
1. Completeness audit. List every positivity statement that survives the macroscopic limit of a dense counterexample
   sequence, and decide which of them can constrain the shape-independent family:
   - P31 windows of all filtered functions;
   - product windows (autocorrelations) of all filtered functions, including cross products (H₁f + M)(H₂f(· + y) + M)
     >= 0;
   - triple product windows (T + m)(T(· + y) + m)(T(· + z) + m) >= 0;
   - P53/P48 twisted atoms with local Bessel, TL1/SG;
   - the binary identity σ_t(T) = p − p².
   Is the shape-independent family optimal for the adversary? Are there constraints coupling p and e beyond
   "both PD + windows" (e.g. through the identity e = p − p², or Schur-product facts)?
2. Compute the reach C₉ := 1/sup d over the admissible macroscopic class (the audit's class, or at least {p PD, e PD,
   both windows at every θ, 0 <= p <= 1}). Use Gurobi on piecewise-linear profiles. PD of e = p − p² needs a careful
   exact treatment: the FT of p² is the autocorrelation of p̂. Use a certified interpolation/aliasing bound or exact
   piecewise-quadratic transforms. Report the extremal profile and which constraints are tight.
3. Prove T-dense(C) for C as close to C₉ as you can, with exact certificates. For example, prove a joint
   doubly-positive inequality ∫p² <= ρ₂·a·d valid when p, p(1 − p) are both PD and a <= ½, with ρ₂ < ρ*. Then
   d <= r/(4(2 − ρ₂)). Or optimise directly over a and the window conditions. Exhibit an exact obstruction witness
   (PD p, PD e, all windows) at the numerical reach, as round 7 did.

## Task 2: effective constants on the proved range
- Extend the explicit-constant proof (P59.6) from C = 3 to every C < 4/r (= 5.196 with Beckner, 4.93 with elementary
  r = 0.811). That range needs only the density window plus finite energy-PD (EM).
- If possible, extend to C < 4(2 − ρ)/r. That needs a finite, robust version of the doubly-positive gap for the smoothed
  profile q_s, which is PD up to the regulariser 2M·k_s, and of the energy window.
- State each theorem with its explicit constant. Say precisely which lemmas a Lean formaliser needs (Gaussian/Poisson:
  mathlib has the Jacobi-theta transformation; P31-E is already kernel-checked in this repo).

## Task 3 (if time remains): beyond the macroscopic reach
- Use the Task-1 extremal profile as the adversary. Beyond C₉ a counterexample must carry its residual energy in
  mesoscopic spikes (P40 applied to every filtered function) whose aggregated marginals are PD and front-loaded.
- Identify the single missing mesoscopic inequality, or a two-scale formal escape, as precisely as possible.

## Deliverable
The macroscopic reach C₉ (numerical, with an exact witness), T-dense(C) for C as close to C₉ as proved (certificates),
explicit constants on the effective range, and for Task 3 the precise mesoscopic gap. Say exactly what is new versus
quoted.
