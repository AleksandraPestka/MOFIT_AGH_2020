import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.interpolate import griddata
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

if __name__ == '__main__':
    df = pd.read_csv('../data/ex3.csv', header=0)
    #df = pd.read_fwf('file:///home/alexandra/Desktop/Studia/semestr_6/MOFIT/Materialy_Kuby/Proejkt3/zad3.txt')
    #df.columns = ['x', 't', 'u']
    plot_u(df['x'], df['t'], df['u'])

    # [INFO] while plotting ex3.csv remove vmin and vmax from plt.scatter