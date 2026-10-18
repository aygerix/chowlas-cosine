#!/bin/sh
mkdir -p .build && cc -O3 -march=native -o .build/e39 src/e39_lam_exact.c || exit 1
printf "3 6 5 40\n3 7 6 40\n3 8 7 40\n3 9 8 36\n3 10 9 30\n3 11 10 30\n" | xargs -P 4 -L 1 sh -c '.build/e39 $0 $1 $2 $3 > examples/lambda_verify/k$1.txt'
grep RESULT examples/lambda_verify/k*.txt
