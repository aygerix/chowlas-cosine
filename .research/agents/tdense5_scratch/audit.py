"""Round-5 finite TL1 and tall-spectrum falsification. NUMERICAL unless marked exact.
Run only through the project's dirun.sh, with -c 2. Writes only this directory.
"""
from pathlib import Path
import sys, json, math, hashlib, platform
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.special import ndtr, ndtri
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'src'))
from singer import singer, is_perfect_difference_set
from e67_zoo import bu
OUT = Path(__file__).resolve().parent

def dump(name, x):
    (OUT/name).write_text(json.dumps(x, indent=2, allow_nan=False)+'\n')

def dy(t, Y):
    t = (np.asarray(t)+np.pi)%(2*np.pi)-np.pi
    den = np.sin(t/2)
    return np.where(np.abs(den)<1e-14, 1+0j,
        np.exp(1j*(Y+1)*t/2)*np.sin(Y*t/2)/(Y*np.where(np.abs(den)<1e-14,1,den)))

def word_test(name, a, xs, D=16):
    a=np.asarray(a,float); Y=len(a); m=np.arange(1,Y+1); p=float(a.mean())
    E=np.exp(1j*np.outer(m,np.asarray(xs)))
    c=((a-p)[:,None]*E).mean(axis=0)
    W=float(np.vdot(c,c).real); R=float(np.abs(c).sum())
    z=E@np.conj(c); L=z.real
    B=float((np.abs(z)**2).mean()-W)
    # U is the coherent normalized moment count. Q is absolute tuple count, degrees <=3.
    U=[]
    if R>0:
        v=z/R
        for d in range(1,D+1):
            U.append(max(float(abs(np.mean(v**j*np.conj(v)**(d-j))))
                         for j in range(d+1) if 2*j!=d))
    else: U=[0.]*D
    w=np.abs(c)/(R or 1); xs=np.asarray(xs)
    Q=[]
    if len(xs)<=80:
        for d in range(1,4):
            vals=[]
            for j in range(d+1):
                if 2*j==d: continue
                freqs=np.array([0.]); weights=np.array([1.])
                for ell in range(d):
                    sgn=1 if ell<j else -1
                    freqs=(freqs[:,None]+sgn*xs[None,:]).ravel()
                    weights=(weights[:,None]*w[None,:]).ravel()
                vals.append(float(np.dot(weights,np.abs(dy(freqs,Y)))))
            Q.append(max(vals))
    # Rotation CVaR by deterministic angular quadrature; independently tests the analytic step.
    ph=np.arange(512)*2*np.pi/512
    rot=(np.abs(z)[:,None]*np.cos(ph)[None,:]).ravel()
    count=int(round(p*len(rot)))
    top=float(np.partition(rot,len(rot)-count)[-count:].sum()/len(rot)) if count else 0.
    bound=math.sqrt(max(0,float(np.mean(abs(z)**2)))*min(1.,4*p*(1-p)))/np.pi
    # Use env <=4p(1-p), not equality with the sharper envelope.
    # Direct actual correlation identity must be W, including centering.
    identity=abs(float(np.mean((a-p)*L))-W)
    # Exact polynomial formula for averaging T_d(r cos(phi)); only floating evaluation is numerical.
    from numpy.polynomial import chebyshev as ch, polynomial as pol
    delta=[]
    for d in range(1,D+1):
        unit=np.zeros(d+1); unit[d]=1
        coeff=ch.cheb2poly(unit)
        radial=np.zeros(d+1)
        for j in range(0,d+1,2):radial[j]=coeff[j]*math.comb(j,j//2)/2**j
        delta.append(float(np.mean(ch.chebval(L/(R or 1),unit))-np.mean(pol.polyval(abs(z)/(R or 1),radial))))
    Ucheb=sum(abs(v)/(d+1)**2 for d,v in enumerate(delta))
    Bab=sum(abs(c[s]*c[r])*abs(dy(xs[s]-xs[r],Y)) for s in range(len(xs)) for r in range(len(xs)) if s!=r)
    majorant=(8/np.pi**2)*p*(1-p)+2*Bab+32*R/(np.pi*D)+(16/np.pi+4*p)*R*Ucheb
    assert 2*W<=majorant+1e-8
    self_mass=sum(abs(c[s])**2 for s in range(len(xs)) if abs(np.sin(xs[s]))<1e-12)
    out=dict(name=name,Y=Y,p=p,S=len(xs),W=W,twoW=2*W,
        variance=p*(1-p),ratio=2*W/(p*(1-p)) if 0<p<1 else 0.,
        genuine_two_sided_mass=2*W-self_mass,
        genuine_ratio=(2*W-self_mass)/(p*(1-p)) if 0<p<1 else 0.,
        R=R,K=R/math.sqrt(W) if W else 0.,B=B,U_by_degree=U,Q_by_degree=Q,
        correlation_error=identity,rot_CVaR=top,rot_bound=bound,
        empirical_CVaR_correlation=float(np.mean(a*L)),
        mean_L=float(L.mean()),max_z=float(np.max(abs(z))),
        Ucheb=Ucheb,Cheb_delta=delta,Babs=float(Bab),finite_TL1_RHS=float(majorant))
    assert identity<1e-10
    assert top<=bound+2e-5
    assert all(Q[i]+1e-10>=U[i] for i in range(len(Q)))
    return out

def finite():
    rng=np.random.default_rng(2026101905); rows=[]; saved=[]
    alpha=(math.sqrt(5)-1)/2
    for Y in (1024,4096,16384):
        m=np.arange(1,Y+1)
        for p in (.25,.5):
            a=(np.mod(m*alpha,1)<p).astype(int)
            xs=[2*np.pi*alpha]
            rows.append(word_test(f'Bohr_{Y}_{p}',a,xs)); saved.append(dict(name=rows[-1]['name'],a=a.tolist(),xs=xs))
        a=rng.integers(0,2,Y)
        xs=2*np.pi*np.array([math.sqrt(2),math.sqrt(3),math.sqrt(5),math.sqrt(7)])
        rows.append(word_test(f'random_{Y}',a,xs)); saved.append(dict(name=rows[-1]['name'],a=a.tolist(),xs=xs.tolist()))
        for q in (2,3,5):
            a=(m%q==0).astype(int); xs=[2*np.pi*j/q for j in range(1,(q+1)//2)] if q>2 else [np.pi]
            rows.append(word_test(f'residue_{q}_{Y}',a,xs)); saved.append(dict(name=rows[-1]['name'],a=a.tolist(),xs=xs))
    # Independent-coordinate Gaussian regime, actual irrational sequence with several frequencies.
    for S in (1,4,16,64):
        Y=32768; m=np.arange(1,Y+1)
        primes=[q for q in range(2,400) if all(q%d for d in range(2,math.isqrt(q)+1))][:S]
        xs=2*np.pi*np.sqrt(primes)
        score=np.cos(np.outer(m,xs)).sum(axis=1)
        a=(score>=0).astype(int)
        rows.append(word_test(f'majority_S{S}',a,xs,D=8))
        saved.append(dict(name=rows[-1]['name'],a=a.tolist(),xs=xs.tolist()))
    dump('finite_sets.json',saved); dump('finite_checks.json',rows)
    print(json.dumps([dict(name=r['name'],ratio=r['ratio'],K=r['K'],U2=r['U_by_degree'][1]) for r in rows]))

def make_zoo():
    rng=np.random.default_rng(2026101906); sets=[]
    for Y in (1024,4096):
        m=np.arange(1,Y+1); alpha=(math.sqrt(5)-1)/2
        for p in (.25,.5): sets.append((f'Bohr_{Y}_{p}',m[np.mod(m*alpha,1)<p].tolist()))
        sets.append((f'random_{Y}',m[rng.random(Y)<1/3].tolist()))
        for q in (2,3,5): sets.append((f'residue_{q}_{Y}',m[m%q==0].tolist()))
    for q in (7,19,43):
        S,v=singer(q); assert is_perfect_difference_set(S,v)
        A=sorted({b-a for b in S for a in S if b>a})
        assert len(A)==q*(q+1)//2
        sets.append((f'Singer_diff_{q}',A))
        A,r=bu(q); assert len(A)==q*(q+1)
        counts=[sum(x%3==r for x in A) for r in range(3)]
        assert 2*counts[0]==len(A)
        sets.append((f'Bu_{q}',A))
    for path in sorted((ROOT/'examples/e68').glob('*.jsonl'))+sorted((ROOT/'examples/e72').glob('*.jsonl')):
        for i,line in enumerate(path.read_text().splitlines()):
            try:d=json.loads(line)
            except ValueError:continue
            if isinstance(d.get('A'),list): sets.append((f'{path.parent.name}_{path.stem}_{i}',d['A']))
    seen=set(); result=[]
    for name,A in sets:
        A=sorted(set(map(int,A))); key=tuple(A)
        if key in seen:continue
        seen.add(key); result.append(dict(name=name,A=A))
    return result

def tall(use_saved=False):
    sets=json.loads((OUT/'zoo_sets.json').read_text()) if use_saved else make_zoo()
    if not use_saved:dump('zoo_sets.json',sets)
    rows=[]; frows=[]
    for rec in sets:
        name=rec['name']; A=np.array(rec['A'],int); X=int(max(A)); n=len(A)
        G=1<<math.ceil(math.log2(128*X)); seq=np.zeros(G); seq[A]=1
        F=np.fft.fft(seq); f=F.real; gridM=float(-f.min()); p=n/X
        idx=int(np.argmin(f)); x0=2*np.pi*idx/G
        opt=minimize_scalar(lambda x:float(np.cos(A*x).sum()),bounds=(x0-2*np.pi/G,x0+2*np.pi/G),method='bounded',options={'xatol':1e-14})
        direct_err=abs(float(np.cos(A*x0).sum())-f[idx])
        for k in (2,4,8,16):
            H=k*math.sqrt(n); mask=f>H
            resid=float(np.mean(f*f*~mask)); share=float(np.mean(f*f*mask)/(n/2))
            # Descending greedy peaks separated by >=2/X, one representative per +/- pair.
            peaks=np.nonzero((f>np.roll(f,1))&(f>=np.roll(f,-1))&mask&(np.arange(G)<=G//2))[0]
            peaks=peaks[np.argsort(f[peaks])[::-1]]; chosen=[]
            sep=math.ceil(G/(np.pi*X))
            for j in peaks:
                if all(min(abs(int(j)-r),G-abs(int(j)-r))>=sep for r in chosen):chosen.append(int(j))
            xs=2*np.pi*np.array(chosen)/G
            if chosen:
                # Coefficients of b=a-p on m=1..X, exactly the finite theorem's convention.
                cs=np.conj(F[chosen])/X-p*dy(xs,X)
                R=float(abs(cs).sum()); W=float(np.vdot(cs,cs).real)
                w=abs(cs)/(R or 1); qcounts=[]; tors=[]
                for d in range(1,5): tors.append(float(np.dot(w,np.abs(dy(d*xs,X)))))
                if len(chosen)<=64:
                    for d in (2,3):
                        vals=[]
                        for j in range(d+1):
                            if 2*j==d:continue
                            freqs=np.array([0.]); weights=np.array([1.])
                            for ell in range(d):
                                freqs=(freqs[:,None]+(1 if ell<j else -1)*xs).ravel()
                                weights=(weights[:,None]*w).ravel()
                            vals.append(float(np.dot(weights,abs(dy(freqs,X)))))
                        qcounts.append(max(vals))
                m=np.arange(1,X+1); z=np.zeros(X,complex)
                for xx,cc in zip(xs,cs):z+=np.conj(cc)*np.exp(1j*m*xx)
                v=z/(R or 1); u=[]
                for d in range(1,9):u.append(max(float(abs(np.mean(v**j*np.conj(v)**(d-j)))) for j in range(d+1) if 2*j!=d))
                if k==4:
                    a=np.zeros(X); a[A-1]=1
                    frows.append(word_test(name+'_tall4',a,xs,D=8))
            else:R=W=0.;qcounts=[];tors=[];u=[]
            # Exclude macro neighborhoods for the claim "Bu has no tall spikes".
            dist=np.minimum(np.arange(G),G-np.arange(G))*2*np.pi/G
            macro=dist<=max(32/X,X**(-.5))
            if name.startswith('Bu_'):
                for center in (2*np.pi/3,4*np.pi/3):
                    dd=abs(np.arange(G)*2*np.pi/G-center); macro|=np.minimum(dd,2*np.pi-dd)<=max(32/X,X**(-.5))
            residual_max=float(np.max(np.where(macro,-np.inf,f)))
            rows.append(dict(name=name,n=n,X=X,G=G,k=k,H=H,M_grid=gridM,M_local=float(-opt.fun),
                R_grid=gridM/math.sqrt(n),height_condition=gridM<=math.sqrt(n)/k**2,
                tall_measure=float(mask.mean()),tall_energy_share=share,residual_energy=resid,
                S=len(chosen),K=R/math.sqrt(W) if W else 0.,W=W,Q23=qcounts,U_by_degree=u,
                torsion_by_degree=tors,residual_peak_over_sqrtn=residual_max/math.sqrt(n),
                parseval_error=abs(float(np.mean(f*f))-n/2)/(n/2),direct_error=direct_err))
        print(json.dumps({key:rows[-1][key] for key in ('name','n','X','R_grid','S','residual_peak_over_sqrtn')}),flush=True)
    dump('tall_checks.json',rows);dump('zoo_tl1_checks.json',frows)

def cyclic():
    from numpy.polynomial import chebyshev as ch, polynomial as pol
    sets=json.loads((OUT/'zoo_sets.json').read_text()); rows=[]
    for rec in sets:
        A=np.array(rec['A'],int); X=int(A.max()); n=len(A); Y=1<<math.ceil(math.log2(8*X))
        sym=np.zeros(Y);sym[A]=1;sym[-A]=1
        assert int(sym.sum())==2*n
        coeff=np.fft.fft(sym).real/Y
        f=coeff*Y/2; Mgrid=-float(f.min()); p=2*n/Y
        for kk in (2,4,8,16):
            H=kk*math.sqrt(n)
            inds=np.nonzero(f[1:Y//2]>H)[0]+1
            c=coeff[inds]; W=float(np.dot(c,c));R=float(c.sum())
            raw=np.zeros(Y,complex);raw[inds]=c;z=np.fft.ifft(raw)*Y
            L=z.real;U=[];deltas=[]
            for d in range(1,17):
                v=z/(R or 1)
                vals=[complex(np.mean(v**j*np.conj(v)**(d-j))) for j in range(d+1) if 2*j!=d]
                assert min(x.real for x in vals)>=-1e-10
                assert max(abs(x.imag) for x in vals)<1e-9
                U.append(max(x.real for x in vals))
                unit=np.zeros(d+1);unit[d]=1;poly=ch.cheb2poly(unit); radial=np.zeros(d+1)
                for j in range(0,d+1,2):radial[j]=poly[j]*math.comb(j,j//2)/2**j
                deltas.append(float(np.mean(ch.chebval(L/(R or 1),unit))-np.mean(pol.polyval(abs(z)/(R or 1),radial))))
            Ucheb=sum(abs(v)/(d+1)**2 for d,v in enumerate(deltas))
            low=float(np.mean(f*f*(f<=H)))
            assert low<=H*Mgrid+2*Mgrid*Mgrid+1e-7
            assert abs(float(np.mean(abs(z)**2))-W)<1e-10
            assert abs(float(np.mean((sym-p)*L))-W)<1e-10
            gamma=1-8/np.pi**2
            budget=p*(1-p)-2*W
            bound=(8/np.pi**2)*p*(1-p)+32*R/(np.pi*16)+(16/np.pi)*R*Ucheb
            assert 2*W<=bound+1e-8
            rows.append(dict(name=rec['name'],Y=Y,n=n,X=X,k=kk,S=len(inds),p=p,
                W=W,R=R,K=R/math.sqrt(W) if W else 0.,capture_ratio=2*W/(p*(1-p)),
                low_cosine_energy=low,P40_upper=H*Mgrid+2*Mgrid*Mgrid,
                Nyquist_mass=float(coeff[Y//2]**2) if f[Y//2]>H else 0.,
                U_by_degree=U,Ucheb=Ucheb,D_sufficient=math.ceil(64*R/(np.pi*gamma*p*(1-p))) if R else 1,
                inverse_numerator=gamma*p*(1-p)-4*(H*Mgrid+2*Mgrid*Mgrid)/Y-float(coeff[Y//2]**2)-32*R/(np.pi*16),
                TL1_RHS=float(bound),gap=budget))
    dump('cyclic_checks.json',rows)
    print(json.dumps(dict(rows=len(rows),max_S=max(r['S'] for r in rows),max_D=max(r['D_sufficient'] for r in rows),min_capture=min(r['capture_ratio'] for r in rows),max_capture=max(r['capture_ratio'] for r in rows))))

def exact():
    from fractions import Fraction as F
    # Exact balanced energy is the obstruction to inferring radial moments from separation.
    energy=[]
    for S in range(1,129):
        counts=[0]*(2*S+1)
        for j in range(1,S+1):
            for k in range(1,S+1):counts[j+k]+=1
        E=sum(x*x for x in counts)
        assert 3*E==2*S**3+S
        energy.append(dict(S=S,energy=E,normalized_fourth=str(F(E,S*S))))
    # Exact SG checks on R times Z/2: h=triangle(t)*(p0-q*chi).
    sg=0;pointwise=0
    for j in range(1,16):
        p0=F(j,16)
        for k in range(0,int(64*min(p0,1-p0))+1):
            q=F(k,64);m=p0/2;b=m-(p0*p0+q*q)/3
            assert b>=m**3/12-2*q*m
            sg+=1
            for i in range(1,65):
                t=F(i,64)
                for chi in (-1,1):
                    h=(1-t)*(p0-q*chi)
                    assert 0<=h<=1
                    assert h<=1-t*t/4+2*q
                    pointwise+=1
    # Independent analytic-coefficient evaluation of the hinge approximation on a grid.
    from numpy.polynomial import chebyshev as ch
    cases=0;maxratio=0.
    us=np.linspace(-1,1,2049)
    for lam in np.linspace(-1,1,17):
        th=math.acos(lam)
        for D in (2,4,8,16,64):
            cs=np.zeros(D+1);cs[0]=(math.sin(th)-lam*th)/np.pi
            cs[1]=(2/np.pi)*(th/2+math.sin(2*th)/4-lam*math.sin(th))
            for d in range(2,D+1):cs[d]=(2/np.pi)*(.5*(math.sin((d-1)*th)/(d-1)+math.sin((d+1)*th)/(d+1))-lam*math.sin(d*th)/d)
            err=float(np.max(abs(ch.chebval(us,cs)-np.maximum(us-lam,0))))
            ratio=err/(4/(np.pi*D));maxratio=max(maxratio,ratio)
            assert ratio<1+1e-12;cases+=len(us)
    dump('exact_checks.json',dict(status='Exact rational SG and integer energy; hinge grid is NUMERICAL',
        energy=energy,SG_integral_cases=sg,SG_pointwise_cases=pointwise,
        hinge_grid_points=cases,hinge_max_error_over_proved_bound=maxratio))
    print(json.dumps(dict(SG_integral_cases=sg,SG_pointwise_cases=pointwise,energy_cases=len(energy),hinge_grid_points=cases,hinge_max_ratio=maxratio)))

def sharp():
    saved=json.loads((OUT/'finite_sets.json').read_text());rows=[]
    for rec in saved:
        if rec['name'] not in ('Bohr_16384_0.5','Bohr_16384_0.25','majority_S1'):continue
        a=np.array(rec['a']);p=float(a.mean());Y=len(a);xx=rec['xs'][0];m=np.arange(1,Y+1)
        c=complex(np.mean((a-p)*np.exp(1j*m*xx)));R=abs(c);W=R*R
        for D in (32,128,512,2048):
            ds=np.arange(1,D+1)
            delta=(np.exp(-1j*ds*np.angle(c))*dy(ds*xx,Y)).real
            U=float(np.sum(abs(delta)/ds**2))
            rhs=(8/np.pi**2)*p*(1-p)+32*R/(np.pi*D)+(16/np.pi+4*p)*R*U
            assert 2*W<=rhs+1e-10
            rows.append(dict(name=rec['name'],Y=Y,D=D,W=W,variance=p*(1-p),Ucheb=U,
                TL1_RHS=rhs,RHS_over_variance=rhs/(p*(1-p)),twoW_over_variance=2*W/(p*(1-p))))
    dump('sharp_checks.json',rows);print(json.dumps(rows,indent=2))

def radial():
    alpha=2*np.pi*(math.sqrt(5)-1)/2;Y=1<<22;rows=[];words=[]
    for S,q in ((8,17),(32,67),(128,257)):
        N=Y//q;tt=np.arange(1,N+1);theta=tt*q*alpha
        chosen=(np.cos(theta)>=0); old=(tt%2==0)
        n=Y//2-N//2+int(chosen.sum());p=n/Y
        common=np.mean((chosen.astype(float)-old)*np.exp(1j*theta))*N/Y
        xs=alpha+2*np.pi*np.arange(1,S+1)/q
        c=(Y//2)/Y*dy(2*xs,Y//2)+common-p*dy(xs,Y)
        W=float(np.vdot(c,c).real);R=float(abs(c).sum())
        v=np.zeros(q,complex);v[1:S+1]=np.conj(c);poly=np.fft.ifft(v)*q
        rr=np.arange(1,q+1);nr=(Y-rr)//q+1;ww=nr/Y
        radial_values=poly[rr%q]
        moment2=float(np.dot(ww,abs(radial_values)**2));moment4=float(np.dot(ww,abs(radial_values)**4))
        U=[]
        for d in range(1,9):
            vals=[]
            for j in range(d+1):
                k=d-j
                if j==k:continue
                beta=(j-k)*alpha
                factors=np.exp(1j*beta*(rr-q))*dy(beta*q,nr)
                vals.append(float(abs(np.sum(ww*radial_values**j*np.conj(radial_values)**k*factors))/R**d))
            U.append(max(vals))
        row=dict(S=S,q=q,Y=Y,p=p,normalized_fourth=moment4/W**2,
            limiting_fourth=(2*S*S+1)/(3*S),W=W,limiting_W=S/(np.pi*np.pi*q*q),
            twoW_over_variance=2*W/(p*(1-p)),max_normalized_amplitude=float(max(abs(c))/math.sqrt(W)),
            pair_orthogonality_error=abs(moment2-W),U_by_degree=U,
            max_relative_coefficient_error=float(max(abs(c-1/(np.pi*q)))/(1/(np.pi*q))))
        rows.append(row)
        words.append(dict(S=S,q=q,Y=Y,alpha=float(alpha),xs=xs.tolist(),
            override_ones=tt[chosen].tolist(),coefficients=[[float(v.real),float(v.imag)] for v in c]))
    dump('radial_words.json',words)
    dump('radial_obstruction_checks.json',rows);print(json.dumps(rows,indent=2))

def verify():
    import scipy
    finite_rows=json.loads((OUT/'finite_checks.json').read_text()); tall_rows=json.loads((OUT/'tall_checks.json').read_text())
    zoo=json.loads((OUT/'zoo_sets.json').read_text())
    for r in zoo:assert r['A']==sorted(set(r['A'])) and min(r['A'])>=1
    index={r['name']:(len(r['A']),max(r['A'])) for r in zoo}
    for r in tall_rows:assert (r['n'],r['X'])==index[r['name']] and r['G']>=128*r['X']
    assert max(r['correlation_error'] for r in finite_rows)<1e-10
    assert max(r['parseval_error'] for r in tall_rows)<1e-10
    for r in finite_rows:assert r['twoW']<=r['finite_TL1_RHS']+1e-8
    cy=json.loads((OUT/'cyclic_checks.json').read_text())
    ex=json.loads((OUT/'exact_checks.json').read_text())
    sh=json.loads((OUT/'sharp_checks.json').read_text())
    rad=json.loads((OUT/'radial_obstruction_checks.json').read_text())
    for r in cy:
        assert (r['n'],r['X'])==index[r['name']] and r['Y']>=8*r['X']
        assert 2*r['W']<=r['TL1_RHS']+1e-8
    summary=dict(status='NUMERICAL, not global certificates',python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,
        finite_count=len(finite_rows),zoo_count=len(zoo),tall_count=len(tall_rows),
        max_direct_error=max(r['direct_error'] for r in tall_rows),
        max_parseval_error=max(r['parseval_error'] for r in tall_rows),
        counterexample_height_condition_rows=sum(r['height_condition'] for r in tall_rows),
        cyclic_count=len(cy),cyclic_max_S=max(r['S'] for r in cy),
        cyclic_max_D=max(r['D_sufficient'] for r in cy),
        exact_counts={k:ex[k] for k in ('SG_integral_cases','SG_pointwise_cases','hinge_grid_points','hinge_max_error_over_proved_bound')},
        sharp=sh,radial_obstruction=rad,
        finite_selected=[{k:r[k] for k in ('name','genuine_ratio','U_by_degree','Ucheb','finite_TL1_RHS')} for r in finite_rows if r['Y']==16384 or r['name'].startswith('majority')],
        bu=[r for r in tall_rows if r['name'].startswith('Bu_') and r['k'] in (4,16)],
        e68e72=[dict(name=r['name'],k=r['k'],S=r['S'],Q23=r['Q23'],W=r['W']) for r in tall_rows if r['name'].startswith(('e68','e72')) and r['k']==4],
        source_counts={prefix:sum(r['name'].startswith(prefix) for r in zoo) for prefix in ('Bohr','random','residue','Singer','Bu','e68','e72')},
        noncentral_peaks_k4={prefix:sum(r['name'].startswith(prefix) and r['k']==4 and r['S']>1 for r in tall_rows) for prefix in ('e68','e72')},
        tall_by_k={str(k):dict(nonempty=sum(r['S']>0 for r in tall_rows if r['k']==k),max_S=max(r['S'] for r in tall_rows if r['k']==k),min_residual_over_n=min(r['residual_energy']/r['n'] for r in tall_rows if r['k']==k)) for k in (2,4,8,16)})
    dump('summary.json',summary)
    manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in OUT.glob('*.json') if p.name!='manifest.json'}
    manifest['audit.py']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();dump('manifest.json',manifest)
    print(json.dumps({k:v for k,v in summary.items() if k not in ('bu','e68e72','finite_selected','sharp','radial_obstruction')},indent=2))

def all_checks():
    finite();tall();cyclic();exact();sharp();radial();verify()

def replay():
    saved=json.loads((OUT/'finite_sets.json').read_text())
    rows=[word_test(r['name'],r['a'],r['xs'],D=8 if r['name'].startswith('majority') else 16) for r in saved]
    dump('finite_checks.json',rows)
    tall(use_saved=True);cyclic();exact();sharp();radial();verify()

if __name__=='__main__':
    {'finite':finite,'tall':tall,'cyclic':cyclic,'exact':exact,'sharp':sharp,'radial':radial,'verify':verify,'all':all_checks,'replay':replay}[sys.argv[1]]()
