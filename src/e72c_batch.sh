#!/bin/bash
# E72c: P47-escape Pareto at box ratio C: args n C iters "mu list"; output examples/e72/e72c_n<n>_C<C>.jsonl
n=$1; C=$2; it=$3; X=$((C*n))
for mu in $4; do src/.build/e72_p47_pareto $X $n $mu $it 2 $((n*13+C*7)) ; done > examples/e72/e72c_n${n}_C${C}.jsonl
