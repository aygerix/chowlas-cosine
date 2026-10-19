# Math brief (codex research agent), round 18: correlated roundings — low window variance at every scale vs a sharp boundary somewhere

You are a research mathematician working on Chowla's cosine problem in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine.
- Read CLAUDE.md first: conventions, honesty labels, and the rule that numerics are not proofs.
- Conventions: f_A = Σ_{a∈A} cos(ax), M(A) = −min f_A, n = |A|, X = max A, S = A ∪ (−A), K = 2M.
- Rules (unchanged):
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents. No LaTeX; markdown only.
  - Report: `.research/agents/tdense18_report.md` (keep it current). Scratch: `.research/agents/tdense18_scratch/`.
  - Computation ONLY on the VM via `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 ...` (at most 4 cores; bash, not
    zsh).
  - Gurobi for every LP/MILP/QP. SDPs, if any, use Clarabel or SCS via cvxpy.
  - Label every claim PROVED / NUMERICAL / HEURISTIC / CONJECTURED, with exact quantifiers.
  - Grep .research/PROOFS.md before any novelty claim.
- GOAL: a PROOF of Chowla (M >= c√n for ALL finite A). Your round-17 report is the starting point.

## State (read PROOFS P28, P29, P41, P63, P70; NOTEBOOK cont. 19 incl. corrections 10–11; STATE's newest block; E66, E99, E99b/c; your tdense17_report.md)
Under M <= ε√n, a counterexample must SIMULTANEOUSLY satisfy (P70.5):
- (i) P28-spikiness: every triangular window with relative energy has small "spread" η. Equivalently, its window sums
  have unusually small L¹ norm for their L² norm.
- (ii) many additive triples: e >= (1/(3ε) − 2ε/3)n^{3/2};
- (iii) no √n-scale bulk in Cay[A];
- (iv) no sharp ambient boundary: c₀k − D_d(k) <= ε√n for every d, k (P70.2).
Already excluded:
- independent roundings of any profile with window variance >~ μ (P70.3, w.h.p.);
- cumulative (Sturmian) roundings of fixed curved profiles (P41; E66 shows R ≈ 1.4–3);
- sets with a sharp boundary (P70.2);
- dense sets with max A <= 7.72n (P63).
The remaining adversary is a CORRELATED (selected) set at vanishing density.
- It must hide its P28 window variance, so it is locally "deterministic".
- It must have no sharp edge in any A_d = {a/d : d | a} at any scale k >~ √n/c₀.
The user wants to know whether the four conditions are genuinely INCONSISTENT for small ε (real progress), or only
an equivalent restatement of Chowla (no progress). Decide which.

## Task 1 (adversary first): build or rule out the remaining adversary
Attempt explicit constructions that satisfy (i) and (iv) together while keeping M small. Measure every certificate,
including the full P9 on W2 = {0} ∪ ±A and max_{d,k}(c₀k − D_d(k)).
Candidates:
- multiscale nested Bohr / Beatty roundings with smoothly varying slopes;
- cumulative roundings at vanishing density (E66's mechanism, rescaled sparse);
- dilation unions ∪_j d_j·A_j of tapered pieces (each A_d then sees only one piece);
- Singer–Bu-type algebraic sets with tapered windows;
- forced-prefix families thinned to vanishing density;
- correlated "antithetic" roundings designed to cancel window variance.
For each: if all four certificates are o(√n) along the family, that is the decisive obstruction. VERIFY it with
certified M before claiming. If every attempt fails, identify the exact mechanism that defeats it.

## Task 2 (proof): low window variance at every scale ⇒ a sharp boundary or √n
Target lemma TAPER(c), CONJECTURED: for every finite A, either
- some P28 window certifies M >= c√n, or
- there exist d, k with k >= √n/c and D_d(k) <= c₀k/2,
- or the star/bulk certificates give c√n.
Route suggestions:
- Small P28 L¹/L² ratio on a window means the window sum Σ w_a e^{iax} is concentrated on a small x-set. Use the
  uncertainty principle / large sieve to show its mass sits near few frequencies x_j. Then A is locally close (in L²)
  to Σ_j c_j(a) e^{−iax_j} with slowly varying c_j.
- Booleanity then forces local Bohr-set structure. Combine with P29(b)/P48 at the right scale, and with the
  sub-multiplicativity of spikes (cont. 19.5(a)): spikes form an approximate group.
- Then show the Bohr window, after dilating by the denominator d of the relevant x_j, produces a sharp boundary in A_d.
- Track every loss in ε. We need constants independent of n. A loss per scale over log n scales is fatal unless it is
  summable.
- If the lemma is false, give the counterexample family from Task 1.

## Task 3: the equivalence check (the user's question)
State precisely whether conditions (i)–(iv) at small ε are:
- (a) provably inconsistent (a proof), or
- (b) consistent for some explicit family (a Chowla counterexample, or at least one that defeats this programme), or
- (c) EQUIVALENT to "M <= ε√n" in a precise sense, e.g. every set with M <= ε√n is reducible to one satisfying
  (i)–(iv) and conversely. Give the reduction, or show it fails.
Answer (c) honestly, even if the answer is that the programme is circular.

## Deliverable
The report contains one of:
- a theorem;
- a conditional theorem with ONE named lemma surviving all adversaries;
- a precise obstruction (an explicit family with certified certificates).
Also include adversarial tables, the Task 3 verdict, and a strategic recommendation. Say exactly what is new versus
quoted.
