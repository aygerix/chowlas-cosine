import json, math
from collections import defaultdict
L=[json.loads(l) for l in open('examples/e108/mu_all.jsonl')]
g=defaultdict(list)
for r in L:
    if 'minRe' not in r: continue
    a=math.log(r['lam'])/math.log(r['b']); S=len(r['delta'])
    ab=min(int(a*10),9)/10
    g[(r['b'],S,ab)].append(r['minRe'])
print("b S alpha-bin  count  max_minRe (closest to PD)")
for k in sorted(g):
    v=g[k]; print(k[0],k[1],f"{k[2]:.1f}-{k[2]+0.1:.1f}",len(v),f"{max(v):+.4f}")
