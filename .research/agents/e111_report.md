# E111: completely-positive flat-block certificate costs

Generated 2026-10-20 00:02:11 UTC.

Side computation for the lead; no core theorem is claimed. All optimization, FFTs, search, and rational verification ran on `dirichlet` through `src/dirun.sh`. No commit was made.

Completed **20 prescribed benchmark cases** and local searches at **every integer X=10,...,40**. The smallest flat upper-bound ratio among these saved cases is **0.7385489459**, for `Singer_q11` (n=66, X=131). Pricing closed to the specified tolerances for 15/20 benchmarks and 31/31 search winners. These are finite numerical flat-class optimization results; they establish no asymptotic CP lower bound.

**Optional non-flat finding:** `X30_s0` has an exact rational two-level certificate with C=5.857342308834, hence R_CP<=0.654870778502 (n=20, X=28). Its grid R is 0.607311315. The exact support, levels, weights and coefficient check are saved; the explicit set and strict rational threshold check appear below. This is a finite non-flat result, not a counterexample to the flat asymptotic target.

## Benchmark table

Convention: `f_A(theta)=sum_{a in A} cos(2*pi*a*theta)`, `n=|A|`, `X=max(A)`. `R_grid = -min_grid f_A / sqrt(n)` uses exactly 2^16 points and is uncertified. `R_CP` denotes the flat certificate upper bound `C_flat/(2 sqrt(n))`, not the unknown optimum over every nonnegative sequence. The LP lower-bound column concerns only the flat class and is numerical. Decimal values are rounded for display; exact primal weights and exact rational costs are in the linked JSON files. Block entries are `size:number` for positive master-LP blocks before tiny rational repairs.

