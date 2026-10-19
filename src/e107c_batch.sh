#!/bin/bash
# E107c: anneal larger automata to minimise the sector violation D (src/e107_sa.py). 8 parallel runs.
mkdir -p examples/e107
run() { python src/e107_sa.py $1 $2 $3 $4 $5 > examples/e107/sa_b$1_S$2_s$5.jsonl; }
run 2 8 6 3000 1 & run 2 10 6 3000 2 & run 3 6 4 3000 3 & run 3 8 4 3000 4 &
run 4 5 3 3000 5 & run 4 6 3 3000 6 & run 5 5 3 3000 7 & run 6 4 3 3000 8 &
wait
echo E107c done
