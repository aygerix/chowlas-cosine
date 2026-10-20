"""R11 random-packet versus Paley probes; all computation on VM.
FFT observations, exact construction bounds, and Arb point certificates kept separate.
"""
import json, math, platform
from pathlib import Path
import numpy as np
from flint import arb,ctx
import sympy as sp
OUT=Path('.research/agents/tdense11_scratch');SEED=2026101911
def fft(a):
    X=len(a);N=1<<math.ceil(math.log2(32*(X+1)))
    freq=np.zeros(N);freq[1:X+1]=a/2;freq[-X:]=a[::-1]/2
    vals=np.fft.irfft(freq[:N//2+1],n=N)*N
    j=int(np.argmin(vals))
    return dict(min=float(vals[j]),index=j,grid=N,angle=float(2*np.pi*j/N),status='NUMERICAL')
def factor():
    rr=[json.loads(l) for l in open('examples/e82/e82.jsonl')]
    rec=max((r for r in rr if r['N']==320),key=lambda r:r['D'])
    gg=np.rint(np.array(rec['g'])*10**6).astype(np.int64)
    cc=np.r_[np.correlate(gg,gg,'full')[len(gg)-1:],0]
    return [int(v) for v in gg],[int(v) for v in cc]
def stats(a,p):
    r=a-p;e=p*(1-p)
    return dict(raw=[float(np.mean(a**j)) for j in range(1,5)],target=float(p.mean()),residual=[float(np.mean(r**j)) for j in range(1,5)],
       cubic_target=float(np.mean(e*(1-2*p))),fourth_target=float(np.mean(e*(1-3*e))),
       defect=float(np.mean(a*a*(a-1)**2)),nearest_energy=float(np.mean((a-(a>=.5))**2)),fft=fft(a))
def point_binary(b,ff,tag):
    ctx.prec=200;A=(np.flatnonzero(b)+1).tolist();OUT.joinpath(tag+'.txt').write_text('\n'.join(map(str,A))+'\n')
    angle=2*arb.pi()*ff['index']/ff['grid'];value=sum(((k*angle).cos() for k in A),arb(0))
    lower=math.floor((-ff['min']/math.sqrt(len(A))-1e-6)*10000)
    assert value < -arb(len(A)).sqrt()*lower/10000
    return dict(n=len(A),X=max(A),angle=f'2*pi*{ff["index"]}/{ff["grid"]}',value_ball=str(value),R_lower=f'{lower}/10000',status='PROVED_POINT_DIP',file=tag+'.txt')
def weighted_point(cc,X,q,ff,full=False):
    ctx.prec=180;N=len(cc)-1;ang=2*arb.pi()*ff['index']/ff['grid'];val=arb(0)
    root=arb(q).sqrt();den=(2*arb(q)).sqrt()
    for k in range(1,X+1):
        i,rem=divmod(k*N,X)
        wn=(cc[i]*(X-rem)+(cc[i+1]*rem if rem else 0));wd=cc[0]*X
        w=arb(wn)/wd;p=(1-(1-w*w).sqrt())/2 if k<X else arb(0)
        ch=0 if k%q==0 else (1 if pow(k%q,(q-1)//2,q)==1 else -1)
        if full:
            S=arb(q-1)/2 if ch==0 else (-1+root*ch)/2
            rr=w*S/den
        else:rr=w*ch/2
        val+=(p+rr)*(k*ang).cos()
    return dict(angle=f'2*pi*{ff["index"]}/{ff["grid"]}',value_ball=str(val),status='PROVED_POINT_VALUE')
def main():
    gg,cc=factor();OUT.joinpath('packet_factor.json').write_text(json.dumps(dict(g=gg,autocorrelation=cc,normalization=cc[0],source='E82 N320 rounded factor integers')))
    rng=np.random.default_rng(SEED);rows=[]
    for X,q in [(4096,61),(65536,257)]:
        assert sp.isprime(q) and q%4==1
        k=np.arange(1,X+1);t=k/X;w=np.interp(t,np.arange(len(cc))/(len(cc)-1),np.array(cc)/cc[0]);p=(1-np.sqrt(np.maximum(0,1-w*w)))/2;e=w*w/4
        J=int(X**.6);N=1<<math.ceil(math.log2(64*(X+1)));centres=rng.integers(0,N,J);counts=np.bincount(centres,minlength=N)
        r=w*np.fft.rfft(counts).real[1:X+1]/math.sqrt(2*J);a=p+r
        st=stats(a,p);b=(a>=.5);bf=fft(b.astype(float))
        st.update(family='random',X=X,J=J,seed=SEED,ideal_global_bound=f'-sqrt({J}/8)-1/4',rounded=point_binary(b,bf,f'random_round_X{X}'))
        st['correction_energy_lower_bound_from_cubic']=float((np.mean(e*(1-2*p)))**2/(math.sqrt(p.mean())+(p.mean()*np.mean(a**4))**.25+math.sqrt(np.mean(a**4)))**2)
        OUT.joinpath(f'packet_centres_X{X}.json').write_text(json.dumps(dict(N=N,indices=centres.tolist())))
        rows.append(st);print('FOURTH_PROBE',json.dumps(st),flush=True)
        chi=np.array([0 if j%q==0 else (1 if pow(int(j%q),(q-1)//2,q)==1 else -1) for j in k])
        S=np.where(chi==0,(q-1)/2,(-1+np.sqrt(q)*chi)/2)
        for name,rr in [('paley_full',w*S/math.sqrt(2*q)),('paley_DC_removed',w*chi/2)]:
            aa=p+rr;st=stats(aa,p)
            st.update(family=name,X=X,q=q,ideal_global_bound=f'-({q}-1)/(4*sqrt(2*{q}))-1/4' if name=='paley_full' else 'NONE; positivity lost')
            if X==65536:st['point_certificate']=weighted_point(cc,X,q,st['fft'],full=name=='paley_full')
            if name=='paley_full':
                ctx.prec=180;st['global_lower_bound_ball']=str(-arb(q-1)/(4*(2*arb(q)).sqrt())-arb(1)/4)
            rows.append(st);print('FOURTH_PROBE',json.dumps(st),flush=True)
    # All exact algebra; prime Paley off-DC centered values are +/-sqrt(q)/2.
    kurt=[]
    for q in (5,13,61,257,1021):
        assert sp.isprime(q) and q%4==1
        chi=np.array([1 if pow(j,(q-1)//2,q)==1 else -1 for j in range(1,q)])
        assert chi.sum()==0 and np.mean(chi**2)==1 and np.mean(chi**4)==1
        kurt.append(dict(q=q,kurtosis_exact='1',normalized_exceptional_DC_fourth_mass_exact=f'{q}/16',individual_cosine_amplitude=f'1/sqrt({q})',status='PROVED_BY_GAUSS_SUM_FORMULA; exact character checks'))
    OUT.joinpath('fourth_probe.json').write_text(json.dumps(dict(seed=SEED,python=platform.python_version(),rows=rows,kurtosis=kurt),indent=2))
if __name__=='__main__':main()
