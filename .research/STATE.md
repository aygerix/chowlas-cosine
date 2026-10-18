# STATE — current targets and honest status (updated 2026-10-17, session 1)

## Targets
- (C) Epoch: algorithm solution(c,n) for all c>0 — requires R(A_k) -> 0. NOT ACHIEVED. No solution.py exists.
- (L) Chowla: M(A) >= c0 sqrt|A|. NOT ACHIEVED. Best known: >> n^{1/5} (Shankar, cited).

## Best known construction constant
- Literature: limsup lambda(n)/sqrt(n) <= 1/2 (Bu et al. 2610.17160, asymptotic; uncertified numerics R≈0.635 at n=25440).
- Ours certified: Erdős–Turán Sidon differences, R ≈ 0.72 (E0), certified by ball-arithmetic DFT.

## Proved here (paper level, not Lean)
P1 Fejér–Riesz reformulation; P2 probabilistic reformulation; P3 projection principle; P4 no exact t>=2 uniform
difference sets in torsion-free groups; P5 M(A∩B) <= 2M(A)M(B); P6 energy/third-moment lower bounds
(sum-free A have R >= 1/sqrt2); P7 cube framework (rigorous template, R(A) <= R_cube(J)).

## Heuristic
H1 Gaussian-chaos (Wick) model: degree-2 chaos has R >= 1/2 (= Bu); conjecture inf R = 1/2 over large-block Wick models.

## Active lines
1. [construction] Cube framework: search families J minimizing R_cube(J) (rigorous). EXP-1.
2. [construction/obstruction] Wick-model barrier: test H1 numerically; identify escapes (small blocks, arithmetic correlation).
3. [lower bound] special classes: sum-free, low energy (done: P6); next: dense sets A ⊂ [1,CN], and a coupling inequality
   beyond Bedert's 1/3 cap.

## First concrete next step
Run EXP-1 (local search over J for k<=12, exact vertex minimum) and EXP-2 (Wick-model optimization).
