#!/bin/bash
# E59: R(n) trend for SMOOTH profiles at larger n: triangle (p=1, P31-covered) vs (1-t)^2, (1-t)^3 (escape class at
# small scales). n ≈ 600 and 1200. Output: examples/profile_sa/e59.jsonl
cd ~/chowla_cosine && mkdir -p src/.build examples/profile_sa
cc -O3 -march=native -o src/.build/profile_sa src/profile_sa.c -lm || exit 1
P=${1:-6}
{
for seed in 1; do
  echo "0 1200 1 1 10 6000000 4 $seed"; echo "0 2400 1 1 10 6000000 4 $seed"
  echo "0 1800 2 1 10 6000000 4 $seed"; echo "0 3600 2 1 10 6000000 4 $seed"
  echo "0 2400 3 1 10 6000000 4 $seed"; echo "0 4800 3 1 10 6000000 4 $seed"
done
} | xargs -P $P -L 1 sh -c 'src/.build/profile_sa "$@" >> examples/profile_sa/e59.jsonl' _
echo done
