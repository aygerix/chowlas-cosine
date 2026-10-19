import json, math, numpy as np, sys
rows=[json.loads(l) for l in open('examples/e106/e106.jsonl')]
for r in rows:
    A=np.array(r['A']); X=r['X']; n=len(A)
    g=np.gcd.reduce(A)
    # best "dilation" fit: for d in 2..X/n*2 check fraction of A within 1 of a multiple of real step
    G=1<<16; x=np.arange(G)/G
    F=np.zeros(G); 
    for a in A: F[a % G]+=1
    f=np.real(np.fft.ifft(F))*G  # f(x)=sum cos(2pi a x) at x=j/G
    M=-f.min(); R=M/math.sqrt(n)
    # top peaks of f (excluding x near 0)
    idx=np.argsort(-f)
    peaks=[]
    for j in idx:
        xx=j/G
        if min(xx,1-xx)<1e-3: continue
        if all(min(abs(xx-p),1-abs(xx-p))>2.0/X for p,_ in peaks): peaks.append((xx,f[j]))
        if len(peaks)>=4: break
    p=1+f/M; L2=np.mean(p**2)
    print(f"X={X} n={n} K={r['K']} mu={r['mu']} beta={r['beta']:.3f} R={R:.3f} gcd={g} int_p2={L2:.2f} 1+1/(2R^2)={1+1/(2*R*R):.2f} peaks="+",".join(f"{a:.4f}:{v/n:.2f}" for a,v in peaks))
