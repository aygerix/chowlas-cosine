#!/bin/sh
cd .research/agents/lambda_scratch
cc -O3 -march=native -o bin/bb_strict bb_lambda.c
export BB_STRICT=1
/usr/bin/time -f "%es" bin/bb_strict 3 12 35 66
/usr/bin/time -f "%es" bin/bb_strict 3 12 46 66
/usr/bin/time -f "%es" bin/bb_strict 3 13 50 78
