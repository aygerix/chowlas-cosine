#!/bin/sh
# E37c: is it cyclicity or coprimality (Galois disjointness of Q(ζ_3) and the H-character field) that caps run-tops?
# t of order 3 in Z_3 x H with 3 ∤ |H| (H cyclic or not), K0 = 3, compared with F_3^4 (18) and Z_9^2 (6).
TL=${1:-900}
run() { python src/group_bt_ilp.py "$1" "$2" "$3" $TL; }
run 3,2,2,2,2,2 1,0,0,0,0,0 3; run 3,5,5 1,0,0 3; run 3,4,4,2 1,0,0,0 3; run 3,32 1,0 3; run 3,25 1,0 3; run 3,7,7 1,0,0 3
