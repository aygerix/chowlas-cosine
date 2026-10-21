"""Same3x3 counts and disjoint differences do not bound the mixed cubic.

Quantile blocks on one parabola yield an asymptotic p^4 obstruction.
Finite cubics are exact integer products; all computation on Dirichlet.
"""
from collections import defaultdict
from fractions import Fraction as F
import json
import math
from pathlib import Path
import socket
import flint


def signed(P):
    S={(x-u,y-v) for x,y in P for u,v in P if (x,y)!=(u,v)}
    assert len(S)==len(P)*(len(P)-1)
    return S


def cubic(A,B,p):
    r=p-1;base=4*r+1;coeff=[0]*((2*r+1)*base)
    for x,y in A|B:coeff[x+r+(y+r)*base]=int((x,y) in A)-int((x,y) in B)
    square=flint.fmpz_poly(coeff)**2
    return sum(int(square[x+2*r+(y+2*r)*base]) for x,y in A)


def variance(shifts):
    centers=[F(i,3)+F(shifts[i],12)+F(1,24) for i in range(3)]
    mean=sum(centers)/3
    return sum((x-mean)**2 for x in centers)/3+F(1,1728)


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    flint.ctx.prec=192;pa=[3,1,0];pb=[0,2,3]
    gap=variance(pb)-variance(pa);assert gap==F(1,9)
    out=dict(qualification='Counterexample to an automatic cubic-cost bound from fixed coarse counts, '
             'not a Chowla counterexample and not a failure of existence of better references.',
             actual_blocks=pa,reference_blocks=pb,normalized_variance_gap=str(gap),cases=[])
    root=Path('.research/experiments/reference_entropy_2026-10-20');root.mkdir(parents=True,exist_ok=True)
    for p in [61,127,251,509,1009]:
        cells=defaultdict(list)
        for t in range(p):cells[3*t//p,3*(t*t%p)//p].append((t,t*t%p))
        P=[];Q=[];counts={}
        for (i,j),points in sorted(cells.items()):
            points.sort();m=len(points)//4;counts[f'{i},{j}']=m
            P.extend(points[pa[i]*m:(pa[i]+1)*m]);Q.extend(points[pb[i]*m:(pb[i]+1)*m])
        assert len(P)==len(Q) and not(set(P)&set(Q))
        A=signed(P);B=signed(Q);assert not(A&B)
        k=len(P);n=k*(k-1)//2;a=2*n;norm=4*n;H=cubic(A,B,p)
        assert norm*k*k+H*k-a*a>=0
        approx=2*a*a/(H+math.sqrt(H*H+4*norm*a*a)) if H>=0 else (-H+math.sqrt(H*H+4*norm*a*a))/(2*norm)
        lower=F(max(0,math.floor(approx*10**8)-2),2*10**8)
        assert norm*(2*lower)**2+H*(2*lower)-a*a<0
        row=dict(p=p,k=k,n=n,actual=P,reference=Q,cell_counts=counts,a=a,Q=norm,H=H,
                 H_over_p3_float=H/p**3,H_over_p4_float=H/p**4,
                 global_M_lower=str(lower),ratio_lower=float(lower)/math.sqrt(n),
                 integer_difference_overlap=0,point_overlap=0)
        out['cases'].append(row);(root/'counterfamily.json').write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({key:row[key] for key in ['p','k','n','H','H_over_p3_float','H_over_p4_float','ratio_lower']}),flush=True)


if __name__=='__main__':main()
