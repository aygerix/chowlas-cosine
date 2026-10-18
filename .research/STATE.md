# STATE — current targets and honest status (updated 2026-10-18, session 2)

## Targets
- (C) Epoch: algorithm solution(c,n) for all c>0 — requires R(A_k) -> 0. NOT ACHIEVED. No solution.py exists.
- (L) Chowla: M(A) >= c0 sqrt|A|. NOT ACHIEVED. Best known: >> n^{1/5} (Shankar 2609.05338, cited, checked).
- Working hypothesis **C½**: M(A) >= sqrt|A|/2 for ALL finite A (sharp by Bu et al.). CONJECTURED. If true, Epoch's
  algorithm cannot exist. Not assumed: both tracks stay open.

## Best certified constructions (ball-arithmetic certificates, E2; Sturm brackets for N <= 40)
- Small-N exhaustive box optima (agent, E14): **N=36, max 50, R <= 0.56481** (best finite R known to us; lead re-certified),
  N=35 0.5677, N=34 0.5741, N=24 0.5769 (= exact [1,40] optimum by MILP, E13), N=27 1/√3 (M = 3 at x = π).
- Structured MILP (E27, C-N45): N=45 R <= 0.571844 (two certificates). LNS-MILP (E18): N=45 0.5948, N=50 0.6036, N=60 0.6243, N=80 0.6630 (uncertified objective; certify before quoting).
- Bu et al. reproduction (E4): N=6320 R <= 0.6573. Bu's identity on FULL Singer sets with best shift (E25, C-SB):
  N=63252 R <= 0.56272; N=94556 R <= 0.55679; **N=161202 R <= 0.55476** (q = 401; best certified finite R known to us).
  Fit R − 1/2 ≈ 0.42–0.45·√(log k / k) (k = 62..402). Nothing below 1/2 anywhere.

## Proved here
Paper: P1 Fejér–Riesz; P2 probabilistic; P3 projection; P4 no exact t>=2 uniform difference sets; P5 intersection;
P6 energy bounds; P7 cube framework; P8 multiplicity bound (R < 1/2 needs coherent multiplicity > 2); P9 star lemma;
gain identity; P10 B_3 differences R >= 0.293; P11 B_h differences -> 1/√2; P12 dissociated Bu class; P13 even part.
NEW 2026-10-18: P14 (averaged boundary bound: precise obstruction L(A); finite-model counterexample to "no middle
layer"); P15 (Bu = P^2 − k/2 − C/2, P(x) = C(x/2)); **P16/P16′: R(A(S)) >= 1/2 − O((L/k^3)^{1/5}) for every Sidon S ⊂ [−L,L]**
— C½ for Bu's construction, unconditional. PROVED on paper and INDEPENDENTLY REVIEWED (agent: CORRECT; P16′ large-sieve
form re-derived by lead). Explicit: R >= 0.302 at k = 1e6 and 0.423 at k = 1e8 for Bu's range L ≈ 12.5k^2. Lean: P16 is
KERNEL-CHECKED in unconditional explicit form (HalfSquareExplicit.lean: R(A(S)) > 1/2 − η whenever η^6k^3 >= 7000L;
re-verified by lead, 85 axiom lines standard); P16′ (exponent 1/5) is KERNEL-CHECKED too (HalfSquareSieve.lean:
R(A(S)) > 1/2 − η whenever η^5k^3 >= 4200L, Gallagher sieve; lead re-elaborated, 103 axiom lines standard).
KERNEL-CHECKED (Lean 4, axioms propext/choice/Quot.sound only, no sorry; re-verified by lead, 37 axiom lines):
difference-set identity; Sidon consequence; mean zero/Parseval; P5; P7 cube identity + vertex min; P9 star lemma and
star bound; P8 multiplicity bound; P13(a) averaging identity, restriction to multiples, (q−1)M >= |A| − q|A∩qZ|.

NEW (session 2): P17 rigorous bounds on the doubly-positive profile constant: ρ* <= 0.9057 (all profiles), <= 0.7698 for
w = h⋆h̃ with h >= 0 (Beckner + Hölder); numerical sup 0.7239.

## Heuristic / numerical
H1 Wick model. Dense-profile identity R = c_E sqrt((1−ρ)/2) (σ_E^2 = (1−ρ)N/2), ρ <= ρ* ≈ 0.7239 (numerical sup over
doubly-positive profiles; autocorrelation analogue of the Matolcsi–Vinuesa constant). Symmetric rounding (c_E >= √2)
⇒ dense limit >~ 0.5255. Exhaustive optima DO use positive skew (E21: +1.18 at N=29) but the skew fades (+0.19 at N=40)
and c_E rises (1.43 → 1.79); anatomy extrapolation from N=36 gives R_∞ ≈ 0.50–0.51 — the dense regime is the one live
candidate against C½ (needs c_E < 1.35 with a p.d. profile). LNS/SA at N >= 45 are search-limited (calibration: random
starts reach only 0.60 at N=36), so "R rises past N=36" is NOT established.

