"""Independent certificates, exact-enclosure exhaustive trade-offs, profile diagnostics and hashes."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json, math, hashlib, platform, ast
import numpy as np
from flint import arb,ctx
ctx.prec=220
ROOT=Path(__file__).resolve().parent

def exact_curve(q):
    h=(q-1)//2;m=(q-1)//4;scale=1<<100
    bounds={}
    for a in range(1,h+1):
        z=2*(2*arb.pi()*a/q).cos()*scale
        lo=z.lower().floor().unique_fmpz();hi=z.upper().ceil().unique_fmpz()
        assert lo is not None and hi is not None
        bounds[a]=(int(lo),int(hi))
    def mask(P):return sum(1<<(a-1) for a in P)
    def image(P,g):return tuple(sorted(min((g*a)%q,q-(g*a)%q) for a in P))
    def eigen(P,g):
        Qs=image(P,g)
        return (sum(bounds[a][0] for a in Qs),sum(bounds[a][1] for a in Qs))
    seen=set();orbits=[];cases=0
    for P in combinations(range(1,h+1),m):
        cases+=1
        if mask(P) in seen:continue
        seen.update(mask(image(P,g)) for g in range(1,h+1))
        eig=[eigen(P,g) for g in range(1,h+1)]
        k=(-min(x[1] for x in eig),-min(x[0] for x in eig))
        peak=(max(x[0] for x in eig),max(x[1] for x in eig))
        gg=max(range(1,h+1),key=lambda g:sum(eig[g-1]))
        orbits.append((k,peak,image(P,gg)))
    orbits.sort(key=lambda x:sum(x[0]));steps=[];prev=None;lastk=None
    for k,peak,P in orbits:
        if lastk is not None:assert lastk[1]<k[0],('unresolved threshold order',q)
        lastk=k
        if prev is None or peak[0]>prev[1]:
            steps.append(dict(K_integer_enclosure=list(k),Lambda_integer_enclosure=list(peak),
                              K_mid=sum(k)/(2*scale),Lambda_mid=sum(peak)/(2*scale),pairs=list(P)))
            prev=peak
        else:assert peak[1]<prev[0],('unresolved peak comparison',q)
    assert len(seen)==cases
    return dict(q=q,candidates=cases,orbits=len(orbits),denominator=scale,steps=steps,
        status='PROVED exhaustive enumeration with integer enclosures of Arb cosine coefficients; exact threshold values defined by stored pairs')

def cyclic():
    import cyclic_probe
    ctx.prec=220
    out=[]
    for row in json.loads((ROOT/'cyclic_tradeoffs.json').read_text()):
        if not row.get('pairs'):continue
        q=row['q'];P=row['pairs'];cert=cyclic_probe.balls(q,P)
        assert cert['K_interval'][1]<row['kappa']
        assert abs(cert['Lambda_interval'][0]-row['objective'])<1e-8
        b=np.zeros(q,dtype=np.int64);b[P]=1;b[[-a for a in P]]=1
        assert int(b.sum())==(q-1)//2 and b[0]==0 and np.array_equal(b,b[np.arange(q)*-1%q])
        row['certificate']=cert;out.append(dict(q=q,factor=row['factor'],certificate=cert))
    rows=json.loads((ROOT/'cyclic_tradeoffs.json').read_text())
    for r,a in zip(rows,out):r['certificate']=a['certificate']
    (ROOT/'cyclic_tradeoffs.json').write_text(json.dumps(rows,indent=2))
    profiles=json.loads((ROOT/'cyclic_profiles.json').read_text())
    for r in profiles:
        if r['q']<=1021:r['certificate']=cyclic_probe.balls(r['q'],r['pairs'])
    (ROOT/'cyclic_profiles.json').write_text(json.dumps(profiles,indent=2))
    return out

def binary():
    from binary_probe import profile
    ctx.prec=220
    out=[]
    for line in (ROOT/'binary_results.jsonl').read_text().splitlines():
        row=json.loads(line);X=row['X'];family=row['family']
        A=np.load(ROOT/(family+'_X'+str(X)+'.npz'))['A'];n=len(A)
        assert n==row['n'] and len(np.unique(A))==n and A.min()>=1 and A.max()<=X
        p,w=profile(X);bits=np.zeros(X);bits[A-1]=1;B=row['block']
        maxdisc=max(abs(bits[:i].sum()-p[:i].sum()) for i in range(B,X+1,B))
        assert maxdisc<=.5000001,(family,X,maxdisc)
        num=row['phase_num'];den=row['phase_den']
        # Group equal residues, then use an independent cosine-recurrence evaluation.
        v=arb(0);x=2*arb.pi()*num/den
        for a in A:v+=(int(a)*x).cos()
        saved=arb(row['point_ball']);assert v.overlaps(saved)
        rball=-v/arb(n).sqrt()
        assert (rball-arb(3)/5).lower()>0
        low=float(rball.lower())
        phase=num/den
        main=float(np.dot(p,np.cos(2*np.pi*np.arange(1,X+1)*phase)))
        # A fixed block comb is a concrete diagnostic for rational atoms.
        comb=[]
        for j in (1,2):
            counts=np.bincount(A%B,minlength=B);val=arb(0)
            for c,count in enumerate(counts):val+=int(count)*(2*arb.pi()*j*c/B).cos()
            comb.append(dict(numerator=j,denominator=B,ball=str(val),value_over_X=float(val.mid())/X))
        err=bits-p
        second=float(np.dot(err,err)/X);expected=float(np.dot(p,1-p)/X)
        third=float(np.mean(err**3));third_expected=float(np.mean(p*(1-p)*(1-2*p)))
        diagnostic=dict(family=family,X=X,n=n,actual_max=int(A.max()),point_ball_220=str(v),
             R_point_lower_float=float(np.nextafter(low,-np.inf)),R_point_ball=str(rball),
             M_over_sqrtX_point_ball=str(-v/arb(X).sqrt()),profile_prefix_discrepancy=maxdisc,
             smooth_value_at_dip=main,residual_value_at_dip=float(v.mid())-main,
             second_binary=second,second_profile=expected,third_binary=third,third_profile=third_expected,
             q=row.get('q'),distance_to_q_root=(abs(phase*row['q']-round(phase*row['q'])) if 'q' in row else None),
             nearest_block_harmonic=round(phase*B),block_offset_scaled_by_X=X*(phase-round(phase*B)/B),
             block_comb=comb)
        out.append(diagnostic)
    return out

def moments():
    # Nonnegative shifted power moments are automatic, while the R12 fake's cubic is irrational.
    import sympy as s
    q,m,u=s.symbols('q m u');a=q-1
    T=a*(u-1);E=a*(u*u-2*u+q+1)
    cubic=-2*T**3/m**2+3*T*E/m-3*u*E+3*T*u*u-a*u**3
    rem=s.rem(s.expand(cubic),u**3-q,u)
    assert s.simplify(rem.coeff(u,2)-3*a*(m-a)*(m-2*a)/m**2)==0
    tests=[]
    for prime in (int(s.nextprime(x)) for x in (1000000,8000000,64000000)):
        rr=arb(prime);uu=(rr.log()/3).exp();tt=(prime-1)*(uu-1)
        ee=rr*rr+rr*uu*(uu-2)-(uu-1)**2
        mm=4*math.ceil(float((tt*tt/(4*ee)).mid()))
        assert mm<prime-1
        tests.append(dict(q=prime,support_count=mm,cubic_u2_coefficient=str(3*Q(prime-1)*(mm-prime+1)*(mm-2*(prime-1))/mm**2)))
    vandermonde=[]
    for r in range(3,11):
        xs=[s.Rational(2)+s.Rational(j+1,r+1) for j in range(r)]
        jac=s.Matrix([[2*k*x**(k-1) for x in xs] for k in range(1,r+1)])
        det=s.factor(jac.det());expected=2**r*s.factorial(r)
        for i in range(r):
            for j in range(i+1,r):expected*=xs[j]-xs[i]
        assert det==expected and det!=0
        vandermonde.append(dict(order=r,points=[str(x) for x in xs],determinant=str(det)))
    return dict(first_failed_integrality_order=3,u2_coefficient=str(s.factor(rem.coeff(u,2))),tests=tests,
                finite_order_repair_jacobians=vandermonde)

def main():
    result=dict(python=platform.python_version(),arb_bits=ctx.prec)
    for key,fn in [('exact_curves',lambda:[exact_curve(q) for q in (17,37)]),
                   ('cyclic_certificates',cyclic),('binary_diagnostics',binary),('moments',moments)]:
        result[key]=fn()
        (ROOT/'audit_results.json').write_text(json.dumps(result,indent=2))
    for r in result['exact_curves']:print('EXACT_CURVE',json.dumps(r),flush=True)
    for r in result['binary_diagnostics']:print('DIAGNOSTIC',json.dumps(r),flush=True)
    print('MOMENTS',json.dumps(result['moments']),flush=True)
    for p in ROOT.glob('*.py'):ast.parse(p.read_text())
    manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.iterdir()
              if p.is_file() and p.name!='manifest.json' and p.suffix not in ('.so','.log')}
    (ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2))

if __name__=='__main__':main()
