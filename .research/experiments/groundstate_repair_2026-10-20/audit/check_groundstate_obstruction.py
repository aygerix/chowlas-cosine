"""Independent finite checks; identities are proved in accompanying audit."""
import itertools, math, json
import numpy as np
from scipy.linalg import eigvalsh, eigh
from pathlib import Path
out={"layers":[],"intervals":[],"implant":{}}
for r,k in [(4,1),(5,1),(6,2),(7,2),(8,2)]:
    T=[]
    for P in itertools.combinations(range(r),k):
        for N in itertools.combinations([i for i in range(r) if i not in P],k):
            s=np.zeros(r,dtype=int);s[list(P)]=1;s[list(N)]=-1;T.append(s)
    T=np.array(T);n=len(T)
    c=((T[:,None,:]==T[None,:,:])&(T[:,None,:]!=0)).sum(2)
    o=(T[:,None,:]*T[None,:,:]==-1).sum(2)
    A=((o==0)&(c==k)).astype(int)
    G=np.array([[math.comb(int(v),k) if v>=k else 0 for v in row] for row in c])
    E=G-A;Fk=sum(math.comb(k,a)**3 for a in range(k+1))
    d=Fk*math.comb(r-2*k,k); e=Fk*(math.comb(r-k,k)-math.comb(r-2*k,k))
    assert (E>=0).all() and (A.sum(1)==d).all() and (E.sum(1)==e).all()
    B=np.zeros((n+1,n+1));B[0,1:]=1;B[1:,0]=1;B[1:,1:]=A
    kc=2*n/(math.sqrt(d*d+4*n)+d)
    kb=-eigvalsh(B,subset_by_index=[0,0])[0]
    assert kc-1e-9<=kb<=max(kc,e)+1e-9
    assert eigvalsh(G,subset_by_index=[0,0])[0]>-1e-8
    out['layers'].append(dict(r=r,k=k,n=n,F=Fk,d=d,e=e,kcentral=kc,kactual=kb))
for L in [2,5,10,30,100]:
    z=np.arange(-L,L+1);B=((abs(z[:,None]-z[None,:])<=L)&(z[:,None]!=z[None,:])).astype(float)
    odd=np.zeros((2*L+1,L));even=np.zeros((2*L+1,L+1));even[L,0]=1
    for i in range(1,L+1):
        odd[L+i,i-1]=1/np.sqrt(2);odd[L-i,i-1]=-1/np.sqrt(2)
        even[L+i,i]=even[L-i,i]=1/np.sqrt(2)
    ko=-eigvalsh(odd.T@B@odd)[0];le=eigvalsh(even.T@B@even)[0]
    exact=1+1/(2*np.sin(3*np.pi/(4*L+2)))
    assert abs(ko-exact)<1e-10
    out['intervals'].append(dict(L=L,kodd=ko,kodd_exact=exact,even_gap=le+ko))
# A genuine implant with distinct direct-sum axes and a moderate interval.
T=[-3,-1,1,3];n=len(T);L=40
base=[0]+T;BT=np.array([[int(a-b in T) for b in base] for a in base]);kt=-eigvalsh(BT)[0]
U=[i for i in range(-L,L+1) if i];S={(t,0) for t in T}|{(0,u) for u in U};I=[(0,0)]+sorted(S)
B=np.array([[int((a[0]-b[0],a[1]-b[1]) in S) for b in I] for a in I],float)
v,q=eigh(B);kl=-v[0];q=q[:,0];assert v[1]-v[0]>1e-5
assert all(abs(q[i])<1e-10 for i,a in enumerate(I) if a[0]!=0 or a==(0,0))
qd={a:q[i] for i,a in enumerate(I)}
def conv(a,b):
    c={}
    for x,v in a.items():
        for y,w in b.items():
            z=(x[0]+y[0],x[1]+y[1]);c[z]=c.get(z,0)+v*w
    return c
D={s:1 for s in S};res=conv(D,qd)
for a,vv in qd.items():res[a]=res.get(a,0)+kl*vv
R=sum(vv*vv for vv in res.values());Dr=conv(D,res);num=sum(vv*Dr.get(a,0) for a,vv in res.items())
DU={(0,u):1 for u in U};ru=conv(DU,qd)
for a,vv in qd.items():ru[a]=ru.get(a,0)+kl*vv
RU=sum(vv*vv for vv in ru.values());Dur=conv(DU,ru);numU=sum(vv*Dur.get(a,0) for a,vv in ru.items())
t3=sum(a+b in T for a in T for b in T)
assert abs(R-n-RU)<1e-8 and abs(num-(t3-kl*n+numU))<1e-8
out['implant']=dict(T=T,L=L,kT=kt,kS=kl,eigen_gap=v[1]-v[0],R=R,RU=RU,numerator=num,identity_rhs=t3-kl*n+numU)
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2));print(path);print(json.dumps(out,indent=2))
