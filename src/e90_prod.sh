#!/bin/bash
# E90 production: large-q tabu search (seed 2026101990 + job index); 4 parallel jobs
mkdir -p examples/e90 src/.build
gcc -O3 -march=native -o src/.build/e90_zp_tabu src/e90_zp_tabu.c -lm || exit 1
i=0
for q in 149 151 197 293 307 401 601 607 797 1009 1019 1201 1601 2003; do
  for beta in 3 5; do
    i=$((i+1)); echo "src/.build/e90_zp_tabu $q 200000 2 0 $((2026101990+i)) $beta"
  done
  if [ $((q % 4)) -eq 1 ]; then i=$((i+1)); echo "src/.build/e90_zp_tabu $q 200000 1 2 $((2026101990+i)) 3"; fi
done | xargs -P 4 -I{} bash -c "{}" > examples/e90/prod.txt
sort -t= -k2 -n examples/e90/prod.txt | cut -c1-170
