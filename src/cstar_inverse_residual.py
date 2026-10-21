"""Finite-band and full-L2 leverage certificates from a CG proposal.

Low K is established separately by an exact difference-square identity.
The inverse is not computed exactly: its residual bounds the error.
FLINT action, including its exterior tail, is independently checked using
two Python integer products. Only the full residual bounds full-L2 leverage.
"""
from fractions import Fraction as F
import argparse
import json
import math
from pathlib import Path
import socket

import flint
import numpy as np
from cstar_gpu_kernel import FourierCost
from cstar_l25_probe import rational_enclosure


def exact_twice_action(A,integers):
    X=max(A);B=len(integers)
    d=[0]*(2*X+1)
    for a in A:d[X-a]=d[X+a]=1
    w=integers[::-1]+[0]+integers
    product=flint.fmpz_poly(d)*flint.fmpz_poly(w)
    actual=[int(product[X+B+j]) for j in range(1,B+X+1)]
    total=sum(map(abs,w))*2*len(A)
    width=(total.bit_length()+7)//8
    assert total < 1<<(8*width)
    encoded_d=bytearray(len(d)*width)
    for j,v in enumerate(d):encoded_d[j*width]=v
    plus=bytearray(len(w)*width);minus=bytearray(len(w)*width)
    for j,v in enumerate(w):
        target=plus if v>=0 else minus
        target[j*width:(j+1)*width]=abs(v).to_bytes(width,'little')
    pd=int.from_bytes(encoded_d,'little')
    length=(len(d)+len(w)-1)*width
    pp=(pd*int.from_bytes(plus,'little')).to_bytes(length,'little')
    pm=(pd*int.from_bytes(minus,'little')).to_bytes(length,'little')
    independent=[]
    for j in range(1,B+X+1):
        lo=(X+B+j)*width;hi=lo+width
        independent.append(int.from_bytes(pp[lo:hi],'little')-int.from_bytes(pm[lo:hi],'little'))
    assert independent==actual
    return actual


