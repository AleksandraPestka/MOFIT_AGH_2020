''' Plot functions for all scripts. '''

import matplotlib.pyplot as plt
import numpy as np

def plot_time_domain(y_t, time_vec):
    plt.figure(figsize=(10,8))
    plt.plot(time_vec, y_t, label="y[au]")
    plt.grid()
    plt.legend()
    plt.ylabel("y[au]")
    plt.xlabel("t[year]")
    plt.show()

def plot_location(x_t, y_t):
    plt.figure(figsize=(10,8))
    plt.plot(x_t, y_t)
    plt.grid()
    plt.legend()
    plt.ylabel("y[au]")
    plt.xlabel("x[au]")
    plt.show()