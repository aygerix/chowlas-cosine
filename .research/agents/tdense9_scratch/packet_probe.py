"""VM-only reproducible NUMERICAL probe of the weighted packet formal escape."""
import json,math
from pathlib import Path
import numpy as np
OUT=Path('.research/agents/tdense9_scratch')
def run():
    rng=np.random.default_rng(2026101909);rows=[]
    for alpha in (.5,.9):
        for X in (256,1024,4096):
            J=math.floor(X**alpha);th=rng.uniform(0,2*np.pi,J);c=1/math.sqrt(32*J)
            kk=np.arange(1,X+1);kap=1-kk/(X+1)
            rr=4*c*kap*(np.cos(np.outer(kk,th)).sum(axis=1))
            tt=kk/(X+1);ee=(1-tt)**2/4;pp=(1-np.sqrt(2*tt-tt*tt))/2;aa=pp+rr
            G=1<<math.ceil(math.log2(32*(X+1)));freq=np.zeros(G);freq[1:X+1]=rr/2;freq[-X:]=rr[::-1]/2
            g=np.fft.ifft(freq).real*G
            row=dict(X=X,J=J,alpha=alpha,seed=2026101909,c=c,analytic_lower_bound=-2*c*J,
                     analytic_lower_bound_full=-2*c*J-.25,min_g_grid=float(g.min()),max_g_grid=float(g.max()),
                     mean_r=float(rr.mean()),mean_r2=float(np.mean(rr*rr)),expected_mean_r2=float(ee.mean()),
                     mean_r3=float(np.mean(rr**3)),binary_required_mean_r3=float(np.mean(ee*(1-2*pp))),
                     coeffs_outside_unit_interval=int(np.count_nonzero((aa<0)|(aa>1))),frequency_count=X,
                     certificate='ANALYTIC GLOBAL LOWER BOUND; NUMERICAL GRID AND MOMENTS; NOT A BINARY SET')
            rows.append(row);print('PACKET',json.dumps(row),flush=True)
    OUT.joinpath('packet_probe.json').write_text(json.dumps(rows,indent=2))
if __name__=='__main__':run()
