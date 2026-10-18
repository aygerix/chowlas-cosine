#!/bin/sh
# E44: Gurobi full-box dense optima (src/grb_dense.py), warm-started from the best certified/class sets.
# Usage (on dirichlet via dirun.sh): sh src/e44_grb_dense.sh THREADS TL
TH=${1:-5}; TL=${2:-14400}
python src/grb_dense.py 64 45 --tl $TL --threads $TH --grid 4 --nodecuts 0 --warm examples/milp/N45_best.json --out examples/gurobi/dense_N45_X64.json
python src/grb_dense.py 72 50 --tl $TL --threads $TH --grid 4 --nodecuts 0 --warm examples/construct/N50_certified.json --out examples/gurobi/dense_N50_X72.json
python src/grb_dense.py 79 55 --tl $TL --threads $TH --grid 4 --nodecuts 0 --warm examples/gurobi/warm_N55.json --out examples/gurobi/dense_N55_X79.json
