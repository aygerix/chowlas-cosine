"""Fill in the remaining Task-3 joint-certificate rows, on the VM only."""
import json
from pathlib import Path
import math
import sys
import numpy as np
sys.path.insert(0,'.research/agents/tdense17_scratch')
from fourway import metrics

ROOT=Path('.research/agents/tdense17_scratch')


def main():
    rng=np.random.default_rng(171705)
    sets=[]
    for alpha in (.05,.25,.5):
        A=np.flatnonzero(rng.random(2048)<alpha)+1
        sets.append((f'flat_random_{alpha}',A))
    for pieces in (8,32):
        A=[1000*j+a for j in range(1,pieces+1) for a in range(1,17)]
        sets.append((f'many_AP_{pieces}_gap1000',A))
        A=[1000*j+a for j in range(1,pieces+1) for a in range(1,33)
           if abs((a*math.sqrt(2)+.5)%1-.5)<.28
           and abs((a*math.sqrt(3)+.5)%1-.5)<.28]
        sets.append((f'many_Bohr_{pieces}_gap1000',A))
    recs=[]
    for name,A in sets:
        rec=metrics(A,fine=False);rec['name']=name
        np.savez_compressed(ROOT/(name+'.npz'),A=np.array(A,dtype=np.int64))
        recs.append(rec)
        print(json.dumps(dict(name=name,n=rec['n'],objective=rec['objective'],certs=rec['certs'])),flush=True)
        (ROOT/'fourway_extras.json').write_text(json.dumps(recs,indent=2)+'\n')
    seedrecs=json.load(open(ROOT/'fourway_seeds.json'))
    rows=seedrecs+recs
    lines=['### Complete seed/adversary joint table','',
        'NUMERICAL coarse evaluations; every value is divided by sqrt(n). Same simultaneous objective and normalization as fourway.py. The complete parameters, individual h values, seeds and saved sets accompany the JSON files.','',
        '| family | n | P28 | W2 | BD | Gibbs | maximum |',
        '|---|---:|---:|---:|---:|---:|---:|']
    for r in rows:
        c=r['certs']
        lines.append(f"| {r['name']} | {r['n']} | {c['spread']:.5f} | {c['graph_W2']:.5f} | {c['bulk_BD']:.5f} | {c['Gibbs_P29']:.5f} | {r['objective']:.5f} |")
    (ROOT/'fourway_all_tables.md').write_text('\n'.join(lines)+'\n')


if __name__=='__main__':main()
