#!/bin/bash
# E116 batch 2: certified MILP bounds for the JL lift at p = 7 (L = n = 49), 4 threads, 3600 s per solve.
out=examples/e116/milp2.jsonl
for K in 7 10.5 14 21; do python src/e116_jl_taper.py milp 7 2 1 49 $K 3600 4 >> $out; done
