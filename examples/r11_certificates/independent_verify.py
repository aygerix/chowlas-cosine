"""Independent exact verifier: SymPy QQ reconstruction, own Bernstein conversion,
Lagrange interpolation of direct Schur integrals, no discovery/certifier imports.
VM only. No optimizer is used or needed to verify the artifact.
"""
import os
os.environ['SYMPY_GROUND_TYPES']='flint'
import json,sys,time,hashlib,platform
from pathlib import Path
from math import comb, factorial, isqrt
from fractions import Fraction
import sympy as sp
from flint import fmpq_poly,fmpq
OUT=Path('.research/agents/tdense11_scratch');start=time.time()
u=sp.Symbol('u');R=sp.Rational

def qstr(v):return R(str(v))
def coeffs(p):
    pp=sp.Poly(p,u,domain=sp.QQ);return [pp.nth(j) for j in range(pp.degree()+1)] if not pp.is_zero else [R(0)]
def bernown(p,l,h):
    # Compose using FLINT exact rational polynomials, then power -> Bernstein.
    cc=coeffs(p);fp=fmpq_poly([fmpq(int(c.p),int(c.q)) for c in cc]);l,h=R(l),R(h)
    linear=fmpq_poly([fmpq(int(l.p),int(l.q)),fmpq(int((h-l).p),int((h-l).q))]);shift=fmpq_poly([0])
    for c in reversed(cc):shift=shift*linear+fmpq(int(c.p),int(c.q))
    n=len(cc)-1
    out=[]
    for k in range(n+1):out.append(sum((R(str(shift[j]))*R(comb(k,j),comb(n,j)) for j in range(k+1)),R(0)))
    return out

def minbern(p,l,h):return min(bernown(p,l,h))

