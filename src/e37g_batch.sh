#!/bin/sh
# E37g: Gurobi reruns of the E37 instances that hit HiGHS's 900 s limit (src/grb_group_bt.py; pip gurobipy, size-limited
# licence suffices: <= ~900 rows, ~400 cols). Usage (on dirichlet via dirun.sh): sh src/e37g_batch.sh TL THREADS
TL=${1:-1800}; TH=${2:-4}
run() { python src/grb_group_bt.py "$1" "$2" "$3" $TL $TH; }   # no cutoff: in v1 the cutoff hint made Gurobi miss Z_256's 7 (2026-10-18)
# K0 = 4, order 256: Z_4^4 (O4 gives 56; HiGHS >= 55, bound 62) and cyclic Z_256
run 4,4,4,4 1,0,0,0 4 55; run 256 64 4 7; run 256 1 4 4
# K0 = 4: Z_125, Z_121, Z_105; K0 = 3: Z_105 (t = 35)
run 125 1 4 4; run 125 25 4 5; run 121 11 4 4; run 105 1 4 13; run 105 35 3 4
# K0 = 3, order ~243 (e37b rank dependence) and e37c
run 243 81 3 3; run 240 80 3 3; run 231 77 3 6; run 3,81 1,0 3 5; run 9,27 3,0 3 6; run 3,3,27 1,0,0 3 6
run 3,9,9 1,0,0 3 6; run 3,3,3,9 1,0,0,0 3 18; run 3,32 1,0 3 6; run 3,7,7 1,0,0 3 6
