#!/bin/bash
# class B&B scan over N: X = round(1.42 N)+1, Y = round(0.82 N), h holes, thr0 = 0.58 sqrt(N) (sets with R < 0.58 only)
# usage: nscan.sh BIN h N1 N2 [ratioY] [thrR]
D=.research/agents/construct_scratch; B=$D/bin; mkdir -p $B $D/runs/scan
cc -O3 -march=native -fopenmp -o $B/coretail_omp $D/coretail_omp.c -lm || exit 1
cc -O3 -march=native -fopenmp -o $B/coretail2 $D/coretail2.c -lm || exit 1
BIN=$1; H=$2; RY=${5:-0.82}; TR=${6:-0.58}
export OMP_NUM_THREADS=${CHOWLA_WORKERS:-4}
for N in $(seq $3 $4); do
  X=$(python3 -c "print(round(1.42*$N)+1)"); Y=$(python3 -c "print(round($RY*$N))"); T=$(python3 -c "print($TR*$N**0.5)")
  $B/$BIN $X $N $Y $H $T 0 1 0 1 > $D/runs/scan/N${N}_X${X}_Y${Y}_h${H}.txt
  echo "N=$N X=$X Y=$Y h=$H thr0=$T :: $(grep DONE $D/runs/scan/N${N}_X${X}_Y${Y}_h${H}.txt | grep -o 'nodes=[0-9]*\|best_M=[0-9.]*\|R=[0-9.]*\|t=[0-9.]*' | tr '\n' ' ')"
done
