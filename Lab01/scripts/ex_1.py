import numpy as np
import matplotlib.pyplot as plt

from utils import f, f_deriv, V, V_deriv
from config import E_0, v_0

def bisection_method(f, a, b, max_iter, epsilon):
    '''
    Root finding method especially for non-linear equation. 
    Approximate solution of f(x)=0 on interval <a,b> based on the function sign only.

    Parameters:
    f : function for which we are trying to approximate a solution f(x)=0
    a, b: float
        The interval in which to search for a solution. 
    max_iter: int
        Number of iteration to implement. 
    epsilon: float
        Precision parameter. 
    '''
    points_buffer = []

    if f(a)*f(b) >= 0:
        print("[INFO] Interval is not right assumed!")
        return None

    iter_counter = 0 
    while ((abs(a-b) > epsilon) and (iter_counter < max_iter)) :
        # find middle point
        m = (a+b)/2 

        if abs(f(m)) <= epsilon:
            print("[INFO] Exact solution founded!")
            return m, points_buffer, iter_counter

        if f(a)*f(m) < 0:
            b = m
        
        elif f(b)*f(m) < 0:
            a = m

        else:
            print("[INFO] Failed!")
            return None

        points_buffer.append(m)
        iter_counter += 1

    print("[INFO] Exact solution NOT founded!")
    return m, points_buffer, iter_counter

def newton_raphson_method(x_init, f, f_deriv, max_iter, epsilon):
    '''
    Newton Raphson root finding method.

    Parameters:
    x_init: float 
        Point to start with.
    f: function for which we are trying to approximate a solution f(x)=0
    f_deriv: derivative of function f
    max_iter: int
        Number of iteration to implement. 
    epsilon: float
        Precision parameter. 
    ''' 

    points_buffer = []
    iter_counter = 0

    x = x_init
    for _ in range(max_iter):
        if abs(f(x)) < epsilon:
            return x, points_buffer, iter_counter
        if f_deriv(x) == 0:
            print('[INFO] Failed. Zero derivative.')
            return None
        
        # update according to :  x(i+1) = x(i) - f(x) / f'(x) 
        points_buffer.append(x)
        h = f(x)/f_deriv(x)
        x = x - h
        iter_counter += 1
    
    return x, points_buffer, iter_counter

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
    plt.scatter(converged_points, y_converged, c='m')
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

if __name__ == "__main__":

    intervals = [(-1,0), (2,4)]
    epsilon = 10e-8 # tolerance 
    max_iterations = 100

    # plot whole function
    basic_plot(V, intervals[0][0], intervals[1][1], E_0)


    #=============== BISECTION METHOD ==================#

    print("[INFO] Bisection method ")

    for interv_begin, interv_end in intervals:
        # convergence time counting
        root, converged_points, iter_counter = \
        bisection_method(f, interv_begin, interv_end, max_iterations, epsilon)

        print(f"V(x) = E for x = {root} after {iter_counter+1} iterations. ")
                
        plot_fun(V, interv_begin, interv_end, converged_points, E_0)
        plot_convergence_tempo(f, converged_points)

    #=============== NETWON-RAPHSON METHOD ==================#

    print("\n[INFO] Newton-Raphson method ")
    
    start_points = [-0.7, 3]

    for value, (interv_begin, interv_end) in zip(start_points, intervals):
        root, converged_points, iter_counter = \
        newton_raphson_method(value, f, f_deriv, max_iterations, epsilon)

        print(f"V(x) = E for x = {root} after {iter_counter+1} iterations. ")

        plot_fun(V, interv_begin, interv_end, converged_points, E_0)
        plot_convergence_tempo(f, converged_points)

