"""Varying-marginal cone leakage and exact Boolean line quantization.

Run on Dirichlet. This is an L2 obstruction, never a sign conclusion.
"""
from fractions import Fraction as F
import itertools
import json
import math
from pathlib import Path
import socket
import numpy as np
from cstar_cone_confinement import coordinates


def quantization(p):
    l=len(p);ordered=sorted(p,reverse=True);total=sum(p);squares=sum(x*x for x in p)
    prefix=F(0);values=[]
    for k in range(l+1):
        if k:prefix+=ordered[k-1]
        values.append(squares+k-2*prefix-(k-total)**2/l)
    return min(values)


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Run through src/dirun.sh')
    rng=np.random.default_rng(20261024)
    out=dict(qualification='Exact coefficient-integrality leakage bounds; '
             'no inference of a negative value from L2 leakage alone.',seed=20261024,
             line_tests=[],cone_tests=[])
    for l in range(2,9):
        for case in range(12):
            p=[F(int(z),20) for z in rng.integers(0,21,size=l)]
            predicted=quantization(p)
            exhaustive=min(sum((F(bit)-x)**2 for bit,x in zip(bits,p))
                           -sum((F(bit)-x for bit,x in zip(bits,p)),F(0))**2/l
                           for bits in itertools.product([0,1],repeat=l))
            pair_bound=sum((min(abs(x-y),1-abs(x-y))**2
                            for i,x in enumerate(p) for y in p[i+1:]),F(0))/l
            assert predicted==exhaustive and predicted>=pair_bound
            if max(p)-min(p)<=F(1,2):
                assert predicted==sum(x*x for x in p)-sum(p)**2/l
            out['line_tests'].append(dict(p=list(map(str,p)),minimum=str(predicted),
                                         pair_lower=str(pair_bound),verified=True))
    for prime in [5,7]:
        points,cells=coordinates(prime);d=len(points)-1
        diff=(points[:,None,:]-points[None,:,:])%prime
        B=prime*prime*np.eye(len(points),dtype=np.int64)+prime*((diff[:,:,0]*diff[:,:,3]-diff[:,:,1]*diff[:,:,2])%prime==0)-1
        for name in ['scalar_tent','central_radial']:
            p=[F(0)]
            for i,M in enumerate(points[1:],1):
                if name=='scalar_tent':
                    z=(i-1)%(prime-1)+1;z=min(z,prime-z)
                    p.append(F(prime-2*z,2*prime))
                else:
                    norm=sum(min(int(z),prime-int(z))**2 for z in M)
                    p.append(F(prime*prime-norm,2*prime*prime))
            D=sum((quantization([p[i] for i in line]) for line in cells),F(0))
            assert D>0
            assert all(max(p[i] for i in cell)-min(p[i] for i in cell)<=F(1,2) for cell in cells)
            masks={name:np.zeros(len(points),dtype=np.int64)
                   for name in ['zero','threshold','one_ruling','seeded_even']}
            for i in range(1,len(points)):
                masks['threshold'][i]=int(p[i]>=F(1,4))
                masks['one_ruling'][i]=int((i-1)//(prime-1)<prime+1)
            for cell in cells:
                for j in range((prime-1)//2):
                    if rng.random()<.5:
                        masks['seeded_even'][cell[j]]=masks['seeded_even'][cell[-1-j]]=1
            for mask_name,eta in masks.items():
                denominator=math.lcm(*(z.denominator for z in p))
                E=np.array([int((F(int(bit))-z)*denominator) for bit,z in zip(eta,p)],dtype=np.int64)
                energy=F(int(E@E),denominator**2)
                inside=F(int(E@B@E),prime**3*denominator**2)
                leakage=energy-inside;bound=(1-F(1,prime))*D
                assert leakage>=bound
                ambient=np.zeros((prime,)*4)
                for M,z in zip(points,E):ambient[tuple(M)]=int(z)/denominator
                fft=np.fft.fftn(ambient,norm='ortho')
                fft_inside=sum(abs(fft[tuple(M)])**2 for M in points)
                assert abs(float(inside)-float(fft_inside))<1e-8
                row=dict(prime=prime,profile=name,selector=mask_name,
                         profile_values=list(map(str,p)),mask_hex=hex(sum(1<<i for i,b in enumerate(eta) if b)),
                         energy=str(energy),inside=str(inside),leakage=str(leakage),
                         quantization_sum=str(D),proved_lower=str(bound),verified=True)
                out['cone_tests'].append(row)
                print(json.dumps({k:row[k] for k in ['prime','profile','selector','leakage','proved_lower']}),flush=True)
    root=Path('.research/experiments/radial_boolean_2026-10-20');root.mkdir(parents=True,exist_ok=True)
    (root/'quantization.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
