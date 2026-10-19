"""Focused check of the complete deleted-atom expression, VM only."""
from pathlib import Path
from fractions import Fraction as Q
import json,math,hashlib
import numpy as np
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parent

def run():
    rows=[]
    for q in (101,257,509):
        for r in range(2,9):
            k=q//(16*r)
            if k<1:continue
            for family in ('interval','random'):
                rng=np.random.default_rng(1414+q+r)
                P=list(range(1,k+1)) if family=='interval' else sorted(rng.choice(np.arange(1,(q+1)//2),k,replace=False).tolist())
                a=Q(2*k,q);d=1-2*a
                assert a<=Q(1,8*r) and q>r
                def ball(x):return arb(x.numerator)/x.denominator
                A=[Q(0)]+[((1-a)**j-(-a)**j)/d**(j-1) for j in range(1,r+1)]
                mu=[Q(1)]+[(a*(1-a)**j+(1-a)*(-a)**j)/d**j for j in range(1,r+1)]
                assert A[r]-r*mu[r-1]>=Q(1,2)
                vals=[arb(0)]+[sum((2*(2*arb.pi()*int(x)*g/q).cos() for x in P),arb(0))/ball(d)
                               for g in range(1,q)]
                count=0;minmargin=None
                for g in range(1,(q+1)//2):
                    T=vals[g]
                    if T.upper()<0:continue
                    assert T.lower()>0
                    exact=ball(A[r])*T-r*T*ball(mu[r-1])
                    for j in range(2,r):
                        # q>r ensures that no intermediate zero-mode term appears.
                        z=(1-j)*g%q
                        assert z!=0
                        exact+=math.comb(r,j)*(-T/q)**j*ball(A[r-j])*vals[z]
                    margin=exact/T-arb(1)/4
                    assert margin.lower()>0,(q,r,family,P,g,str(margin))
                    v=float(margin.lower())
                    minmargin=v if minmargin is None else min(minmargin,v)
                    count+=1
                rows.append(dict(q=q,r=r,cardinality=2*k,density=str(a),family=family,pairs=P,
                                 positive_frequencies_checked=count,min_ratio_margin_lower_float=minmargin))
    out=dict(arb_bits=256,sets=len(rows),positive_frequencies=sum(x['positive_frequencies_checked'] for x in rows),
             claim='For alpha<=1/(8r), q>r, U(gamma)=T>0: (U-T*1_gamma)^(r)(gamma)>=T/4',rows=rows)
    (ROOT/'fixed_order_test.json').write_text(json.dumps(out,indent=2))
    files=sorted(p for p in ROOT.iterdir() if p.suffix in ('.py','.json','.npz','.pdf'))
    manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files if p.name!='manifest.json'}
    (ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2))
    print('FIXED ORDER CHECK COMPLETE',out['sets'],'sets',out['positive_frequencies'],'positive frequencies',flush=True)

if __name__=='__main__':run()
