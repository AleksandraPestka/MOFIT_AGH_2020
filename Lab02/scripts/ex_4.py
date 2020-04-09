import math
import csv
import copy

import numpy as np
import pandas as pd

from config import *
from utils_calc import v_deriv
from ex_2 import rk4_method, calc_derivatives

if __name__ == '__main__':
    # params
    orbital_period = 75
    sec_in_year = 365.25*24*60*60
    number_lap = 3
    delta_t = 900 
    years = number_lap * orbital_period

    tolerance = 1000
    c = 0.9 # safety param
    n = 4 # numbers of parameters k[i]

    f = calc_derivatives

    # standard initial variable
    u = np.array([x_0, y_0, vx_0, vy_0])

    # additional variable (for dela_t/2)
    u2 = copy.deepcopy(u) 
    u3 = copy.deepcopy(u)
    
    # total time
    time_sum = 0   

    with open(f'../data/ex4_tol_{tolerance}.csv',"w+") as tmp_file:
        wr = csv.writer(tmp_file, quoting=csv.QUOTE_NONE)
        wr.writerow(['t', 'x', 'y', 'dt', 'r'])

        while time_sum < years:
            u3 = rk4_method(delta_t, n, u3, f)
            u2 = rk4_method(delta_t/2, n, u2, f)
            u2 = rk4_method(delta_t/2, n, u2, f)

            x_error = abs(u2[0] - u3[0])/(2**n-1)
            y_error = abs(u2[1] - u3[1])/(2**n-1)

            # take higher error value
            epsilon = x_error if x_error > y_error else y_error
                
            if epsilon < tolerance:
                time_sum += delta_t/sec_in_year

                # save data to file
                wr.writerow([time_sum, 
                            u3[0]/au, u3[1]/au, 
                            delta_t, 
                            np.power((u3[0]**2+u3[1]**2)/(au*au),0.5)])
                
                # update 
                u2 = copy.deepcopy(u3)
                u = copy.deepcopy(u3)

            else:
                u3 = copy.deepcopy(u)
                u2 = copy.deepcopy(u)

            # new delta time
            delta_t = c*delta_t* np.power((tolerance/epsilon), 0.2)
