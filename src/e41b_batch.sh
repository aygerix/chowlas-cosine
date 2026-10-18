#!/bin/sh
# E41b: SA upper bounds on min M_p over half-sets of Z_p (src/zp_sa.c), calibration on exact p and trend for larger p.
mkdir -p src/.build && cc -O3 -march=native -o src/.build/zp_sa src/zp_sa.c -lm || exit 1
for p in $1; do for m in 0 1; do echo "$p $m"; done; done | xargs -P 2 -L 1 sh -c 'src/.build/zp_sa $1 $0 6 $2 7' "$2"
