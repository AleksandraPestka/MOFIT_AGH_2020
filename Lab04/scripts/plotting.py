import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

from ex2 import wave_func

def plot_moments_vs_number_of_steps(dataframe):
    plt.figure()
    plt.xscale('log')

    for i in np.arange(1,5):
        plt.plot(dataframe['l'], dataframe.iloc[:, i], label=f'$I_{{{i}}}$')
   
    plt.legend()
    plt.grid()
    plt.xlabel('no. of steps')
    plt.ylabel('moment value')
    plt.show()

def plot_random_walk(no_steps, dist_fun, x_list, y_list):
    x_vals = np.linspace(-3, 3, 1000)
    y_vals = np.linspace(-3, 3, 1000)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = [dist_fun(i,j) for (i,j) in zip(X, Y)]

    plt.figure()
    cp = plt.contourf(X, Y, Z)
    plt.colorbar(cp, label='distribution function values')
    plt.plot(x_list[:no_steps], y_list[:no_steps], c='k', 
             alpha=0.5, label='random walk')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

def plot_energy_vs_number_of_steps(dataframe):
    plt.figure()
    plt.xscale('log')
    plt.plot(dataframe['l'], dataframe['E'])   
    plt.legend()
    plt.grid()
    plt.xlabel('no. of steps')
    plt.ylabel('E')
    plt.show()

if __name__ == '__main__':
    df = pd.read_csv('../data/ex1.csv', header=0, index_col=None)
    plot_moments_vs_number_of_steps(df)

    df2 = pd.read_csv('../data/ex2.csv', header=0, index_col=None)
    plot_random_walk(10000, wave_func, df2['x'], df2['y'])

    df3 = pd.read_csv('../data/ex2_energy.csv', header=0, index_col=None)
    plot_energy_vs_number_of_steps(df3)