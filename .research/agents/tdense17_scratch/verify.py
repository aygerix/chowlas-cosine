"""Independent finite audits, exact profile checks, tables. VM only."""
import itertools
import json
import math
from pathlib import Path
import sys

import flint
import numpy as np
from scipy.linalg import eigvalsh

sys.path.insert(0,'src')
sys.path.insert(0,'.research/agents/tdense17_scratch')
from chowla import min_estimate_fft
from probe import spline_prob

ROOT=Path('.research/agents/tdense17_scratch')


def main():
    exact=0
    for L in range(2,40):
        a,p,Q=spline_prob(L)
        g={j:L-abs(j) for j in range(-L+1,L)}
        for v,pp in zip(a,p):
            r=sum(z*g.get(j+int(v),0) for j,z in g.items())
            if v<=L:
                formula=Q-L*int(v)**2+(int(v)**3-int(v))//2
            else:
                d=2*L-int(v); formula=(d**3-d)//6
            assert r==formula
            assert 0<=r<=Q
            assert 2*(Q-r)<=2*L*int(v)**2
            exact+=1
    # Independent, elementary all-circle certificate: Arb grid + global second derivative.
    A=np.load(ROOT/'spline_L4096_s17_p5_6.npz')['A'].tolist()
    flint.ctx.prec=140
    G=1<<18
    B=80
    vals=[flint.acb(0)]*G
    for a in A: vals[a]=flint.acb(1)
    F=flint.acb.dft(vals)
    S2=sum(a*a for a in A)
    remainder=flint.arb(S2)*flint.arb(22)**2/(2*49*G*G)
    # At a global minimizer f'=0; Taylor to its nearest grid point incurs <=remainder.
    passed=all(z.real+B-remainder>0 for z in F)
    assert passed
    est=min_estimate_fft(A,oversample=32,polish=32)
    xx=flint.arb(str(est.xmin))
    point=sum((xx*a).cos() for a in A)
    certificate=dict(M_upper_integer=B, clique_size=1025,
                     rigorous_ratio_lower='1025/160 = 6.40625',
                     grid=G, precision_bits=140, sum_a2=S2,
                     remainder=str(remainder), point_value=str(point), passed=passed,
                     method='Arb DFT; nearest global minimum, f-prime=0, global sum(a^2) Taylor bound; pi<22/7')
    print(json.dumps(certificate),flush=True)
    # Cross-check exact additive counts by explicit closed walks for all nonempty A in [1,7].
    moment_cases=0
    for bits in range(1,1<<7):
        aa=[j+1 for j in range(7) if bits>>j&1]
        aset=set(aa)
        H=np.array([[int(abs(x-y) in aset) for y in aa] for x in aa],dtype=np.int64)
        t2=sum(abs(x-y) in aset for x in aa for y in aa)
        t3=sum(abs(x-y) in aset and abs(y-z) in aset and abs(z-x) in aset
               for x in aa for y in aa for z in aa)
        common={(x,z):sum(abs(x-y) in aset and abs(z-y) in aset for y in aa)
                for x in aa for z in aa}
        t4=sum(v*v for v in common.values())
        assert t2==int(np.trace(H@H))
        assert t3==int(np.trace(H@H@H))
        assert t4==int(np.trace(H@H@H@H))
        w=eigvalsh(H.astype(float))
        for tau in (0.1,1.,math.sqrt(len(aa)),10.):
            low=w[w<=tau]
            mu=float(low.mean()); var=float(low.var())
            assert -w[0]+1e-8 >= var/(tau+abs(mu))+abs(mu)
        moment_cases+=1
    # Translates of the explicit obstruction, including overlaps and a distant translate.
    uniform=[]
    for m in (24,96,192):
        aa=np.arange(m+1,3*m+1)
        for t in (0,1,m,2*m,10*m):
            W=np.union1d(aa,aa+t)
            H=((np.abs(W[:,None]-W[None,:])>m)&(np.abs(W[:,None]-W[None,:])<=3*m)).astype(float)
            w=eigvalsh(H)
            rec=dict(m=m,t=t,vertices=len(W),
                     beta1=float(np.sum(w[np.abs(w)<=math.sqrt(2*m)]**2)/(2*m)**2),
                     psd_distance_per_vertex=float(np.linalg.norm(w[w<0])/len(W)))
            uniform.append(rec)
    (ROOT/'verification.json').write_text(json.dumps(dict(exact_profile_checks=exact,
        exact_moment_sets=moment_cases, independent_certificate=certificate,
        translated_intervals=uniform, flint_version=flint.__version__),indent=2)+'\n')
    # Tables are generated on the VM; local work only inserts the returned markdown.
    zoo=json.load(open(ROOT/'zoo.json'))['records']
    lines=['## Adversarial tables','',
           'NUMERICAL unless a separate exact or interval certificate is explicitly stated. Density alpha is tr(H²)/n² (including the diagonal normalization). B1 and B2 are the spectral energies inside sqrt(n) and 2sqrt(n), divided by n². Dpsd is the Frobenius distance to the PSD cone divided by n. BD is the truncated Bhatia–Davis bound at tau=sqrt(n), divided by sqrt(n).','',
           '| family | n | R est | alpha | B1 | B2 | Dpsd | −min eig / sqrt n | star | BD |',
           '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    for d in zoo:
        keys=['R_est','alpha','beta1','beta2','psd_distance','min_over_sqrtn','star_min_over_sqrtn','bd_over_sqrtn']
        lines.append('| '+d['name']+' | '+str(d['n'])+' | '+' | '.join(f'{d[k]:.5g}' for k in keys)+' |')
    lines += ['', 'NUMERICAL moment and rank audit. T3=tr(H³)/n³, T4=tr(H⁴)/n⁴, C4res=(tr(H⁴)−lambda_max^4)/n³. The effective rank is (tr P)²/tr(P²); traceP is tr(P)/n^(3/2). Qneg is sum_negative lambda² divided by n K_est². Raw integer counts and cutoff mean/variance for every row are in zoo.json.', '',
              '| family | T3 | T4 | C4res | eff rank | traceP | Qneg |',
              '|---|---:|---:|---:|---:|---:|---:|']
    for d in zoo:
        keys=['tr3_n3','tr4_n4','residual4_n3','r_eff','traceP_n32','neg_energy_over_nK2']
        lines.append('| '+d['name']+' | '+' | '.join(f'{d[k]:.5g}' for k in keys)+' |')
    lines += ['', 'NUMERICAL clique lower bounds. Clique membership and all pair differences are checked exactly. These are heuristic lower bounds for the clique number, not maximum-clique certificates. The column +0 extends the clique by the common neighbor 0; K_est is an uncertified minimum estimate.','',
              '| family | clique in S | with 0 | K est | (with 0)/K est |',
              '|---|---:|---:|---:|---:|']
    for d in json.load(open(ROOT/'cliques.json')):
        lines.append(f"| {d['name']} | {d['omega_S_lower']} | {d['omega_global_lower']} | {d['K_est']:.7g} | {d['omega_global_over_K_est']:.7g} |")
    lines += ['', 'NUMERICAL and separately certified profile examples. All listed ratios use a known clique; global clique maxima were not computed.','',
              '| L | forced prefix | seed | n | clique | M est | clique/K est | certified ratio lower |',
              '|---|---:|---:|---:|---:|---:|---:|---:|']
    for d in json.load(open(ROOT/'probe.json')):
        if d['test']!='forced_spline': continue
        bound=d.get('certified_omega_over_K_lower')
        lines.append(f"| {d['L']} | {d['forced_prefix']} | {d['seed']} | {d['n']} | {d['omega_lower']} | {d['M_est']:.8g} | {d['omega_over_K_est']:.8g} | {bound if bound is not None else '—'} |")
    (ROOT/'tables.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps(dict(exact_profile_checks=exact,exact_moment_sets=moment_cases,
                         translated_interval_cases=len(uniform),tables='tables.md')),flush=True)


if __name__=='__main__': main()
