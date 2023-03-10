import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import solve_ivp

ode_kwargs = {
    'method': 'Radau',
    'atol': 1e-8,
    'rtol': 1e-8,
}

'''
####################
#      Part A      #
####################
'''

def ode_a(t, y):
    f = y*0

    C_A = y[0]
    C_B = y[1]
    C_C = y[2]

    k_1 = 0.4
    k_2 = 0.01
    k_b1 = 0.3
    k_b2 = 0.005

    r_1 = k_1 * C_A
    r_2 = k_2 * C_B

    f[0] = -r_1
    f[1] = r_1 - r_2
    f[2] = r_2

    return f

C_A0 = 1.6

init_cond = [C_A0, 0, 0]

sol_a = solve_ivp(ode_a, [0, 20], init_cond, **ode_kwargs)

plt.plot(sol_a.t, sol_a.y[0], label=r"$C_{A}$")
plt.plot(sol_a.t, sol_a.y[1], label=r"$C_{B}$")
plt.plot(sol_a.t, sol_a.y[2], label=r"$C_{C}$")
plt.title("Problem 2 Part a Concentration Plot")
plt.xlabel(r"$t$ (hr)")
plt.ylabel("Concentration (mol/L)")
plt.legend()
plt.show()

'''
####################
#      Part B      #
####################
'''

def ode_b(t, y):
    f = y*0

    C_A = y[0]
    C_B = y[1]
    C_C = y[2]

    k_1 = 0.4
    k_2 = 0.01
    k_b1 = 0.3
    k_b2 = 0.005

    r_1 = k_1 * C_A
    r_2 = k_2 * C_B
    r_b1 = k_b1 * C_B

    f[0] = -r_1 + r_b1
    f[1] = r_1 - r_2 - r_b1
    f[2] = r_2

    return f

C_A0 = 1.6

init_cond = [C_A0, 0, 0]

sol_b = solve_ivp(ode_b, [0, 20], init_cond, **ode_kwargs)

plt.plot(sol_b.t, sol_b.y[0], label=r"$C_{A}$")
plt.plot(sol_b.t, sol_b.y[1], label=r"$C_{B}$")
plt.plot(sol_b.t, sol_b.y[2], label=r"$C_{C}$")
plt.title("Problem 2 Part b Concentration Plot")
plt.xlabel(r"$t$ (hr)")
plt.ylabel("Concentration (mol/L)")
plt.legend()
plt.show()

'''
####################
#      Part C      #
####################
'''

def ode_c(t, y):
    f = y*0

    C_A = y[0]
    C_B = y[1]
    C_C = y[2]

    k_1 = 0.4
    k_2 = 0.01
    k_b1 = 0.3
    k_b2 = 0.005

    r_1 = k_1 * C_A
    r_2 = k_2 * C_B
    r_b1 = k_b1 * C_B
    r_b2 = k_b2 * C_C

    f[0] = -r_1 + r_b1
    f[1] = r_1 - r_2 - r_b1 + r_b2
    f[2] = r_2 - r_b2

    return f

C_A0 = 1.6

init_cond = [C_A0, 0, 0]

sol_c = solve_ivp(ode_c, [0, 20], init_cond, **ode_kwargs)

plt.plot(sol_c.t, sol_c.y[0], label=r"$C_{A}$")
plt.plot(sol_c.t, sol_c.y[1], label=r"$C_{B}$")
plt.plot(sol_c.t, sol_c.y[2], label=r"$C_{C}$")
plt.title("Problem 2 Part c Concentration Plot")
plt.xlabel(r"$t$ (hr)")
plt.ylabel("Concentration (mol/L)")
plt.legend()
plt.show()