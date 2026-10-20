"""Finite matched-profile certificate for deterministic partial parabolas.

All computation on Dirichlet. Actual supports are fixed; randomness is
only a reproducible way to select one reviewable reference certificate.
"""
from collections import defaultdict
from fractions import Fraction as F
import json
import math
from pathlib import Path
import socket
import random
import sys
import numpy as np
from cstar_sidon_fibers import matrix_sample
from cstar_sidon_mixed import group,add_q,cubic


def diffs(B):
    S=set()
    for i,(x,y) in enumerate(B):
        for u,v in B[:i]:
            a,b=x-u,y-v
            if a<0 or (a==0 and b<0):a,b=-a,-b
            assert (a,b) not in S;S.add((a,b))
    return S


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    data=json.loads(Path('.research/experiments/sidon_fibers_2026-10-20/results.json').read_text())
    row=next(r for r in data['cases'] if r['X']==64 and r['rotated'])
    rng=random.Random(20261102);left=defaultdict(group);right=defaultdict(group);lines=defaultdict(group)
    windowed='--window' in sys.argv;nprng=np.random.default_rng(20261103)
    fibers=[];a=0;n=0;high=0;cut2=2
    for f in row['fibers']:
        u=tuple(f['u']);p=f['p'];k=(p-1)//2;P=[(t,t*t%p) for t in range(k)]
        if windowed:
            P=[(t,t*t%p) for t in range(p) if 2*t<p and 2*(t*t%p)<p];k=len(P)
        coeff=[rng.randrange(1,p),rng.randrange(p),rng.randrange(p)]
        active=sum(x*x for x in u)>=cut2
        Q=[(t,(coeff[0]*t*t+coeff[1]*t+coeff[2])%p) for t in range(k)] if active else P
        reference_parameters={};adjustment=0;before=k
        if windowed and active:
            M=matrix_sample(p,nprng);shift=nprng.integers(0,p,size=2)
            full=sorted(tuple(map(int,z)) for z in ((np.array([(t,t*t%p) for t in range(p)])@M.T+shift)%p))
            inside=[z for z in full if 2*z[0]<p and 2*z[1]<p];before=len(inside)
            Q=inside[:k] if before>=k else inside+[z for z in full if z not in inside][:k-before]
            adjustment=abs(before-k)
            reference_parameters=dict(A=M.tolist(),shift=list(map(int,shift)))
        S=diffs(P);T=diffs(Q);assert len(S)==len(T)==k*(k-1)//2
        n+=len(S);high+=len(S)*active;a+=2*len(S-T)
        for w in S:
            g=math.gcd(abs(w[0]),abs(w[1]));v=(w[0]//g,w[1]//g);z=(g*u[0],g*u[1])
            left[u]['target'].append(w);right[v]['target'].append(z);lines[u,v]['target'].append((g,))
        for D,c in [(S-T,1),(T-S,-1)]:
            for w in D:
                g=math.gcd(abs(w[0]),abs(w[1]));v=(w[0]//g,w[1]//g);z=(g*u[0],g*u[1])
                for sign in [1,-1]:
                    add_q(left,u,tuple(sign*x for x in w),c)
                    add_q(right,v,tuple(sign*x for x in z),c)
                    add_q(lines,(u,v),(sign*g,),c)
        fibers.append(dict(u=list(u),p=p,k=k,actual=P,reference=Q,reference_coefficients=coeff,
                           frozen=not active,reference_parameters=reference_parameters,
                           reference_window_count_before=before,adjustment=adjustment))
    HL,_=cubic(left);HR,_=cubic(right);HI,_=cubic(lines);H=HL+HR-HI;norm2=2*a
    root=2*a*a/(H+math.sqrt(H*H+4*norm2*a*a)) if H>=0 else (-H+math.sqrt(H*H+4*norm2*a*a))/(2*norm2)
    bound=F(max(0,math.floor(root*10**8)-2),10**8)
    assert norm2*bound*bound+H*bound-a*a<0
    result=dict(X=64,U=row['U'],cutoff_squared=cut2,n=n,high_n=high,a=a,Q=norm2,
                H_left=HL,H_right=HR,H_line=HI,H=H,global_M_lower=str(bound/2),
                ratio_lower=float(bound)/(2*math.sqrt(n)),fibers=fibers,windowed=windowed,
                encoding='Any integer linear encoding with kernel gap>3X; e.g. base6X+1',
                qualification='Exact global negative-minimum lower certificate for actual Boolean partial fibers.')
    filename='windowed.json' if windowed else 'partial.json'
    Path('.research/experiments/sidon_cutoff_2026-10-20',filename).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['X','U','n','high_n','a','Q','H_left','H_right','H_line','H','ratio_lower']}),flush=True)


if __name__=='__main__':main()
