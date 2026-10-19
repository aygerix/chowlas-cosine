#!/bin/bash
# E107 screen: all automata with S reachable states (delta[0][0] = 0), sparse (1.05 < lambda < b).
# Output examples/e107/screen_b{b}_S{S}.jsonl. Grid minima (UNCERTIFIED). See src/e107_automatic.py.
mkdir -p examples/e107
s() { python src/e107_automatic.py screen $1 $2 $3 $4 $5 > examples/e107/screen_b$1_S$2.jsonl; }
s 2 2 12 15; s 2 3 12 15; s 3 2 8 10; s 4 2 6 8; s 5 2 5 7
s 2 4 12 15; s 3 3 8 10
s 4 3 6 8 300000
echo E107 screen done
