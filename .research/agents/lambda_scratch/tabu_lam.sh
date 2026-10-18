#!/bin/sh
# HEURISTIC: how does min W/k scale with lambda?  tabu, lam in {2,...,8}, several k, L = c*k^2/(2 lam).
cd .research/agents/lambda_scratch
cc -O3 -march=native -o bin/tabu_lambda tabu_lambda.c
for lam in 2 3 4 5 6 8; do
 for mult in 2 3 4 5; do
  k=$(( lam * mult + 2 )); [ $k -gt 30 ] && continue
  for c in 10 13 16 20; do
   L=$(( c * k * k / (20 * lam) )); [ $L -le $k ] && L=$((k+1))
   for s in 1 2 3; do echo "$lam $k $L 40000 $s"; done
  done
 done
done | xargs -P ${CHOWLA_WORKERS:-4} -n 5 sh -c 'bin/tabu_lambda $0 $1 $2 $3 $4' > out/tabu_lam.txt
echo done
