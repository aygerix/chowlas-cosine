"""Round-3 probes. Execute ONLY through DIRICHLET_IP=... src/dirun.sh -c 2.

All minima/integrals here are NUMERICAL. No LP/MILP is used.
Exact input sets are retained in sets.json; JSON summaries omit large arrays.
"""
import json
import math
import platform
import sys
from pathlib import Path
import numpy as np
from scipy.optimize import minimize_scalar

ROOT = Path('.research/agents/tdense3_scratch')
sys.path.insert(0, 'src')
from singer import singer


def metrics(A, over=64):
    A = sorted(set(map(int, A)))
    n, X = len(A), max(A)
    G = 1 << math.ceil(math.log2(over*X))
    c = np.zeros(G)
    c[A] = 1
    f = np.fft.rfft(c).real
    w = np.ones(len(f)); w[0] = w[-1] = .5
    mean = lambda v: float(w@v/(len(v)-1))
    # Independent direct-cosine refinement of the lowest FFT grid points.
    aa = np.asarray(A, dtype=float)
    j = int(f.argmin())
    lo, hi = max(0, 2*math.pi*(j-2)/G), min(math.pi, 2*math.pi*(j+2)/G)
    obj = lambda x: float(np.cos(aa*x).sum())
    z = minimize_scalar(obj, bounds=(lo, hi), method='bounded', options={'xatol': 1e-15})
    candidates = [(float(f[j]), 2*math.pi*j/G), (float(z.fun), float(z.x)), (obj(math.pi), math.pi)]
    fm, xm = min(candidates)
    row = dict(n=n, X=X, C=X/n, G=G, R_grid=-float(f.min())/math.sqrt(n),
               R_refined=-fm/math.sqrt(n), x_refined=xm,
               parseval_error=mean(f*f)/(n/2)-1,
               direct_fft_error=abs(obj(2*math.pi*j/G)-float(f[j])),
               negative_energy_fraction=mean(f*f*(f<0))/(n/2))
    for K in (1, 2, 3):
        row[f'beta{K}'] = mean(f*f*(f<=K*math.sqrt(n)))/(n/2)
    # Common Fejer-bump deconvolution, order 2X. This is a diagnostic,
    # not a universal lower-bound conjecture.
    c[:] = 0
    av = np.asarray(A, dtype=int)
    c[av] = 1/(1-av/(2*X))
    g = np.fft.rfft(c).real
    row['fejer_2X_deconvolved_R_grid'] = -float(g.min())/math.sqrt(n)
    return row


def cumround(p, sigma=.37):
    p = np.asarray(p, dtype=float)
    u = np.floor(sigma+np.cumsum(p))
    a = np.diff(np.r_[0., u])
    assert np.all((a==0)|(a==1))
    return (np.flatnonzero(a)+1).tolist(), a-p


