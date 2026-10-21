"""Adaptive ordered-prefix witness spaces for arbitrary integer supports.

Numerical Gram-normalized optimization proposes integer witnesses.
All reported Rayleigh bounds use exact integer quadratic forms.
No finite success is an asymptotic or universal theorem.
"""
from collections import Counter
from fractions import Fraction as F
import itertools
import json
import math
from pathlib import Path
import socket
import sys
import numpy as np
from scipy.sparse import csr_matrix


def directions(A,nums,suffix=False,include_D=True):
    D={s:c for a,c in zip(A,nums) for s in [a,-a]};rows=[{0:1}]
    if include_D:rows.append(D)
    for j,a in enumerate(A):
        row=Counter()
        for b in [0]+A[:j]:row[a-b]+=1;row[b-a]+=1
        rows.append(dict(row))
    if suffix:
        for j,a in enumerate(A):
            row=Counter({a:1,-a:1})
            for b in A[j+1:]:row[b-a]+=1;row[a-b]+=1
            rows.append(dict(row))
    return D,rows


def solve(label,A,nums=None,denom=1,suffix=False):
    A=sorted(A);nums=[1]*len(A) if nums is None else list(nums)
    assert len(A)==len(set(A)) and min(A)>0 and len(A)==len(nums)
    include_D=denom==1
    # Weighted controls have all consecutive frequencies; prefix differences
    # already span their D, so omit the large-denominator redundant row.
    if not include_D:assert A==list(range(1,len(A)+1))
    D,rows=directions(A,nums,suffix,include_D);support=sorted({w for r in rows for w in r});index={w:i for i,w in enumerate(support)}
    B=np.zeros((len(rows),len(support)),dtype=np.int64)
    for j,row in enumerate(rows):
        for w,c in row.items():B[j,index[w]]=c
    ii=[];jj=[];vv=[]
    for i,w in enumerate(support):
        for s,c in D.items():
            j=index.get(w+s)
            if j is not None:ii.append(i);jj.append(j);vv.append(c)
    kernel=csr_matrix((vv,(ii,jj)),shape=(len(support),len(support)),dtype=np.int64)
    Q=B@B.T;H=B@(kernel@B.T);assert np.array_equal(H,H.T)
    val,U=np.linalg.eigh(Q.astype(float));keep=val>max(val)*1e-11
    W=U[:,keep]/np.sqrt(val[keep]);small=W.T@(H/denom)@W
    eigen,V=np.linalg.eigh((small+small.T)/2);weights=W@V[:,0]
    weights/=np.max(np.abs(weights));weights=list(map(int,np.rint(weights*10**8)))
    q=sum(weights[i]*int(Q[i,j])*weights[j] for i in range(len(rows)) for j in range(len(rows)))
    h=sum(weights[i]*int(H[i,j])*weights[j] for i in range(len(rows)) for j in range(len(rows)))
    assert q>0 and h<0
    poly={w:sum(weights[i]*int(B[i,j]) for i in range(len(rows))) for j,w in enumerate(support)}
    poly={w:c for w,c in poly.items() if c};N2=2*sum(F(c,denom)**2 for c in nums)
    bound=F(-h,2*q*denom)
    result=dict(label=label,actual=A,coefficient_numerators=nums,coefficient_denominator=denom,
                Boolean=all(c==denom for c in nums),n=len(A),max_A=max(A),suffix=suffix,
                include_D_basis_row=include_D,N2=str(N2),
                coefficient_Boolean_defect=str(sum(F(c,denom)**2*(1-F(c,denom))**2 for c in nums)),
                basis_count=len(rows),support_count=len(support),numerical_Gram_rank=int(sum(keep)),
                discarded_Gram_eigenvalues_are_not_exact_nullity=True,
                global_M_lower=str(bound),K_over_sqrt_N2=float(2*bound)/math.sqrt(float(N2)),
                numerical_K=-float(eigen[0]),integer_weights=weights,norm_numerator=q,
                Dnum_energy_numerator=h,test_polynomial=[[w,c] for w,c in sorted(poly.items())],
                qualification='Exact achieved Rayleigh bound; eigenvalues/rank are numerical, '
                              'no global optimum or universal lower bound inferred.')
    print(json.dumps({k:result[k] for k in ['label','suffix','n','support_count','basis_count',
                    'numerical_Gram_rank','K_over_sqrt_N2']}),flush=True)
    return result


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    root=Path('.research/experiments/ordered_prefix_2026-10-20');root.mkdir(parents=True,exist_ok=True)
    cases=[('hereditary8',[1,2,3,4,5,6,7,9],None,1)]
    cases += [(f'interval{n}',list(range(1,n+1)),None,1) for n in [16,32,64]]
    for tag,row in json.loads(Path('examples/construct/N50_certified.json').read_text()).items():
        cases.append((tag,sorted(row['A']),None,1))
    for r in [6,8,10,12]:
        A=sorted({(7**j-7**i)//6 for j in range(r) for i in range(j)})
        cases.append((f'root_difference_r{r}',A,None,1))
    for r in [6,7,8]:
        S=set()
        for plus in itertools.combinations(range(r),2):
            for minus in itertools.combinations([j for j in range(r) if j not in plus],2):
                value=sum(7**i for i in plus)-sum(7**j for j in minus)
                if value>0:S.add(value)
        cases.append((f'balanced_r{r}_k2',sorted(S),None,1))
    rng=np.random.default_rng(20261023)
    cases.append(('sparse_seed20261023',sorted(map(int,rng.choice(np.arange(1,1001),24,replace=False))),None,1))
    for L in [16,32,64]:cases.append((f'weighted_fejer{L}',list(range(1,L+1)),list(range(L,0,-1)),L+1))
    extra='--extra' in sys.argv
    if extra:
        cases=[]
        plateau=json.loads(Path('.research/experiments/forced_plateau_2026-10-20/results.json').read_text())
        for row in plateau['cases']:
            if row['L']<=729:cases.append((f"forced_plateau_L{row['L']}",sorted(row['A']),None,1))
        for p in [3,5,7]:
            B=12*p+1;h=(p-1)//2;A=set()
            for x,y,z,w in itertools.product(range(-h,h+1),repeat=4):
                if (x,y,z,w)!=(0,0,0,0) and (x*w-y*z)%p==0:
                    a=x+B*y+B*B*z+B**3*w
                    if a>0:A.add(a)
            assert 2*len(A)==p**3+p*p-p-1
            cases.append((f'cyclic_cone_lift_p{p}',sorted(A),None,1))
        for X in [64,128,256]:
            s=1;qperiod=4*s*s+1;T=2*s*4096;denom=2*(X+1)*T;nums=[]
            for k in range(1,X+1):
                residual=(X+1)**2-(X+1-k)**2;integer_sqrt=math.isqrt(T*T*residual)
                pnum=T*(X+1)-integer_sqrt-int(integer_sqrt*integer_sqrt<T*T*residual)
                rnum=(X+1-k)*(4*s*s if k%qperiod==0 else -1)*4096
                nums.append(pnum+rnum)
            cases.append((f'weighted_P61_periodic_X{X}',list(range(1,X+1)),nums,denom))
    out=[]
    for label,A,nums,denom in cases:
        for suffix in [False,True]:
            result=solve(label,A,nums,denom,suffix)
            if label.startswith('weighted_fejer'):
                result['global_M_upper']='1/2';assert F(result['global_M_lower'])<=F(1,2)
            if label.startswith('weighted_P61'):
                result['global_M_upper']=str(F(3,4)+F(len(A),denom))
                result['upper_certificate']='Catalan PD profile plus two symmetric Fejer packet pairs; coefficient rounding error.'
                assert F(result['global_M_lower'])<=F(result['global_M_upper'])
            out.append(result)
            (root/('extra.json' if extra else 'results.json')).write_text(json.dumps(dict(host=socket.gethostname(),seed=20261023,cases=out),indent=2)+'\n')


if __name__=='__main__':main()
