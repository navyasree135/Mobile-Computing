import numpy as np, matplotlib.pyplot as plt

rng = np.random.default_rng(1)
D, n, sigma = 2000, 3.5, 4                  # BS spacing (m), path-loss exponent, shadowing (dB)
x = np.arange(1, D, 5)                      # MS moves from BS1 to BS2
rss1 = -30 - 10*n*np.log10(x/100)   + rng.normal(0, sigma, len(x))
rss2 = -30 - 10*n*np.log10((D-x)/100) + rng.normal(0, sigma, len(x))

def handoffs(H):
    cur, count, serving = 1, 0, []
    for a, b in zip(rss1, rss2):
        if cur == 1 and b > a + H: cur, count = 2, count + 1
        elif cur == 2 and a > b + H: cur, count = 1, count + 1
        serving.append(cur)
    return count, serving

for H in (0, 3, 6, 10):
    print(f"Hysteresis {H:2d} dB -> {handoffs(H)[0]} handoffs")

fig, ax = plt.subplots(2, 1, sharex=True)
ax[0].plot(x, rss1, label="BS1"); ax[0].plot(x, rss2, label="BS2"); ax[0].legend(); ax[0].set_ylabel("RSS (dBm)")
for H in (0, 6): ax[1].step(x, handoffs(H)[1], label=f"H = {H} dB")
ax[1].set_ylabel("Serving BS"); ax[1].set_xlabel("Distance from BS1 (m)"); ax[1].legend(); plt.show()
