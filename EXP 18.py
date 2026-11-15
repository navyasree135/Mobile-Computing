import numpy as np, matplotlib.pyplot as plt

def erlang_b(A, m):
    B = 1.0
    for k in range(1, m + 1):
        B = A*B / (k + A*B)
    return B

A = 6                                       # offered traffic (Erlang)
for m in (5, 8, 10, 12, 15):
    print(f"A={A} E, {m} channels -> blocking = {erlang_b(A, m)*100:.2f} %")
m = 1
while erlang_b(A, m) > 0.02: m += 1
print("Channels needed for 2 % blocking:", m)

traffic = np.linspace(0.1, 30, 200)
for m in (5, 10, 20):
    plt.semilogy(traffic, [erlang_b(a, m) for a in traffic], label=f"{m} channels")
plt.xlabel("Offered traffic (Erlang)"); plt.ylabel("Blocking probability"); plt.legend(); plt.grid(True); plt.show()
