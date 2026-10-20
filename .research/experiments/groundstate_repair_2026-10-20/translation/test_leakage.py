import itertools,numpy as np
best=(1e9,None)
best_low=(1e9,None)
for n in range(1,8):
 for A in itertools.combinations(range(1,13),n):
  S=set(A)|set(-a for a in A);I=sorted(S|{0}); W=sorted(set(a+b for a in I for b in I));N=len(S)
  B=np.array([[int(a-b in S)for b in I]for a in I],float)
  vals,vecs=np.linalg.eigh(B);k=-vals[0];q=vecs[:,0]
  h=np.array([sum(q[j]for j,b in enumerate(I)if a-b in S)+(k*q[I.index(a)]if a in I else 0)for a in W])
  ratio=(np.dot(h,h)+k*k)/N
  if ratio<best[0]:best=(ratio,(A,k,np.dot(h,h),N))
  if k/np.sqrt(N)<.9 and np.dot(h,h)/N<best_low[0]:best_low=(np.dot(h,h)/N,(A,k,np.dot(h,h),N))
print('best total second moment/N',best)
print('best leakage/N with k/sqrtN<.9',best_low)
