#!/bin/sh
# E37: run-top maxima in CYCLIC groups vs non-cyclic groups of the same order at small K (exact ILP, HiGHS 4 threads).
# Usage (on dirichlet via dirun.sh): sh src/e37_batch.sh TIMELIMIT >> examples/cyclic_ilp/e37.jsonl
TL=${1:-600}
run() { python src/group_bt_ilp.py "$1" "$2" "$3" $TL; }
# order 81: F_3^4 (agent: 18 at K0=3) vs Z_81 (t of order 3, 9, 81) and Z_9 x Z_9, Z_3 x Z_27
run 81 27 3; run 81 9 3; run 81 1 3; run 9,9 3,0 3; run 3,27 1,0 3; run 3,27 0,9 3
# order 64: Z_64 (t of order 4, 64) vs Z_4^3 and Z_8^2 at K0 = 4
run 64 16 4; run 64 1 4; run 4,4,4 1,0,0 4; run 8,8 2,0 4; run 8,8 1,0 4
# order 125 / 121 / 105 (cyclic, t of order p or large) at K0 = 3, 4
run 125 25 4; run 125 1 4; run 5,5,5 1,0,0 4; run 121 11 4; run 105 35 3; run 105 1 4
# order 256: Z_4^4 has O4 (|B_t| = 56 at K = 4); Z_256 with t of order 4, 256
run 256 64 4; run 256 1 4; run 4,4,4,4 1,0,0,0 4
