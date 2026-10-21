"""Full-space resolvent proposals and an exact lower bound for a prefix space.

Numerical integrals/eigenvalues only propose rational polynomials and
dual parameters. Integer Fourier moments and a positive-definite exact
matrix supply the saved certificates. All computation on Dirichlet.
"""
from fractions import Fraction as F
import json
import math
from pathlib import Path
import socket
import numpy as np
from scipy.linalg import null_space
from scipy.optimize import brentq
from scipy.sparse import csr_matrix
import flint
from cstar_ordered_prefix import directions
from cstar_coupling_ball import ball_minimum


def positive_leading_minors(matrix):
    M=[[int(t) for t in row] for row in matrix];pivots=[];previous=1
    for k in range(len(M)):
        pivot=M[k][k]
        if pivot<=0:return None
        pivots.append(pivot)
        if k==len(M)-1:break
        for i in range(k+1,len(M)):
            for j in range(k+1,len(M)):
                numerator=pivot*M[i][j]-M[i][k]*M[k][j]
                quotient,remainder=divmod(numerator,previous);assert remainder==0
                M[i][j]=quotient
        previous=pivot
    return pivots


def prefix_dual(A):
    n=len(A);D,rows=directions(A,[1]*n);rows=rows[1:]
    support=sorted({w for r in rows for w in r});index={w:i for i,w in enumerate(support)}
    B=np.array([[r.get(w,0) for w in support] for r in rows],dtype=np.int64)
    ii=[];jj=[]
    for i,w in enumerate(support):
        for s in D:
            j=index.get(w+s)
            if j is not None:ii.append(i);jj.append(j)
    kernel=csr_matrix((np.ones(len(ii),dtype=np.int64),(ii,jj)),shape=(len(support),len(support)))
    Q=B@B.T;H=B@(kernel@B.T);a=np.array([sum(r.get(w,0) for w in D) for r in rows],dtype=np.int64)
    vals,U=np.linalg.eigh(Q.astype(float));assert min(vals)>1e-8
    W=U/np.sqrt(vals);g=W.T@a;T=W.T@H@W;Z=null_space(g[None,:]);center=n*g/(g@g)
    C=Z.T@T@Z;b=Z.T@T@center;u=ball_minimum(C,b,math.sqrt(25*n-center@center))
    lam=-float(u@(C@u+b))/(u@u);y=center+Z@u;eta=float(y@(T+lam*np.eye(len(T)))@y)/(n*n)
    den=10**6
    for padding in [1,10,100,1000,10000]:
        lp=math.ceil(lam*den)+padding;ep=math.floor(eta*den)-padding
        assert lp>=0
        M=den*H+lp*Q-ep*np.outer(a,a);pivots=positive_leading_minors(M)
        if pivots is not None:
            lower=F(ep*n*n-lp*25*n,den)
            return dict(lambda_numerator=lp,eta_numerator=ep,denominator=den,
                        positive_leading_minors=pivots,H_lower=str(lower),norm_budget=25*n,
                        basis_count=len(rows),meaning='For every mean-zero prefix-space q with a=n,Q<=25n, H>=H_lower.')
    raise RuntimeError('No exact positive-definite prefix dual found')


def full_w2_cap(A):
    S=set(A)|{-a for a in A};W=sorted({0}|S|{a+b for a in S for b in S})
    M=flint.fmpz_mat([[15*int(i==j)+2*int(x-y in S) for j,y in enumerate(W)] for i,x in enumerate(W)])
    # det(tI+M) has only positive coefficients, so no root t>=0.
    # M is real symmetric; therefore every eigenvalue is positive.
    coeff=list((-M).charpoly());assert all(c>0 for c in coeff)
    return dict(rows=W,integer_shift=15,integer_scale=2,K_upper='15/2',
                charpoly_of_negative_matrix=list(map(int,coeff)),
                meaning='2*B_W2+15I is positive definite; every full-W2 Rayleigh certificate has K<15/2.')


