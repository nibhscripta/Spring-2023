import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, trapezoid
from scipy.optimize import curve_fit, fsolve
import time, math
# ODE for pfr
def HW_3_P_2_PFR(t, x):
    # constants
    k = 10**-4
    E = 87000
    R = 8.314
    T_1 = 50 + 273.15
    T_2 = 125 + 273.15
    P = 10 * 101325
    C_A0 = P / T_2 / R
    F_A0 = 2.7
    # get conversion for independent var array
    X = x[0]
    return [k * np.exp(E / R *(1/T_1 - 1/T_2)) * C_A0 * (1 - X)/(1 + 2*X) / F_A0]
# solve ODE implicitly
HW_3_P_2_solution_pfr = solve_ivp(HW_3_P_2_PFR, [0, 5], [0],  method="Radau", rtol=1e-6, atol=1e-6)
# plot solution
V_81 = np.interp(0.81, HW_3_P_2_solution_pfr.y[0], HW_3_P_2_solution_pfr.t)
plt.plot(HW_3_P_2_solution_pfr.t, HW_3_P_2_solution_pfr.y[0])
plt.plot(V_81, 0.81, 'rx')
plt.xlabel(r"$V$")
plt.ylabel(r"$X$")
plt.title("Problem 2 Volume v Conversion of a PFR")
plt.show()
# interpolate for X=0.81
print(round(V_81, 3))
# Aggie Honor Code: An Aggie does not lie, cheat, or steal or tolerate
# those who do.
# I certify that this work is my own and not the work of another.
#
# Name: Mark Levchenko
# Assignment #: HW 3
# Question #: 1a