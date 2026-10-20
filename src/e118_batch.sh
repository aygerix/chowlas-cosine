#!/bin/bash
for args in "3 2 1 200 1" "5 2 1 200 1" "7 2 1 100 1" "3 3 1 100 1" "3 3 0 100 1" "5 3 1 30 1" "3 4 1 30 1"; do
  timeout 3000 python src/e118_cvp.py $args
done >> examples/e118/cvp.jsonl 2>> examples/e118/cvp.err
