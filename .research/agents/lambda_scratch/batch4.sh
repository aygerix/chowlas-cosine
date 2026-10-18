#!/bin/sh
cd .research/agents/lambda_scratch
cc -O3 -march=native -o bin/bb_lambda bb_lambda.c
python driver2.py 3 13 12 46 18 4 > out/dec3_k13.txt
python driver2.py 3 14 39 44 19 4 > out/dec3_k14b.txt
sh tabu_lam.sh
