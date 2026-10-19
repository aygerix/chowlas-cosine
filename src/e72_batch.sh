#!/bin/bash
# E72 batch: one stream per n (arg1), mu in {0.1, 0.3, 1.0}; X = 3n; output examples/e72/e72_n<n>.jsonl
n=$1; X=$((3*n)); it=$2
for mu in 0.1 0.3 1.0; do src/.build/e72_p47_pareto $X $n $mu $it 2 $((n*7+${mu/./})) ; done > examples/e72/e72_n$n.jsonl
