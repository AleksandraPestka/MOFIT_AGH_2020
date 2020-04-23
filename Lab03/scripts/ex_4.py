''' Script doesn't work properly. '''

import numpy as np
import pandas as pd
from tqdm import tqdm

from ex_1_2_3 import fill_acceleration, Verlet_method

def calc_energy(E, u, v, dx, N):
    for i in np.arange(1, N-1):
        E += 0.5*(v[i]**2 + ((u[i+1] - u[i])/dx)**2)
    return E

if __name__ == '__main__':
    # constants
    N = 101         # no. of points
    dx = 0.01       # length of one piece of string
    dt = 0.005      # delta time
    (t1, t2) = (16, 20) # start and stop time of steady-state 
    boundary_condition = 'stiff'
    beta = 1        # damping factor
    x_force = 0.5   # force point

    # initial conditions
    x_vec = np.arange(0, dx*N, step=dx)
    u = np.zeros(N, dtype='float32')
    v = np.zeros(N, dtype='float32')

    if boundary_condition == 'stiff':
        # stiff problem
        u[0] = u[N-1] = 0

    elif boundary_condition == 'free':
        u[0] = u[1]
        u[N-1] = u[N-2]

    # init acceleration
    a = fill_acceleration(u, dx, N, v, beta)
    a_new = np.zeros(N, dtype='float32')

    # frequency 
    omega_vec = np.arange(0, 10*np.pi, step=0.01)

    with open('../data/ex4.csv', 'w') as tmp_file:
        # reset average energy
        E_avg = 0

        for omega in tqdm(omega_vec):            
            for t in np.arange(dt, t2, step=dt):
                # reset energy 
                E = 0
            
                # update
                u, v, a, a_new = Verlet_method(u, v, a, a_new, dt, dx, N, 
                                                    boundary_condition, beta, 
                                                    omega, x_force, t)
                # calculate energy
                E = calc_energy(E, u, v, dx, N)
                
                if t > t1:
                    E_avg += E
            
            # save omega and average energy to file
            tmp_file.write(f"{omega/np.pi}, {E_avg/4}\n")
