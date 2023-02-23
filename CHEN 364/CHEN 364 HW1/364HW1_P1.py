import numpy as np
from scipy.integrate import trapezoid
# dV for PFR in Problem 1b
def P_1b_PFR_eq(C_A):
    return -10 / 0.36 / C_A
# array for C_A
# C_A starts at 1x and ends at 0.01x
C_A = np.linspace(1, 0.01, 1000)
# calculate dV in an array
dV = P_1b_PFR_eq(C_A)
# integrate
V = trapezoid(dV, C_A)
# output
print(V)
# Aggie Honor Code: An Aggie does not lie, cheat, or steal or tolerate
# those who do.
# I certify that this work is my own and not the work of another.
#
# Name: Mark Levchenko
# Assignment #: HW 1
# Question #: 1b