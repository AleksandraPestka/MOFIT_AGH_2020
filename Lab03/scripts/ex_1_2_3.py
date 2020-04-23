import numpy as np
import pandas as pd

def u0(x, t=0):
    return np.exp(-100*(x-0.5)**2)

def v0(x, t=0):
    return 0

def fill_acceleration(u, dx, N, v, beta):
    a = np.zeros(N, dtype='float32')

    for i in np.arange(0, N):
        a[i] = (u[(i+1+N)%N] + u[(i-1+N)%N] - 2*u[i])/dx**2 - 2*beta*v[i]
    return a

def Verlet_method(u, v, a, a_next, dt, dx, N, 
                  boundary_condition, beta, omega, x_force, time):
    '''Return new deviation and velocity from current values, 
    time step and acceleration using Verlet method.'''

    for i in np.arange(1, N-1):
        u[i] += dt*v[i] + 0.5*dt**2*a[i]

    if boundary_condition == 'stiff':
        # stiff problem
        u[0] = u[N-1] = 0

    elif boundary_condition == 'free':
        u[0] = u[1]
        u[N-1] = u[N-2]

    for i in np.arange(1, N-1):
        a_next[i] = (u[i-1] + u[i+1] - 2*u[i])/(dx**2) - 2*beta*v[i]
        if (i*dx) != x_force:
            v[i] = (v[i] + 0.5*dt*(a[i] + a_next[i]))/(1 + beta*dt)
        else:
            v[i] = (v[i] + 0.5*dt*(a[i] + a_next[i] + \
                    np.cos(time * omega) + np.cos((time + dt)*omega)))/(1 + beta*dt)
        a[i] = a_next[i]

    return u, v, a, a_next

if __name__ == '__main__':
    # constants
    N = 101         # no. of points
    dx = 0.01       # length of one piece of string
    dt = 0.005      # delta time
    t_max = 10
    boundary_condition = 'stiff'
    force = True
    beta = 1        # damping factor
    omega = np.pi/2 # force frequency 
    x_force = 0.5

    # initial conditions
    x_vec = np.arange(0, dx*N, step=dx)
    if not force:
        u = np.array([u0(item) for item in x_vec], dtype='float32')
    else:
        u = np.zeros(N, dtype='float32')
    
    v = np.array([v0(item) for item in x_vec], dtype='float32')

    if boundary_condition == 'stiff':
        # stiff problem
        u[0] = u[N-1] = 0

    elif boundary_condition == 'free':
        u[0] = u[1]
        u[N-1] = u[N-2]

    # init acceleration
    a = fill_acceleration(u, dx, N, v, beta)
    a_new = np.zeros(N, dtype='float32')

    with open('../data/ex3.csv', 'w') as tmp_file:
        for t in np.arange(0, t_max, dt):
        #for t in np.arange(0, 2*dt, dt):
            if t != 0:
                # update
                u, v, a, a_new = Verlet_method(u, v, a, a_new, dt, dx, N, 
                                                boundary_condition, beta, 
                                                omega, x_force, t)
        
            df_temp = pd.DataFrame(columns=['x', 't', 'u'])
            df_temp['x'] = x_vec
            df_temp['u'] = u
            df_temp['t'] = t

            df_temp.to_csv(tmp_file, 
                            mode='a', 
                            header=tmp_file.tell()==0, 
                            index=False)
            tmp_file.writelines('\n')