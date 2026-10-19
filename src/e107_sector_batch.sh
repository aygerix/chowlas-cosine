#!/bin/bash
# E107b: exact b-adic sector violation D for all small sparse automata (src/e107_sector.py). D > 0 => M >= (D - o(1)) n.
mkdir -p examples/e107
s() { python src/e107_sector.py $1 $2 $3 $4 > examples/e107/sector_b$1_S$2.jsonl; }
s 2 2 7; s 2 3 7; s 2 4 7; s 3 2 5; s 3 3 5; s 4 2 4; s 5 2 4; s 4 3 4 300000
echo E107b sector done
