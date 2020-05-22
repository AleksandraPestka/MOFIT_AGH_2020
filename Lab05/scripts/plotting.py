import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy

def plot_omega_convergence(df):
    plt.figure()
    plt.plot(df['omega'], df['iterations'], label=r'$\omega(iteration)$')
    plt.plot(1.92, 58, marker='o', markersize=5, color="red", label='optimum')
    plt.xlabel(r'$\omega$')
    plt.ylabel('no. of iterations')
    plt.grid()
    plt.legend()
    plt.show()

def plot_potential_for_optimum(df):
    plt.figure()
    x = np.unique(df['X'])
    y = np.unique(df['Y'])
    X, Y = np.meshgrid(x, y)
    Z = df['Phi'].values.reshape(len(x), len(y))
    cp = plt.contourf(X, Y, Z, levels=100, cmap='inferno')
    plt.colorbar(cp)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

if __name__ == '__main__':
    df1 = pd.read_csv('../data/ex1.csv', header=0)
    # plot_omega_convergence(df1)

    df2 = pd.read_csv('../data/ex1b.csv', header=0)
    plot_potential_for_optimum(df2)