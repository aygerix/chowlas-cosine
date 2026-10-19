#!/bin/bash
set -euo pipefail
s=.research/agents/tdense15_scratch
mkdir -p /tmp/r15v && cp -r $s /tmp/r15v/
python $s/mixing_sturm.py > /tmp/r15v/sturm.log 2>&1; tail -3 /tmp/r15v/sturm.log
python $s/certify_sigma.py examples/e95/discovery_sigma0.6667_K64_d10_s0.1_t0.json 1/10000 73/1000 > /tmp/r15v/cert.log 2>&1; tail -4 /tmp/r15v/cert.log
python $s/verify_sigma.py > /tmp/r15v/ver.log 2>&1; tail -6 /tmp/r15v/ver.log
