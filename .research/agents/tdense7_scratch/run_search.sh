#!/bin/bash
set -euo pipefail
out=.research/agents/tdense7_scratch
cc -O3 -march=native "$out/pareto.c" -lm -o "$out/pareto_vm"
for mu in 0 0.1 0.3; do
    "$out/pareto_vm" 384 128 "$mu" 300000 2 2026101907
done > "$out/adversarial_128.jsonl"
for mu in 0 0.1; do
    "$out/pareto_vm" 1536 512 "$mu" 180000 1 2026101908
done > "$out/adversarial_512.jsonl"
cat "$out/adversarial_128.jsonl" "$out/adversarial_512.jsonl"
