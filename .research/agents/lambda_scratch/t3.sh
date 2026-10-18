#!/bin/sh
cd .research/agents/lambda_scratch
cc -O3 -march=native -o bin/bb_lambda bb_lambda.c
( /usr/bin/time -f "%es MD3 MF0" bin/bb_lambda 3 12 36 66 3 0 ) 2>&1 &
( /usr/bin/time -f "%es MD3 MF4" bin/bb_lambda 3 12 36 66 3 4 ) 2>&1 &
( /usr/bin/time -f "%es MD5 MF6" bin/bb_lambda 3 12 36 66 5 6 ) 2>&1 &
( /usr/bin/time -f "%es MD4 MF12" bin/bb_lambda 3 12 36 66 4 12 ) 2>&1 &
wait
