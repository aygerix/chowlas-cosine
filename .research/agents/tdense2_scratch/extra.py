"""Only execute on the VM through dirun.sh -c 2. Additional targeted probes."""
import json
import math
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from audit import OUT, P_ALPHA, bohr, run_one, moment_witness


def mean_half(v):
    return float((v.sum()-(v[0]+v[-1])/2)/(len(v)-1))


def mask_probe(kind,X,over):
    row=json.load(open(OUT/f'{kind}_X{X}.json'))
    par=row['parameters']
    mm=np.arange(1,X+1,dtype=np.int64)
    if kind=='bohr':
        union=np.zeros(X,dtype=bool)
        for a in par['alpha_numerators']:
            rr=(mm*a)%P_ALPHA
            union |= np.minimum(rr,P_ALPHA-rr)*(8*par['J'])<P_ALPHA
        prob=.8*(1-mm/(X+1))**2*union
    else:
        cc=np.zeros(X)
        for a in par['alpha_numerators']:
            cc+=np.cos(2*math.pi*((mm*a)%P_ALPHA)/P_ALPHA)
        prob=.5*(1-mm/(X+1))*(1+.5/par['J']*cc)
    G=1<<math.ceil(math.log2(over*X))
    coef=np.zeros(G)
    coef[row['A']]=1
    f=np.fft.rfft(coef).real
    coef[:]=0
    coef[1:X+1]=prob
    signal=np.fft.rfft(coef).real
    out=[]
    for name,H in [('reciprocal_abs_expected_signal',1/(1+abs(signal))),
                   ('positive_spike_clip',np.minimum(1,math.sqrt(row['n'])/np.maximum(f,1e-100)))]:
        Y=H*f
        mu=mean_half(Y)
        T=Y-mu
        V=mean_half(T*T)
        W=mean_half(T*T*T)
        b=W/V**1.5
        m=2*math.sqrt(V)/(math.sqrt(b*b+4)+b)
        out.append(dict(mask=name,mu=mu,V_over_n=V/row['n'],
            W_over_V_threehalves=b,M_lb_over_sqrt_n=(m-mu)/math.sqrt(row['n']),
            H_mean=mean_half(H)))
    return dict(kind=kind,X_ambient=X,grid_full_size=G,status='NUMERICAL quadrature, not certified',masks=out)


def local_rounding(X,B=4096,front=.05):
    # Exact counts at block boundaries, arbitrary rearrangement inside each block.
    den=2*X*X
    acc=old=0
    aa=np.zeros(X+1,dtype=np.int64)
    for start in range(1,X+1,B):
        end=min(X,start+B-1)
        for j in range(start,end+1):
            acc+=(X-j)**2
        new=acc//den
        count=new-old
        old=new
        if start<=front*X:
            # 1100 blocks give high q=2 variation.
            positions=[start+4*(k//2)+(k%2) for k in range(count)]
        else:
            # A single q=2 chain gives small q=2 variation.
            positions=[start+2*k for k in range(count)]
        assert all(p<=end for p in positions)
        aa[positions]=1
    p=np.r_[0,.5*(1-np.arange(1,X+1)/X)**2]
    discrepancy=float(abs(np.cumsum(aa-p)).max())
    results=[]
    for q in [2,4,8,16]:
        D=X+q
        ext=np.pad(aa,(0,q))
        j=np.arange(1,D+1)
        b=ext[j]-(ext[abs(j-q)]+np.where(j+q<=D,ext[np.minimum(j+q,D)],0))/2
        e=b*b
        E=float(e.sum())
        ws=np.arange(1,D+1)
        p0=np.cumsum(e)
        p1=np.cumsum(e*ws)
        p2=np.cumsum(e*ws*ws)
        S=p0-2*p1/(ws+1)+p2/(ws+1)**2
        W=2*(ws+1)/3+1/(3*(ws+1))
        C=.811*(D+ws+1)+71/300
        lbs=(W*E-C*S)/(2*(C-W))
        i=int(lbs.argmax())
        results.append(dict(q=q,E=E,E_over_X=E/X,best_w=i+1,
            best_m_square=float(lbs[i]),best_m_square_over_X=float(lbs[i])/X))
    return dict(X=X,B=B,front=front,n=int(aa.sum()),max_A=int(np.flatnonzero(aa)[-1]),
        prefix_discrepancy=discrepancy,prefix_discrepancy_bound=B+1,results=results)


if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='bohr4':
        res=[]
        for X in [4096,16384,65536,200000]:
            A,par=bohr(X,2026101900+X,factor=4)
            res.append(run_one(f'bohr4_X{X}',A,par,with_moments=True))
        (OUT/'bohr4_summary.json').write_text(json.dumps(res,indent=2))
    elif mode=='masks':
        res=[]
        for kind in ['bohr','fejer']:
            for X in [4096,16384,65536,200000]:
                for over in [16,32]:
                    row=mask_probe(kind,X,over)
                    res.append(row)
                    print(json.dumps(row),flush=True)
        (OUT/'masks.json').write_text(json.dumps(res,indent=2))
    elif mode=='local':
        res=[]
        B=int(sys.argv[2]) if len(sys.argv)>2 else 4096
        sizes=list(map(int,sys.argv[3:])) if len(sys.argv)>3 else [65536,262144,1048576]
        for X in sizes:
            row=local_rounding(X,B=B)
            res.append(row)
            print(json.dumps(row),flush=True)
        (OUT/('local.json' if B==4096 else f'local_B{B}.json')).write_text(json.dumps(res,indent=2))
    elif mode=='moments':
        for kind in ['bohr','fejer']:
            for X in [4096,16384,65536,200000]:
                path=OUT/f'{kind}_X{X}.json'
                row=json.load(open(path))
                row['higher_moments']=[moment_witness(row['A'],q) for q in [0,row['filter']['q']]]
                path.write_text(json.dumps(row,indent=2))
                print(json.dumps(dict(name=row['name'],bounds=[dict(q=m['q'],M_lb_over_sqrt_n=[w['M_lb_over_sqrt_n'] for w in m['witnesses']]) for m in row['higher_moments']])),flush=True)
