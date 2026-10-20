"""Independent endpoint reconstruction, Mobius residues and mixed counts.

No imports from either producer. Direct four-coordinate cubic counting
at X=64 checks the ruling-polynomial computation. All on Dirichlet.
"""
from collections import Counter,defaultdict
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import socket
import flint


def mobius(n):
    sign=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;sign=-sign
            if n%p==0:return 0
        p+=1
    return -sign if n>1 else sign


def reconstruct(f):
    p=f['p'];A=f['A'];s=f['shift']
    B=[((A[0][0]*t+A[0][1]*t*t+s[0])%p,
        (A[1][0]*t+A[1][1]*t*t+s[1])%p) for t in range(p-1,-1,-1)]
    assert len(set(B))==p and set(B)==set(map(tuple,f['points']))
    assert (A[0][0]*A[1][1]-A[0][1]*A[1][0])%p!=0
    W=set()
    for i,(x,y) in enumerate(B):
        for x1,y1 in B[i+1:]:
            w=(x-x1,y-y1)
            if w[0]<0 or (w[0]==0 and w[1]<0):w=(-w[0],-w[1])
            assert w not in W and w!=(0,0);W.add(w)
    assert len(W)==p*(p-1)//2
    return B,W


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    flint.ctx.prec=192;root=Path('.research/experiments/sidon_fibers_2026-10-20')
    data=json.loads((root/'results.json').read_text());mixed=json.loads((root/'mixed.json').read_text())
    checked=[];small=None
    for row in data['cases']:
        X=row['X'];P=math.prod(row['h']);C=[P//h for h in row['h']];j=row['j']
        assert P==row['P'] and [j%h for h in row['h']]==row['crt_residues']
        encoded=[];contents=Counter();right=defaultdict(list);n=0;maxp=0;A_small=set();small_groups={}
        for f in reversed(row['fibers']):
            a,b=f['u'];assert math.gcd(abs(a),abs(b))==1 and a*a+b*b<=row['U']**2
            B,W=reconstruct(f);p=f['p'];maxp=max(maxp,p);n+=len(W)
            assert 2*p*p*(a*a+b*b)<=X*X
            for x,y in W:
                g=math.gcd(abs(x),abs(y));contents[g]+=1;v=(x//g,y//g);z=(g*a,g*b);right[v].append(z)
                M=(a*x,a*y,b*x,b*y);encoded.append(abs(sum(c*m for c,m in zip(C,M))))
                if X==64:A_small.add(M);small_groups[M]=(tuple(f['u']),v)
        encoded.sort();assert len(set(encoded))==n==row['n'] and encoded[0]>0
        assert encoded[-1]==row['max_A']
        assert hashlib.sha256((' '.join(map(str,encoded))).encode()).hexdigest()==row['sha256']
        assert dict(sorted(contents.items()))=={int(g):c for g,c in row['content_counts'].items()}
        error=F(44*X*n,7*min(row['h']))
        for r in row['residue_certificates']:
            q=r['q'];J=sum(d*d*mobius(q//d) for d in range(1,q+1) if q%d==0);value=F(0)
            for g,c in contents.items():
                numerator=sum(d*d*mobius(q//d) for d in range(1,q+1) if q%d==0 and g%d==0)
                value+=F(c*numerator,J)
            assert value==F(r['average_f']) and max(F(0),-value-error)==F(r['scalar_M_lower'])
        val=flint.arb(0)
        for a in encoded:val+=(2*flint.arb.pi()*(a*j%P)/P).cos()
        lower=F(row['point_M_lower']);assert val+flint.arb(lower.numerator)/lower.denominator<0
        assert F(row['left_plane_all_phase_M_upper'])==F(maxp,2)
        relevant={v:Z for v,Z in right.items() if len(Z)>=row['right_unscanned_trivial_upper']}
        assert set(relevant)==set(tuple(z['v']) for z in row['right_plane_diagnostics'])
        worst=max(row['right_plane_diagnostics'],key=lambda z:z['numerical_M'])
        v=tuple(worst['v']);Z=right[v];K=worst['K'];ix,iy=worst['grid_index']
        # Positive Fejer plane test, with no aliases in the scalar encoding.
        m=64*(math.isqrt((X*X)//(v[0]*v[0]+v[1]*v[1]))+1)
        assert 2*(m+1)*math.sqrt(v[0]*v[0]+v[1]*v[1])+X<min(row['h'])
        plane=flint.arb(0)
        for x,y in Z:
            w=F((m+1-abs(x))*(m+1-abs(y)),(m+1)**2)
            assert w>=0
            plane+=(2*flint.arb.pi()*((ix*x+iy*y)%K)/K).cos()*w.numerator/w.denominator
        plower=F(max(0,math.floor(-float(plane.mid())*10**6)-2),10**6)
        assert plane+flint.arb(plower.numerator)/plower.denominator<0
        result=dict(X=X,rotated=row['rotated'],n=n,point_M_lower=str(lower),
                    best_tested_residue=row['best_residue'],
                    right_Fejer_plane_M_lower=str(plower),right_Fejer_v=list(v),
                    all_phase_right_upper_claimed=False,passed=True)
        checked.append(result);print(json.dumps(result),flush=True)
        if X==64:small=(A_small,small_groups)
    assert small is not None
    A,groups=small;record=next(r for r in mixed if r['X']==64)
    B=set();Bgroups={}
    for f in record['references']:
        _,W=reconstruct(f);u=tuple(f['u'])
        for x,y in W:
            M=(u[0]*x,u[0]*y,u[1]*x,u[1]*y);B.add(M)
            g=math.gcd(abs(x),abs(y));Bgroups[M]=(u,(x//g,y//g))
    q={};left=defaultdict(set);right=defaultdict(set)
    for c,S,G in [(1,A,groups),(-1,B,Bgroups)]:
        for M in S:
            u,v=G[M]
            for t in [1,-1]:
                T=tuple(t*x for x in M);q[T]=q.get(T,0)+c
                left[u].add(T);right[v].add(T)
    q={M:c for M,c in q.items() if c};H=0
    for M in A:
        u,v=groups[M]
        # Count the union directly in four coordinates; no line
        # subtraction or polynomial Kronecker substitution is used.
        for T in left[u]|right[v]:
            H+=2*q.get(T,0)*q.get(tuple(M[i]-T[i] for i in range(4)),0)
    a=2*len(A-B);Q=sum(c*c for c in q.values())
    assert (a,Q,H)==(record['a'],record['Q'],record['H'])
    for r in mixed:
        k=F(r['global_K_lower'])
        assert r['Q']*k*k+r['H']*k-r['a']**2==F(r['exact_inequality_Qk2_Hk_minus_a2'])<0
        assert r['H']==r['H_left']+r['H_right']-r['H_line'] and r['Q']==2*r['a']
    out=dict(status='PASS',host=socket.gethostname(),precision_bits=192,cases=checked,
             direct_four_coordinate_cubic_check=dict(X=64,a=a,Q=Q,H=H),
             larger_cubics='Exact producer integer polynomial/sparse sums, with certificate algebra rechecked; '
                            'not independently recounted in four coordinates.',
             qualification='No numerical right-plane minima are promoted to global upper certificates.')
    (root/'verification.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
