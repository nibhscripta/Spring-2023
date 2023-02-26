import numpy as np
import matplotlib.pylab as plt
from scipy.signal import lti, step, lsim

def main():
    A_1 = 1
    A_2 = 2
    F_in = 1
    h_1 = 1.5
    h_2 = 0.5

    A = np.array([
        [-1 / A_1, 1 / A_1],
        [1 / A_2, -2 / A_2]
    ])
    B = np.array([
        [1 / A_1],
        [0]
    ])
    C = np.array([0, 1])
    D = 0

    t_input = np.linspace(0, 20, 100)
    u = 0

    sys_h2 = lti(A, B, C, D)
    t_1, y_1, x = lsim(sys_h2, u, t_input, X0=h_2)
    plt.plot(t_1, y_1, label=r"$h_2$")
    t_interp = np.interp(0.2, np.flip(y_1), np.flip(t_1))
    # plt.plot(t_interp, 0.2, 'rx')

    print(f"h_2 reaches 0.2 m in {round(t_interp, 4)} min.")

    C = np.array([1, 0])
    sys_h1 = lti(A, B, C, D)
    t_2, y_2, x = lsim(sys_h1, u, t_input, X0=h_1)
    plt.plot(t_2, y_2, label=r"$h_1$")
    h1_interp = np.interp(t_interp, t_2, y_2)
    # plt.plot(t_interp, h1_interp, 'gx')
    print(f"h_1 is {round(h1_interp, 4)} m at that time.")

    plt.xlim([0, t_interp])
    plt.title("Part 1")
    plt.legend()
    plt.show()

    t_input = np.linspace(0, 20, 100)
    u = F_in * np.ones(len(t_input))


    t_1, y_1, x = lsim(sys_h2, u, t_input, X0=0.2)
    plt.plot(t_1, y_1, label=r"$h_2$")


    t_2, y_2, x = lsim(sys_h1, u, t_input, X0=h1_interp)
    plt.plot(t_2, y_2, label=r"$h_1$")

    plt.title("Part 2")
    plt.legend()
    plt.show()

    print(f"After the alarm, h_1 reaches {round(y_2[-1], 4)} m, and h_2 reaches {round(y_1[-1], 4)} m.")

if __name__ == "__main__":
    main()