| Set | n | X | R (grid) | R_CP (flat UB) | C_flat (UB) | Flat-class LP lower bound | Blocks used (size:number) | Pricing |
|---|---:|---:|---:|---:|---:|---:|---|---|
| [N50_x72](../../examples/e111/N50_x72_certificate.json) | 50 | 72 | 0.57006024 | 0.85667560 | 12.11522252 | 12.11522252 | 4:1, 6:2, 7:3, 8:8, 9:17, 10:9, 11:5, 12:2, 13:2, 16:1 | closed |
| [N50_x71](../../examples/e111/N50_x71_certificate.json) | 50 | 68 | 0.57251685 | 0.83454495 | 11.80224794 | 11.35719839 | 2:1, 3:1, 4:2, 6:1, 7:5, 8:11, 9:9, 10:9, 11:3, 12:1, 13:1, 14:5, 15:1 | total_time_limit |
| [X120_s0](../../examples/e111/X120_s0_certificate.json) | 73 | 115 | 0.67281911 | 0.98768680 | 16.87759938 | 8.58823529 | 6:1, 7:4, 8:17, 9:19, 10:19, 11:5, 12:6, 13:2 | total_time_limit |
| [X120_s1](../../examples/e111/X120_s1_certificate.json) | 73 | 120 | 0.67909292 | 1.00366198 | 17.15058350 | 9.73333333 | 4:1, 5:1, 6:3, 7:3, 8:11, 9:17, 10:17, 11:13, 12:3, 13:3, 14:1 | total_time_limit |
| [X30_s0](../../examples/e111/X30_s0_certificate.json) | 20 | 28 | 0.60731132 | 0.80836270 | 7.23021583 | 7.23021583 | 4:1, 5:4, 6:5, 7:2, 8:6, 9:1, 10:1 | closed |
| [X30_s1](../../examples/e111/X30_s1_certificate.json) | 20 | 30 | 0.60109185 | 0.84226913 | 7.53348416 | 7.53348416 | 2:1, 4:1, 5:4, 6:5, 7:4, 8:3, 9:2 | closed |
| [X50_s0](../../examples/e111/X50_s0_certificate.json) | 34 | 49 | 0.60426098 | 0.84245764 | 9.82465992 | 9.82465992 | 4:1, 5:1, 6:5, 7:6, 8:9, 9:8, 10:3, 11:1 | closed |
| [X50_s1](../../examples/e111/X50_s1_certificate.json) | 31 | 45 | 0.63479072 | 0.82296095 | 9.16410525 | 9.16410525 | 2:1, 5:1, 6:4, 7:11, 8:6, 9:6, 10:2 | closed |
| [X80_s0](../../examples/e111/X80_s0_certificate.json) | 54 | 80 | 0.64020444 | 0.91104058 | 13.38950736 | 13.38950736 | 2:1, 5:1, 6:2, 7:12, 8:10, 9:8, 10:7, 11:6, 12:6, 13:1 | closed |
| [X80_s1](../../examples/e111/X80_s1_certificate.json) | 49 | 80 | 0.65265788 | 0.93701345 | 13.11818825 | 13.11818825 | 5:1, 6:4, 7:8, 8:12, 9:8, 10:7, 11:5, 12:3, 13:1 | closed |
| [Singer_q5](../../examples/e111/Singer_q5_certificate.json) | 15 | 29 | 0.74943367 | 0.77459667 | 6.00000000 | 6.00000000 | 6:1 | closed |
| [Singer_q7](../../examples/e111/Singer_q7_certificate.json) | 28 | 55 | 0.75592895 | 0.75592895 | 8.00000000 | 8.00000000 | 8:1 | closed |
| [Singer_q11](../../examples/e111/Singer_q11_certificate.json) | 66 | 131 | 0.73844881 | 0.73854895 | 12.00000000 | 10.15384615 | 12:1 | total_time_limit |
| [interval_20](../../examples/e111/interval_20_certificate.json) | 20 | 20 | 1.10958561 | 1.11209718 | 9.94689958 | 9.94689958 | 2:1, 3:1, 4:4, 5:4, 6:8, 7:2 | closed |
| [interval_40](../../examples/e111/interval_40_certificate.json) | 40 | 40 | 1.47084974 | 1.47874824 | 18.70485005 | 2.00000000 | 2:4, 3:3, 5:5, 6:13, 7:5, 8:5, 9:3, 10:2 | total_time_limit |
| [random60_half](../../examples/e111/random60_half_certificate.json) | 31 | 55 | 1.50499716 | 1.56778019 | 17.45806134 | 17.45806134 | 3:1, 4:17, 5:8, 6:5 | closed |
| [Sidon_union_1](../../examples/e111/Sidon_union_1_certificate.json) | 12 | 15 | 0.68015500 | 0.80479128 | 5.57575758 | 5.57575758 | 2:1, 3:1, 4:4, 5:2, 6:1, 7:3 | closed |
| [Sidon_union_2](../../examples/e111/Sidon_union_2_certificate.json) | 17 | 24 | 0.86742172 | 0.91732961 | 7.56449376 | 7.56449376 | 3:1, 4:4, 5:3, 6:5, 7:1, 8:2, 10:1 | closed |
| [Sidon_union_3](../../examples/e111/Sidon_union_3_certificate.json) | 11 | 11 | 0.90880331 | 0.92170873 | 6.11392405 | 6.11392405 | 2:1, 3:2, 4:2, 5:2, 6:2, 7:1 | closed |
| [Sidon_union_4](../../examples/e111/Sidon_union_4_certificate.json) | 13 | 18 | 0.88832748 | 0.93232302 | 6.72307692 | 6.72307692 | 2:2, 4:6, 5:2, 6:2, 7:1 | closed |

The `N50_x71` input label has actual max(A)=68; the table uses the set itself. The qualifying dense rows are selected by actual max(A)<=120. Singer A is the set of positive **integer** differences of the representatives returned by `src/singer.py`, rather than all nonzero cyclic residues. The random row uses Python `random.Random(20261019)` and includes each a=1,...,60 independently when `random()<1/2`; its explicit A is saved in its certificate JSON. Each Sidon-union input records both B1 and B2 in `input_info`; both were checked to have no repeated positive integer differences.

## Numerical optimization and exact checks

The restricted master starts with every pair {0,a}, plus greedy cliques and supplied generating blocks. Greedy pricing adds improving columns before MILP pricing. The MILP uses vertices {0} union A, fixes 0 in the clique, forbids x_b+x_c>1 when c-b is absent from A, and linearizes each allowed binary product with all three McCormick inequalities. Its objective is sum_{b<c} y_{c-b} x_b x_c - sum_b x_b. Singleton blocks cannot improve the master. Translation normalization loses no admissible block, since a clique of minimum 0 has all its other vertices in A.

