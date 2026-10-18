#!/bin/sh
# even-lambda symmetric route: tabu over D = H ∪ (c − H), lambda in {2,4,6}; then actual R(A) of the best sets
cd .research/agents/lambda_scratch
cc -O3 -march=native -o bin/symtabu symtabu.c -lm
for lam in 2 4 6; do for k in 10 14 18 22 26 30; do for m in 12 15 20 30; do
  c=$(( m * k * k / (20 * lam) )); [ $c -le $((k + 2)) ] && c=$((k + 3))
  for s in 1 2; do echo "$lam $k $c 20000 $s"; done
done; done; done | xargs -P 4 -n 5 sh -c 'bin/symtabu $0 $1 $2 $3 $4' > out/symtabu.txt
python3 - <<'PY'
import re
best = {}
for line in open("out/symtabu.txt"):
    m = re.search(r"lam=(\d+) k=(\d+) c=(\d+) \|A\|=(\d+) Wp=(\d+) .* Rn'=([\d.]+) D=(\S+)", line)
    if not m: continue
    key = (int(m.group(1)), int(m.group(2))); v = float(m.group(6))
    if key not in best or v < best[key][0]: best[key] = (v, line)
with open("out/symtabu_best.txt", "w") as f:
    for key in sorted(best): f.write(best[key][1])
PY
python3 evalR.py --file out/symtabu_best.txt > out/evalR_sym.txt
python3 evalR.py --file cands_signed.txt > out/evalR_signed.txt
echo done
