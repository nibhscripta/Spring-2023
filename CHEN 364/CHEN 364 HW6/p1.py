import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import solve_ivp

ode_kwargs = {
    'method': 'Radau',
    'atol': 1e-8,
    'rtol': 1e-8,
}

def ode_non_isothermal(t, y):
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

sol_non_isothermal = solve_ivp(ode_non_isothermal, [0, 43.2], [0], **ode_kwargs)

plt.plot(sol_non_isothermal.t, sol_non_isothermal.y[0])
plt.ylabel("Conversion")
plt.xlabel("Catalyst Weight (kg)")
plt.title("Problem 1 Conversion v Catalyst Weight")
plt.show()

plt.plot(sol_non_isothermal.t, 450 + 500 * sol_non_isothermal.y[0])
plt.ylabel("Temperature (K)")
plt.xlabel("Catalyst Weight (kg)")
plt.title("Problem 1 Temperature Profile")
plt.show()


def ode_non_isothermal(t, y):
    f = y*0

    X = y[0]

    R = 8.314
    T_0 = 450
    F_A0 = 20
    E = 31.4e3

    T = T_0
    k = 0.133 * np.exp(E / R * (1/450 - 1/T))

    f[0] = k * (1 - X) / (1 + X) * T_0 / T / F_A0
    
    return f

sol_isothermal = solve_ivp(ode_non_isothermal, [0, 50], [0], **ode_kwargs)

def Q(X):
    F_A0 = 10 * 20 / 0.08206 / 450
    return F_A0 * (-20 * X)

X = sol_isothermal.y[0]
plt.plot(sol_isothermal.t, Q(X))
plt.ylabel("Heat (kJ)")
plt.xlabel("Catalyst Weight (kg)")
plt.title("Problem 1 Heat Profile")
plt.show()
print(f"Isothermal conversion: {X[-1]}")