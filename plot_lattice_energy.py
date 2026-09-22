import numpy as np
import matplotlib.pyplot as plt

# Silicon lattice parameter scan
a = np.array([10.00, 10.25, 10.30, 10.35, 10.36, 10.37, 10.40, 10.50])

energy = np.array([
    -22.81627843,
    -22.82558989,
    -22.82620297,
    -22.82644536,
    -22.82645217,
    -22.82644311,
    -22.82632744,
    -22.82509261
])

# Find the lowest calculated energy
minimum_index = np.argmin(energy)

print("Lowest calculated energy:")
print(f"Lattice parameter = {a[minimum_index]:.2f} Bohr")
print(f"Energy = {energy[minimum_index]:.8f} Ry")

# Plot energy against lattice parameter
plt.plot(a, energy, 'o-')
plt.xlabel("Lattice parameter (Bohr)")
plt.ylabel("Total energy (Ry)")
plt.title("Silicon: DFT Energy vs Lattice Parameter")
plt.grid(True)
plt.savefig("silicon_lattice_energy.png", dpi=150)
