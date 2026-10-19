import json, sys
from collections import Counter
L=[json.loads(l) for l in open(sys.argv[1])]
print(len(L), Counter((r['status'], r.get('certified')) for r in L))
c=[r for r in L if r.get('certified')]
c.sort(key=lambda r: -r['bound_upper'])
print("weakest certified bounds (Re nu^(t) < bound):")
for r in c[:5]: print(f"  b={r['b']} lam={r['lam']:.4f} t={r['t']} h={r['h']} bound={r['bound_upper']:.5f} delta={r['delta']}")
bad=[r for r in L if not r.get('certified')]
print("uncertified:", len(bad)); [print(" ", r) for r in bad[:5]]
