#!/bin/bash
# usage: cto_run.sh tag X N Y h thr [G] [hmin]   -- OpenMP coretail (shared threshold, 4 threads)
D=.research/agents/construct_scratch; B=$D/bin; mkdir -p $B $D/runs/ct
[ -x $B/coretail_omp ] || cc -O3 -march=native -fopenmp -o $B/coretail_omp $D/coretail_omp.c -lm || exit 1
tag=$1; shift
OMP_NUM_THREADS=${CHOWLA_WORKERS:-4} $B/coretail_omp $1 $2 $3 $4 $5 ${6:-0} 1 0 ${7:-1} > $D/runs/ct/${tag}.txt
echo "== $tag X=$1 N=$2 Y=$3 h=$4 thr0=$5"
grep -h DONE $D/runs/ct/${tag}.txt | awk '{print $8, $9, $10, $11, $12, $13, $14, $15}'
grep -h IMPROVE $D/runs/ct/${tag}.txt | tail -1 | cut -c1-300