For a master dual y and a global MILP pricing upper bound U, the saved lower bound is sum(y)/(1+max(U,0)/2), maximized over pricing calls (and 0). Every nontrivial flat column has cost at least 2, so rescaling by this factor satisfies every flat dual inequality, conditional on the floating-point LP/MILP bounds. The master itself supplies C_lp. `closed` means a global pricing bound U<=1e-8; it is not an exact-rational proof of dual optimality. For time-limited cases the table deliberately retains the feasible certificate and the available scaled-dual lower bound, and reports the remaining gap.

Environment: host `dirichlet.us-east1-b.c.littlewood-paley-8375.internal`, Python 3.12.3, NumPy 2.5.4, Gurobi 13.0.3. Gurobi settings: FeasibilityTol=OptimalityTol=IntFeasTol=1e-9; MIPGap=0; MIPGapAbs=1e-9; positive reduced-cost threshold 1e-8; master dual simplex; at most two solver threads per job. Benchmark case budget 120 seconds, each MILP pricing call at most 8 seconds. Final search-winner budget 60 seconds, each MILP call at most 6 seconds. All timing includes model construction, master iterations, and pricing; a final master solve and rational repair can slightly exceed a case budget. Full pricing incumbent values, global bounds, solver statuses, nodes, duals, and runtimes are in each JSON `history`. Status 2 is Gurobi OPTIMAL; status 9 is TIME_LIMIT. A time-limited pricing call can still produce a valid numerical global upper bound.

Every flat case here with X<=30 closed its pricing gap to solver tolerances; all 31 final adversarial winners at X<=40 also closed. Larger benchmark cases used bounded MILP pricing plus the stated heuristics; the table identifies any unclosed cases. A globally solved Gurobi MILP is still floating-point optimization, distinct from the exact rational primal checks.

Some nonclosed benchmark cases were then refined from their saved master blocks, with a 120-second total budget and an initial 10-second MILP call limit, increasing on stalled calls within the total budget. Refinement also enumerates at most 200,000 anchored cliques in a seeded order and uses their exact multiplicity vectors to propose up to 32 improving columns per iteration. Truncated enumeration is only a heuristic; all reported full-class bounds still come from global Gurobi pricing bounds. `enumeration_heuristic` records the count and whether enumeration completed; `refinement` records limits and initial results. Initial runs are retained in `*_initial.json`.

Refinement also solves an anchored maximum-clique MILP for at most 5 seconds. A global upper bound W on clique size gives the constant flat dual y_a=2/(W-1), with value 2*n/(W-1). This is included when stronger than the quadratic-pricing dual bound. If it matches the feasible master value to 1e-8, the stop reason is `clique_dual_matched_to_tolerance`, also counted as closed. The value and status of the clique solve are saved in `clique_bound`; its bounds and matching statement remain numerical.

For every saved certificate, positive numerical weights are rounded with Fraction.limit_denominator(10^9). If any frequency is overcovered, all rounded weights are divided by the largest rational coverage (or 1). Each residual is then filled by a rationally weighted pair {0,a}. This gives an actual exact feasible certificate, even when simple rounding of the LP basis would fail. The cost in C_flat_UB includes these repairs. A separate verifier rereads saved JSON and directly accumulates all pair products and diagonal costs using Python Fraction; it checks every positive coefficient is exactly 1 on A, all other positive coefficients vanish, all weights are positive, and the exact diagonal cost matches C_exact. Negative coefficients follow by symmetry. The independent pass checked **63 files**; see [verification.json](../../examples/e111/verification.json). Thus primal feasibility is exact; displayed optimality and dual lower bounds remain numerical.

FFT values are independently checked by direct cosine summation at the winning grid point (error recorded). For the search winners, every sampled local minimum is also refined by bounded scalar minimization. The resulting `R_refined_uncertified` is an estimate of the actual R=M/sqrt(n), not a certified global minimum. Neither a grid result nor the scalar refinement is called a true or rigorous minimum here.

## Adversarial search: best set per X

