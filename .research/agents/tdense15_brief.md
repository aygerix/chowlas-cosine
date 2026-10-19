# Math brief (codex research agent), round 15: verify P66; then break the cyclic ¼ barrier through the stability of its equality case

You are a research mathematician working on Chowla's cosine problem in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine.
- Read CLAUDE.md first: conventions, honesty labels, and the rule that numerics are not proofs.
- Conventions: f_A = Σ_{a∈A} cos(ax), M(A) = −min f_A, n = |A|, X = max A.
- Rules (unchanged):
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents. No LaTeX; markdown only.
  - Report: `.research/agents/tdense15_report.md` (keep it current). Scratch: `.research/agents/tdense15_scratch/`.
  - Computation ONLY on the VM via `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 ...` (at most 4 cores). The VM has
    bash, not zsh: wrap shell loops in `bash script.sh`.
  - Gurobi for every LP/MILP/QP. SDPs, if any, use Clarabel or SCS through cvxpy; mosek is not installed.
  - Label every claim PROVED / NUMERICAL / HEURISTIC / CONJECTURED, with exact quantifiers.
  - Grep .research/PROOFS.md before any novelty claim.

## State (read PROOFS P61–P67, NOTEBOOK cont. 17–18, EXPERIMENTS E93–E96)
- Dense integers.
  - T-dense (exponent ½): C < 7.722 (P63).
  - NEW exponent 1/3 for C < 13.2548 (P66 + E94b). Ours; not yet independently checked.
  - Bu et al.: ¼ for every C.
- Cyclic half-sets (q prime, B = −B, 0 ∉ B, |B| = (q − 1)/2, λ(γ) = Σ_{b∈B} e(γb/q), K = −min_{γ≠0} λ,
  Λ = max_{γ≠0} λ).
  - The second-order bound is Λ <= √(2q)K + 1. With Parseval's ΛK >~ q/4 it gives K >~ q^{1/4}.
- Round 14 (P67): every Sanders-type transfer ends at ¼, through the norm estimate ‖P^{(r)} − F^{(r)}‖ <= rKL^{r−1}.
  - Sanders' half-set "1/3 by careful accounting" was NOT reconstructed in the small-spectrum branch (all nonprincipal
    coefficients < m/32).
- Barriers you must respect: R12-S (scalar moments cap at 1/3); R13-C and R13-M2 (partial convolution and
  fixed-order arithmetic are consistent with 1/3); R13-PK (PK false).
  - E96: degree-3 SOS / Sherali–Adams gives K = O(1), through two-point pseudo-marginals. Do not use low-degree
    symmetric SOS.

## Part A (bounded, at most about 25% of your effort): adversarial verification of P66 and E94b
1. Re-derive P66 (PROOFS) step by step and try to break it. Check in particular:
   - (a) The weak limit of the cubes r³ under the diagonal h = εX.
     - q -> k_ε⋆p uniformly; then r·(1 − 3q + 3q²) and g(q) converge weakly; then ε -> 0.
     - Is the limit of the cubic profile g(p), with no leftover cross term?
   - (b) The PD closure under these limits, and the error 4m³/X: is the normalization of ĥ and of m right?
   - (c) The front cap (step 5): continuity of p, "g∘p PD ⇒ g(p(t)) <= g(p(0))", and the IVT argument.
     - Note P59.1 gives a <= ½. Is p(0) = max p actually needed, or only p(0) <= ½?
   - (d) Step 6: P61 with φ(σx), σ = 4e(0) <= 2/3.
     - p = φ(4e) needs p <= ½. Check the Jensen step over the Gabor mixture, and that D_σ is monotone in σ.
   - (e) E94b: re-run `src/e94b_mix_certify.py` and certify the mixing inequality by a DIFFERENT method. For example,
     reduce G(x) >= 0 to a polynomial inequality by squaring with sign bookkeeping, then use Sturm or exact
     isolation.
   - Then check that D_{2/3} <= α1·(259/2000) + α2·(2√3/9) is a valid use of P63 and Beckner on the SAME class 𝒲.
2. Port the P63 certificate to σ = 2/3 (mechanical).
   - `src/e95_discover_sigma.py` is the discovery LP, saturating at D_{2/3} <= 0.0723.
   - The certifier is `examples/r11_certificates/certify.py`.
   - Produce an exact rational certificate of D_{2/3} <= 0.073, i.e. P66 for C < 13.69, or explain the obstacle.
   - Report the certified constant.
3. Deliverable: a verdict per step (CORRECT / GAP with an explicit fix / WRONG with a counterexample), plus the
   certified constant.

