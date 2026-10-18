#!/bin/sh
# E41c: core-plus-tail half-sets (core = pairs 1..L forced, tail annealed), L = f*k for f in 0.5..0.85, seeds 1 and 0.
mkdir -p src/.build && cc -O3 -march=native -o src/.build/zp_sa src/zp_sa.c -lm || exit 1
for p in $1; do
  k=$(( p % 4 == 1 ? (p-1)/4 : (p+1)/4 ))
  for f in 50 60 70 80 85; do L=$(( k * f / 100 )); echo "$p $L"; done
done | xargs -P 4 -L 1 sh -c 'src/.build/zp_sa $0 '"$2"' 4 1 11 $1' 
