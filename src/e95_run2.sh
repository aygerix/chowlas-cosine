#!/bin/bash
set -e
for s in 0.0 0.05; do python src/e95_discover_sigma.py 64 10 $s 0 0.6666666666666666; done
python src/e95_discover_sigma.py 192 12 0.1 0 0.6666666666666666
