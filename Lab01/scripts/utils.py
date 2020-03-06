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