The search fixes max(A)=X and |A|>=10, with X=10,...,40. At each X it attempts up to three restarts, 80 add/remove/swap proposals per restart, with a 20-second search budget. Starting families alternate between greedy Sidon differences (filled to n>=10 and including X), a density-0.65 Bernoulli set, and an interval. Annealing accepts improvements and accepts uphill moves with exp(-delta/T), T=0.025*(1-move/80)+0.001. Repeated sets use a cache. Each new trial has a 1-second column-generation budget with 0.25-second MILP calls; the objective during search is therefore a feasible restricted-master upper bound, and is not guaranteed to be the flat optimum. Each winner is subsequently re-solved at the longer limits above and rationally verified. The move trace records every evaluated proposal, including cached proposals and acceptance decisions. This is a bounded heuristic falsification attempt, not enumeration of all A or proof of local/global optimality in A.

An additional 10-second pass at each X=15,...,40 uses a verified Sidon difference set of diameter exactly X and the previous winner as starts (up to 60 moves per start). The Sidon start is selected from verified templates and 500 seeded greedy extensions of {0,X}; it is not claimed to be a largest Sidon set. This pass uses seed 20261019+1009*X+4096 and temperature 0.015*(1-move/60)+0.0005. The original summaries are retained in `search_initial_summary.json`, new trace entries have stage=polish, and each winner's `search.polish` records the added budget, seed, start, and runtime. The timing and move totals below sum both passes; expensive evaluations are counted within each pass, so the same set can be counted once in each pass.

After the short pass, a Sidon control check reconstructs the generating block from the saved seed and inserts its known one-block column whenever its cost improves the current numerical incumbent. Such a check uses a 30-second case budget and a 5-second initial pricing limit, is recorded as `sidon_warm_control` in the trace, and contributes one start/evaluation to the totals. This corrects a short pricing run that can fail to rediscover its own generating block. The final source supplies that block as a warm start during polishing as well. All generating blocks are saved in `search.polish.sidon_block`.

| X | n | R (grid) | R (refined, uncertified) | R_CP (flat UB) | Flat LP lower bound | Explicit best A |
|---:|---:|---:|---:|---:|---:|---|
| 10 | 10 | 0.88495235 | 0.88495235 | 0.90124913 | 5.70000000 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| 11 | 10 | 0.67478770 | 0.67478770 | 0.75894664 | 4.80000000 | [1, 2, 3, 4, 5, 6, 7, 9, 10, 11] |
| 12 | 11 | 0.68671630 | 0.68671632 | 0.75377836 | 5.00000000 | [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12] |
| 13 | 12 | 0.71244375 | 0.71244385 | 0.75436804 | 5.22641509 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13] |
| 14 | 13 | 0.75058160 | 0.75058166 | 0.76548627 | 5.52000000 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14] |
| 15 | 13 | 0.70320046 | 0.70320054 | 0.77518355 | 5.58992806 | [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15] |
| 16 | 13 | 0.73013976 | 0.73013984 | 0.77658027 | 5.60000000 | [1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 16] |
| 17 | 15 | 0.72791324 | 0.72791335 | 0.77459667 | 6.00000000 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17] |
| 18 | 15 | 0.76757982 | 0.76757988 | 0.77459667 | 6.00000000 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 16, 18] |
| 19 | 15 | 0.77459667 | 0.77459667 | 0.77459667 | 6.00000000 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 19] |
| 20 | 17 | 0.70557417 | 0.70557429 | 0.76658581 | 6.32142857 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 20] |
| 21 | 18 | 0.71693764 | 0.71693768 | 0.76294929 | 6.47383942 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 19, 20, 21] |
| 22 | 15 | 0.77459667 | 0.77459667 | 0.77459667 | 6.00000000 | [1, 2, 3, 4, 6, 9, 10, 11, 12, 15, 17, 18, 19, 21, 22] |
| 23 | 15 | 0.77455404 | 0.77455417 | 0.77459667 | 6.00000000 | [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 19, 20, 23] |
| 24 | 15 | 0.77459667 | 0.77459667 | 0.77459667 | 6.00000000 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 17, 19, 20, 24] |
| 25 | 21 | 0.75863836 | 0.75863853 | 0.76376262 | 7.00000000 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 17, 18, 19, 21, 22, 23, 24, 25] |
| 26 | 21 | 0.76345938 | 0.76345939 | 0.76376262 | 7.00000000 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 16, 18, 19, 21, 23, 24, 25, 26] |
| 27 | 21 | 0.76355877 | 0.76355889 | 0.76376262 | 7.00000000 | [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16, 17, 18, 19, 23, 24, 26, 27] |
| 28 | 21 | 0.76259266 | 0.76259269 | 0.76376262 | 7.00000000 | [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 22, 23, 24, 25, 27, 28] |
| 29 | 21 | 0.76376096 | 0.76376105 | 0.76376262 | 7.00000000 | [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 14, 16, 17, 19, 20, 21, 23, 26, 27, 28, 29] |
| 30 | 21 | 0.76373136 | 0.76373175 | 0.76376262 | 7.00000000 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17, 18, 19, 20, 23, 27, 29, 30] |
| 31 | 21 | 0.76272445 | 0.76272456 | 0.76376262 | 7.00000000 | [1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 16, 18, 21, 22, 24, 25, 26, 28, 29, 31] |
| 32 | 21 | 0.75756354 | 0.75756359 | 0.76376262 | 7.00000000 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 17, 19, 20, 21, 26, 28, 31, 32] |
| 33 | 21 | 0.75233167 | 0.75233187 | 0.76376262 | 7.00000000 | [1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 14, 16, 17, 20, 24, 25, 26, 27, 30, 31, 33] |
| 34 | 28 | 0.74577650 | 0.74577653 | 0.75592895 | 8.00000000 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25, 28, 30, 31, 32, 33, 34] |
| 35 | 28 | 0.75592895 | 0.75592895 | 0.75592895 | 8.00000000 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 26, 29, 30, 31, 33, 35] |
| 36 | 28 | 0.74694528 | 0.74694581 | 0.75592895 | 8.00000000 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 20, 21, 24, 25, 26, 28, 29, 30, 32, 33, 34, 35, 36] |
| 37 | 28 | 0.75161085 | 0.75161085 | 0.75592895 | 8.00000000 | [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 26, 28, 29, 32, 34, 35, 37] |
| 38 | 28 | 0.74961601 | 0.74961608 | 0.75592895 | 8.00000000 | [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 16, 18, 19, 21, 22, 24, 26, 27, 30, 31, 32, 34, 35, 36, 37, 38] |
| 39 | 28 | 0.75581667 | 0.75581715 | 0.75592895 | 8.00000000 | [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 19, 20, 22, 23, 24, 27, 29, 33, 34, 35, 36, 37, 39] |
| 40 | 28 | 0.73283910 | 0.73283968 | 0.75592895 | 8.00000000 | [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 20, 21, 22, 23, 24, 25, 27, 29, 30, 31, 33, 37, 38, 40] |

