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

def plot_dt_vs_r(r, dt):
    plt.figure(figsize=(8,6))
    plt.plot(r, dt, label=r'$dt(\sqrt{x^2+y^2})$')
    plt.grid()
    plt.legend()
    plt.ylabel("dt[s]")
    plt.xlabel("r[au]")
    plt.show()

if __name__ == '__main__':
    file_paths = ['../data/ex2_dt_120.csv',
                '../data/ex3_tol_1000.csv',
                '../data/ex3_tol_10.csv']

    for path in file_paths:
        dataframe = pd.read_csv(path, header=0)
        plot_location(dataframe['x'], dataframe['y'])
        plot_time_domain(dataframe['y'], dataframe['t'])

        if 'tol' in path:
            plot_dt_vs_r(dataframe['r'], dataframe['dt'])