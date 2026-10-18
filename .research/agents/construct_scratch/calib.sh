#!/bin/bash
# calibration of dsearch against exhaustive optima (N=36 in [1,52]: 0.56479; N=41 in [1,57]: 0.57404; N=42 in [1,60]: 0.57896)
D=.research/agents/construct_scratch; B=$D/bin; mkdir -p $B $D/runs
cc -O3 -march=native -o $B/dsearch $D/dsearch.c -lm || exit 1
T=${1:-60}
for cfg in "52 36" "57 41" "60 42"; do
  set -- $cfg
  for s in 1 2 3 4; do
    mode=$(( (s-1) % 3 ))
    $B/dsearch $1 $2 0 1000000000 $s 8 $mode 0.62 $T > $D/runs/calib_X$1_N$2_s$s.txt &
  done
  wait
  grep -h FINAL $D/runs/calib_X$1_N$2_s*.txt | cut -c1-80
done