The seeds are deterministic: `20261019+1009*X`. The next table counts attempted moves that reached objective evaluation (including cache hits), distinct expensive evaluations, and accepted states (including restart starts). Runtime includes the final longer solve and FFT comparison. Per-trial timing and completed restart counts are also saved.

| X | Seed | Starts/add/remove/swap | Distinct evaluations | Accepted | Restarts started | Runtime (s) | Final pricing |
|---:|---:|---|---:|---:|---:|---:|---|
| 10 | 20271109 | 3/0/0/0 | 1 | 3 | 3 | 0.249 | closed |
| 11 | 20272118 | 3/74/1/74 | 11 | 19 | 3 | 1.023 | closed |
| 12 | 20273127 | 3/84/66/82 | 44 | 29 | 3 | 4.245 | closed |
| 13 | 20274136 | 3/67/86/84 | 39 | 11 | 3 | 6.445 | closed |
| 14 | 20275145 | 3/82/83/73 | 73 | 27 | 3 | 15.091 | closed |
| 15 | 20276154 | 5/102/82/94 | 152 | 29 | 5 | 30.224 | closed |
| 16 | 20277163 | 4/85/48/70 | 121 | 24 | 4 | 28.002 | closed |
| 17 | 20278172 | 3/40/37/43 | 81 | 18 | 3 | 30.860 | closed |
| 18 | 20279181 | 3/35/36/34 | 84 | 14 | 3 | 31.053 | closed |
| 19 | 20280190 | 2/29/30/27 | 65 | 14 | 2 | 31.068 | closed |
| 20 | 20281199 | 2/27/35/28 | 67 | 6 | 2 | 30.452 | closed |
| 21 | 20282208 | 3/26/47/23 | 57 | 8 | 3 | 31.007 | closed |
| 22 | 20283217 | 2/35/27/38 | 80 | 7 | 2 | 31.249 | closed |
| 23 | 20284226 | 4/46/53/45 | 86 | 8 | 4 | 30.683 | closed |
| 24 | 20285235 | 4/44/54/51 | 105 | 8 | 4 | 31.360 | closed |
| 25 | 20286244 | 2/13/20/16 | 48 | 9 | 2 | 31.805 | closed |
| 26 | 20287253 | 2/14/22/19 | 54 | 9 | 2 | 33.083 | closed |
| 27 | 20288262 | 2/13/7/15 | 35 | 10 | 2 | 32.971 | closed |
| 28 | 20289271 | 2/19/12/18 | 42 | 8 | 2 | 30.984 | closed |
| 29 | 20290280 | 2/26/25/29 | 71 | 7 | 2 | 32.410 | closed |
| 30 | 20291289 | 2/9/11/12 | 33 | 2 | 2 | 31.549 | closed |
| 31 | 20292298 | 2/7/16/10 | 33 | 8 | 2 | 31.948 | closed |
| 32 | 20293307 | 2/11/12/9 | 32 | 6 | 2 | 33.187 | closed |
| 33 | 20294316 | 2/12/12/9 | 35 | 9 | 2 | 33.419 | closed |
| 34 | 20295325 | 2/8/7/15 | 30 | 5 | 2 | 51.325 | closed |
| 35 | 20296334 | 3/8/9/12 | 31 | 9 | 2 | 45.312 | closed |
| 36 | 20297343 | 2/15/8/9 | 31 | 8 | 2 | 46.231 | closed |
| 37 | 20298352 | 2/13/12/8 | 33 | 7 | 2 | 38.505 | closed |
| 38 | 20299361 | 2/12/8/9 | 31 | 5 | 2 | 34.194 | closed |
| 39 | 20300370 | 2/10/10/10 | 32 | 8 | 2 | 37.636 | closed |
| 40 | 20301379 | 2/10/12/13 | 37 | 9 | 2 | 35.420 | closed |

