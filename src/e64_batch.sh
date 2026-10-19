#!/bin/bash
# E64 batch: one Bu step with D fixed (src/e64_bu_step.py). Args: list of k. Mt = M_Bu (eps = 0).
for k in "$@"; do
  python src/e64_bu_step.py $k --tl 1800 --threads 2 --out examples/e64/e64.jsonl > examples/e64/run_k$k.log 2>&1
done
