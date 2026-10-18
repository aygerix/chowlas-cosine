#!/bin/sh
# tabu L-scan for k = 13 (validation: exact def 15 at L = 42) and k = 14, 15, 16 (L around 1.3-1.8 k^2/6)
cd .research/agents/lambda_scratch
cc -O3 -march=native -o bin/tabu_lambda tabu_lambda.c
( for L in 40 41 42 43 44 45 46 47 48 49 50; do for s in 1 2 3; do echo "3 13 $L 40000 $s"; done; done
  for L in $(seq 42 2 62); do for s in 1 2 3; do echo "3 14 $L 40000 $s"; done; done
  for L in $(seq 48 3 75); do for s in 1 2 3; do echo "3 15 $L 40000 $s"; done; done
  for L in $(seq 56 4 92); do for s in 1 2 3; do echo "3 16 $L 40000 $s"; done; done ) |
  xargs -P 4 -n 5 sh -c 'bin/tabu_lambda $0 $1 $2 $3 $4' > out/tabu_k1316.txt
echo done
