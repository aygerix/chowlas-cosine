#!/bin/bash
# E116 spread test: do one-rep lifts with reps in [−Rn, Rn]² (R = 2, 3) beat R = 1? (P77's bound weakens with spread.)
out=examples/e116/spread.jsonl
for s in 1 2; do for R in 2 3; do
  python src/e116_fd_driver.py 5 2 1 $R 300000 $s box >> $out
  python src/e116_fd_driver.py 5 2 1 $R 300000 $s rand >> $out
done; done