def verify():
    c=json.loads(OUT.joinpath('certificate_td.json').read_text());assert c['status']=='PROVED'
    K=c['K'];m=c['degree'];D=R(c['D1']);shape=R(c['shape']);aa=list(map(R,c['a']))
    assert len(aa)==K and min(aa)>=0
    betas=[]
    for row,power in zip(c['beta_bernstein'],c['beta_power']):
        b=list(map(R,row));assert len(b)==m+1 and b[0]==0 and min(b)>=0 and all(b[i]<=b[i+1] for i in range(m))
        p=sp.Poly(sum(b[i]*comb(m,i)*u**i*(1-u)**(m-i) for i in range(m+1)),u,domain=sp.QQ)
        assert coeffs(p.as_expr())==list(map(R,power));betas.append(p)
    x=1-u*u;common=[R(0),2*x*x-1,x-u]
    # Independently reconstruct and prove every quoted long line by Sturm.
    zz=sp.Symbol('z');gram=json.load(open('.research/agents/tdense9_scratch/long_gram_bounds.json'))
    for r in gram:
        lam=list(map(R,r['lambda_coefficients']));assert min(lam)>=0
        P=sp.Poly(sp.chebyshevt(2,zz)-R(r['m'])*zz-R(r['b'])-sum(lam[n-3]*sp.chebyshevt(n,zz) for n in range(3,r['N']+1)),zz,domain=sp.QQ)
        assert P.count_roots(-1,1)==0 and P.eval(1)>0 and P.eval(-1)>0
        common.append(R(r['m'])*x+R(r['b']))
    support=json.load(open(OUT/'support_lines.json'));support_count=0
    def cheb(z,k):
        vals=[R(1),z]
        for i in range(2,k+1):vals.append(2*z*vals[-1]-vals[-2])
        return vals
    for kk,rows in support.items():
        k=int(kk)
        for r in rows:
            assert r['k']==k
            nodes=[(R(z),R(a)) for z,a in r['nodes']];assert all(-1<=z<=1 and a>=0 for z,a in nodes)
            v=[sum((2*a*cheb(z,k)[n] for z,a in nodes),R(0)) for n in range(k+1)]
            norm=v[2];err=sum((max(R(0),a) for a in v[3:]),R(0));assert norm>0
            assert R(r['m'])==-v[1]/norm and R(r['b'])==-(sum(a for z,a in nodes)+err)/norm
            assert R(r['normalization'])==norm and R(r['positive_moment_repair'])==err;support_count+=1
    count=0;capcount=0
    # Independent rational pi enclosure, from a different truncation count.
    def atan(z,N):
        s=sum(((-1)**j*z**(2*j+1)/R(2*j+1) for j in range(N)),R(0));r=(-1)**N*z**(2*N+1)/R(2*N+1)
        return min(s,s+r),max(s,s+r)
    a0,a1=atan(R(1,5),36);b0,b1=atan(R(1,239),36);piL,piH=16*a0-4*b1,16*a1-4*b0
    assert piL>3 and piH<R(22,7)
    for expected,cell in enumerate(c['pointwise']):
        jj=cell['jj'];assert jj==expected;j=jj//2;cap=R(cell['cap']);ulo=R(cell['u_lower'])
        k=(2*K+jj-1)//jj-1 if jj else None
        assert cell['support_k']==k
        branches=common+[R(r['m'])*x+R(r['b']) for r in support.get(str(k),[])]
        assert len(branches)==len(cell['branches'])
        for br,raw in zip(branches,cell['branches']):assert sp.expand(br)==sum(R(v)*u**i for i,v in enumerate(raw))
        assert ulo>=0 and ulo*ulo<=1-cap
        if jj:
            k=(2*K+jj-1)//jj-1;z=piL/R(k+2)
            # 10-term even truncation j=10, with pi lower; weaker but below the rounded cap.
            cosU=sum(((-1)**i*z**(2*i)/factorial(2*i) for i in range(11)),R(0))
            assert cap>=cosU;capcount+=1
        else:assert cap==1 and ulo==0
        left=ulo
        all_leaves=sorted(cell['leaves'],key=lambda a:R(a['lo']))
        cache={}
        for leaf in all_leaves:
            l,h=R(leaf['lo']),R(leaf['hi']);assert l==left and h>l;left=h
            branch=leaf['branch'];L=branches[branch]
            bb=bernown(L,l,h);assert min(bb)>=0 and max(bb)<=1
            if branch not in cache:
                A=sp.Poly(aa[j]*x-betas[j].as_expr().subs(u,x)/2-R(1,2),u,domain=sp.QQ)
                if jj<K:A+=sp.Poly(betas[jj].as_expr().subs(u,L),u,domain=sp.QQ)
                cache[branch]=A
            A=cache[branch]
            if leaf['mode']=='A':P=A
            else:
                P=sp.Poly(u*u*(2-u*u)/4,u,domain=sp.QQ)-A*A
                if leaf['endpoint_factor']:
                    P,rem=sp.div(P,sp.Poly(1-u,u,domain=sp.QQ));assert rem.is_zero
            vmin=min(bernown(P.as_expr(),l,h))
            if vmin<0:
                print('INDEPENDENT_REFINE',jj,branch,leaf['mode'],str(l),str(h),'degree',P.degree(),'bern',str(vmin),flush=True)
                todo=[(l,h,0)]
                while todo:
                    ll,hh,depth=todo.pop();vv=min(bernown(P.as_expr(),ll,hh))
                    if vv>=0:continue
                    assert depth<24 and P.eval((ll+hh)/2)>=0, (jj,branch,leaf['mode'],ll,hh,depth)
                    mid=(ll+hh)/2;todo.extend([(ll,mid,depth+1),(mid,hh,depth+1)])
            count+=1
        assert left==1
    assert len(c['pointwise'])==2*K
    print('INDEPENDENT_POINTWISE',count,'leaves;',capcount,'CF caps verified',flush=True)
    # Direct exact row integrals at four rational nodes in every t cell.
    U=lambda y:1+4*shape*y*(1-y)
    F=lambda y:y+2*shape*y*y-R(4,3)*shape*y**3
    clip=lambda z:min(R(1),max(R(0),z))
    rows=[];mins=[]
    for cell in range(K):
        pts=[]
        for i in range(4):
            s=R(8*cell+2*i+1,8*K);row=R(0)
            for j,a in enumerate(aa):
                lo,hi=R(j,K),R(j+1,K)
                row+=a*(F(clip(s-lo))-F(clip(s-hi))+F(clip(s+hi))-F(clip(s+lo)))
            pts.append((s,2*D*U(s)-row))
        P=sp.Poly(sp.interpolate(pts,u),u,domain=sp.QQ)
        minb=min(bernown(P.as_expr(),R(cell,K),R(cell+1,K)));assert minb>=0
        assert coeffs(P.as_expr())==list(map(R,c['schur'][cell]['polynomial']))
        assert minb==R(c['schur'][cell]['min_bernstein']);mins.append(minb)
    print('INDEPENDENT_SCHUR',K,'cells, minimum margin',min(mins),flush=True)
    assert D==R(259,2000) and 1/D>R(77,10)
    # Exact algebra behind sparse moment correction and binary tightness.
    p=sp.Symbol('p',real=True);e=p*(1-p);sk=e*(1-2*p)
    assert sp.expand(p**3+3*p*e+sk-p)==0
    a=sp.Symbol('a',real=True)
    assert sp.expand(a*a*(a-1)**2-(a**4-2*a**3+a*a))==0
    assert sp.expand(a*(a-1)**2-(a**3-2*a*a+a))==0
    files=sorted(OUT.glob('*.py'))+[OUT/'certificate_td.json']
    manifest={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in files}
    out=dict(status='PROVED',independent_method='SymPy QQ + FLINT composition; direct exact Schur integrals/interpolation; Sturm long lines; rational finite-symbol evaluations',pointwise_leaves=count,CF_caps=capcount,support_lines=support_count,schur_cells=K,min_schur=str(min(mins)),D1=str(D),C11=str(1/D),C11_float=float(1/D),binary_algebra_checked=True,python=platform.python_version(),sympy=sp.__version__,sha256=manifest,seconds=time.time()-start)
    OUT.joinpath('independent_verification.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='sha256'}),flush=True)
if __name__=='__main__':verify()
