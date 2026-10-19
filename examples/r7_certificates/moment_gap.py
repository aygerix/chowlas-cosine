"""VM-only exact algebra for a new universal doubly-positive L2/L1 gap."""
from fractions import Fraction as F
from pathlib import Path
import json,math
OUT=Path('.research/agents/tdense7_scratch')
def cert(C,r,v):
    C=F(C);r=F(r);v=F(v);k=2/r
    # v exceeds (1+sqrt(17))/(4sqrt(2)).
    assert v*v>F(1,2) and 8*(v*v-F(1,2))**2>v*v
    margin=k-(k*v+C)**2/(4*C)
    return dict(C=str(C),rho=str(r),v_upper=str(v),verified=margin>0,
                margin=str(margin),margin_float=float(margin),beckner_constant_less_r=(r*r>F(16,27)))
if __name__=='__main__':
    rows=[cert('4.439','.769801','.905646'),cert('4.4393','.769801','.905646'),
          cert('4.213','.811','.905646'),cert('4.43','.77','.906')]
    v=(1+math.sqrt(17))/(4*math.sqrt(2));r=4/(3*math.sqrt(3))
    result=dict(exact=rows,numerical=dict(v=v,C_limit=2/r*(1+math.sqrt(1-v))**2,
                                        C_limit_elementary=2/.811*(1+math.sqrt(1-v))**2))
    OUT.joinpath('moment_gap.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
