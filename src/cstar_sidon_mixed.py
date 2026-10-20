"""Exact mixed cubic certificates, using rank-one ruling decomposition.

Integer FLINT polynomial products, not floating FFT convolutions.
Run on Dirichlet. Scalar encoding has no aliases in these degree-three
moments because the kernel gap exceeds 3X.
"""
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import socket
import flint
import numpy as np
from cstar_sidon_fibers import differences,matrix_sample


def group():return {'q':{},'target':[]}


def add_q(G,key,z,c):
    d=G[key]['q'];d[z]=d.get(z,0)+c
    if d[z]==0:del d[z]


def cubic(G):
    total=0;methods=defaultdict(int)
    for item in G.values():
        q=item['q'];targets=item['target']
        if not q or not targets:continue
        dim=len(next(iter(q)))
        if len(q)*len(targets)<2000000:
            value=sum(c*q.get(tuple(s[j]-t[j] for j in range(dim)),0)
                      for s in targets for t,c in q.items())
            methods['sparse']+=1
        else:
            r=max(abs(z) for t in q for z in t);base=4*r+1
            if dim==1:
                coeff=[q.get((i-r,),0) for i in range(2*r+1)]
                square=flint.fmpz_poly(coeff)**2
                value=sum(int(square[s[0]+2*r]) for s in targets if abs(s[0])<=2*r)
            else:
                coeff=[0]*((2*r+1)*base)
                for (x,y),c in q.items():coeff[x+r+(y+r)*base]=c
                square=flint.fmpz_poly(coeff)**2
                value=sum(int(square[x+2*r+(y+2*r)*base]) for x,y in targets
                          if abs(x)<=2*r and abs(y)<=2*r)
            methods['integer_polynomial']+=1
        total+=2*value
    return total,dict(methods)


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    root=Path('.research/experiments/sidon_fibers_2026-10-20')
    data=json.loads((root/'results.json').read_text());out=[]
    for row in data['cases']:
        X=row['X']
        if X>256:continue
        rng=np.random.default_rng(20261031+X+int(row['rotated']))
        left=defaultdict(group);right=defaultdict(group);lines=defaultdict(group)
        Aset=set();Bset=set();references=[]
        for fiber in row['fibers']:
            u=tuple(fiber['u']);p=fiber['p'];A=matrix_sample(p,rng);shift=rng.integers(0,p,size=2)
            B=[tuple(map(int,z)) for z in ((np.array([(t,t*t%p) for t in range(p)])@A.T+shift)%p)]
            refs=dict(u=list(u),p=p,A=A.tolist(),shift=list(map(int,shift)),points=B);references.append(refs)
            for label,points,sign in [('A',fiber['points'],1),('B',B,-1)]:
                for w in differences(points):
                    M=(u[0]*w[0],u[0]*w[1],u[1]*w[0],u[1]*w[1])
                    (Aset if label=='A' else Bset).add(M)
                    g=math.gcd(abs(w[0]),abs(w[1]));v=(w[0]//g,w[1]//g);z=(g*u[0],g*u[1])
                    for t in [1,-1]:
                        add_q(left,u,tuple(t*x for x in w),sign)
                        add_q(right,v,tuple(t*x for x in z),sign)
                        add_q(lines,(u,v),(t*g,),sign)
                    if label=='A':
                        left[u]['target'].append(w);right[v]['target'].append(z);lines[u,v]['target'].append((g,))
        assert len(Aset)==len(Bset)==row['n']
        a=2*len(Aset-Bset);Q=2*len(Aset^Bset);assert Q==2*a
        HL,ml=cubic(left);HR,mr=cubic(right);HI,mi=cubic(lines);H=HL+HR-HI
        approx=2*a*a/(H+math.sqrt(H*H+4*Q*a*a)) if H>=0 else (-H+math.sqrt(H*H+4*Q*a*a))/(2*Q)
        lower=F(max(0,math.floor(approx*10**6)-2),10**6)
        assert Q*lower*lower+H*lower-a*a<0
        result=dict(X=X,rotated=row['rotated'],n=row['n'],seed=20261031+X+int(row['rotated']),
                    a=a,Q=Q,H_left=HL,H_right=HR,H_line=HI,H=H,
                    H_over_n_three_halves=H/(row['n']**1.5),
                    global_K_lower=str(lower),global_M_lower=str(lower/2),
                    ratio_lower=float(lower)/(2*math.sqrt(row['n'])),
                    exact_inequality_Qk2_Hk_minus_a2=str(Q*lower*lower+H*lower-a*a),
                    methods=dict(left=ml,right=mr,line=mi),references=references,
                    qualification='All-phase lower certificate for M via positivity of (D+K)(s+tq)^2; '
                                  'integer cubic computation; not an all-phase upper bound.')
        out.append(result);(root/'mixed.json').write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({key:result[key] for key in ['X','rotated','n','a','Q','H_left','H_right','H_line',
                    'H','H_over_n_three_halves','ratio_lower']}),flush=True)


if __name__=='__main__':main()
