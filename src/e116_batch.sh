#!/bin/bash
# E116 batch 1: jointly optimised Boolean subsets of the JL lift P_L (L = n), Gurobi, 4 threads, 1800 s per solve.
out=examples/e116/milp1.jsonl
for K in 3 4 5 6; do python src/e116_jl_taper.py milp 3 2 1 9 $K 1800 4 >> $out; done
for K in 3 4 5 6; do python src/e116_jl_taper.py milp 3 2 1 9 $K 1800 4 full >> $out; done
for K in 5 7.5 10 15; do python src/e116_jl_taper.py milp 5 2 1 25 $K 1800 4 >> $out; done
