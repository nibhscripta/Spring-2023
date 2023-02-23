import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ode system to solve dp/dW and dX/dW
def ode(t, y):
    X = y[0]
    p = y[1]
    # constants
    F_A0 = 2e-5
    v_0 = 2.83e-7
    alpha = 3.55e5
    k = 0.004

    f = np.zeros(len(y))

    f[0] = k * F_A0 * p**2 / v_0**2 * ((1 - X) / (1 - X/2)) **2
    f[1] = -alpha / 2 / p * (1 - X/2)

    return f

# arguments to pass to the ode solver
ode_kwargs = {
    'method': 'Radau',
    'atol': 1e-8,
    'rtol': 1e-8,
}

# solving the ode system
solution = solve_ivp(ode, [0, 3.53e-6], [0, 1], **ode_kwargs)

# plottting
plt.plot(solution.t, solution.y[0])
plt.plot(solution.t, solution.y[1])
plt.legend([r'$\frac{dX}{dW}$', r'$\frac{dp}{dW}$'])
plt.xlabel(r"$W$(kg)")
plt.ylabel(r"$X/p$")
plt.title("Problem 2a Conversion and Pressure Drop Plot")
plt.show()

# functions to calculate flow rates
F_A0 = 2e-5
F_A = lambda X: F_A0 * (1 - X)
F_C = lambda X: F_A0 * X

# plotting
plt.plot(solution.t, F_A(solution.y[0]))
plt.plot(solution.t, F_C(solution.y[0]))
plt.legend([r'$F_A/F_B$', r'$F_C$'])
plt.xlabel(r"$W$(kg)")
plt.ylabel(r"Flow rate(mol/s)")
plt.title("Problem 2a Flow Rate Plot")
plt.show()