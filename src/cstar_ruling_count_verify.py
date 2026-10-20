"""Direct small-matrix and lattice checks for the sharp ruling count.

No producer imports. All computations on Dirichlet.
"""
from fractions import Fraction as F
import itertools
import json
import math
from pathlib import Path
import socket


def primitive_left(M):
    a,b,c,d=M
    col=(a,c) if a or c else (b,d)
    g=math.gcd(*col);u=(col[0]//g,col[1]//g)
    if u[0]<0 or (u[0]==0 and u[1]<0):u=(-u[0],-u[1])
    return u


def formula(X,U):
    V=[(a,b) for b in range(-U,U+1) for a in range(U+1)
       if (a>0 or b>0) and math.gcd(a,abs(b))==1 and a*a+b*b<=U*U]
    total=0
    for u,v,w in itertools.combinations(V,3):
        h=(v[0]*w[1]-v[1]*w[0],w[0]*u[1]-w[1]*u[0],u[0]*v[1]-u[1]*v[0]);g=math.gcd(*h)
        L=max((h[i]//g)**2*(z[0]*z[0]+z[1]*z[1]) for i,z in enumerate([u,v,w]))
        q=X*X//L;r=math.isqrt(q)
        total+=6*(sum(2*math.isqrt(q-y*y)+1 for y in range(-r,r+1))-1)
    return total


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    controls=[]
    for X,U in [(4,2),(6,3),(8,4)]:
        matrices={}
        # Enumerate FOUR coordinates, not factorizations.
        for M in itertools.product(range(-X,X+1),repeat=4):
            if not 0<sum(z*z for z in M)<=X*X or M[0]*M[3]!=M[1]*M[2]:continue
            u=primitive_left(M)
            if sum(z*z for z in u)<=U*U:matrices[M]=u
        count=0
        for M,u in matrices.items():
            for N,v in matrices.items():
                if u==v:continue
                if tuple(-M[i]-N[i] for i in range(4)) in matrices:count+=1
        exact=formula(X,U);assert count==exact
        controls.append(dict(X=X,U=U,signed_matrices=len(matrices),ordered_triples=count,
                             primitive_relation_formula=exact,passed=True))
    lattice_tests=0
    for A in range(1,13):
        for a,b in itertools.product(range(1,A+1),repeat=2):
            if math.gcd(a,b,A)!=1:continue
            for R in [1,2,4,8,12]:
                points=[(x,y) for x in range(-(R//a),R//a+1) for y in range(-(R//b),R//b+1)
                        if (a*x+b*y)%A==0]
                nonzero=next((v for v in points if v!=(0,0)),None)
                independent=nonzero is not None and any(nonzero[0]*v[1]-nonzero[1]*v[0] for v in points)
                if independent:
                    assert 4*len(points)*A*a*b<=81*R*R
                    lattice_tests+=1
    for d in [F(0),F(1,6),F(1,4),F(2,5),F(49,100)]:
        threshold=2*d/(1+2*d);eta=(threshold+F(1,2))/2
        assert threshold<eta<F(1,2) and 3+2*d-eta*(1+2*d)<3
    root=Path('.research/experiments/sidon_cutoff_2026-10-20')
    out=dict(status='PASS',host=socket.gethostname(),direct_matrix_controls=controls,
             independent_vector_lattice_cases=lattice_tests,
             window_delta_checks=['0','1/6','1/4','2/5','49/100'],
             qualification='Finite controls corroborate counts and normalizations; uniform D(U) bound is the paper proof.')
    (root/'triple_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out),flush=True)


if __name__=='__main__':main()
