from pathlib import Path
ARCHIVE_ROOT = Path(__file__).resolve().parent.parent
from search import *
seed=np.r_[np.arange(1,19),np.arange(20,38),[39,40,41,42,47,48,50,52,57,61,62,64,65,68]]
for J in range(8,13):
 A=np.unique(np.concatenate([2**j*seed for j in range(J+1)]));calc(A,f'dyadic_extended_J{J}')
