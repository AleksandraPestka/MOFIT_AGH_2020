import numpy as np
import matplotlib.pyplot as plt

from utils import V, V_deriv, V_double_deriv
from config import E_0, v_0, m

def Newton_system(F, J, x, x0, v, v0, eps):
    """
    Solve nonlinear system F=0 by Newton's method.
    J is the Jacobian of F. Both F and J must be functions of x.
    At input, x holds the start value. The iteration continues
    until ||F|| < eps.
    """
    F_value = F(x, x0, v, v0)
    F_norm = np.linalg.norm(F_value, ord=2)  # l2 norm of vector
    
    iteration_counter = 0
    while abs(F_norm) > eps and iteration_counter < 100:
        delta = np.linalg.solve(J(x), -F_value)
        x = x + delta
        F_value = F(x)
        F_norm = np.linalg.norm(F_value, ord=2)
        iteration_counter += 1

    # Here, either a solution is found, or too many iterations
    if abs(F_norm) > eps:
        iteration_counter = -1
        
    return x, iteration_counter

def trapezoidal_method(x_init, v_init, delta_time, alpha, max_iter, epsilon):
    
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
    
    for _ in range(max_iter):
        while abs(F1(xn, x, vn, v)) > epsilon or abs(F2(xn, x, vn, v)) > epsilon:
            delta = np.linalg.solve(J(xn), F(xn, x, vn, v))
            xn += delta[0]
            vn += delta[1]
            
        x = xn
        v = vn
    
    return x
    


def main():
    time_step = 0.01
    alpha = 0                       #   damping factor
    precision = 10e-10              #   acceptable precision
    x_0 = 2.8325                    #   inital position
    max_iteration = int(10e3)       #   maximum iteration number

    x_solve = trapezoidal_method(x_0, v_0, 
                                        time_step, alpha, max_iteration, precision)
    print(x_solve)

if __name__ == "__main__":
    main()