Quadratic ("square-identity") class (NOTEBOOK 2026-10-18 late): in the Gaussian model R >~ 1/2 with equality only for one
positive eigenvalue (= complete multipartite by Smith's theorem) with small parts, i.e. Bu. E22: complete-multipartite
Bu sums with blocks of size >= 2 are much worse (M/k ≈ 1.0 at b = 2 vs 0.65 for Bu). Killed as a construction route.
Literature check: Erdélyi 2607.21877v1's n^{1/3} proof for Littlewood cosine polynomials has a gap (LITERATURE.md;
Fejér-kernel counterexample to the displayed chain); not used here.

## Session-2 late additions (2026-10-18)
- P16′ KERNEL-CHECKED (HalfSquareSieve.lean, η^5k^3 >= 4200L). Formalization corrected the window-folding step of the
  lead's Gallagher sketch (windows inside one period window); conclusion unaffected.
- P18 (dense min–max Bernstein lemma) PROVED but numerically empty on records (E28): qualitative only.
- E29: Erdős–Turán quadratic Sidon sets have min|F_B|^2/k -> 0 (killed). Profile analysis: Sidon forces the profile
  autocorrelation <= λ, so the spike carries <= ρ* of E|F|^4 — the doubly-positive constant ρ* ≈ 0.724 is a COMMON
  obstruction to dense sets and Sidon-difference sets (NOTEBOOK).
- Bedert framework barrier (NOTEBOOK): the K^4 in Prop 7.3 = O(K^2) (degree-2 gap inequality) × ||H||_1^2; PROVED that no
  degree-1 (single nonnegative multiplier) inequality has a coefficient gap (|c_1| <= c_0). Exponent 1/4 would need a
  run-top test function with L^1 <~ K^{1/2}.

- P19 (agent, proof read by lead): Bedert's |B_t| << K^4 is sharp for all degree-2 gap-inequality methods (random
  relaxed sets); the universal exponent 1/4 needs Target Lemma S (degree-1 input). Open group question: finite abelian
  groups with |B_t| >> K^{2+ε}?

## Refuted / killed routes (keep)
Cube vertex framework; A_{k-1} root squares; quarter-integer trick; fractional decomposition; dithered Fejér/Beatty;
error diffusion; separated-block unions; local SA from Bu seeds; Sidon lower-flat polynomials (E8/E12/E15: c -> 0);
cyclotomic Z-lifts and model sets (E11); Erdős–Turán quadratic Sidon flatness (E29); P18 as a finite probe (E28); averaged Bedert (P14: (a) is t-independent); sums of several squares
Σ P_j^2 (P15 remark: pseudo-random squares give R ~ √log X).

## Active lines (>= 3)
1. [lower bound, class] P16 follow-ups: extend the range of L (local Lipschitz, higher moments), and attack SNZ-weak for
   Sidon differences (min|F_D|^2 <= 0.29k) with a 2-D visit lemma (locally linear phase).
2. [lower bound, universal] "visit + concentration" for arbitrary A via a spectral factor (gain identity); Bedert–Shankar
   middle-layer exclusion needs torsion-freeness (P14(v)) — parked unless a level-set decomposition appears.
3. [construction / C½ falsification] dense regime: is there a positively skewed rounding error (c_E < 1.35) for a
   doubly-positive profile? Only such an error lets dense sets beat 1/2 (E16). Exhaustive N = 41–50 in [1, 1.5N] (on F4).
4. [obstruction] identify ρ* exactly (extremal problem for doubly-positive functions) and prove the dense-profile bound.

## Compute policy
Heavy jobs run on F4 (src/f4run.sh; ~/chowla_venv on f4-magma). Never swap the Mac (user request 2026-10-18).

## First concrete next step
(1) Collect the structured MILP result for N = 45 (examples/milp/X62_n45_Y34_H3.log, F4) and certify it; if R(45) <
0.565 the dense regime trends down — then run N = 50, 55, 60 the same way (one job at a time, F4 load < 12). Exhaustive
box search is too slow at L − N >= 19 (N = 41, L = 60 ran > 2 h); rerun with L = round(1.375N) + 1.
(2) Integrate the Lean agent's unconditional explicit P16 (lean/ChowlaCosine/HalfSquare*.lean; report
.research/agents/lean_p16_explicit.md): re-run lake build + AxiomCheck yourself before recording KERNEL-CHECKED.
(3) Lower-bound line: the only universal lead is Bedert's (S') "approximate additive closure of {F > K^2}"; the
measure form ν∗ν = ν/K + (1 − 1/K)λ (NOTEBOOK session 2) is the cleanest language for it.
