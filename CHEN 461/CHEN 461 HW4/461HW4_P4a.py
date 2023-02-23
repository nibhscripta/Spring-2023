import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
import math, os

# load data
data_file = loadmat(f'{os.path.dirname(os.path.realpath(__file__))}\datafile.mat')

# low pass filter function
def lpf(t, y, tau_f):
    filt_y = y.copy()

    T_s = t[1] - t[0]
    f = 1 - math.exp(-T_s[0]/tau_f)

    # filter algorithm
    for i in range(1, len(y)-1):
        filt_y[i] = (1 - f) * filt_y[i-1,0] + f * y[i,0]

    return filt_y

# filter with different tau_f values
filt_1 = lpf(data_file['t'], data_file['y_data'], 1.3)
filt_2 = lpf(data_file['t'], data_file['y_data'], 2)
filt_3 = lpf(data_file['t'], data_file['y_data'], 0.5)

# plotting
plt.plot(data_file['t'], data_file['y_data'])
plt.plot(data_file['t'], filt_1, label=r"$\tau_f=1.3$")
plt.plot(data_file['t'], filt_2, label=r"$\tau_f=2$")
plt.plot(data_file['t'], filt_3, label=r"$\tau_f=0.5$")
plt.xlabel(r'$t$')
plt.ylabel('Response')
plt.legend()
plt.title('Problem 4 Filter Plot')
plt.show()