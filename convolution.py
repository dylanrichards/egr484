"""
Convolution
    https://numpy.org/doc/stable/reference/generated/numpy.convolve.html
Stem Plot
    https://matplotlib.org/stable/gallery/lines_bars_and_markers/stem_plot.html
   
"""

import numpy as np
import matplotlib.pyplot as plt


def convplt(x, y):
    fig, ax = plt.subplots()
    ax.stem(x, y)
    ax.set_title("Convolution")
    ax.set_xlabel("Time index n")
    ax.set_ylabel("Amplitude")


def convolution(a, v):
    con = np.convolve(a, v)

    n = np.linspace(0, len(con) - 1, num=len(con))

    print("Output sequence")
    print(con)

    return n, con


def main():
    a = input("Type in the first sequence = ")
    b = input("Type in the second sequence = ")

    alst = [int(item) for item in a.split()]
    blst = [int(item) for item in b.split()]

    n, con = convolution(alst, blst)

    convplt(n, con)
    plt.show()


if __name__ == '__main__':
    main()
