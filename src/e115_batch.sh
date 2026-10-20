#!/bin/bash
# E115 batch: exact N_p(K) for K = 2..7 over primes 31..211 (Gurobi, 8 threads, 1800 s cap per solve).
out=examples/e115/np_k.jsonl
for K in 2 3 4 5 6 7; do
  for p in 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211; do
    python src/e115_zp_ilp.py $p $K 1800 8 >> $out
  done
done
