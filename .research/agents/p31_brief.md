# Brief: adversarial review of P31 and a rigorous Nikolskii-constant lemma (codex agent, Sol 6.1 xhigh)
(lead, 2026-10-19)

## What to review
Read `.research/PROOFS.md` sections P29 and P31 (and P17 for the doubly-positive constant). The lead claims:

**P31.** Notation:
- A ⊂ Z_{>0} finite, X = max A, n = |A|, M = −min_x Σ_{a∈A} cos(ax).
- w >= 1 an integer, κ(k) = (1 − |k|/(w+1))₊, W = Σ_k κ(k)², S_A = Σ_{a∈A} κ(a)², L = X + w.
- ρ_L = sup ‖v∗v‖₂² / ((L+1)‖v‖₂⁴) over v >= 0 on {0..L}. Equivalently ‖U‖₄⁴ <= ρ_L(L+1)‖U‖₂⁴ for trigonometric
  polynomials of degree <= L.

Claim:

    W(n/2 + M²) <= ρ_L (L+1) (M² + S_A/2).

Proof idea:
- h = F_{w+1}(x − x₀)(f_A + M) >= 0 has degree <= L.
- Fejér–Riesz gives h = |U|².
- Apply the Nikolskii-type bound to U.
- Integrate over x₀.

Claimed consequences:
- (i) M >> √n for every A whose Fejér²-weighted density in [1, εX] is below (1 − η)·2δ/ρ (δ = n/X).
- (ii) Dense Chowla: |A| >= (ρ/2)(1+ε)(1+η)X ⇒ M >= c√n.
- (iii) Any family with M/√n -> 0 is front-loaded beyond 2δ/ρ at every fixed scale ε.

Numerics: ρ_L ≈ 0.687 for L ~ 120 (E48, src/scratch/rhoL.py).

## Tasks
1. **Adversarial check of P31 itself.**
   - Check every step: degrees, Fejér–Riesz, the x₀-integration identities, and the normalizations
     (1/2π)∫ s² = M² + S_A/2 and W = (1/2π)∫F².
   - Check consequences (i)–(iii) with explicit constants, including how d_ε and δ enter, and whether the small-ε
     and ε = 1 regimes are stated correctly.
   - Test numerically on adversarial sets: intervals; random sets; triangle/(1−t)^p tapered sets; Bu/Singer sets
     (examples/singer_bu/certified.json, src/bu.py); lacunary sets; core + sparse tail; the dense records
     (examples/construct/N50_certified.json).
   - Report any counterexample to the inequality (that would mean an error), and how the implied bounds compare
     with true M.
   - Check whether P31 or an equivalent statement is already in the literature, especially dense-set Chowla in Z
     and "Nikolskii + Fejér–Riesz" averaging arguments.
2. **Lemma P31-N, rigorous.** Prove ρ_L <= A_{4/3}⁴ + o(1) = 0.7698 + o(1) with an explicit rate.
   - Lead's sketch (PROOFS P31 "Status"):
     - embed h(t) = Σ_j u_j e^{ijθ} B(t − j), with B̂ a smooth square-root partition of unity equal to 1 on
       [−π + 1/T, π − 1/T];
     - choose θ to keep |U|⁴ out of the aliasing bands;
     - apply Beckner's sharp Young inequality plus Hölder on supp h, truncating B at length O(T log T).
   - Write it out with all error terms. Then give an explicit uniform bound valid for ALL L >= 0 (even a crude one
     like 0.95; the lead sketched a cumulative-mass/Cauchy–Schwarz argument). Make the combination explicit:
     "ρ_L <= ρ̄ for all L >= L₀" plus the finite range.
   - If you can, find the true ρ_∞ (≈ 0.687?) or a rigorous upper bound below 0.7698. One option: an SDP/Lasserre
     certificate for small L combined with a monotonicity argument. Gurobi (non-convex QCQP) or an SDP solver on the
     VM may help. State exactly what is certified.
3. **Push P31 toward the escape class** if 1–2 go well. Attempt a multi-scale or effective-degree version, in which
   a sparse tail of A does not inflate L + 1. Target: front-loaded sets such as dense core [1, Y] plus sparse tail up
   to X >> Y, or profiles (1−t)^p with p >= 2. Even a precise obstruction is useful.

## Rules
- All computation on the GCP VM dirichlet via `src/dirun.sh` (see its header). Use at most `-c 4`.
  - Gurobi 13.0.3 (full licence, gurobipy in the VM venv) for any MILP/LP/QCQP.
  - Write C for anything heavy. Never compute on the laptop beyond trivial checks.
  - Never touch the VM fejer. Never kill processes you did not start.
- Edit only `.research/agents/p31_report.md` and files under `.research/agents/p31_scratch/`. Do not edit other
  .research files. Do not commit.
- Label every claim PROVED (full proof, constants), NUMERICAL (code path, seed), CITED (exact statement and source),
  or CONJECTURED.
- Write the report early and overwrite it as you go.
- If you find an error in P31, say so at the top of the report with the smallest counterexample.
