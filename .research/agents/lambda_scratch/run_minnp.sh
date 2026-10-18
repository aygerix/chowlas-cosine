#!/bin/sh
# exhaustive min n_p (p = 2, 3) over D ⊂ [0,L], 0,L ∈ D, |D| = k
cd .research/agents/lambda_scratch
mkdir -p bin out
cc -O3 -march=native -o bin/minnp minnp.c
( for k in 3 4 5 6 7 8 9; do bin/minnp 3 $k 24; done > out/minnp3_a.txt ) &
( for k in 10 11; do bin/minnp 3 $k 22; done > out/minnp3_b.txt ) &
( for k in 3 4 5 6 7 8 9; do bin/minnp 2 $k 24; done > out/minnp2_a.txt ) &
( for k in 10 11; do bin/minnp 2 $k 22; done > out/minnp2_b.txt ) &
wait
