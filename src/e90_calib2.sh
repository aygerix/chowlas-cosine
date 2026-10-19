#!/bin/bash
mkdir -p examples/e90 src/.build
gcc -O3 -march=native -o src/.build/e90_zp_tabu src/e90_zp_tabu.c -lm || exit 1
for q in 83 89; do
  for beta in 3 10 20; do
    echo "src/.build/e90_zp_tabu $q 200000 4 0 $((q*7+${beta})) $beta"
  done
done | xargs -P 4 -I{} bash -c "{}" > examples/e90/calib2.txt
cut -c1-150 examples/e90/calib2.txt
