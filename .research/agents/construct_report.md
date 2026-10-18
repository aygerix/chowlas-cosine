# Construct agent report — dense regime at larger N and new sub-1/2 mechanisms (2026-10-18, INTERIM)

Status: work in progress; this file is overwritten with the final version at the end of the run.

## Interim findings
- Single-swap local search (tabu with soft-max guidance, src in construct_scratch/dsearch.c) is fundamentally inadequate
  in the dense regime: the N = 36 optimum (R = 0.5648) has 7 dips within 0.08 of the minimum (equi-ripple), and tabu
  started 2 random swaps away from it fails to return in 2 of 4 runs (basin test). From random/structured starts tabu
  reaches only 0.595–0.614 at N = 36 (exact 0.5648).
- Complete branch-and-bound over the structured class C(X,N,Y,h) = {core [1,Y] with <= h holes, free tail in (Y,X]}
  (construct_scratch/coretail*.c) recovers the exhaustive optima N = 36, 41, 42 in 2–13 s (full exhaustive: hours).
  N = 45: class optimum R = 0.5718436 (X = 64, Y in {36, 38}, h = 3; same set as E27's unproven MILP incumbent).
  N = 50: R <= 0.5725176 found (X = 71, Y = 40), previous best 0.5842; class-optimality run in progress.
