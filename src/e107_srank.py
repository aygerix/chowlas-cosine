import json, glob
rows=[]
for fn in sorted(glob.glob('examples/e107/sector_*.jsonl')):
    for l in open(fn):
        r=json.loads(l); r['f']=fn.split('/')[-1]; rows.append(r)
print("total", len(rows))
import collections
by=collections.defaultdict(list)
for r in rows: by[r['f']].append(r)
for f,rs in by.items():
    rs.sort(key=lambda r:r['D'])
    print(f, len(rs), "minD=%.4f"%rs[0]['D'], "min h0=%.4f"%min(r['h0'] for r in rs))
rows.sort(key=lambda r:r['D'])
for r in rows[:12]:
    print(f"b={r['b']} lam={r['lam']:.3f} D={r['D']:.4f} kD={r['kD']} h0={r['h0']:.4f} delta={r['delta']}")
