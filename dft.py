"""
Fourier Power vs Frequency

Performs Discrete Fourier Transform (DFT) with the efficient Fast Fourier Transform (FFT) algorithm
    https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html
Then take the square of the absolute value

"""

import numpy as np
import matplotlib.pyplot as plt


def fourierplt(x, y, F):
    fig, ax = plt.subplots()
    ax.semilogy(x, y)
    ax.set(xlabel="Frequency (Hz)", ylabel="Power",
           title="Fourier Freq = {}".format(F))
    ax.set_xlim([0, 20])


def fourier(F, N, T, noise=False):
    t = np.linspace(0, N, num=N, endpoint=False) / N
    t = t*T

    f = np.sin(2 * np.pi * F * t)
    if noise:
        f = f + 2 * np.random.randn(N)

    N = int(N/2)
    p = np.absolute(np.fft.fft(f)) / N
    p = p[0:N] ** 2
    freq = np.linspace(0, N, num=N, endpoint=False) / T

    return freq, p


def main():
    Frequency = [5, 10, 15]
    N = 10000
    T = 3.4

    for F in Frequency:
        freq, p = fourier(F, N, T, True)
        fourierplt(freq, p, F)

    plt.show()


if __name__ == '__main__':
    main()
