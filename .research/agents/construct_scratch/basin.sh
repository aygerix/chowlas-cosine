#!/bin/bash
# basin test: perturb the N=36 exhaustive optimum by k random swaps inside [1,52], run dsearch 15 s, report best R
D=.research/agents/construct_scratch; B=$D/bin; mkdir -p $B $D/runs/basin
cc -O3 -march=native -o $B/dsearch $D/dsearch.c -lm || exit 1
OPT="1 2 3 4 5 6 7 8 9 10 11 13 14 15 16 17 18 19 20 21 22 23 25 26 27 28 29 30 31 34 35 37 44 45 48 50"
for k in 1 2 3 4 6 8; do
  for s in 1 2 3 4; do
    python3 - "$k" "$s" "$OPT" > $D/runs/basin/init_k${k}_s$s.txt <<'PY'
import sys, random
k, s = int(sys.argv[1]), int(sys.argv[2]); A = set(map(int, sys.argv[3].split()))
random.seed(1000 * k + s)
for _ in range(k):
    a = random.choice(sorted(A)); b = random.choice([n for n in range(1, 53) if n not in A]); A.remove(a); A.add(b)
print(" ".join(map(str, sorted(A))))
PY
    $B/dsearch 52 36 0 1000000000 $s 8 3 $D/runs/basin/init_k${k}_s$s.txt 15 > $D/runs/basin/out_k${k}_s$s.txt &
  done
  wait
  echo "k=$k: $(grep -h FINAL $D/runs/basin/out_k${k}_s*.txt | sed 's/.*R=\([0-9.]*\).*/\1/' | tr '\n' ' ')"
done
