# Math brief (codex research agent), round 13: the cyclic peak problem through full convolution; binary escapes

You are a research mathematician working on Chowla's cosine problem in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine.
- Read CLAUDE.md first: conventions, honesty labels, and the rule that numerics are not proofs.
- Conventions: f_A = Σ_{a∈A} cos(ax), M(A) = −min f_A, n = |A|, X = max A.
- Rules (unchanged):
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents. No LaTeX; markdown only.
  - Report: `.research/agents/tdense13_report.md` (keep it current). Scratch: `.research/agents/tdense13_scratch/`.
  - Computation ONLY on the VM via `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 ...` (at most 4 cores). The VM has
    bash, not zsh: wrap shell loops in `bash script.sh`.
  - Gurobi for every LP/MILP/QP.
  - Label every claim PROVED / NUMERICAL / HEURISTIC / CONJECTURED, with exact quantifiers.
  - Grep PROOFS.md before any novelty claim.

## State (read PROOFS P61–P64, NOTEBOOK cont. 15–17, EXPERIMENTS E41, and your round-12 report)
- T-dense(C) is PROVED for every C < 2000/259 = 7.722. The second-order reach is 1/D ≈ 8.571.
- Round 12 (P64) pinned the missing ingredient:
  - integer side: CSFG(20) ⇒ T-dense beyond 1/D (R12-B);
  - cyclic side: TBS ⇒ √-strength cyclic half-set Chowla (R12-H + the root filter);
  - scalar moments cannot beat exponent 1/3 (R12-S); the full off-zero convolution (binarity) is required.
- Notation for Task 1. q is an odd prime; B = −B ⊂ Z_q with |B| = (q − 1)/2 and 0 ∉ B (toggling 0 costs O(1));
  λ(γ) = Σ_{c∈B} e(γc/q); K = −min_{γ≠0} λ; Λ = max_{γ≠0} λ; P = λ⁺ and N = λ⁻ on γ ≠ 0.
- Lead's verified facts (P64.12, NOTEBOOK cont. 17).
  - Exact off-zero identity (this IS binarity): Σ_{β≠0,γ} λ(β)λ(γ − β) = λ(γ) for every γ ≠ 0.
  - Parseval: Σλ⁺ <= (K − ½)(q − 1), so Λ >= ((q + 1)/4 − K²)/(K − ½). In Bhatia–Davis form, ΛK >~ q/4; Paley is
    tight with Λ ≈ K ≈ √q/2.
  - Second order: dilate so Λ = λ(1), then read the identity at γ = 2. This gives Λ <= √(2q)K + 1, hence
    K >~ 0.42q^{1/4}. The loss is the mixed-pair bound |Σ_β N(β)P(2 − β)| <= KΣP.
  - R12-H corollary: K = o(√q) ⇒ max_{γ≠0}|λ| = o(q) (Fourier uniformity, via dilation transitivity).
  - Weak limits at order k need K = o(q^{1/k}). So a √q proof must be quantitative at finite q.
  - The spectrum {λ(γ)} is the Galois orbit of α = λ(1) ∈ Z[ζ + ζ⁻¹]. Power sums are additive counts:
    Σ_{γ≠0}λ^k = q·T_k(B) − λ(0)^k.

## Task 1 (main, about two thirds): beat Sanders' 1/3 through the full convolution, or find the exact obstruction
1. Correct the target first. PK(η) (Λ <= CK^{2−η} for ALL half-sets) is probably FALSE.
   - Candidate refutation: profile-modulated textures. Take a smooth PD profile p = ½ + ε·cos(2πt) and a Paley-like or
     other structured texture, giving Λ ≍ εq with K = O(√q·polylog).
   - Energy-PD needs only K >~ ε√q/2, so nothing at second order forbids this. Decide it: a proof or a VM
     construction with certified values of K and Λ.
   - If PK fails, the correct intermediate is quantitative uniformity:
         QU(β): there are C, δ0 > 0 with K <= δ√q, δ <= δ0  ⇒  Λ <= C·q·δ^β.
   - Bookkeeping, which you should check: combined with Λ >= q/(4K), QU(β) gives K >~ q^{1/2 − 1/(2(β+1))}.
     - The finite second-order identity is QU(1), giving exponent 1/4.
     - QU(2) is Sanders' level, 1/3.
     - Any β > 2 is new, and β = ∞ is the √q conjecture.
   - QU only restricts the hypothetical small-δ regime. So it cannot be refuted by sets with K ≍ √q.
