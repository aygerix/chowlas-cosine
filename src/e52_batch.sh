#!/bin/bash
# E52: two-level front-loaded profiles (density d1 on [1, eX], d2 beyond, 0.05X linear ramp) — the simplest profiles in
# P31's escape class (d1 >= 2δ/ρ at every small scale) — vs a non-escape two-level control (d1 = 2δ) and E49's triangle.
# n ≈ 150 and 300. Output: examples/profile_sa/e52.jsonl
cd ~/chowla_cosine && mkdir -p src/.build examples/profile_sa
cc -O3 -march=native -o src/.build/profile_sa src/profile_sa.c -lm || exit 1
P=${1:-6}
{
for seed in 1 2; do
  for X in 600 1200; do
    echo "0 $X 100.2 0.75 10 3000000 6 $seed 0.1219"    # δ=0.25: d1 = 3δ on [1,0.2X], d2 = 0.122   (escape)
    echo "0 $X 100.2 0.50 10 3000000 6 $seed 0.1859"    # δ=0.25: d1 = 2δ (control, P31-covered)
  done
  for X in 1000 2000; do
    echo "0 $X 100.25 0.45 10 3000000 6 $seed 0.0480"   # δ=0.15: d1 = 3δ on [1,0.25X], d2 = 0.048  (escape)
  done
  for X in 500 1000; do
    echo "0 $X 100.15 0.90 10 3000000 6 $seed 0.1879"   # δ=0.30: d1 = 3δ on [1,0.15X], d2 = 0.188  (escape)
  done
done
} | xargs -P $P -L 1 sh -c 'src/.build/profile_sa "$@" >> examples/profile_sa/e52.jsonl' _
echo done