def zoo():
    rng = np.random.default_rng(2026101903)
    sets = {}
    for n in (256, 1024, 4096):
        sets[f'interval_{n}'] = list(range(1,n+1))
        sets[f'random_dense_{n}'] = sorted(rng.choice(np.arange(1,3*n+1),n,replace=False).tolist())
        sets[f'random_sparse_{n}'] = sorted(rng.choice(np.arange(1,50*n+1),n,replace=False).tolist())
        t = np.arange(1,6*n+1)/(6*n)
        sets[f'curved_quadratic_{n}'] = cumround(.5*(1-t)**2)[0]
        t = np.arange(1,2*n+1)/(2*n)
        sets[f'curved_linear_{n}'] = cumround(1-t)[0]
        sets[f'multidilate_{n}'] = sorted({p*j for p in (11,13,17,19,23,29,31,37) for j in range(1,n//8+1)})
    for q in (7, 11, 13, 17, 23, 31):
        S0, _ = singer(q)
        shift = -max(S0)//2
        S = [s+shift for s in S0]
        D = {3*(b-a) for a in S for b in S if b>a}
        E = {abs(3*(a+b)+1) for i,a in enumerate(S) for b in S[i+1:]}
        sets[f'Bu_Singer_q{q}'] = sorted(D|E)
    # The actual optimized-shift representatives used by E67, in addition to
    # the centered representatives above. bu() does not write any files.
    from e67_zoo import bu
    for q in (7, 11, 13, 17, 23, 31):
        sets[f'E67_optimized_Bu_q{q}'] = bu(q)[0]
    for path in (Path('examples/smallN_best.json'), Path('examples/construct/N50_certified.json')):
        d = json.loads(path.read_text())
        for key, row in d.items():
            if isinstance(row,dict) and isinstance(row.get('A'),list):
                sets[f'{path.stem}_{key}'] = row['A']
    for X in (4096, 16384, 65536, 200000):
        path = Path(f'.research/agents/tdense2_scratch/fejer_X{X}.json')
        if path.exists(): sets[f'P42_fejer_X{X}'] = json.loads(path.read_text())['A']
    paths = sorted(Path('examples/e68').glob('*.jsonl')) if Path('examples/e68').exists() else []
    for path in paths:
        for i, line in enumerate(path.read_text().splitlines()):
            try: row = json.loads(line)
            except json.JSONDecodeError: continue
            if isinstance(row.get('A'),list): sets[f'E68_{path.stem}_{i}'] = row['A']
    rows = []
    for name, A in sets.items():
        row = dict(name=name, **metrics(A))
        print(json.dumps(row),flush=True); rows.append(row)
    (ROOT/'sets.json').write_text(json.dumps(sets))
    (ROOT/'zoo.json').write_text(json.dumps(dict(status='NUMERICAL, not interval certified',
        python=platform.python_version(),numpy=np.__version__,
        E68_files=[str(x) for x in paths],rows=rows),indent=2))


def extensions():
    from fractions import Fraction as F
    rows, sets = [], {}
    for X in (4096,16384,65536):
        t = np.arange(1,X+1)/X
        curve = (t>.25)&(t<=.75)
        for label, alpha, spec in [('rational_2_5',.4,(2,0,5,0)),
                                  ('irrational_golden',(math.sqrt(5)-1)/2,(-1,1,2,5)),
                                  ('near_rational',.4+math.sqrt(2)*1e-7,(4000000,1,10000000,2))]:
            p = np.where(t<=.25,alpha,np.where(t<=.75,alpha*(1.5-2*t),0.))
            for sigma in (0.,.37,.999):
                # Exact Q(sqrt(d)) floors. All X here are divisible by four.
                sig=F(str(sigma)); an,bn,ad,rad=spec; left=X//4
                den=2*X*ad*sig.denominator
                old=0; A=[]; av=np.zeros(X)
                for mm in range(1,X+1):
                    j=min(mm,3*X//4)
                    Bnum=2*X*j if j<=left else 2*X*left+3*X*(j-left)-2*(j*(j+1)-left*(left+1))
                    u=Bnum*an*sig.denominator+sig.numerator*2*X*ad
                    v=Bnum*bn*sig.denominator
                    new=(u+math.isqrt(rad*v*v))//den
                    assert new-old in (0,1)
                    if new>old: A.append(mm); av[mm-1]=1
                    old=new
                beta=av-p
                expected = float(np.sum(p[curve]*(1-p[curve])))
                row = dict(name=f'flatcurve_{label}_{X}_{sigma}',X_ambient=X,sigma=sigma,
                    rounding_status='Exact integer and quadratic-field floors; p values in energy diagnostics floating',
                    alpha=alpha,curved_rounding_energy=float(np.sum(beta[curve]**2)),
                    expected_curved_energy=expected,
                    energy_difference=float(np.sum(beta[curve]**2))-expected,**metrics(A))
                print(json.dumps(row),flush=True); rows.append(row); sets[row['name']]=A
        alpha = (math.sqrt(5)-1)/2
        theta = 2*math.pi*alpha*np.arange(1,X+1)
        for label,p in [('bohr_1mode',.5*(1-t)*(1+.30*np.cos(theta))),
                        ('bohr_2mode',.5*(1-t)*(1+.20*np.cos(theta)+.10*np.cos(2*theta)))]:
            for sigma in (0.,.37,.999):
                A,beta=cumround(p,sigma)
                expected=float(np.sum(p*(1-p)))
                row=dict(name=f'{label}_{X}_{sigma}',X_ambient=X,sigma=sigma,
                    rounding_status='Floating cumulative floors, not certified membership in the analytic profile family',
                    rounding_energy=float(beta@beta),expected_rounding_energy=expected,
                    energy_error_over_X=(float(beta@beta)-expected)/X,**metrics(A))
                print(json.dumps(row),flush=True); rows.append(row); sets[row['name']]=A
    (ROOT/'extension_sets.json').write_text(json.dumps(sets))
    (ROOT/'extensions.json').write_text(json.dumps(dict(status='NUMERICAL, not a proof',rows=rows),indent=2))


def checks():
    from fractions import Fraction as F
    # Exact Fourier dictionaries for the nonmonotone positive bump.
    for L in range(2,65):
        tri={k:F(L-abs(k),L) for k in range(-L+1,L)}
        coeff={}
        for k,v in tri.items():
            for j,b in [(0,F(1)),(2*L,F(1,2)),(-2*L,F(1,2))]:
                coeff[k+j]=coeff.get(k+j,F(0))+v*b
        assert coeff[0]==1 and coeff.get(L,0)==0 and coeff[2*L]==F(1,2)
    rational=[]
    for q in range(2,25):
        for r in range(1,q):
            if math.gcd(r,q)>1: continue
            expected=abs(math.sin(math.pi*r/q))/(q*math.sin(math.pi/q))
            errors=[]
            for v in (0,1,7,15):
                sigma=F(v,16)
                word=[math.floor(sigma+F(r*m,q))-math.floor(sigma+F(r*(m-1),q)) for m in range(1,2*q+1)]
                assert word[:q]==word[q:] and sum(word[:q])==r
                c=sum(word[m-1]*np.exp(2j*math.pi*r*m/q) for m in range(1,q+1))/q
                errors.append(abs(abs(c)-expected))
            rational.append(max(errors))
    # First-order cohomological expansion for a finite-mode affine profile.
    cohom=[]
    alpha=(math.sqrt(5)-1)/2
    for X in (1024,4096,16384):
        m=np.arange(1,X+1); t=m/X
        p=.5*(1-t)*(1+.3*np.cos(2*math.pi*alpha*m))
        Phi=np.cumsum(p); Phi0=.5*m-.25*m*(m+1)/X
        Om=lambda tt,mm: 2*np.real(.075*(1-tt)*np.exp(2j*math.pi*alpha*mm)/(1-np.exp(-2j*math.pi*alpha)))
        rem=Phi-Phi0-Om(t,m)+Om(0,0)
        cohom.append(dict(X=X,max_error=float(abs(rem).max()),X_times_error=float(abs(rem).max())*X))
    out=dict(exact_bump_checks=63,rational_period_checks=len(rational)*4,
        rational_DFT_max_error=max(rational),cohomology=cohom,
        status='Exact rational periodicity and Fourier dictionaries; floating DFT/cohomology diagnostics')
    (ROOT/'checks.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out),flush=True)


def summarize():
    zoo=json.loads((ROOT/'zoo.json').read_text())['rows']
    ext=json.loads((ROOT/'extensions.json').read_text())['rows']
    keys=['name','n','X','R_refined','beta1','beta2','negative_energy_fraction']
    selected=[r for r in zoo if r['name'] in ['interval_4096','curved_quadratic_4096','P42_fejer_X200000',
        'N50_certified_N50_x72','E67_optimized_Bu_q31']]
    e68=[r for r in zoo if r['name'].startswith('E68')]
    if e68:
        for key in ['R_refined','beta1','beta2']: selected.append(min(e68,key=lambda r:r[key]))
    out=dict(zoo_count=len(zoo),extension_count=len(ext),E68_count=len(e68),
        selected=[{k:r[k] for k in keys} for r in selected],
        extension_R_range=[min(r['R_refined'] for r in ext),max(r['R_refined'] for r in ext)],
        bohr_R_range=[min(r['R_refined'] for r in ext if r['name'].startswith('bohr')),
                      max(r['R_refined'] for r in ext if r['name'].startswith('bohr'))],
        max_parseval_error=max(abs(r['parseval_error']) for r in zoo+ext),
        max_direct_fft_error=max(r['direct_fft_error'] for r in zoo+ext),
        beta_below_013_and_R_below_060=[r['name'] for r in zoo if r['beta1']<.13 and r['R_refined']<.6],
        max_flat_energy_difference=max(abs(r['energy_difference']) for r in ext if r['name'].startswith('flatcurve')),
        max_bohr_energy_error_over_X=max(abs(r['energy_error_over_X']) for r in ext if r['name'].startswith('bohr')))
    (ROOT/'summary.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out),flush=True)


def final_audit():
    zoo()
    checks()
    summarize()


def verify():
    import re
    checks()
    summarize()
    report=Path('.research/agents/tdense3_report.md').read_text()
    match=re.search(r'A = \{([^}]+)\}',report,re.S)
    exact=[int(v) for v in re.findall(r'\d+',match.group(1))]
    saved=json.loads((ROOT/'sets.json').read_text())['E68_e68_14']
    assert exact==saved and len(exact)==64 and max(exact)==91
    print('Exact E68 set copied in report verified against saved snapshot.',flush=True)


def certify_bohr():
    """Ball-arithmetic certification of every tested Bohr floor decision."""
    from flint import arb,ctx
    ctx.prec=192
    alpha=(arb(5).sqrt()-1)/2
    twopi=2*arb.pi()
    sigmas=[('0.0',arb(0)),('0.37',arb(37)/100),('0.999',arb(999)/1000)]
    saved=json.loads((ROOT/'extension_sets.json').read_text())
    doc=json.loads((ROOT/'extensions.json').read_text())
    rows={r['name']:r for r in doc['rows']}
    results=[]
    for X in (4096,16384,65536):
        Phis=[arb(0),arb(0)]
        old=[[0]*3 for _ in range(2)]
        sets=[[[] for _ in range(3)] for _ in range(2)]
        for m in range(1,X+1):
            angle=twopi*alpha*m
            co=angle.cos(); co2=(2*angle).cos()
            base=arb(X-m)/(2*X)
            ps=[base*(1+arb(3)/10*co),base*(1+arb(1)/5*co+arb(1)/10*co2)]
            for kind in range(2):
                Phis[kind]+=ps[kind]
                for j,(_,sig) in enumerate(sigmas):
                    value=(Phis[kind]+sig).floor().unique_fmpz()
                    if value is None: raise RuntimeError(f'Floor undetermined at X={X},m={m},kind={kind},sigma={j}')
                    value=int(value)
                    assert value-old[kind][j] in (0,1)
                    if value>old[kind][j]: sets[kind][j].append(m)
                    old[kind][j]=value
        for kind in range(2):
            for j,(sig,_) in enumerate(sigmas):
                name=f'bohr_{kind+1}mode_{X}_{sig}'
                assert sets[kind][j]==saved[name],f'Floating and certified sets differ for {name}'
                rows[name]['rounding_status']='All floor decisions certified by Arb ball arithmetic at 192 bits'
                results.append(dict(name=name,n=len(sets[kind][j]),certified_floor_decisions=X))
        print(f'Arb certified all six Bohr roundings at X={X}.',flush=True)
    (ROOT/'extensions.json').write_text(json.dumps(doc,indent=2))
    out=dict(status='PROVED finite membership using Arb enclosures; minima and energies still NUMERICAL',
             precision_bits=192,rows=results,total_floor_decisions=sum(r['certified_floor_decisions'] for r in results))
    (ROOT/'bohr_membership_certificate.json').write_text(json.dumps(out,indent=2))


if __name__=='__main__':
    ROOT.mkdir(parents=True,exist_ok=True)
    globals()[sys.argv[1]]()
