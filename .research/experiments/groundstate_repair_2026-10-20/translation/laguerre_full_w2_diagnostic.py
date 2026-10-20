from pathlib import Path
from math import factorial
from fractions import Fraction
import json
import numpy as np
from pathlib import Path

def triple(k,i,j):
 ans=0
 for d in range(min(k,i,j)+1):
  numer=[k+i-j-d,k+j-i-d,i+j-k-d]
  if min(numer)<0 or any(a%2 for a in numer): continue
  a,b,c=[v//2 for v in numer]
  ans+=factorial(a+b+c+d)*2**d//(factorial(a)*factorial(b)*factorial(c)*factorial(d))
 return ans

def poly(n):return [Fraction((-1)**(n+j)*factorial(n),factorial(n-j)*factorial(j)**2) for j in range(n+1)]
def mul(p,q):
 r=[Fraction(0)]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):r[i+j]+=a*b
 return r
for k in range(5):
 for i in range(5):
  for j in range(5):
   p=mul(mul(poly(k),poly(i)),poly(j));assert sum(c*factorial(a)for a,c in enumerate(p))==triple(k,i,j)
results=[]
for k in range(1,11):
 M=[[triple(k,i,j)for j in range(2*k+1)]for i in range(2*k+1)]
 vals,vecs=np.linalg.eigh(np.array(M,float));v=vecs[:,0];res=np.linalg.norm(np.array(M,float)@v-vals[0]*v)
 row={'k':k,'dimension':2*k+1,'lambda_min_float':float(vals[0]),'negative_min_float':float(-vals[0]),'residual_float':float(res),'norm_float':float(max(abs(vals))),'matrix_exact':M,'lowest_vector_float':v.tolist()}
 results.append(row);print(k, -vals[0], 'norm',max(abs(vals)), 'res',res)
Path(str(Path(__file__).resolve().parent / 'laguerre_full_w2_diagnostic.json')).write_text(json.dumps(results,indent=2))
