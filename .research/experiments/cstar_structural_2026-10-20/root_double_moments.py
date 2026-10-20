from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import numpy as np,math
from scipy.linalg import eigvalsh
for r in [6,10,30,100,1000]:
 c=np.array([1/math.factorial(j)**2 for j in range(6)]);p=np.array([1.])
 for _ in range(r):p=np.convolve(p,c)[:6]
 M=np.array([p[j]*math.factorial(j)**2/r**j for j in range(6)])
 vals=[]
 for h in [1,2]:
  H=np.array([[M[i+j] for j in range(h+1)]for i in range(h+1)]);T=np.array([[M[i+j+1] for j in range(h+1)]for i in range(h+1)])
  z=eigvalsh(T,H)[0];vals.append((h,z,r*(1-z)))
 print(r,vals)
