import numpy as np, matplotlib.pyplot as plt

S, M, n = 420, 84, 4                        # total channels, cells, path-loss exponent
print("N   D/R   S/I(dB)   capacity")
Ns = [1, 3, 4, 7, 9, 12, 13, 19]            # N = i^2 + ij + j^2
si = []
for N in Ns:
    Q = np.sqrt(3*N)                        # reuse ratio D/R
    s = 10*np.log10(Q**n / 6)               # 6 first-tier interferers
    si.append(s)
    print(f"{N:<3} {Q:5.2f} {s:8.2f} {M/N*S:9.0f}")
plt.plot(Ns, si, "o-"); plt.axhline(18, color="r", ls="--")
plt.xlabel("Cluster size N"); plt.ylabel("S/I (dB)"); plt.grid(True); plt.show()