def certificate(A,Kupper,label,expected=None,expected_full=None):
    n=len(A);B=2*max(A);assert Kupper*Kupper<=4*n
    op=FourierCost(A,list(range(1,B+1)))
    c=np.zeros(B);c[np.array(A)-1]=1
    def action(v):return op.apply(v)[0]+2*math.sqrt(n)*v
    w=np.zeros(B);r=c.copy();p=r.copy();rr=r@r;trace=[]
    for iteration in range(250):
        ap=action(p);alpha=rr/(p@ap);w+=alpha*p;r-=alpha*ap
        newrr=r@r;trace.append(float(math.sqrt(newrr/n)))
        if newrr<1e-20*n:break
        p=r+(newrr/rr)*p;rr=newrr
    else:raise RuntimeError('CG did not reach the proposal tolerance')
    scale=2**30;t=[int(round(x*scale)) for x in w]
    M_all=exact_twice_action(A,t)
    M=M_all[:B];M_tail=M_all[B:]
    ctimes=sum(t[a-1] for a in A)
    tM=sum(x*y for x,y in zip(t,M));t2=sum(x*x for x in t)
    support=set(A)
    residual=[2*scale*int(j+1 in support)-m for j,m in enumerate(M)]
    R2=sum(x*x for x in residual);Rt=sum(x*y for x,y in zip(residual,t))
    flint.ctx.prec=160;root=flint.arb(n).sqrt()
    E=2*flint.arb(ctimes)/scale-flint.arb(tM)/(2*scale*scale)-2*root*t2/(scale*scale)
    r2=(flint.arb(R2)/4-2*root*Rt+4*n*t2)/(scale*scale)
    assert r2>=0
    upper=E+r2/root
    tail_square=sum(x*x for x in M_tail)
    full_r2=r2+flint.arb(tail_square)/(4*scale*scale)
    full_upper=E+full_r2/root
    low,_=rational_enclosure(E);_,high=rational_enclosure(upper)
    ell_lo,_=rational_enclosure(E/root);_,ell_hi=rational_enclosure(upper/root)
    _,full_hi=rational_enclosure(full_upper)
    _,full_ell_hi=rational_enclosure(full_upper/root)
    assert ell_lo>F(1,140)
    if expected is not None:assert low<F(expected)<high
    if expected_full is not None:
        value=expected_full()
        assert E<value and value<full_upper
    return dict(label=label,A=A,n=n,band=B,K_upper_exact=str(Kupper),
                integer_w=t,denominator=scale,integer_twice_Cw=M,
                integer_twice_Cw_exterior=M_tail,
                aggregates=dict(ctimes=ctimes,tM=tM,t2=t2,R2=R2,Rt=Rt,
                                exterior_twice_action_square=tail_square),
                J_lower=str(low),J_upper=str(high),J_over_sqrt_n_lower=str(ell_lo),
                J_over_sqrt_n_upper=str(ell_hi),OP140_finite_certified=True,
                full_L2_J_lower=str(low),full_L2_J_upper=str(full_hi),
                full_L2_J_over_sqrt_n_lower=str(ell_lo),
                full_L2_J_over_sqrt_n_upper=str(full_ell_hi),
                full_residual_band=B+max(A),
                independent_python_action_match=True,CG_iterations=len(trace),
                numerical_relative_residual=trace[-1],precision_bits=160,
                qualification='Finite J uses interior residual; full-L2 J uses every residual frequency through B+X. Both conditional on separately proved lowK; no uniform OP140 claim.')


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    parser=argparse.ArgumentParser()
    parser.add_argument('--primes',default='31,127')
    parser.add_argument('--output',default='.research/experiments/l25_2026-10-21/inverse_residual.json')
    args=parser.parse_args();wanted={'p'+p for p in args.primes.split(',')}
    rows=json.loads(Path('.research/experiments/l25_2026-10-21/probe.json').read_text())['cases']
    inputs=[dict(label='singleton',A=[1],Kupper=F(2),expected=F(8,15),
                 expected_full=lambda:4-2*flint.arb(3).sqrt())]
    for row in rows:
        if row['label'].split('_')[-1] in wanted:
            B=row['metadata']['B'];A=sorted({abs(b-c) for b in B for c in B if b!=c})
            assert A==row['A'] and len(A)==len(B)*(len(B)-1)//2
            inputs.append(dict(label=row['label'],A=A,Kupper=F(len(B))))
    output=dict(host=socket.gethostname(),cases=[])
    path=Path(args.output)
    path.parent.mkdir(parents=True,exist_ok=True)
    for row in inputs:
        result=certificate(**row);output['cases'].append(result)
        path.write_text(json.dumps(output,indent=2)+'\n')
        print(json.dumps({k:result[k] for k in ['label','n','CG_iterations','J_over_sqrt_n_lower','J_over_sqrt_n_upper',
            'full_L2_J_over_sqrt_n_lower','full_L2_J_over_sqrt_n_upper','independent_python_action_match']}),flush=True)
    # A genuine non-Boolean countercontrol: D=Fejer_(X+1)-1>=-1,
    # weights 1-a/(X+1), effective n=sum weights². Its full-space
    # leverage upper bounds every finite band and is <=lambda/(lambda-1).
    X=120000;mass=F(X*(2*X+1),6*(X+1));root=(flint.arb(mass.numerator)/mass.denominator).sqrt()
    upper=4*root/(4*root-1)
    assert upper<root/140
    output['weighted_Fejer_countercontrol']=dict(Boolean=False,X=X,effective_n=str(mass),K_upper='1',L1_upper='2',
        full_space_J_upper=str(rational_enclosure(upper)[1]),
        fails_coefficient_relaxed_OP140=True,
        proof='For mean-zero q, J<=integral D²/(D+lambda)<=lambda/(lambda-1)*L1/2, lambda=4sqrt(effective_n).')
    path.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',output=str(path))),flush=True)


if __name__=='__main__':main()
