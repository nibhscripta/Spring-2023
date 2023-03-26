import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import solve_ivp
from scipy.optimize import fsolve

def ode(t, y):
    f = y*0

    X = y[0]

    R = 8.314
    T_0 = 450
    F_A0 = 20
    E = 31.4e3

    T = T_0 + 500 * X
    k = 0.133 * np.exp(E / R * (1/450 - 1/T))

    f[0] = k * (1 - X) / (1 + X) * T_0 / T / F_A0
    
    return f

ode_kwargs = {
    'method': 'Radau',
    'atol': 1e-8,
    'rtol': 1e-8,
}

catalyst_weight = 43.13710530642165

sol = solve_ivp(ode, [0, catalyst_weight], [0], **ode_kwargs)
print(f"Final conversion: {sol.y[0][-1]}")
plt.plot(sol.t, sol.y[0])
plt.ylabel("Conversion")
plt.xlabel("Catalyst Weight (kg)")
plt.title("Problem 1 Conversion v Catalyst Weight")
plt.show()

plt.plot(sol.t, 450 + 500 * sol.y[0])
plt.ylabel("Temperature (K)")
plt.xlabel("Catalyst Weight (kg)")
plt.title("Problem 1 Temperature Profile")
plt.show()
print(f"Final temperature: {(450 + 500 * sol.y[0])[-1]}")


def Q(X, T):
    F_A0 = 10 * 20 / 0.08206 / 450
    return F_A0 * (40 * (T - 450) + 20 * X)

print(10 * 20 / 0.08206 / 450)
X = sol.y[0]
T = 450 + 500 * sol.y[0]
plt.plot(sol.t, Q(X, T))
plt.ylabel("Heat (kJ)")
plt.xlabel("Catalyst Weight (kg)")
plt.title("Problem 1 Heat Profile")
plt.show()