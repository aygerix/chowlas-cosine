#!/bin/bash
# lead 2026-10-18 night: N = 55 structured classes C(X,55,Y,2), threshold R = 0.575 (M = 4.2644), scaled from the
# N = 36/45/50 optima (X/N ~ 1.44, Y/N ~ 0.77-0.86). Sequential, 4 OpenMP threads each.
D=.research/agents/construct_scratch
$D/cto_run.sh o55y42x79 79 55 42 2 4.2644
$D/cto_run.sh o55y44x79 79 55 44 2 4.2644
$D/cto_run.sh o55y42x81 81 55 42 2 4.2644
