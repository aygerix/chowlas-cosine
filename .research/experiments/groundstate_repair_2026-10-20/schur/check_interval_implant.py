from pathlib import Path
"""Numerical smoke check of exact structural theorem, not asymptotic evidence."""
import json
import numpy as np
from scipy.linalg import eigh
out=[]
T=np.array([-2,-1,1,2]); IT=np.r_[0,T]
BT=np.isin(IT[:,None]-IT,T).astype(float)
kT=-eigh(BT,eigvals_only=True)[0]
for L in [20,50,100,200]:
 U=np.arange(-L,L+1)
 BU=((abs(U[:,None]-U)<=L)&(U[:,None]!=U)).astype(float)
 w,v=eigh(BU); kU=-w[0]; q=v[:,0]
 E=np.zeros((len(U),L+1));E[L,0]=1
 for j in range(1,L+1):E[L-j,j]=E[L+j,j]=1/np.sqrt(2)
 gap=eigh(E.T@BU@E,eigvals_only=True)[0]+kU
 B=np.zeros((len(T)+len(U),)*2);B[:len(T),:len(T)]=BT[1:,1:]
 B[len(T):,len(T):]=BU
 B[:len(T),len(T)+L]=B[len(T)+L,:len(T)]=1
 ww=eigh(B,eigvals_only=True)
 qq=np.r_[np.zeros(len(T)),q]
 out.append(dict(L=L,kT=float(kT),kU=float(kU),even_gap=float(gap),full_k=float(-ww[0]),kernel_residual=float(np.linalg.norm(B@qq+kU*qq)),global_bottom_retained=bool(abs(ww[0]+kU)<1e-9),first_gap=float(ww[1]-ww[0])))
print(json.dumps(out,indent=2))
open(str(Path(__file__).resolve().parent / 'check_interval_implant.json'),'w').write(json.dumps(out,indent=2)+'\n')
