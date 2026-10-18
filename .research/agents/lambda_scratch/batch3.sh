#!/bin/sh
# Batch 3: exact per-L optima for lam = 3 restricted to B_2[3] sets (no class with r > 3), k = 10..16.
cd .research/agents/lambda_scratch
cc -O3 -march=native -o bin/bb_strict bb_lambda.c
export BB_STRICT=1 BB_BIN=bb_strict
for k in 10 11 12 13; do python driver.py 3 $k $((k+2)) 64 3 4 > out/strict3_k$k.txt; done
python driver.py 3 14 16 64 3 4 > out/strict3_k14.txt
python driver.py 3 15 18 64 0 4 > out/strict3_k15.txt
python driver.py 3 16 20 64 0 4 > out/strict3_k16.txt
