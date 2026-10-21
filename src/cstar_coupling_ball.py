"""Direct a=n, Q<=25n mixed-certificate probes on arbitrary supports.

The finite proposal is a Gram-normalized trust-region problem. Exact
integer reconstruction fixes coupling after rounding; no global finite
or universal optimality claim relies on floating eigenvalues.
"""
from collections import Counter
from fractions import Fraction as F
import json
import math
from pathlib import Path
import socket
import numpy as np
from scipy.linalg import null_space
from scipy.sparse import csr_matrix
from cstar_ordered_prefix import directions


def ball_minimum(C,b,radius):
    if C.shape[0]==0:return np.zeros(0)
    vals,U=np.linalg.eigh((C+C.T)/2);d=U.T@b;r2=radius*radius
    lo=max(0.,-vals[0]);tol=1e-10*max(1.,np.max(np.abs(vals)))
    gap=vals+lo;regular=gap>tol
    u=np.zeros_like(d);u[regular]=-d[regular]/gap[regular]
    if np.linalg.norm(d[~regular])<tol and u@u<=r2:
        if lo>0:u[int(np.argmin(vals))]=math.sqrt(max(0.,r2-u@u))
        return U@u
    def value(lam):return float(np.sum((d/(vals+lam))**2))
    left=lo+tol;right=max(left+1.,2*left)
    while value(right)>r2:right=2*right+1
    for _ in range(100):
        mid=(left+right)/2
        if value(mid)>r2:left=mid
        else:right=mid
    return U@(-d/(vals+right))


def solve(row):
    A=row['actual'];n=len(A);D,allrows=directions(A,[1]*n,row['suffix']);rows=allrows[1:]
    support=sorted({w for r in rows for w in r});index={w:i for i,w in enumerate(support)}
    B=np.zeros((len(rows),len(support)),dtype=np.int64)
    for j,r in enumerate(rows):
        for w,c in r.items():B[j,index[w]]=c
    ii=[];jj=[]
    for i,w in enumerate(support):
        for s in D:
            j=index.get(w+s)
            if j is not None:ii.append(i);jj.append(j)
    kernel=csr_matrix((np.ones(len(ii),dtype=np.int64),(ii,jj)),shape=(len(support),len(support)))
    Q=B@B.T;H=B@(kernel@B.T)
    a=np.array([sum(r.get(s,0) for s in D) for r in rows],dtype=float)
    vals,U=np.linalg.eigh(Q.astype(float));keep=vals>max(vals)*1e-11;W=U[:,keep]/np.sqrt(vals[keep])
    g=W.T@a;assert abs(g@g-2*n)<1e-6*n
    T=W.T@H@W;T=(T+T.T)/2;center=n*g/(g@g);Z=null_space(g[None,:])
    radius=math.sqrt(24*n-center@center)
    u=ball_minimum(Z.T@T@Z,Z.T@T@center,radius);weights=W@(center+Z@u)
    scale=2**20;rounded=list(map(int,np.rint(weights*scale)))
    raw_a=sum(int(a[i])*rounded[i] for i in range(len(rows)))
    numerator=[2*n*v for v in rounded];numerator[0]+=n*scale-raw_a
    den=2*n*scale
    poly={w:sum(numerator[i]*int(B[i,j]) for i in range(len(rows))) for j,w in enumerate(support)}
    poly={w:c for w,c in poly.items() if c}
    q=sum(v*v for v in poly.values());aexact=sum(poly.get(s,0) for s in D)
    h=sum(numerator[i]*int(H[i,j])*numerator[j] for i in range(len(rows)) for j in range(len(rows)))
    assert aexact==n*den and q<=25*n*den*den
    gamma=0 if h<=0 else max(1,math.ceil(h/(den*den*n**1.5)))
    while h>0 and h*h>gamma*gamma*n**3*den**4:gamma+=1
    Qf=q/den**2;Hf=h/den**2
    root=2*n*n/(Hf+math.sqrt(Hf*Hf+4*Qf*n*n)) if Hf>=0 else (-Hf+math.sqrt(Hf*Hf+4*Qf*n*n))/(2*Qf)
    K=F(max(1,math.floor(root*10**8)-2),10**8)
    assert q*K*K+h*K-n*n*den*den<0
    result=dict(label=row['label'],suffix=row['suffix'],actual=A,n=n,max_A=max(A),
                coefficient_denominator=den,integer_weights=[0]+numerator,
                test_polynomial=[[w,c] for w,c in sorted(poly.items())],a=n,
                norm_numerator=q,energy_numerator=h,Q_over_n_exact=str(F(q,n*den*den)),
                H_over_n32_float=h/(den*den*n**1.5),certified_integer_gamma=gamma,
                global_M_lower=str(K/2),global_M_upper=str(n),
                qualification='Exact achieved coupling, norm and mixed cost; trust-region optimum is numerical only.')
    print(json.dumps({k:result[k] for k in ['label','suffix','n','Q_over_n_exact','H_over_n32_float',
                      'certified_integer_gamma','global_M_lower']}),flush=True)
    return result


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    source=Path('.research/experiments/ordered_prefix_2026-10-20')
    wanted={'hereditary8','interval64','N50_x71','N50_x72','root_difference_r12',
            'forced_plateau_L64','forced_plateau_L729','sparse_seed20261023',
            'cyclic_cone_lift_p7','balanced_r8_k2'}
    inputs=[]
    for name in ['results.json','extra.json']:
        inputs.extend(r for r in json.loads((source/name).read_text())['cases'] if r['Boolean'] and r['label'] in wanted)
    out=[]
    for row in inputs:
        out.append(solve(row));(source/'coupling.json').write_text(json.dumps(dict(cases=out,host=socket.gethostname()),indent=2)+'\n')


if __name__=='__main__':main()
