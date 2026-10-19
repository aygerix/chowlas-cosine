#!/bin/bash
# E95: D_sigma discovery (Gurobi, 4 threads), sigma = 1 (reproduction) and sigma = 2/3 (P66).
set -e
python src/e95_discover_sigma.py 64 10 0.2 0 1.0
python src/e95_discover_sigma.py 64 10 0.2 0 0.6666666666666666
for s in 0.1 0.3 0.5; do python src/e95_discover_sigma.py 64 10 $s 0 0.6666666666666666; done
