""" Try symbolic expression using sympy library. """

import numpy as np
from sympy import symbols, exp, diff
from sympy.utilities import lambdify

from config import E_0, v_0

# use symbolic expression
x = symbols('x')
expression = -exp(-x**2) - 1.2*exp(-(x-2)**2)

def V(var):
    ''' Potential energy function. '''
    return expression.subs(x, var)

def f(var):
    return V(var) - E_0

def f_deriv(var):
    ''' f(x) derivative '''
    print('Calculating ...')
    fun = lambdify(x, diff(expression, x))
    return fun(np.float64(var))

def f_second_deriv(var):
    ''' f(x) second derivative '''
    fun = lambdify(x, diff(expression, x, 2))
    return fun(var)

def V_deriv(var):
    return f_deriv(var)

def V_second_deriv(var):
    return f_second_deriv(var)