#!/bin/sh
# HEURISTIC sweep: tabu search for min def at lam = 2, 3, 4 over (k, L = c * k^2 / (2 lam)).
cd .research/agents/lambda_scratch
cc -O3 -march=native -o bin/tabu_lambda tabu_lambda.c
mkdir -p out
for lam in 3 4 2; do
 for k in 13 14 15 16 18 20 22 24 27 30 35 40; do
  for c in 11 14 18 24; do
   L=$(( c * k * k / (20 * lam) )); [ $L -le $k ] && L=$((k+2))
   it=60000; [ $k -ge 22 ] && it=30000; [ $k -ge 30 ] && it=15000
   for s in 1 2; do echo "$lam $k $L $it $s"; done
  done
 done
done | xargs -P 4 -n 5 sh -c 'bin/tabu_lambda $0 $1 $2 $3 $4' > out/tabu_sweep.txt
echo done
