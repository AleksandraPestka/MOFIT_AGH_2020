import numpy as np
import matplotlib.pyplot as plt
from itertools import product

from utils_calc import f, f_deriv, V, V_deriv
from utils_plot import plot_energy, plot_phase_diagram, plot_time_domain
from config import E_0, v_0, m
from ex_1 import newton_raphson_method

def Explicit_Euler_Method(V, V_deriv, time_max, delta_t, mass, v_0, x_0, 
                          damping_factor=None):
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

        if damping_factor == None:
            v = v_prev - V_deriv(x_prev)/m * delta_t
        else:
            v = v_prev - V_deriv(x_prev)/m * delta_t - damping_factor * v_prev * delta_t

        x_buffer.append(x)
        v_buffer.append(v)

    return x_buffer, v_buffer 

if __name__ == "__main__":
    time_limits = [100, 1000]    # time limits for phase diagram
    time_limit = [30]            # time limit for other plots
    time_steps = [0.01, 0.001]

    epsilon = 10e-8 # tolerance 
    max_iterations = 100

    # x_0 (root) calculation
    start_point = 3
    x_0, _ , _= newton_raphson_method(start_point, f, V_deriv, max_iterations, epsilon) # initial position

    #=============== EULER METHOD - NO DAMPING ==================#

    def Euler_Method_basic_plots(damping=None):
        ''' Go through computations and creating plots for each configuration of
            time limit and delta time. '''

        print(f"\n[INFO] Damping factor: {damping}")

        for time_max, delta_t in product(time_limit, time_steps):
            print(f"[INFO] Delta time: {delta_t}, max time: {time_max}")

            positions, velocities = Explicit_Euler_Method(V, V_deriv, time_max, 
                                                        delta_t, m, v_0, x_0, damping)

            time_vec = np.arange(time_max, step=delta_t)

            plot_time_domain(positions, velocities, time_vec)
            plot_energy(positions, velocities, V, m, time_vec)

        for time_max, delta_t in product(time_limits, time_steps):
            print(f"[INFO] Delta time: {delta_t}, max time: {time_max}")
            positions, velocities = Explicit_Euler_Method(V, V_deriv, time_max, 
                            delta_t, m, v_0, x_0, damping)
            plot_phase_diagram(positions, velocities)

    Euler_Method_basic_plots()

    #=============== EULER METHOD - DAMPING ==================#

    time_step_damping = 0.01
    damping_factor_list = [0.5, 5, 201]

    for damping_factor in damping_factor_list:
        # repeat computation and creating plots for each damping_factor 
        Euler_Method_basic_plots(damping=damping_factor)
