#!/bin/sh
# signed vs unsigned: exhaustive small k (signed_ex), tabu for larger k (signed_tabu)
cd .research/agents/lambda_scratch
cc -O3 -march=native -o bin/signed_ex signed_ex.c -lm
cc -O3 -march=native -o bin/signed_tabu signed_tabu.c -lm
mkdir -p out
( bin/signed_ex 3 6 5 18 4; bin/signed_ex 3 7 6 18 5; bin/signed_ex 3 8 7 18 7 ) > out/signed_ex3_a.txt &
( bin/signed_ex 3 9 8 20 9; bin/signed_ex 3 10 9 24 12 ) > out/signed_ex3_b.txt &
( bin/signed_ex 4 6 5 18 2; bin/signed_ex 4 7 6 18 4; bin/signed_ex 4 8 7 18 5 ) > out/signed_ex4_a.txt &
( bin/signed_ex 4 9 8 20 6; bin/signed_ex 4 10 9 22 8 ) > out/signed_ex4_b.txt &
wait
for lam in 3 4 5 6; do for k in 10 12 14 16 20; do for c in 8 12 16; do
  L=$(( c * k * k / (10 * 2 * lam) )); [ $L -le $k ] && L=$((k+2))
  for mode in 1 0; do for s in 1 2; do echo "$lam $k $L 20000 $s $mode"; done; done
done; done; done | xargs -P 4 -n 6 sh -c 'bin/signed_tabu $0 $1 $2 $3 $4 $5' > out/signed_tabu.txt
echo done
