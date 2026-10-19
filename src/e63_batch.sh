#!/bin/bash
# E63: are near-optimal DENSE sets front-loaded?  Free SA (profile_sa mode 1: any element <-> any non-element in [1,X]) at
# density 1/C, C in {2.5,3,4,6,8}, X in {150,300}; then src/e63_post.py computes R, front ratio and the P31 lower bound of
# every optimum.  If optima are NOT front-loaded, P31 already covers the numerically relevant dense sets (target T-dense).
cd ~/chowla_cosine && mkdir -p src/.build examples/e63
cc -O3 -march=native -o src/.build/profile_sa src/profile_sa.c -lm || exit 1
P=${1:-6}
: > examples/e63/e63_raw.jsonl
{
for X in 150 300; do for C in 2.5 3 4 6 8; do for seed in 1 2; do
  c=$(python3 -c "print(1/$C)"); echo "1 $X 0 $c 10 3000000 6 $seed"
done; done; done
} | xargs -P $P -L 1 sh -c 'src/.build/profile_sa "$@" >> examples/e63/e63_raw.jsonl' _
python src/e63_post.py > examples/e63/e63.jsonl
echo done