## Part B (main): stability of the equality case of the cyclic ¼ argument ⇒ an exponent > ¼ for half-sets
Read NOTEBOOK cont. 18.5 first; it contains the lead's analysis. Summary (verify it):
- Decompose b − ½ = P̌ − Ň, with P = λ⁺ and N = λ⁻ on γ ≠ 0. Both are PD on the physical side.
- Equality in "Λ <= √(2q)K together with Parseval" forces four things:
  - (i) N ≈ K on almost all γ, so Ň ≈ Kδ_0;
  - (ii) the positive spectrum Π has |Π| ≈ 4K², with heights ≈ q/(4K);
  - (iii) off x = 0, P̌ = b − ½ = ±½ (flat), with NONNEGATIVE coefficients on Π;
  - (iv) P̌² ≡ ¼ off 0. So Σ_{γ+β=ξ}c_γc_β is the same for every ξ ≠ 0: a weighted symmetric (reversible) perfect
    difference set in Z_q. This needs |Π|² >= q − 1, which is exactly K >~ q^{1/4}.
- Exact versions are impossible:
  - two-valued spectra are Galois-forced into Q(√q) with EQUAL multiplicities (Paley);
  - cyclic reversible difference sets are classically trivial. Find the precise reference or a proof.
- So the ¼ bound is never tight in Z_q. The task is to make that QUANTITATIVE.

Tasks.
1. Make the equality-case analysis rigorous and quantitative.
   - State a stability lemma of the form:
         if K <= δ q^{1/4}·(large constant) and Λ >= c q/K, then (i)–(iv) hold up to errors controlled by explicit
         powers of q and K;
     or, better, a defect-sensitive version of the second-order bound:
         Λ² <= 2qK²·(1 − Δ) + O(Λ),
     with an explicit defect Δ measuring the deviation from (i)–(iv).
   - Track every error term. Note the c = 0 spike: Ň(0) ≈ K carries all of Ň's L² mass. Avoid any step that is
     defeated by it; cont. 17.7(c) records such a slip.
2. Show that the approximate configuration (iii)–(iv) is impossible beyond some threshold. Candidate tools:
   - POSITIVITY of the coefficients c_γ: there is no cancellation in P̌², so (P̌²)^ >= 0 pointwise;
   - flatness |P̌| ≈ ½ off 0, with only |Π| ~ √q frequencies. Compare large-sieve, Turán-type or Nazarov-type
     inequalities for sparse exponential sums, and uncertainty principles in Z_p (Tao 2005: |supp f| + |supp f̂| >= p + 1);
   - Galois / algebraic integrality of λ(γ), and the unequal-multiplicity requirement;
   - the exact off-zero identity Σ_{β≠0,γ} λ(β)λ(γ − β) = λ(γ) at γ ∈ Π + Π, not only at 2γ.
   - The goal is an explicit exponent θ > ¼ with K >~ q^θ for every symmetric half-set, or QU(β) with β > 1 in the
     sense of P65.
3. Adversarial checks before investing.
   - Test each intermediate lemma on Paley sets (K ≈ √q/2) and on E41/E90 optima (examples/zp_half/,
     examples/e90/; dilated near-intervals with Λ ≈ 0.27q).
   - Test on R14-UNION-type and R13-PK-type random profile sets.
   - Test on the R12-S / R13 fakes. They are not Boolean, so (iii) cannot hold for them: say exactly which step uses
     Booleanity.
   - Numerically (VM), for exact small-q data, measure how far the optima are from (i)–(iv): the fraction of γ with
     λ ≈ −K, |Π|, and the flatness of P̌ off 0.
4. If a half-set exponent θ > ¼ is proved:
   - attempt the fixed-density version (density α, with the (1 − 2α)qλ term of P67 item "density-dependent
     second-order equation");
   - state the integer corollary via q ∈ (4X, 8X] (P67.4), with the uniformity caveat.
5. If it fails: give the exact obstruction.
   - Ideally a Boolean or near-Boolean configuration that is approximately (i)–(iv) at K ~ q^{1/4}·polylog.
   - Otherwise a precise statement of which additional estimate is missing.
   - Preserve every failed step with its counterexample.

## Deliverable
- Part A: per-step verdicts and the certified D_{2/3} constant.
- Part B: a theorem (exponent > ¼ for cyclic half-sets, or QU(β > 1)), a conditional theorem with a single named
  missing lemma that survives all the adversaries above, or a precise obstruction.
- Say exactly what is new versus quoted.
