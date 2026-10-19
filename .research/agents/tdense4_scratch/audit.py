"""Round-4 audits. Run only with DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2.
Fraction assertions are exact; Arb assertions are interval-certified; FFT data are NUMERICAL.
"""
import json, math, sys, platform
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from scipy.optimize import minimize_scalar
from flint import arb, ctx
ROOT=Path('.research/agents/tdense4_scratch')
ctx.prec=128
sys.path.insert(0,'src')

def dump(name, data):
    (ROOT/name).write_text(json.dumps(data,indent=2)+'\n')

def exact():
    count=positive=useful=0
    max_conv_ratio=Q(0)
    failures=[]
    # Complete enumeration of every word through ambient X=6 and four rational models.
    for X in range(1,7):
        models=[[Q(0)]*X,[Q(1,2)]*X,[Q(X-j,X) for j in range(1,X+1)],
                [Q((X-j)**2,2*X*X) for j in range(1,X+1)]]
        for mask in range(1,1<<X):
            a=[(mask>>j)&1 for j in range(X)]
            A=[j+1 for j,v in enumerate(a) if v]
            # Each value -f(x) supplies a rigorous lower bound on M. No global-grid claim.
            Mlo=arb(0)
            for k in range(65):
                angle=arb.pi()*k/64
                v=-sum(((angle*j).cos() for j in A),arb(0))
                if v.lower()>Mlo.upper(): Mlo=arb(v.lower())
            ml=Q(str(float(Mlo.lower())-1e-12)).limit_denominator(10**14)
            assert arb(ml.numerator)/ml.denominator < Mlo
            for P in models:
                beta=[Q(ai)-pi for ai,pi in zip(a,P)]
                pref=[]; z=Q(0)
                for v in beta: z+=v; pref.append(z)
                D=max(map(abs,pref)); V=sum(abs((P+[Q(0)])[j+1]-P[j]) for j in range(X))
                e=[p*(1-p) for p in P]
                pz=lambda j: P[abs(j)-1] if 1<=abs(j)<=X else (P[0] if j==0 else Q(0))
                bz=lambda j: beta[abs(j)-1] if 1<=abs(j)<=X else Q(0)
                Q2=sum(abs(pz(j+1)-2*pz(j)+pz(j-1)) for j in range(-X-1,X+2))
                energy=sum(b*b for b in beta)
                err=sum(beta[j]*(1-2*P[j]) for j in range(X))
                assert energy==sum(e)+err
                assert abs(err)<=D*(1+2*V)
                hmin=max(1,math.ceil(4*D)-1)
                for h in sorted({hmin,4*hmin+3,16*hmin+15}):
                    delta=4*D/(h+1); assert delta<=1
                    kt={k:Q(h+1-abs(k),(h+1)**2) for k in range(-h,h+1)}
                    # Direct exact convolution, including all generated tail coefficients.
                    conv={j:sum(kt[k]*bz(j-k) for k in kt) for j in range(0,X+h+1)}
                    assert max(map(abs,conv.values()))<=delta
                    if delta: max_conv_ratio=max(max_conv_ratio,max(map(abs,conv.values()))/delta)
                    gamma={j:bz(j)-conv[j] for j in conv}
                    E=sum(v*v for j,v in gamma.items() if j>0)
                    Em=sum(e)-D*(1+2*V)-2*delta*sum(map(abs,beta))
                    assert E>=Em
                    for w in sorted({1,X//2+1,X}):
                        kw=lambda j:Q(max(0,w+1-j),w+1)
                        W=1+2*sum(kw(j)**2 for j in range(1,w+1))
                        S=sum(kw(j)**2*gamma.get(j,Q(0))**2 for j in range(1,w+1))
                        ep=sum(kw(j)**2*(e[j-1] if j<=X else 0) for j in range(1,w+1))
                        bp=sum(kw(j)**2*(beta[j-1]**2 if j<=X else 0) for j in range(1,w+1))
                        assert abs(bp-ep)<=D*(2+2*V)
                        Sp=ep+D*(2+2*V)+3*delta*w
                        assert S<=Sp
                        R=Q(X+h+w+1) # rho=1 is a rigorous (conservative) Nikolskii upper bound.
                        assert R>W
                        Delta=W*Em-R*Sp
                        # pi^2>9; upper bound the claimed lower bound using this smaller subtraction.
                        Ulo=Q(9*h*(h+2),96)*Q2
                        if Delta>0:
                            positive+=1
                            z=ml+Ulo+delta/2
                            assert z>=0 and 2*(R-W)*z*z>=Delta, (X,mask,h,w)
                            if Delta>2*(R-W)*(Ulo+delta/2)**2: useful+=1
                        # Independently certify the full P31 chain at a lower test value of M.
                        # Ubound uses pi^2<(22/7)^2. If it passes at Mlo, it passes at true M.
                        Uhi=Q(22*22*h*(h+2),49*96)*Q2
                        mp=ml+Uhi+gamma[0]/2
                        if mp>=0:
                            assert W*(mp*mp+E/2)<=R*(mp*mp+S/2), (X,mask,h,w,'window')
                        count+=1
    # Exact second moment of the normalized Fejer kernel, fixes the 96 normalization.
    for h in range(1,101):
        kt={k:Q(h+1-abs(k),(h+1)**2) for k in range(-h,h+1)}
        assert sum(kt.values())==1
        assert sum(v*k*k for k,v in kt.items())==Q(h*(h+2),6)
    result=dict(status='PROVED finite exact/Arb checks',X_range=[1,6],models=4,
                word_policy='all nonempty binary words',window_checks=count,positive_Delta=positive,
                strictly_positive_bounds=useful,max_convolution_bound_ratio=str(max_conv_ratio),
                rho_used='1, conservative valid Nikolskii upper bound',arb_precision=ctx.prec,
                minimum_policy='Arb point evaluations give lower bounds on M, never grid global certificates')
    dump('exact_checks.json',result); print(json.dumps(result),flush=True)

def fft_metrics(A,ambient=None,windows=True):
    A=np.array(sorted(set(map(int,A))),dtype=int); n=len(A); X=int(A.max()); ambient=ambient or X
    G=1<<math.ceil(math.log2(64*X)); c=np.zeros(G); c[A]=1
    F=np.fft.fft(c); f=F.real; j=int(f.argmin()); aa=A.astype(float)
    obj=lambda x: float(np.cos(aa*x).sum())
    z=minimize_scalar(obj,bounds=((j-2)*2*math.pi/G,(j+2)*2*math.pi/G),method='bounded',options={'xatol':1e-14})
    M=max(-float(f.min()),-float(z.fun))
    out=dict(n=n,X=X,X_ambient=ambient,G=G,M_est=M,M_over_X=M/ambient,R_est=M/math.sqrt(n),
             parseval_error=float(np.mean(f*f)/(n/2)-1),direct_fft_error=abs(obj(j*2*math.pi/G)-f[j]))
    for K in (1,2,3): out[f'beta{K}']=float(np.mean(f*f*(f<=K*math.sqrt(n)))/(n/2))
    if windows:
        # Greedy fixed width energy windows for |F_A|^2, not the cosine/symmetric energy.
        p=np.abs(F)**2; half=max(1,round(8*G/(2*math.pi*X)))
        ext=np.r_[p[-half:],p,p[:half]]; cs=np.r_[0,np.cumsum(ext)]
        score=cs[2*half+1:]-cs[:-(2*half+1)]
        mask=np.zeros(G,dtype=bool); scores=score.copy(); records={}
        for k in range(1,65):
            ctr=int(scores.argmax()); idx=(np.arange(ctr-half,ctr+half+1)%G)
            mask[idx]=True; block=(np.arange(ctr-2*half,ctr+2*half+1)%G); scores[block]=-1
            if k in (1,4,16,64): records[str(k)]=float(p[mask].sum()/p.sum())
            if mask.all(): break
        out['complex_energy_greedy_K8']=records
        # Tallest positive noncentral cosine spike; full local shape is tested directly.
        dist=np.minimum(np.arange(G),G-np.arange(G))*2*math.pi/G
        ok=dist>32/X
        hh=np.where(ok,f,-np.inf); jj=int(hh.argmax()); H=float(hh[jj]); theta=2*math.pi*jj/G
        out.update(secondary_H=H,secondary_H_over_sqrtX=H/math.sqrt(X),M_over_secondary_H=M/H)
        shapes={}
        for B in (8,32):
            edges=np.linspace(0,X,B+1).astype(int); r=[]
            for l,u in zip(edges[:-1],edges[1:]):
                sub=A[(A>l)&(A<=u)]
                r.append(complex(np.exp(1j*sub*theta).sum()*X/(H*(u-l))))
            shapes[str(B)]=dict(L2=float(np.mean(np.abs(r)**2)),max_abs=float(max(map(abs,r))),
                                nominal_random_noise=math.sqrt(B*X)/H)
        out['normalized_block_profiles']=shapes
    return out

def bohr():
    from flint import fmpz
    rows=[]; sets={}
    # Quadratic-irrational membership is checked with Arb for EVERY m in these examples.
    alpha=(arb(5).sqrt()-1)/2
    for X in (2048,8192,32768,131072):
        ms=np.arange(1,X+1); t=ms/X
        # Floating pre-generation is independently checked at 128-bit precision below.
        u=np.remainder(ms*((math.sqrt(5)-1)/2),1)
        certified=[]
        for m in ms:
            v=alpha*int(m); fl=v.floor(); assert fl.is_exact()
            certified.append(v-fl)
        for k in (1,2,4):
            p=.5*(1-t)**k
            for centered in (False,True):
                hit=(np.minimum(u,1-u)<p/2) if centered else (u<p)
                A=ms[hit].tolist()
                for m,v,want in zip(ms,certified,hit):
                    pp=arb(1)/2*(arb(X-int(m))/X)**k
                    if centered:
                        if v<arb(1)/2: test=v<pp/2; opposite=v>=pp/2
                        else: test=arb(1)-v<pp/2; opposite=arb(1)-v>=pp/2
                    else: test=v<pp; opposite=v>=pp
                    assert test if want else opposite, (X,k,centered,int(m))
                name=f'bohr_{"center" if centered else "left"}_k{k}_X{X}'
                sets[name]=A
                row=dict(name=name,k=k,centered=centered,membership='Arb certified 128-bit',**fft_metrics(A,X,False))
                rows.append(row); print(json.dumps(row),flush=True)
    dump('bohr_sets.json',sets); dump('bohr_checks.json',dict(python=platform.python_version(),numpy=np.__version__,rows=rows))

def zoo():
    old=json.loads(Path('.research/agents/tdense3_scratch/sets.json').read_text())
    ex=json.loads(Path('.research/agents/tdense3_scratch/extension_sets.json').read_text())
    sets={k:v for k,v in old.items() if k.startswith(('E67_optimized_Bu','P42_fejer','E68_','random_dense'))}
    sets.update({k:v for k,v in ex.items() if 'bohr' in k.lower()})
    # Call the requested generator for three fresh Singer/Bu representatives as an independent input check.
    from e67_zoo import bu
    for q in (7,19,43): sets[f'fresh_e67_bu_q{q}']=bu(q)[0]
    rows=[]
    for name,A in sets.items():
        row=dict(name=name,**fft_metrics(A)); rows.append(row)
        print(json.dumps(row),flush=True)
    dump('zoo_sets.json',sets); dump('zoo_checks.json',dict(python=platform.python_version(),numpy=np.__version__,rows=rows))

def finite_cover():
    # Exact obstruction to omitting the sufficiently-large-X clause in window formulations.
    from singer import singer
    rows=[]
    for q in (7,19,43,101):
        S,v=singer(q); A=sorted({b-a for a in S for b in S if b>a}); k=len(S); X=max(A); n=len(A)
        assert n==k*(k-1)//2
        delta=Q(k,2*X) # Exact square identity gives M<=k/2=delta*X.
        J=(delta.denominator**2)//(delta.numerator**2)
        # K=16 windows cover the circle if JK >= pi X; use pi<22/7.
        cover=16*J*7>22*X
        assert cover
        rows.append(dict(q=q,n=n,X=X,C=str(Q(X,n)),M_upper=str(Q(k,2)),delta=str(delta),
                         J=J,K=16,cover_certified=cover))
    dump('finite_cover.json',rows); print(json.dumps(rows),flush=True)

# Additional nonvacuous exact cases.
def exact_extended():
    rows=[]
    for X in (1024,4096,16384):
        P=[Q(X-j,X) for j in range(1,X+1)]; u=Q(1,2); prev=0; a=[]
        for p in P:
            u+=p; nxt=u.numerator//u.denominator; a.append(nxt-prev); prev=nxt
        beta=[Q(z)-p for z,p in zip(a,P)]; pref=[]; z=Q(0)
        for b in beta: z+=b; pref.append(z)
        D=max(map(abs,pref)); V=sum(abs((P+[Q(0)])[j+1]-P[j]) for j in range(X))
        h=128; w=X//8; delta=4*D/(h+1)
        vals=[beta[abs(j)-1] if j else Q(0) for j in range(-X,X+1)]
        s=[Q(0)]; ss=[Q(0)]
        for j,b in zip(range(-X,X+1),vals): s.append(s[-1]+b); ss.append(ss[-1]+j*b)
        def part(l,r):
            l=max(-X,l);r=min(X,r)
            if l>r:return Q(0),Q(0)
            return s[r+X+1]-s[l+X],ss[r+X+1]-ss[l+X]
        def bz(j): return beta[j-1] if 1<=j<=X else Q(0)
        gamma=[]; maxc=Q(0)
        for j in range(X+h+1):
            sl,tl=part(j-h,j);sr,tr=part(j+1,j+h)
            conv=((h+1-j)*sl+tl+(h+1+j)*sr-tr)/(h+1)**2
            maxc=max(maxc,abs(conv)); gamma.append(bz(j)-conv)
        assert maxc<=delta
        e=[p*(1-p) for p in P]
        err=sum(beta[j]*(1-2*P[j]) for j in range(X))
        assert sum(b*b for b in beta)==sum(e)+err
        assert abs(err)<=D*(1+2*V)
        E=sum(g*g for g in gamma[1:]); Em=sum(e)-D*(1+2*V)-2*delta*sum(map(abs,beta))
        kw=lambda j:Q(w+1-j,w+1)
        W=1+2*sum(kw(j)**2 for j in range(1,w+1))
        S=sum(kw(j)**2*gamma[j]**2 for j in range(1,w+1))
        Sp=sum(kw(j)**2*e[j-1] for j in range(1,w+1))+D*(2+2*V)+3*delta*w
        assert E>=Em and S<=Sp
        R=Q(X+h+w+1); Delta=W*Em-R*Sp
        Q2=Q(4,X) # For this exact even extension with Pbar_0=P1.
        pz=lambda j: P[abs(j)-1] if 1<=abs(j)<=X else (P[0] if j==0 else Q(0))
        assert sum(abs(pz(j+1)-2*pz(j)+pz(j-1)) for j in range(-X-1,X+2))==Q2
        ar=lambda q:arb(q.numerator)/q.denominator
        U=arb.pi()**2*h*(h+2)*ar(Q2)/96
        bound=(ar(Delta/(2*(R-W))).sqrt()-U-ar(delta)/2) if Delta>0 else None
        A=np.flatnonzero(a)+1; G=1<<math.ceil(math.log2(64*X)); c=np.zeros(G);c[A]=1
        j=int(np.fft.rfft(c).real.argmin()); x=arb.pi()*2*j/G
        Mlo=-sum(((x*int(k)).cos() for k in A),arb(0))
        if bound is not None: assert bound.upper()<Mlo.lower()
        rows.append(dict(X=X,n=len(A),h=h,w=w,D=str(D),delta=str(delta),Delta_positive=Delta>0,
                         bound=str(bound),M_point_lower=str(Mlo.lower()),Q2=str(Q2),rho='1',
                         status='Fraction identities and Arb certified finite lower-bound comparison'))
    dump('exact_extended.json',rows);print(json.dumps(rows),flush=True)

def meso():
    sets=json.loads((ROOT/'zoo_sets.json').read_text()); chosen={}
    for name,A in sets.items():
        if ('Bu' in name or 'bu' in name or 'P42' in name or 'random_dense' in name
            or ('bohr' in name.lower() and ('65536' in name or '16384' in name))): chosen[name]=A
    # Larger centered Bu set, with input generated by the same Singer construction.
    from singer import singer
    for q in (61,127):
        S0,_=singer(q); shift=-max(S0)//2; S=[s+shift for s in S0]
        D={3*(b-a) for a in S for b in S if b>a}
        E={abs(3*(a+b)+1) for i,a in enumerate(S) for b in S[i+1:]}
        chosen[f'centered_bu_q{q}']=sorted(D|E)
    rows=[]
    for name,A in chosen.items():
        A=np.array(A,dtype=int);X=int(A.max());n=len(A)
        G=1<<math.ceil(math.log2(64*X));c=np.zeros(G);c[A]=1;F=np.fft.fft(c);f=F.real
        angle=np.arange(G)*2*math.pi/G
        centers=[0,2*math.pi/3,4*math.pi/3] if ('Bu' in name or 'bu' in name) else [0]
        radius=max(32/X,X**(-.5))
        ok=np.ones(G,dtype=bool)
        for ctr in centers:
            dist=np.abs(np.remainder(angle-ctr+math.pi,2*math.pi)-math.pi);ok&=dist>radius
        j=int(np.where(ok,f,-np.inf).argmax());H=float(f[j]);theta=float(angle[j]);M=-float(f.min())
        r=dict(name=name,n=n,X=X,G=G,excluded_centers=centers,excluded_radius=radius,
               H=H,H_over_X=H/X,H_over_sqrtX=H/math.sqrt(X),M_grid_over_H=M/H)
        r['outside_energy_fraction']=float(np.mean(f*f*ok)/(n/2))
        r['profiles']={}
        for B in (8,32,128):
            edge=np.linspace(0,X,B+1).astype(int);vals=[]
            for l,u in zip(edge[:-1],edge[1:]):
                sub=A[(A>l)&(A<=u)]
                vals.append(complex(np.exp(1j*sub*theta).sum()*X/(H*(u-l))))
            r['profiles'][str(B)]=dict(L2=float(np.mean(np.abs(vals)**2)),max_abs=float(max(map(abs,vals))),
                                      random_noise_scale=math.sqrt(B*X)/H)
        if len(centers)>1:
            residue_real=int(np.count_nonzero(A%3==0))*1 - .5*int(np.count_nonzero(A%3!=0))
            assert residue_real==n/4
            r['exact_residue_peak']=dict(f_at_2pi_over3=n/4,normalization='exact integer count')
        rows.append(r);print(json.dumps(r),flush=True)
    dump('meso_checks.json',rows);dump('meso_sets.json',{k:list(map(int,v)) for k,v in chosen.items()})

def summary():
    bo=json.loads((ROOT/'bohr_checks.json').read_text())['rows']
    zoo=json.loads((ROOT/'zoo_checks.json').read_text())['rows']
    me=json.loads((ROOT/'meso_checks.json').read_text())
    tab=[]
    for k in (1,2,4):
        for cent in (False,True):
            rr=[r for r in bo if r['k']==k and r['centered']==cent]
            tab.append(dict(k=k,centered=cent,values=[dict(X=r['X_ambient'],n=r['n'],M_over_X=r['M_over_X']) for r in rr]))
    summary=dict(bohr_cases=len(bo),bohr_membership_decisions=sum(r['X_ambient'] for r in bo),
                 zoo_cases=len(zoo),mesoscopic_cases=len(me),bohr_table=tab,
                 max_parseval_error=max(abs(r['parseval_error']) for r in bo+zoo),
                 max_direct_fft_error=max(r['direct_fft_error'] for r in bo+zoo),
                 min_zoo_beta1=min((r['beta1'],r['name']) for r in zoo),
                 min_zoo_R=min((r['R_est'],r['name']) for r in zoo),
                 meso_rows=[r for r in me if ('q127' in r['name'] or 'q61' in r['name'] or '200000' in r['name'])])
    dump('summary.json',summary);print(json.dumps(summary,indent=2),flush=True)

def hcg():
    sets=json.loads((ROOT/'zoo_sets.json').read_text())
    sets.update(json.loads((ROOT/'meso_sets.json').read_text()))
    rows=[]
    for name,aa in sets.items():
        A=np.array(aa,dtype=int);X=int(A.max());n=len(A)
        G=1<<math.ceil(math.log2(64*X)); c=np.zeros(G);c[A]=1
        f=np.fft.fft(c).real;M=-float(f.min()); rad=math.ceil(G/(2*math.pi*X))
        for scale in (2,4,8,16):
            H=scale*math.sqrt(n);hit=f>H
            ext=np.r_[hit[-rad:],hit,hit[:rad]].astype(np.int32)
            cs=np.r_[0,np.cumsum(ext,dtype=np.int64)]
            expanded=(cs[2*rad+1:]-cs[:-(2*rad+1)])>0
            # This expands the ENTIRE superlevel set. It contains every allowed window union.
            residual=float(np.mean(f*f*(~expanded))/X)
            rows.append(dict(name=name,n=n,X=X,scale=scale,M_grid_over_H=M/H,
                             residual_over_X=residual,expanded_measure=float(expanded.mean()),
                             residual_plus_M_over_H=residual+M/H))
        print(name,flush=True)
    dump('hbcg_checks.json',rows)
    out=dict(status='NUMERICAL only',sets=len(sets),rows=len(rows),
             minimum_residual_plus_M_over_H=min(rows,key=lambda r:r['residual_plus_M_over_H']),
             minimum_residual_over_X=min(rows,key=lambda r:r['residual_over_X']),
             convention='K=1, expand all f>H grid points by ceil(G/(2pi X)); lower-bounds residual outside any selected center windows up to grid resolution')
    dump('hbcg_summary.json',out);print(json.dumps(out,indent=2),flush=True)

def verify():
    import hashlib
    checked={}
    for stem,rowsfile in (('bohr','bohr_checks.json'),('zoo','zoo_checks.json'),('meso','meso_checks.json')):
        sets=json.loads((ROOT/(stem+'_sets.json')).read_text())
        data=json.loads((ROOT/rowsfile).read_text())
        rows=data['rows'] if isinstance(data,dict) else data
        assert len(rows)==len(sets)
        for row in rows:
            A=sets[row['name']]
            assert all(type(a)==int and a>0 for a in A)
            assert len(A)==len(set(A))==row['n'] and max(A)==row['X']
            if stem=='meso' and len(row['excluded_centers'])>1:
                d=sum(a%3==0 for a in A)
                assert 4*d-2*(len(A)-d)==len(A)
        checked[stem]=len(rows)
    ex=json.loads((ROOT/'exact_checks.json').read_text())
    assert ex['window_checks']==4260
    extended=json.loads((ROOT/'exact_extended.json').read_text())
    assert all(r['Delta_positive'] for r in extended)
    cover=json.loads((ROOT/'finite_cover.json').read_text())
    assert all(r['cover_certified'] for r in cover)
    hb=json.loads((ROOT/'hbcg_checks.json').read_text())
    assert len(hb)==304 and all(r['residual_over_X']>=0 for r in hb)
    checked['hbcg']=len(hb)
    files=[p for p in ROOT.glob('*.json') if p.name not in ('verification.json','manifest.json')]+[ROOT/'audit.py']
    manifest={p.name:dict(bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in files}
    dump('manifest.json',manifest)
    result=dict(status='PROVED finite artifact-integrity and integer-set checks passed',checked=checked,
                artifact_count=len(manifest),python=platform.python_version(),numpy=np.__version__)
    dump('verification.json',result);print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':
    ROOT.mkdir(exist_ok=True)
    modes={'exact':exact,'extended':exact_extended,'bohr':bohr,'zoo':zoo,
           'finite_cover':finite_cover,'meso':meso,'summary':summary,'hcg':hcg,'verify':verify}
    modes[sys.argv[1]]()
