# Brief: OR(2)-weak in Z — the minimal Z-specific statement behind any run-top improvement (codex agent, Sol 6.1 xhigh)
(lead, 2026-10-18 late night)

## Why this matters
Every universal lower bound M(A) >= c|A|^α currently goes through the run-top chain (Bedert 2509.05260, Shankar
2609.05338): Roth's count T >= n²/K − nK, Shankar's Σ_{t∈A}|B_t| >= T/3, and Bedert's |B_t| << K⁴, giving α = 1/5.
Here B_t = {m ∈ A : m − t ∈ A, m + t ∉ A}, n = |A|, K = M(A) = −min_x Σ_{a∈A} cos(ax).
- In finite groups the exponent 4 is SHARP, even on average over t ∈ A: the O4 construction in Z_4^a has
  |B_t| ~ K⁴ for all t ∈ A (PROOFS P22 and E36b). So any improvement must use a property of Z that groups lack.
- NOTEBOOK "Where a Z-specific run-top bound must come from" reduces the improvement to the 2-run class. Read it first.
  For A = S ∪ (S + t) with S ∩ (S + jt) = ∅ for j = ±1, ±2, an improvement must contain
      **OR(2)-weak: M(S ∪ (S + t)) >= c|S|^{1/4 + δ} for some absolute c, δ > 0.**
  O4 violates the group analogue: every run is a 2-run and K ~ |A|^{1/4}.

## What is known here (do not re-derive; read)
- f_A(x) = 2cos(tx/2)·Re(e^{itx/2}F_S(x)) = |F_S|(cos θ + cos(tx + θ)), with θ = arg F_S.
- Rotation sweep (PROVED): for S = qY with q ≡ 1 (mod t) and q >> t², M(A) >= √((t − [0∈Y])/2) − o(1).
  Reason: F_{qY}(x) = F_Y(qx) is 2π/q-periodic, so the phase tx sweeps independently of F_S.
- A local rotation sweep needs S dense in a short window (the trivial Dirichlet regime). NOTEBOOK (iv).
- P24, localization lemma (PROVED, PROOFS.md): for all m >= H and x₀,
      |Σ_a (1 − |a − m|/H)₊ e^{iax₀}| <= 2M + 2Σ_{a∈A, a<H}(1 − a/H).
  Caution, checked by the lead: for a 2-run set, P24 at scale H << t does NOT separate the two copies of S.
  Shifting x₀ by π/t multiplies both local terms by the same phase.
- Numerics:
  - E38: pair-SA in the class gives R ≈ 0.6.
  - E40: transversal 2-run sets with random tapered levels have M ≈ 5√t.
  - Z is numerically far from violating OR(2)-weak.

## Task
Pick whichever of these you can actually push; report precisely what is proved.
1. **Prove OR(2)-weak for a natural subclass strictly larger than the dilated class S = qY.** Candidates:
   - S with bounded multiplicative spread;
   - S that is t-separated, with a quantitative Diophantine condition;
   - S a union of a bounded number of dilates;
   - S with small doubling.
   State exact quantifiers.
2. **Or prove a conditional/structural theorem.** Example shape: if M(S ∪ (S+t)) <= |S|^{1/4+δ}, then S has a
   specific Bohr-set or almost-periodic structure modulo t. Then show that structure is impossible in Z, or that it
   forces something checkable.
3. **Or find a genuine obstruction**: a Z family of 2-run sets with M(S ∪ (S+t)) <= C|S|^{1/4+o(1)}. That would show
   the run-top route cannot beat 1/4 in Z and redirect the program. Give an explicit construction and certify its
   minimum rigorously (src/chowla.py certify_lower_bound, the arb ball DFT); a numerical minimum is not enough.

## Rules
- All computation runs on the GCP VM dirichlet through `src/dirun.sh` (see its header). Gurobi 13.0.3 with a full
  licence is available there (gurobipy in the VM's venv) and should be used for any optimisation/ILP. Never compute
  on the laptop beyond trivial checks. Never touch the VM fejer.
- The lead is running Gurobi jobs on dirichlet. Never kill or modify processes you did not start. Use at most
  `src/dirun.sh -c 3`.
- Edit only your report `.research/agents/or2_report.md` and files under `.research/agents/or2_scratch/`. Do not edit
  other .research files. Do not commit.
- Label every claim PROVED (full proof written out), NUMERICAL (with code path and seeds), or CONJECTURED. If a step
  uses an outside theorem, state its exact hypotheses.
- Interim report: write the report file early and overwrite it as you go, so partial progress survives.
