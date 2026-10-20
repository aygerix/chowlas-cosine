from itertools import combinations
from math import comb
import numpy as np

def sphere(r,k):
 out=[]
 for P in combinations(range(r),k):
  for M in combinations([j for j in range(r)if j not in P],k):
   v=np.zeros(r,dtype=np.int8);v[list(P)]=1;v[list(M)]=-1;out.append(v)
 return np.array(out)
for r,k in [(4,1),(6,2),(7,2),(9,3)]:
 S=sphere(r,k);s=S[0];N=len(S);same=((S==s)&(S!=0)).sum(1);opp=((S==-s)&(S!=0)).sum(1);overlap=((S!=0)&(s!=0)).sum(1)
 adj=(same==k)&(opp==0);g=np.array([comb(int(j),k)if j>=k else 0 for j in same]);err=g-adj
 F=sum(comb(k,a)**3 for a in range(k+1));D=comb(r-2*k,k)*F
 assert N==comb(r,k)*comb(r-k,k)
 assert sum(adj)==D
 assert np.all(err>=0)
 assert np.all(overlap[err!=0]>=k+1)
 Q=sum(comb(k,a)**2*comb(r-k,k-a)*comb(r-2*k+a,a)for a in range(k+1))
 assert sum(g)==Q
 print({'r':r,'k':k,'N':N,'F':F,'D':D,'exact_error_row_sum':int(sum(err))})
 if N<300:
  same2=((S[:,None,:]==S[None,:,:])&(S[:,None,:]!=0)).sum(2);opp2=((S[:,None,:]==-S[None,:,:])&(S[:,None,:]!=0)).sum(2);A=((same2==k)&(opp2==0)).astype(float);G=np.vectorize(lambda j:comb(int(j),k)if j>=k else 0)(same2)
  print('lambda_min(G)',np.linalg.eigvalsh(G)[0], 'lambda_min(A)',np.linalg.eigvalsh(A)[0])
print('All exact counting assertions passed.')
