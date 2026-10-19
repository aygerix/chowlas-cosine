#!/bin/bash
mkdir -p examples/e105
for L in 8 16 32; do for g in 1.25 1.3334 1.5 2.0; do
  python src/e105_pr_largepeak.py $L $g 150 | tail -1 >> examples/e105/e105.jsonl &
done; wait; done
cat examples/e105/e105.jsonl
