"""Independent exact checks of full-space witness and subspace separation."""
from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path
import socket
import flint


def auto(P):
    out=Counter(x-y for x in P for y in P);del out[0];return out


def bareiss_reverse(M):
    M=[row[::-1] for row in M[::-1]];prev=1;pivots=[]
    for k in range(len(M)):
        pivot=M[k][k];assert pivot>0;pivots.append(pivot)
        for i in range(k+1,len(M)):
            for j in range(i,len(M)):
                val,rem=divmod(pivot*M[i][j]-M[i][k]*M[k][j],prev);assert rem==0
                M[i][j]=M[j][i]=val
        prev=pivot
    return pivots


def rational_psd(M):
    M=[[F(t) for t in row] for row in M[::-1]];M=[row[::-1] for row in M];pivots=[]
    while M:
        p=M[0][0];assert p>0;pivots.append(p)
        M=[[M[i][j]-M[i][0]*M[0][j]/p for j in range(1,len(M))] for i in range(1,len(M))]
    determinant=F(1)
    for p in pivots:determinant*=p
    return determinant


def check_upper(A,B):
    x=flint.fmpz_poly([0,1]);T0=flint.fmpz_poly([1]);T1=x;f=flint.fmpz_poly([0])
    for j in range(1,max(A)+1):
        if j in A:f+=T1
        T0,T1=T1,2*x*T1-T0
    poly=flint.fmpq_poly(list(B.denominator*f+B.numerator));seq=[poly,poly.derivative()]
    while len(seq[-1])>1:
        r=-(seq[-2]%seq[-1])
        if len(r)==0:break
        seq.append(r)
    def variations(t):
        values=[p(t) for p in seq];signs=[1 if v>0 else -1 for v in values if v]
        return sum(a!=b for a,b in zip(signs,signs[1:]))
    assert poly(-1)>0 and poly(1)>0 and poly(0)>0 and variations(-1)==variations(1)
    return len(seq)


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    root=Path('.research/experiments/resolvent_2026-10-20');data=json.loads((root/'results.json').read_text())
    A=data['actual'];n=data['n'];assert A==sorted(set(A)) and len(A)==n and max(A)==data['max_A']
    S=set(A)|{-a for a in A};X=max(A);cap=data['full_W2_cap']
    W=sorted({0}|S|{s+t for s in S for t in S});assert W==cap['rows']
    M=[[15*int(i==j)+2*int(x-y in S) for j,y in enumerate(W)] for i,x in enumerate(W)]
    pivots=bareiss_reverse(M);assert pivots[-1]==cap['charpoly_of_negative_matrix'][0]
    assert all(t>0 for t in cap['charpoly_of_negative_matrix'])
    rows=[{s:1 for s in S}]
    for j in range(1,n+1):
        r=Counter(auto([0]+A[:j]))
        for w,c in auto([0]+A[:j-1]).items():r[w]-=c
        rows.append({w:c for w,c in r.items() if c})
    poly=[flint.fmpz_poly([r.get(k-X,0) for k in range(2*X+1)]) for r in rows]
    Q=[];H=[]
    for p in poly:
        qq=[];hh=[]
        for q in poly:
            prod=p*q;qq.append(int(prod[2*X]));hh.append(2*sum(int(prod[2*X+a]) for a in A))
        Q.append(qq);H.append(hh)
    a=[sum(r.get(s,0) for s in S) for r in rows];dual=data['prefix_dual']
    den=dual['denominator'];lp=dual['lambda_numerator'];ep=dual['eta_numerator'];assert lp>=0
    M=[[den*H[i][j]+lp*Q[i][j]-ep*a[i]*a[j] for j in range(len(rows))] for i in range(len(rows))]
    determinant=rational_psd(M);assert determinant==dual['positive_leading_minors'][-1]
    lower=F(ep*n*n-lp*25*n,den);assert lower==F(dual['H_lower'])
    checks=[]
    for row in data['polynomials']:
        B=row['degree'];nums=row['positive_numerators'];den=row['denominator'];assert len(nums)==B
        coeff={j:c for k,c in enumerate(nums,1) for j in [-k,k] if c}
        q=sum(c*c for c in coeff.values())
        h=2*sum(sum(c*coeff.get(w+a,0) for w,c in coeff.items()) for a in A)
        assert (q,h)==(row['norm_numerator'],row['energy_numerator'])
        assert 2*sum(coeff.get(a,0) for a in A)==n*den and q<=25*n*den*den
        assert F(h,den*den)==F(row['H'])
        K=2*F(row['global_M_lower']);assert q*K*K+h*K-n*n*den*den<0
        strict=F(h,den*den)<lower;assert strict==row['strictly_below_prefix_dual']
        escape=K>F(cap['K_upper']);assert escape==row['exceeds_full_W2_K_cap']
        checks.append(dict(degree=B,a_equals_n=True,Q_at_most_25n=True,H=str(F(h,den*den)),
                           global_M_lower=row['global_M_lower'],below_prefix_dual=strict,above_W2_cap=escape))
    assert checks[-1]['below_prefix_dual'] and checks[-1]['above_W2_cap']
    assert 400*F(checks[-1]['global_M_lower'])**2>121*n
    assert 10**6*F(data['global_M_upper'])**2<571**2*n
    final=data['polynomials'][-1];K0=F(79,10);s=-F(n)/K0
    negative_form=K0*s*s+2*n*s+F(final['energy_numerator'],final['denominator']**2)+K0*F(final['norm_numerator'],final['denominator']**2)
    assert negative_form<0
    sturm=check_upper(A,F(data['global_M_upper']))
    # Analytic singleton resolvent at lambda=5/2 has q_k=-(-1/2)^k.
    singleton=[]
    for B in [2,4,8,16]:
        c={s:-F(-1,2)**abs(s) for s in range(-B,B+1) if s}
        Qs=sum(t*t for t in c.values());Hs=2*sum(t*c.get(w+1,0) for w,t in c.items())
        assert 2*c[1]==1 and Qs==F(2,3)*(1-F(1,4)**B)
        assert Hs==-F(2,3)*(1-F(1,4)**(B-1))
        singleton.append(dict(B=B,Q=str(Qs),H=str(Hs)))
    singer={0,1,3};diff=Counter(s-t for s in singer for t in singer if s!=t)
    assert len({d%7 for d in diff})==6 and diff[-1]==1 and diff[6]==0
    out=dict(status='PASS',host=socket.gethostname(),full_W2_rows=len(W),
             reversed_Bareiss_positive_pivots=len(pivots),full_W2_K_upper='15/2',
             prefix_dual_independent_rational_Schur=True,prefix_H_lower=str(lower),
             polynomials=checks,negative_form_at_K_79_over_10=str(negative_form),
             independent_Sturm_upper=data['global_M_upper'],Sturm_chain_length=sturm,
             singleton_formula_checks=singleton,
             screened_literature_identity_counterexample=dict(S=[0,1,3],q=7,c_minus1=1,c_qminus1=0,
                 scope='This invalidates the literal c_-l=c_(q-l) equality used in the screened source; '
                       'no general flatness theorem is assumed or globally adjudicated.'),
             qualification='Exact achieved certificates and whole-space upper bounds. Numerical resolvent '
                           'integrals, optimal lambda and full-space optimum remain uncertified diagnostics.')
    (root/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['status','full_W2_rows','prefix_H_lower','negative_form_at_K_79_over_10',
                                     'independent_Sturm_upper']}))


if __name__=='__main__':main()
