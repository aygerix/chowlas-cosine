from pathlib import Path
ARCHIVE_ROOT = Path(__file__).resolve().parent.parent
import json,numpy as np
from scipy.fft import rfft,irfft,next_fast_len
from lifts import support
root=str(ARCHIVE_ROOT / 'correlated/') + "/";tests=[]
for r in json.load(open(root+'singer_results.json')):
 T=r['T'];S=np.array([x-y for x in T for y in T if x!=y]);tests.append((r['tag'],S))
for r in json.load(open(root+'optimized_results.json')):
 q=r['N']+1;h=np.array(r['h']);a=np.arange(1,len(h)+1)+q*h;tests.append((r['tag'],np.r_[a,-a]))
for r in json.load(open(root+'collapsed_results.json')):
 T=r['T'];S=np.unique(np.array([x-y for x in T for y in T if x!=y]));tests.append((r['tag'],S))
checks=[]
for tag,S in tests:
 S=list(map(int,S));R=max(map(abs,S));bits=sum(1<<(s+R) for s in S);wbits=(1<<(2*R))|(bits<<R)
 for s in S:wbits|=bits<<(s+R)
 W=np.array([i-2*R for i in range(4*R+1) if (wbits>>i)&1]);grid=next_fast_len(6*R+1);ker=np.zeros(grid);ker[np.array(S)%grid]=1;conv=irfft(rfft(ker)**2,n=grid);Fw=np.union1d(np.flatnonzero((conv>.5)|(ker>.5)),[0]);assert np.array_equal(np.sort(W%grid),Fw)
 checks.append(dict(tag=tag,exact_W2_size=len(W),max_fft_integer_error=float(np.max(abs(conv-np.rint(conv))))))
open(root+'support_checks.json','w').write(json.dumps(checks,indent=2));print('All',len(checks),'exact bitset support checks passed')
