"""Exact QQ/Bernstein certificate for t-dependent potentials and continuum Schur.
Numerical solver outputs are inputs to reconstruction only; every sign is exact.
"""
import os
os.environ['SYMPY_GROUND_TYPES']='flint'
import json,math,sys,time
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import numpy as np
OUT=Path('.research/agents/tdense11_scratch')
sys.path.insert(0,str(Path('.research/agents/tdense8_scratch').resolve()))
from potential import add,mul,compose,peval,bern
from flint import fmpq_poly,fmpq
def bern(p,lo,hi):
    n=len(p)-1;linear=fmpq_poly([fmpq(lo.numerator,lo.denominator),fmpq((hi-lo).numerator,(hi-lo).denominator)])
    composed=fmpq_poly([0])
    for c in reversed(p):composed=composed*linear+fmpq(c.numerator,c.denominator)
    return [sum((composed[j]*fmpq(comb(k,j),comb(n,j)) for j in range(k+1)),fmpq(0)) for k in range(n+1)]

def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def divide_endpoint(p):
    if peval(p,Q(1))!=0:return p,False
    out=[];s=Q(0)
    for v in p[:-1]:s+=v;out.append(s)
    assert -out[-1]==p[-1]
    return trim(out),True

def bpower(bs):
    m=len(bs)-1;p=[Q(0)]*(m+1)
    for k,v in enumerate(bs):
        for j in range(m-k+1):p[k+j]+=v*comb(m,k)*comb(m-k,j)*(-1)**j
    return trim(p)

