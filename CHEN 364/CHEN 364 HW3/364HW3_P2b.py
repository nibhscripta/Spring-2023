import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, trapezoid
from scipy.optimize import curve_fit, fsolve
import time, math
# constants
k = 10**-4
E = 87000
R = 8.314
T_1 = 50 + 273.15
T_2 = 125 + 273.15
P = 10 * 101325
C_A0 = P / T_2 / R
F_A0 = 2.7
# CSTR design equation
HW_3_P_2_CSTR = lambda X: X * F_A0 / (k * np.exp(E / R *(1/T_1 - 1/T_2)) * C_A0 * (1 - X)/(1 + 2*X))

X = np.linspace(0, 0.99, 100)
# plot CSTR conversion
V_81 = HW_3_P_2_CSTR(0.81)
plt.plot(HW_3_P_2_CSTR(X), X)
plt.plot(V_81, 0.81, 'rx')
plt.xlabel(r"$V$")
plt.ylabel(r"$X$")
plt.title("Problem 2 Volume v Conversion of a CSTR")
plt.show()
# V at X=0.81
print(round(V_81, 3))

# Part C code

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

# solve for CSTR conversion at 1000L = 1m^3
cstr_conversion = fsolve(lambda x: HW_3_P_2_CSTR(x) - 1, [0.5])
# find PFR conversion at 400L = 0.4m^3
# CSTR conversion is initial condition for PFR ODE
total_conversion = solve_ivp(HW_3_P_2_PFR, [0, 0.4], cstr_conversion, method="Radau", rtol=1e-6, atol=1e-6)
# final conversion is last value in PFR ODE solution
print(round(total_conversion.y[0][-1], 3))