#!/bin/bash
# usage: ct_run.sh tag X N Y h thr [hmin]   -- 4 parts in parallel, prints summary
D=.research/agents/construct_scratch; B=$D/bin; mkdir -p $B $D/runs/ct
[ -x $B/coretail ] || cc -O3 -march=native -o $B/coretail $D/coretail.c -lm || exit 1
tag=$1; shift
for p in 0 1 2 3; do $B/coretail $1 $2 $3 $4 $5 0 4 $p ${6:-1} > $D/runs/ct/${tag}_p$p.txt & done; wait
echo "== $tag X=$1 N=$2 Y=$3 h=$4 thr0=$5"
grep -h DONE $D/runs/ct/${tag}_p*.txt | awk '{print $8, $10, $11, $14, $15}'
grep -h IMPROVE $D/runs/ct/${tag}_p*.txt | sort -t= -k2 -n | head -1 | cut -c1-260
