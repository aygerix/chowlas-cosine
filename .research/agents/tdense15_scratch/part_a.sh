#!/bin/bash
set -euo pipefail
scratch=.research/agents/tdense15_scratch
python src/e94b_mix_certify.py | tee "$scratch/e94b_rerun.log"
python "$scratch/certify_sigma.py" examples/e95/discovery_sigma0.6667_K64_d10_s0.1_t0.json 1/10000 73/1000 | tee "$scratch/certify_sigma.log"
