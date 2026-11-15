import numpy as np
from scipy.linalg import hadamard

codes = hadamard(8)[1:5]                    # 4 orthogonal Walsh codes, 8 chips each
bits = np.array([[1,0,1,1], [0,0,1,0], [1,1,0,0], [0,1,1,0]])   # 4 users x 4 bits
data = 2*bits - 1                           # 0/1 -> -1/+1

tx = sum(np.kron(data[u], codes[u]) for u in range(4))    # spread and add
rx = tx + np.random.default_rng(0).normal(0, 1, tx.size)  # add noise

for u in range(4):                          # despread: correlate with own code
    corr = rx.reshape(-1, 8) @ codes[u]
    out = (corr > 0).astype(int)
    print(f"User {u+1}: sent {bits[u]}  received {out}  {'OK' if (out == bits[u]).all() else 'errors'}")
