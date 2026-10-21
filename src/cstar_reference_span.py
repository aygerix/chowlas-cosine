"""Signed spans can be stronger than choosing or averaging one reference.

Complete enumeration of the stated p11 profiles; floating eigensolvers
only propose integer vectors, whose exact quadratic forms decide success.
All research computation runs on Dirichlet.
"""
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import socket
import numpy as np


def spectrum(P):
    return {(x-u,y-v) for x,y in P for u,v in P if (x,y)!=(u,v)}


def references(P,p,g):
    counts=Counter((g*x//p,g*y//p) for x,y in P)
    cells=[]
    for cell,k in sorted(counts.items()):
        V=[(x,y) for x in range(p) for y in range(p) if (g*x//p,g*y//p)==cell]
        cells.append(list(itertools.combinations(V,k)))
    A=spectrum(P);n=len(A)//2;out=[];cyclic=0
    for choices in itertools.product(*cells):
        Q=[w for group in choices for w in group]
        if len({((x-u)%p,(y-v)%p) for x,y in Q for u,v in Q if (x,y)!=(u,v)})!=2*n:continue
        cyclic+=1;B=spectrum(Q)
        if len(A&B)//2<=3*n//4:out.append(Q)
    return out,cyclic


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    root=Path('.research/experiments/reference_entropy_2026-10-20')
    baseline=json.loads((root/'results.json').read_text());verified=json.loads((root/'verification.json').read_text())
    expected={(r['label'],r['grid']):r for r in verified['exhaustive_profiles']};out=[];actuals=[]
    for row in baseline['cases']:
        if row['p']!=11 or row['grid']!=3:continue
        p=11;P=list(map(tuple,row['actual_points']));A=spectrum(P);n=len(A)//2
        base=6*p+1;freq=sorted({abs(x+base*y) for x,y in A});assert len(freq)==n and 0 not in freq
        body=' '.join(map(str,freq))+'\n';name=f"p11_{row['label']}_A.txt";(root/name).write_text(body)
        actuals.append(dict(label=row['label'],n=n,max_A=max(freq),base=base,frequency_file=name,
                            sha256=hashlib.sha256(body.encode()).hexdigest(),global_M_upper='5/2',
                            upper_certificate='Distinct differences: f=(|F|^2-5)/2.'))
        for g in [7,9,10]:
            refs,cyclic=references(P,p,g);assert len(refs)==expected[row['label'],g]['macro_turnover_point_sets']
            assert cyclic==expected[row['label'],g]['cyclic_sidon_point_sets']
            directions=[]
            for R in refs:
                B=spectrum(R);directions.append({w:int(w in A)-int(w in B) for w in A|B if (w in A)!=(w in B)})
            support=sorted({(0,0)}|{w for q in directions for w in q});index={w:i for i,w in enumerate(support)}
            Z=np.zeros((len(refs)+1,len(support)),dtype=np.int64);Z[0,index[0,0]]=1
            for j,q in enumerate(directions,1):
                for w,c in q.items():Z[j,index[w]]=c
            # Twice <(D_A+5/2) r^2>, exact symmetric Fourier kernel.
            kernel=np.array([[5*int(u==(-v[0],-v[1]))+2*int((u[0]+v[0],u[1]+v[1]) in A)
                              for v in support] for u in support],dtype=np.int64)
            T=Z@kernel@Z.T;assert np.array_equal(T,T.T)
            vals,vecs=np.linalg.eigh(T.astype(float));v=np.rint(vecs[:,0]*10**6).astype(np.int64)
            weights=list(map(int,v));value=sum(weights[i]*int(T[i,j])*weights[j]
                                             for i in range(len(weights)) for j in range(len(weights)))
            result=dict(label=row['label'],p=p,grid=g,actual_points=P,n=n,reference_count=len(refs),
                        reference_points=refs,K_target='5/2',global_M_target='5/4',
                        individual_optimum_margin_twice=expected[row['label'],g]['optimal_margin_twice'],
                        numerical_minimum_eigenvalue=float(vals[0]),target_witness_found=value<0,
                        qualification='A negative exact form proves the target. A nonnegative proposed vector '
                                      'does not certify absence of another vector.')
            if value<0:
                polynomial={}
                for j,w in enumerate(support):
                    c=sum(weights[i]*int(Z[i,j]) for i in range(len(weights)))
                    if c:polynomial[w]=c
                assert all(polynomial.get((-x,-y))==c for (x,y),c in polynomial.items())
                result.update(integer_weights=weights,twice_weighted_square=value,
                              test_polynomial=[[x,y,c] for (x,y),c in sorted(polynomial.items())])
            out.append(result)
            (root/'span.json').write_text(json.dumps(dict(host=socket.gethostname(),actuals=actuals,cases=out),indent=2)+'\n')
            print(json.dumps({k:result[k] for k in ['label','grid','reference_count',
                  'individual_optimum_margin_twice','target_witness_found','numerical_minimum_eigenvalue']}),flush=True)


if __name__=='__main__':main()
