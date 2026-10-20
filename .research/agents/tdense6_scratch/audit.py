"""Round 6. Execute only on dirichlet with dirun.sh -c 2.

All writes stay in this directory. Floating results are NUMERICAL.
LPs use gurobipy, Threads=2. No numerical minimum is a certificate.
"""
from pathlib import Path
import sys, json, math, platform, hashlib, time
from fractions import Fraction as F
import numpy as np
from scipy.optimize import minimize_scalar
import gurobipy as gp
from gurobipy import GRB

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT/'src'))
from singer import singer, is_perfect_difference_set
from bu import A_of_S

def dump(name, data):
    (OUT/name).write_text(json.dumps(data, indent=2, allow_nan=False)+'\n')

def minimum(A):
    A=np.asarray(A,int); X=int(A.max()); n=len(A)
    G=1 << (64*X).bit_length()
    coeff=np.zeros(G); coeff[A]=1
    f=np.fft.fft(coeff).real
    inds=np.where((f<=np.roll(f,1))&(f<=np.roll(f,-1)))[0]
    inds=sorted(inds,key=lambda j:f[j])[:16]
    best=(float(f.min()),float(np.argmin(f)*2*np.pi/G))
    for j in inds:
        x=j*2*np.pi/G
        rr=minimize_scalar(lambda y:float(np.cos(A*y).sum()),
            bounds=(x-2*np.pi/G,x+2*np.pi/G),method='bounded',
            options={'xatol':1e-14})
        if rr.fun<best[0]:best=(float(rr.fun),float(rr.x%(2*np.pi)))
    return dict(M=-best[0],R=-best[0]/math.sqrt(n),xmin=best[1],
        grid_M=-float(f.min()),G=G), f

def tent_delta(q, q0=0., G=16384):
    """Whole-line negative mass, exact identity; numerical periodic quadrature.

    q_j is value at j/B; q_0 real, q_B=0, negative nodes conjugate.
    Delta=(2pi)^-1 integral [-qhat]_+ dy = mean[-S]_+.
    """
    G=max(G,1 << (2*len(q)+1).bit_length())
    c=np.zeros(G,complex); c[0]=q0
    c[1:len(q)+1]=q
    c[-len(q):]=np.conj(q[::-1])
    vals=np.fft.ifft(c).real*G
    return float(np.maximum(-vals,0).mean()),vals

def exact_checks():
    rows=[]
    for L in range(3,35):
        # Exact weighted Fejer relaxation at finite X=L-1.
        a=[F(L-j,L) for j in range(1,L)]
        mass=sum(a); energy=sum(v*v for v in a); latent=sum(v*(1-v) for v in a)
        assert mass==F(L-1,2)
        assert energy==F((L-1)*(2*L-1),6*L)
        assert latent==F(L*L-1,6*L)
        assert energy+latent==mass
        rows.append(dict(L=L,mass=str(mass),sum_a_squared=str(energy),latent=str(latent)))
    # Independent negative-spectrum integral against sinc^2 on the line.
    A=np.array([1,3,4,8,10]); X=int(A.max()); Y=X+1
    th=np.arange(131072)*2*np.pi/131072
    fv=np.cos(np.outer(th,A)).sum(axis=1)
    l1=float(np.abs(fv).mean())
    q=np.zeros(X,complex);q[A-1]=1
    d,_=tent_delta(q,G=131072)
    assert abs(d-l1)<1e-11
    # Periodization truncated to 201 periods: independently evaluates FT.
    ph=(np.arange(8192)+.5)*2*np.pi/8192
    psum=sum(np.sinc((ph+2*np.pi*k)/(2*np.pi))**2 for k in range(-100,101))
    fn=np.cos(np.outer(ph,A)).sum(axis=1)
    direct=float(np.mean(psum*np.maximum(-2*fn,0)))
    assert direct<=d+2e-6 and d-direct<.02
    shifted=[]
    for theta in (0.,.137,1.37,math.pi):
        qs=q*np.exp(1j*np.arange(1,X+1)*theta)
        ds,_=tent_delta(qs,G=131072)
        shifted.append(dict(theta=theta,delta=ds))
        assert abs(ds-d)<1e-7
    dump('exact_checks.json',dict(fejer=rows,tent_l1=l1,
        tent_delta=d,direct_201_periods=direct,shifted=shifted))

