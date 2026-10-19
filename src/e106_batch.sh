#!/bin/bash
# E106: kill test for the many-spike lemma (NOTEBOOK cont. 25): Pareto search beta_K + mu*R in SPARSE boxes
# (X = 20n, 50n), against E68's dense boxes (X = 3n). Same SA code (src/e68_pareto_sa.c). Output examples/e106/e106.jsonl.
mkdir -p examples/e106 src/.build
cc -O3 -march=native -o src/.build/e68_pareto_sa src/e68_pareto_sa.c -lm
run() { src/.build/e68_pareto_sa $1 $2 $3 $4 $5 2 $6 >> examples/e106/e106.jsonl; }
for mu in 0.1 0.2 0.5; do
  run 1280 64 1 $mu 6000000 $((64*1000+1)) &
  run 1280 64 2 $mu 6000000 $((64*1000+2)) &
  run 3200 64 2 $mu 6000000 $((64*5000+2)) &
  run 2560 128 2 $mu 6000000 $((128*1000+2)) &
  wait
done
