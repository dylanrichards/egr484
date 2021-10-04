"""
Fourier Series Odd Function

"""

import matplotlib.pyplot as plt
import numpy as np


def seriesplt(x, y, N):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel="Time (t)", ylabel="f(t)", title="Fourier Series N = {}".format(N))
    fig.savefig("HW3_N{}".format(N))


def fourier_series(N):
    t = np.linspace(0, 1, num=100)

    f = 0.5
    oddn = range(1, N, 2)

    for n in oddn:
        a = 2 / (n * np.pi)
        f = f + a * np.sin(2 * n * np.pi * t)

    return t, f, N


def main():
    nvalues = [2, 5, 10, 20, 30, 50, 100]

    for n in nvalues:
        t, f, N = fourier_series(n)
        seriesplt(t, f, N)

    plt.show()


if __name__ == "__main__":
    main()
