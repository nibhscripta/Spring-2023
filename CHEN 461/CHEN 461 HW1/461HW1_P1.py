import numpy as np
from scipy.integrate import solve_ivp
import math
import matplotlib.pyplot as plt

def P_2_5_ODE(t, h):
  f = np.zeros(len(h))

  F_in = 1
  r = 1
  c_1 = 0.7
  c_2 = 0.8
  h_1, h_2 = h[0], h[1]

  f[0] = ( F_in - c_1 * pow(h_1, 0.5) ) / ( math.pi * pow(r, 2) )
  f[1] = ( c_1 * pow(h_1, 0.5) - c_2 * pow(h_2, 0.5) ) / ( math.pi * pow(r, 2) )

  return f

h_initial = (0.1, 0.1)

t_final_min = 100

P_2_5_solution = solve_ivp(P_2_5_ODE, [0, t_final_min], h_initial, method="Radau", rtol = 1e-8, atol = 1e-8)

plt.plot(P_2_5_solution.t, P_2_5_solution.y[0])
plt.plot(P_2_5_solution.t, P_2_5_solution.y[1])
plt.xlabel("Time (min)")
plt.ylabel("Tank height (m)")
plt.title("Problem 2.5 Solution")
plt.legend(["Tank 1", "Tank 2"], loc="lower right")
plt.show()