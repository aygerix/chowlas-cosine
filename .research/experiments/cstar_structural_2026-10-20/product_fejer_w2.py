from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
from w2_operator import *
rng=np.random.default_rng(80901)
for m,ds in [(3,[2,3,4,5]),(4,[2,3,4]),(5,[2,3,4])]:
 for d in ds:
  grid=np.array(list(itertools.product(range(1-m,m),repeat=d)));half=grid[np.array([tuple(z)>tuple(-z)for z in grid])];prob=np.prod(1-abs(half)/m,axis=1)
  Z=half[rng.random(len(half))<prob];S=np.r_[Z,-Z]
  test(S,f'product_fejer_m{m}_d{d}')
  open(str(HERE / 'product_fejer_w2.json'),'w').write(json.dumps(out,indent=2))
