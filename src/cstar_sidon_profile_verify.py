"""Independent conditional-profile and concrete Boolean certificate checks.

Direct integer convolution at p31, exact reference-law summation at p7,
and direct four-coordinate moment counts for both small global probes.
Run on Dirichlet. No imports from producers, no FFT/FLINT convolution.
"""
from collections import Counter,defaultdict
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path
import socket


def S(B):
    ans={(x-u,y-v) for x,y in B for u,v in B if (x,y)!=(u,v)}
    assert len(ans)==len(B)*(len(B)-1)
    return ans


def pairH(A,B):
    q={w:int(w in A)-int(w in B) for w in A|B};q={w:c for w,c in q.items() if c}
    return sum(c*q.get((s[0]-t[0],s[1]-t[1]),0) for s in A for t,c in q.items())


def small_law(data):
    p=7;I=[t[0] for t in data['cases'][0]['actual_points']]
    I=[t for t in range(p) if 2*(t*t%p)<p] if data.get('actual_kind')=='quadratic_arc' else list(range(3))
    k=len(I);A=S([(t,t*t%p) for t in I]);full=set()
    for a,b,c,d in itertools.product(range(p),repeat=4):
        if (a*d-b*c)%p==0:continue
        base=[((a*t+b*t*t)%p,(c*t+d*t*t)%p) for t in range(p)]
        for x,y in itertools.product(range(p),repeat=2):
            full.add(tuple(sorted(((u+x)%p,(v+y)%p) for u,v in base)))
    assert len(full)==2352
    law=Counter()
    for B in full:law.update(itertools.combinations(B,k))
    matched=Counter(tuple((t,(a*t*t+b*t+c)%p) for t in I)
                    for a in range(1,p) for b,c in itertools.product(range(p),repeat=2))
    result={}
    for kind,L in [('isotropic',law),('matched',matched)]:
        value=F(sum(weight*pairH(A,S(B)) for B,weight in L.items()),sum(L.values()))
        target=data['small_reference_check']['cases'][kind]
        assert value==F(target['exact_H']) and value>=F(target['lower'])
        result[kind]=str(value)
    return result


def check_costs(data):
    checked=[]
    for row in data['cases']:
        p=row['p'];k=row['k'];P=list(map(tuple,row['actual_points']));A=S(P);I=[x for x,y in P]
        dx=Counter(x-y for x in I for y in I if x!=y)
        for kind,record in row['means'].items():
            if kind=='isotropic':
                c=F(k*(k-1),p*p-1);sp=F(2*p*p+1,3*p)
                norm=c*c*(sp*sp-1)
            else:
                norm=F(sum(v*v for v in dx.values())*(2*p**3+p),3*p**4)
            var=k*(k-1)-norm
            assert var==F(record['reference_variance_integral'])
            assert F(record['conditional_H_lower'])==F(record['H_fixed_mean'])-k*var
            if p==31:
                den=(p*p-1)*p*p if kind=='isotropic' else p*p
                coeff={}
                for x in range(-p+1,p):
                    for y in range(-p+1,p):
                        if x==0 and y==0:continue
                        m=k*(k-1)*(p-abs(x))*(p-abs(y)) if kind=='isotropic' else dx[x]*(p-abs(y))
                        coeff[x,y]=den*int((x,y) in A)-m
                H=F(sum(v*coeff.get((s[0]-t[0],s[1]-t[1]),0)
                          for s in A for t,v in coeff.items()),den*den)
                assert H==F(record['H_fixed_mean'])
        checked.append(dict(p=p,variance_and_lower_algebra=True,direct_fixed_mean_cubic_recount=p==31))
    return checked


