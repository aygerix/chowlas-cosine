import json, glob
for f in sorted(glob.glob('examples/e107/sa_*.jsonl')):
    L = [json.loads(l) for l in open(f) if l.strip()]
    if not L: print(f, 0); continue
    r = L[-1]
    print(f, len(L), "D=%s" % (r.get('D', r.get('D_fine'))), "lam=%s kD=%s it=%s final=%s" % (r.get('lam'), r.get('kD'), r.get('it'), r.get('final', False)))
