#!/bin/bash
D=.research/agents/construct_scratch; B=$D/bin; mkdir -p $B
cc -O3 -march=native -o $B/coretail $D/coretail.c -lm || exit 1
$D/ct_run.sh n45y36 64 45 36 3 3.93
$D/ct_run.sh n45y38 64 45 38 3 3.93
$D/ct_run.sh n50y40 71 50 40 3 4.16
$D/ct_run.sh n50y42 71 50 42 3 4.16
