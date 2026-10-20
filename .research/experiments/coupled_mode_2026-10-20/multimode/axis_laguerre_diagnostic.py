"""Floating diagnostics only. Supply the earlier pass's exact Laguerre JSON."""
import numpy as np
import json, math, argparse
from pathlib import Path
parser=argparse.ArgumentParser()
parser.add_argument('--input', type=Path, required=True, help='Earlier laguerre_full_w2_diagnostic.json')
parser.add_argument('--output', type=Path, default=Path(__file__).with_suffix('.json'))
args=parser.parse_args()
data=json.loads(args.input.read_text());out=[]
for r in data:
 k=r['k'];M=np.array(r['matrix_exact'],float);F=M[k,k];beta=-np.linalg.eigvalsh(M)[0]
 vals=[]
 for m in [1,max(2,round(beta*F)),max(2,round(F**2/100)),max(2,round(F**2))]:
  A=np.zeros((2*k+2,2*k+2));A[:2*k+1,:2*k+1]=M
  A[0,k]=A[k,0]=math.sqrt(m)
  A[k,-1]=A[-1,k]=math.sqrt(2*(m-1));A[-1,-1]=2*F
  ev=np.linalg.eigvalsh(A);K=-ev[0]
  vals.append(dict(m=m,K_radial=float(K),ratio=float(K/math.sqrt(m))))
 eig,vec=np.linalg.eigh(M[1:,1:])
 mass={str(t):float((vec[k-1,eig<=t]**2).sum()) for t in [0,1,10]}
 out.append(dict(k=k,F=float(F),beta=float(beta),punctured_level_k_cheap_mass=mass,tests=vals));print(out[-1])
args.output.write_text(json.dumps(out,indent=2))
