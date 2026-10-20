from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import numpy as np,time,json
rng=np.random.default_rng(20261021);rows=[]
for target in [1000,4000,16000]:
 for ex in [.5,1/3,.25]:
  alpha=target**(-ex);X=round(target/alpha);a=np.arange(1,X+1);A=a[rng.random(X)<2*alpha*(1-a/X)]
  if ex!=1/3:continue
  t=time.time();s=np.r_[X-A,X+A];bits=np.zeros(2*X+1,np.uint8);bits[s]=1;z=int.from_bytes(np.packbits(bits,bitorder='little').tobytes(),'little');zz=0
  for j in s:zz |= z<<int(j)
  zz|=z<<X;zz|=1<<(2*X)
  missing=(~(zz>>(2*X)))&((1<<(2*X+1))-1);radius=(missing&-missing).bit_length()-2
  row=dict(target=target,n=len(A),radius_exact=radius,size_exact=zz.bit_count(),seconds=time.time()-t);print(row,flush=True);rows.append(row)
open(str(HERE / 'double_bitset_checks.json'),'w').write(json.dumps(rows,indent=2))
