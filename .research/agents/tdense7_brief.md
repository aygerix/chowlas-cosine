# Math brief (codex research agent), round 7: the C₁ programme — prove T-dense for every box ratio C <= 3 (or beyond)

You are a research mathematician working on Chowla's cosine problem in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine.
- Read CLAUDE.md first: conventions, honesty labels, and the rule that numerics are not proofs.
- Conventions: f_A = Σ_{a∈A} cos(ax), M(A) = −min f_A, n = |A|, X = max A.
- Rules (unchanged):
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents. No LaTeX; markdown only.
  - Report: `.research/agents/tdense7_report.md` (keep it current). Scratch: `.research/agents/tdense7_scratch/`.
  - Computation ONLY on the VM via `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 ...` (at most 2 cores).
  - Gurobi (gurobipy) for any LP/MILP/QP (NonConvex=2 for bilinear terms).
  - Label every claim PROVED / NUMERICAL / HEURISTIC / CONJECTURED, with exact quantifiers.

## Target
T-dense(C): there is c(C) > 0 with M(A) >= c(C)√n for every finite A ⊂ Z_{>0} with max A <= C·|A|.
- Known (ours):
  - P31 is kernel-checked. The dense theorem gives T-dense(C) for C <= 1/0.41 ≈ 2.44, i.e. |A| >= 0.41·max A
    ⇒ M >= √|A|/1000. The threshold is 2.466 with the numerical Nikolskii constant.
  - Classical (Kolountzakis 1996, our P29): linear M for density > 1/2.
- Goal of this round: the FIRST extension of the dense theorem. Prove T-dense(3), i.e. Chowla for every A with
  |A| >= max(A)/3, with an explicit (preferably effective) constant. If that falls quickly, push C as far as the
  method allows. If it fails, give the exact obstruction at the smallest C where it fails.
- Read first:
  - PROOFS P29, P31 (+ P31-C), P36, P38, P44, P47, P49, P53.
  - NOTEBOOK "2026-10-19 (night, cont. 6)": the candidate theorem "P31 + P47 ⇒ T-dense for C < C₁"; the explicit
    escape set at C ≈ 4–7 (random dense front + sparse tail) and why it still has M >= c√|front| ("dip filling").
  - EXPERIMENTS E70/E70b/E72/E72c: P47 window family numerics.
    - E72c: at C = 3 the Pareto search shrinks max A back into P31's range, i.e. no escape was found.
    - At C = 6 and 10, box-filling escapes exist with R ≈ 0.9–1.3.

## Why C <= 3 looks closable (lead's θ → 0 computation; check it, make it complete)
Write p for the macroscopic density profile on [0,1] (positions a/X), p̄ = ∫p = n/X >= 1/C, e = p(1 − p), ē = ∫e,
and ρ = 4/(3√3).
- P31 fails at every small window only if p(0) >= (2/ρ)p̄ (front density). At C = 3 this means p(0) >= 0.866.
- P47 fails at every small window only if e(0) >= (2/ρ)ē (front rounding energy).
- Together at C = 3: e(0) <= 0.866·0.134 = 0.116, so ē <= 0.0447. The profile is nearly 0/1.
  - Example front + tail (front [0, φ] at density p_f, tail density d_t): escape at θ → 0 forces (at p_f = 0.9) φ >= 0.369 and tail
    mass <= 0.0015X (<= ~0.002X over all p_f ∈ [0.866, 1]). The set is then a near-interval front (density >= 0.87 on [1, φX]) plus a few far elements.
  - Such sets should have LINEAR M (interval sidelobes, P29/P49-type), unless the front's internal profile is itself
    graded, which the profile-level window conditions already see.
- At C ≈ 4–7 the front can be fractional (random half) and the window family genuinely fails (NOTEBOOK cont. 6).
So the natural theorem is T-dense(C) for C < C₁, with C₁ the reach of: P31 + P47 at every scale and model
+ P36 truncation + a quantitative near-interval / near-0/1-profile lemma.

## Task 1 (main): prove T-dense(3)
A complete proof for EVERY A with max A <= 3|A| — not only roundings of fixed profiles. Ingredients to make rigorous:
1. Model selection. For an arbitrary A, choose a model profile P (Lipschitz, or piecewise C² with jumps) with small
   prefix discrepancy D₀ (P47's error term is C(p)(1 + D₀²Q₂)). Uniformity in the Lipschitz constant / number of
   jumps is the delicate point. If no model with D₀ <= X^{3/4−} exists, A has block structure at scales >= X^{3/4}.
   Prove a BLOCK LEMMA for that case: blocks of length L give M >~ L·(something), via Dirichlet sidelobes of the blocks
   against the block-centre exponential sum. The lead's heuristic is M >~ 0.5√(nL).
2. Window failure at ALL θ (not just θ → 0) for P31 and P47 simultaneously ⇒ the macroscopic profile is within
   O(η) of a 0/1 profile with mass near the front. Quantify this.
3. Near-0/1 profile lemma (effective): if the profile is within η (in L¹ of e) of an indicator of a finite union of
   intervals with front mass, then M >= c·X — or at least c√n — directly. P29 (Fejér grid), P36 (cut far tails at
   gaps), interval sidelobes. Watch the "front + sparse far tail" sets: the tail can have up to ~0.002X elements
   spread over [φX, X], so removing it costs up to linear M. Use dip-filling: a tail of size o(front) cannot fill
   the front's linear sidelobe dip.
4. Assemble: an explicit c(3) (any positive effective constant is a success; ineffective via P49/P53 compactness is
   a weaker success — label it).
Falsification first: before investing, search adversarially (VM, annealing or Gurobi) for sets A ⊂ [1, 3n] whose
best P31/P47/P29/P36 certificate is tiny. E72c's code (src/e72c_*.c, src/e72_p47_pareto.c) is a starting point.
Report the worst sets found and what certifies them.

## Task 2: the reach C₁* of the method
- Formulate the profile-level escape problem: the smallest C for which some profile p (∫p = 1/C, support reaching 1)
  defeats P31 and P47 at every θ AND every alternative model, and is not near-0/1 (so no linear-M lemma applies).
- Compute it numerically: discretised profiles, Gurobi NonConvex=2 for e = p(1 − p).
- Report C₁* and the extremal escaping profile. Realise that profile as actual sets (cumulative rounding, random
  rounding) at n = 512–4096 on the VM, and report R (FFT minimum + refinement).
- Is the escape set at C₁* a small-R mechanism (construction lead) or Chowla-safe for another reason (dip filling)?
  Say which.

## Task 3 (only if Tasks 1–2 settle): beyond C₁*
- At the reach limit the escaping sets have a fractional front and a sparse tail (cont. 6 at C ≈ 7). The lead's
  "dip filling" heuristic: the tail B cannot fill the front's dips unless |B| >= 2c²|D_F||F|.
- Make dip filling a lemma for "dense front F ⊂ [1, φX] with P31-certified M(F) >= c√|F| plus arbitrary tail B ⊂
  (φX, X] with |B| <= δ|F|". Does it give T-dense(C) for larger C?

## Deliverable
A theorem T-dense(C₀) with C₀ >= 3 and a complete proof (effective constant if possible), or the precise obstruction
with a numerical witness. Also the computed reach C₁* with its extremal profile. Say exactly what is new versus quoted.
