#!/bin/sh
cd .research/agents/lambda_scratch
cc -O3 -march=native -o bin/tabu_lambda tabu_lambda.c
for s in 1 2 3 4; do echo "3 10 24 20000 $s"; echo "3 11 28 20000 $s"; echo "3 12 35 20000 $s"; echo "4 11 22 20000 $s"; done |
  xargs -P 4 -n 5 sh -c '/usr/bin/time -f "%es" bin/tabu_lambda $0 $1 $2 $3 $4 2>&1' | paste - - 
