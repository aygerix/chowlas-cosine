from pathlib import Path
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np
from scipy.linalg import eigh
from scipy.signal import fftconvolve
import json,time
def test(A,tag):
 S=np.r_[-A[::-1],A]; I=np.r_[-A[::-1],0,A]; N=len(S); m=int(max(A)); lookup=np.zeros(2*m+1);lookup[m+S]=1
 diff=I[:,None]-I[None,:]; B=np.zeros(diff.shape); mask=abs(diff)<=m;B[mask]=lookup[m+diff[mask]]
 val,v=eigh(B,subset_by_index=[0,0]);k=-val[0];q=v[:,0]; qcoef=np.zeros(2*m+1);qcoef[m+I]=q
 gamma=fftconvolve(qcoef,qcoef[::-1]); h=fftconvolve(lookup,gamma)
 G=gamma[2*m+diff]; H=h[3*m+diff]
 gv=eigh(G,eigvals_only=True,subset_by_index=[0,0])[0]
 lo=eigh(H,G,eigvals_only=True,subset_by_index=[0,0])[0]
 r=fftconvolve(lookup,qcoef);r[m:3*m+1]+=k*qcoef
 R=float(r@r); dr=fftconvolve(lookup,r);g=float(r@dr[m:5*m+1]/R);Ktwo=-float(np.linalg.eigvalsh([[-k,np.sqrt(R)],[np.sqrt(R),g]])[0])
 rec=dict(R_over_N=R/N,exteriorCost=g,Ktwo=Ktwo,ratioTwo=Ktwo/np.sqrt(N),tag=tag,n=len(A),K1=k,Ktranslated=-lo,ratio1=k/np.sqrt(N),ratioTranslated=-lo/np.sqrt(N),gramMin=gv,parity=float(q@q[::-1]))
 return rec

controls=[('A50',np.array(list(range(1,19))+list(range(20,38))+[39,40,41,42,47,48,50,52,57,61,62,64,65,68]))]
for d in json.load(open(str(Path(__file__).resolve().parents[1] / 'inputs' / 'singer_results.json'))):
 if d['N']>1100:continue
 T=d['T'];controls.append((d['tag'],np.array(sorted({x-y for x in T for y in T if x>y}))))
for n in [16,64,256]:controls.append(('interval'+str(n),np.arange(1,n+1)))
out=[]
for tag,A in controls:
 rec=test(A,tag);out.append(rec);print(json.dumps(rec),flush=True)
open(str(Path(__file__).resolve().parent / 'translated_kernel_controls.json'),'w').write(json.dumps(out,indent=2))
