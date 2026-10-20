#!/bin/bash
# E116 scaling scan: fundamental-domain lifts (one rep per class) and free Boolean subsets of the lift, p = 3, 5, 7 (a = 2)
# and p = 3, a = 3. Seeds 1–3. Output examples/e116/scan.jsonl.
out=examples/e116/scan.jsonl
for s in 1 2 3; do
  python src/e116_fd_driver.py 3 2 1 1 400000 $s box >> $out
  python src/e116_fd_driver.py 5 2 1 1 400000 $s box >> $out
  python src/e116_fd_driver.py 3 3 1 1 300000 $s box >> $out
  python src/e116_fd_driver.py 7 2 1 1 300000 $s box >> $out
  python src/e116_sa_driver.py 5 2 1 25 3000000 $s >> $out
  python src/e116_sa_driver.py 3 3 1 27 2000000 $s >> $out
  python src/e116_sa_driver.py 7 2 1 49 2000000 $s >> $out
done
