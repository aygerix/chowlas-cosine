#!/bin/bash
# E54: adversarial test of PROOFS P31-C(a) (every A ⊂ (X/2, X] has M >= 0.370 √|A|): SA over DYADIC sets (density 0 on
# [1, X/2], ramp to d2 on [0.5X, 0.55X], d2 on [0.55X, X]). How far is 0.370 from the best findable R?
# Output: examples/profile_sa/e54.jsonl
cd ~/chowla_cosine && mkdir -p src/.build examples/profile_sa
cc -O3 -march=native -o src/.build/profile_sa src/profile_sa.c -lm || exit 1
P=${1:-6}
{
for seed in 1 2 3; do
  echo "0 526 100.5 0.0 10 3000000 6 $seed 0.6"     # upper-half density 0.6, n ≈ 150
  echo "0 1052 100.5 0.0 10 3000000 6 $seed 0.6"    # n ≈ 300
  echo "0 1052 100.5 0.0 10 3000000 6 $seed 0.3"    # upper-half density 0.3, n ≈ 150
  echo "0 2104 100.5 0.0 10 3000000 6 $seed 0.3"    # n ≈ 300
done
} | xargs -P $P -L 1 sh -c 'src/.build/profile_sa "$@" >> examples/profile_sa/e54.jsonl' _
echo done
