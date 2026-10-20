import json, numpy as np
from scipy.special import comb
from pathlib import Path
OUT=Path('.research/agents/tdense10_scratch');r=json.loads(OUT.joinpath('coupled_td_d10_K64_s0.2.json').read_text());m=r['degree'];K=r['K']
u=np.linspace(1e-8,1,200001);x=2*u/(1+u*u);y=np.maximum.reduce([np.zeros(len(x)),2*x*x-1,x-np.sqrt(np.maximum(0,1-x))]);F=x*u/2
bp=lambda b,z:sum(b[i]*comb(m,i)*z**i*(1-z)**(m-i) for i in range(m+1))
worst=[]
for jj in range(2*K):
    j=jj//2;k=int(np.ceil(2*K/jj))-1 if jj else None;cap=np.cos(np.pi/(k+2)) if jj else 1;mask=x<=cap+1e-15
    margin=(r['a'][j]*x-bp(r['beta'][j],x)/2-F+(bp(r['beta'][jj],y) if jj<K else 0))/x
    ix=np.flatnonzero(mask)[np.argmin(margin[mask])];worst.append(dict(jj=jj,x=float(x[ix]),margin=float(margin[ix])))
print(json.dumps(sorted(worst,key=lambda q:q['margin'])[:20],indent=2))
# Inspect exact-failure location in the square-root-of-1-x parameter.
u2=166079665/268435456;x2=1-u2*u2;y2=max(0,2*x2*x2-1,x2-u2);a=r['a'][0]+1e-4
A=a*x2-bp(r['beta'][0],x2)/2+bp(r['beta'][0],y2)-.5
print('FAILPOINT',u2,x2,y2,A,'gap',A+u2*np.sqrt(2-u2*u2)/2,'square',u2*u2*(2-u2*u2)/4-A*A)
