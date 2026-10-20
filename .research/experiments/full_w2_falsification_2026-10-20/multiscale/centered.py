from pathlib import Path
ARCHIVE_ROOT = Path(__file__).resolve().parent.parent
from search import *
for n in [32,64,128,256,512,1024,2048,4096]:
 X=int(round(n**(4/3)));a=np.arange(1,X+1);p=2*n/X*(1-a/(X+1));theta=(np.sqrt(5)-1)/2
 for kind in ['golden_centered','quadratic_centered','two_rotations']:
  u=(a*theta if kind!='quadratic_centered' else a*a*theta)%1
  if kind=='two_rotations':
   v=(a*np.sqrt(2))%1;mask=(2*np.minimum(u,1-u)<np.sqrt(p))&(2*np.minimum(v,1-v)<np.sqrt(p))
  else:mask=2*np.minimum(u,1-u)<p
  calc(a[mask],f'tri_{kind}_{n}',verify=n<=64)
