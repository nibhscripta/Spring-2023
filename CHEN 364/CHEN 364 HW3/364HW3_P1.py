import numpy as np
from scipy.optimize import curve_fit, fsolve
from sklearn.metrics import r2_score
# data
r_A = np.array([0.002, 0.046, 0.73, 8.33])
T_K = np.array([300, 320, 340, 360])
# reaction concentration
C_A = 2
C_B = 1.5
# convert r_A to k; elementary reaction
# 2A + B -> C
k = r_A / C_A**2 / C_B
# linearize data
ln_k = np.log(k)
inverse_T = 1 / T_K
# function to fit data to
def obj_func(T, E, A):
  return -E / 8.314 * T + np.log(A)
# fit data
fit_covs, _ = curve_fit(obj_func, inverse_T, ln_k)
# check fit against data
print("r^2:" ,r2_score(ln_k, obj_func(inverse_T, *fit_covs)))
# Output results
print(f"Activation energy: {round(fit_covs[0]/1000, 3)} kJ")
print(f"Frequency factor: {round(fit_covs[1], 3)}")
# Aggie Honor Code: An Aggie does not lie, cheat, or steal or tolerate
# those who do.
# I certify that this work is my own and not the work of another.
#
# Name: Mark Levchenko
# Assignment #: HW 3
# Question #: 1