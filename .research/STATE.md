# STATE — current targets and honest status (updated 2026-10-18, session 1)

## Targets
- (C) Epoch: algorithm solution(c,n) for all c>0 — requires R(A_k) -> 0. NOT ACHIEVED. No solution.py exists.
- (L) Chowla: M(A) >= c0 sqrt|A|. NOT ACHIEVED. Best known: >> n^{1/5} (Shankar 2609.05338, cited, checked).
- NEW working hypothesis **C½**: M(A) >= sqrt|A|/2 for ALL finite A (sharp by Bu et al.). CONJECTURED; evidence in
  NOTEBOOK 2026-10-17 late. If true, Epoch's algorithm cannot exist. Not assumed: both tracks stay open.

## Best certified constructions (ours; ball-arithmetic certificates, E2/E4)
- Dense SA (E5, src/dense_sa.py): N=20, max 30, R <= 0.6011 (= exact box optimum for lam=2.7 by MILP);
  N=34, max 49, R <= 0.6043; N=54 R <= 0.6403; N=73 R <= 0.6730; N=122 R <= 0.6942.
- Bu et al. reproduction (E4): N=6320, max 432979, R <= 0.6573 (approaches 1/2 from above; excess ≈ 1.3 sqrt k).
- Exhaustive box optima (agent; [1,40]/[1,100]): N<=17, R >= 0.6137 (N=16).
- NO finite set with R < 0.60 found by any method. Nothing below 1/2.

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
1. [construction / C½ falsification] exact box MILP (src/box_ilp.py) for X = 40..80: true box optimum R(X);
   dense-regime trend; any R < 1/2 kills C½. Design search for coherent rounding (two-sided squares matched to a
   p.d. profile).
2. [lower bound] C½ restricted classes: Sidon differences (⟺ every Sidon D has min|F_D|^2 <= 0.293|D|); Bu class
   (⟺ ρ^2 >= g/2 fails somewhere); induced-subgraph/clique bounds (JMTZ framework) toward exponent > 1/5.
3. [obstruction] multiplicity barrier: is coherent gain Γ > 2 possible for any exact FR factor? (P8 sharpening.)

## First concrete next step
Read examples/box_ilp/X{40,50,60}.jsonl (MILP runs launched 2026-10-18 00:00, ~30 min/lam); compare the exact box
optimum R(X) with SA; then try to prove min_x |F_D(x)|^2 = o(|D|) for Sidon D (would prove C½ for Sidon differences).
