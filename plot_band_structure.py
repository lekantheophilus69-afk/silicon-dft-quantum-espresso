import numpy as np
import matplotlib.pyplot as plt

# Load Quantum ESPRESSO band data
data = np.loadtxt("silicon_bands.dat.gnu")

# 12 bands × 101 k-points
x = data[:, 0].reshape(12, 101)
energy = data[:, 1].reshape(12, 101)

# Common k-point path
k = x[0]

# Valence band maximum (band 4)
vbm_band = energy[3]
vbm_index = np.argmax(vbm_band)
vbm = vbm_band[vbm_index]

# Conduction band minimum (band 5)
cbm_band = energy[4]
cbm_index = np.argmin(cbm_band)
cbm = cbm_band[cbm_index]

# Band gap
band_gap = cbm - vbm

# Shift all energies so VBM = 0 eV
energy_shifted = energy - vbm

# Symmetry-point positions
L = k[0]
Gamma = k[50]
X = k[100]

# Direct or indirect along this calculated path
if vbm_index == cbm_index:
    gap_type = "Direct"
else:
    gap_type = "Indirect"

print("======================================")
print("Silicon Band Structure")
print("======================================")
print(f"VBM = {vbm:.4f} eV")
print(f"CBM = {cbm:.4f} eV")
print(f"Band gap = {band_gap:.4f} eV")
print(f"Gap type = {gap_type}")
print("--------------------------------------")
print(f"VBM k-position = {k[vbm_index]:.4f}")
print(f"CBM k-position = {k[cbm_index]:.4f}")
print("--------------------------------------")
print(f"L     = {L:.4f}")
print(f"Gamma = {Gamma:.4f}")
print(f"X     = {X:.4f}")
print("======================================")

# Plot
plt.figure(figsize=(9, 6))

for i in range(12):
    plt.plot(k, energy_shifted[i], linewidth=1.2)

# Fermi/VBM reference
plt.axhline(0, linestyle="--", linewidth=1)

# High-symmetry vertical lines
plt.axvline(L, linestyle="--", linewidth=0.8)
plt.axvline(Gamma, linestyle="--", linewidth=0.8)
plt.axvline(X, linestyle="--", linewidth=0.8)

# Labels
plt.xticks([L, Gamma, X], ["L", "Γ", "X"])

plt.xlabel("Wave vector")
plt.ylabel("Energy relative to VBM (eV)")
plt.title("Silicon Band Structure")

plt.xlim(L, X)
plt.ylim(-6, 8)

plt.grid(axis="y", alpha=0.2)

plt.tight_layout()

plt.savefig("silicon_band_structure_referenced.png", dpi=300)

plt.show()
