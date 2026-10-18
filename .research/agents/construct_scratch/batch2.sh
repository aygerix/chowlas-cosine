#!/bin/bash
D=.research/agents/construct_scratch; B=$D/bin; mkdir -p $B
cc -O3 -march=native -fopenmp -o $B/coretail_omp $D/coretail_omp.c -lm || exit 1
# validation on N=42 (known optimum 3.7518844 in C(60,42,36,3)), then N=50 classes with tight thresholds
$D/cto_run.sh o42 60 42 36 3 3.76
$D/cto_run.sh o50y40 71 50 40 3 4.0484
$D/cto_run.sh o50y42 71 50 42 3 4.0484
$D/cto_run.sh o50y38x72 72 50 38 2 4.0484
