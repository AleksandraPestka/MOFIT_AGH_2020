import numpy as np
import matplotlib.pyplot as plt

def calc_position_and_velocity(V, V_deriv, time_max, delta_t, mass, v_0, x_0):
    ''' Calculate x(t) and v(t) using Explicit Euler Method. '''
    
    x_buffer = []
    v_buffer = []

    # add initial conditions to memory 
    x_buffer.append(x_0)
    v_buffer.append(v_0)
    
    for _ in range(int(time_max//delta_t)):
        # take the last elements
        x_prev = x_buffer[-1]   
        v_prev = v_buffer[-1]

        # update
        x = x_prev + v_prev * delta_t
        v = v_prev - V_deriv(x_prev)/m * delta_t

        x_buffer.append(x)
        v_buffer.append(v)

    return x_buffer, v_buffer 

def calc_kinetic_energy(v_t, mass):
    ''' Calculate kinetic energy Ek = mv^2/2 using v(t). '''

    return [0.5*mass*item**2 for item in v_t]

def calc_potential_energy(x_t, V):
    ''' Calculate potential energy using x(t) and V(x). '''

    return [V(x) for x in x_t]

def plot_time_domain(x_t, v_t, time_vec):
    ''' Plot v(t) and x(t) on one figure. '''

    plt.figure(figsize=(10,8))
    plt.plot(time_vec, x_t, label="x[m]")
    plt.plot(time_vec, v_t, label="v[m/s]")
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

def plot_kin_vs_potential_energy(x_t, v_t, V, mass, time_vec):
    ''' Plot kinetic energy and potential energy vs time. '''

    kin_energy = calc_kinetic_energy(v_t, mass)
    potential_energy = calc_potential_energy(x_t, V)

    plt.figure(figsize=(10,8))
    plt.plot(time_vec, kin_energy, label="Ek[J]")
    plt.plot(time_vec, potential_energy, label="V[J]")
    plt.grid()
    plt.legend()
    plt.xlabel("t[s]")
    plt.show()

def plot_sum_kin_potential_energy(x_t, v_t, V, mass, time_vec):
    ''' Plot sum of kinetic and potential energy over time. '''

    kin_energy = calc_kinetic_energy(v_t, mass)
    potential_energy = calc_potential_energy(x_t, V)
    total_energy = [sum(item) for item in zip(kin_energy, potential_energy)]

    plt.figure(figsize=(10,8))
    plt.plot(time_vec, total_energy, label="Ek + V[J]")
    plt.grid()
    plt.legend()
    plt.xlabel("t[s]")
    plt.show()


if __name__ == "__main__":
    time_limits = [100, 1000]    # time limits for phase diagram
    time_limit = [30]            # time limit for other plots
    time_steps = [0.01, 0.001]

    # initial conditions
    v_0 = 0                      # initial velocity 
    # TO DO: load this variable from the file
    x_0 = 2.8328820498299936     # initial position
    m = 1                        # mass

    # potential function
    V = lambda x: -np.exp(-x**2) - 1.2*np.exp(-(x-2)**2) 
    # derivative of potential function
    V_deriv = lambda x: 2*x*(np.exp(-x**2)) + 2.4*(x-2)*np.exp(-(x-2)**2)

    for time_max, delta_t in zip(time_limit, time_steps):
        positions, velocities = calc_position_and_velocity(V, V_deriv, time_max, 
                                delta_t, m, v_0, x_0)

        time_vec = np.arange(time_max, step=delta_t)

        plot_time_domain(positions, velocities, time_vec)
        plot_kin_vs_potential_energy(positions, velocities, V, m, time_vec)
        plot_sum_kin_potential_energy(positions, velocities, V, m, time_vec)


    # TO DO: correct phase diagram limit time !
    for time_max, delta_t in zip(time_limits, time_steps):
        plot_phase_diagram(positions, velocities)
