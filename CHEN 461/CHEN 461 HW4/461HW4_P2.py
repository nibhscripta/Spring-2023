from sympy import lambdify, Heaviside
from sympy.abc import t

import numpy as np
import matplotlib.pyplot as plt

# convert sympy expressions to lambda func
u_expr = Heaviside(t) - Heaviside(t - 1)
u = lambdify(t, u_expr, 'numpy')

y_expr = t * Heaviside(t) - (t - 1) * Heaviside(t - 1)
y = lambdify(t, y_expr, 'numpy')

# plotting
t_ran = np.linspace(-1, 2, 100)

plt.plot(t_ran, u(t_ran))
plt.plot(t_ran, y(t_ran))
plt.xlabel(r"$t$")
plt.ylabel(r"$y(t)$")
plt.legend(['Input', 'Reponse'])
plt.title('Problem 3.14 Response Plot')
plt.show()