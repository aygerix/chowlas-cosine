#!/bin/bash
# E68: Pareto search beta_K + mu*R on dense boxes X = 3n (src/e68_pareto_sa.c). Output examples/e68/e68.jsonl.
mkdir -p examples/e68 src/.build
cc -O3 -march=native -o src/.build/e68_pareto_sa src/e68_pareto_sa.c -lm
for n in 64 128; do
  X=$((3*n))
  for mu in 0.05 0.1 0.2 0.5; do
    for K in 1 2; do
      src/.build/e68_pareto_sa $X $n $K $mu 3000000 2 $((n*1000+K)) >> examples/e68/e68.jsonl &
    done
    wait
  done
done
