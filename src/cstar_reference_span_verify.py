"""Independently check saved span certificates by scalar integer squaring."""
from collections import Counter
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import socket
import flint


def psd_by_rational_schur(T):
    """Exact PSD test; zero diagonal rows must be identically zero."""
    S=[[F(t) for t in row] for row in T];pivots=[]
    while S:
        if any(S[i][i]<0 for i in range(len(S))):return False,pivots
        positive=[i for i in range(len(S)) if S[i][i]>0]
        if not positive:return all(t==0 for row in S for t in row),pivots
        j=positive[0];pivot=S[j][j];pivots.append(str(pivot));keep=[i for i in range(len(S)) if i!=j]
        S=[[S[i][l]-S[i][j]*S[j][l]/pivot for l in keep] for i in keep]
    return True,pivots


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    root=Path('.research/experiments/reference_entropy_2026-10-20');data=json.loads((root/'span.json').read_text());out=[]
    for info in data['actuals']:
        raw=(root/info['frequency_file']).read_bytes();assert hashlib.sha256(raw).hexdigest()==info['sha256']
        A=list(map(int,raw.split()));assert len(A)==len(set(A))==info['n'] and min(A)>0 and max(A)==info['max_A']
    for row in data['cases']:
        p=row['p'];base=6*p+1;P=[x+base*y for x,y in row['actual_points']]
        A={abs(a-b) for a,b in itertools.combinations(P,2)};assert len(A)==row['n']
        S=A|{-a for a in A};basis=[{0:1}]
        for R in row['reference_points']:
            assert Counter((row['grid']*x//p,row['grid']*y//p) for x,y in R)==Counter(
                (row['grid']*x//p,row['grid']*y//p) for x,y in row['actual_points'])
            assert len({((x-u)%p,(y-v)%p) for x,y in R for u,v in R if (x,y)!=(u,v)})==2*row['n']
            pts=[x+base*y for x,y in R];B={abs(a-b) for a,b in itertools.combinations(pts,2)}
            assert len(B)==row['n'] and len(A&B)<=3*row['n']//4
            q={}
            for d in A|B:
                c=int(d in A)-int(d in B)
                if c:q[d]=q[-d]=c
            basis.append(q)
        if not row['target_witness_found']:
            T=[[sum(c*d*(5*int(u+v==0)+2*int(u+v in S)) for u,c in r.items() for v,d in s.items())
                for s in basis] for r in basis]
            psd,pivots=psd_by_rational_schur(T)
            out.append(dict(label=row['label'],grid=row['grid'],exact_PSD_at_K_target=psd,
                            rational_positive_pivots=pivots,global_M_target='5/4',
                            qualification='PSD excludes a strict negative-form certificate at this target '
                                          'in the complete enumerated signed span only.'))
            continue
        # Build q's anew in one scalar dimension, using the stored integer weights.
        poly=Counter({0:row['integer_weights'][0]})
        counts=Counter((row['grid']*x//p,row['grid']*y//p) for x,y in row['actual_points'])
        for weight,R in zip(row['integer_weights'][1:],row['reference_points']):
            assert Counter((row['grid']*x//p,row['grid']*y//p) for x,y in R)==counts
            assert len({((x-u)%p,(y-v)%p) for x,y in R for u,v in R if (x,y)!=(u,v)})==2*row['n']
            S=[x+base*y for x,y in R];B={abs(a-b) for a,b in itertools.combinations(S,2)}
            assert len(A&B)<=3*row['n']//4
            for d in A|B:
                c=weight*(int(d in A)-int(d in B))
                poly[d]+=c;poly[-d]+=c
        poly={w:c for w,c in poly.items() if c}
        saved=Counter()
        for x,y,c in row['test_polynomial']:saved[x+base*y]+=c
        assert poly==dict(saved)
        radius=max(map(abs,poly));coeff=[poly.get(j-radius,0) for j in range(2*radius+1)]
        sq=flint.fmpz_poly(coeff)**2
        value=5*int(sq[2*radius])+4*sum(int(sq[d+2*radius]) for d in A if d<=2*radius)
        assert value==row['twice_weighted_square']<0
        out.append(dict(label=row['label'],grid=row['grid'],exact_form=value,global_M_lower='5/4',
                        strict=True,independent_scalar_square=True))
    result=dict(status='PASS',host=socket.gethostname(),certificates=out,
                qualification='Negative scalar forms certify lower bounds; rational PSD checks exclude '
                              'strict negative forms at the target only in the complete stated finite spans.')
    (root/'span_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],negative_scalar_forms=sum('exact_form' in r for r in out),
                          exact_PSD_forms=sum(r.get('exact_PSD_at_K_target',False) for r in out))))


if __name__=='__main__':main()
