#!/bin/bash
# E119d: one-rep SA (taper init) at p = 17. Pre-registered: 0.92p² = 266; random taper lifts 303–314 (E119b);
# if SA keeps ≈ 0.65 × random (p <= 7), K_SA ≈ 200 < 266 refutes the p² law for OPTIMISED lifts at p = 17.
python src/e116_fd_driver.py 17 2 1 1 2500000 1 taper >> examples/e119/sa_p17.jsonl
