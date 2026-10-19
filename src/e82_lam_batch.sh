#!/bin/bash
for a in 0.45 0.4 0.3333333333 0.3 0.25 0.2113248654; do
  lam=$(python3 -c "a=$a; print(round(4*a*(1-a),10))")
  E82_MODE=lam E82_LAM=$lam python src/e82_cp_reach.py 80 160 | grep -v triangle | python3 -c "
import sys,json
best=max((json.loads(l) for l in sys.stdin), key=lambda r:r['D'])
print('a*=$a lam=$lam N=%d D=%.6f C=%.4f'%(best['N'],best['D'],best['C']))"
done
