import numpy as np
import matplotlib.pyplot as plt

from utils import V, V_deriv, V_double_deriv
from config import E_0, v_0, m

def trapezoidal_method(x_init, v_init, delta_time, alpha, max_iter, epsilon):
    """
    Solve nonlinear system F=0 by trapezoidal method.
    J is the Jacobian of F. Both F and J must be functions of x.
    At input, x holds the start value. The iteration continues
    until ||F|| < eps.
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

    for num_attempt in range(max_iter):
        print(f"\nAttempt number: {num_attempt}")
        iter_counter = 0
        while abs(F1(xn, x, vn, v)) > epsilon or abs(F2(xn, x, vn, v)) > epsilon:
            delta = np.linalg.solve(J(xn), F(xn, x, vn, v))
            print("Delta: ", delta) 
            xn += delta[0]
            vn += delta[1]
            iter_counter += 1

        print(f"Number of iterations to converge: {iter_counter}")
        x = xn
        v = vn
    
    return x
    
def main():
    time_step = 0.001
    alpha = 0                       #   damping factor
    epsilon = 10e-8                 #   acceptable precision
    x_0 = 2.8325                    #   inital position
    max_iteration = 5               #   maximum iteration number

    x_solve = trapezoidal_method(x_0, v_0, 
                                time_step, alpha, max_iteration, epsilon)
    print("\nX computed solution: ", x_solve)

if __name__ == "__main__":
    main()