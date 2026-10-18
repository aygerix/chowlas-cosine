#!/bin/bash
# mechanism tests M-B (multi-residue profiles) and M-D (dense real squares); 2 cores each
D=.research/agents/construct_scratch; mkdir -p $D/runs/mech
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python $D/mres_profile.py 120 1,2,3,4,6 10 > $D/runs/mech/mres_K120.jsonl 2>&1 &
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python $D/dense_square.py 40,80,160 6 > $D/runs/mech/dsq.jsonl 2>&1 &
wait
grep best $D/runs/mech/mres_K120.jsonl; grep -v trial $D/runs/mech/dsq.jsonl | cut -c1-200
