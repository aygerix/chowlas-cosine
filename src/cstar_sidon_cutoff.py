"""Freeze short fibers in the reference, leaving the actual set intact.

Exact integer mixed moments. The finite cutoffs below are mechanism
probes, not instances of the far larger asymptotic polylog threshold.
All computation on Dirichlet.
"""
from collections import defaultdict
from fractions import Fraction as F
import json
import math
from pathlib import Path
import socket
import numpy as np
from cstar_sidon_fibers import differences,matrix_sample
from cstar_sidon_mixed import group,add_q,cubic


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    source=Path('.research/experiments/sidon_fibers_2026-10-20')
    data=json.loads((source/'results.json').read_text())
    old=json.loads((source/'mixed.json').read_text())
    root=Path('.research/experiments/sidon_cutoff_2026-10-20');root.mkdir(parents=True,exist_ok=True)
    out=[]
    for X,cut2 in [(64,2),(256,2),(256,4),(1024,4)]:
        row=next(r for r in data['cases'] if r['X']==X and r['rotated'])
        previous=next((r for r in old if r['X']==X and r['rotated']),None)
        cached={tuple(f['u']):f for f in previous['references']} if previous else {}
        rng=np.random.default_rng(20261101+X)
        left=defaultdict(group);right=defaultdict(group);lines=defaultdict(group)
        a=0;high=0;frozen=0;references=[]
        for fiber in row['fibers']:
            u=tuple(fiber['u']);p=fiber['p'];WA=set(differences(fiber['points']))
            active=u[0]*u[0]+u[1]*u[1]>=cut2
            if active:
                high+=len(WA)
                if u in cached:ref=cached[u]
                else:
                    A=matrix_sample(p,rng);shift=rng.integers(0,p,size=2)
                    B=[tuple(map(int,z)) for z in ((np.array([(t,t*t%p) for t in range(p)])@A.T+shift)%p)]
                    ref=dict(u=list(u),p=p,A=A.tolist(),shift=list(map(int,shift)),points=B)
                WB=set(differences(ref['points']));assert len(WA)==len(WB)
                references.append(ref);a+=2*len(WA-WB)
            else:WB=WA;frozen+=len(WA)
            # Targets include ALL actual fibers, including those where
            # q vanishes. Their right-ruling cross terms must survive.
            for w in WA:
                g=math.gcd(abs(w[0]),abs(w[1]));v=(w[0]//g,w[1]//g);z=(g*u[0],g*u[1])
                left[u]['target'].append(w);right[v]['target'].append(z);lines[u,v]['target'].append((g,))
            if not active:continue
            for S,c in [(WA-WB,1),(WB-WA,-1)]:
                for w in S:
                    g=math.gcd(abs(w[0]),abs(w[1]));v=(w[0]//g,w[1]//g);z=(g*u[0],g*u[1])
                    for t in [1,-1]:
                        add_q(left,u,tuple(t*x for x in w),c)
                        add_q(right,v,tuple(t*x for x in z),c)
                        add_q(lines,(u,v),(t*g,),c)
        assert high+frozen==row['n'];Q=2*a
        HL,ml=cubic(left);HR,mr=cubic(right);HI,mi=cubic(lines);H=HL+HR-HI
        approx=2*a*a/(H+math.sqrt(H*H+4*Q*a*a)) if H>=0 else (-H+math.sqrt(H*H+4*Q*a*a))/(2*Q)
        k=F(max(0,math.floor(approx*10**8)-2),10**8)
        assert Q*k*k+H*k-a*a<0
        result=dict(X=X,U=row['U'],cutoff_norm_squared=cut2,n=row['n'],high_n=high,
                    frozen_n=frozen,actual_sha256=row['sha256'],a=a,Q=Q,H_left=HL,
                    H_right=HR,H_line=HI,H=H,global_K_lower=str(k),global_M_lower=str(k/2),
                    ratio_lower=float(k)/(2*math.sqrt(row['n'])),
                    exact_polynomial=str(Q*k*k+H*k-a*a),references=references,
                    methods=dict(left=ml,right=mr,line=mi),
                    qualification='Actual support unchanged; only the reference freezes short fibers. '
                                  'Exact global lower certificate, not a global upper bound.')
        out.append(result);(root/'frozen.json').write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({k:result[k] for k in ['X','cutoff_norm_squared','n','high_n','frozen_n',
                         'a','Q','H_left','H_right','H_line','H','ratio_lower']}),flush=True)


if __name__=='__main__':main()
