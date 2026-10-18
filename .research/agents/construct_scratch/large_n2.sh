#!/bin/bash
# exact-window LNS from Tukey-profile seeds; usage: large_n2.sh N X T w a1 a2 a3 a4
D=.research/agents/construct_scratch; B=$D/bin; mkdir -p $B $D/runs/ln
[ -x $B/wlns ] || cc -O3 -march=native -o $B/wlns $D/wlns.c -lm || exit 1
N=$1; X=$2; T=$3; W=$4; shift 4
s=0
for a in "$@"; do s=$((s+1))
  python3 $D/seeds2.py $N $X $a $((200*N + s)) > $D/runs/ln/tseed_N${N}_a$a.txt
  $B/wlns $X $N 0 $((50+s)) $T $D/runs/ln/tseed_N${N}_a$a.txt $W 20000000 300 > $D/runs/ln/twl_N${N}_X${X}_a$a.txt &
done
wait
for a in "$@"; do echo "a=$a $(grep -h "START\|FINAL" $D/runs/ln/twl_N${N}_X${X}_a$a.txt | cut -c1-60 | tr '\n' ' ')"; done
