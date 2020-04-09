import math

import numpy as np
import pandas as pd

from config import *
from utils_calc import v_deriv
from plotting import plot_location, plot_time_domain

def Explicit_Euler_Method(time_max, delta_t, 
                          x_init, y_init, 
                          vx_init, vy_init, 
                          sec_in_year):
    ''' Calculate x(t) and v(t) using Explicit Euler Method. 
    Output in AU unit. '''

    buffer = pd.DataFrame(data={'t':[0], 
                                'x': [x_init/au], 
                                'y': [y_init/au]})
    vx_next = 0
    vy_next = 0
    x = x_init
    y = y_init
    vx = vx_init
    vy = vy_init
        
    for i in range(int(math.ceil(time_max/delta_t))):      
        x_next = x + vx*delta_t
        y_next = y + vy*delta_t
        r = math.sqrt(x**2+y**2)
        vx_next = vx + v_deriv(x, r)*delta_t
        vy_next = vy + v_deriv(y, r)*delta_t

        # update 
        x = x_next
        y = y_next
        vx = vx_next
        vy = vy_next        

        if i%10000 == 0:
            print(f'Iteration: {i}')
            buffer = buffer.append({'t': i*(delta_t/sec_in_year), 
                                    'x': (x/au), 
                                    'y': (y/au)}, ignore_index=True)

    return buffer

if __name__ == "__main__":
    orbital_period = 75
    sec_in_year = 365.25*24*60*60
    number_lap = 3

    delta_time = 60*2
    max_time = number_lap * orbital_period * sec_in_year

    dataframe = Explicit_Euler_Method(max_time, delta_time, 
                            x_0, y_0, 
                            vx_0, vy_0, 
                            sec_in_year)

    dataframe.to_csv(f'../data/ex1_dt_{delta_time}.csv', index=False)