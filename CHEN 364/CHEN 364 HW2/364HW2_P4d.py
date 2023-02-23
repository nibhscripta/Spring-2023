import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, trapezoid

# function inside integral
def P_4_d_diff(x):
  return ( (1 - x) / (1 - x / 3) ) ** (-3 / 2)

# constants
F_A0 = 100
k = 40
C_A0 = 830.865 / 8.314 / 500.15 # = 0.2

# conversion values array
X = np.linspace(0, 0.6, 1000)

# evaluate innner function at X
dV = P_4_d_diff(X)

# analytical integral
V = trapezoid(dV, X) * F_A0 / k / C_A0 ** 2
print(V)
# Aggie Honor Code: An Aggie does not lie, cheat, or steal or tolerate
# those who do.
# I certify that this work is my own and not the work of another.
#
# Name: Mark Levchenko
# Assignment #: HW 2
# Question #: 4d