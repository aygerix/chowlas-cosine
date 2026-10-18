#!/bin/bash
D=.research/agents/construct_scratch; B=$D/bin; mkdir -p $B $D/runs/ct
cc -O3 -march=native -fopenmp -o $B/coretail_omp $D/coretail_omp.c -lm || exit 1
cc -O3 -march=native -fopenmp -o $B/coretail2 $D/coretail2.c -lm || exit 1
export OMP_NUM_THREADS=4
$B/coretail_omp 64 45 36 3 3.8361 0 1 0 1 > $D/runs/ct/sp_plain.txt; echo plain $(grep DONE $D/runs/ct/sp_plain.txt | cut -c60-)
$B/coretail2 64 45 36 3 3.8361 0 1 0 1 6 > $D/runs/ct/sp_pair6.txt; echo pair6 $(grep DONE $D/runs/ct/sp_pair6.txt | cut -c60-)
