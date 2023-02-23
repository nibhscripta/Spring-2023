import numpy as np
import matplotlib.pyplot as plt
from sympy.integrals import inverse_laplace_transform, laplace_transform
from sympy.abc import t, s
from sympy.functions import exp, Heaviside
from sympy import lambdify
# input function
u = lambda t: 20 + 5 * np.exp(-t)
# inverse laplace transform Y(s)
y_expr = inverse_laplace_transform(5 / (s + 1) / (s/6 + 1), s, t)
# convert sympy expression y(t) into lambda func
y = lambdify(t, y_expr, 'numpy')
# lambdify won't work on Heaviside() with sympy version <1.11
t_range_min = np.linspace(0, 6, 100)
# plotting
plt.plot(t_range_min, y(t_range_min) + 20) # +20 to add initial condition back
plt.plot(t_range_min, u(t_range_min), '--')
plt.xlabel(r'$t$ (min)')
plt.ylabel(r'$T(t)$')
plt.title(r'Problem 3.12 Response Plot')
plt.legend(['Response', 'Input'])
plt.show()