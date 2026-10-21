"""Exact scalar check of fixed-coupling probes; no optimizer import."""
from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path
import socket
from cstar_ordered_prefix_verify import auto,exact


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    root=Path('.research/experiments/ordered_prefix_2026-10-20');data=json.loads((root/'coupling.json').read_text());out=[]
    for row in data['cases']:
        A=row['actual'];n=row['n'];den=row['coefficient_denominator'];assert A==sorted(set(A)) and len(A)==n
        rows=[{0:1},{s:1 for a in A for s in [-a,a]}]
        for j in range(1,n+1):
            r=Counter(auto([0]+A[:j]))
            for w,c in auto([0]+A[:j-1]).items():r[w]-=c
            rows.append(r)
        if row['suffix']:
            for j in range(n):
                r=Counter(auto([0]+A[j:]))
                for w,c in auto([0]+A[j+1:]).items():r[w]-=c
                rows.append(r)
        assert len(rows)==len(row['integer_weights']);poly=Counter()
        for c,r in zip(row['integer_weights'],rows):
            for w,v in r.items():poly[w]+=c*v
        poly={w:c for w,c in poly.items() if c};assert poly==dict(row['test_polynomial']) and poly.get(0,0)==0
        Q,H=exact(A,poly);a=2*sum(poly.get(w,0) for w in A)
        assert (Q,H)==(row['norm_numerator'],row['energy_numerator']) and a==n*den
        assert Q<=25*n*den*den
        gamma=row['certified_integer_gamma'];assert H<=0 or H*H<=gamma*gamma*n**3*den**4
        K=2*F(row['global_M_lower']);assert Q*K*K+H*K-n*n*den*den<0
        out.append(dict(label=row['label'],suffix=row['suffix'],a_equals_n=True,Q_at_most_25n=True,
                        H_nonpositive=H<=0,certified_integer_gamma=gamma,global_M_lower=row['global_M_lower']))
    result=dict(status='PASS',cases=out,host=socket.gethostname(),
                qualification='Achieved exact witnesses only; no numerical optimum or universal estimate certified.')
    (root/'coupling_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',witnesses=len(out),nonpositive_H=sum(r['H_nonpositive'] for r in out))))


if __name__=='__main__':main()
