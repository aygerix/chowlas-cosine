#!/bin/bash
# exact-window LNS (wlns) from structured core+tail seeds; usage: large_n.sh N X T w [cf]
D=.research/agents/construct_scratch; B=$D/bin; mkdir -p $B $D/runs/ln
[ -x $B/wlns ] || cc -O3 -march=native -o $B/wlns $D/wlns.c -lm || exit 1
N=$1; X=$2; T=$3; W=$4; CF=${5:-0.84}
for s in 1 2 3 4; do
  python3 $D/seeds.py $N $X $CF $((1 + s % 3)) $((100*N + s)) > $D/runs/ln/seed_N${N}_s$s.txt
  $B/wlns $X $N 0 $s $T $D/runs/ln/seed_N${N}_s$s.txt $W 20000000 300 > $D/runs/ln/wl_N${N}_X${X}_s$s.txt &
done
wait
for s in 1 2 3 4; do grep -h "START\|FINAL" $D/runs/ln/wl_N${N}_X${X}_s$s.txt | cut -c1-100; done
