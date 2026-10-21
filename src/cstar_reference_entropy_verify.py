"""Independent scalar cubics and exhaustive small reference frontiers.

All computation on Dirichlet. Exact enumeration replaces optimizer
optimality claims for the stated p11 reference classes only.
"""
from collections import Counter
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path
import socket
import flint


def positive(w):return w[0]>0 or (w[0]==0 and w[1]>0)


def spectrum(P):
    S={(x-u,y-v) for x,y in P for u,v in P if (x,y)!=(u,v)}
    assert len(S)==len(P)*(len(P)-1)
    return S


def scalar_moments(P,Q,p):
    base=6*p+1;pts=[x+base*y for x,y in P];refs=[x+base*y for x,y in Q]
    A={abs(x-y) for x,y in itertools.combinations(pts,2)};B={abs(x-y) for x,y in itertools.combinations(refs,2)}
    n=len(P)*(len(P)-1)//2;assert len(A)==len(B)==n and 0 not in A|B
    q={}
    for S,c in [(A,1),(B,-1)]:
        for x in S:
            for sign in [-1,1]:q[sign*x]=q.get(sign*x,0)+c
    q={x:c for x,c in q.items() if c};a=2*len(A-B);norm=sum(c*c for c in q.values())
    r=max(map(abs,q));coeff=[q.get(j-r,0) for j in range(2*r+1)]
    product=flint.fmpz_poly(coeff)**2
    H=2*sum(int(product[x+2*r]) for x in A if x<=2*r)
    return a,norm,H,A


