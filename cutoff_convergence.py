import numpy as np

ecut = np.array([30, 35, 40, 45, 50, 55])

energy = np.array([
    -22.82578384,
    -22.82586842,
    -22.82591527,
    -22.82596671,
    -22.82600804,
    -22.82602164
])

# 1 Ry = 13.605693 eV
ry_to_ev = 13.605693

print("Cutoff convergence")
print("------------------")

for i in range(1, len(ecut)):
    delta_ry = energy[i] - energy[i-1]

    # Absolute change
    delta_ev = abs(delta_ry) * ry_to_ev

    # Two Si atoms in the cell
    delta_mev_atom = delta_ev * 1000 / 2

    print(
        f"{ecut[i-1]:2.0f} -> {ecut[i]:2.0f} Ry: "
        f"{delta_mev_atom:.4f} meV/atom"
    )
