#!/bin/sh
cd .research/agents/lambda_scratch
python3 evalR.py --file cands3.txt > out/evalR3.txt
echo done