def exhaustive(P,p,g):
    assert p==11
    k=len(P);n=k*(k-1)//2;cap=3*n//4
    A=spectrum(P);freq=[(x,y) for x in range(p) for y in range(-p+1,p) if positive((x,y))]
    fi={w:i for i,w in enumerate(freq)}
    abits=sum(1<<fi[w] for w in A if positive(w))
    conv=Counter((a+c,b+d) for a,b in A for c,d in A);H0=sum(conv[w] for w in A)
    lin=[-4*conv[w] for w in freq];ms=[];md=[]
    for w in freq:
        ms.append(sum(1<<j for j,v in enumerate(freq) if (w[0]+v[0],w[1]+v[1]) in A))
        md.append(sum(1<<j for j,v in enumerate(freq) if (w[0]-v[0],w[1]-v[1]) in A))
    allpoints=[(x,y) for x in range(p) for y in range(p)]
    classes={};pair={}
    for i,(x,y) in enumerate(allpoints):
        for j in range(i):
            a,b=allpoints[j];dx=x-a;dy=y-b
            w=(dx,dy) if positive((dx,dy)) else (-dx,-dy)
            r=(dx%p)*p+dy%p;s=((-dx)%p)*p+(-dy)%p;c=min(r,s)
            if c not in classes:classes[c]=len(classes)
            pair[i,j]=pair[j,i]=(1<<classes[c],1<<fi[w])
    counts=Counter((g*x//p,g*y//p) for x,y in P)
    cells=[];raw=1
    for cell,count in sorted(counts.items()):
        candidates=[i for i,(x,y) in enumerate(allpoints) if (g*x//p,g*y//p)==cell]
        cells.append((candidates,count));raw*=math.comb(len(candidates),count)
    frontier={};cyclic=0;macro=0;distinct=set();minoverlap=n
    def dfs(depth,chosen,used,bits):
        nonlocal cyclic,macro,minoverlap
        if depth==len(cells):
            cyclic+=1;ov=(bits&abits).bit_count();minoverlap=min(minoverlap,ov)
            if ov>cap:return
            macro+=1;distinct.add(bits);a=2*(n-ov);H=H0;t=bits
            while t:
                low=t&-t;i=low.bit_length()-1;t-=low
                H+=lin[i]+2*((ms[i]&bits).bit_count()+(md[i]&bits).bit_count())
            if a not in frontier or H<frontier[a][0]:frontier[a]=(H,chosen[:])
            return
        candidates,count=cells[depth]
        for combo in itertools.combinations(candidates,count):
            new=chosen[:];u=used;b=bits;valid=True
            for i in combo:
                for j in new:
                    c,f=pair[i,j]
                    if u&c:valid=False;break
                    u|=c;b|=f
                if not valid:break
                new.append(i)
            if valid:dfs(depth+1,new,u,b)
    dfs(0,[],0,0)
    rows=[]
    for a,(H,chosen) in sorted(frontier.items()):
        Q=2*a
        root=2*a*a/(H+math.sqrt(H*H+4*Q*a*a)) if H>=0 else (-H+math.sqrt(H*H+4*Q*a*a))/(2*Q)
        lower=F(max(0,math.floor(root*10**8)-2),2*10**8)
        assert Q*(2*lower)**2+H*(2*lower)-a*a<0
        rows.append(dict(a=a,Q=Q,H_min=H,margin_twice=2*a*a-k*H-k*k*a,
                         global_M_lower=str(lower),points=[allpoints[i] for i in chosen]))
    return dict(p=p,grid=g,raw_profile_point_sets=raw,cyclic_sidon_point_sets=cyclic,
                macro_turnover_point_sets=macro,distinct_macro_difference_sets=len(distinct),
                minimum_overlap=minoverlap,frontier=rows,
                optimal_margin_twice=max((r['margin_twice'] for r in rows),default=None),
                exhaustive=True)


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    root=Path('.research/experiments/reference_entropy_2026-10-20')
    data=json.loads((root/'results.json').read_text());fine=json.loads((root/'fine.json').read_text())
    miqp=json.loads((root/'miqp.json').read_text());out=[];catalog={};witnesses=0
    for row in data['cases']+fine['cases']:
        p=row['p'];g=row['grid'];P=list(map(tuple,row['actual_points']));k=len(P)
        assert P==[(t,t*t%p) for t in row['actual_t_indices']]
        counts=Counter((g*x//p,g*y//p) for x,y in P)
        for ref in row['references']:
            Q=list(map(tuple,ref['points']));assert len(Q)==k
            assert Counter((g*x//p,g*y//p) for x,y in Q)==counts
            assert len({((x-u)%p,(y-v)%p) for x,y in Q for u,v in Q if (x,y)!=(u,v)})==k*(k-1)
            a,norm,H,A=scalar_moments(P,Q,p)
            assert (a,norm,H)==(ref['a'],ref['Q'],ref['H'])
            assert len(A)-(a//2)==ref['integer_difference_overlap']<=row['overlap_cap']
            bound=2*F(ref['global_M_lower']);assert norm*bound*bound+H*bound-a*a<0
            witnesses+=1
        if p==11:
            result=exhaustive(P,p,g);result['label']=row['label'];catalog[row['label'],g]=result;out.append(result)
            assert bool(result['macro_turnover_point_sets'])==row['feasible']
            print(json.dumps({key:result[key] for key in ['label','grid','raw_profile_point_sets',
                  'cyclic_sidon_point_sets','macro_turnover_point_sets','optimal_margin_twice']}),flush=True)
    optimized=[]
    for row in miqp['cases']:
        P=list(map(tuple,row['actual_points']));Q=list(map(tuple,row['reference_points']));p=row['p'];g=row['grid']
        assert Counter((g*x//p,g*y//p) for x,y in P)==Counter((g*x//p,g*y//p) for x,y in Q)
        assert len({((x-u)%p,(y-v)%p) for x,y in Q for u,v in Q if (x,y)!=(u,v)})==len(Q)*(len(Q)-1)
        a,norm,H,A=scalar_moments(P,Q,p);assert (a,norm,H)==(row['a'],row['Q'],row['H'])
        assert 2*a*a-row['k']*H-row['k']**2*a==row['margin_twice']
        exact=catalog[row['label'],g]['optimal_margin_twice']
        assert row['margin_twice']<=exact
        bound=2*F(row['global_M_lower']);assert norm*bound*bound+H*bound-a*a<0
        optimized.append(dict(label=row['label'],grid=g,returned_margin=row['margin_twice'],
                              exact_optimum=exact,returned_is_exact_optimum=exact==row['margin_twice']))
    counter=json.loads((root/'counterfamily.json').read_text());counter_checks=[]
    def variance(blocks):
        I=[(F(i,3)+F(s,12),F(i,3)+F(s+1,12)) for i,s in enumerate(blocks)]
        rho=sum(b-a for a,b in I);mu=sum((b*b-a*a)/2 for a,b in I)/rho
        return sum((b**3-a**3)/3 for a,b in I)/rho-mu*mu
    assert variance(counter['reference_blocks'])-variance(counter['actual_blocks'])==F(1,9)
    for row in counter['cases']:
        p=row['p'];P=list(map(tuple,row['actual']));Q=list(map(tuple,row['reference']))
        cells={}
        for t in range(p):cells.setdefault((3*t//p,3*(t*t%p)//p),[]).append((t,t*t%p))
        actual=[];reference=[]
        for (i,j),C in sorted(cells.items()):
            C.sort();m=len(C)//4;s=counter['actual_blocks'][i];r=counter['reference_blocks'][i]
            actual.extend(C[s*m:(s+1)*m]);reference.extend(C[r*m:(r+1)*m])
        assert P==actual and Q==reference
        assert Counter((3*x//p,3*y//p) for x,y in P)==Counter((3*x//p,3*y//p) for x,y in Q)
        A=spectrum(P);B=spectrum(Q);assert not(A&B) and not(set(P)&set(Q))
        if p<=251:
            a,norm,H,_=scalar_moments(P,Q,p);assert (a,norm,H)==(row['a'],row['Q'],row['H'])
        lower=2*F(row['global_M_lower']);assert row['Q']*lower*lower+row['H']*lower-row['a']**2<0
        counter_checks.append(dict(p=p,profile_and_disjointness=True,independent_scalar_cubic=p<=251))
    result=dict(status='PASS',host=socket.gethostname(),scalar_cubic_witnesses=witnesses,
                exhaustive_profiles=out,miqp_exact_comparisons=optimized,counterfamily=counter_checks,
                qualification='Exhaustive optima only for the stated p11 profile families; '
                              'counter cubics independently recounted through p251 only.')
    (root/'verification.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
