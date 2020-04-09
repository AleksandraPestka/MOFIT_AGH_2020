import pandas as pd
import matplotlib.pyplot as plt

def plot_time_domain(y1, t1, label1, 
                    y2, t2, label2):
    ''' Compare y(t) for 2 dataset on the plot. '''
    plt.figure(figsize=(8,6))
    plt.plot(t1, y1, label=label1, c='k')
    plt.plot(t2, y2, label=label2, linestyle='-', c='r')
    plt.grid()
    plt.ylabel("y[au]")
    plt.xlabel("t[year]")
    plt.legend()
    plt.show()

def plot_location(x1, y1, label1,
                 x2, y2, label2):
    ''' Compare y(x) for 2 dataset on the plot. '''
    plt.figure(figsize=(8,6))
    plt.plot(x1, y1, label=label1, c='k')
    plt.plot(x2, y2, label=label2, linestyle=':', c='r')
    plt.scatter(0,0, marker='x', c='y', label='sun')
    plt.grid()
    plt.legend()
    plt.xlim([-30, 30])
    plt.ylabel("y[au]")
    plt.xlabel("x[au]")
    plt.show()

def plot_dt_vs_r(r1, dt1):
    ''' Plot dt(r) for 1 dataset. '''
    plt.figure(figsize=(8,6))
    plt.plot(r1, dt1, label=r'$dt(\sqrt{x^2+y^2})$')
    plt.grid()
    plt.legend()
    plt.ylabel("dt[s]")
    plt.xlabel("r[au]")
    plt.show()

if __name__ == '__main__':
    df1 = pd.read_csv('../data/ex1_dt_120.csv', header=0)
    df2 = pd.read_csv('../data/ex2_dt_120.csv', header=0)

    plot_time_domain(df1['y'], df1['t'], 'Euler method',
                    df2['y'], df2['t'], 'RK4 method')
    plot_location(df1['x'], df1['y'], 'Euler method',
                df2['x'], df2['y'], 'RK4 method')