## Search certificate block structure

Each entry below is `size/type: weight, weight, ...`, giving every positive numerical master block weight (10 significant figures). AP means equally spaced support (including pairs), Sidon means all positive differences are distinct, and other means neither. AP takes precedence for classification. The linked JSON gives **all supports and exact rational weights**, including any tiny pair repairs; its `blocks_numerical` field records the unrounded master solution. When final pricing is closed, this is a numerically optimal flat certificate; otherwise it is a feasible certificate only.

| X | Master blocks | Size/type and weights | Complete certificate |
|---:|---:|---|---|
| 10 | 10 | 2/AP: 0.04, 0.26; 3/AP: 0.4; 3/Sidon: 0.08; 4/other: 0.04, 0.12; 5/other: 0.02, 0.08; 6/other: 0.02, 0.4 | [search_X10](../../examples/e111/search_X10_certificate.json) |
| 11 | 8 | 2/AP: 0.1; 4/Sidon: 0.15; 4/other: 0.075, 0.075, 0.1; 6/other: 0.125, 0.175, 0.2 | [search_X11](../../examples/e111/search_X11_certificate.json) |
| 12 | 10 | 2/AP: 0.0625; 3/AP: 0.125; 3/Sidon: 0.0625; 5/other: 0.125, 0.125; 6/other: 0.0625, 0.0625, 0.125, 0.1875; 7/other: 0.0625 | [search_X12](../../examples/e111/search_X12_certificate.json) |
| 13 | 11 | 3/Sidon: 0.2075471698; 4/Sidon: 0.03773584906; 5/other: 0.01886792453, 0.1132075472, 0.1509433962; 6/other: 0.01886792453, 0.01886792453, 0.05660377358, 0.07547169811, 0.09433962264; 7/other: 0.2075471698 | [search_X13](../../examples/e111/search_X13_certificate.json) |
| 14 | 10 | 3/Sidon: 0.1; 5/Sidon: 0.2; 5/other: 0.04, 0.04; 6/other: 0.02, 0.04, 0.06, 0.18, 0.22; 7/other: 0.1 | [search_X14](../../examples/e111/search_X14_certificate.json) |
| 15 | 13 | 2/AP: 0.02158273381; 3/Sidon: 0.07913669065; 4/Sidon: 0.07913669065; 4/other: 0.1007194245; 5/other: 0.02158273381, 0.2158273381; 6/other: 0.02877697842, 0.08633093525, 0.09352517986, 0.1654676259; 7/other: 0.05035971223, 0.05755395683; 8/other: 0.05035971223 | [search_X15](../../examples/e111/search_X15_certificate.json) |
| 16 | 5 | 5/other: 0.2, 0.2; 6/other: 0.2, 0.2, 0.2 | [search_X16](../../examples/e111/search_X16_certificate.json) |
| 17 | 1 | 6/Sidon: 1 | [search_X17](../../examples/e111/search_X17_certificate.json) |
| 18 | 1 | 6/Sidon: 1 | [search_X18](../../examples/e111/search_X18_certificate.json) |
| 19 | 1 | 6/Sidon: 1 | [search_X19](../../examples/e111/search_X19_certificate.json) |
| 20 | 17 | 4/Sidon: 0.03174603175; 5/Sidon: 0.01587301587; 5/other: 0.05158730159, 0.123015873; 6/other: 0.01587301587, 0.01587301587, 0.03174603175, 0.03174603175, 0.06349206349, 0.07142857143, 0.08333333333, 0.119047619; 7/other: 0.01587301587, 0.07142857143, 0.1547619048; 8/other: 0.03174603175, 0.0873015873 | [search_X20](../../examples/e111/search_X20_certificate.json) |
| 21 | 18 | 2/AP: 0.02473363775; 4/Sidon: 0.02130898021; 5/other: 0.07734018265; 6/other: 0.03833713851, 0.05289193303, 0.06050228311, 0.06097792998, 0.08409436834, 0.2728310502; 7/other: 0.005136986301, 0.02910958904, 0.09237062405; 8/other: 0.004280821918, 0.01379375951, 0.02302130898, 0.1470700152; 9/other: 0.009227549467; 10/other: 0.005993150685 | [search_X21](../../examples/e111/search_X21_certificate.json) |
| 22 | 1 | 6/Sidon: 1 | [search_X22](../../examples/e111/search_X22_certificate.json) |
| 23 | 1 | 6/Sidon: 1 | [search_X23](../../examples/e111/search_X23_certificate.json) |
| 24 | 1 | 6/Sidon: 1 | [search_X24](../../examples/e111/search_X24_certificate.json) |
| 25 | 1 | 7/Sidon: 1 | [search_X25](../../examples/e111/search_X25_certificate.json) |
| 26 | 1 | 7/Sidon: 1 | [search_X26](../../examples/e111/search_X26_certificate.json) |
| 27 | 1 | 7/Sidon: 1 | [search_X27](../../examples/e111/search_X27_certificate.json) |
| 28 | 1 | 7/Sidon: 1 | [search_X28](../../examples/e111/search_X28_certificate.json) |
| 29 | 1 | 7/Sidon: 1 | [search_X29](../../examples/e111/search_X29_certificate.json) |
| 30 | 1 | 7/Sidon: 1 | [search_X30](../../examples/e111/search_X30_certificate.json) |
| 31 | 1 | 7/Sidon: 1 | [search_X31](../../examples/e111/search_X31_certificate.json) |
| 32 | 1 | 7/Sidon: 1 | [search_X32](../../examples/e111/search_X32_certificate.json) |
| 33 | 1 | 7/Sidon: 1 | [search_X33](../../examples/e111/search_X33_certificate.json) |
| 34 | 1 | 8/Sidon: 1 | [search_X34](../../examples/e111/search_X34_certificate.json) |
| 35 | 1 | 8/Sidon: 1 | [search_X35](../../examples/e111/search_X35_certificate.json) |
| 36 | 1 | 8/Sidon: 1 | [search_X36](../../examples/e111/search_X36_certificate.json) |
| 37 | 1 | 8/Sidon: 1 | [search_X37](../../examples/e111/search_X37_certificate.json) |
| 38 | 1 | 8/Sidon: 1 | [search_X38](../../examples/e111/search_X38_certificate.json) |
| 39 | 1 | 8/Sidon: 1 | [search_X39](../../examples/e111/search_X39_certificate.json) |
| 40 | 1 | 8/Sidon: 1 | [search_X40](../../examples/e111/search_X40_certificate.json) |

