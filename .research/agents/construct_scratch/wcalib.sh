#!/bin/bash
D=.research/agents/construct_scratch; B=$D/bin; mkdir -p $B $D/runs/wl
cc -O3 -march=native -o $B/wlns $D/wlns.c -lm || exit 1
W=${1:-26}; T=${2:-90}
$B/wlns 52 36 0 1 $T $D/runs/calib_X52_N36_s1.A $W > $D/runs/wl/c36a.txt &
$B/wlns 52 36 0 2 $T $D/runs/calib_X52_N36_s2.A $W > $D/runs/wl/c36b.txt &
$B/wlns 60 42 0 3 $T $D/runs/calib_X60_N42_s1.A $W > $D/runs/wl/c42a.txt &
$B/wlns 60 42 0 4 $T $D/runs/calib_X60_N42_s2.A $W > $D/runs/wl/c42b.txt &
wait
for f in c36a c36b c42a c42b; do grep -h "START\|FINAL" $D/runs/wl/$f.txt | cut -c1-90; done
