#!/bin/sh
# E41: exact min M over symmetric half-sets of Z_p (src/zp_half.c). Usage: sh src/e41_batch.sh "p1 p2 ..." > out
mkdir -p src/.build && cc -O3 -march=native -o src/.build/zp_half src/zp_half.c -lm || exit 1
for p in $1; do echo $p; done | xargs -P 4 -I{} sh -c 'timeout 5400 src/.build/zp_half {}'
