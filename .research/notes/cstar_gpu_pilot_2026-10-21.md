# Chowla-only bounded GPU pilot, 2026-10-21

## Scope and outcome

The user authorized a QUICK RunPod pilot using approximately $7 of existing
credit, after writing/testing the operator on GCP and consulting one internal
PhD Advisor agent (GPT-6.1 Sol, MAX reasoning). Wilf is excluded. The original
sustained research goal remains paused; this bounded pilot is complete.

NEW ENGINEERING RESULT: the float64 NumPy/CuPy Fourier operator passes CPU and
GPU checks. A same-host large-band workload shows 2.22x, 4.91x and 18.22x warmed
operator speedups at batch sizes 1, 8 and 32. This is not an end-to-end solver
or proof speedup, nor a new universal certificate-cost theorem.

The new L4 worker was deleted after results were copied back. RunPod's balance
was $7.4312024352 before provisioning and $7.4120309232 at the final account
check. This observed difference includes account activity; it is not a
reconciled invoice for the pilot. Existing pods and storage were untouched.

## Operator and checks

Code: [cstar_gpu_kernel.py](../../src/cstar_gpu_kernel.py).
For q=sum_{k in B} v_k cos(kx) and D=2 sum_{a in A} cos(ax), it applies

    (C v)_j = (1/2) sum_k v_k [1_A(|j-k|)+1_A(j+k)],
    H=<D,q^2>=v^T C v.

Two real FFTs and a pointwise multiplication implement the action without a
dense matrix. A and B contain distinct positive frequencies. The real inverse
FFT constructs the symmetric Fourier polynomial, with explicit normalization.
The length satisfies L>max(2 max(A), max(A)+2 max(B)), preventing half-spectrum
index overflow and cyclic alias in the cubic average. The advisor identified
the small-B/large-A padding edge case before deployment; A={101},B={1} is now
a regression control.

Checks run on Dirichlet before deployment, and then on both RunPod backends:

* A={1},q=cos(x): H=0.
* A={2},q=cos(x): H=1/2, including the Hankel diagonal.
* A={101},q=cos(x): H=0 and safe half-spectrum construction.
* Two integer-vector batches compared against independently built exact
  Toeplitz-plus-Hankel actions, including a widely spaced support.
* The existing degree1152 N50_x72 witness was reconstructed with Python
  integer/Fraction arithmetic: a=50,Q<=25n, its saved rational H, and its
  strict determinant certificate M>3.954718245 all pass. GPU evaluation
  agrees numerically with the exact H. This reproduces an existing result.

Maximum GPU error in the small exact operator controls: 3.1086244689504383e-15.
No floating calculation is used as the proof of the rational witness.

## Matched performance evidence

RunPod NVIDIA L4, float64, NumPy 2.4.6, CuPy 14.2.0. Both backends ran on
the same host, with OPENBLAS_NUM_THREADS=2 and OMP_NUM_THREADS=2. Timings are
medians of seven warmed applications. RNG seed: 20261021.

The large-band control has n=256,max(A)=4095,8192 witness frequencies and
FFT length32768. It is an operator benchmark, not an optimized witness search.

| Batch | NumPy FFT (ms) | CuPy FFT (ms) | Resident operator speedup |
| --- | ---: | ---: | ---: |
| 1 | 0.5602 | 0.2529 | 2.22x |
| 8 | 2.9028 | 0.5914 | 4.91x |
| 32 | 18.2326 | 1.0005 | 18.22x |

CRITICAL LIMIT: setup, initial allocation/input transfer and output transfer
are outside these operator timings. Large-band setup was87.1ms on GPU; the
batch32 input allocation/host-to-device transfer was20.06ms. Thus that batch
does NOT establish a one-shot offload win. Keep vectors resident across many
iterative actions before expecting an end-to-end gain. Output transfer was
not separately timed.

The small144-frequency case was faster with the direct CPU matrix. The
wide-sparse case has only12 witness frequencies but max(A)=131071: at batch32
GPU FFT took13.04ms versus about0.0027ms for the direct CPU action. A GPU/CPU
FFT speedup on that case would be a misleading reason to select FFT.

DECISION: preserve this as an optional large-band matvec for a future
projected trust-region/Krylov implementation, keeping state on device. Retain
CPU direct/sparse actions for small or sparse spaces. Do not port the dense
solver, change the norm budget, start a large support search, or claim a
universal bound based on this pilot.

## Reproduction and artifacts

Dirichlet baseline:

    src/dirun.sh -c 2 -m 8 -t 180 python src/cstar_gpu_kernel.py --backend numpy --output .research/experiments/gpu_pilot_2026-10-21/cpu.json

On the authorized RunPod worker, only the kernel source and the existing
resolvent results.json fixture were copied. With CuPy14.2.0 installed:

    OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 python cstar_gpu_kernel.py --backend numpy --fixture results.json --output cpu_runpod.json --repeats 7
    OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 python cstar_gpu_kernel.py --backend cupy --fixture results.json --output gpu_runpod.json --repeats 7

Raw data and comparison: ../experiments/gpu_pilot_2026-10-21/.
The comparison was computed on Dirichlet after copying the RunPod results.
Worker lifecycle/account observations: runpod_lifecycle.json in that folder.

The [advisor review](phd_advisor_review_2026-10-21.md) separately audits the
resolvent and flatness arguments and derives a full-space cost lower bound
from certified K/L1 upper bounds. It is an independent internal AI paper
review, not an external credentialed review or Lean/kernel check. Its next
Boolean flatness target is conjectural and conditional on research resuming.

Full Chowla remains OPEN. No new universal exponent, new counterexample
construction, optimized-cost bound or kernel-checked theorem is claimed.
