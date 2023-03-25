from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import control

w = np.linspace(1e-3, 1e3, int(1e5))

# sys = control.zpk([], [0, -1/0.1, -1/10], 1)
# mag, phase, omega = control.bode_plot(sys, omega=w)
# plt.show()

# sys = control.zpk([-1/10], [-1, -1], 10)
# mag, phase, omega = control.bode_plot(sys, omega=w)
# plt.show()

sys = control.tf([-10, 1], [1, 2, 1])
mag, phase, omega = control.bode_plot(sys, omega=w)
plt.show()

# sys = control.tf([1], [9, 1.2, 10.03, 0.4, 1])
# mag, phase, omega = control.bode_plot(sys)
# plt.show()