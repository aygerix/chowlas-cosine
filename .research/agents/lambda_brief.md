# Brief: λ-uniform difference multisets, the one live construction mechanism (lead, 2026-10-18 night)

## Why this matters
Chowla's cosine problem asks for f_A(x) = Σ_{a∈A} cos(ax), M(A) = −min f_A and R(A) = M/√|A|. Epoch wants sets with R → 0.
The best known constructions reach R → 1/2 (Bu et al.).

P8 (kernel-checked) says R < 1/2 forces the Fejér–Riesz factor of f_A + M to have weighted mean difference multiplicity
above 2. Reflection symmetry supplies at most multiplicity 2 (Bu's S ∪ −S). Multiplicity ≥ 3 needs non-symmetric
"accidental" coincidences.

The cleanest form of the mechanism follows. Read `.research/NOTEBOOK.md`, entry "2026-10-18 (evening) — λ-fold rulers",
and E35 in `.research/EXPERIMENTS.md` before starting.

**Statement (PROVED, elementary).** Let D ⊂ Z, |D| = k, r(d) = #{(u,v) ∈ D² : u − v = d}, λ ≥ 2 an integer,
A = {d > 0 : r(d) = λ}, Δ = {d > 0 : r(d) ∉ {0, λ}} and W = Σ_{d∈Δ} 2r(d). Then exactly

    2λ f_A(x) = |F_D(x)|² − k − E(x),   E(x) = Σ_{d∈Δ} 2 r(d) cos(dx),

so M(A) = max_x (k + E(x) − |F_D(x)|²)/(2λ) ≤ (k + W)/(2λ), and λ|A| = k(k−1)/2 − W/2.

If for some λ ≥ 3 there were sets with W ≤ εk, then R(A) ≤ (1 + ε)/√(2λ)·(1 + o(1)) < 1/2. If this held for every λ
with an effective construction, it would solve Epoch's problem. E35 (simulated annealing) found:
- λ = 2: Bu-type coherent sets immediately.
- λ = 3 and 4: the exact fraction φ = λ|A|/(k(k−1)/2) DECREASES with k (λ = 3: 0.80 at k = 10, 0.57 at k = 30).
- Every candidate had actual R ≥ 0.68, because E is large exactly where |F_D| is small.

## Your task: settle the λ = 3 case as far as possible, with exact methods and theory
1. **Exact optima (not heuristics).** For λ = 3, and λ = 4 if feasible, compute the exact maximum of φ (equivalently,
   the minimum defect weight W) over D ⊂ [0, L], |D| = k, for small k. Aim for k up to ~12–16, letting L range up to a
   justified bound or reporting L-dependence. Use ILP/SAT/branch-and-bound written in C or a good solver; HiGHS is on
   the VM via highspy, and pysat may be pip-installable in ~/chowla_venv. Report exact optima with proofs of
   optimality (solver status, search completeness), and compare them with E35's SA values
   (examples/lambda_ruler/e35_grid.txt).
2. **Theory: forced defects.** Prove the best lower bound you can on W, or on 1 − φ, for λ ≥ 3 as a function of k.
   - Boundary counting (the largest difference has r = 1, and so on) gives only O(λ²) forced defects; find a real
     mechanism.
   - Natural targets: W ≥ c(λ)·k^{1+δ}, or φ ≤ 2/3 + o(1) for λ = 3. Either would kill this route to R < 1/2 for λ = 3.
   - Alternatively, construct families with W = O(k) for λ = 3, which would be spectacular.
3. **Algebraic candidates.**
   - Test lifts of cyclic difference sets with λ ≥ 3, for example Singer sets of PG(3,q): (15,7,3), (40,13,4),
     (85,21,5), (156,31,6).
   - For every multiplier m ∈ Z_v^* and shift c, form D = {(m x + c) mod v} ⊂ [0, v). Aperiodically,
     r(d) + r(v − d) = λ, so coherence means all λ representations wrap together. Report the best coherent fraction.
   - Also test homometric-triple ideas (NOTEBOOK evening entry) and anything from finite geometry you think of.
4. For any D with φ above the generic level, compute R(A) = M(A)/√|A| numerically. Use a dense FFT grid plus Newton
   refinement; label it uncertified. Also show where E is large relative to the zero set of F_D.

## Rules
- **Compute:** run everything on the GCP VM dirichlet via `src/dirun.sh -c 4 ...` (see the header of src/dirun.sh;
  `python` means the VM's venv). Never compute on the laptop, never touch the VM `fejer`. C sources are compiled on the
  VM inside your scripts (cc -O3 -march=native). Expect another job (an ILP batch of the lead's) to share the VM.
- Label every claim PROVED / NUMERICAL-EXACT (exhaustive or solver-certified) / NUMERICAL (heuristic) / CONJECTURED /
  FAILED. A search that finds nothing is not a proof that nothing exists unless it is exhaustive.
- Edit only `.research/agents/lambda_report.md` and files under `.research/agents/lambda_scratch/`. Do not edit other
  `.research` files and do not commit.
- Falsify early. If λ = 3 near-rulers look impossible, try to PROVE it. If they look possible, try to construct an
  infinite family.

## Deliverable
`.research/agents/lambda_report.md` with:
- exact optima tables;
- any theorems with complete proofs;
- the best candidates, with D listed explicitly;
- refuted ideas;
- the single most promising next step.

Reply with a concise summary when done.
