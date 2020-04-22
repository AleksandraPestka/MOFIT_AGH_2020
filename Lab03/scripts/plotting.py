import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.interpolate import griddata
import pandas as pd
import numpy as np

def plot_u(x, t, u):
    # works well, but the data is wrong
    plt.figure()
    points = plt.scatter(x, t, c=u, cmap='seismic', vmin=-1, vmax=1)
    plt.colorbar(points)
    plt.xlabel('x')
    plt.ylabel('t[s]')
    plt.show()

if __name__ == '__main__':
    df = pd.read_csv('../data/ex1_stiff.csv', header=0)
    #df = pd.read_fwf('file:///home/alexandra/Desktop/Studia/semestr_6/MOFIT/Materialy_Kuby/Proejkt3/zad1 (copy).txt')
    #df.columns = ['x', 't', 'u']
    plot_u(df['x'], df['t'], df['u'])