import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, trapezoid
# ODE function for Problem 4
def P_4_ODE(t, w):
    # init ode array
    f = np.zeros(len(w))
    # define x & y from input array
    x = w[0]
    y = w[1]
    # define constants
    k_1 = 0.02
    k_2 = 0.00004
    k_3 = 0.00004
    k_4 = 0.04
    # define ode system
    f[0] = k_1 * x - k_2 * x * y
    f[1] = k_3 * x * y - k_4 * y
    # return system as an array
    return f

# set initial condition
xy_initial = (500, 200)
# final time
t_final_days = 800
# solve ODE system
P_4_solution = solve_ivp(P_4_ODE, [0, t_final_days], xy_initial, method="Radau", rtol = 1e-6, atol = 1e-6)
# plotting
fig, ax = plt.subplots(2, dpi=100, figsize=(6.4,9.6))
# solution arrays
ax[0].plot(P_4_solution.t, P_4_solution.y[0])
ax[0].plot(P_4_solution.t, P_4_solution.y[1])
# labels
ax[0].set_xlabel("Time (days)")
ax[0].set_ylabel("Number of animals")
ax[0].set_title("Problem 4 Solution")
ax[0].legend(["rabbits", "foxes"], loc="upper right")
# second plot
ax[1].plot(P_4_solution.y[0], P_4_solution.y[1])
ax[1].set_xlabel("Rabbits")
ax[1].set_ylabel("Foxes")
ax[1].set_title("Rabbits v Foxes Plot")
plt.show()
# save figure to image
plt.savefig(fname="P_4_figure1.png", dpi=150)
# Aggie Honor Code: An Aggie does not lie, cheat, or steal or tolerate
# those who do.
# I certify that this work is my own and not the work of another.
#
# Name: Mark Levchenko
# Assignment #: HW 1
# Question #: 4