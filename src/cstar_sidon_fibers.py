"""Lifted parabola difference fibers: residue/plane/global diagnostics.

All computation on Dirichlet. FFT and optimization only select points;
Arb certifies the saved negative points, never a global upper bound.
"""
from collections import Counter,defaultdict
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path
import socket
import flint
import numpy as np
from scipy.optimize import minimize


def prime(n):
    return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))


def largest_prime(n):
    return next(p for p in range(n,2,-1) if prime(p))


def differences(B):
    ans=[]
    for i,(a,b) in enumerate(B):
        for c,d in B[:i]:
            x,y=int(a-c),int(b-d)
            if x<0 or (x==0 and y<0):x,y=-x,-y
            ans.append((x,y))
    assert len(set(ans))==len(ans) and (0,0) not in ans
    return ans


def matrix_sample(p,rng,rotated=True):
    if not rotated:return np.eye(2,dtype=int)
    while True:
        A=rng.integers(0,p,size=(2,2))
        if int(A[0,0]*A[1,1]-A[0,1]*A[1,0])%p:return A


def ensemble_check(p):
    hist=Counter();G=[a for a in itertools.product(range(p),repeat=4) if (a[0]*a[3]-a[1]*a[2])%p]
    curve=np.array([(t,t*t%p) for t in range(p)])
    for A in G:
        base=curve@np.array(A).reshape(2,2).T
        for shift in itertools.product(range(p),repeat=2):
            B=(base+np.array(shift))%p
            hist.update(differences([tuple(z) for z in B]))
    for x in range(p):
        for y in range(-p+1,p):
            if x==0 and y<=0:continue
            assert F(hist[x,y],len(G)*p*p)==F(p,p+1)*F(p-x,p)*F(p-abs(y),p)
    return dict(p=p,ensembles=len(G)*p*p,exact_marginal_identity=True)


def local_ramanujan(g,p,k):
    if g%(p**k)==0:return F(1)
    if g%(p**(k-1))==0:return -F(1,p*p-1)
    return F(0)