def sqrt_floor(x,den=10**10):
    return Q(math.isqrt(x.numerator*den**2//x.denominator),den)

def cosupper(k):
    # Machin: pi/4=4 atan(1/5)-atan(1/239). Alternating rational series.
    def atanbounds(z,N=42):
        a=sum(((-1)**j*z**(2*j+1)/Q(2*j+1) for j in range(N)),Q(0))
        b=a+(-1)**N*z**(2*N+1)/Q(2*N+1)
        return min(a,b),max(a,b)
    al,ah=atanbounds(Q(1,5));bl,bh=atanbounds(Q(1,239));pl=16*al-4*bh
    z=pl/Q(k+2);v=sum(((-1)**j*z**(2*j)/Q(math.factorial(2*j)) for j in range(13)),Q(0))
    # even truncation j=12 is an upper bound; pi lower gives cos upper.
    den=10**10;return Q((v.numerator*den+v.denominator-1)//v.denominator,den)

def schur_poly(a,shape,K,cell):
    mid=Q(2*cell+1,2*K);U=[Q(0),Q(1),2*shape,-4*shape/3]
    pp=[Q(0)]
    def clipped(c0,c1):
        v=c0+c1*mid
        if v<=0:return [Q(0)]
        if v>=1:return [peval(U,Q(1))]
        return compose(U,[c0,c1])
    for j,v in enumerate(a):
        lo,hi=Q(j,K),Q(j+1,K)
        term=add(clipped(-lo,Q(1)),[-c for c in clipped(-hi,Q(1))])
        term=add(term,clipped(hi,Q(1)));term=add(term,[-c for c in clipped(lo,Q(1))])
        pp=add(pp,[v*c for c in term])
    return trim(pp)

def run(path,slack=Q(1,100000),D=Q(13,100)):
    rec=json.loads(OUT.joinpath(path).read_text());K=rec['K'];deg=rec['degree'];shape=Q(str(rec['shape']))
    a=[Q(math.ceil(x*10**9),10**9)+slack for x in rec['a']]
    bs=[[Q(round(x*10**10),10**10) for x in row] for row in rec['beta']]
    assert all(row[0]==0 and all(row[i]<=row[i+1] for i in range(deg)) for row in bs)
    beta=[bpower(row) for row in bs];xb=[Q(1),Q(0),-Q(1)]
    gram=json.load(open('.research/agents/tdense9_scratch/long_gram_bounds.json'))
    support=json.load(open(OUT/'support_lines.json'))
    common=[[Q(0)],[Q(1),Q(0),-Q(4),Q(0),Q(2)],[Q(1),-Q(1),-Q(1)]]+[[Q(r['m'])+Q(r['b']),Q(0),-Q(r['m'])] for r in gram]
    vpoly=[Q(0),Q(0),Q(1,2),Q(0),-Q(1,4)]
    leaves=[];failed=[];started=time.time()
    for jj in range(2*K):
        j=jj//2;k=(2*K+jj-1)//jj-1 if jj else None
        extra=support.get(str(k),[])
        branches=common+[[Q(r['m'])+Q(r['b']),Q(0),-Q(r['m'])] for r in extra]
        cap=cosupper(k) if jj else Q(1)
        ulo=sqrt_floor(1-cap)
        # We deliberately enlarge x range by rounding u down.
        base=add([a[j]-Q(1,2),Q(0),-a[j]],[-x/2 for x in compose(beta[j],xb)])
        As={};Ps={};factors={}
        def build(b):
            br=branches[b]
            A=add(base,compose(beta[jj],br)) if jj<K else base
            P=add(vpoly,[-x for x in mul(A,A)])
            P,factor=divide_endpoint(P)
            As[b]=A;Ps[b]=P;factors[b]=factor
        stack=[(ulo,Q(1),0)];local=[]
        while stack:
            lo,hi,depth=stack.pop();mid=(lo+hi)/2
            candidates=sorted(range(len(branches)),key=lambda b:peval(branches[b],mid),reverse=True)[:3]
            valid=[]
            for b in candidates+[0]:
                br=branches[b]
                bc=bern(br,lo,hi)
                if min(bc)>=0 and max(bc)<=1:valid.append(b)
            valid.sort(key=lambda b:peval(branches[b],mid),reverse=True)
            done=False
            for b in valid:
                if b not in As:build(b)
                ba=bern(As[b],lo,hi)
                if min(ba)>=0:
                    local.append(dict(lo=str(lo),hi=str(hi),branch=b,mode='A',min=str(min(ba))));done=True;break
                bp=bern(Ps[b],lo,hi)
                if min(bp)>=0:
                    local.append(dict(lo=str(lo),hi=str(hi),branch=b,mode='square',endpoint_factor=factors[b],min=str(min(bp))));done=True;break
            if done:continue
            if depth>=28:
                failed.append(dict(jj=jj,lo=str(lo),hi=str(hi)));break
            stack.extend([(lo,mid,depth+1),(mid,hi,depth+1)])
        leaves.append(dict(jj=jj,cap=str(cap),u_lower=str(ulo),support_k=k,branches=[[str(v) for v in br] for br in branches],leaves=local))
        print('POINTWISE',jj,'leaves',len(local),'failed',len(failed),'seconds',round(time.time()-started,2),flush=True)
        if failed:break
    schur=[];Utest=[Q(1),4*shape,-4*shape]
    for cell in range(K):
        P=schur_poly(a,shape,K,cell);rhs=add([2*D*x for x in Utest],[-x for x in P]);minb=min(bern(rhs,Q(cell,K),Q(cell+1,K)))
        schur.append(dict(cell=cell,min_bernstein=str(minb),polynomial=list(map(str,rhs))))
    good=not failed and all(Q(x['min_bernstein'])>=0 for x in schur)
    out=dict(status='PROVED' if good else 'UNRESOLVED',source=path,K=K,degree=deg,D1=str(D),C10=str(1/D),C10_float=float(1/D),a=list(map(str,a)),beta_bernstein=[[str(x) for x in row] for row in bs],beta_power=[[str(x) for x in row] for row in beta],shape=str(shape),pointwise=leaves,failed=failed,schur=schur,min_schur=str(min(Q(x['min_bernstein']) for x in schur)),seconds=time.time()-started)
    OUT.joinpath('certificate_td.json').write_text(json.dumps(out,indent=2))
    print('RESULT',json.dumps({k:v for k,v in out.items() if k not in ('a','beta_bernstein','beta_power','pointwise','schur')}),flush=True)
if __name__=='__main__':run(sys.argv[1],Q(sys.argv[2]) if len(sys.argv)>2 else Q(1,100000),Q(sys.argv[3]) if len(sys.argv)>3 else Q(13,100))
