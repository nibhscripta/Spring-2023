import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import fsolve

k = lambda T: np.exp(20000 * (1/400 - 1/T))
H = -80000 * 4.184
K_c = lambda T: 100 * np.exp(H/8.314 * (1/400 - 1/T))
tau = 10
X = lambda T: tau * k(T) / (1 + tau * k(T) * (1 + K_c(T)**-1))

G = lambda T: 80000 * X(T)
R = lambda T: 400 * (T - 310.5)

T_ran = np.linspace(310, 450, 100)

plt.plot(T_ran, G(T_ran), label=r"$G(T)$")
plt.plot(T_ran, R(T_ran), label=r"$R(T)$")
plt.xlabel("Temperature (K)")
plt.ylabel(r"$G(T)/R(T)$")
plt.title(r"Problem 4 $G(T)/R(T)$ Plot")
plt.legend()
plt.show()

point_1 = fsolve(lambda T: G(T) - R(T), [310])
point_2 = fsolve(lambda T: G(T) - R(T), [370])
point_3 = fsolve(lambda T: G(T) - R(T), [420])

print(f"Lower steady-state: {point_1[0]}\nMiddle steady-state: {point_2[0]}\nUpper steady-state: {point_3[0]}\n")
print(f"Upper steady state conversion: {X(point_3[0])}")