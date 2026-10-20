"""Round 14 experiments. Execute only on dirichlet through dirun -c 4.

Gurobi supplies floating-coefficient MILP optima; exhaustive Arb/integer
enclosures certify finite optima for q<=31. No numerical result is promoted
to an asymptotic theorem. The combinatorial input sets are exact.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json, math, platform, time, hashlib
import numpy as np
import sympy as sy
import gurobipy as gp
from gurobipy import GRB
from flint import arb, ctx

ROOT = Path(__file__).resolve().parent
ctx.prec = 220

def arr(q, pairs):
    b = np.zeros(q, dtype=np.int64)
    for a in pairs: b[a] = b[-a] = 1
    return b

def conv_exact(x, y):
    q = len(x)
    return [sum(x[j]*y[(k-j)%q] for j in range(q)) for k in range(q)]

def bvals(q, pairs):
    return [sum((2*(2*arb.pi()*((g*a)%q)/q).cos() for a in pairs), arb(0))
            for g in range(1,(q+1)//2)]

def certify(q, pairs):
    b = arr(q, pairs); m = int(b.sum()); a = Q(m,q); d = 1-2*a
    assert b[0] == 0 and np.array_equal(b,b[(-np.arange(q))%q])
    vals = bvals(q,pairs)
    ik = min(range(len(vals)),key=lambda j:float(vals[j].mid()))
    ip = max(range(len(vals)),key=lambda j:float(vals[j].mid()))
    kval, peak = -vals[ik], vals[ip]
    assert all((v+kval).lower()>=0 or v.overlaps(-kval) for v in vals)
    aa = arb(m)/q
    # All inequalities below have strict margin at tested witnesses.
    margins = {
        'trace_K_ge_alpha': kval-aa,
        'brief_Parseval_peak': peak-(aa*(1-aa)*q-kval*kval)/kval,
        'sharp_Parseval_peak': peak-(aa*(1-aa)*q*q-m*kval)/((q-1)*kval-m),
        'A_norm_le_2K': 2*kval-(arb(m)+2*sum((abs(v) for v in vals),arb(0)))/q,
    }
    # The second-order bound requires the density-dependent linear term.
    allv = [arb(m)]+[vals[min(g,q-g)-1] for g in range(1,q)]
    S = sum((v for v in allv[1:] if v.lower()>0),arb(0))
    margins['quadratic_with_linear_term'] = (1-2*aa)*q*peak+2*kval*S-peak*peak
    equalities=[]
    def equal_frequency(g,j):
        coeff=[0]*q
        for sign in (-1,1):
            for x in pairs:
                coeff[sign*g*x%q]+=1
                coeff[sign*j*x%q]-=1
        return len(set(coeff))==1
    for j,v in enumerate(vals,1):
        assert (v+kval).lower()>0 or equal_frequency(j,ik+1)
        assert (peak-v).lower()>0 or equal_frequency(j,ip+1)
    for key,val in margins.items():
        if val.lower()>0:continue
        if key=='sharp_Parseval_peak' and val.contains(0):
            assert all(equal_frequency(g,ik+1) or equal_frequency(g,ip+1)
                       for g in range(1,(q+1)//2))
            equalities.append(key)
        else:raise AssertionError((q,pairs,key,str(val)))

    # Check the Fourier power identities independently in physical space,
    # using exact rational two-valued functions and cyclotomic polynomials.
    h = [Q(int(x))-a for x in b]
    Uphysical = [x/d for x in h]
    c = a*(1-a)/(d*d)
    for x in Uphysical:
        assert x*x == x+c
        assert x**3 == (1+c)*x+c
        assert x**4 == (1+2*c)*x+c*(1+c)
    # Exact DFT of the rational residual is zero: a direct certificate.
    counts = b.tolist()
    powers=[]
    for r in range(1,9):
        if r>1:counts=conv_exact(counts,b.tolist())
        powers.append(counts[0])
    for r in range(1,9):
        target=m**r+sum((v**r for v in allv[1:]),arb(0))
        assert (target-q*powers[r-1]).contains(0)
    posgamma = ip+1
    # At nonzero frequency, U^3-U=cU; its nonzero size is certified.
    Upeak = peak/(arb(d.numerator)/d.denominator)
    defect = (arb(c.numerator)/c.denominator)*Upeak
    assert defect.lower()>0
    return dict(q=q,cardinality=m,density=str(a),pairs=pairs,
                K_ball=str(kval),Lambda_ball=str(peak),
                K=float(kval.mid()),Lambda=float(peak.mid()),
                minimum_frequency=ik+1,peak_frequency=posgamma,
                margins={k:str(v) for k,v in margins.items()},exact_equalities=equalities,
                cubic_idempotence_defect_ball=str(defect),
                centered_first_two_terms_coefficient=str(1-2*c),
                exact_zero_sum_counts=powers,
                status='Exact set; 220-bit Arb inequalities; rational power identities exact')

def exact_optimum(q,k):
    scale=1<<100; h=(q-1)//2
    cosb={}
    for a in range(1,h+1):
        v=2*(2*arb.pi()*a/q).cos()*scale
        cosb[a]=(int(v.lower().floor().unique_fmpz()),int(v.upper().ceil().unique_fmpz()))
    def image(P,g):return tuple(sorted(min(g*a%q,q-g*a%q) for a in P))
    def mask(P):return sum(1<<(a-1) for a in P)
    seen=set(); groups=[];cases=0
    for P in combinations(range(1,h+1),k):
        cases+=1
        if mask(P) in seen:continue
        seen.update(mask(image(P,g)) for g in range(1,h+1))
        eig=[]
        for g in range(1,h+1):
            ims=image(P,g)
            eig.append((sum(cosb[a][0] for a in ims),sum(cosb[a][1] for a in ims)))
        kval=(-min(x[1] for x in eig),-min(x[0] for x in eig))
        groups.append((kval,list(P)))
    assert len(seen)==cases
    groups.sort(key=lambda t:sum(t[0]))
    best,pairs=groups[0]
    tied=[]
    for val,P in groups:
        if val[0]>best[1]:continue
        # Cyclotomic equality for exact ties, not overlap-as-equality.
        vb=bvals(q,P); vg=min(range(len(vb)),key=lambda i:float(vb[i].mid()))+1
        wb=bvals(q,pairs); wg=min(range(len(wb)),key=lambda i:float(wb[i].mid()))+1
        coeff=[0]*q
        for sign in (-1,1):
            for x in P:coeff[sign*vg*x%q]+=1
            for x in pairs:coeff[sign*wg*x%q]-=1
        assert len(set(coeff))==1,('unresolved exact optimum',q,P,pairs)
        tied.append(P)
    return dict(q=q,pair_count=k,cases=cases,dilation_orbits=len(groups),
                scale=str(scale),K_integer_enclosure=list(best),pairs=pairs,tied_orbits=tied,
                status='PROVED exact optimum by exhaustive integer-enclosure/cyclotomic comparison')

def algebra():
    a=sy.symbols('a'); d=1-2*a;c=a*(1-a)/d**2
    rows=[]
    for r in range(2,21):
        A=((1-a)**r-(-a)**r)/d**(r-1)
        mu=(a*(1-a)**(r-1)+(1-a)*(-a)**(r-1))/d**(r-1)
        Dr=sy.factor(A-r*mu)
        rows.append(dict(r=r,coefficient=str(Dr),at_quarter=str(Dr.subs(a,sy.Rational(1,4))),
                         at_eighth=str(Dr.subs(a,sy.Rational(1,8)))))
    assert sy.simplify(((1-a)**3+a**3)/d**2-3*c-(1-2*c))==0
    orders=[]
    for aa in (Q(1,4),Q(1,8),Q(1,16),Q(1,32),Q(1,64)):
        tt=aa/(1-aa)
        first=next(r for r in range(2,1000) if 1-r*tt-(r-tt)*(-tt)**(r-1)<0)
        orders.append(dict(alpha=str(aa),first_negative_order=first))
    return dict(centered_coefficients=rows,first_negative_orders=orders)

def milps():
    out=[]
    primes=[q for q in range(5,62) if all(q%d for d in range(2,math.isqrt(q)+1))]
    for q in primes:
        h=(q-1)//2
        for den in (4,8):
            k=max(1,math.floor(q/(2*den)+.5))
            C=2*np.cos(2*np.pi*np.outer(np.arange(1,h+1),np.arange(1,h+1))/q)
            model=gp.Model();model.Params.OutputFlag=0;model.Params.Threads=4
            model.Params.TimeLimit=12;model.Params.Seed=1914
            model.Params.MIPGap=0;model.Params.IntFeasTol=1e-9;model.Params.FeasibilityTol=1e-9
            x=model.addMVar(h,vtype=GRB.BINARY);K=model.addVar(lb=0)
            model.addConstr(x.sum()==k);model.addConstr(x[0]==1)
            model.addConstr(C@x+K>=0);model.setObjective(K,GRB.MINIMIZE);model.optimize()
            assert model.SolCount>0
            pairs=(np.flatnonzero(x.X>.5)+1).tolist()
            row=dict(target_density='1/'+str(den),q=q,pair_count=k,status=int(model.Status),
                     solver_bound=float(model.ObjBound),objective=float(model.ObjVal),
                     runtime=float(model.Runtime),certificate=certify(q,pairs))
            if q<=31:
                row['exact_optimum']=exact_optimum(q,k)
                lo,hi=row['exact_optimum']['K_integer_enclosure'];scale=1<<100
                assert abs(model.ObjVal-(lo+hi)/(2*scale))<1e-7
            out.append(row)
            (ROOT/'small_q_results.json').write_text(json.dumps(out,indent=2))
            print('ROW',q,den,k,row['status'],row['objective'],row['solver_bound'],flush=True)
    return out

def main():
    data=dict(python=platform.python_version(),numpy=np.__version__,gurobi=gp.gurobi.version(),
              arb_bits=ctx.prec,seed=1914,threads=4,per_model_time_limit=12,
              scope='All odd primes 5<=q<=61; cardinality 2*round(q/(2den)), at least 2, den=4,8')
    data['algebra']=algebra()
    (ROOT/'algebra_results.json').write_text(json.dumps(data,indent=2))
    rows=milps()
    print('COMPLETE',len(rows),'models',flush=True)

if __name__=='__main__':main()
