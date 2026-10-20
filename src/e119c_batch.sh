#!/bin/bash
# E119c: jointly optimised FREE-subset lift (Bernoulli-taper init, SA on K/√|T|) at p = 11 (advisor: naive vs joint).
python src/e116_sa_driver.py 11 2 1 121 6000000 1 >> examples/e119/free_p11.jsonl
