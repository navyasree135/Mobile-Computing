import numpy as np, matplotlib.pyplot as plt

rng = np.random.default_rng(5)
U, RB, T = 10, 50, 2000                     # users, resource blocks, time slots
snr = 10**(np.linspace(25, 2, U)/10)        # mean SNR: user 1 near BS, user 10 at edge
rate = 180e3*np.minimum(0.75*np.log2(1 + snr*rng.exponential(1, (T, RB, U))), 5.5)

def run(kind):
    thr, avg = np.zeros(U), np.full(U, 1e5)
    for t in range(T):
        r = rate[t]
        if kind == "Round robin": pick = (np.arange(RB) + t) % U
        elif kind == "Max C/I":   pick = r.argmax(1)
        else:                     pick = (r/avg).argmax(1)          # proportional fair
        got = np.zeros(U); np.add.at(got, pick, r[np.arange(RB), pick])
        thr += got; avg = 0.99*avg + 0.01*got
    return thr/T/1e6                                                 # Mbit/s

jain = lambda x: x.sum()**2 / (len(x)*(x**2).sum())
for k in ("Round robin", "Max C/I", "Proportional fair"):
    th = run(k)
    print(f"{k:18s} cell = {th.sum():5.1f} Mbit/s   edge user = {th[-1]:.2f}   Jain = {jain(th):.3f}")
    plt.plot(range(1, U+1), th, "o-", label=k)
plt.xlabel("User (10 = cell edge)"); plt.ylabel("Throughput (Mbit/s)"); plt.legend(); plt.grid(True); plt.show()
