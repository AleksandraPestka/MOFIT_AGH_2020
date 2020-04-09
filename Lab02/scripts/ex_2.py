import math
import csv

import numpy as np
import pandas as pd

from config import *
from utils_calc import v_deriv

def rk4_method(dt, n, u, f):
    ''' Apply 4th order Runge Kutta Formulas to find next value of u matrix '''
    k1 = f(u)
    k2 = f(u + dt/2 * k1)
    k3 = f(u + dt/2 * k2)
    k4 = f(u + dt * k3)

    # update value of u matrix
    u = u + dt/6 * (k1 + 2*k2 + 2*k3 + k4)
    return u

def calc_derivatives(u_vec):
    r =  math.sqrt(u_vec[0]**2 + u_vec[1]**2)
    k = np.zeros(4)
    k[0] = u_vec[2]
    k[1] = u_vec[3]
    k[2] = v_deriv(u_vec[0], r)
    k[3] = v_deriv(u_vec[1], r)

    return k

if __name__ == "__main__":
    # params
    orbital_period = 75
    sec_in_year = 365.25*24*60*60
    number_lap = 3
    max_time = number_lap * orbital_period * sec_in_year
    n = 4 # numbers of parameters k[i]
    delta_time = 60*2
    N = math.ceil(max_time/delta_time) # number of iterations

    f = calc_derivatives

    # initial conditions
    u = np.array([x_0, y_0, vx_0, vy_0])
    t = 0

    with open(f'../data/ex2_dt_{delta_time}.csv',"w+") as tmp_file:
        wr = csv.writer(tmp_file, quoting=csv.QUOTE_NONE)
        wr.writerow(['t', 'x', 'y'])
        for i in range(N):
            u = rk4_method(delta_time, n, u, f)
            if i%10000 == 0:
                print(f'Iteration: {i}')
                wr.writerow([i*(delta_time/sec_in_year), u[0]/au, u[1]/au])
            t += delta_time
