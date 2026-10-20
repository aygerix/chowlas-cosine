#!/bin/bash
# E118b: direct K-minimising SA (one rep per class, R = 1) on the deep JL set p = 3, a = 4 (λ_odd = 0.935), against
# the a = 2, 3 scan values. Output examples/e118/deep.jsonl.
for s in 1 2; do python src/e116_fd_driver.py 3 4 1 1 1500000 $s box; done >> examples/e118/deep.jsonl
