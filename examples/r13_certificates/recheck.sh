#!/bin/bash
set -e
python .research/agents/tdense13_scratch/binary_probe.py milp_only
python .research/agents/tdense13_scratch/audit.py
