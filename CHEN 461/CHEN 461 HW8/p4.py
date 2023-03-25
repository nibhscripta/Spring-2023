import numpy as np
import matplotlib.pyplot as plt
import control

# parameters
T = 10
tau = 0.1
k = 1

# bode
sys = k * control.tf([-T, 1], [tau, 1, 0])
w = np.linspace(1e-3, 1e3, int(1e5))
mag, phase, omega = control.bode_plot(sys, omega=w)
plt.show()