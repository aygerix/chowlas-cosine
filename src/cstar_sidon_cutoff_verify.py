"""Independent frozen-reference and completion checks, on Dirichlet.

Four-coordinate cubic recount at X64 includes ALL actual targets, even
those whose own reference is frozen. Larger moment certificates have
their exact algebra/correlation rechecked, not a full cubic recount.
"""
from collections import Counter,defaultdict
from fractions import Fraction as F
import json
import math
from pathlib import Path
import socket
import flint


def points(f):
    p=f['p'];A=f['A'];s=f['shift']
    B=[((A[0][0]*t+A[0][1]*t*t+s[0])%p,
        (A[1][0]*t+A[1][1]*t*t+s[1])%p) for t in range(p-1,-1,-1)]
    assert set(B)==set(map(tuple,f['points'])) and len(set(B))==p
    return B


def signed_differences(B):
    S={(x-u,y-v) for x,y in B for u,v in B if (x,y)!=(u,v)}
    assert len(S)==len(B)*(len(B)-1)
    return S


def ex(turn):
    z=2*flint.arb.pi()*turn.numerator/turn.denominator
    return z.cos(),z.sin()


def norm_checks(p,B,C):
    S=signed_differences(B);T=signed_differences(C)
    cyclic=Counter((x%p,y%p) for x,y in S)
    assert len(cyclic)==p*(p-1) and set(cyclic.values())=={1}
    assert len({(x%p,y%p) for x,y in T})==p*(p-1)
    missing={(x,y) for x in range(p) for y in range(p) if x or y}-set(cyclic)
    assert len(missing)==p-1
    sums=Counter((x+u,y+v) for x,y in B for u,v in B)
    assert sum(c*c for c in sums.values())==2*p*p-p
    q={w:int(w in S)-int(w in T) for w in S|T};q={w:c for w,c in q.items() if c}
    H=sum(c*q.get((s[0]-t[0],s[1]-t[1]),0) for s in S for t,c in q.items())
    L=3+2*flint.arb(p).log();bound=416*p**3*L**4
    assert H<bound
    samples=[]
    for tx,ty in [(F(1,3*p),F(2,5*p)),(F(1,2),F(1,4)),(F(1,100*p),F(1,100*p))]:
        re=flint.arb(0);im=flint.arb(0)
        for x,y in B:
            a,b=ex(tx*x+ty*y);re+=a;im+=b
        ax=flint.arb(0);bx=flint.arb(0);ay=flint.arb(0);by=flint.arb(0)
        for t in range(p):
            a,b=ex(tx*t);ax+=a;bx+=b
            a,b=ex(ty*t);ay+=a;by+=b
        er=re-(ax*ay-bx*by)/p;ei=im-(ax*by+bx*ay)/p
        assert er*er+ei*ei<2*p*L**4
        samples.append(str((er*er+ei*ei)/p))
    return dict(p=p,missing=p-1,pair_H=H,pair_bound_checked=True,
                off_grid_E_squared_over_p_balls=samples,integer_fourth_moment=2*p*p-p)


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    flint.ctx.prec=192
    old=Path('.research/experiments/sidon_fibers_2026-10-20')
    root=Path('.research/experiments/sidon_cutoff_2026-10-20')
    originals=json.loads((old/'results.json').read_text());rows=json.loads((root/'frozen.json').read_text())
    verified=[]
    C3=5184*416+19683
    assert C3==2176227
    for row in rows:
        original=next(r for r in originals['cases'] if r['X']==row['X'] and r['rotated'])
        assert row['actual_sha256']==original['sha256']
        refs={tuple(f['u']):f for f in row['references']};a=0;Q=0;high=0;low=0
        targets={};q={};ql=defaultdict(set);qr=defaultdict(set)
        for f in original['fibers']:
            u=tuple(f['u']);B=points(f);p=f['p'];active=sum(t*t for t in u)>=row['cutoff_norm_squared']
            if active:
                S=signed_differences(B);T=signed_differences(points(refs[u]))
                assert len(S)==len(T);a+=len(S-T);Q+=len(S^T);high+=len(S)//2
            else:
                assert u not in refs;low+=p*(p-1)//2
                S=signed_differences(B) if row['X']==64 else None
                T=S
            if row['X']!=64:continue
            for w in S:
                M=(u[0]*w[0],u[0]*w[1],u[1]*w[0],u[1]*w[1])
                if next(x for x in w if x)!=abs(next(x for x in w if x)):continue
                g=math.gcd(abs(w[0]),abs(w[1]));v=(w[0]//g,w[1]//g);targets[M]=(u,v,active)
            if not active:continue
            for w in S|T:
                c=int(w in S)-int(w in T)
                if not c:continue
                M=(u[0]*w[0],u[0]*w[1],u[1]*w[0],u[1]*w[1]);q[M]=c
                g=math.gcd(abs(w[0]),abs(w[1]));v=(w[0]//g,w[1]//g)
                if next(x for x in v if x)<0:v=(-v[0],-v[1])
                ql[u].add(M);qr[v].add(M)
        assert (a,Q,high,low)==(row['a'],row['Q'],row['high_n'],row['frozen_n'])
        assert Q==2*a and high+low==row['n']
        k=F(row['global_K_lower']);assert Q*k*k+row['H']*k-a*a==F(row['exact_polynomial'])<0
        assert row['H']==row['H_left']+row['H_right']-row['H_line']
        extra={}
        if row['X']==64:
            H=0;frozen_H=0
            for M,(u,v,active) in targets.items():
                h=2*sum(q[T]*q.get(tuple(M[j]-T[j] for j in range(4)),0) for T in ql[u]|qr[v])
                H+=h
                if not active:frozen_H+=h
            assert H==row['H']
            extra=dict(independent_four_coordinate_H=H,frozen_actual_target_contribution=frozen_H)
        result=dict(X=row['X'],cutoff_squared=row['cutoff_norm_squared'],a=a,Q=Q,
                    n=high+low,actual_support_unchanged=True,
                    conservative_asymptotic_size_test_met=(64*C3*row['X']**3)**2<row['n']**3,
                    **extra,passed=True)
        verified.append(result);print(json.dumps(result),flush=True)
    populations=json.loads((old/'population.json').read_text())+json.loads((old/'population_extra.json').read_text())
    probes=json.loads((root/'cyclic_probe.json').read_text())
    norms=[]
    for row in populations:
        p=row['p'];B=list(map(tuple,row['worst_H_points']))
        probe=next((r for r in probes if r['p']==p),None)
        C=list(map(tuple,probe['sample_points'])) if probe else [(t,t*t%p) for t in range(p)]
        norms.append(norm_checks(p,B,C))
        L=3+2*flint.arb(p).log();z=F(row['conditional_H_max'])
        assert flint.arb(z.numerator)/z.denominator<416*p**3*L**4
    for W in range(2,1001):
        m=max(1,math.isqrt(W*W//2))
        assert 8*(F(1,m*m)+F(1,m))<=F(64,W)
    out=dict(status='PASS',host=socket.gethostname(),precision_bits=192,cases=verified,
             completion_and_pair_checks=norms,
             constants=dict(pair_cost=416,tail=64,log_comparison=81,global_C3=C3),
             qualification='Finite probes corroborate identities; all-parameter completion/cutoff theorem is a paper proof. '
                           'No independent four-coordinate cubic recount at X256/1024.')
    (root/'verification.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