2. Main attempt: derive QU(β) with β > 1 from the identity applied at MANY γ at once. Use the structure the
   second-order loss requires.
   - Equality in the γ = 2 bound needs the positive mass P to pair with near-threshold negative values N ≈ K at
     2 − β for essentially every β. Write the analogous requirement at γ = 2, 3, …, J along the orbit of the peak.
   - Then show the pairings are incompatible. Candidate tools:
     - additive energy of the large positive spectrum: from the identity, r_{S+ + S+}(γ) <~ 32K⁴/q off zero, where
       S+ is the positive spectrum at level q/(4K);
     - Chang/dissociativity and Bohr sets;
     - the physical-side decomposition b − ½ = P̌ − Ň (both PD, each of size ~K at 0);
     - the full-Haar kurtosis >= 3/2 for P̌ (P63.5) against kurtosis 1 for b − ½.
       - Lead's check: the naive version is defeated by the c = 0 spike and returns q^{1/4}.
       - Decide whether removing the spike, or bounding max_{c≠0}|Ň(c)|, gives more.
   - Also look for a self-contained new proof of β = 2, i.e. Sanders 1/3. Its mechanism shows what a β > 2 step
     needs.
3. Moment test (bounded). Do the k >= 4 power-sum constraints kill the R12-S fake? These are positivity of
   Σ_{γ≠0}(λ + K)^k, actual integer counts T_k, and integrality and divisibility.
   - If yes: what exponent does the k-moment problem allow? This is a small LP/SDP in the moments; use Gurobi.
   - If no: prove that all scalar power-sum constraints together stay at exponent 1/3, or find the first order that
     moves it.
4. Data (bounded; Gurobi MILP, q <= ~110).
   - Compute the exact trade-off curve Λ_max(κ, q) = max λ(1) subject to λ(γ) >= −κ for all γ ≠ 0, for κ from
     K_min(q) upward.
   - E41 gives K_min for q <= 89 (examples/zp_half/). At K_min the optima are dilated near-intervals with
     Λ ≈ 0.27q and K ≈ 0.49√q, so Λ ≈ 1.1K² there.
   - Report the local shape of the curve. Small-q data cannot probe δ -> 0; say what it does and does not show.
5. Deliverable for Task 1, one of the following:
   - QU(β) or an exponent beyond 1/3 with a full proof;
   - a conditional result with a precisely named lemma that survives the R12-S fake AND the profile-modulated test;
   - a precise barrier: an explicit relaxation that keeps the exact identity at a stated set of γ and is consistent
     with exponent <= 1/3.

## Task 2 (bounded, about one third): binary escapes (construction track)
- P61 is sharp for positivity plus two binary moments: WEIGHTED escapes exist at every density below D ≈ 0.1167. A
  binary realization with M = o(√X) at density d < D would disprove Chowla. One with M ≈ c√X and small c would beat
  the record R <= 0.5537 (STATE).
- Known failures:
  - nearest rounding of Paley escapes costs (X/8)∫w²;
  - deleting qZ costs X/√q (P63.5);
  - periodic local laws with modulus q pay about (X/q)·K_q, so the local structure must live at modulus ≍ X;
  - nested schedules with N = o(√X) are excluded (R12-N).
- Probe: build binary sets A ⊂ [1, X] that follow an E82 extremal profile.
  - The profile: examples/e82/e82.jsonl, N = 320 row with the largest D. Read P61 for the map from w to the density
    profile p, with front a = ½.
  - Local laws, at least three:
    - dilated near-intervals, i.e. E41 optimum anatomy;
    - sub-Paley or Paley textures with q ≍ X^θ for θ ∈ {½, ⅔, 1};
    - spectral error diffusion: choose bits in order to keep the running tapered sum's negative part small;
    - Gurobi-optimized rounding at small X, seeded with the profile.
- Measure M (FFT oversampling plus refinement), R = M/√n and M/√X, for X up to about 2^20 where feasible.
  - Certify any R < 0.56 with ball arithmetic (Arb) as an all-x upper bound; a grid is not enough.
  - Certify every reported dip as an Arb point value.
- Kill criterion: if every family has R >= 0.6 with an increasing trend, record the mechanism that breaks it. Say
  which binary constraint is violated, in the language of P61–P64.

## Deliverable
- Task 1: QU(β) / exponent result, conditional result, or barrier, with full proofs; plus the PK test and the data.
- Task 2: the table (family, X, n, M, R, certificate status) and the mechanism behind the trend.
- Say exactly what is new versus quoted. Preserve every failed step with its counterexample.
