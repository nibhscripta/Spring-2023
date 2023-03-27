import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import fsolve

plt.grid(visible=True, which='both', axis='both')

# Definitions
X = lambda K: np.sqrt(K) / (1 + np.sqrt(K))
K = lambda T: 500000 * np.exp(-30000 * 4.184/8.314 * (1/(50+273.15) - 1/T))
T = lambda X: 600 * X + 300.15
X_T = lambda T: (T - 300.15) / 600

# Equilibrium plot
T_ran = np.linspace(300, 550, 100)
plt.plot(T_ran, X(K(T_ran)), label="Equilibrium")

# Reactor 1
def sys1(x):
    f = x*0

    f[0] = T(x[1]/0.999) - x[0]
    f[1] = X(K(x[0])) - x[1]/0.999

    return f

point_1 = fsolve(sys1, [300, 0.3])

T_r1 = np.linspace(300, point_1[0], 100)

plt.plot(T_r1, X_T(T_r1), color="tab:orange", label="Reactor 1")
plt.plot(point_1[0], point_1[1], 'o', color="tab:orange")
plt.plot(T_r1, np.ones(len(T_r1))*point_1[1], '--', color="tab:orange")

# Reactor 2
def sys2(x):
    f = x*0

    f[0] = T(x[1]/0.999 - point_1[1]) - x[0]
    f[1] = X(K(x[0])) - x[1]/0.999

    return f

point_2 = fsolve(sys2, [point_1[0], 0.5])

T_r2 = np.linspace(300, point_2[0], 100)

plt.plot(T_r2, X_T(T_r2)+point_1[1], color="tab:green", label="Reactor 2")
plt.plot(point_2[0], point_2[1], 'o', color="tab:green")
plt.plot(T_r2, np.ones(len(T_r2))*point_2[1], '--', color="tab:green")

# Reactor 3
def sys3(x):
    f = x*0

    f[0] = T(x[1]/0.999 - point_2[1]) - x[0]
    f[1] = X(K(x[0])) - x[1]/0.999

    return f

point_3 = fsolve(sys3, [point_2[0], 0.5])

T_r3 = np.linspace(300, point_3[0], 100)

plt.plot(T_r3, X_T(T_r3)+point_2[1], color="tab:red", label="Reactor 3")
plt.plot(point_3[0], point_3[1], 'o', color="tab:red")
plt.plot(T_r3, np.ones(len(T_r3))*point_3[1], '--', color="tab:red")

# Reactor 4
def sys4(x):
    f = x*0

    f[0] = T(x[1]/0.999 - point_3[1]) - x[0]
    f[1] = X(K(x[0])) - x[1]/0.999

    return f

point_4 = fsolve(sys4, [point_3[0], 0.5])

T_r4 = np.linspace(300, point_4[0], 100)

plt.plot(T_r4, X_T(T_r4)+point_3[1], color="tab:purple", label="Reactor 4")
plt.plot(point_4[0], point_4[1], 'o', color="tab:purple")

plt.title("Problem 3 Reactor Conversion v Temperature")
plt.xlabel("Temperature (K)")
plt.ylabel("Conversion")
plt.legend()
plt.show()

print(f"Maximum conversion: {point_4[1]}")