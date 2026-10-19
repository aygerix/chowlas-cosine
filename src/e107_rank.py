import json, glob, sys, math
rows=[]
for fn in sorted(glob.glob('examples/e107/screen_*.jsonl')):
    for l in open(fn):
        r=json.loads(l); ks=[k for k in r if k.startswith('L')]
        if len(ks)<2: continue
        a,b=sorted(ks,key=lambda k:int(k[1:]))
        r['Ra']=r[a]['R']; r['Rb']=r[b]['R']; r['nb']=r[b]['n']; r['bad']=r[b]['badic_min']; r['ratio']=r['Rb']/r['Ra']
        rows.append(r)
print("total",len(rows))
print("--- smallest R at larger L (n>=100) ---")
for r in sorted([r for r in rows if r['nb']>=100],key=lambda r:r['Rb'])[:15]:
    print(f"b={r['b']} lam={r['lam']:.3f} n={r['nb']} Ra={r['Ra']:.3f} Rb={r['Rb']:.3f} badic={r['bad']:.3f} delta={r['delta']}")
print("--- decreasing R (ratio<1), n>=100 ---")
for r in sorted([r for r in rows if r['nb']>=100],key=lambda r:r['ratio'])[:15]:
    print(f"b={r['b']} lam={r['lam']:.3f} n={r['nb']} Ra={r['Ra']:.3f} Rb={r['Rb']:.3f} badic={r['bad']:.3f} delta={r['delta']}")
