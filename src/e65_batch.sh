#!/bin/bash
# E65 batch (queued after E64 stream A): one Bu step at k = 12..24 (Singer q = 11..23) by annealing.
while pgrep -f "e64_batch.sh 7 9 11" > /dev/null; do sleep 60; done
python src/e65_driver.py 11 13 17 19 23 --iters 20000000 --restarts 2 > examples/e65/e65_run.log 2>&1
