"""Independent arithmetic/spectral audit and density-union probe, VM only."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json, math, hashlib, platform
import numpy as np
from flint import arb,ctx
import pymupdf

ROOT=Path(__file__).resolve().parent
ctx.prec=256

def finite_audit():
    # Recheck every stored witness with the strengthened exact-tie validator;
    # do not repeat the MILP search.
    import check_round14
    rows=json.loads((ROOT/'small_q_results.json').read_text())
    checked=[];total=0;orbits=0
    for row in rows:
        q=row['q'];P=row['certificate']['pairs'];m=2*len(P)
        ctx.prec=256
        recert=check_round14.certify(q,P)
        assert arb(recert['K_ball']).overlaps(arb(row['certificate']['K_ball']))
        # Independently evaluate the full DFT using a cached cosine table.
        co=[(2*arb.pi()*j/q).cos() for j in range(q)]
        eig=[sum((co[(g*x)%q]+co[(-g*x)%q] for x in P),arb(0)) for g in range(q)]
        assert (eig[0]-m).contains(0)
        assert sum(eig,arb(0)).contains(0)
        assert (sum((x*x for x in eig),arb(0))-q*m).contains(0)
        i=min(range(1,q),key=lambda j:float(eig[j].mid()))
        k=-eig[i]
        assert k.overlaps(arb(row['certificate']['K_ball']))
        assert (k-1).lower()>0
        if 'exact_optimum' in row:
            total+=row['exact_optimum']['cases'];orbits+=row['exact_optimum']['dilation_orbits']
            e=row['exact_optimum'];scale=int(e['scale'])
            assert (k*scale-arb(e['K_integer_enclosure'][0])).lower()>0
            assert (arb(e['K_integer_enclosure'][1])-k*scale).lower()>0
        checked.append(dict(q=q,target=row['target_density'],cardinality=m,
                            K_ball_256=str(k),status=row['status']))
    return dict(models=len(rows),independent_DFT_checks=checked,
                exhaustive_cases_including_duplicate_cardinalities=total,
                exhaustive_orbits_including_duplicate_cardinalities=orbits,
                all_gurobi_status_optimal=all(r['status']==2 for r in rows))

def centered_orders():
    result=[]
    for m in range(3,101):
        t=Q(1,m-1)
        vals=[1-r*t-(r-t)*(-t)**(r-1) for r in range(2,2*m+1)]
        rmin=2+next(i for i,x in enumerate(vals) if x<0)
        assert rmin==(m-1 if m%2==0 else m)
        if m%2==0:
            a=Q(1,m);d=1-2*a;r=m-1
            A=((1-a)**r-(-a)**r)/d**(r-1)
            mu=(a*(1-a)**(r-1)+(1-a)*(-a)**(r-1))/d**(r-1)
            assert A-r*mu==-Q(1,(m-2)**(m-3))
        result.append(dict(alpha='1/'+str(m),first_negative=rmin))
    # Projected convolution is not associative, even on real even arrays.
    q=5;e1=[0,1,0,0,1];e2=[0,0,1,1,0]
    def op(x,y):
        z=[sum(x[j]*y[(i-j)%q] for j in range(q)) for i in range(q)]
        z[0]=0
        return z
    lhs=op(op(e1,e1),e2);rhs=op(e1,op(e1,e2))
    assert lhs==e1 and rhs==[e1[i]+2*e2[i] for i in range(q)]
    return dict(reciprocal_density_orders=result,projected_convolution=dict(q=q,left=lhs,right=rhs))

def unions():
    out=[]
    for q in (4093,65537,1048583):
        assert all(q%d for d in range(2,math.isqrt(q)+1))
        h=(q-1)//2;xs=np.arange(1,h+1)
        for den,eps in ((4,.125),(8,.1)):
            a=1/den;rng=np.random.default_rng(1400000+q+den)
            bit=rng.random(h)<a+eps*np.cos(2*np.pi*xs/q)
            k=math.floor(a*q/2+.5)
            if bit.sum()>k:bit[rng.choice(np.flatnonzero(bit),int(bit.sum()-k),replace=False)]=False
            elif bit.sum()<k:bit[rng.choice(np.flatnonzero(~bit),int(k-bit.sum()),replace=False)]=True
            b=np.zeros(q,dtype=np.int8);b[xs[bit]]=1;b[-xs[bit]]=1
            c=b|b[(3*np.arange(q))%q]
            F=np.fft.fft(b).real;Fc=np.fft.fft(c).real
            row=dict(q=q,alpha_target=a,epsilon=eps,seed=1400000+q+den,
                     cardinality_B=int(b.sum()),cardinality_C=int(c.sum()),
                     K_B_fft=float(-F[1:].min()),K_C_fft=float(-Fc[1:].min()),
                     C_lambda2_fft=float(Fc[2]),C_lambda2_leading=-eps*eps*q/4,
                     C_density=float(c.mean()),C_density_leading=2*a-a*a)
            P=xs[bit].tolist()
            if q<=65537:
                val=sum((2*(4*arb.pi()*int(x)/q).cos()
                         for x in np.flatnonzero(c[1:h+1])+1),arb(0))
                assert abs(float(val.mid())-Fc[2])<1e-8
                row['C_lambda2_Arb_256']=str(val)
            # The saved exact pair lists reproduce every probe.
            np.savez_compressed(ROOT/('union_q%d_den%d.npz'%(q,den)),pairs=np.array(P,dtype=np.int64))
            out.append(row)
            print('UNION',json.dumps(row),flush=True)
    return out

def render_source():
    doc=pymupdf.open(ROOT/'sanders_0807.5104v2.pdf')
    for page in (2,3,4,5,7,8,9):
        doc[page-1].get_pixmap(matrix=pymupdf.Matrix(1.5,1.5)).save(ROOT/('sanders_p%d.png'%page))

def main():
    result=dict(python=platform.python_version(),arb_bits=ctx.prec,
                finite_audit=finite_audit(),centered_orders=centered_orders(),unions=unions())
    result['Bu_constants']={str(C):str((arb(1)/(128*C*200000))**(arb(1)/4)) for C in (8,16,32)}
    render_source()
    (ROOT/'audit_results.json').write_text(json.dumps(result,indent=2))
    # Hash the exact source/data artifacts; exclude this hash manifest itself.
    files=sorted(p for p in ROOT.iterdir() if p.suffix in ('.py','.json','.npz','.pdf'))
    manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files if p.name!='manifest.json'}
    (ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2))
    print('AUDIT COMPLETE',len(manifest),'artifacts',flush=True)

if __name__=='__main__':main()
