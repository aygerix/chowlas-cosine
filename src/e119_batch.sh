#!/bin/bash
# E119: p² law vs noise law for one-rep JL lifts. Pre-registered predictions (CSTAR A10, written before the run):
# advisor K ≈ 0.92p² = 111 (p = 11), 155 (p = 13); lead (taper-random) K ≈ 101, 132, and SA-optimised <= taper-random.
out=examples/e119/scaling.jsonl
for p in 3 5 7 11 13; do python src/e119_taper_random.py $p 4 >> $out; done
python src/e118_cvp.py 11 2 1 30 1 >> $out
python src/e118_cvp.py 13 2 1 30 1 >> $out
python src/e116_fd_driver.py 11 2 1 1 1500000 1 taper >> $out
python src/e116_fd_driver.py 13 2 1 1 2500000 1 taper >> $out
python src/e116_fd_driver.py 11 2 1 1 1500000 2 box >> $out
