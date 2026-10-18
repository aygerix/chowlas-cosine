#!/bin/sh
# E35 batch (run ON dirichlet via src/dirun.sh): lambda-fold ruler SA over a (lambda, k, L) grid, 4 jobs in parallel.
set -e
mkdir -p src/.build examples/lambda_ruler
cc -O3 -march=native -o src/.build/lambda_ruler_sa src/lambda_ruler_sa.c -lm
ITERS=${ITERS:-50000000}; RESTARTS=${RESTARTS:-4}
for lam in 2 3 4; do for k in 8 10 12 15 18 21 24 30; do
  base=$(( k * k / (2 * lam) )); [ $base -lt $k ] && base=$k
  for mult in 10 15 25 40; do L=$(( base * mult / 10 )); [ $L -le $k ] && L=$((k + 2))
    echo "$lam $k $L"; done; done; done |
  xargs -P ${CHOWLA_WORKERS:-4} -n 3 sh -c 'src/.build/lambda_ruler_sa $0 $1 $2 '"$ITERS $RESTARTS"' 1' \
  > examples/lambda_ruler/e35_grid.txt
sort -t= -k2,2n examples/lambda_ruler/e35_grid.txt > /dev/null
echo done
