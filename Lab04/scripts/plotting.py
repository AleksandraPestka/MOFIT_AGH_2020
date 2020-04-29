import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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

if __name__ == '__main__':
    df = pd.read_csv('../data/ex1.csv', header=0, index_col=None)
    plot_moments_vs_number_of_steps(df)
