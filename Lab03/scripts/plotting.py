import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_u(x, t, u):
    plt.figure()
    # gnuplot-like pm3d
    points = plt.scatter(x, t, c=u, cmap='seismic', vmin=-1, vmax=1)
    plt.colorbar(points)
    plt.xlabel('x')
    plt.ylabel('t[s]')
    plt.show()

def plot_energy(om, E):
    plt.figure()
    plt.plot(om, E)
    plt.xlabel(r'$\omega (t) [\pi \: rad]$')
    plt.ylabel(r'$<E> [J]$')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    df = pd.read_csv('../data/ex4.csv', header=None)
    plot_energy(df.iloc[:, 0], df.iloc[:, 1])

    # [INFO] while plotting ex3.csv remove vmin and vmax from plt.scatter