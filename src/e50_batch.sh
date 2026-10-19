#!/bin/bash
# E50: power-law profiles min(1, c (a/X)^{-alpha}) (front-loaded at every scale: P31's escape class) vs E49's triangle.
# n ≈ 150 and 300 (X chosen per profile). Output: examples/profile_sa/e50.jsonl
cd ~/chowla_cosine && mkdir -p src/.build examples/profile_sa
cc -O3 -march=native -o src/.build/profile_sa src/profile_sa.c -lm || exit 1
P=${1:-6}
{
for seed in 1 2; do
  echo "0 417 -0.5 0.2 10 3000000 6 $seed"    # alpha 0.5, c 0.2: n/X ≈ 0.36  -> n ≈ 150
  echo "0 833 -0.5 0.2 10 3000000 6 $seed"    #                                 n ≈ 300
  echo "0 610 -0.7 0.1 10 3000000 6 $seed"    # alpha 0.7, c 0.1: n/X ≈ 0.246 -> n ≈ 150
  echo "0 1220 -0.7 0.1 10 3000000 6 $seed"   #                                 n ≈ 300
  echo "0 900 -0.85 0.05 10 3000000 6 $seed"  # alpha 0.85, c 0.05: steeper, n/X ≈ 0.17
done
} | xargs -P $P -L 1 sh -c 'src/.build/profile_sa "$@" >> examples/profile_sa/e50.jsonl' _
echo done
