import numpy as np

a = np.array([
    10.20,
    10.25,
    10.30,
    10.35,
    10.40,
    10.45,
    10.50
])

energy = np.array([
    -22.83856870,
    -22.83939304,
    -22.83983573,
    -22.83991446,
    -22.83964622,
    -22.83904756,
    -22.83813439
])

# Fit a quadratic: E(a) = A*a^2 + B*a + C
A, B, C = np.polyfit(a, energy, 2)

# Position of the minimum
a_min = -B / (2 * A)

# Energy at the fitted minimum
E_min = A * a_min**2 + B * a_min + C

print("Quadratic fit")
print("-------------")
print(f"A = {A:.10f}")
print(f"B = {B:.10f}")
print(f"C = {C:.10f}")
print()
print(f"Fitted equilibrium lattice parameter = {a_min:.6f} Bohr")
print(f"Fitted minimum energy = {E_min:.10f} Ry")
print(f"Fitted lattice parameter = {a_min * 0.529177:.6f} Angstrom")
