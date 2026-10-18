#!/bin/sh
# E38: SA on the O4-shaped class A = S ∪ (S+t) (mode 0) vs unrestricted sets of the same size and span (mode 1).
# Usage (dirichlet): sh src/e38_batch.sh > examples/pair_sa/e38.txt
mkdir -p .build && cc -O3 -march=native -o .build/pair_sa src/pair_sa.c -lm || exit 1
for spec in "18 50" "30 85" "50 150" "30 170"; do
  set -- $spec; n=$1; span=$2
  for t in 1 2 3 $((span / 8)) $((span / 4)) $((span / 2)); do
    L=$((span - t)); echo "0 $n $t $L"; echo "1 $n $t $L"
  done
done | xargs -P 4 -L 1 sh -c '.build/pair_sa $0 $1 $2 $3 3000000 4 1'
