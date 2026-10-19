#!/bin/bash
# E90 calibration: reproduce E41 exact optima (q <= 89) with e90_zp_tabu
mkdir -p examples/e90 src/.build
gcc -O3 -march=native -o src/.build/e90_zp_tabu src/e90_zp_tabu.c -lm || exit 1
for q in 53 79 83 89; do
  for m in 0 3; do
    echo "src/.build/e90_zp_tabu $q 20000 6 $m $((q*10+m)) 6"
  done
done | xargs -P 4 -I{} bash -c "{}" > examples/e90/calib.txt
cat examples/e90/calib.txt | cut -c1-160