## Threshold audit and scope

**No benchmark, saved search winner, or recorded search proposal had R_CP<0.68.** Here R_CP refers to the flat upper bound. The full trace audit scanned 2923 proposals and 1643 distinct sets; [sub068_audit.json](../../examples/e111/sub068_audit.json) records the empty flat result. This finite failure to falsify the flat target does not prove it.

The optional **non-flat two-level** class does produce the following sub-0.68 certificates. These do not falsify the flat-class target. Every set is explicit, and the linked JSON contains supports, levels and exact rational weights. The independent verifier also checks the strict threshold in rational arithmetic as C^2 < 4*n*(17/25)^2:

- **X30_s0**: A=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 24, 28]; n=20; X=28; R_CP(two-level UB)=0.654870778502; exact C=1597863279404275978430215/272796636282355449163507; [exact certificate](../../examples/e111/X30_s0_two_level.json). All coefficients and nonnegativity checked in exact rational arithmetic after rounding and repair.

## Optional two-level blocks

Values are in {0,1,2} times sqrt(w). Pricing includes mutually exclusive level choices at each location and binary-product linearization; the nonzero value at location 0 may be 1 or 2. Flat columns are warm starts. The same solver tolerances, rescaled-dual bound, and exact rational verification apply. Each case had a 45-second total limit and an initial 5-second pricing limit; stalled pricing limits increase within the total budget.

