import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

sys = signal.lti([1, 1, 0], [1, 4, 4])


t_step, y_step = signal.step(sys)

step_analytical = lambda t: (1 - t) * np.exp(-2 * t)

plt.plot(t_step, y_step, label="Simulated Response")
plt.plot(t_step, step_analytical(t_step), "--", label="Analytical Response")
plt.xlabel(r"$t$")
plt.ylabel(r"$y(t)$")
plt.title("Problem 8.1 Verify Analytical Step Response")
plt.legend()
plt.show()

t_ramp = np.linspace(0, 10, 100)
u_ramp = t_ramp

t_ramp, y_ramp, _ = signal.lsim(sys, u_ramp, t_ramp)

plt.plot(t_ramp, y_ramp, label="Simulated Response")
plt.xlabel(r"$t$")
plt.ylabel(r"$y(t)$")
plt.title("Problem 8.1 Verify Analytical Ramp Response")
plt.legend()
plt.show()

# for ω=1

sin_analytical = lambda t: np.sin(t) / 25 + np.cos(t) * 7 / 25

t_sin = np.linspace(0, 20, 100)
u_sin  = np.sin(t_sin)

t_sin, y_sin, _ = signal.lsim(sys, u_sin, t_sin)

plt.plot(t_sin, y_sin, label="Simulated Response")
plt.plot(t_sin, sin_analytical(t_sin), '--', label="Analytical Response")
plt.xlabel(r"$t$")
plt.ylabel(r"$y(t)$")
plt.title("Problem 8.1 Verify Analytical Sinusoidal Response")
plt.legend()
plt.show()