def make_sets():
    sets=[]
    for q in (7,19,43,83,163):
        S,v=singer(q);assert is_perfect_difference_set(S,v)
        A=sorted({b-a for a in S for b in S if b>a})
        assert len(A)==q*(q+1)//2
        sets.append(dict(name=f'Singer_diff_{q}',A=A,q=q,v=v,
            exact_M_upper=(q+1)/2,source_S=S))
        if q in (7,19,43,83):
            T=[s-v//2 for s in S]
            sets.append(dict(name=f'Bu_Singer_{q}',A=A_of_S(T),q=q,source_S=T))
    for rel in ('examples/e68/e68.jsonl','examples/e68/e68b.jsonl',
                'examples/e72/e72_n64.jsonl','examples/e72/e72_n128.jsonl',
                'examples/e72/e72_n256.jsonl','examples/e72/e72c_n128_C6.jsonl'):
        path=ROOT/rel
        if not path.exists():continue
        data=[json.loads(line) for line in path.read_text().splitlines() if line.strip()]
        data=[r for r in data if 'A' in r]
        if data:
            r=min(data,key=lambda r:r.get('grid_R',100))
            sets.append(dict(name=path.stem,A=r['A'],source=rel,source_row=r))
    rng=np.random.default_rng(2026101906)
    for X in (768,3072,12288):
        m=np.arange(1,X+1)
        sets.append(dict(name=f'random_flat_{X}',A=m[rng.random(X)<1/3].tolist()))
        sets.append(dict(name=f'random_taper_{X}',A=m[rng.random(X)<(1-m/(X+1))].tolist()))
    dump('sets.json',sets)
    return sets

def profiles(A, f, H, B, cap=8):
    X=max(A);n=len(A);G=len(f)
    # Restrict to half-circle and choose actual local maxima, separated by 1/X.
    inds=np.where((f>=np.roll(f,1))&(f>=np.roll(f,-1))&(f>H))[0]
    inds=[j for j in inds if j<=G//2]
    chosen=[]
    for j in sorted(inds,key=lambda j:-f[j]):
        x=j*2*np.pi/G
        if all(abs(x-xx)>=1/X for xx in chosen):chosen.append(x)
        if len(chosen)>=cap:break
    aa=set(A);m=np.arange(1,X+1);a=np.isin(m,A).astype(float)
    data=[];allq=[]
    for theta in chosen:
        E=np.exp(1j*m*theta)
        q=[];qc=[];means=[]
        for j in range(1,B):
            mask=(m>(j-.5)*X/B)&(m<=(j+.5)*X/B)
            p=float(a[mask].mean()); means.append(p)
            q.append(complex(np.mean(a[mask]*E[mask])))
            qc.append(complex(np.mean((a[mask]-p)*E[mask])))
        q=np.array(q);qc=np.array(qc);allq.append(q)
        end=float(np.clip(q[0].real,0,1))
        d0,_=tent_delta(q);dn,_=tent_delta(q,end);dm,_=tent_delta(q,1)
        dc,_=tent_delta(qc)
        data.append(dict(theta=theta,height=float(np.cos(np.array(A)*theta).sum()),
            q=[[float(z.real),float(z.imag)] for z in q],
            centered_q=[[float(z.real),float(z.imag)] for z in qc],means=means,
            q0_natural=end,delta_q0_zero=d0,delta_natural=dn,
            delta_q0_one=dm,delta_centered_zero=dc))
    return data,allq

def allocate_diagonal(qs, budget, G=1024):
    # Necessary aggregate diagonal bound only; not a full completion LP.
    S=len(qs)
    if not S:return None
    vals=np.array([tent_delta(q,G=G)[1] for q in qs])
    model=gp.Model();model.Params.OutputFlag=0;model.Params.Threads=2
    d=model.addMVar(S,lb=0,ub=1,name='diag')
    neg=model.addMVar((S,G),lb=0,name='neg')
    model.addConstr(d.sum()<=budget)
    for s in range(S):model.addConstr(neg[s,:]>=-vals[s,:]-d[s])
    model.setObjective(neg.sum()/G,GRB.MINIMIZE);model.optimize()
    if model.Status!=GRB.OPTIMAL:raise RuntimeError(model.Status)
    fine=sum(tent_delta(q,float(v),G=16384)[0] for q,v in zip(qs,d.X))
    return dict(budget=budget,status=int(model.Status),grid=G,
        objective=float(model.ObjVal),fine_objective=fine,diag=d.X.tolist())

def joint_word_lift(A, ell, G=1024, optimize=False):
    # Block words are indexed in absolute residues r=m mod ell.
    X=max(A);B=(X+ell-1)//ell
    G=max(G,1 << (2*B+1).bit_length())
    words=np.zeros((B,ell))
    for a in A:words[(a-1)//ell,a%ell]=1
    q=np.fft.ifft(words,axis=1)
    # h(t,r) at t=j/(B+1) is words[j-1,r], endpoints zero.
    spectra=np.array([tent_delta(q[:,s],G=G)[1] for s in range(ell)])
    delta=float(np.maximum(-spectra,0).mean(axis=1).sum())
    deltafine=sum(tent_delta(q[:,s],G=16384)[0] for s in range(ell))
    mass=float(words.mean(axis=1).sum()/(B+1))
    adjacent=float((words[:-1]*words[1:]).mean(axis=1).sum())
    l2=(2*float(words.mean(axis=1).sum())+adjacent)/(3*(B+1))
    result=dict(ell=ell,B=B,mass=mass,l2=l2,defect=mass-l2,
        delta=delta,deltafine=deltafine,G=G,sg_lower_bound=mass**3/12-2*deltafine*mass)
    assert mass-l2>=mass**3/12-2*deltafine*mass-1e-8
    if optimize:
        model=gp.Model();model.Params.OutputFlag=0;model.Params.Threads=2
        v=model.addMVar(ell,lb=0,ub=1,name='identity_values')
        for r in range(ell):model.addConstr(v[r]==v[(-r)%ell])
        neg=model.addMVar((ell,G),lb=0,name='negative_spectrum')
        angles=2*np.pi*np.outer(np.arange(ell),np.arange(ell))/ell
        Fmat=np.cos(angles)/ell
        diag=Fmat@v
        for s in range(ell):model.addConstr(neg[s,:]>=-spectra[s,:]-diag[s])
        model.setObjective(neg.sum()/G,GRB.MINIMIZE);model.optimize()
        assert model.Status==GRB.OPTIMAL
        q0=Fmat@v.X
        df=sum(tent_delta(q[:,s],float(q0[s]),G=16384)[0] for s in range(ell))
        result['optimized']=dict(status=int(model.Status),objective=float(model.ObjVal),
            fine_objective=df,identity_values=v.X.tolist(),q0=q0.tolist())
    return result

def zoo():
    sets=make_sets();summary=[];profile_rows=[];joint_rows=[]
    for rec in sets:
        A=rec['A'];n=len(A);X=max(A)
        info,f=minimum(A)
        l1=float(np.abs(f).mean())
        row=dict(name=rec['name'],n=n,X=X,C=X/n,**info,l1=l1,
            micro_delta=l1,certificate='NUMERICAL, no global lower certificate')
        H=n**.75
        row['H']=H;row['M_over_H']=info['M']/H
        row['micro_delta_over_MH']=l1*H/info['M']
        row['energy_above_H']=float(np.mean(f*f*(f>H)))
        row['energy_total']=float(np.mean(f*f))
        assert abs(row['energy_total']-n/2)<1e-6
        summary.append(row)
        for B in (8,16,32):
            if X<2*B:continue
            ds,qs=profiles(A,f,H,B)
            pp=dict(name=rec['name'],B=B,H=H,M_over_H=info['M']/H,
                total_candidates_measured=len(ds),profiles=ds)
            # The central profile is never graded and cannot be charged twice
            # as a conjugate pair. This toy LP applies only to noncentral pairs.
            pair_qs=[q for q,d in zip(qs,ds)
                     if abs(math.sin(d['theta']))>1e-10]
            if pair_qs and B==16:
                pfront=sum(a<=max(1,X//16) for a in A)/max(1,X//16)
                pp['toy_pd_diagonal_lp']=allocate_diagonal(pair_qs,max(0,(1-pfront)/2))
            profile_rows.append(pp)
        if rec['name'] in ('Singer_diff_19','Singer_diff_43','Singer_diff_163',
                           'Bu_Singer_43','e72_n128','e68','random_taper_3072'):
            for ell in (8,16,32):
                jr=joint_word_lift(A,ell,optimize=ell==16)
                joint_rows.append(dict(name=rec['name'],M_over_H=info['M']/H,**jr))
        print(json.dumps({k:v for k,v in row.items() if k!='certificate'}),flush=True)
        dump('summary.json',summary);dump('profiles.json',profile_rows);dump('joint_lifts.json',joint_rows)
    dump('manifest.json',dict(python=platform.python_version(),numpy=np.__version__,
        gurobi=gp.gurobi.version(),seed=2026101906,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        normalization='cos(ax); negative spectral mass integral [-FT h]_+ dy/(2pi)',
        all_minima='NUMERICAL, FFT plus direct local refinement, no interval certificate'))

def consistency_lp():
    rows=[]
    for X,n in ((24,6),(48,12),(96,24)):
        G=2048;angles=2*np.pi*np.arange(G//2+1)/G
        mat=np.cos(np.outer(angles,np.arange(1,X+1)))
        for binary in (False,True):
            model=gp.Model();model.Params.OutputFlag=0;model.Params.Threads=2
            model.Params.TimeLimit=45
            a=model.addMVar(X,lb=0,ub=1,vtype=GRB.BINARY if binary else GRB.CONTINUOUS)
            M=model.addVar(lb=0)
            model.addConstr(a.sum()==n);model.addConstr(mat@a>=-M)
            model.setObjective(M,GRB.MINIMIZE);model.optimize()
            rr=dict(X=X,n=n,binary=binary,status=int(model.Status),
                runtime=float(model.Runtime),lower_bound=float(model.ObjBound),
                G=G,meaning='floating solver result, not exact infeasibility certificate')
            if model.SolCount:
                vals=a.X
                rr.update(M_grid=float(M.X),coefficients=vals.tolist(),
                    sum_squares=float(vals@vals),missing_variance=float(sum(vals*(1-vals))))
                if binary:
                    A=(np.where(vals>.5)[0]+1).tolist(); rr['A']=A
                    inf,_=minimum(A);rr['actual_minimum_numerical']=inf
            rows.append(rr);dump('consistency_lp.json',rows);print(json.dumps(rr),flush=True)

def review():
    ss=json.loads((OUT/'summary.json').read_text())
    pp=json.loads((OUT/'profiles.json').read_text())
    jj=json.loads((OUT/'joint_lifts.json').read_text())
    print('SUMMARY')
    for r in ss:
        print(r['name'],r['n'],r['X'],round(r['R'],6),
              round(r['M_over_H'],6),round(r['l1'],6))
    print('BLOCK PROFILES: B=16')
    small=[]
    for r in pp:
        if r['B']!=16:continue
        ds=r['profiles'];lp=r.get('toy_pd_diagonal_lp')
        row=dict(name=r['name'],B=16,S=len(ds),M_over_H=r['M_over_H'],
            sum_delta_zero=sum(s['delta_q0_zero'] for s in ds),
            sum_delta_natural=sum(s['delta_natural'] for s in ds),
            sum_delta_one=sum(s['delta_q0_one'] for s in ds),
            lp_min=lp['fine_objective'] if lp else None)
        small.append(row);print(json.dumps(row))
    print('JOINT LIFTS')
    for r in jj:
        if r['ell']==16:print(json.dumps(r))
    dump('compact_profile_summary.json',small)
    # All signed-tent kernels used to independently check the weighted Gram proof.
    checks=0;worst=F(0)
    for p in (F(1,4),F(1,2),F(3,4)):
        for q in (F(0),min(p,1-p)/2,min(p,1-p)):
            for T in range(1,201):
                t=F(T,200);N=t.denominator//t.numerator+1
                phi=1-t
                for chi in (-1,1):
                    h=phi*(p-q*chi)
                    charge=q*(1-chi*phi-F(1,N*N))
                    # Signed-spectrum kernel is nonnegative even at a boundary t=1.
                    assert charge>=0
                    assert h<=1-F(1,N*N)+charge
                    assert charge<=2*q
                    checks+=1
    dump('weighted_gram_checks.json',dict(exact_rational_pointwise_checks=checks))
    print('WEIGHTED GRAM',checks)

def meso():
    # Additional lower-height audit, excluding the central lobe in summaries.
    sets=json.loads((OUT/'sets.json').read_text());rows=[]
    for rec in sets:
        A=rec['A'];info,f=minimum(A);H=math.sqrt(len(A))
        for B in (16,32):
            if max(A)<2*B:continue
            ds,qs=profiles(A,f,H,B,cap=12)
            noncentral=[d for d in ds if abs(math.sin(d['theta']))>1e-10]
            rr=dict(name=rec['name'],B=B,H=H,M_over_H=info['M']/H,
                profiles=ds,noncentral_measured=len(noncentral),
                delta_noncentral=sum(d['delta_natural'] for d in noncentral),
                delta_centered_noncentral=sum(d['delta_centered_zero'] for d in noncentral))
            rows.append(rr)
            print(json.dumps({k:v for k,v in rr.items() if k!='profiles'}),flush=True)
        dump('lower_height_profiles.json',rows)

def finalize():
    sets={r['name']:r for r in json.loads((OUT/'sets.json').read_text())}
    ps=json.loads((OUT/'profiles.json').read_text())
    # Remove the superseded toy diagonal allocation, which included the
    # central character in an invalid conjugate-pair budget. It was not used
    # in any conclusion. Raw measured profiles are unaffected.
    for rr in ps:
        rr.pop('necessary_diagonal_lp',None)
        rr['central_profile_separate']=True
    dump('profiles.json',ps)
    compact=[]
    for rr in ps:
        if rr['B']!=16:continue
        ds=rr['profiles']
        compact.append(dict(name=rr['name'],B=16,S=len(ds),M_over_H=rr['M_over_H'],
            sum_delta_zero=sum(d['delta_q0_zero'] for d in ds),
            sum_delta_natural=sum(d['delta_natural'] for d in ds),
            sum_delta_one=sum(d['delta_q0_one'] for d in ds)))
    dump('compact_profile_summary.json',compact)
    rows=json.loads((OUT/'joint_lifts.json').read_text());stable=[]
    for rr in rows:
        if rr['ell']!=16:continue
        A=sets[rr['name']]['A'];ell=16;X=max(A);B=(X+ell-1)//ell
        words=np.zeros((B,ell))
        for a in A:words[(a-1)//ell,a%ell]=1
        q=np.fft.ifft(words,axis=1)
        q0=np.array(rr['optimized']['q0'])
        refined=sum(tent_delta(q[:,s],float(q0[s]),G=65536)[0] for s in range(ell))
        stable.append(dict(name=rr['name'],ell=ell,
            delta_G16384=rr['optimized']['fine_objective'],delta_G65536=refined,
            difference=refined-rr['optimized']['fine_objective'],M_over_H=rr['M_over_H']))
    dump('quadrature_refinement.json',stable)
    # Exact independent run-top count check on fixed small finite sets.
    rng=np.random.default_rng(2026101906);exact_count=0
    for n in range(1,33):
        for trial in range(8):
            aa=set(rng.choice(np.arange(1,5*n+1),n,replace=False).tolist())
            E=aa|{-a for a in aa};N=len(E)
            tops=sum(sum(a-t in E and a+t not in E for a in E)
                     for t in range(1,2*max(aa)+1))
            T3=sum(sum(a-t in E and a+t in E for t in range(1,2*max(aa)+1)) for a in E)
            assert tops==N*(N-1)//2-T3 and tops>=n*n
            exact_count+=1
    dump('run_top_checks.json',dict(exact_integer_cases=exact_count,n_range=[1,32]))
    summary=json.loads((OUT/'summary.json').read_text())
    lows=json.loads((OUT/'lower_height_profiles.json').read_text())
    final=dict(sets=len(sets),high_height_block_rows=len(ps),
        high_height_individual_profiles=sum(len(r['profiles']) for r in ps),
        lower_height_block_rows=len(lows),
        lower_height_individual_profiles=sum(len(r['profiles']) for r in lows),
        joint_lift_rows=len(rows),optimized_joint_lifts=len(stable),
        smallest_observed_R=min(r['R'] for r in summary),
        exact_run_top_cases=exact_count,quadrature_refinement=stable)
    dump('final_summary.json',final)
    manifest=json.loads((OUT/'manifest.json').read_text())
    manifest.update(final_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        corrected_toy_lp='Removed central-lobe double-counting allocation; not used in any conclusion',
        commands=['audit.py all','audit.py review','audit.py meso','audit.py finalize'],
        required_launcher='DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2')
    dump('manifest.json',manifest)
    print(json.dumps(final,indent=2))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else 'all'
    if mode in ('all','exact'):exact_checks()
    if mode in ('all','zoo'):zoo()
    if mode in ('all','lp'):consistency_lp()
    if mode=='review':review()
    if mode=='meso':meso()
    if mode=='finalize':finalize()
