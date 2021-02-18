"""
Cross Correlation
    https://numpy.org/doc/stable/reference/generated/numpy.correlate.html
Stem Plot
    https://matplotlib.org/stable/gallery/lines_bars_and_markers/stem_plot.html

"""

import numpy as np
import matplotlib.pyplot as plt


def corrplt(x, y):
    fig, ax = plt.subplots()
    ax.stem(x, y)
    ax.set_title("Cross-Correlation")
    ax.set_xlabel("Lag index")
    ax.set_ylabel("Amplitude")


def crosscorr(a, v):
    corr = np.correlate(a, v, "full")

    n1 = (len(v) - 1) * -1
    n2 = len(a) - 1
    n = np.linspace(n1, n2, num=len(corr))

    print(corr)

    return n, corr


def main():
    a = input("Type in the reference sequence = ")
    b = input("Type in the second sequence = ")

    x = [int(item) for item in a.split()]
    y = [int(item) for item in b.split()]

    n, corr = crosscorr(x, y)

    corrplt(n, corr)
    plt.show()


if __name__ == '__main__':
    main()
