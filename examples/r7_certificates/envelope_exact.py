"""Exact rational certificate for the scalar CF-envelope reduction; VM only."""
from fractions import Fraction as F
from pathlib import Path
import json

OUT=Path('.research/agents/tdense7_scratch')
def cos_upper(n):
    # 333/106 < pi, and the even-degree-8 cosine Taylor sum is an upper bound.
    x=F(333,106*(n+2));z=x*x
    return 1-z/2+z*z/24-z**3/720+z**4/40320
def certify(C,r,N=100):
    C=F(C);r=F(r);k=2/r
    pieces=[(F(1,N+1),F(1))]
    pieces += [(F(1,n)-F(1,n+1),cos_upper(n)) for n in range(N,0,-1)]
    mass=F(0);energy=F(0);best=None;bestrec=None;records=[]
    for width,u in pieces:
        lo=mass;hi=min(mass+width*u,1/k)
        if lo>1/k:break
        # F(mu)=energy+u*(mu-mass).
        vertex=(C+k*u)/(2*C*k)
        mu=max(lo,min(hi,vertex))
        ff=energy+u*(mu-mass)
        q=1-C*mu+C*k*mu*mu-k*ff
        rec=dict(lo=str(lo),hi=str(hi),u=str(u),mu=str(mu),margin=str(q))
        records.append(rec)
        if best is None or q<best:best=q;bestrec=rec
        energy+=width*u*u;mass+=width*u
    return dict(C=str(C),rho=str(r),N=N,verified=best>0,margin=str(best),margin_float=float(best),
                worst_piece=bestrec,checked_pieces=len(records),pieces=records)
if __name__=='__main__':
    recs=[certify('4.16','.811'),certify('4.33','.77'),certify('4.164','.811'),certify('4.331','.77')]
    OUT.joinpath('envelope_exact.json').write_text(json.dumps(recs,indent=2))
    # Machin identity pi=16 atan(1/5)-4 atan(1/239), alternating lower/upper sums.
    lower_pi=16*sum(F((-1)**j,(2*j+1)*5**(2*j+1)) for j in range(4))-F(4,239)
    assert lower_pi>F(333,106)
    assert F(16,27)<F(77,100)**2
    OUT.joinpath('constants_exact.json').write_text(json.dumps(dict(
        machin_lower=str(lower_pi),pi_lower_333_over_106=True,beckner_less_77_over_100=True),indent=2))
    print(json.dumps([dict(C=r['C'],rho=r['rho'],verified=r['verified'],margin_float=r['margin_float'],
                           checked_pieces=r['checked_pieces']) for r in recs],indent=2))
