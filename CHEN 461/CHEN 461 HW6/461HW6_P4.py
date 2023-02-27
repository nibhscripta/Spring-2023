import numpy as np
from scipy import linalg
import matplotlib.pylab as plt
import math


def steady_state_composition(A, B) -> None:
    C_R0s = 2

    Bu = B * C_R0s

    steady_state_solution = -linalg.solve(A, Bu)

    print(steady_state_composition)


def step_response(t, M, A, B, c):
    step_response_formula = lambda t: M * (c @ (linalg.expm(A * t) - np.eye(3)) @ linalg.inv(A) @ B)
    response = np.zeros(len(t))

    for i, val in enumerate(t):
        response[i] = step_response_formula(val)[0]

    return response


def ramp_response(t, M, A, B, c):
    ramp_response_formula = lambda t: M * (c @ ((linalg.expm(A * t) - np.eye(3)) @ linalg.inv(A) - t * np.eye(3)) @ linalg.inv(A) @ B)
    response = np.zeros(len(t))

    for i, val in enumerate(t):
        response[i] = ramp_response_formula(val)[0]

    return response


def sinusoidal_response(t, M, omega, A, B, c):
    sinusoidal_response_formula = lambda t: c @ (omega * linalg.expm(A * t) - A * math.sin(omega * t) - omega * np.eye(3) * math.cos(omega * t)) @ linalg.inv(np.linalg.matrix_power(A, 2) + omega**2 * np.eye(3)) @ B * M
    response = np.zeros(len(t))

    for i, val in enumerate(t):
        response[i] = sinusoidal_response_formula(val)[0]

    return response


# def zero_order_hold_discretization()


def plot_step_response(A, B):
    M = 2

    c_C_R = np.array([1, 0, 0])
    c_C_I = np.array([0, 1, 0])
    c_C_P = np.array([0, 0, 1])

    t_plot = np.linspace(0, 15, 50)

    plt.plot(t_plot, step_response(t_plot, M, A, B, c_C_R))
    plt.plot(t_plot, step_response(t_plot, M, A, B, c_C_I))
    plt.plot(t_plot, step_response(t_plot, M, A, B, c_C_P))

    plt.legend([r"$C_R$", r"$C_I$", r"$C_P$"])
    plt.show()


def plot_ramp_response(A, B):
    M = 0.5

    c_C_R = np.array([1, 0, 0])
    c_C_I = np.array([0, 1, 0])
    c_C_P = np.array([0, 0, 1])

    t_plot = np.linspace(0, 15, 50)

    plt.plot(t_plot, ramp_response(t_plot, M, A, B, c_C_R))
    plt.plot(t_plot, ramp_response(t_plot, M, A, B, c_C_I))
    plt.plot(t_plot, ramp_response(t_plot, M, A, B, c_C_P))

    plt.legend([r"$C_R$", r"$C_I$", r"$C_P$"])
    plt.show()


def plot_sinusoidal_response(A, B):
    M = 1 
    omega = 0.2

    c_C_R = np.array([1, 0, 0])
    c_C_I = np.array([0, 1, 0])
    c_C_P = np.array([0, 0, 1])

    t_plot = np.linspace(0, 15, 50)

    plt.plot(t_plot, sinusoidal_response(t_plot, M, omega, A, B, c_C_R))
    plt.plot(t_plot, sinusoidal_response(t_plot, M, omega, A, B, c_C_I))
    plt.plot(t_plot, sinusoidal_response(t_plot, M, omega, A, B, c_C_P))

    plt.legend([r"$C_R$", r"$C_I$", r"$C_P$"])
    plt.show()


def main():
    k_1 = 0.1 
    k_2 = 0.05
    k_3 = 0.02
    F = 10 
    V = 100

    A = np.array([
        [-(F / V + k_1), 0, 0],
        [k_1, -(F / V + k_2), k_3],
        [0, k_2, -(F / V + k_3)],
    ])

    B = np.array([
        [F/V],
        [0],
        [0],
    ]) 

    steady_state_composition(A, B)


    plot_step_response(A, B)


    plot_ramp_response(A, B)


    plot_sinusoidal_response(A, B)

if __name__ == "__main__":
    main()