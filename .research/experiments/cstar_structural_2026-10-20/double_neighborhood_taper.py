from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import numpy as np, json
from scipy.fft import rfft,irfft,next_fast_len
rng=np.random.default_rng(20261021);out=[]
old=[json.loads(x) for x in open(str(REPO / 'examples/e99/e99c.jsonl'))]
for target in [1000,4000,16000]:
 for ex in [.5,1/3,.25]:
  alpha=target**(-ex);X=round(target/alpha);a=np.arange(1,X+1);A=a[rng.random(X)<2*alpha*(1-a/X)];n=len(A)
  if ex!=1/3:continue
  s=np.zeros(2*X+1);s[X+A]=1;s[X-A]=1;L=next_fast_len(4*X+1);F=rfft(s,L);conv=np.rint(irfft(F*F,L)[:4*X+1]).astype(np.int64);assert conv.min()>=0
  W=conv>0;W[2*X+A]=1;W[2*X-A]=1;W[2*X]=1
  zeros=np.flatnonzero(~W[2*X:]);rad=int(zeros[0]-1) if len(zeros) else 2*X;length=2*rad+1
  N=next_fast_len(32*X);coef=np.zeros(N);weights=1-A/length;coef[A]=weights;coef[-A]=weights;vals=irfft(rfft(coef),N) if False else np.fft.fft(coef).real
  bound=-float(vals.min());prev=next(t for t in old if t['n_target']==target and abs(t['alpha_exp']-ex)<.001)
  rec=dict(n=n,X=X,alpha=alpha,W2_size=int(W.sum()),contained_radius=rad,rayleigh_K_bound=bound,rayleigh_over_sqrt_n=bound/np.sqrt(n),first_K=-prev['W2_0pmA']['lam_min'],true_K_est=2*prev['M'],matches_old_n=n==prev['n']);print(rec,flush=True);out.append(rec)
open(str(HERE / 'double_neighborhood_taper.json'),'w').write(json.dumps(out,indent=2))
