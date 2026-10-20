from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import json,time
records=json.load(open(str(REPO / 'examples/construct/N50_certified.json')))
A=[r['A'] for r in records.values() if 'A' in r][1]
S=set(A)|{-a for a in A};W=sorted({0}|S|{a+b for a in S for b in S});n=len(W)
p,q=353,50
B=[[p if i==j else q*int(W[i]-W[j] in S) for j in range(n)] for i in range(n)]
prev=1;mins=1;t=time.time();pivots=[]
for k in range(n):
 pivot=B[k][k];pivots.append(pivot)
 if pivot<=0:print('FAIL',k,pivot,flush=True);break
 if k%25==0: print('pivot',k,'digits',len(str(pivot)),'seconds',time.time()-t,flush=True)
 for i in range(k+1,n):
  for j in range(i,n):
   num=pivot*B[i][j]-B[i][k]*B[k][j]
   v,rem=divmod(num,prev)
   assert rem==0
   B[i][j]=B[j][i]=v
 prev=pivot
else:
 result=dict(A=A,W_size=n,p=p,q=q,K_upper=str(p/q),leading_principal_minors_all_positive=True,determinant=str(pivots[-1]),seconds=time.time()-t,rho_lower=2*len(A)*q*q/(p*p))
 json.dump(result,open(str(HERE / 'w2_exact_certificate.json'),'w'),indent=2)
 print('CERTIFIED',json.dumps(result),flush=True)
