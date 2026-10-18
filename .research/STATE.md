# STATE — current targets and honest status (updated 2026-10-18, session 1)

## Targets
- (C) Epoch: algorithm solution(c,n) for all c>0 — requires R(A_k) -> 0. NOT ACHIEVED. No solution.py exists.
- (L) Chowla: M(A) >= c0 sqrt|A|. NOT ACHIEVED. Best known: >> n^{1/5} (Shankar 2609.05338, cited, checked).
- NEW working hypothesis **C½**: M(A) >= sqrt|A|/2 for ALL finite A (sharp by Bu et al.). CONJECTURED; evidence in
  NOTEBOOK 2026-10-17 late. If true, Epoch's algorithm cannot exist. Not assumed: both tracks stay open.

## Best certified constructions (ours; ball-arithmetic certificates, E2/E4)
- Small-N optimizer agent (src/smallN_search.py, examples/smallN_runs/sa_best_raw.json), arb-certified by lead
  2026-10-18: N=29 max 44 R <= 0.57665; N=24 max 37 R <= 0.57692; N=27 max 43 R <= 0.57735 (min = -3 at x = π);
  N=32 R <= 0.57966. BEST FINITE R KNOWN TO US: 0.5767.
- Dense SA (E6, src/dense_sa.py): N=20, max 30, R <= 0.6011 (= exact box optimum for lam=2.7 by MILP);
  N=34, max 49, R <= 0.6043; N=54 R <= 0.6403; N=73 R <= 0.6730; N=122 R <= 0.6942.
- Bu et al. reproduction (E4): N=6320, max 432979, R <= 0.6573 (approaches 1/2 from above; excess ≈ 1.3 sqrt k).
- Exhaustive box optima (agent; [1,40]/[1,100]): N<=17, R >= 0.6137 (N=16).
- No finite set with R < 0.576 found by any method. Nothing below 1/2.

## Proved here
Paper: P1 Fejér–Riesz; P2 probabilistic; P3 projection Z^k->Z; P4 no exact t>=2 uniform difference sets (torsion-free);
P5 M(A∩B) <= 2M(A)M(B); P6 energy/third-moment bounds; P7 cube framework; P8 weighted-multiplicity bound
(R < 1/2 needs FR-support coherent multiplicity > 2); P9 induced-subgraph lemma M >= -λ_min(Cay[W])/2 (star bound);
gain identity Γ(1-L) = 1/(2R^2).
KERNEL-CHECKED (Lean 4, mathlib pin 0df444a, axioms propext/choice/Quot.sound only, no sorry; re-verified by lead):
difference-set square identity; Sidon consequence f_{D-D} >= -|D|/2 with |D-D|_+ = k(k-1)/2; mean-zero and
Parseval; P5 intersection lemma; P7 cube identity + vertex minimum.  NOT formalized: P1 (Fejér–Riesz absent from
mathlib), P6, P8, P9, P7 admissibility count.

## Heuristic
H1 Wick model (degree-2 chaos optimum = 1/2 = Bu). Dense-regime "rounding" heuristic: R ≈ sqrt(κ/(2 μ̄)) IF the
rounding error of a positive-definite profile (variance fraction κ ≈ 1/3 for the triangle) could be realised as a
coherent autocorrelation — this is the only mechanism found that would beat 1/2; no realisation known.

## Refuted / killed routes (keep)
Cube vertex framework (R_cube >= 0.8165, k<=8 exact ILP); A_{k-1} root squares; quarter-integer trick; fractional
decomposition; dithered Fejér/Beatty; error diffusion (R>1); separated-block unions (strictly worse); local SA from
Bu seeds (strict local optima: 61_12, 101_20, 199_40); Sidon "lower-flat" polynomials (min|F_D|^2/k: 0.10 at k=5 ->
0.0017 at k=16; 0.293 needed to beat 1/2).

## Active lines (>= 3)
1. [construction / C½ falsification] exact fixed-size box MILP (src/box_minlam.py, highspy, warm starts) around the
   small-N minimum R ≈ 0.577 (N ≈ 24–29): is the box optimum lower? Any certified R < 1/2 kills C½.
   Lead for an escape (only one found): a NON-WICK, nearly two-valued value distribution, as realised in Z_p by aligned
   cyclotomic classes (E10: R_p = 0.416/0.368/0.313 for m = 3/4/6) — needs an identity valid on all of R (E11: naive
   lifts and model sets fail).
2. [lower bound] (a) averaged Bedert–Shankar boundary bound Σ_t |B_t| << nK^3 => K >> n^{1/4} (agent running);
   (b) C½ on classes: SNZ (Sidon near-zero) conjecture => C½ for Sidon differences and for the whole Bu class (P13).
3. [obstruction] multiplicity barrier (P8, gain identity, consistent-thinning heuristic); dissociated classes proved
   (P10–P12); finite-vs-Z contrast (E10) shows any proof of C½ must use continuity/torsion-freeness.

## First concrete next step
Read examples/box_minlam/X40_n24.log and X45_n27.log (fixed-size MILP, launched 2026-10-18 00:35); then attempt SNZ for
Singer sets via equidistribution of the Singer Fourier phases (sinc-interpolation of |G(l)| = √q values with
pseudo-random phases), or a counterexample search for SNZ with structured (non-Singer) Sidon sets.
