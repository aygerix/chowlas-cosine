"""Independent exact sparse-window counts; no import of the constructor."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter,defaultdict
import json,math
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parent

def ball(z):return arb(z.numerator)/z.denominator

def independent(rec):
    q=rec['q'];m=rec['m'];s=2*m;t=Q(rec['t']);C=q*(t*t-Q(1,4));V=Q(q*q,4)+C
    ell=32*m;B=100*m;L2=C/(8*m)
    D=set(range(10*m+1,11*m+1));D|={-x for x in D}
    r=Counter(x-y for x in D for y in D);S=sorted(x for x in r if x>0)
    sq={'t':t*t,'L':L2};sites={0:'t',**{x:'L' for x in D}}
    j=1
    for d in S:
        lab='a'+str(d);sq[lab]=(C-r[d]*L2)/(2*ell)
        assert 0<sq[lab]<L2/4
        for k in range(j,j+ell):
            for x in (B*k,B*k+d,-B*k,-B*k-d):
                assert x not in sites;sites[x]=lab
        j+=ell
    # Independent short-window pair scan: counts all explicit point differences
    # up to max(S), rather than querying the constructor's membership partition.
    xs=sorted(sites);cc=defaultdict(Counter)
    for i,x in enumerate(xs):
        k=i+1
        while k<len(xs) and xs[k]-x<=max(S):
            d=xs[k]-x
            if d in r:cc[d][tuple(sorted((sites[x],sites[xs[k]])))]+=1
            k+=1
    for d in S:
        assert all(a==b for a,b in cc[d])
        val=sum(num*sq[a] for (a,b),num in cc[d].items())
        assert val==C,(q,m,d,val-C)
        expected=rec['core_sum_checks'][S.index(d)]['counts']
        assert {str(k):v for k,v in cc[d].items()}==expected
    multiplicities=Counter(sites.values());Q0=sum(num*sq[lab] for lab,num in multiplicities.items())
    vals={lab:ball(z).sqrt() for lab,z in sq.items()}
    M0=sum((num*vals[lab] for lab,num in multiplicities.items()),arb(0))
    T=ball(q*t)-M0;E=ball(V-Q0);n=rec['repair_sites'];mu=T/n;v=E/n-mu*mu
    assert n%4==0 and ball(Q(n-4,4))<3*T*T/(8*E) and 3*T*T/(8*E)<ball(Q(n,4))
    assert v>0 and v<mu*mu
    hi=mu+v.sqrt();lo=mu-v.sqrt();assert hi<vals['L']/2 and lo>0
    last=B*(j+n//2);assert last+B<q//2
    assert B-max(S)>max(S) and min(x for x in xs if x>11*m)-11*m>max(S)
    omitted_lower=E-2*(hi*hi+lo*lo-hi*lo)
    assert omitted_lower>ball(C)
    return {'q':q,'m':m,'exact_rational_sumset_equations':2*len(S),
            'exact_zero_energy_identity':True,'mass_repair_identity':True,
            'peak_levels_verified':True,'capacity_verified':True,
            'omitted_B_lower_over_q2':str(omitted_lower/(q*q))}

r=json.loads((ROOT/'adaptive_fake.json').read_text())
checks=[independent(v) for v in r['records']]
a=json.loads((ROOT/'adversaries.json').read_text())['records']
genuine=[v for v in a if 'fake' not in v['name']]
print('Independent fake verification:',checks,flush=True)
print('Genuine cases:',len(genuine),'max core-sum relative error:',max(v['core_sum_relative_error'] for v in genuine),flush=True)
print('Max Mellin transform error:',max(v['gauss_transform_error'] for v in a),flush=True)
print('Max Hasse-Davenport error:',max(v['hasse_davenport_error'] for v in a),flush=True)
print('SELECTED ADVERSARIES',flush=True)
selected={('small_enumeration_candidate',17),('small_enumeration_candidate',37),('E41_stored',61),('E41_stored',89),
          ('E90_stored_candidate',149),('E90_stored_candidate',601),('Paley',65537),('R13_PK_repaired',65537),
          ('R14_UNION_repaired',65537),('R12_S_weighted_fake',1000033),('R15_B3_scalar_fake',1000033)}
for v in a:
    if (v['name'],v['q']) in selected:
        print(json.dumps({k:v[k] for k in ['name','q','epsilon','core_size','core_energy_fraction','core_core_fraction_mean',
             'core_sum_relative_error','mellin_max_coefficient','mellin_required_count','mellin_effective_count',
             'boolean_mellin_quadratic_error','boolean_square_residual']}),flush=True)
(ROOT/'verification.json').write_text(json.dumps({'status':'PROVED_EXACT_SUPPORT_COUNTS_AND_ARB_LEVELS',
  'bits':ctx.prec,'independent_fake_checks':checks,'genuine_numerical_cases':len(genuine),
  'max_genuine_sumset_relative_error':max(v['core_sum_relative_error'] for v in genuine),
  'max_gauss_transform_error':max(v['gauss_transform_error'] for v in a),
  'max_hasse_davenport_error':max(v['hasse_davenport_error'] for v in a)},indent=2))
