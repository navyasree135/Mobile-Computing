import numpy as np, matplotlib.pyplot as plt

Pt, Gt, Gr = 43, 15, 0                      # dBm, dBi, dBi
d = np.logspace(-1, 1, 100)                 # 0.1 to 10 km
for f in (900, 1800, 2100):                 # MHz
    fspl = 20*np.log10(d) + 20*np.log10(f) + 32.44
    Pr = Pt + Gt + Gr - fspl
    print(f"{f} MHz: FSPL at 1 km = {20*np.log10(f)+32.44:.1f} dB, Pr at 1 km = {Pt+Gt+Gr-(20*np.log10(f)+32.44):.1f} dBm")
    plt.semilogx(d, Pr, label=f"{f} MHz")
plt.xlabel("Distance (km)"); plt.ylabel("Received power (dBm)"); plt.legend(); plt.grid(True); plt.show()
