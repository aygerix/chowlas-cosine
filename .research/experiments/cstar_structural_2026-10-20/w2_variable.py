from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
exec(open(str(HERE / 'w2_anneal.py')).read().split('best=(0,None)')[0])
rng=np.random.default_rng(6530)
A=set([r['A'] for r in json.load(open(str(REPO / 'examples/construct/N50_certified.json'))).values() if 'A' in r][1]);X=80;score,k,w=calc(A);best=score
print(json.dumps(dict(kind='initial',n=len(A),X=X,rho=score,K=k,W=w,A=sorted(A))),flush=True)
for i in range(10000):
 if rng.random()<.5:
  t=int(rng.integers(1,X+1));B=A^{t}
 else:
  old=int(rng.choice(list(A)));new=int(rng.integers(1,X+1))
  if new in A:continue
  B=(A-{old})|{new}
 sc,k,w=calc(B);temp=.01*(1-i/10000)+.00002
 if sc>score or rng.random()<np.exp((sc-score)/temp):A=B;score=sc
 if sc>best:
  best=sc;print(json.dumps(dict(kind='best',step=i,n=len(B),X=X,rho=sc,K=k,W=w,A=sorted(B))),flush=True)
print('DONE',best,flush=True)
