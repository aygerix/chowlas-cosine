#!/bin/sh
cd .research/agents/lambda_scratch
cc -O3 -march=native -o bin/bb_lambda bb_lambda.c
mkdir -p out
/usr/bin/time -f "%es" bin/bb_lambda 3 12 36 66
/usr/bin/time -f "%es" bin/bb_lambda 3 12 36 14
for k in 4 5 6 7 8; do python driver.py 3 $k $((k-1)) 40 full 4 > out/ex3_k$k.txt; done
python driver.py 3 9 8 45 full 4 > out/ex3_k9.txt
tail -n 2 out/ex3_k*.txt
