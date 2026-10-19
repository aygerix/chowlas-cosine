# Math brief (codex research agent), round 5: finite TL1 and the additive-structure dichotomy

You are a research mathematician working on Chowla's cosine problem in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine.
- Read CLAUDE.md first: conventions, honesty labels, and the rule that numerics are not proofs.
- Conventions: f_A = Σ_{a∈A} cos(ax), F_A = Σ e^{iax}, M(A) = −min f_A, n = |A|, X = max A.
- Rules (unchanged):
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents. No LaTeX; markdown only.
  - Report: `.research/agents/tdense5_report.md` (keep it current). Scratch: `.research/agents/tdense5_scratch/`.
  - Computation ONLY on the VM via `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 ...` (at most 2 cores).
  - Gurobi (gurobipy) for any LP/MILP.
  - Label every claim PROVED / NUMERICAL / HEURISTIC / CONJECTURED, with exact quantifiers.

## Target
T-dense: for every C >= 1 there is c(C) > 0 with M(A) >= c(C)√n for all A ⊂ [1, Cn], |A| = n.
Read first:
- PROOFS P40, P47, P52–P54;
- your round-4 report (.research/agents/tdense4_report.md: P47/P53 verdicts, the defect b >= m³/12, the fixed-complexity
  finite-window QD);
- NOTEBOOK entries "2026-10-19 (night, cont. 2)" and "(night, cont. 3)" (the TL1 dichotomy).

## The lead's new input: P54 (torus level-1 inequality, PROVED)
- Statement: if ψ: K^ → R is a homomorphism with ψ ≡ 1 on a character set Λ, then for every E ⊂ K
  Σ_{λ∈Λ∪−Λ} |1̂_E(λ)|² <= (8/π²)|E|(1 − |E|).
- Proof: L = P_Λ 1_E = Re Z, where Z has a rotation-invariant law (translate along the one-parameter subgroup dual to
  ψ), so Re Z = |Z|cos Φ with Φ uniform. Then a superquantile bound plus Cauchy–Schwarz.
- It also holds for [0,1]-valued g, with p = mean g (realize g as a conditional expectation of an indicator).
- Program (NOTEBOOK cont. 3). In a counterexample, P40 puts almost all energy in tall spikes, at heights >= √(n/ε).
  - If the tall-spike frequency set Λ were "graded-dissociated", TL1 would force >= 19% of the rounding energy off Λ,
    i.e. into the bulk. That contradicts P40.
  - So Λ must carry short UNBALANCED additive relations: torsion (residue classes), or x_s + x_r ≈ x_u-type relations
    (approximate groups / Bohr structure).

## Task 1 (main): finite TL1
State and prove a finite-window version for an actual 0/1 sequence a ∈ {0,1}^Y (or a ∈ {0,1}^X with a slowly varying
profile p_m), at frequencies x_1..x_S with amplitudes c_s = â(x_s).
- Suggested route.
  - W = Σ|c_s|² = (1/Y)Σ_m a_m L_m with L_m = Re Σ_s c̄_s e^{−imx_s}, so W <= Λ_p(L), the empirical top-p superquantile.
  - Use the CVaR dual Λ_p(L) = inf_λ [pλ + E(L − λ)₊] and a polynomial majorant of (u)₊ of degree D.
  - Moments of L involve the empirical moments E[Z^j Z̄^k]. Unbalanced ones (j ≠ k) are weighted counts of near-relations
    Σ_{i<=j} x_{s_i} − Σ_{i<=k} x_{r_i} ≈ 0 mod 2π, at the scale 1/Y.
  - Balanced cross terms are large-sieve terms (separation of the x_s).
- Target form:
  W <= (8/π² + ε_D)·p(1 − p) + C_D·U_D(Λ, c; Y) + (large-sieve error),
  where U_D is an explicit weighted unbalanced-relation count up to degree D and ε_D → 0.
  Make every error term explicit. Handle many small spikes (S large) without exponential dependence on S if at all
  possible. The CLT regime (many small c_s, small additive energy) should give the Gaussian constant 2/π.
- Check it numerically on:
  - Sturmian/Bohr-window sets (the bound must hold, with equality behaviour at a single irrational frequency);
  - random sets;
  - Bu/Singer sets;
  - residue-class sets (TL1 must FAIL there: torsion; make sure your U_D detects it).

## Task 2: the dichotomy, made precise
Combine finite TL1 with P40 (spike domination at heights >= √(n/ε)) to prove a structural theorem of the form:
- if M(A) <= ε√n and A ⊂ [1, Cn], then the weighted tall-spike measure μ = Σ_s |c_s|² δ_{x_s} has an unbalanced
  relation count U_D >= κ(C, D)·n² (or the appropriate normalization), for some D = D(ε) and κ > 0.
Then pursue the structured side:
- (I) torsion: rational spikes 2πr/q with q <= D. Residue-class structure. Combine the dilation pinch (PROOFS),
  P31 on residue classes, and the P53 defect for finite K.
- (II) additive relations: use Balog–Szemerédi–Gowers / Freiman-type structure (cite precisely, with constants) to
  extract a bounded-rank GAP or Bohr structure carrying a fixed fraction of the spike mass. Then apply P53's
  rigidity, with the quantitative defect b >= m³/12 and your fixed-complexity QD.
Identify exactly where constants degrade. Does the argument close for small ε, or does it need a recursion (growing
rank)? If it needs a recursion, state the single missing inequality.

## Falsification first
- Bu/Singer sets (src/e67_zoo.py bu(q)): no tall spikes, so the dichotomy must be vacuous there. Check this.
- E68/E72 near-optimal dense sets (examples/e68, examples/e72): measure their tall-spike sets and relation counts.
- Bohr-window and residue-pattern sets: linear M, and the dichotomy must land in (I)/(II).

## Deliverable
A proved finite TL1 with explicit errors (main deliverable), plus a proof of T-dense, a precise single missing lemma
with evidence, or a rigorous obstruction. Say exactly what is new versus quoted.
