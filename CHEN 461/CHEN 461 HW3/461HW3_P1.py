import numpy as np
import matplotlib.pyplot as plt
from sympy.integrals import inverse_laplace_transform, laplace_transform
from sympy.abc import t, s
from sympy.functions import exp, Heaviside
from sympy import lambdify
# input a sympy expression
u_expr = t*Heaviside(t) - 2*(t-2)*Heaviside(t-2) + (t-4)*Heaviside(t-4)
# convert sympy expression u(t) into lambda func
u = lambdify(t, u_expr, 'numpy')
# lambdify won't work on Heaviside() with sympy version <1.11
# inverse laplace transform Y(s)
y_expr = inverse_laplace_transform( (1 - 2*exp(-2*s) + exp(-4*s)) / s**2 / (s/2 + 1), s, t)
# convert sympy expression y(t) into lambda func
y = lambdify(t, y_expr, 'numpy')
t_range = np.linspace(0, 6, 100)
# plotting
plt.plot(t_range, y(t_range))
plt.plot(t_range, u(t_range), '--')
plt.xlabel(r'$t$')
plt.ylabel(r'$y(t)$')
plt.title(r'Problem 3.8 Response Plot')
plt.legend(['Response', 'Input'])
plt.show()