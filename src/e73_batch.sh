#!/bin/bash
# E73 batch: Gaussian-threshold sets at X = 2^14, 2^16, 2^18, seeds 1-2. Output examples/e73/e73.jsonl.
mkdir -p examples/e73
for X in 16384 65536 262144; do for s in 1 2; do
  python src/e73_gauss_threshold.py $X $s >> examples/e73/e73.jsonl
done; done
