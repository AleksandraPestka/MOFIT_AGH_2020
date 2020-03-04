import numpy as np
import matplotlib.pyplot as plt

def bisection_method(f, a, b, n_iter):
    '''
    Root finding method especially for non-linear equation. 
    Approximate solution of f(x)=0 on interval <a,b> based on the function sign only.

    Parameters:
    f : function for which we are trying to approximate a solution f(x)=0
    a, b: float
        The interval in which to search for a solution. 
    n_iter: int
            Number of iteration to implement. 
    '''
    points_buffer = []

    if f(a)*f(b) >= 0:
        print("[INFO] Failed!")

    for _ in np.arange(1, n_iter+1):
        m = (a+b)/2 # mid point

        if f(a)*f(m) < 0:
            b = m
        
        elif f(b)*f(m) < 0:
            a = m

        elif f(m) == 0:
            print("[INFO] Exact solution founded!")
            return m, points_buffer

        else:
            print("[INFO] Failed!")
            return None

        points_buffer.append(m)

    print("[INFO] Too few iteration to converge!")
    return (a+b)/2, points_buffer

def newton_raphson_method(x, f, f_deriv):
    '''
    Newton Raphson root finding method.

    Parameters:
    x: float 
        Point to start with.
    f: function for which we are trying to approximate a solution f(x)=0
    f_deriv: derivative of function f
    ''' 

    points_buffer = []

    h = f(x) / f_deriv(x)
    while f(x)!=0 and f_deriv(x)!=0:
        # update according to :  x(i+1) = x(i) - f(x) / f'(x) 
        points_buffer.append(x)
        x = x - h
        h = f(x)/f_deriv(x)
    
    return x, points_buffer

def plot_fun(fun, start, stop, converging_points, energy):
    x = np.linspace(start, stop, num=1000)

    # y-values for function f
    y_f =  [(fun(item)+energy) for item in x]
    # y-values for converging points
    y_converged = [(fun(item)+energy) for item in converging_points]

    plt.figure(figsize=(10,8))

    # plot potential function
    plt.plot(x, y_f, label='$V(x)$')
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
    # values x for which f(x)=0 are no allowed to plot because of log scale 
    plt.yscale('log') 
    plt.scatter(range(len(converging_points)), np.abs(y_converged))
    plt.xlabel('Iteration')
    plt.ylabel('|f(x)|')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # initial conditions
    v_0 = 0
    E_0 = -0.6

    # potential function
    f = lambda x: -np.exp(-x**2) - 1.2*np.exp(-(x-2)**2) - E_0
    # derivative of potential function
    deriv_f = lambda x: 2*x*(np.exp(-x**2)) + 2.4*(x-2)*np.exp(-(x-2)**2)

    #=============== BISECTION METHOD ==================#

    print("[INFO] Bisection method ")

    intervals = [(-1,0), (2,4)]
    iterations = 100

    roots_buffer_bisection = []

    for interv_begin, interv_end in intervals:
        # convergence time counting
        root, converged_points = bisection_method(f, interv_begin, interv_end, iterations)
        
        roots_buffer_bisection.append(root)
        
        plot_fun(f, interv_begin, interv_end, converged_points, E_0)
        plot_convergence_tempo(f, converged_points)

    print(f"\nV(x) <= E for x in {roots_buffer_bisection}")

    #=============== NETWON-RAPHSON METHOD ==================#

    print("\n[INFO] Newton-Raphson method ")
    
    start_points = [-0.7, 3]
    roots_buffer_newton = []

    for value, (interv_begin, interv_end) in zip(start_points, intervals):
        root, converged_points = newton_raphson_method(value, f, deriv_f)
        roots_buffer_newton.append(root)
        
        plot_fun(f, interv_begin, interv_end, converged_points, E_0)
        plot_convergence_tempo(f, converged_points)

    print(f"\nV(x) <= E for x in {roots_buffer_newton}")
