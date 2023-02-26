import numpy as np
from scipy import linalg
import matplotlib.pylab as plt

k_1 = 0.1 
k_2 = 0.05
k_3 = 0.02
F = 10 
V = 100
C_R0s = 2

A = np.array([
    [-(F / V + k_1), 0, 0],
    [k_1, -(F / V + k_2), k_3],
    [0, k_2, -(F / V + k_3)],
])

B = np.array([
    [F/V],
    [0],
    [0],
]) 

Bu = B * C_R0s

sol = -linalg.solve(A, Bu)

print(sol)

M = 2

c_C_R = np.array([1, 0, 0])
c_C_I = np.array([0, 1, 0])
c_C_P = np.array([0, 0, 1])



t_plot = np.linspace(0, 15, 50)

def impusle(t, c):
    impulse_response = lambda t: M * (c @ linalg.expm(A * t) @ B)
    response = np.zeros(len(t))

    for i, val in enumerate(t):
        response[i] = impulse_response(val)[0]

    return response


plt.plot(t_plot, impusle(t_plot, c_C_I))
plt.plot(t_plot, impusle(t_plot, c_C_R))
plt.plot(t_plot, impusle(t_plot, c_C_P))

plt.show()



def step(t, c):
    step_response = lambda t: M * (c @ (linalg.expm(A * t) - np.eye(3)) @ linalg.inv(A) @ B)
    response = np.zeros(len(t))

    for i, val in enumerate(t):
        response[i] = step_response(val)[0]

    return response


plt.plot(t_plot, step(t_plot, c_C_R))
plt.plot(t_plot, step(t_plot, c_C_I))
plt.plot(t_plot, step(t_plot, c_C_P))

plt.show()