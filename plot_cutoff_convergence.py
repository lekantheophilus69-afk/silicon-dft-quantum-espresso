import numpy as np
import matplotlib.pyplot as plt

ecutwfc = np.array([30, 35, 40, 45, 50, 55])

energy = np.array([
    -22.82578384,
    -22.82586842,
    -22.82591527,
    -22.82596671,
    -22.82600804,
    -22.82602164
])

plt.figure(figsize=(8, 5))

plt.plot(ecutwfc, energy, marker='o')

plt.xlabel("Wavefunction cutoff (Ry)")
plt.ylabel("Total energy (Ry)")
plt.title("Silicon DFT Cutoff Convergence")

plt.grid(True)
plt.tight_layout()

plt.savefig("silicon_cutoff_convergence.png", dpi=150)
