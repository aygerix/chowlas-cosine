#!/bin/sh
# E37b: rank dependence at order ~243 for t of order 3, K0 = 3 (F_3^5 has >= 36, agent ILP): cyclic Z_243 (non-split),
# split cyclic Z_3 x Z_m (m coprime to 3), and rank-2/3 groups.  Usage: sh src/e37b_batch.sh TL >> examples/cyclic_ilp/e37b.jsonl
TL=${1:-900}
run() { python src/group_bt_ilp.py "$1" "$2" "$3" $TL; }
run 243 81 3; run 240 80 3; run 231 77 3; run 3,81 1,0 3; run 9,27 3,0 3; run 3,3,27 1,0,0 3; run 3,9,9 1,0,0 3; run 3,3,3,9 1,0,0,0 3
