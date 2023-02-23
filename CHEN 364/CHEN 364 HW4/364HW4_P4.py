import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def ode(t, y):
    N_A = y[0]
    N_B = y[1]
    V = y[4]
    
    f = np.zeros(len(y))

    C_B0 = 1.5
    F_B0 = 6
    k = 5.1
    M_E = 44.0095
    rho_E = 1000
    v_0 = F_B0 / C_B0

    r = k * N_A * N_B / V**2

    f[0] = -r * V
    f[1] = F_B0 - r * V
    f[2] = r * V
    f[3] = r * V
    f[4] = v_0 - r * V * M_E / rho_E

    return f


ode_kwargs = {
    "method": 'Radau',
    'rtol': 1e-8,
    'atol': 1e-8,
}    

N_A0 = 0.75*1500

initial_cond = [N_A0, 0, 0, 0, 1500]

solution = solve_ivp(ode, [0, 262], initial_cond, **ode_kwargs)

for i in range(4):
    plt.plot(solution.t, solution.y[i]/solution.y[4])

plt.legend([r'$C_A$', r'$C_B$', r'$C_C$', r'$C_D$'])
plt.xlabel(r"$t$ (hr)")
plt.ylabel(r"$C_j$ (mol/L)")
plt.title('Problem 4a Concentration Plot')
print(solution.y[4][-1])
plt.show()

plt.plot(solution.t, 1 - solution.y[0]/solution.y[4]/1.5)
plt.xlabel(r"$t$ (hr)")
plt.ylabel(r"$X$")
plt.title('Problem 4a Conversion Plot')
plt.show()