"""VM-only exact support counts and Arb checks for the round-16 fake.
No dense q-array, no optimization. The infinite-family proof is in the report.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction
import json, platform
import sympy as sp
from flint import arb, ctx
ctx.prec=200
ROOT=Path(__file__).resolve().parent

def run(q,m,t):
    assert sp.isprime(q) and q%4==1
    t=arb(t); C=arb(q)*(t*t-arb(1)/4); V=arb(q*q)/4+C
    s=2*m; ell=16*s; B=100*m; L=(C/(4*s)).sqrt()
    D=list(range(10*m+1,11*m+1));D=D+[-x for x in D]
    r=Counter(x+y for x in D for y in D)
    S=sorted(x for x in r if x>0)
    values={'t':t,'L':L};sites={0:'t'}
    for x in D:sites[x]='L'
    j=1
    for d in S:
        label='a'+str(d);values[label]=((C-r[d]*L*L)/(2*ell)).sqrt()
        assert values[label]>0 and values[label]<L/2
        for _ in range(ell):
            for x in (B*j,B*j+d,-B*j,-B*j-d):
                assert x not in sites;sites[x]=label
            j+=1
    M=sum((values[v] for v in sites.values()),arb(0))
    Q=sum((values[v]**2 for v in sites.values()),arb(0))
    T=q*t-M; E=V-Q
    assert T>0 and E>0
    z=3*T*T/(8*E)
    k=int(float(z.mid()))+1
    assert arb(k-1)<z and z<k
    n=4*k; mu=T/n; var=E/n-mu*mu
    assert var>=0 and var<mu*mu
    values['hi']=mu+var.sqrt();values['lo']=mu-var.sqrt()
    assert values['lo']>0 and values['hi']<L/2
    # Positive repair sites B*j, then reflection, in two constant-level runs.
    runs=[(j,j+n//4-1,'hi'),(j+n//4,j+n//2-1,'lo')]
    runs+= [(-b,-a,v) for a,b,v in runs]
    last=B*(j+n//2)
    assert last+B<q//2 and max(abs(x) for x in sites)<B*j
    def lookup(x):
        # Every queried point stays away from cyclic wraparound in these checks.
        if x in sites:return sites[x]
        if x%B:return None
        k=x//B
        for a,b,v in runs:
            if a<=k<=b:return v
        return None
    def counts(d):
        out=Counter()
        def add(v,w,num=1):out[tuple(sorted((v,w)))]+=num
        for x,v in sites.items():
            y=x-d;w=lookup(y)
            if w is not None:add(v,w)
            # The reverse partition: repair x and explicit y.
            y=x+d;w=lookup(y)
            if w is not None and y not in sites:add(v,w)
        if d%B==0:
            k=d//B
            for a,b,v in runs:
                for c,e,w in runs:
                    num=max(0,min(b,e+k)-max(a,c+k)+1)
                    if num:add(v,w,num)
        return out
    def evaluate(cc):return sum((num*values[v]*values[w] for (v,w),num in cc.items()),arb(0))
    checks=[]
    for d in S:
        cc=counts(d)
        # Independent expected support polynomial, not just a floating residual.
        assert cc==Counter({('L','L'):r[d],('a'+str(d),'a'+str(d)):2*ell}),(d,cc)
        residual=evaluate(cc)-C
        assert residual.contains(0)
        checks.append({'d':d,'r_D':r[d],'counts':{str(k):v for k,v in cc.items()},'residual_ball':str(residual)})
    zero=evaluate(counts(0))-V;assert zero.contains(0)
    mass=M+n*mu-q*t;assert mass.contains(0)
    omitted=evaluate(counts(B));repair_lower=E-2*(values['hi']**2+values['lo']**2-values['hi']*values['lo'])
    assert omitted>=repair_lower-arb('1e-30') and omitted>C
    # A deterministic Boolean plateau failure at physical x=1.
    # Entire support lies in |a|<last<q/2. Pair cosines use all explicit sites,
    # while repair APs are evaluated by a geometric sum independently.
    zeta=2*arb.pi()/q
    inv=sum((values[v]*(zeta*x).cos() for x,v in sites.items()),arb(0))
    for a,b,v in runs:
        count=b-a+1
        co=(zeta*B*(a+b)/2).cos()*(zeta*B*count/2).sin()/(zeta*B/2).sin()
        inv+=values[v]*co
    inv/=q
    out={'status':'PROVED_FINITE_SUPPORT_COUNTS_AND_ARB','q':q,'m':m,'s':s,'t':str(t),'L':str(L),'C0':str(C),
         'sumset_offzero_size':2*len(S),'support_size':len(sites)+n,'repair_sites':n,'spacing_B':B,
         'last_support_bound':last,'mass_residual':str(mass),'energy_residual':str(zero),
         'core_energy_fraction':str(s*L*L/V),'bulk_peak_over_L':str(values['hi']/L),
         'core_sum_checks':checks,'omitted_B_convolution_over_C0':str(omitted/C),
         'omitted_B_convolution_over_q2':str(omitted/(q*q)),'inverse_at_1':str(inv),
         'inverse_at_1_plateau_square_defect':str(inv*inv-arb(1)/4)}
    print(q,m,'s',s,'S',2*len(S),'support',len(sites)+n,'omitted/C0',out['omitted_B_convolution_over_C0'],flush=True)
    return out

qs=[]
for base,m in [(10**9,1),(10**10,2),(10**11,4)]:
    q=int(sp.nextprime(base))
    while q%4!=1:q=int(sp.nextprime(q))
    u=sp.integer_nthroot(q,4)[0]
    qs.append(run(q,m,2*(int(u)+1)))
ROOT.joinpath('adaptive_fake.json').write_text(json.dumps({'python':platform.python_version(),'sympy':sp.__version__,'bits':ctx.prec,'records':qs},indent=2))
