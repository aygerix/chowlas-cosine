from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
from w2_operator import *
rng=np.random.default_rng(80901)
for d in [2,3,4,5,6]:
 grid=np.array(list(itertools.product(range(-2,3),repeat=d)));half=grid[np.array([tuple(z)>tuple(-z)for z in grid])];prob=np.prod(1-abs(half)/3,axis=1);Z=half[rng.random(len(half))<prob];S=np.r_[Z,-Z]
 if d==6:test(S,'product_fejer_m3_d6');open(str(HERE / 'product_fejer_d6.json'),'w').write(json.dumps(out,indent=2))
