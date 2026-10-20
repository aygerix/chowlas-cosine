#!/bin/bash
# E120: certified sup_T |T|/K(T)² over symmetric T ⊂ P_L (Dinkelbach MIQP, Gurobi, lazy cuts). Advisor's item (3).
out=examples/e120/ratio.jsonl
python src/e116_jl_taper.py ratio 3 2 1 9 0.8 1800 4 >> $out
python src/e116_jl_taper.py ratio 3 2 1 9 0.8 1800 4 full >> $out
python src/e116_jl_taper.py ratio 5 2 1 25 0.30 10800 4 >> $out
python src/e116_jl_taper.py ratio 7 2 1 49 0.20 10800 4 >> $out
