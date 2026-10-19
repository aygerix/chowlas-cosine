#!/bin/bash
# E64 dense: one Bu step with D = a certified dense optimum, Mt = (1+eps) M(D).
for f in D_N24 D_N36 D_N50; do
  for eps in 0 0.05; do
    python src/e64_bu_step.py 0 --D-file examples/e64/$f.json --eps $eps --tl 1500 --threads 2 \
      --out examples/e64/e64_dense.jsonl > examples/e64/run_${f}_$eps.log 2>&1
  done
done
