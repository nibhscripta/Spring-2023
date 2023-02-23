import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# constants
F_V = 0.5
k_1 = 3
k_b = 1.25
k_2 = 0.75

# matrices
A = np.array([
    [-(F_V + k_1), k_b],
    [k_1, -(F_V + k_2 + k_b)]
])
B = np.array([
    [F_V],
    [0]
])
C = np.array([0, 1])
D = 0

# define state space system
sys = signal.StateSpace(A, B, C, D)

# compute step/impulse response
t_step, y_step = sys.step()

t_impulse, y_impulse = sys.impulse()

# plot
plt.plot(t_step, y_step, label="Step response")
plt.plot(t_impulse, y_impulse, label="Impulse response")
plt.xlabel(r"t")
plt.ylabel(r"y(t)")
plt.title("Problem 4.2 CSTR with Reversible Reaction Response")
plt.legend()
plt.show()

# compute transfer function
transfer_func = sys.to_tf()

print(transfer_func)

# manually create system from transfer function
sys_manual = signal.lti(transfer_func.num, transfer_func.den)

# comput step/impulse response
t_step, y_step = sys_manual.step()

t_impulse, y_impulse = sys_manual.impulse()

plt.plot(t_step, y_step, label="Step response")
plt.plot(t_impulse, y_impulse, label="Impulse response")
plt.xlabel(r"t")
plt.ylabel(r"y(t)")
plt.title("Problem 4.2 CSTR with Reversible Reaction Response")
plt.legend()
plt.show()