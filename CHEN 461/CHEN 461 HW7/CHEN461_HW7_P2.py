import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp 

ode_kwargs = {
    'method': "Radau",
    'rtol': 1e-8,
    'atol': 1e-8,
}

def ode_1(t, y):
    f = y*0

    x_1 = y[0]
    x_2 = y[1]

    u_1 = 1
    u_2 = 0

    f[0] = -83 * x_1 + 21 * u_1 + 4 * u_2
    f[1] = 50 * x_1 - 75 * x_2 - u_2

    return f

def ode_2(t, y):
    f = y*0

    x_1 = y[0]
    x_2 = y[1]

    u_1 = 0
    u_2 = 1

    f[0] = -83 * x_1 + 21 * u_1 + 4 * u_2
    f[1] = 50 * x_1 - 75 * x_2 - u_2

    return f

init = [0, 0]

sol_1 = solve_ivp(ode_1, [0, 0.1], init, **ode_kwargs)
sol_2 = solve_ivp(ode_2, [0, 0.1], init, **ode_kwargs)

plt.plot(sol_1.t, sol_1.y[0], label="First Case")
plt.plot(sol_2.t, sol_2.y[0], label="Second Case")
plt.xlabel(r"$t$")
plt.ylabel(r"$x_1$")
plt.title(r"Problem 6.9 $x_1$ Plot")
plt.legend()
plt.show()

plt.plot(sol_1.t, sol_1.y[1], label="First Case")
plt.plot(sol_2.t, sol_2.y[1], label="Second Case")
plt.xlabel(r"$t$")
plt.ylabel(r"$x_2$")
plt.title(r"Problem 6.9 $x_2$ Plot")
plt.legend()
plt.show()