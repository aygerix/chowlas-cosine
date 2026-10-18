#!/bin/sh
set -e
cd .research/agents/lambda_scratch
mkdir -p bin
cc -O3 -march=native -o bin/bb_lambda bb_lambda.c
for L in 15 20 24; do /usr/bin/time -f "%es" bin/bb_lambda 3 10 $L 45; done
for L in 15 20 24; do python cpsat_lambda.py 3 10 $L $L 120 4; done
