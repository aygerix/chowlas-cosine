from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import numpy as np
for n in [16,32,64,128,256]:
 a=np.arange(1,n+1); C=(abs(a[:,None]-a)>0).astype(float)-(a[:,None]+a<=n);w=1./a;v=C@w; vv=v@v; H=w@w; r=v@C@v/vv; bound=(-r+np.sqrt(r*r+4*vv/H))/2
 ev=np.linalg.eigvalsh(C)
 print('interval',n,'k',-ev[0],'r',r,'schur',bound,'energy_ratio',np.sum(C*C)/(n*ev[0]**2),'negmass',np.sum(ev[ev<0]**2)/np.sum(ev**2))
for d in range(2,10):
 a=np.arange(1,2**d); comp=((a[:,None]&a)==a[:,None])|((a[:,None]&a)==a)
 C=comp.astype(float)-np.eye(len(a))-(a[:,None]&a==0)
 ev=np.linalg.eigvalsh(C);print('cube',d,len(a),-ev[0],np.sum(C*C)/(len(a)*ev[0]**2))
