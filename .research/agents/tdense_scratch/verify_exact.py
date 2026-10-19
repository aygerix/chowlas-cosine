"""Exact auxiliary checks for the paper proof; execute on VM only.

This script checks finite instances and rational constants. The report contains
the all-X proof; finite checks are not substituted for that proof.
"""
import json
from fractions import Fraction as F
from pathlib import Path

OUT = Path(".research/agents/tdense_scratch")


def quadratic(X, phase_num=0, phase_den=1):
    den = 2*X*X*phase_den
    acc = 2*X*X*phase_num
    old = acc//den
    a = [0]*(X+1)
    for j in range(1,X+1):
        acc += (X-j)**2*phase_den
        new = acc//den
        a[j] = new-old
        old = new
    return a


def check(X, phase_num=0, phase_den=1):
    a = quadratic(X,phase_num,phase_den)
    n = sum(a)
    assert all(v in (0,1) for v in a)
    assert all(a[j]+a[j+1]<=1 for j in range(X))
    def av(j):
        return a[abs(j)] if abs(j)<=X else 0
    B = [0]+[2*av(j)-av(j-2)-av(j+2) for j in range(1,X+3)]
    E = F(sum(b*b for b in B[1:]),4)
    w = X//100
    W = F(2*(w+1),3)+F(1,3*(w+1))
    S = F(sum(B[j]**2*(w+1-j)**2 for j in range(1,w+1)),4*(w+1)**2)
    C = F(811,1000)*(X+2+w+1)+F(71,300)
    lb2 = (W*E-C*S)/(2*(C-W))
    assert E>=F(X,16)-3
    # The bound with constant 7 is derived for phase 0; allow 2 for phase !=0.
    assert S<=F(X,5000)+9
    if phase_num==0:
        assert a[2]==0
        assert S<=F(X,5000)+7
        assert C<=F(7*X,8)
        coarse = F(29*X,210000)-F(1229,350)
        assert lb2>=coarse
        if X>=100000:
            assert coarse>=F(X,10000)
    return {"X":X,"phase":[phase_num,phase_den],"n":n,
            "E":str(E),"S":str(S),"C":str(C),"w":w,
            "transformed_M_squared_lower_bound":str(lb2),
            "transformed_M_squared_lower_bound_decimal":float(lb2),
            "finite_checks":"PASS"}


def main():
    rows = [check(X) for X in [100,384,1536,6144,20000,100000,150000]]
    rows += [check(6144,num,10) for num in [1,3,7,9]]
    # Exact arithmetic in the two constant estimates used in the proof.
    assert F(1,2400)-F(7,40000)==F(29,120000)
    assert F(29,120000)*F(4,7)==F(29,210000)
    assert (F(3,150)+F(49,8))*F(4,7)==F(1229,350)
    assert F(29,210000)-F(1,10000)==F(1,26250)
    assert F(1229,350)*26250==92175
    result = {"status":"EXACT FINITE CHECKS; all-X proof in report",
              "rows":rows,"constant_checks":"PASS"}
    (OUT/"verify_exact.json").write_text(json.dumps(result,indent=2))
    print(json.dumps(result),flush=True)


if __name__=="__main__":
    main()
