import math
import csv

import numpy as np
import pandas as pd

from config import *
from utils_calc import v_deriv

def Explicit_Euler_Method_auto_dt(delta_t,
                                    tolerance, save_param,
                                    x_init, y_init, 
                                    vx_init, vy_init, 
                                    sec_in_year):
    ''' Calculate x(t) and v(t) using Explicit Euler Method. 
    Output in AU unit. Use automatic delta time. Save data to csv file. '''
    
    # standard variables
    x, y = x_init, y_init
    vx, vy = vx_init, vy_init

    # additional variables (for delta/2)
    x2, y2 = x, y
    vx2, vy2 = vx, vy

    # total time
    time_sum = 0    

    # maximum number of years
    max_num_years = 75*3

    with open(f'../data/ex3_tol_{tolerance}.csv',"w+") as tmp_file:
        wr = csv.writer(tmp_file, quoting=csv.QUOTE_NONE)
        wr.writerow(['t', 'x', 'y', 'dt', 'r'])

        while time_sum < max_num_years:
            # calculations with dt
            x_next = x + vx*delta_t
            y_next = y + vy*delta_t
            r = math.sqrt(x**2+y**2)
            vx_next = vx + v_deriv(x, r)*delta_t
            vy_next = vy + v_deriv(y, r)*delta_t

            ## calculations with dt/2 

            # step k+1/2 
            x_next2 = x2 + vx2*delta_t/2
            y_next2 = y2 + vy2*delta_t/2
            r2 = math.sqrt(x2**2+y2**2)
            vx_next2 = vx2 + v_deriv(x2, r2)*delta_t/2
            vy_next2 = vy2 + v_deriv(y2, r2)*delta_t/2

            # step k+1
            x_next3 = x_next2 + vx_next2*delta_t/2
            y_next3 = y_next2 + vy_next2*delta_t/2

            x_error = abs(x_next3-x_next)
            y_error = abs(y_next3-y_next)

            # take higher error value
            epsilon = x_error if x_error > y_error else y_error
                
            if epsilon < tolerance:
                # update
                x2 = x_next
                y2 = y_next
                vx2 = vx_next
                vy2 = vy_next

                time_sum += delta_t/sec_in_year

                # save data to file
                wr.writerow([time_sum, 
                            x/au, y/au, 
                            delta_t, 
                            np.power((x_next**2+y_next**2)/(au*au),0.5)])

                x = x_next
                y = y_next
                vx = vx_next
                vy = vy_next

            # new delta time
            delta_t = c*delta_t* np.power((tolerance/epsilon), 0.5)

if __name__ == '__main__':
    # params
    orbital_period = 75
    sec_in_year = 365.25*24*60*60
    number_lap = 3
    delta_time = 900 # 60*2
    max_time = number_lap * orbital_period * sec_in_year

    tol = 10 # tolerance
    c = 0.9 # safety param

    Explicit_Euler_Method_auto_dt(delta_time, 
                                tol, c, 
                                x_0, y_0, 
                                vx_0, vy_0, 
                                sec_in_year)