#!/bin/bash
# E75 batch: per-t run-top maximisation (mode 0) at several (X, n); output examples/e75/e75.jsonl
mkdir -p examples/e75 src/.build
cc -O3 -march=native -o src/.build/e75_runtop_sa src/e75_runtop_sa.c -lm
for cfg in "60 20" "120 30" "120 60" "200 40" "200 100" "300 60" "400 80"; do
  set -- $cfg
  src/.build/e75_runtop_sa $1 $2 0 200000 3 $(( $1 * 7 + $2 )) >> examples/e75/e75.jsonl
done
