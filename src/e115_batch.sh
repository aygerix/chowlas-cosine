#!/bin/bash
# E115 run 2: exact N_p(K) near the half-set regime, K = c·sqrt(p), c in {0.42, 0.46, 0.50}; Gurobi 8 threads,
# 1200 s cap per solve (ObjBound is a valid upper bound on N_p(K) even when the solve is not finished).
# Run 1 (K = 2, 3 integer thresholds, primes <= 211) is in examples/e115/np_k_run1.jsonl.
out=examples/e115/np_k_run2.jsonl
for p in 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 149 151; do
  for c in 0.42 0.46 0.50; do
    K=$(python -c "import math; print(round($c*math.sqrt($p), 6))")
    python src/e115_zp_ilp.py $p $K 1200 8 >> $out
  done
done
