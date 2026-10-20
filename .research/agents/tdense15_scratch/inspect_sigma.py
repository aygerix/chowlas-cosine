from pathlib import Path
import json
from fractions import Fraction as Q
rec=json.loads(Path('examples/e95/discovery_sigma0.6667_K64_d10_s0.1_t0.json').read_text())
for j,row in enumerate(rec['beta']):
    rr=[Q(round(x*10**10),10**10) for x in row]
    if rr[0]!=0 or any(x>y for x,y in zip(rr,rr[1:])):
        print('BAD_MONOTONICITY',j,list(map(str,rr)))
