import pandas as pd
import matplotlib.pyplot as plt

def plot_time_domain(y_t, time_vec):
    plt.figure(figsize=(8,6))
    plt.plot(time_vec, y_t)
    plt.grid()
    plt.ylabel("y[au]")
    plt.xlabel("t[year]")
    plt.show()

def plot_location(x_t, y_t):
    plt.figure(figsize=(8,6))
    plt.plot(x_t, y_t, label="Halley's Comet")
    plt.scatter(0,0, marker='x', c='r', label='sun')
    plt.grid()
    plt.legend()
    plt.xlim([-30, 30])
    plt.ylabel("y[au]")
    plt.xlabel("x[au]")
    plt.show()

if __name__ == '__main__':
    dataframe = pd.read_csv('../data/ex2_dt_3600.csv', header=0)

    plot_location(dataframe['x'], dataframe['y'])
    plot_time_domain(dataframe['y'], dataframe['t'])