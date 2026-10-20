"""Rebuild a saved full W2 rowset from text support inputs, without NPZ files."""
from pathlib import Path
import hashlib
import json
import numpy as np

def load_saved_support(tag):
    record = json.loads((Path(__file__).parent / 'supports' / (tag + '.json')).read_text())
    A = np.asarray(record['A'], dtype=np.int64)
    assert len(A) == len(np.unique(A)) and np.all(A > 0)
    S = set(map(int, A)) | {-int(a) for a in A}
    W = np.asarray(sorted({0} | S | {a+b for a in S for b in S}), dtype='<i8')
    assert len(W) == record['W2_size']
    assert hashlib.sha256(W.tobytes()).hexdigest() == record['W2_sha256_int64_little_endian']
    return {'A': A, 'W': W, 'K': record['K_numerical']}
