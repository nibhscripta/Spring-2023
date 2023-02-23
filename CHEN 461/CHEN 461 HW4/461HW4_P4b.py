import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
import math, os

# load data
data_file = loadmat(f'{os.path.dirname(os.path.realpath(__file__))}\datafile.mat')

from sympy import Heaviside, exp, lambdify
from sympy.abc import t

# plot data
plt.plot(data_file['t'], data_file['y_data'], '.')

# create a response formula with tau=5.5
resp_expr = (15 * (1 - exp(-(t - 6) / 5.5))) * Heaviside(t - 6)
# convert expression to lamdba func
resp = lambdify(t, resp_expr, 'numpy')

# plotting
plt.plot(data_file['t'], resp(data_file['t']))
plt.title('Problem 4 Time Constant Comparison for Input')
plt.legend(['Data', r"$\tau=5.5$"])
plt.xlabel(r"$t$")
plt.ylabel("Response")
plt.show()