| Set | Flat C | Two-level C (UB) | Two-level class LP lower | R_CP (two-level UB) | Pricing |
|---|---:|---:|---:|---:|---|
| X30_s0 | 7.23021583 | 5.85734231 | 5.85734231 | 0.65487078 | pricing_proved_no_improvement_to_tolerance |
| X30_s1 | 7.53348416 | 6.47705533 | 6.47705533 | 0.72415680 | pricing_proved_no_improvement_to_tolerance |
| search_X11 | 4.80000000 | 4.31169251 | 4.31169251 | 0.68173844 | pricing_proved_no_improvement_to_tolerance |
| search_X12 | 5.00000000 | 4.57571246 | 4.57571246 | 0.68981461 | pricing_proved_no_improvement_to_tolerance |
| search_X13 | 5.22641509 | 4.94435698 | 4.94435698 | 0.71365646 | pricing_proved_no_improvement_to_tolerance |
| search_X14 | 5.52000000 | 5.41584379 | 5.41584379 | 0.75104240 | pricing_proved_no_improvement_to_tolerance |

## Reproduction and artifacts

Source: [src/e111_cp.py](../../src/e111_cp.py). Data: [examples/e111](../../examples/e111/). All paths in this report are relative to `.research/agents/`. No files outside the permitted code, data, and report locations were intentionally edited by this task.

```sh
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 3600 python src/e111_cp.py suite --seconds 120 --price-seconds 8
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 2400 python src/e111_cp.py search --seconds 60 --price-seconds 6 --search-seconds 20 --eval-seconds 1 --eval-price-seconds 0.25 --moves 80 --restarts 3
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 1800 python src/e111_cp.py refine --seconds 120 --price-seconds 10
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 1200 python src/e111_cp.py polish --X 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 --seconds 60 --price-seconds 6 --search-seconds 10 --moves 60 --eval-seconds 1 --eval-price-seconds 0.25
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 1 -t 300 python src/e111_cp.py warm_controls --seconds 30 --price-seconds 5
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 1 -t 600 python src/e111_cp.py levels --seconds 45 --price-seconds 5 --only search_X11 search_X12 X30_s0
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 1 -t 600 python src/e111_cp.py levels --seconds 45 --price-seconds 5 --only X30_s1 search_X13 search_X14
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 1 -t 600 python src/e111_cp.py audit
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 1 -t 300 python src/e111_cp.py verify
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 1 -t 300 python src/e111_cp.py report
```

The first two jobs ran concurrently with two-core quotas each; do not add their per-case wall times to infer elapsed session time. `suite.jsonl`, `search_summary.json`, `search_trace.jsonl`, `*_certificate.json`, and `verification.json` contain the results. `metadata_*.json` records commands, host, Python/NumPy/Gurobi versions, and tolerances; later metadata also includes the final source SHA-256. The initial suite/search processes loaded the initial source before the optional refinement, polish, and postprocessing code was added. The final source retains the algorithms and adds stronger bounded pricing retries for stalled cases; under time limits, reproduction need not yield identical search move counts or identical LP bases.
