import numpy as np
import matplotlib.pyplot as plt

C_A_ran = np.linspace(0.01, 0.2, 10000)

k_1 = 0.004
k_2 = 0.3
k_3 = 0.25

SX = lambda C_A: k_2 * C_A / (k_1 * C_A**0.5)
SY = lambda C_A: k_2 * C_A / (k_3 * C_A**2)
SXY = lambda C_A: k_2 * C_A / (k_1 * np.sqrt(C_A) + k_3 * C_A**2)

fig, ax = plt.subplots(3, figsize=(6.4, 2*4.8))
ax[0].plot(C_A_ran, SX(C_A_ran), label="Reaction X Selectivity")
ax[0].set_ylabel(r"$S_{B/X}$")
ax[1].plot(C_A_ran, SY(C_A_ran), "tab:orange", label="Reaction Y Selectivity")
ax[1].set_ylabel(r"$S_{B/Y}$")
ax[2].plot(C_A_ran, SXY(C_A_ran), "tab:green", label="Reaction X & Y Selectivity")
ax[2].set_ylabel(r"$S_{B/XY}$")
ax[2].set_xlabel(r"$C_A$ (mol/L)")
ax[0].set_title("Problem 3 Selectivity Plots")
fig.legend()
plt.show()

C_A_opt_index = np.where(SXY(C_A_ran)==SXY(C_A_ran).max())[0][0]
C_A_opt = C_A_ran[C_A_opt_index]

print(f"Optimum C_A = {C_A_opt}")

F = 10 
C_A0 = 4 / 0.08206 / (27 + 273.15)
print(f"CSTR volume = {F * (C_A0 - C_A_opt) / (k_1 * C_A_opt**0.5 + k_2 * C_A_opt + k_3 * C_A_opt**2)}")