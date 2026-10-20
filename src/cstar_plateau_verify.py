"""Independent stdlib integer verification of variable-coupling witnesses.

Uses signed Kronecker substitution and Python integer multiplication,
independently of FLINT polynomial multiplication in the producer.
Run on Dirichlet. This verifies algebraic lower certificates, not the
separate Arb DFT enclosures used for upper certificates.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import socket
from cstar_forced_plateau import correlation


def square_signed(coeff):
    max_bound=sum(abs(z) for z in coeff)**2
    width=(2*max_bound).bit_length()//8+1
    base=1<<(8*width)
    positive=int.from_bytes(b''.join(max(z,0).to_bytes(width,'little') for z in coeff),'little')
    negative=int.from_bytes(b''.join(max(-z,0).to_bytes(width,'little') for z in coeff),'little')
    packed=(positive-negative)**2
    size=2*len(coeff)-1
    digits=packed.to_bytes(size*width,'little')
    carry=0;result=[]
    for j in range(size):
        value=int.from_bytes(digits[j*width:(j+1)*width],'little')+carry
        if value>=base//2:
            value-=base;carry=1
        else:carry=0
        assert abs(value)<=max_bound
        result.append(value)
    assert carry==0
    return result


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run through src/dirun.sh')
    root=Path('.research/experiments/forced_plateau_2026-10-20')
    cases=json.loads((root/'results.json').read_text())['cases']
    noise=json.loads((root/'noise.json').read_text())['cases']
    # Direct convolution controls the signed encoding, including negative terms.
    example=[-5,7,-2,0,3,-1]
    direct=[sum(example[j]*example[k-j] for j in range(len(example))
                if 0<=k-j<len(example)) for k in range(2*len(example)-1)]
    assert square_signed(example)==direct
    out=dict(status='independent exact integer verification',cases=[])
    for row,certificate in zip(cases,noise):
        L,b,A=row['L'],row['b'],row['A'];X=L-2;N=2*len(A)
        assert len(set(A))==len(A) and min(A)>0 and max(A)<=X
        assert set(range(1,b+1)).issubset(A)
        E=(L**5-L)//30
        p=[E if a<=b else correlation(L,a) for a in range(1,X+1)]
        selected=set(A)
        c=[(E if a in selected else 0)-p[a-1] for a in range(1,X+1)]
        z=c[::-1]+[0]+c
        convolution=square_signed(z)
        Q=F(sum(v*v for v in z),E**2)
        H=F(2*sum(convolution[2*X+a] for a in A),E**2)
        fourth=F(sum(v*v for v in convolution),E**4)
        coupling=F(2*sum(c[a-1] for a in A),E)
        assert Q==F(certificate['norm_squared'])
        assert H==F(certificate['energy'])
        assert fourth==F(certificate['fourth_power'])
        assert coupling==F(certificate['coupling'])
        k=F(certificate['K_lower_rational'])
        determinant=k*k*Q+k*H-coupling*coupling
        assert determinant==F(certificate['negative_determinant'])<0
        prefix_bound=F(b**4,(b+1)*N*N)
        assert prefix_bound==F(row['completion_fourth_over_N2_lower'])
        upper=row['certificate'];grid=upper['grid']
        remainder=F(242*sum(a*a for a in A),49*grid*grid)
        assert remainder==F(upper['remainder'])
        assert upper['grid_M_upper_integer']+remainder==F(upper['M_upper_rational'])
        if row['t']==5:
            assert prefix_bound>128
            assert k*k>4*len(A)*F(3567,10000)**2
            assert F(upper['M_upper_rational'])**2<len(A)*F(729,500)**2
        out['cases'].append(dict(t=row['t'],n=len(A),verified=True,
                                 uniform_completion_128_obstructed=prefix_bound>128))
        print(json.dumps(out['cases'][-1]),flush=True)
    (root/'verification.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
