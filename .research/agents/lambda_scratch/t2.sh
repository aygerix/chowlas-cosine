#!/bin/sh
cd .research/agents/lambda_scratch
mkdir -p bin
cc -O3 -march=native -o bin/bb_lambda bb_lambda.c
( /usr/bin/time -f "%es" bin/bb_lambda 3 12 36 66 ) 2>&1 &
( /usr/bin/time -f "%es" bin/bb_lambda 3 12 50 66 ) 2>&1 &
( /usr/bin/time -f "%es" bin/bb_lambda 3 12 50 15 ) 2>&1 &
( timeout 600 /usr/bin/time -f "%es" bin/bb_lambda 3 14 40 91 ) 2>&1 &
wait
