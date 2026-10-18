#!/bin/sh
# Batch 1: exact per-L optima (span exactly L) for lam = 3 (k = 10, 11, 12) and lam = 4 (k = 4..11).
cd .research/agents/lambda_scratch
cc -O3 -march=native -o bin/bb_lambda bb_lambda.c
mkdir -p out
python driver.py 3 10 9 60 full 4 > out/ex3_k10.txt
python driver.py 4 4 3 40 full 4 > out/ex4_k4.txt
python driver.py 4 5 4 40 full 4 > out/ex4_k5.txt
python driver.py 4 6 5 40 full 4 > out/ex4_k6.txt
python driver.py 4 7 6 40 full 4 > out/ex4_k7.txt
python driver.py 4 8 7 40 full 4 > out/ex4_k8.txt
python driver.py 4 9 8 40 full 4 > out/ex4_k9.txt
python driver.py 4 10 9 40 3 4 > out/ex4_k10.txt
python driver.py 3 11 10 50 2 4 > out/ex3_k11.txt
python driver.py 4 11 10 36 3 4 > out/ex4_k11.txt
python driver.py 3 12 11 46 0 4 > out/ex3_k12.txt
