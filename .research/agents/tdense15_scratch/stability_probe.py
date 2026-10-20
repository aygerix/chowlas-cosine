"""Round 15 adversarial stability measurements; VM only, no optimizer.

Integer pair lists specify the sets exactly. Floating measurements are NUMERICAL.
Arb balls independently enclose spectra of the selected small-q sets only.
Exhaustive floating enumeration is used only to select candidates, not as a proof.
"""
from pathlib import Path
from itertools import combinations
import json, math, re, platform
import numpy as np
from flint import arb, ctx

ROOT=Path(__file__).resolve().parent
ctx.prec=180

def metrics(b, name, pairs=None, enclose=False, boolean=True):
    q=len(b); alpha=float(np.mean(b)); F=np.fft.fft(b).real
    v=F.copy();v[0]=0
    K=float(-min(v[1:]));Lam=float(max(v[1:]));a=int(np.argmax(v[1:])+1)
    P=np.maximum(v,0);N=np.maximum(-v,0)
    pi=np.fft.ifft(P).real;ni=np.fft.ifft(N).real
    S=float(sum(P));C=q*K*(K-1);L=Lam+K;t=K-.5
    h=v+K;h[0]=t
    conv=np.fft.ifft(np.fft.fft(h)**2).real
    E=float(np.sum((Lam-v[1:])*(v[1:]+K)))
    core=(h>=L/2);core[0]=False
    r=dict(status='NUMERICAL',name=name,q=q,density=alpha,
           is_exact_halfset=bool(boolean and b[0]==0 and 2*sum(b)==q-1),
           K=K,Lambda=Lam,K_over_qquarter=K/q**.25,
           LambdaK_over_q=Lam*K/q,positive_count=int(sum(P>1e-8)),
           positive_effective_support=S*S/float(sum(P*P)),
           positive_core_count=int(sum(core)),predicted_4K2=4*K*K,
           negative_10pct_fraction=float(np.mean(N[1:]>=.9*K)),
           negative_saturation=float(sum(N)/(K*(q-1))),
           negative_zero_spike_fraction=float(ni[0]**2/sum(ni*ni)),
           positive_flat_rms=float(np.sqrt(np.mean((pi[1:]-(b[1:]-.5))**2))),
           positive_square_flat_rms=float(np.sqrt(np.mean((pi[1:]**2-.25)**2))),
           second_order_peak_ratio=L*L/C if C>0 else None,
           local_defect=1-L*L/C if C>0 else None,
           endpoint_defect=E,endpoint_defect_over_q2=E/q**2,
           boolean_square_error=float(np.max(np.abs((2*b-1)**2-1))),
           pairs=pairs)
    if r['is_exact_halfset']:
        target=np.full(q,C);target[0]+=q*q/4
        err=float(max(abs(conv-target))/max(1,C))
        assert err<1e-8,(name,err)
        assert L*L<=C*(1+1e-8)
        assert E>=-1e-6*q*q
        z=L*core
        assert sum((h-z)**2)<=E+t*t+1e-7*q*q
        assert abs(sum(h)-q*t)<1e-7*q*max(1,K)
        r['shifted_convolution_relative_error']=err
        r['peak_equation_residual']=(C-L*L-2*t*h[(2*a)%q])
        r['endpoint_defect_formula_error']=E-(q-1)*(Lam*(K-.5)+K/2-(q+1)/4)
        r['rounding_L2_bound']=E+t*t
        r['rounding_L2_actual']=float(sum((h-z)**2))
    if enclose:
        vals=[]
        for g in range(1,(q+1)//2):
            vals.append(sum((2*(2*arb.pi()*((g*x)%q)/q).cos() for x in pairs),arb(0)))
        imin=min(range(len(vals)),key=lambda i:float(vals[i].mid()))
        imax=max(range(len(vals)),key=lambda i:float(vals[i].mid()))
        r['Arb_K_ball']=str(-vals[imin]);r['Arb_Lambda_ball']=str(vals[imax]);r['Arb_bits']=ctx.prec
        assert abs(K-float((-vals[imin]).mid()))<1e-10
        assert abs(Lam-float(vals[imax].mid()))<1e-10
    return r

def array(q,pairs):
    b=np.zeros(q);b[pairs]=1;b[[q-x for x in pairs]]=1
    return b

out=[]
for q in (5,13,17,29,37):
    h=(q-1)//2;m=(q-1)//4
    A=2*np.cos(2*np.pi*np.outer(np.arange(1,h+1),np.arange(1,h+1))/q)
    best=math.inf;bp=None;tested=0
    for pp in combinations(range(1,h+1),m):
        k=-min(A[:,np.array(pp)-1].sum(axis=1));tested+=1
        if k<best:best=k;bp=list(pp)
    r=metrics(array(q,bp),'small_enumeration_candidate',bp,True)
    r['enumerated_sets']=tested;out.append(r)

stored={}
for fn in Path('examples/zp_half').glob('*.txt'):
    for line in fn.read_text().splitlines():
        mm=re.search(r'p=(\d+).*?P=([\d ]+)',line)
        if not mm:continue
        q=int(mm[1]);pp=list(map(int,mm[2].split()))
        if q%4==1 and q in (41,53,61,73,89,97,101) and len(pp)==(q-1)//4:
            stored[q]=pp
for q,pp in sorted(stored.items()):out.append(metrics(array(q,pp),'E41_stored',pp,True))

stored={}
for line in Path('examples/e90/prod.txt').read_text().splitlines():
    mm=re.search(r'q=(\d+).*?bestK=([\d.]+).*?P=([\d ]+)',line)
    if not mm:continue
    q=int(mm[1]);k=float(mm[2]);pp=list(map(int,mm[3].split()))
    if q in (149,401,601,1201,1601) and q%4==1 and len(pp)==(q-1)//4:
        if q not in stored or k<stored[q][0]:stored[q]=(k,pp)
for q,(k,pp) in sorted(stored.items()):out.append(metrics(array(q,pp),'E90_stored_candidate',pp))

for q in (257,4093,65537):
    pp=sorted({(a*a)%q for a in range(1,q) if (a*a)%q<=q//2})
    out.append(metrics(array(q,pp),'Paley',pp))

rng=np.random.default_rng(151019)
def repair(b):
    q=len(b);m=(q-1)//4;pp=np.flatnonzero(b[1:(q+1)//2]>.5)+1
    if len(pp)>m:
        remove=rng.choice(pp,len(pp)-m,replace=False);b[remove]=0;b[q-remove]=0
    elif len(pp)<m:
        avail=np.flatnonzero(b[1:(q+1)//2]<.5)+1
        add=rng.choice(avail,m-len(pp),replace=False);b[add]=1;b[q-add]=1
    return b
for q in (4093,65537):
    x=np.arange(1,(q+1)//2)
    pp=x[rng.random(len(x))<.5+.2*np.cos(2*np.pi*x/q)]
    out.append(metrics(repair(array(q,pp.tolist())),'R13_PK_random_profile'))
    alpha=1-1/math.sqrt(2)
    pp=x[rng.random(len(x))<alpha+.1*np.cos(2*np.pi*x/q)]
    base=array(q,pp.tolist());union=np.maximum(base,base[(3*np.arange(q))%q])
    out.append(metrics(repair(union),'R14_UNION_repaired_halfset'))

# Non-Boolean R12-S fake, with its exact defining scalar formulas.
q=1000033;u=q**(1/3);h0=u-1
T=q*(u-1);Energy=q*q+q*u*(u-2)
Tp=T-h0;Ep=Energy-h0*h0
m=4*math.ceil(Tp*Tp/(4*Ep));mean=Tp/m;var=Ep/m-mean*mean
fake=np.zeros(q);fake[0]=h0
for j in range(m//2):
    a=j+1;fake[a]=fake[q-a]=mean+(1 if j<m//4 else -1)*math.sqrt(var)
sign=np.fft.ifft(fake-u).real
b=(sign+1)/2
r=metrics(b,'R12_S_nonboolean',boolean=False)
r['raw_scalar_mass_error']=float(sum(fake)-T)
r['raw_scalar_energy_relative_error']=float((sum(fake*fake)-Energy)/Energy)
out.append(r)

result=dict(status='NUMERICAL',python=platform.python_version(),numpy=np.__version__,seed=151019,records=out)
ROOT.joinpath('stability_probe.json').write_text(json.dumps(result,indent=2))
for r in out:
    print(r['name'],r['q'],'K',round(r['K'],6),'Lambda',round(r['Lambda'],6),
          'Pi',r['positive_count'],'N90',round(r['negative_10pct_fraction'],4),
          'flat',round(r['positive_flat_rms'],6),'peak_ratio',r['second_order_peak_ratio'],flush=True)
