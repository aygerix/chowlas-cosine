from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
exec(open(str(HERE / 'w2_anneal.py')).read().split('best=(0,None)')[0])
rng=np.random.default_rng(6528)
sets=[json.load(open(str(REPO / 'examples/dense_runs/X30_s0.json')))['A']]
sets += [r['A'] for r in json.load(open(str(REPO / 'examples/construct/N50_certified.json'))).values() if 'A' in r][:3]
for init in sets:
 A=set(init);X=max(A)+4;n=len(A);score,k,w=calc(A);best=score
 print(json.dumps(dict(kind='initial',n=n,X=X,rho=score,K=k,W=w,A=sorted(A))),flush=True)
 for i in range(5000):
  old=int(rng.choice(list(A)));new=int(rng.integers(1,X+1))
  if new in A:continue
  B=(A-{old})|{new};sc,k,w=calc(B);temp=.005*(1-i/5000)+.00005
  if sc>score or rng.random()<np.exp((sc-score)/temp):A=B;score=sc
  if sc>best:
   best=sc;print(json.dumps(dict(kind='best',step=i,n=n,X=X,rho=sc,K=k,W=w,A=sorted(B))),flush=True)
 print('DONE',n,X,best,flush=True)