def global_check(root,filename):
    data=json.loads((root/filename).read_text());A=set();q={};left=defaultdict(set);right=defaultdict(set);groups={}
    total_points=0
    for f in data['fibers']:
        p=f['p'];u=tuple(f['u']);P=list(map(tuple,f['actual']));B=list(map(tuple,f['reference']))
        assert len(P)==len(B)==f['k'];total_points+=len(P)
        if data.get('windowed'):
            expected=[(t,t*t%p) for t in range(p) if 2*t<p and 2*(t*t%p)<p]
            assert P==expected
            if not f['frozen']:
                params=f['reference_parameters'];T=params['A'];shift=params['shift']
                full=sorted(((T[0][0]*t+T[0][1]*t*t+shift[0])%p,
                             (T[1][0]*t+T[1][1]*t*t+shift[1])%p) for t in range(p))
                inside=[z for z in full if 2*z[0]<p and 2*z[1]<p]
                k=f['k'];expected=inside[:k] if len(inside)>=k else inside+[z for z in full if z not in inside][:k-len(inside)]
                assert B==expected and f['adjustment']==abs(len(inside)-k)
                assert f['reference_window_count_before']==len(inside)
        else:
            assert P==[(t,t*t%p) for t in range(f['k'])]
            if not f['frozen']:
                aa,bb,cc=f['reference_coefficients']
                assert B==[(t,(aa*t*t+bb*t+cc)%p) for t in range(f['k'])]
        AA=S(P);BB=S(B)
        assert len({(x%p,y%p) for x,y in AA})==len(AA)
        assert len({(x%p,y%p) for x,y in BB})==len(BB)
        if f['frozen']:assert set(P)==set(B)
        for w in AA:
            g=math.gcd(abs(w[0]),abs(w[1]));v=(w[0]//g,w[1]//g)
            M=(u[0]*w[0],u[0]*w[1],u[1]*w[0],u[1]*w[1]);A.add(M)
            if next(x for x in v if x)<0:v=(-v[0],-v[1])
            groups[M]=(u,v)
        for w in AA|BB:
            c=int(w in AA)-int(w in BB)
            if not c:continue
            M=(u[0]*w[0],u[0]*w[1],u[1]*w[0],u[1]*w[1]);q[M]=c
            g=math.gcd(abs(w[0]),abs(w[1]));v=(w[0]//g,w[1]//g)
            if next(x for x in v if x)<0:v=(-v[0],-v[1])
            left[u].add(M);right[v].add(M)
    a=sum(q.get(M,0) for M in A);Q=sum(c*c for c in q.values());H=0
    for M in A:
        u,v=groups[M]
        H+=sum(q[T]*q.get(tuple(M[i]-T[i] for i in range(4)),0) for T in left[u]|right[v])
    assert (a,Q,H)==(data['a'],data['Q'],data['H'])
    lower=F(data['global_M_lower']);k=2*lower
    assert Q*k*k+H*k-a*a<0
    base=6*data['X']+1;C=[base**i for i in range(4)]
    encoded=sorted({abs(sum(c*m for c,m in zip(C,M))) for M in A})
    assert len(encoded)==data['n']==len(A)//2 and encoded[0]>0
    label=filename.removesuffix('.json')
    (root/(label+'_A.txt')).write_text('\n'.join(map(str,encoded))+'\n')
    return dict(kind=label,n=data['n'],max_A=encoded[-1],base=base,
                sha256=hashlib.sha256((' '.join(map(str,encoded))).encode()).hexdigest(),
                a=a,Q=Q,H=H,global_M_lower=str(lower),global_M_upper=str(F(total_points,2)),
                direct_four_coordinate_recount=True,exact_square_identity_upper=True)


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    root=Path('.research/experiments/sidon_cutoff_2026-10-20')
    profiles={}
    for name in ['profile_probe.json','profile_arc.json']:
        data=json.loads((root/name).read_text())
        profiles[name]=dict(cost_checks=check_costs(data),direct_p7_reference_laws=small_law(data))
        print(json.dumps(dict(profile=name,status='PASS')),flush=True)
    global_rows=[global_check(root,name) for name in ['partial.json','windowed.json']]
    out=dict(status='PASS',host=socket.gethostname(),profiles=profiles,global_certificates=global_rows,
             qualification='All cubic lower inequalities exact; large-prime FLINT convolutions rechecked '
                           'algebraically, with independent direct cubic recount at p31 only.')
    (root/'profile_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(global_rows),flush=True)


if __name__=='__main__':main()
