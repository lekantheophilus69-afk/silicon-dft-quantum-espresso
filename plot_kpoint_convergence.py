import numpy as np
import matplotlib.pyplot as plt

kpoints = np.array([2, 3, 4, 6, 8, 10])

energy = np.array([
    -22.65203135,
    -22.79439503,
    -22.82600804,
    -22.83806904,
    -22.83954413,
    -22.83977668
])

plt.figure(figsize=(8, 5))
plt.plot(kpoints, energy, marker='o')

plt.xlabel("K-point grid (N×N×N)")
plt.ylabel("Total energy (Ry)")
plt.title("Silicon DFT K-point Convergence")
plt.grid(True)
plt.tight_layout()

plt.savefig("silicon_kpoint_convergence.png", dpi=150)
