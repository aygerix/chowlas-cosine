#!/bin/bash
# E119b: taper-random one-rep lifts at p = 17..31 (crossover test of the 0.92p² law; corrected noise law 1.25√(|D| ln n²)
# predicts K ≈ 716 (p = 29), 799 (p = 31) < 0.92p² = 774, 884). Grid oversampling 4 for p >= 23.
out=examples/e119/taper_large.jsonl
python src/e119_taper_random.py 17 3 8 >> $out
python src/e119_taper_random.py 19 3 8 >> $out
python src/e119_taper_random.py 23 3 4 >> $out
python src/e119_taper_random.py 29 3 4 >> $out
python src/e119_taper_random.py 31 3 4 >> $out
