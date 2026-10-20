"""VM-only pointwise PD-envelope bound and independent scalar maximization scan."""
import json, math
from pathlib import Path
import numpy as np

OUT=Path('.research/agents/tdense7_scratch')
N=200000
# Exact step widths of u(t)=cos(pi/(floor(1/t)+2)). Tail t<1/(N+1)
# is replaced by 1, an upper bound, with explicitly vanishing error.
left=np.r_[0,1/np.arange(N+1,1,-1,dtype=float)]
right=np.r_[1/(N+1),1/np.arange(N,0,-1,dtype=float)]
u=np.r_[1,np.cos(np.pi/np.arange(N+2,2,-1,dtype=float))]
width=right-left
cap=np.cumsum(width*u);en2=np.cumsum(width*u*u)

def F(mu):
    mu=np.asarray(mu)
    inds=np.searchsorted(cap,mu)
    prev=np.where(inds==0,0,cap[np.maximum(inds-1,0)])
    prev2=np.where(inds==0,0,en2[np.maximum(inds-1,0)])
    return prev2+(mu-prev)*u[inds]

def scan(r):
    k=2/r
    mus=np.linspace(1e-8,r/2,1000000)
    ff=F(mus);aa=(1-k*mus)/(1-k*ff)
    dd=mus*aa;j=int(np.argmax(dd))
    return dict(rho=r,density_upper_scan=float(dd[j]),C_lower_scan=float(1/dd[j]),
                mu=float(mus[j]),a=float(aa[j]),F=float(ff[j]),
                scan_step=float(mus[1]-mus[0]),tail_cutoff=float(1/(N+1)))
recs=[scan(r) for r in [.811,4/(3*math.sqrt(3)),.687]]
OUT.joinpath('envelope.json').write_text(json.dumps(recs,indent=2));print(json.dumps(recs,indent=2))
