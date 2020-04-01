''' Utility functions for all scripts. '''

import numpy as np

from config import E_0, v_0

def V(x):
    ''' Potential energy function. '''
    return -np.exp(-x**2) - 1.2*np.exp(-(x-2)**2)

def f(x):
    return V(x) - E_0

def f_deriv(x):
    ''' f(x) derivative '''
    return 2*x*(np.exp(-x**2)) + 2.4*(x-2)*np.exp(-(x-2)**2)

def f_double_deriv(x):
    ''' f(x) double derivative '''
    return -4*np.exp(-x**2)*x**2 + 2*np.exp(-x**2) - \
            1.2*(4*np.exp(-(x-2)**2)*(x-2)**2-2*np.exp(-(x-2)**2))

def V_deriv(x):
    return f_deriv(x)

def V_double_deriv(x):
    return f_double_deriv(x)

def calc_kinetic_energy(v_t, mass):
    ''' Calculate kinetic energy Ek = mv^2/2 using v(t). '''

    return [0.5*mass*item**2 for item in v_t]

def calc_potential_energy(x_t, V):
    ''' Calculate potential energy using x(t) and V(x). '''

    return [V(x) for x in x_t]