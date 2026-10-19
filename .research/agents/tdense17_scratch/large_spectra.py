"""Stochastic spectral audit of all E99 Singer-Bu sizes. VM only; NOT certificates."""
import json
import math
from pathlib import Path
import sys
import time

import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.sparse.linalg import LinearOperator,eigsh

sys.path.insert(0,'src')
from bu import A_of_S

ROOT=Path('.research/agents/tdense17_scratch')


def run(key, stored, probes=10, depth=96, deflation=24):
    start=time.time()
    A=np.array(A_of_S(stored['S']),dtype=np.int64)
    n=len(A); X=int(A.max())
    L=1<<(2*X+2).bit_length()
    coeff=np.zeros(L); coeff[A]=1.; coeff[(-A)%L]=1.
    kernel=np.fft.rfft(coeff)
    def mv(v):
        buf=np.zeros(L); buf[A]=np.ravel(v)
        return np.fft.irfft(np.fft.rfft(buf)*kernel,L)[A]
    op=LinearOperator((n,n),matvec=mv,dtype=float)
    top,U=eigsh(op,k=deflation,which='LA',tol=1e-9,ncv=3*deflation+10,
                 v0=np.random.default_rng(17).normal(size=n))
    order=np.argsort(top)[::-1]; top=top[order]; U=U[:,order]
    bottom=float(eigsh(op,k=1,which='SA',tol=1e-9,
                       v0=np.random.default_rng(18).normal(size=n))[0][0])
    degree=mv(np.ones(n))
    assert np.max(np.abs(degree-np.rint(degree)))<1e-5
    tr2=int(np.rint(degree).sum())
    tau=math.sqrt(n)
    def funcs(w):
        low=w<=tau
        return np.array([np.sum(w*w*(np.abs(w)<=tau)),
                         np.sum(w*w*(np.abs(w)<=2*tau)),
                         np.sum(w*w*(w<0)), np.sum(w*(w>0)),
                         np.sum(w*w*(w>0)), np.sum(low),
                         np.sum(w*low),np.sum(w*w*low),
                         np.sum(w**3),np.sum(w**4)])
    topfun=funcs(top)
    samples={48:[],depth:[]}
    rng=np.random.default_rng(20261019)
    for probe in range(probes):
        z=rng.choice([-1.,1.],size=n)
        z-=U@(U.T@z)
        weight=float(z@z)
        q=z/math.sqrt(weight); previous=np.zeros(n); beta=0.
        basis=np.empty((n,depth)); diag=[]; off=[]
        for j in range(depth):
            basis[:,j]=q
            w=mv(q)-beta*previous
            alpha=float(q@w); w-=alpha*q
            # Full reorthogonalization and projection away from known positive outliers.
            w-=U@(U.T@w)
            for _ in range(2): w-=basis[:,:j+1]@(basis[:,:j+1].T@w)
            diag.append(alpha)
            beta=float(np.linalg.norm(w))
            if j+1 in samples:
                nodes,V=eigh_tridiagonal(np.array(diag),np.array(off))
                quadweight=weight*V[0,:]**2
                low=nodes<=tau
                fun=np.array([np.sum(quadweight*nodes**2*(np.abs(nodes)<=tau)),
                              np.sum(quadweight*nodes**2*(np.abs(nodes)<=2*tau)),
                              np.sum(quadweight*nodes**2*(nodes<0)),
                              np.sum(quadweight*nodes*(nodes>0)),
                              np.sum(quadweight*nodes**2*(nodes>0)),
                              np.sum(quadweight*low),np.sum(quadweight*nodes*low),
                              np.sum(quadweight*nodes**2*low),
                              np.sum(quadweight*nodes**3),np.sum(quadweight*nodes**4)])
                samples[j+1].append(fun+topfun)
            if j+1<depth:
                off.append(beta); previous=q; q=w/beta
    out=dict(q=int(key),n=n,X=X,probes=probes,depth=depth,deflation=deflation,
             seed=20261019,tr2=tr2,alpha=tr2/n**2,
             bottom_over_sqrtn=-bottom/tau, top_eigenvalues=top.tolist(),
             R_cert_quoted=stored['R_cert'])
    for dep,ss in samples.items():
        ss=np.array(ss); mean=ss.mean(axis=0); se=ss.std(axis=0,ddof=1)/math.sqrt(probes)
        b1,b2,neg2,trP,trP2,count,first,second,t3,t4=mean
        mu=first/count; var=second/count-mu**2
        out['depth'+str(dep)]=dict(beta1=b1/n**2,beta2=b2/n**2,
            beta1_standard_error=se[0]/n**2,beta2_standard_error=se[1]/n**2,
            psd_distance=math.sqrt(neg2)/n,r_eff=trP**2/trP2,
            traceP_n32=trP/n**1.5,mu_cut=mu,variance_cut=var,
            bd_over_sqrtn=(var/(tau+abs(mu))+abs(mu))/tau,
            tr3_n3=t3/n**3,tr4_n4=t4/n**4,
            residual4_n3=(t4-top[0]**4)/n**3,
            raw_estimates=mean.tolist(),raw_standard_errors=se.tolist())
    out['seconds']=time.time()-start
    print(json.dumps({k:v for k,v in out.items() if k!='top_eigenvalues'}),flush=True)
    return out


def main():
    sb=json.load(open('examples/singer_bu/certified.json'))
    if len(sys.argv)>1 and sys.argv[1]=='validate':
        out=run('61',sb['61'],probes=80)
        (ROOT/'large_validation.json').write_text(json.dumps(out,indent=2)+'\n')
        return
    out=[]
    for key in ('61','101','151','199'):
        out.append(run(key,sb[key]))
        (ROOT/'large_spectra.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
