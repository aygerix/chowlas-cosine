#!/bin/bash
# E64 second level: D = Bu set (k = 6, 7), Mt = (1+eps) M(D). Queued after stream B.
while pgrep -f "e64_batch.sh 8 10 12" > /dev/null; do sleep 60; done
python src/e64_make_bu_D.py 6 7
for k in 6 7; do
  for eps in 0.05 0.15; do
    python src/e64_bu_step.py 0 --D-file examples/e64/D_bu_k$k.json --eps $eps --tl 2400 --threads 2 \
      --out examples/e64/e64_bu2.jsonl > examples/e64/run_bu2_k${k}_$eps.log 2>&1
  done
done
