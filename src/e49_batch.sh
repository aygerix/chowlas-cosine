#!/bin/bash
# E49: profile-constrained SA (src/profile_sa.c). Triangle (p=1, covered by P31) vs steep front-loading (p=2,3,
# P31's escape class) vs free calibration, at n ≈ 150 and 300. Output: examples/profile_sa/e49.jsonl
cd ~/chowla_cosine && mkdir -p src/.build examples/profile_sa
cc -O3 -march=native -o src/.build/profile_sa src/profile_sa.c -lm || exit 1
P=${1:-6}
{
for n in 150 300; do
  for seed in 1 2; do
    echo "0 $((2*n)) 1 1 10 3000000 6 $seed"     # triangle, density 1 at 0 (d = 2δ)
    echo "0 $((3*n)) 2 1 10 3000000 6 $seed"     # (1-t)^2, d = 3δ
    echo "0 $((4*n)) 3 1 10 3000000 6 $seed"     # (1-t)^3, d = 4δ
    echo "1 $((2*n)) 1 1 10 3000000 6 $seed"     # free moves, same span as triangle
    echo "1 $((3*n)) 2 1 10 3000000 6 $seed"     # free moves, same span as p=2
  done
done
} | xargs -P $P -L 1 sh -c 'src/.build/profile_sa "$@" >> examples/profile_sa/e49.jsonl' _
echo done
