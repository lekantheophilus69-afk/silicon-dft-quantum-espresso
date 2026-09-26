import numpy as np

kpoints = np.array([2, 3, 4, 6, 8])

energy = np.array([
    -22.65203135,
    -22.79439503,
    -22.82600804,
    -22.83806904,
    -22.83954413
])

print("K-point convergence")
print("-------------------")

for i in range(1, len(kpoints)):
    delta_ry = energy[i] - energy[i-1]
    delta_mev_atom = abs(delta_ry) * 13.605693 * 1000 / 2

    print(
        f"{kpoints[i-1]}x{kpoints[i-1]}x{kpoints[i-1]} -> "
        f"{kpoints[i]}x{kpoints[i]}x{kpoints[i]}: "
        f"{delta_mev_atom:.4f} meV/atom"
    )
