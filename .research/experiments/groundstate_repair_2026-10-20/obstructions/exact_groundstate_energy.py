"""Exact counterexample to ||Dq||_2^2 >= |S| for a W1 groundstate."""
import sympy as s
phi=(1+s.sqrt(5))/2
I=list(range(-2,3));B=s.Matrix([[int(0<abs(i-j)<=2) for j in I]for i in I])
v=s.Matrix([1,-phi,0,phi,-1]);assert all(s.simplify(x)==0 for x in B*v+phi*v)
E=s.Matrix([[phi,s.sqrt(2),s.sqrt(2)],[s.sqrt(2),phi+1,1],[s.sqrt(2),1,phi]])
minors=[s.simplify(E[:k,:k].det()) for k in [1,2,3]]
assert minors==[phi,s.sqrt(5),3-s.sqrt(5)]
r=[sum(v[j] for j in range(5) if 0<=i-j<5 and i-j!=2)for i in range(9)]
energy=s.simplify(sum(x*x for x in r)/v.dot(v));assert energy==3
print('Unique bottom eigenvalue:',-phi)
print('Even shifted-block leading minors:',minors)
print('Exact normalized ||Dq||^2:',energy,'< N=4')
print('Exact R:',s.simplify(energy-phi**2))
