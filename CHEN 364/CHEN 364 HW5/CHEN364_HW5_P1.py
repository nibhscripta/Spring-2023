import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def ode(t, y):
    f = y*0

    N_A1 = y[0]
    N_C1 = y[1]
    N_A2 = y[2]
    N_C2 = y[3]

    k = 0.0445
    F = 10
    V_1_0 = 1000

    V_1 = V_1_0 - F * t
    V_2 = F * t

    r_A1 = k * N_A1**2 / V_1**2
        
    if V_2 == 0:
        r_A2 = 0
    else:
        r_A2 = k * N_A2**2 / V_2**2

    f[0] = -r_A1 * V_1 - F * N_A1 / V_1
    f[1] = r_A1 * V_1 - F * N_C1 / V_1
    f[2] = -r_A2 * V_2 + F * N_A1 / V_1
    f[3] = r_A2 * V_2 + F * N_C1 / V_1

    return f

V_1_0 = 1000.
C_A1_0 = 2.
N_A1_0 = V_1_0 *  C_A1_0


init_cond = [N_A1_0, 0., 0., 0.]

ode_kwargs = {
    'method': 'Radau',
    'atol': 1e-8,
    'rtol': 1e-8,
}

sol = solve_ivp(ode, [0.001, 99.999], init_cond, **ode_kwargs)

F = 10
V_1 = V_1_0 - F * sol.t
V_2 = F * sol.t

C_A1 = sol.y[0] / V_1
C_C1 = sol.y[1] / V_1
C_A2 = sol.y[2] / V_2
C_C2 = sol.y[3] / V_2

plt.plot(sol.t, C_A1, label=r"$C_{A1}/C_{B1}$")
plt.plot(sol.t, C_C1, label=r"$C_{C1}$")
plt.xlabel(r"$t$ (min)")
plt.ylabel(r"$C$ (M)")
plt.title("Problem 1 Reactor 1 Concentrations")
plt.legend()
plt.show()


plt.plot(sol.t, C_A2, label=r"$C_{A2}/C_{B2}$")
plt.plot(sol.t, C_C1, label=r"$C_{C2}$")
plt.xlabel(r"$t$ (min)")
plt.ylabel(r"$C$ (M)")
plt.title("Problem 1 Reactor 2 Concentrations")
plt.legend()
plt.show()