from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
from w2_operator import *
for p,a in [(3,3),(3,4),(5,3)]:
 D,n=jl_set(p,a,1);Z=(np.array(sorted(D))+n//2)%n-n//2;test(Z,f'JL_p{p}_depth{a}_centered')
 open(str(HERE / 'depth_w2.json'),'w').write(json.dumps(out,indent=2))
for p,d in [(3,6),(5,6)]:
 Z=np.array([z for z in itertools.product(range(-(p//2),p//2+1),repeat=d) if any(z) and sum(z[2*j]*z[2*j+1] for j in range(d//2))%p==0]);test(Z,f'quadric_p{p}_dim{d}')
 open(str(HERE / 'depth_w2.json'),'w').write(json.dumps(out,indent=2))
