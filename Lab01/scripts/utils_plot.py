''' Plot functions for all scripts. '''

import matplotlib.pyplot as plt
import numpy as np

from utils_calc import calc_kinetic_energy, calc_potential_energy

def basic_plot(fun, start, stop, energy):
    """ Plot function in wide range. """

    x = np.linspace(start, stop, num=1000)
    y = [fun(item) for item in x]

    plt.figure(figsize=(10,8))
    plt.plot(x, y, label='$V(x)$')
    plt.axhline(y=energy, color='k', label='E')
    plt.grid()
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('V')
    plt.show()

def plot_fun(fun, start, stop, converging_points, energy):
    x = np.linspace(start, stop, num=1000)

    # y-values for function V(x)
    y_V =  [fun(item) for item in x]
    # y-values for converging points
    y_converged = [fun(item) for item in converging_points]

    plt.figure(figsize=(10,8))

    # plot potential function
    plt.plot(x, y_V, label='$V(x)$')
    # plot converging points
    plt.scatter(converging_points, y_converged, c='m')
    # plot initial energy
    plt.axhline(y=energy, color='k', label='E')

    # annotations (numerate each converged point)
    for index, (xs, ys) in enumerate(zip(converging_points, y_converged)):
        plt.annotate(index, (xs, ys), ha='right')

    plt.legend()
    plt.xlabel('X')
    plt.ylabel('V')
    plt.grid()
    plt.show()

def plot_convergence_tempo(fun, converging_points):
    y_converged = [fun(item) for item in converging_points]
    plt.figure(figsize=(10,8))
    # setting log scale must be before plotting
    # values x for which f(x)=0 are not allowed to plot because of log scale 
    plt.yscale('log') 
    plt.scatter(range(len(converging_points)), np.abs(y_converged))
    plt.xlabel('Iteration')
    plt.ylabel('|f(x)|')
    plt.grid()
    plt.show()

def plot_time_domain(x_t, v_t, time_vec):
    ''' Plot v(t) and x(t) on one figure. '''

    plt.figure(figsize=(10,8))
    plt.plot(time_vec, v_t, label="v[m/s]")
    plt.plot(time_vec, x_t, label="x[m]")
    plt.grid()
    plt.legend()
    plt.xlabel("t[s]")
    plt.show()

def plot_phase_diagram(x_t, v_t):
    ''' Plot phase diagram: v(t) vs x(t).'''

    plt.figure(figsize=(10,8))
    plt.plot(x_t, v_t)
    plt.grid()
    plt.xlabel("x[m]")
    plt.ylabel("v[m/s]")
    plt.show()

def plot_energy(x_t, v_t, V, mass, time_vec):
    ''' Plot kinetic energy and potential energy vs time. '''

    kin_energy = calc_kinetic_energy(v_t, mass)
    potential_energy = calc_potential_energy(x_t, V)
    total_energy = [sum(item) for item in zip(kin_energy, potential_energy)]

    plt.figure(figsize=(10,8))
    plt.plot(time_vec, kin_energy, label="Ek[J]")
    plt.plot(time_vec, potential_energy, label="V[J]")
    plt.plot(time_vec, total_energy, label="Ek + V[J]")
    plt.grid()
    plt.legend()
    plt.xlabel("t[s]")
    plt.show()