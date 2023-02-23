import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, trapezoid
from scipy.optimize import curve_fit, fsolve
# PFR ODE
def HW_3_P_3_ODE(t, y):
    X = y[0]
    k_f = 4.25e-3
    k_e = 2.5
    k_b = k_f/k_e
    P_A0 = 18
    F_A0 = 23.6
    return [ (k_f * (1 - X)**2 - k_b * X**2 / 4) * P_A0**2 / F_A0 ]

# solve ODE implicitly
p_3_solution = solve_ivp(HW_3_P_3_ODE, [0, 50], [0], method="Radau", rtol=1e-6, atol=1e-6)

# plotting
plt.plot(p_3_solution.t, p_3_solution.y[0])
plt.xlabel(r"W")
plt.ylabel(r"X")
plt.title("Plot of Conversion v Catalyst Weight for a PBR")
plt.show()