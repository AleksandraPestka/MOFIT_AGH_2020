import numpy as np
import matplotlib.pyplot as plt
from itertools import product
import math

from utils_calc import (f, V, V_deriv, V_double_deriv, 
                        calc_kinetic_energy, calc_potential_energy)
from utils_plot import (plot_time_domain, plot_energy,
                         plot_convergence_tempo, plot_phase_diagram)
from config import v_0, m

def trapezoidal_method(x_init, v_init, delta_time, time_max, alpha, max_iter, epsilon):
    """
    Solve nonlinear system F=0 by trapezoidal method.
    J is the Jacobian of F. Both F and J must be functions of x.
    At input, x holds the start value. The iteration continues
    until ||F|| < eps.

    Calculate x(t) and v(t) using Trapezoidal Method.
    """

    def J(xn):
        """
        Calculate Jacobian matrix.

        Parameters:
        xn: float
            Position at time (n+1)
        """    
        return np.array(
            [[1, -delta_time/2], 
            [delta_time/(2*m)*V_double_deriv(xn), 1+delta_time/2*alpha]]
        )
    
    def F1(xn, x, vn, v):
        """
        Parameters:
        x: float
            Position at time n
        xn: float
            Position at time n+1
        v: float 
            Velocity at time n
        Vn: float
            Velocity at time n+1        
        """
        return xn - x - delta_time/2*(vn+v)

    def F2(xn, x, vn, v):
        """
        Parameters:
        x: float
            Position at time n
        xn: float
            Position at time n+1
        v: float 
            Velocity at time n
        Vn: float
            Velocity at time n+1        
        """
        return vn - v - delta_time/2*(-1/m*V_deriv(xn) - alpha*vn) \
            - delta_time/2*(-1/m*V_deriv(x) - alpha*v)

    def F(xn, x, vn, v):
        """ Make a matrix from functions: F1 and F2. """
        return np.array([-F1(xn, x, vn, v), -F2(xn, x, vn, v)])

    x = x_init
    v = v_init
    xn = x
    vn = v

    x_buffer = []
    v_buffer = []
    
    converging_points = []
    iter_counter = 0     

    for _ in range(int(math.ceil(time_max/delta_time))):     
        # add initial conditions to memory 
        x_buffer.append(xn)
        v_buffer.append(vn)

        while abs(F1(xn, x, vn, v)) > epsilon or abs(F2(xn, x, vn, v)) > epsilon: 
            if iter_counter < max_iter:
                iter_counter += 1
                delta = np.linalg.solve(J(xn), F(xn, x, vn, v))
                xn += delta[0]
                vn += delta[1]
                converging_points.append(xn)
            else: 
                break
        
        x = xn
        v = vn   
    
    return x, converging_points, iter_counter, x_buffer, v_buffer
    
def main():
    time_step = 0.01
    alpha = 0                        #   damping factor
    epsilon = 10e-10                 #   acceptable precision
    x_0 = 2.8325                     #   inital position
    max_iteration = 10e6             #   maximum iteration number

    #=============== TRAPEZOIDAL METHOD - CONVERGENCE ==================#

    x_0, converging_points, iter_counter, _, _ = trapezoidal_method(x_0, v_0, 
                                time_step, time_step, alpha, max_iteration, epsilon)
    print(f"V(x) = E for x = {x_0} after {iter_counter} iterations. ")             
    plot_convergence_tempo(f, converging_points)

    #=============== TRAPEZOIDAL METHOD - NO DAMPING ==================#
    time_limits = [100, 1000]    # time limits for phase diagram
    time_limit = [30]            # time limit for other plots
    time_steps = [0.01, 0.001]

    def trapezoidal_method_basic_plots(alpha):
        ''' Go through computations and creating plots for each configuration of
            time limit and delta time. '''

        print(f"\n[INFO] Damping factor: {alpha}")

        for time_max, delta_t in product(time_limit, time_steps):
            print(f"[INFO] Delta time: {delta_t}, max time: {time_max}")

            _, _, _, positions, velocities = trapezoidal_method(x_0, v_0, 
                                delta_t, time_max, alpha, max_iteration, epsilon)

            time_vec = np.arange(time_max, step=delta_t)

            plot_time_domain(positions, velocities, time_vec)
            plot_energy(positions, velocities, V, m, time_vec)

        for time_max, delta_t in product(time_limits, time_steps):
            print(f"[INFO] Delta time: {delta_t}, max time: {time_max}")
            _, _, _, positions, velocities = trapezoidal_method(x_0, v_0, 
                                delta_t, time_max, alpha, max_iteration, epsilon)
            plot_phase_diagram(positions, velocities)

    trapezoidal_method_basic_plots(alpha=0)

    #=============== TRAPEZOIDAL METHOD - DAMPING ==================#

    time_step_damping = 0.01
    damping_factor_list = [0.5, 5, 201]

    for damping_factor in damping_factor_list:
        # repeat computation and creating plots for each damping_factor 
        trapezoidal_method_basic_plots(alpha=damping_factor)

    
if __name__ == "__main__":
    main()