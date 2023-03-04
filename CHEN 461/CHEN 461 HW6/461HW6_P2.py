import numpy as np
import matplotlib.pylab as plt
from scipy.signal import lti, step, lsim

h_1_0 = 1.5
h_2_0 = 0.5

A = np.array([
    [-1, 1],
    [.5, -1.5]
])
B = np.array([
    [1],
    [0]
])
C_h1 = np.array([1, 0])
C_h2 = np.array([0, 1])
D = 0

sys_h1 = lti(A, B, C_h1, D)
sys_h2 = lti(A, B, C_h2, D)

# Part A
u = 0
t = np.linspace(0, 3, 50)

t_h1_a, h1_a, x1 = lsim(sys_h1, u, t, h_1_0)
t_h2_a, h2_a, x2 = lsim(sys_h2, u, t, h_2_0)

plt.plot(t_h1_a, h1_a, label=r"$h_1$")
plt.plot(t_h2_a, h2_a, label=r"$h_2$")
plt.xlabel(r"t")
plt.ylabel(r"h")
plt.title("Problem 6.7 Part a Response plot")
plt.legend()
plt.show()

# Part B
t_react = np.interp(0.2, np.flip(h2_a), np.flip(t_h2_a))
h_1_react = np.interp(t_react, t_h1_a, h1_a)
print(f"Time when h_2 = 0.2 m: {t_react} min")
print(f"h_1 at that time: {h_1_react}")

# Part C
t_h1_c, h1_c = step(sys_h1, X0=h_1_react)
t_h2_c, h2_c = step(sys_h2, X0=0.2)

plt.plot(t_h1_c, h1_c, label=r"$h_1$")
plt.plot(t_h2_c, h2_c, label=r"$h_2$")
plt.xlabel(r"t")
plt.ylabel(r"h")
plt.title("Problem 6.7 Part c Response plot")
plt.legend()
plt.show()

print(f"Final h_1 = {h1_c[-1]}")
print(f"Final h_2 = {h2_c[-1]}")