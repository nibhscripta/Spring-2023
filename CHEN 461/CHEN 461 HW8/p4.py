import numpy as np
import matplotlib.pyplot as plt
import control

T = 10
t = 0.1
k = 1

sys = k * control.tf([-T, 1], [t, 1, 0])
w = np.linspace(1e-3, 1e3, int(1e5))
mag, phase, omega = control.bode_plot(sys, omega=w)
plt.show()