def factor(q):
    out=[];p=2
    while p*p<=q:
        k=0
        while q%p==0:q//=p;k+=1
        if k:out.append((p,k))
        p+=1
    if q>1:out.append((q,1))
    return out


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    flint.ctx.prec=160
    out=dict(qualification='Boolean Sidon fibers; certified point/positive-average lower bounds; '
             'right-plane FFT minima and optimizers are numerical diagnostics only.',
             ensemble_checks=[ensemble_check(p) for p in [3,5]],cases=[])
    root=Path('.research/experiments/sidon_fibers_2026-10-20');root.mkdir(parents=True,exist_ok=True)
    for X,rotated in [(64,True),(256,False),(256,True),(1024,True)]:
        U=round(X**(1/3))
        while (U+1)**3<=X:U+=1
        while U**3>X:U-=1
        rng=np.random.default_rng(20261021+X+int(rotated));fibers=[];content=Counter();right=defaultdict(list);allM=[]
        for a in range(U+1):
            for b in range(-U,U+1):
                d=a*a+b*b
                if not (a>0 or b>0) or math.gcd(a,abs(b))!=1 or d>U*U:continue
                p=largest_prime(math.isqrt(X*X//(2*d)))
                A=matrix_sample(p,rng,rotated);shift=rng.integers(0,p,size=2)
                points=[tuple(map(int,z)) for z in ((np.array([(t,t*t%p) for t in range(p)])@A.T+shift)%p)]
                W=differences(points)
                for x,y in W:
                    g=math.gcd(abs(x),abs(y));v=(x//g,y//g)
                    content[g]+=1;right[v].append((g*a,g*b))
                    allM.append((a*x,a*y,b*x,b*y))
                fibers.append(dict(u=[a,b],p=p,A=A.tolist(),shift=list(map(int,shift)),points=points))
        n=sum(content.values());assert len(set(allM))==n
        h=[6000*X**3+i for i in [1,3,5,7]];P=math.prod(h);C=[P//z for z in h]
        encoded=sorted(abs(sum(ci*mi for ci,mi in zip(C,M))) for M in allM)
        assert 0 not in encoded and len(set(encoded))==n
        error=F(44*X*n,7*min(h));residues=[]
        for q in range(2,129):
            factors=factor(q);average=F(0)
            for g,count in content.items():
                coefficient=F(1)
                for p,k in factors:coefficient*=local_ramanujan(g,p,k)
                average+=count*coefficient
            residues.append(dict(q=q,average_f=str(average),scalar_M_lower=str(max(F(0),-average-error))))
        best_residue=max(residues,key=lambda z:F(z['scalar_M_lower']))
        # Rank-two matrix points: evaluate via the square identity, using
        # only sum p terms rather than all sum p(p-1)/2 differences.
        coordinates=[(np.array(f['u']),np.array(f['points'])) for f in fibers]
        def value_gradient(Y):
            Y=Y.reshape(2,2);value=0.;grad=np.zeros((2,2))
            for u,B in coordinates:
                phase=B@(Y.T@u);e=np.exp(1j*phase);S=e.sum()
                value+=(abs(S)**2-len(B))/2
                grad+=np.outer(u,np.real(np.conj(S)*1j*(B.T@e)))
            return float(value),grad.ravel()
        seeds=[np.array(A).reshape(2,2)*math.pi for A in itertools.product([0,1],repeat=4)]
        seeds+=list(rng.uniform(0,2*math.pi,size=(32,2,2)))
        options=[minimize(lambda y:value_gradient(y),s.ravel(),jac=True,method='L-BFGS-B',
                          options={'maxiter':120,'ftol':1e-10}) for s in seeds]
        best=min(options,key=lambda z:z.fun)
        turns=[F(float((z/(2*math.pi))%1)) for z in best.x]
        k=[((2*t.numerator*hi+t.denominator)//(2*t.denominator))%hi for t,hi in zip(turns,h)]
        j=sum(ki*ci*pow(ci,-1,hi) for ki,ci,hi in zip(k,C,h))%P
        scalar_value=flint.arb(0)
        for f in fibers:
            a,b=f['u'];qx=F(a*k[0],h[0])+F(b*k[2],h[2]);qy=F(a*k[1],h[1])+F(b*k[3],h[3])
            re=flint.arb(0);im=flint.arb(0)
            for x,y in f['points']:
                angle=(x*qx+y*qy)%1;z=2*flint.arb.pi()*angle.numerator/angle.denominator
                re+=z.cos();im+=z.sin()
            scalar_value+=(re*re+im*im-f['p'])/2
        point_lower=F(max(0,math.floor(-float(scalar_value.mid())*10**6)-2),10**6)
        assert scalar_value+flint.arb(point_lower.numerator)/point_lower.denominator<0
        # Only large right fibers need scanning; smaller ones have the
        # elementary all-phase bound M<=number of terms.
        plane_rows=[];cut=max(8,int(math.sqrt(n)/8))
        for v,Z in sorted(right.items(),key=lambda z:-len(z[1])):
            if len(Z)<cut:continue
            radius=max(max(abs(x),abs(y)) for x,y in Z);K=1
            while K<4*radius+4:K*=2
            grid=np.zeros((K,K),dtype=np.complex128)
            for x,y in Z:grid[x%K,y%K]+=.5;grid[-x%K,-y%K]+=.5
            vals=np.fft.fft2(grid).real;index=np.unravel_index(np.argmin(vals),vals.shape)
            plane_rows.append(dict(v=list(v),n=len(Z),K=K,numerical_M=-float(vals[index]),grid_index=list(map(int,index))))
        max_right=max((z['numerical_M'] for z in plane_rows),default=0.)
        left_upper=max(f['p'] for f in fibers)/2
        row=dict(X=X,U=U,rotated=rotated,seed=20261021+X+int(rotated),fibers=fibers,n=n,
                 max_A=max(encoded),sha256=hashlib.sha256((' '.join(map(str,encoded))).encode()).hexdigest(),
                 content_counts={str(g):count for g,count in sorted(content.items())},
                 residue_certificates=residues,best_residue=best_residue,
                 left_plane_all_phase_M_upper=str(F(max(f['p'] for f in fibers),2)),
                 left_plane_upper_ratio=left_upper/math.sqrt(n),
                 right_plane_diagnostics=plane_rows,right_unscanned_trivial_upper=cut,
                 max_right_sampled_ratio=max_right/math.sqrt(n),
                 fractional_mean_M_upper=str(sum((F(f['p'],2*(f['p']+1)) for f in fibers),F(0))) if rotated else None,
                 h=h,j=j,P=P,crt_residues=k,scalar_f_ball=str(scalar_value),
                 point_M_lower=str(point_lower),point_ratio_lower=float(point_lower)/math.sqrt(n))
        out['cases'].append(row);(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({key:row[key] for key in ['X','U','rotated','n','left_plane_upper_ratio',
              'max_right_sampled_ratio','best_residue','point_ratio_lower']}),flush=True)


if __name__=='__main__':main()
