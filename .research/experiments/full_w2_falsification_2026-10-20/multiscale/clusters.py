from pathlib import Path
ARCHIVE_ROOT = Path(__file__).resolve().parent.parent
from search import *
seed=np.r_[np.arange(1,19),np.arange(20,38),[39,40,41,42,47,48,50,52,57,61,62,64,65,68]]
for L in [1,2,4,8,16,32,64,128]:
 for variant in ['filled','tapered','dyadic_union']:
  if variant=='filled':A=np.concatenate([(2*L+1)*a+np.arange(L) for a in seed])
  elif variant=='tapered':A=np.concatenate([(2*L+1)*a+np.arange(max(1,int(L*(1-a/69)))) for a in seed])
  else:A=np.unique(np.concatenate([2**j*seed for j in range(int(np.log2(L))+1)]))
  calc(A,f'clusters_{variant}_{L}',verify=L<=2)
