#!/bin/bash
D=.research/agents/construct_scratch; B=$D/bin; mkdir -p $B $D/runs/ct
cc -O3 -march=native -o $B/coretail $D/coretail.c -lm || exit 1
run() { # X N Y h thr tag
  for p in 0 1 2 3; do $B/coretail $1 $2 $3 $4 $5 0 4 $p > $D/runs/ct/$6_p$p.txt & done; wait
  grep -h DONE $D/runs/ct/$6_p*.txt | awk '{print $8, $9, $10, $12, $14}'
  grep -h IMPROVE $D/runs/ct/$6_p*.txt | sort -t= -k2 -n | head -2 | cut -c1-200
}
run 52 36 31 3 3.40 c36
run 57 41 33 2 3.70 c41
run 60 42 36 3 3.76 c42
