#!/bin/bash
# E68b: Pareto search beta_K + mu*R at larger n (dense boxes X = 3n). Output examples/e68/e68b.jsonl.
mkdir -p examples/e68 src/.build
cc -O3 -march=native -o src/.build/e68_pareto_sa src/e68_pareto_sa.c -lm
for n in 256 512; do
  X=$((3*n))
  src/.build/e68_pareto_sa $X $n 1 0.1 4000000 2 $((n*1000+1)) >> examples/e68/e68b.jsonl &
  src/.build/e68_pareto_sa $X $n 1 0.2 4000000 2 $((n*1000+2)) >> examples/e68/e68b.jsonl &
  wait
done
