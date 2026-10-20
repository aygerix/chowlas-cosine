"""Exact small cyclic Sidon search with a stated node/time boundary.

Tests the broader actual-fiber hypothesis; reference fibers can remain
affine parabolas. All computation on Dirichlet.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import socket
import time


def parabolas(p):
    result=set()
    for direction in range(p+1):
        for a in range(1,p):
            for b in range(p):
                for c in range(p):
                    B=[]
                    for t in range(p):
                        z=(a*t*t+b*t+c)%p
                        x,y=((t-direction*z)%p,z) if direction<p else (z,t)
                        B.append(x*p+y)
                    result.add(tuple(sorted(B)))
    return result


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    out=[]
    for p in [3,5,7]:
        orbit=parabolas(p);n=p*p
        classes=sorted({min(x*p+y,((-x)%p)*p+(-y)%p) for x in range(p) for y in range(p) if x or y})
        class_index={g:i for i,g in enumerate(classes)}
        masks=[[0]*n for _ in range(n)]
        for a in range(n):
            for b in range(n):
                if a==b:continue
                x=(a//p-b//p)%p;y=(a%p-b%p)%p
                masks[a][b]=1<<class_index[min(x*p+y,((-x)%p)*p+(-y)%p)]
        start=time.monotonic();nodes=0;normalized=[];outsider=None;stopped=False
        def dfs(S,used,next_point):
            nonlocal nodes,outsider,stopped
            if stopped:return
            nodes+=1
            if nodes%4096==0 and time.monotonic()-start>45:stopped=True;return
            if len(S)==p:
                key=tuple(S);normalized.append(key)
                if key not in orbit:outsider=key;stopped=True
                return
            need=p-len(S)
            for a in range(next_point,n-need+1):
                added=0
                for b in S:
                    bit=masks[a][b]
                    if bit&(used|added):break
                    added|=bit
                else:dfs(S+[a],used|added,a+1)
                if stopped:return
        dfs([0],0,1)
        sample=outsider or normalized[0]
        ordered=Counter(((a//p-b//p)%p,(a%p-b%p)%p) for a in sample for b in sample if a!=b)
        assert len(ordered)==p*(p-1) and set(ordered.values())=={1}
        missing=[(x,y) for x in range(p) for y in range(p) if (x or y) and (x,y) not in ordered]
        assert len(missing)==p-1
        complete=not stopped
        row=dict(p=p,complete=complete,nodes=nodes,normalized_found=len(normalized),
                 total_if_complete=len(normalized)*p if complete else None,
                 affine_parabola_count=len(orbit),nonparabola_found=outsider is not None,
                 sample_points=[[a//p,a%p] for a in sample],missing_nonzero_differences=missing,
                 normalization='Search all sets containing0, ascending point indices; stop at first '
                               'nonparabola or45 seconds. No completeness claim on a stopped search.',
                 exact_fourier_bound='At nonzero character: |F|^2=p-1-sum_missing character, so <=2p-2.',
                 enumeration_sha256=hashlib.sha256(repr(normalized).encode()).hexdigest(),
                 elapsed_seconds=time.monotonic()-start)
        out.append(row);print(json.dumps(row),flush=True)
    root=Path('.research/experiments/sidon_cutoff_2026-10-20');root.mkdir(parents=True,exist_ok=True)
    (root/'cyclic_probe.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