def rational_polynomial(A,coeff,B):
    n=len(A);scale=2**20;raw=[int(round(float(t)*scale)) for t in coeff[1:B+1]]
    a_raw=2*sum(raw[a-1] for a in A);deficit=n*scale-a_raw
    nums=[2*n*c+deficit*int(j+1 in A) for j,c in enumerate(raw)];den=2*n*scale
    assert 2*sum(nums[a-1] for a in A)==n*den
    z=nums[::-1]+[0]+nums;square=flint.fmpz_poly(z)**2
    Q=sum(c*c for c in z);H=2*sum(int(square[2*B+a]) for a in A)
    assert int(square[2*B])==Q and Q<=25*n*den*den
    q=Q/den**2;h=H/den**2
    root=(-h+math.sqrt(h*h+4*q*n*n))/(2*q) if h<0 else 2*n*n/(h+math.sqrt(h*h+4*q*n*n))
    K=F(math.floor(root*10**8)-2,10**8);assert Q*K*K+H*K-n*n*den*den<0
    return dict(degree=B,positive_numerators=nums,denominator=den,a=n,norm_numerator=Q,
                energy_numerator=H,Q_over_n=str(F(Q,n*den*den)),H=str(F(H,den*den)),
                global_M_lower=str(K/2),qualification='Exact achieved Fourier polynomial; no exact global optimality claim.')


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    source=json.loads(Path('examples/construct/N50_certified.json').read_text())['N50_x72']
    A=sorted(source['A']);n=len(A);X=max(A);upper=F(source['sturm_up'][0],source['sturm_up'][1])
    root=Path('.research/experiments/resolvent_2026-10-20');root.mkdir(parents=True,exist_ok=True)
    dual=prefix_dual(A);cap=full_w2_cap(A);trials=[];probes=[]
    for L in [2**16,2**18]:
        spectrum=np.zeros(L)
        spectrum[A]=1;spectrum[-np.array(A)]=1;D=np.fft.ifft(spectrum).real*L
        def stats(lam,output=False):
            h=1/(lam+D);I=float(np.mean(h));gap=lam*I-1
            q=n*(I-h)/gap;Q=float(np.mean(q*q))
            return (Q,I,gap,q) if output else Q
        left=float(2*upper)+1e-9;assert stats(left)>24*n
        right=max(left*2,2*n)
        while stats(right)>24*n:right*=2
        lam=brentq(lambda t:stats(t)-24*n,left,right,xtol=1e-12)
        Q,I,gap,q=stats(lam,True);cost=float(np.mean(D*q*q));coeff=np.fft.fft(q).real/L
        probe=dict(grid=L,lambda_float=lam,I_float=I,norm_float=Q,cost_float=cost,
                   cost_from_resolvent_float=n*n*I/gap-lam*Q,
                   all_quadrature_and_lambda_values_uncertified=True)
        probes.append(probe)
        if L==2**18:
            for factor in [1,2,4,8,16]:
                row=rational_polynomial(A,coeff,factor*X)
                row['strictly_below_prefix_dual']=F(row['H'])<F(dual['H_lower']);trials.append(row)
                row['exceeds_full_W2_K_cap']=2*F(row['global_M_lower'])>F(cap['K_upper'])
                print(json.dumps({k:row[k] for k in ['degree','Q_over_n','H','global_M_lower',
                                 'strictly_below_prefix_dual']}),flush=True)
    out=dict(host=socket.gethostname(),actual=A,n=n,max_A=X,global_M_upper=str(upper),
             upper_status='Imported existing exact Sturm certificate; not rerun here.',
             prefix_dual=dual,full_W2_cap=cap,numerical_resolvent=probes,polynomials=trials)
    (root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(prefix_H_lower=dual['H_lower'],numerical_cost=probes[-1]['cost_float'])),flush=True)


if __name__=='__main__':main()
