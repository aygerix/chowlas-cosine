#!/bin/sh
cd .research/agents/lambda_scratch
cc -O3 -march=native -o bin/tabu_seed tabu_lambda.c
sed 's/bin\/tabu_lambda/bin\/tabu_seed/' seeded.txt | xargs -P 2 -I{} sh -c '{}' > out/tabu_seeded.txt
